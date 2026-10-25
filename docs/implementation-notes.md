# Implementation notes

This file records how each part of the functional spec is realised in code. It focuses on the
**fallback heuristics**: the places where the reference behaviour was not recovered and something
else is used instead.

## Where things live

| Concern | Module |
|---|---|
| Recovered rules (pure, no I/O): expected points, outcome buckets, precision, classification tree, mate rules, CAPS2, tallies | `backend/crates/review-core/src/*` |
| Engine-facing score model (White-relative `Eval`, mover-relative reference `Value`) | `review-core/src/value.rs` |
| Facts computed from board + engine lines (material walks, sacrifices, free pieces, recaptures) | `review-server/src/analysis/detectors.rs` |
| Orchestration: searches, perspective conversion, facts → `MoveFacts`, CAPS2, summary | `review-server/src/analysis/mod.rs` |
| Generated explanations (facts for the details drawer) | `review-server/src/analysis/explain.rs` |
| Coach: position facts, tag detectors, circumstances, prioritiser, realiser, English text | `review-server/src/coach/` (`text/en.toml`) |
| Coach fact checker and its CLI | `review-server/src/coach/verify.rs`, `examples/coach_verify.rs` |
| Phase heuristic, material values, FEN helpers | `review-server/src/board.rs` |

Every recovered constant is a default in `ReviewConfig` and is pinned by a unit test in `review-core`.
`GET /api/config/defaults` returns them, and `POST /api/reviews` accepts an override for
experiments.

## Search model

- **One search per position.** Each position before a move gets one MultiPV search. The final position
  is searched as well, unless it is checkmate, stalemate or a drawn final position.
- **Best move.** The best move's resulting score is line 1 of the search *before* the move. A mate
  distance is reduced by one move when the mover is the one mating (`eval_after_first_move`).
- **Played move.** If the played move appears among the MultiPV lines, the score of that line is used.
  This keeps both scores from one search, as the reference compares sibling nodes. Otherwise the
  played move is scored from the next position's search. If the played move is line 1, its value
  equals the best value by construction, which gives **Best**.
  - *Confirmed by calibration data:* scoring a played move outside the lines with a search of the
    same position restricted to it (`go … searchmoves`) matched Chess.com worse (26 labels worse,
    12 better on the tuning set). The restricted search rates the move higher than the next
    position's own search, which finds the refutation at full depth. `searchmoves` is supported by
    the engine layer but not used by the pipeline.
- **Determinism.** Every search starts with `ucinewgame` and `setoption name Clear Hash`, and engines
  run with one thread, so a search depends only on its request. Without this, hash tables carried over
  between searches in the engine pool changed about 14% of labels between two runs of the same games.
- **Repetition.** Threefold repetition is tracked along the game (EPD counts). A position drawn by
  rule has EP 0.5, matching the reference `Position::draw()`.
- **Threat search (coach only).** A null-move search (`coach.threat_search_depth`, default depth 10,
  MultiPV 1) runs on positions with the side to move flipped and the en passant square cleared
  (`board::null_move`). It is skipped when the side to move is in check or the flipped position has no
  legal move. One search per position serves two moves: the position after move *i* with its mover to
  move again is N for move *i* (THREATENS), and the same position is N_prev for move *i + 1*
  (PREVENTS). Only positions next to a move that is neither Book nor Forced are searched. The
  searches share the engine pool and the progress count with the main searches, and never change a
  classification. A failed threat search is logged and skipped, not fatal. Depth 0 turns them off.
  - **After the best move** (`coach.best_threat_search`, on): for every such move that is not the
    engine's best move B, one more search of the same kind runs on the position after B with B's
    mover to move again (N_B, what B threatens). These run after the main searches, outside the
    progress count.

## Fallback heuristics

All horizons and thresholds are in `ReviewConfig`.

### Material along a line (`walk_line`)

- Plays the engine PV from the position before the move, for `material_horizon_plies` (6) plies.
- It then **extends while captures, promotions or checks continue**, up to 6 more plies, so material
  is measured at a quiet point. Without this, a horizon that cut an exchange in half graded near-best
  moves as Mistakes. See `docs/parity.md` for the Opera Game case.
- **Reported quantities:** start, end, min and max balance, what the first move captured, and the
  *gain ply*: the first settled ply (one not followed by a capture) from which the balance stays at
  its final level. The coach looks for the tactic behind a gain at or before it.

### Static exchange evaluation (`analysis/see.rs`)

- The standard swap list on one square: each side captures with its least valuable piece and may stop
  when going on loses material. Attackers are recomputed as pieces leave the board, so x-ray
  attackers join in.
- Pieces pinned to their king capture only along the pin line, a king never captures a defended
  piece, and promotions during the exchange are ignored. The king is valued at 99999, as in the
  reference sacrifice gates.
- `capture_gain` also requires a legal first capture, so a piece the opponent cannot take (for
  example because they are in check) is not counted as threatened.

### Facts derived from the walks

| Reference fact | Fallback |
|---|---|
| `material_lost` | `max(0, start − end)` of the played line. It is reported as unknown when the played move's score is a forced mate, because the mate rules decide those positions and material is meaningless there. |
| `is_losing_material_or_getting_mated` | material lost ≥ `blunder_material_threshold_cp` (100), or the played score is a mate against the mover while the best move's is not (recovered: being mated counts unless the best alternative is mated too) |
| `loses_more_material_than_best` | the played line ends at least `forgiving_material_lost_cp` (200) below the best line. The margin was added after parity runs: in lost positions every line sheds material, and tiny PV differences between runs flipped the verdict. |
| Guard A ("drops material") | the move is not the best move, it loses ≥ 100, and it loses more than the best line gains |
| Sacrifice (`is_sacrifice`) | static test, not a line walk: see Brilliant below |

The line-based material facts were kept after calibration. Replacing them with the material the
opponent can win immediately (static exchange) lowered agreement with Chess.com in two variants: it
softened Blunders that lose material through a later tactic, such as a fork. See
`docs/calibration/log.md`.

### Event detectors

- **Brilliant** follows Chess.com's own rule, recovered from libcee 4.10.15 (circumstance 13; details
  and results in `docs/calibration/great-blunder-analysis.md` §8). It requires all of
  (`brilliant.*` in the config):
  - the move is Best, or graded Excellent or Good while the best move does not force mate
    (`near_best`);
  - the mover's EP after the move is at least `min_ep_after` (0.47); when answering check, the
    second line is not mated; the move neither threatens to promote nor takes a pawn about to;
  - a **sacrifice** (`detectors::sacrifice`): a piece the opponent wins at least `min_threat_cp`
    (200, the reference's "strongly SEE-threatened") by exchange on. The piece is
    - the moved piece, which had a safe square (a square it attacks where its own exchange does not
      lose, `reference_safe_squares`), loses material in its own exchange (`moved_net_loss`), is not
      a doomed or mutual-threat piece, and does not save more than one other strongly threatened
      piece (`reference_moved`);
    - or a piece left standing (`reference_standing`, after `ignored_threats`,
      `is_indirect_sacrifice` and `is_sacrifice_of_not_moved`): the single most valuable piece
      strongly threatened before and after the move, unless an earlier move of the same side already
      ignored it while it stayed threatened (`ignored_threats`); or the most valuable piece newly
      strongly threatened (`left_en_prise`). Either way not when the move gives or answers check or
      promotes, saves a piece worth as much, captures plus newly threatens at least what is lost, or
      hits back at a bigger piece; an ignored piece must not be trapped or pinned to its king;
      and no attacker of the piece may be pinned (`ref_pinned_attacker`) or overloaded, i.e. its only
      capturer also guards another piece (`ref_overloaded`), nor may the move take away the
      opponent's safe promotion squares (`ref_promotion`);
    - in high-rated games (max Elo ≥ `great_find.high_rated_min`) the moved piece must be worth more
      than what the move captured plus the best piece an uncovered slider now strongly threatens (no
      disguised trade), have a capturer that is not relatively pinned, and not be a deflection whose
      single capturer is overloaded (`ref_deflection`). Newer players get no such test;
  - the recovered gates: not when the mover is already ahead by the piece's value against an
    opponent whose EP before the move (at rating 2000) is below `opponent_lost_ep` (0.10); in the
    endgame the position is critical or the line wins at least `endgame_min_gain_cp` (200).
- **Great Find** (`facts::judge_move`, rebuilt 2026-10-23 on the recovered structure;
  `docs/calibration/great-blunder-analysis.md` §2.1 and §5) is a candidate with a tag.
  - `high_rated` is `max(Elo) ≥ great_find.high_rated_min` (1000). It picks a branch, and is not a
    gate: below it Great is more generous.
  - **Candidate:** all of:
    - precision Best or Excellent;
    - not easy to find. Castling is never easy. Easy moves are:
      - a promotion that cannot be won back by exchange;
      - a threatened piece (not a pawn) going to its only safe square;
      - only when high-rated: a best-move recapture, or a free capture (static exchange, not a
        recapture);
      - a shallow search's own choice (`easy_search_depth`, off).
    - only when high-rated: not a recapture of equal or greater value with no capture in reply, not
      a mate on the board, and not taking the attacker in an even exchange;
    - if the mover's previous move carried a tag, this move is neither a capture nor a passed-pawn
      push.
  - **Tags** (any one):
    - **key moments.** They need all of:
      - the opponent's previous move graded Mistake or Blunder, a missed mate, or ungraded;
      - EP after the move ≥ `key_moment_min_ep` (0.47);
      - the mover not completely winning after their own previous move;
      - not a recapture.

      Then the move does one of these:
      - forces mate in ≤ `forces_mate_max_moves` (4), with the mover's score after their previous
        move ≤ `forces_mate_max_previous_cp` (1499);
      - gains more than `wins_material_min_gain_cp` (100) along the line walk, is not a free capture,
        and the mover's previous move's line did not already win material;
      - not high-rated only: takes a free piece.
    - **critical.** The best move, with all of:
      - EP(best) ≥ `critical_min_best_ep` (0.35);
      - the second line's EP < `critical_max_alternative_ep` (0.80), and at least
        `critical_min_alternative_loss` (0.10) below;
      - the second line is not an interposition with a piece that is lost there;
      - the move is not a best-move recapture.
    - **winning.** The opponent's outcome before the mover's previous move was Equal or better; the
      mover's now is Winning or better.
    - **comeback.** The opponent's outcome then was Winning or better; the mover's now is Equal or
      Better.
  - **Deliberate departures from the decompile**, each because the 142 calibration games disagreed:
    - the reference asks an obvious recapture to land safely. Here any best-move recapture counts,
      because no recapture was Great whatever our exchange test said: 0 of 25;
    - the only-safe-square exclusion needs a threatened non-pawn piece. A pawn nearly always has one
      legal move, and the wider rule removed more Great moves than wrong ones.
  - **Previous moves.** The review fills these from the moves before (`PreviousMoves`). A sideline
    knows the game's moves before its branch point. For its own earlier moves it reads only the
    loss the browser sends: the opponent counts as erring above the Inaccuracy bound, and the
    mover's outcome and wins-material history are unknown.
  - **Tuning.** The recovered constants are kept. `critical_min_alternative_loss` 0.09 gave precision
    0.79 and recall 0.78, but it was not adopted: it was measured on all 142 games, holdout
    included.
- **Tricky** is not implemented (it needs ML models, and the reference client drops it).

### Miss subtypes

These are only consulted when precision is Mistake or Blunder, under the recovered A/B guards and order,
and never for a move that walks into a forced mate. In the calibration games, 1 of Chess.com's 319
Misses allows mate, against 34 of its 228 Blunders.

| Subtype | Fallback test |
|---|---|
| free piece | the best move's first capture is worth ≥ 300 and is not won back, after an opponent's move that lost ≥ 0.05 EP (`miss.tactic_min_opponent_ep_lost`) |
| tactic | the best line gains ≥ 200, after an opponent's move that lost ≥ 0.05 EP |
| win | best outcome bucket ≥ Winning and played ≤ Equal |
| comeback | mover ≤ Worse before the move, best ≥ Equal, played ≤ Worse |
| brilliant | the best move is a sacrifice (the Brilliant test above) and EP(best) ≥ 0.20 (`miss.brilliant_min_best_ep`) |
| opportunity | the opponent's previous move lost ≥ 0.10 EP |

### Other fallbacks

- **Phases.**
  - Endgame when there are ≤ 6 non-pawn, non-king pieces.
  - Middlegame when there are ≤ 10 such pieces, either side has fewer than 4 pieces on its back rank,
    or from ply 40.
  - Phases never go backwards.
- **Key moments.**
  - The recovered candidate filter: precision Best or Excellent, not forced, not book, mover not
    completely winning, not a recapture.
  - Plus a trigger: the line wins ≥ 200 material, the move keeps or delivers mate, it is a promotion,
    or it takes a free piece.
  - Critical moments are Blunder, Mistake, Miss, Brilliant and Great Find.
- **Book.** A move is Book when the position after it appears in the Lichess openings data (any
  position along a named line), even after earlier non-book moves: Chess.com marks moves that
  transpose back into the book as Book (calibration: +0.5 points on tuning, +0.7 on holdout).
  `book_requires_unbroken` restores the stricter "every earlier move was Book" rule. Chess.com's
  book is also larger than this one: in several games it continues 3–8 plies longer.
- **Explanations.** Only computed facts are stated: mate distance, the best move, material along the
  engine line, and expected score. They are labelled "generated" in the UI.

## Coach

`review-server/src/coach/` implements phases 1 and 2 of [`coach-analysis.md`](coach-analysis.md)
§6–7. It explains Inaccuracies, Mistakes, Blunders and Misses by naming a tactic and showing the line
(phase 1), and Brilliant, Great Find, Best, Excellent and Good moves by what they do, threaten or stop
(phase 2). Phase 2b ([`coach-gap-analysis.md`](coach-gap-analysis.md) §4.2) speaks the best move like a
played good move and adds trade, check, tempo, sacrifice, only-move and slide tags; it is described in
"Coach phase 2b" below, which supersedes the bullets here where they differ. It is pure: it reads
the engine lines the review already has, including the null-move threat searches (see "Search
model"), and makes no engine calls. The output is `PlyReview.coach`;
`explanation` stays for the details drawer. A Forced move gets one sentence ("Kh2 was the only legal
move."); a Book move gets a note only for a development idea (phase 4).

- **Nodes.** P is the played move, with its own line (the MultiPV line that starts with it, or P
  followed by the next position's line 1). R is the opponent's best reply: line 1 of the next position
  and its PV. B is the best alternative: line 1 of this position. B is skipped when it is P. N is the
  null-move threat search after P (the mover to move again), and N_prev the one before P (the opponent
  to move). Their lines start from the flipped positions, so their show-lines carry that FEN.
- **Facts** (`facts.rs`): attackers, SEE (`analysis/see.rs`), hanging pieces, absolute and relative
  pins, x-rays, pinned guards, and trapped pieces. A piece is trapped when the opponent wins it where
  it stands and on every square it can reach, unless it captures something at least as valuable.
- **Tags** (`detect/`): our own `Tag` enum, whose declaration order is the priority order. Groups 1–7
  of §6.4 are written from chess semantics and the lichess tagger *description*
  (`coach-research-notes.md` §2.1), not from its code. Choices that differ from that description:
  - a fork target is worth more than the forker (the king counts), or is undefended and cannot take
    the forker; pawns count only when undefended;
  - a line piece also forks through a friendly piece in front of it (a battery) when the piece
    behind becomes newly lost (6...Nf6 7.Qb3 hits b7, and f7 through the c4 bishop);
  - `FreePiece` counts only on the first move of a line (later captures collect what a tactic won),
    never on a recapture (taking back on the square the opponent just captured on; what the exchange
    nets is reported as the line's gain, e.g. 13.Rxd7 Nxd7 "wins the exchange", not "wins White's
    rook"), and gives way to `ExploitsPin` when the only defender is pinned to its king;
  - the bad-move tags (`HangsPiece`, `IgnoresThreat`, ...) also need R's line to take the piece in
    its first two moves, so a poisoned "hanging" piece is not called hanging.
- **Defence tags** (`detect/defence.rs`, group 8, after the bad-move tags): `DefendsPiece` (a
  threatened piece stays and is safe because the moved piece guards it or blocks the attacker),
  `EscapesThreat` (the threatened moved piece is safe on its new square; captures are left to the
  capture tags, so a recapture is not an escape), `BlocksCheck` (a piece other than the king steps
  between a single line checker and the king) and `CounterThreat` (a threatened piece is left, and the
  moved piece attacks a new target it can win for at least as much). "Threatened" is SEE before the
  move; when N_prev is known, its line must also take that piece in its first two moves.
- **Circumstances** (`circ.rs`):
  - BASE: for a bad move, the bad-move tags on P. For a good move, the event of P's own line (as for
    PERMITS below: a mate, the tactic behind its gain, or a tactic of P itself) and the defence tags.
  - PERMITS / MISSES: R's or B's line. If its first mover mates, the event is a mate tag:
    `BackRankMate` or `Checkmate` when the first move mates; a longer mate is `ForcedMate`, whatever
    the final pattern (a pattern is named only on the mating move). If the line wins at least a pawn,
    the highest-priority tactic among that side's moves up to the gain ply is chosen: WINS_MATERIAL
    when it is the first move, LEADS_TO when it comes later. In R's line (PERMITS) a tactic is named
    only on R's first move, or on its second after a quiet check (a check that captures nothing);
    further down the gain is `MaterialGain`, "allows … to win material". This follows Chess.com,
    which says LosesMaterial for most deeper tactics (coach run `coach-main-e4ead28`).
    If no tactic is found, the fallback is `MaterialGain`. A line that wins nothing reports a tactic of
    its first move, if any. The gain is placed on the winning side's last capture before the material
    settles, never on the other side's move after it (10...cxb5 Bxb5+ "cxb5 wins a pawn").
  - THREATENS: N's line, read the same way, kept only when it is a threat: its first move mates or
    carries out the tactic, and the material falls by the mover's next move (an idea that needs a
    quiet move first is a plan, not a threat). It is also dropped
    when R's first move takes the moved piece (a trade, or a piece given up: 4...Bxf3 "threatens"
    nothing that 5.Qxf3 does not answer), and when the material threat is on a piece the mover could
    already win before P.
  - PREVENTS: N_prev's line, read the same way, when it is a threat (as above) and is gone after P: R
    no longer mates, or R wins less than the threat and does not take on the threatened square.
  - Gains are counted from **before** the move that led to the line, when that move captured. So a
    recapture is not a gain: after 4...Bxf3, 5.Qxf3 wins nothing. Null-move lines have no such move.
  - MISSES_SAME: B takes, for free, the piece on the square the opponent's last move went to.
  - A capture that R takes back, where R's piece cannot be won in turn, gave the piece away: R's event
    is `FreePiece`, although it is a recapture (7...Nxd5 8.Bxd5 "wins Black's knight on d5").
  - R's first move takes a free piece only if R keeps it and the line wins about that much. When the
    line wins more than the piece plus a pawn (or the mover takes back on the square anyway), R's
    event is `MaterialGain` about the same piece ("h6 allows Bxa5, which wins …"). A piece
    the mover can take back with profit is `WinsTrade` already (phase 2b, below).
- **Prioritiser** (`priority.rs`, §6.5):
  - The Permits block: mate; when the BASE tag is `IgnoresThreat` or `BadTrade`, R's first move that
    takes the piece (a free piece, or `MaterialGain` about that piece); a bad BASE tag (unless R's
    tactic wins 200 cp more than it puts at stake, not counting a tactic that wins the BASE tag's own
    piece); a named tactic with a gain; a free piece; `MaterialGain`; any PERMITS event. An
    `IgnoresThreat` or `BadTrade` that is kept (R takes the piece later in its line) is worded as
    losing material.
  - The Misses block: mate; MISSES_SAME; a named tactic with a gain; a free piece; `MaterialGain`; any
    MISSES event.
  - A Miss runs the Misses block first, every other bad move the Permits block first. When the main
    event comes from the Permits side, the Misses block gives the best-move sentence. Without one, the
    sentence is a plain "Better was …". When neither block has an event, a THREATENS event is said,
    followed by "Better was …".
  - A non-Miss explained only by B is phrased as "Better was …", never "missed".
  - A good move: a mate on its own line; a tactic (or free piece) that wins material there;
    THREATENS a mate; PREVENTS a mate; a BASE tag without a gain (a tactic of P, or a defence tag);
    any THREATENS; any PREVENTS; `MaterialGain` on its own line. Good moves get no "better" sentence.
- **Realiser** (`realise.rs`, `text/en.toml`):
  - A sentence is a frame (by circumstance chain and style) with the tag's phrase spliced in.
  - Styles `you`, `opponent` and `neutral`. The review request's `player_side` picks `you` for the
    player's moves and `opponent` for the other side's; without it the style is `neutral` ("White",
    "Black's knight"). The frontend asks before the review ("This is me") and remembers the username.
  - Placeholders: `{move} {reply} {line} {best} {mover} {piece} {piece_role} {square} {targets}
    {gain} {n}`.
  - Fragments for moves and pieces carry the event's arrows and squares. Moves keep their SAN
    capitalisation.
  - The wording varies by ply (the seed).
  - Lead-in lines longer than four plies are not spelled out in the sentence.
  - Good moves use the `good*`, `threatens*` and `prevents*` frames. Brilliant and Great Find moves use
    `brilliant_<frame>` / `great_find_<frame>` when the corpus has one; otherwise their own sentence
    (`brilliant`, `great_find`) comes first, and it is said alone when there is no event.
  - Show-lines replay the event's line through the gain (or the mate), plus two plies, with one
    narration per move: the move's best tag, or a capture, recapture, check, forced or quiet move.
    THREATENS and PREVENTS lines are labelled "Show the threat" and start from the null-move position.
- **Text.** Every sentence in `en.toml` was written for this project. None of it is the reference
  app's text.
- **Frontend.** `Coach.tsx` shows the sentences, with the named moves and pieces in bold. For a bad
  move they replace the generic advice; a good move keeps its one-line advice after them. The board
  draws the arrows of the main sentence's first marked fragment. Phase 3 makes it interactive (see
  "Coach UI (phase 3)").
- **Tests.** `tests/coach_detect.rs` has hand-built positions per tag, including the defence tags.
  `tests/coach_note.rs` checks circumstances (THREATENS and PREVENTS included), the bad-move and
  good-move priority, Brilliant and Great Find wording, styles and wording. `tests/coach_pipeline.rs`
  runs the fake and scripted engines, null-move searches included (scripted by FEN and depth).
  `cargo run --release --example coach_report -- game.pgn [depth] [threat depth]` (with
  `STOCKFISH_PATH`) prints the coach's notes for a real game and the review time.
- **Sample game** (Morphy, Paris 1858; Stockfish 18, depth 18, threat search depth 10). 26 of the 33
  moves are reviewed (the rest are Book). 21 get a sentence with geometry and a line (a selection
  below); 4...Bxf3, 9...b5, 11.Bxb5+, 12...Rd8 and 14...Qe6 get none.

  | Move | Class | Coach sentence |
  |---|---|---|
  | 5.Qxf3 | Best | Qxf3 stops Bxd1, which wins White's queen on d1. |
  | 6.Bc4 | Best | Bc4 threatens Qxf7#, which is checkmate. |
  | 6...Nf6 | Mistake | After Nf6, Qb3 forks Black's pawns on b7 and f7, winning a pawn. |
  | 7.Qb3 | Best | Qb3 forks Black's pawns on b7 and f7, winning a pawn. |
  | 7...Qe7 | Best | Qe7 defends against Bxf7+, which starts a forced mate in 2. |
  | 8.Nc3 | Good | Nc3 defends White's pawn on e4. |
  | 8...c6 | Best | c6 defends against Qxb7, which wins Black's pawn on b7. |
  | 9.Bg5 | Best | Bg5 pins Black's knight on f6 to Black's queen on e7, winning a pawn. |
  | 10.Nxb5 | Brilliant | Nxb5 is a sacrifice that works: it stops bxc4, which wins White's bishop on c4. |
  | 11...Nbd7 | Best | Nbd7 blocks the check. |
  | 13.Rxd7 | Best | After Rxd7 Nxd7, Bxe7 takes Black's queen on e7, which was guarding Black's rook on d8, winning material worth about 4 pawns. |
  | 13...Rxd7 | Mistake | After Rxd7, Rd1 makes use of the pin on Black's rook on d7. |
  | 15...Nxd7 | Mistake | After Nxd7, Qb8+ starts a back-rank mate in 2. |
  | 16.Qb8+ | Best | Qb8+ starts a back-rank mate in 2. |

  - Stockfish 18 rates the moves differently from 16.1 (used for the phase 1 table): 6.Bc4 is Best,
    9...b5 an Inaccuracy, 10...cxb5 and 14...Qe6 good moves. 6.Bc4's missing explanation in phase 1
    is now its threat.
  - 4...Bxf3 and 9...b5 are bad moves with nothing to name: their engine lines win no material within
    the horizon, and their threats (Bxd1, bxc4) are answered by taking the moved piece, so THREATENS
    is dropped. They need positional tags (phase 4).
  - 5.Qxf3 is really a recapture; it is said as the threat it stops, because there is no recapture
    tag yet. (Phase 2b adds it: "Qxf3 takes back on f3.")
- **Cost of the threat search** (same game; the machine was shared, so wall-clock times varied from
  30 to 56 s for one setting and do not resolve the difference). The review makes 33 main searches
  (depth 18, MultiPV 3) and 23 threat searches (depth 10, MultiPV 1). Measured alone (main search at
  depth 1, three runs each), the threat searches add about 0.9 s of engine CPU at depth 10 and 1.6 s
  at depth 12, against 100–180 s of CPU for the depth-18 review: about 1%. That is far below the 25–35%
  estimated in `coach-analysis.md` §6.2, because a depth-10 MultiPV-1 search is much cheaper than a
  depth-18 MultiPV-3 one.

## Coach phase 2b

Phase 2b of [`coach-gap-analysis.md`](coach-gap-analysis.md) §4.2 (gaps B1, B4, B5, B9, B10, G1, G3–G6).
It is built on the quick fixes (§4.1). Measured on all 142 calibration games
([`calibration/coach-log.md`](calibration/coach-log.md), run `coach-phase2b`): bad-move exact 35.4%
(quick fixes 29.0%), good-move exact 44.3% (23.4%), best-move sentence exact 37.6% (12.1%).

- **The best move, said like a good move** (`circ::best_events`). B goes through the good-move
  pipeline, and every event is put under MISSES:
  - its own line (as before: a mate, the tactic behind its gain, MISSES_SAME);
  - what it does by itself (`detect::good_tags`: trades, defence, tempo), on B's line;
  - what it threatens: N_B, the null-move search after B (see "Search model"), read like THREATENS,
    chain `[misses, threatens, …]`;
  - which of the opponent's threats it stops: N_prev against B's own continuation, chain
    `[misses, prevents, …]`;
  - a sacrifice (`Sacrifice` / `OffersPiece`) when B is one by `static_sacrifice`, unless B answers a
    check (then the answer is the point);
  - `OnlyMove` when every other engine line loses more than a Good move may (EP gap to line 2 above
    `precision_thresholds[1]`, from the MultiPV lines the review already has).
- **The Misses block** follows the good-move order: mate; MISSES_SAME; sacrifice; a named tactic
  with a gain; a piece taken (`FreePiece`, `WinsTrade`); a threatened mate; a stopped mate; a trade,
  defence or tempo tag; a tactic that wins nothing; a threat; a stopped threat; `MaterialGain`;
  `OnlyMove`. A bad move's main event: Permits block, else Misses block (the other way round for a
  Miss), else the played move's threat, else "the only good move", else the evaluation slide. The best
  move is said after every main event that is not already about it.
- **Frames.** `best_threatens` ("Better was Rd2, threatening Rd8#, which mates on the back rank."),
  `best_prevents`, `best_sacrifice`, `best_only` and their `misses_*` forms for a Miss. A best-move idea
  on a null-move line is shown on B's own line ("Show the best line").
- **Trades** (`detect/trade.rs`, group 8, and `WinsTrade` / `LosesTrade`):
  - `Recapture`: takes back on the square the opponent just captured on, ending the exchange without
    losing it. When B's or the played move's line settles a gain on that move, it carries it ("takes
    back on d7, winning the exchange").
  - `EqualTrade`: a capture that the opponent takes back with profit, the exchange within 100 cp of
    even. A recapture that the opponent can take back again evenly is an `EqualTrade` too: the trade
    goes on. (A first run on 60 games had Chess.com say EqualTrade 14 times where we said
    `recapture`; this split targets them.)
  - `WinsTrade`: split from `FreePiece`. A capture the opponent can take back with profit that still
    nets a pawn or more (a knight takes a rook guarded by a pawn). It sits next to `FreePiece` in the
    tag order because it wins material on lines too (PERMITS, MISSES, own line), as Chess.com's
    PileTrade comes before its equal-trade and recapture tags.
  - `LosesTrade` (a bad-move base): a capture that R takes back on the same square and comes out at
    least a pawn ahead (line-based), where the static `BadTrade` did not fire.
  - `OffersTrade` (group 10): a quiet move that faces an opponent piece of the same value, both sides
    guarded, nothing won by taking first.
- **Check** (`detect/defence.rs`): `EvadesCheck` (the king steps out of check, or a piece takes the only
  checker) next to `BlocksCheck`. Both now come before `DefendsPiece`, as in Chess.com's order.
- **Tempo** (`detect/tempo.rs`): `Kicks` (a pawn) and `GainsTempo` (another piece) newly attack exactly
  one knight, bishop, rook or queen from a safe square, and that piece has a safe square
  (`facts::has_safe_square`).
- **THREATENS tightened.** A material threat on one piece (`FreePiece`, `WinsTrade`, `MaterialGain`)
  whose target can simply move to a safe square is no longer a threat; it is the tempo tag above.
  Mates and double attacks stay threats.
- **Small events.** `Slide` for an Inaccuracy whose expected outcome drops a step (losing, worse, equal,
  better, winning; the extreme buckets fold in) and that has nothing else to say ("Ke8 lets Black's
  position slide from equal to worse."). `Sacrifice` / `OffersPiece` for Brilliant moves from the
  static sacrifice square: said first, then what it leads to in a second sentence
  (`Selection::follow`).
- **Priority for good moves**: own mate; sacrifice; own tactic with a gain; threatened mate; stopped
  mate; trade, defence or tempo tag; a tactic that wins nothing; any threat; any stopped threat;
  `MaterialGain`; `OnlyMove`. Trades and defences now come before tactics that win nothing, so a
  recapture is said as a recapture rather than "removes the defender" or "stops … winning a piece".
- **Frontend.** `lib/tags.ts` names every new tag for hints and takeaways. Trade, defence and tempo
  tags are `routine`: takeaways do not praise them. The retry hint prefers the best-move event a
  sentence says.
- **Tests.** Per-tag positions in `tests/coach_detect.rs` (trades, check, tempo), notes in
  `tests/coach_note.rs` (best move defends, threatens mate, only move, slide, recapture, check,
  sacrifices), slot order in `priority.rs`, and the extra search count in `tests/coach_pipeline.rs`.
- **Sample game** (same setting as above), the sentences that changed:

  | Move | Class | Coach sentence |
  |---|---|---|
  | 5.Qxf3 | Best | Qxf3 takes back on f3. |
  | 6...Nf6 | Mistake | After Nf6 Qb3 Bc5, Bxf7+ wins a pawn. Qf6 was better: it stops Qxf7#, which is checkmate. |
  | 10.Nxb5 | Brilliant | Nxb5 is a sacrifice: it gives up White's knight on b5, and that pays off. Nxb5 stops bxc4, which wins the trade on c4, winning two pawns. |
  | 11.Bxb5+ | Best | Bxb5+ takes back on b5. |
  | 13...Rxd7 | Mistake | After Rxd7, Rd1 makes use of the pin on Black's rook on d7. Nxd7 was better: it takes back on d7. |
  | 14...Qe6 | Excellent | Qe6 offers to trade Black's queen on e6 for White's queen on b3. |
  | 15.Bxd7+ | Best | Bxd7+ wins the trade on d7, winning material worth about 3 pawns. |
  | 15...Nxd7 | Mistake | After Nxd7, Qb8+ starts a forced mate in 2. Qxd7 was better: it gets out of the check from White's bishop on d7. |

  4...Bxf3, 9...b5 and 12...Rd8 still get no sentence (positional; Phase 4).
- **Cost.** The extra searches are one depth-10 MultiPV-1 search per coached move that is not the best
  move. On the sample game (main searches at depth 1 so the threat searches dominate, three runs, one
  engine) they add about 0.3 s of engine CPU to the 1.2 s of the other threat searches; the depth-18
  review takes 100–180 s of CPU, so the extra search costs about 0.2–0.3% of review time.
  The sample game plays the best move often; over the 142 calibration games the search ran for 4,735
  of 7,668 coached moves, about 33 per game. At the same cost per search (about 0.04 s) that is
  roughly 1.4 s of CPU per game against 190–330 s for a game of average length: about 0.5% of review
  time. (The calibration run's wall-clock time shared the machine with another run and does not
  resolve it.)

## Coach phase 4

Phase 4 of [`coach-analysis.md`](coach-analysis.md) (§6.4 group 9, §6.7, §7 row 4), scoped in
[`coach-gap-analysis.md`](coach-gap-analysis.md) §4.3 (gaps B6, G2, G7 and book moves): positional
tags, rating gates and an optional human-move model. Measured on all 142 calibration games
([`calibration/coach-log.md`](calibration/coach-log.md) "Results: Phase 4", run `coach-phase4`):
good-move exact 58.3% (44.4% before), bad-move exact 39.2% (36.0%), opening-phase bad moves 34.4%
(27.6%), best-move sentence 46.0% (37.6%), Blunders 138 of 228 (137).

- **Positional ideas** (group 13, `detect/develop.rs`, `activity.rs`, `structure.rs`), written from
  chess semantics; the pawn-structure helpers (doubled, isolated, passed, backward, open files,
  mobility) are in `facts.rs`. Home squares are those of standard chess, and a piece on its home square
  counts as undeveloped. In priority order:
  - `ForcesDoubledPawns`, `ForcesIsolatedPawn`: a capture that the next move of the line takes back
    with a pawn, leaving the opponent doubled pawns or a new isolated pawn. Doubled pawns are said
    before trades (Chess.com says "forces > DoublesPawns" where we said `equal_trade`); an isolated
    pawn after them (a first run had Chess.com say EqualTrade 12 times and the isolated pawn 6).
  - Centre: `StrikesAtCenter` (a pawn hits an opponent pawn on d4/e4/d5/e5, locked or not: 3.d4
    against e5), `CentralBreak` (after the opening, a pawn hits a locked pawn on the c- or f-file; a
    first run that made locked centre pawns breaks matched Chess.com 0 of 10 times), `PutsPawnInCenter` (a pawn reaches a centre square in the opening without hitting a
    pawn), `AttacksPawnChain` (a pawn hits a pawn that guards or is guarded by another pawn),
    `PreparesCentralPush` (in the opening, a pawn off the d- to f-files guards the empty centre square
    a d- or e-pawn of ours can advance to, where no pawn guarded it).
  - Activity: `RookOnSeventh` (with opponent pawns there or its king on the back rank), `Outpost` (a
    knight or bishop on ranks 4–6, guarded by a pawn, no opponent pawn on the next files ahead of it),
    `TakesOpenFile` (a rook, also a castling rook, onto a file with no pawns), `Battery` (two line pieces
    one behind the other on a line both move along, the front one bearing on opponent pieces or the
    king's squares; doubled rooks on a file free of our pawns count), `CentralizesKnight` (from outside
    c3–f6 into it), `MovesToActiveSquare` / `BishopGainsScope` (a piece that already stood somewhere
    gains at least 3 squares of mobility and ends with at least 5 for a knight, 7 for a bishop or rook,
    12 for the queen).
  - Development: `CastlesSameSide` / `CastlesOppositeSide` (by the other king: on its back rank, on
    the g/h or a–c files, no castling rights left), else `CastlesKingside` / `CastlesQueenside`;
    `ConnectsRooks` (the moved piece stood between the two back-rank rooks); `Fianchetto`;
    `PreparesToCastleKingside` / `Queenside` (the move empties the castling path while the right
    remains); `DevelopsCenter` (a minor piece leaves home in the opening and attacks a centre square),
    `DevelopsOpening` (any other piece leaving home in the opening), `DevelopsMiddlegame` (leaving home
    later, mostly rooks from a1/h1); `PreparesBishopDevelopment` (a pawn move frees a bishop with no
    square at home).
  - Endgame and structure: `PushesPassedPawn` / `PushesPassedPawnEndgame`, `MakesPassedPawn`,
    `KingActivity` (in the endgame a king on its first two ranks steps closer to the centre, onto a
    square not attacked; without the rank condition 50 of 72 were remarks Chess.com does not make),
    `CreatesLuft` (after castling, a g- or h-pawn one step forward).
- **Positional errors** (group 14, BASE of a bad move): `LosesCastling`, `DoubledPawns`,
  `IsolatedPawn`, `BackwardPawn` (new weaknesses in our own pawns; a pawn that was already weak and
  moves on is none), `WeakensKing` (f3/f6 in the opening, king at home or castled short; Chess.com's
  NeverPlayF3), `MovesPawnInFrontOfKing` (a shelter pawn of the castled king), `TooEarlyQueen` and
  `MovesSamePiece` (in the opening, while two or more minor pieces are at home), `MovesToPassiveSquare`
  (a piece not under attack loses at least 4 squares and ends with at most 3).
- **Circumstances.** BASE on a good move (its own line gives the recapture for the forced
  weaknesses), MISSES on the best move (with B's line), BASE errors on a bad move, and PERMITS for a
  reply that forces a weakness on our pawns (`circ::permits_weakness`). The phase is the game phase
  after the move (`CoachInput.phase`).
- **Priority.**
  - Good moves: … stopped mate; a forced weakness; trade, defence, tempo; a tactic that wins nothing;
    **a positional idea**; any threat; any stopped threat; `MaterialGain`; `OnlyMove`. This follows
    Chess.com's add_good: any BASE event comes before any THREATENS.
  - The best move's sentence (Misses block): the same order, so B's positional idea comes after its
    tactics, trades and defences and before its threats.
  - Bad moves: what it allows and what it misses (tactics, material, defence: unchanged; positional
    PERMITS and MISSES events are left out here), then **a positional error of the move**, then a
    weakness the reply forces, then **the best move's positional idea**, then the move's threat, the
    only move, the slide.
- **Book moves** get a note when a development or centre tag applies (`Tag::is_development`):
  "Nf3 is a book move: it develops White's knight toward the centre." (`frame.book_good`, said on
  the played move so the fragment carries its arrow). Other book moves stay empty.
- **Rating gates.** Every tag has a `min_rating` in `text/en.toml`: tactics, material, defence and
  development 0 (overloaded defender and decoy 600); activity 600–900; structure 1000–1100. The rating
  is the player's Elo from the PGN when the request sets `player_side`, else `rating_used` (the higher
  Elo plus 200, at least 1000). Gated events are dropped before selection, so when the only idea of a
  move is gated the note is empty. `ReviewConfig.coach.rating_gates` (default `true`) turns it off.
- **Human-move model** (`human.rs`, `tools/maia/maia_sidecar.py`): Maia-2 (MIT) as an optional
  sidecar process started from `MAIA_COMMAND`, speaking one JSON line per batch of positions. After the
  engine searches, `run_review_with_model` asks, for every non-book move from move 11 on, P(played)
  and P(best) at the mover's Elo (else `rating_used`) against the opponent's, in batches of 256. A
  failing model is logged and left out. Moves 1–10 are not asked: Maia-2's training config skips the
  first ten moves of each game (`first_n_moves: 10`), and there it rates 1.e4 below 1.Na3 at 1200
  and 2.Ke2 among its top moves after 1.e4 e5. In the coach:
  - P(best) < 0.10 on a bad move: the "missed" and "better was" frames take their `_hard` wording
    ("Better was Nf3, a hard move to find at this level: it …").
  - P(played) ≥ 0.30 on a Mistake or Blunder: what it allows is said with the `_natural` wording,
    leading with the safety check ("Ke8 looks natural, but check the reply first: Nc7+ forks …").
  - **Why a sidecar and not `ort`.** Maia-2 ships as PyTorch code and weights, not ONNX; an ONNX
    export would have to be made and kept in step with its board encoding, Elo bucketing and
    1,880-move vocabulary, all reimplemented in Rust. `ort` also brings onnxruntime's native library
    into every build (downloaded at build time), for a feature most users will not enable, and does
    not fit the zig-cc cross build used here. The sidecar runs the reference implementation
    unchanged, behind a process boundary like Stockfish, and costs nothing when it is not configured.
    It needs Python, PyTorch and the weights, installed separately (`docs/configuration.md`).
  - **Checked against the real model** (Maia-2 rapid, torch 2.8.0 CPU, on the 142 calibration
    games): of 1,422 bad moves from move 11 on, 282 (20%) get the "hard to find" wording and 130 of
    619 Mistakes and Blunders (21%) the "looks natural" wording. Tags are unchanged (the comparison
    gives the same 58.3% / 39.2%). The model adds about 0.5 s per game on 2 CPU threads. Examples:
    "Qxa8 looks natural, but check the reply first: Qxh3 starts a forced mate in 3. Better was Qh7, a
    hard move to find at this level: it moves White's queen out of danger."; "Kh1 allows Qf3+, which
    starts a forced mate in 2. Better was Rf1, hard to find at this level: it stops Re2+, which starts
    a forced mate in 3."
  - The sidecar points `sys.stdout` at stderr: the maia2 package prints progress with `print()`,
    which would otherwise break the line protocol.
- **Frontend.** `lib/tags.ts` names the new tags. Development and castling are `routine` (takeaways
  do not praise them); the errors have takeaway verbs and Retry hints. Book notes show in the bubble
  above the opening name.
- **Tests.** One or more positions per tag in `tests/coach_positional.rs`; notes, the gate, book notes
  and the difficulty wording in `tests/coach_note.rs`; book notes in the pipeline in
  `tests/coach_pipeline.rs`; the sidecar protocol (against `tests/fixtures/fake_maia.sh`) and a model
  through the review pipeline in `tests/human_model.rs`.

## Coach fact checker

`coach/verify.rs` (`coach-analysis.md` §8 item 3, `coach-gap-analysis.md` §7.2 step 1). It checks a
`CoachNote` the way a user reads it, as text, so it can also hold reworded text (Phase 5) to the
facts. It is pure: the position before the move, the move, the previous move, the engine's best line,
and the event lines stored in the note.

- **Parsing.** Each sentence is matched against every wording of every frame in `en.toml`, with
  `{pred}` replaced by its event's tag phrases (`vp`, `vp_long`, the "wins" form). Each placeholder
  only matches words of its kind: one SAN, a line of SANs, "Black's knight on f6", a list of pieces, a
  gain phrase, a number, a side. A sentence no frame produces is `unparsed`. When several frames
  match ("{move} {pred}." and "{reply} {pred}."), the reading with the fewest false claims wins, then
  the one with the fewest unchecked claims.
- **Where moves are played.** `{move}` and `{best}` from the position before the move. `{line}` from
  the position after it for what the move allows (BASE and PERMITS frames), before it otherwise. A
  `{reply}` without a line comes from:
  - after the move, for what it allows;
  - the null-move position after the move, for "threatens";
  - before it with the opponent to move, for "stops";
  - after the best move with its mover to move again, for what the best move threatens.

  Every SAN must be legal there and written as SAN writes it, check suffix included. The sentence's
  moves must be the start of its event's engine line (the event's `line`, from the position its
  circumstance implies). `{move}` must be the played move, `{best}` the engine's first move.
- **Pieces.** A named piece must stand on its square after the subject move (the reply, else the
  played or best move). It must stand there before the move when the move takes it or the text says
  it "was" there: free piece, removed defender, the targets of a losing trade, a checker escaped.
  Exploited pins, overloads and attraction accept either; "once a pawn takes back" is checked after
  the answer. "Your" and "their" are resolved by the note's style; a piece named without its square
  must be the moved piece, or the side's own bishop or king.
- **Tag phrases**, checked from the board, not from the detectors:
  - fork: the moved piece attacks every target;
  - pin and skewer: a line piece of the side attacks the front piece, and the back one is next on the
    same ray;
  - discovered check and attack: a piece other than the moved one gives check, or newly attacks the
    targets;
  - double check: two checkers;
  - removes defender: the move takes it, and it guarded the targets;
  - hanging, under attack, offered: the other side attacks it;
  - defends: the piece was attacked, and the moved piece guards it or blocks the attack;
  - also captures and take-backs, promotion, castling side, open file, seventh rank, passed and
    isolated pawns, the central push, and the bishop's opened diagonal.
- **Material.** The gain words promise a minimum: "a knight" more than two pawns, "about N pawns" at
  least N − ½. The line's first mover must be that far ahead at some settled point (no capture next)
  from the subject on. The lead is counted three ways, and any one is enough: from the line's start,
  from before the move that led to it (taking back is not a gain, as in `Line::net`), or from the
  subject move.
- **Mate.** "A forced mate in N" must mate within N moves of the subject on the line. A mate beyond the
  12 plies the coach keeps is reported as *unchecked*, not false.
- **Arrows.** A move arrow must be a move of the sentence, a best arrow the best move. An attack or
  defence arrow needs a real attack, or an x-ray through one piece, from the piece on its tail, before
  or after the subject move.
- **Show-lines** must start from a position the note is about. Each move must be legal, with the
  right SAN and FEN, and the line must be its event's line (or the best line). There must be one
  narration per move, each naming its own move; captures, take-backs, checks, "only move" and tactic
  narrations are checked as above.
- **Not checked:** the engine's judgement ("the only good move", "hard to find", a slide from equal to
  worse, a sacrifice that works, a book move), and whether the coach picked the best idea.
- **The checker itself is tested** by `verify::mutate`, which changes one claim at a time. On the 142
  games (`--mutate`):

  | changed claim | tried | caught |
  |---|---:|---:|
  | a move goes to the next file | 8,678 | 100% |
  | a narration names the next move | 15,260 | 100% |
  | a piece's owner | 5,533 | 100% |
  | a piece's square (next file) | 3,697 | 99.7% |
  | a gain made larger | 1,185 | 96.6% |
  | a mate in N said as N − 1 | 473 | 71.9% |

  The uncaught squares are phrases whose geometry is not checked (offers to trade, battery), or a
  pawn on the next file that fits the claim as well. The uncaught gains are lines that do win that
  much later. The uncaught mates are the 133 mates past the line's end.
- **Results** (run `coach-verify-4b84721`, the 142 calibration games, with the engine results of the
  `582bdd9` run from the local disk cache; labels unchanged at 68.7%):

  | | `582bdd9` | `4b84721` |
  |---|---:|---:|
  | sentences (8,884) with a false claim | 75 (0.84%) | 0 |
  | narrations (24,274) with a false claim | 12 (0.05%) | 0 |
  | claims unchecked (mates in 7–20) | 133 | 133 |

  101,440 claims were checked. All 75 false sentences had a false arrow. The fixes in the coach:
  - **En passant.** The narration "exf6 takes Black's pawn on f6" and the material-gain focus named
    the destination; `board::captured_square` gives the captured pawn's square (f5).
  - **Blocks.** `DefendsPiece` by interposition ("f3 defends White's queen on d1") was drawn as a
    guard from f3 to d1. It is now drawn as the attack the blocker stands in, an x-ray through f3.
  - **The central push.** `PreparesCentralPush` drew the planned d7–d5 as an attack. It now draws the
    moved pawn guarding d5.
  - **King shelter.** `WeakensKing` (f7 to e8) and `MovesPawnInFrontOfKing` (g1 to f3) drew attacks
    from squares that attack nothing. They mark the squares instead.

  The Chess.com comparison (`coach_compare.py`) gives the same report as `582bdd9`.
- **Tests.** `tests/coach_verify.rs` reviews the fixtures and the first 16 calibration games with the
  fake engine, as neither side and as each side, and requires every claim to be true. It also requires
  every changed move and narration to be caught, and nine in ten changed squares and owners. Against
  the `582bdd9` coach it fails on the en passant narration and the central-push arrow.
- **CLI.** `cargo run --release -p review-server --example coach_verify -- <run dir | game.json |
  game.pgn> [depth] [--list] [--mutate]`. For a PGN it reviews the game first (`STOCKFISH_PATH`). It
  prints the false claims (all with `--list`, plus the unchecked ones and the missed mutations), and
  the rate by kind.

## Coach UI (phase 3)

Frontend only (`coach-analysis.md` §6.8). It reads `PlyReview.coach` and keeps working when a move
has no note, or when the backend adds fields or tags.

- **Fragments.** In `Coach.tsx`, fragments with arrows or squares are buttons. Hover (mouse) or focus
  (keyboard) draws that fragment's arrows and square rings on the board, in place of the default
  main-sentence arrows. A click or tap pins it; a second tap unpins it.
- **Show-lines.** Each `show_line` is a button with its `label`. It opens a `LinePreview` with source
  `"coach"`. The board starts at `start_fen` (move -1) and plays itself. The bubble shows each move's
  `narration` and the line's moves as chips. Prev, Play/Pause, Next and ← → step through it; Hide or
  Esc returns to the game.
- **Avatar mood** (`coachMood`): impressed for Brilliant and Great, happy for Best, concerned for
  Mistake and Miss, sad for Blunder, neutral otherwise. In Retry it is happy when solved and
  concerned after a wrong try. It is drawn with CSS only (tile colour, tilt, a short hop or slump).
- **Retry** (`lib/retry.ts`):
  - The hint ladder comes from one event: a MISSES / MISSES_SAME event of the mover when there is
    one, else the main sentence's event.
  - Rung 1 rings the geometry's target squares (fan targets, the x-ray's front and back, the
    relation's end, and so on). Rung 2 names the motif: "Look for a free piece", "Make sure your
    move doesn't allow a fork", or the error tag's own hint for BASE events. The last step reveals
    the move.
  - Without an event, the only rung is the old one: the piece to move.
  - `judgeRetry` accepts the best move, or the first move of any engine line within 0.04 expected
    points of it. It uses the backend's curve at `rating_used`. Moves outside the engine lines
    cannot be judged and count as wrong. In a lost position most engine lines pass, as on lichess.
- **Takeaways** (`lib/takeaways.ts`, report view): events said by a move's sentences, counted once per
  move under (side, kind, tag family).
  - Kinds: PERMITS gives "Allowed", MISSES gives "Missed", an error tag in BASE gives its own verb
    ("Left a piece hanging"), and BASE on a good move gives "Found".
  - The four most frequent are shown, then the most costly by expected points lost. Each links to
    its moves.
  - Tag wording for hints and takeaways is in `lib/tags.ts`. Unknown tags fall back to "a tactic".
