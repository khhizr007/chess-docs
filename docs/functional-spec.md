# Functional Specification — Game Review

This document records the behaviour of the reference application's game-review system as
recovered by reverse engineering, and states how this project reproduces it.

Every rule is tagged:

- **Confirmed** — read directly from decompiled code or binary data of the reference build.
- **Inferred** — strongly suggested by the evidence (names, call structure, data), but the
  exact behaviour was not fully decoded.
- **Unknown** — not recovered. This project implements a documented, configurable fallback.

Unresolved items are tracked in [`open-questions.md`](open-questions.md).

## 0. Evidence base

| Artifact | Identity | What it contributed |
|---|---|---|
| Android app, v4.10.9 (universal APK) | `280025_4_10_9_googleplay_universal_1787158510211.apk` | Kotlin client: transport, request/response mapping, UI predicates |
| Native review engine `lib/arm64-v8a/libcee.so` | SHA-256 `85559784dc68be1dad2d3f58e06e27a1dff33f48fa2dc82d6cea0d4ff969447d` | Classification, expected points, accuracy (CAPS2), mate handling |
| Decompilers | JADX 1.5.6 (Java/Kotlin), Ghidra 12.1.4 headless (native), Capstone (spot disassembly) | |

The native library exports about 16,900 C++ symbols (namespace `TEP`), so recovered functions are cited
by name, with the `nm` address in brackets. No code or data from the reference application is copied
into this project; formulas and constants are restated from the analysis.

### Where the reference app computes a review
- **Confirmed.** The full review screen requests analysis from a cloud service over a WebSocket. The
  request carries the game's moves, both ratings, the user's colour, a strength preset
  (Fast/Standard/Deep/Maximum) and an engine (`ENGINE_SF16_1_NNUE` = Stockfish 16.1 NNUE, or `ENGINE_TORCH_HUMAN`),
  and asks for classification version 3.
- **Confirmed.** On-device, the same review engine (`libcee.so`) is used for the game-over summary and for
  "play your own move" feedback (default depth 18). A flag can enable it as a fallback for the full review.
- **Inferred.** The cloud runs the same engine: the protobuf contracts and option names are shared. This
  project treats the on-device engine as the reference algorithm.
- **Consequence.** The original separates *search* (Stockfish/Torch) from *review logic* (`TEP`). This
  project keeps the same split: Stockfish over UCI for search, and an independent Rust crate
  (`review-core`) for the review rules.

## 1. Game representation and parsing
- **Confirmed.** The client sends games either as PGN or as a move list with start FEN, move clocks and
  metadata (players, `WhiteElo`/`BlackElo`, time control, result, game id).
- **Confirmed.** The engine accepts PGN and FEN, and supports Chess960 (UCI option `UCI_Chess960`).
- **This project.** PGN import (multiple games per file, standard headers, SAN, comments/NAGs ignored for
  analysis but preserved, `[SetUp "1"]`/`[FEN]` start positions) via `pgn-reader` + `shakmaty`.
  Chess960 is accepted when the `Variant` header says so.

## 2. Position reconstruction & 3. legal-move validation
- **Confirmed** (by necessity): every move is applied to a full board model, and illegal moves are
  rejected (`FEATURE_ID_VALIDATE_PGN`, `RELAXED_*` features).
- **This project.** `shakmaty` performs SAN resolution and legality checks. An illegal or ambiguous SAN
  produces a structured error naming the ply and the SAN token.

## 4. Position evaluation
- **Confirmed.** Positions are searched by an external engine (cloud: SF 16.1 NNUE or a "human" Torch
  network; local: Komodo or Torch inside `libcee`). Review rules consume one score per tree node: the
  score of the position after a move, from the perspective of the side that made the move.
- **Confirmed.** Score units: centipawns. Mates are encoded near ±32000; `to_score` [`0x1138938`] converts to
  pawns as `cp / 100`, and a mate in N becomes `±(1000 − 10·min(N, 50))`.
- **This project.** Stockfish (configurable version and path) through UCI with MultiPV. One search per position.
  - Best line and alternatives come from the search of the position *before* the move.
  - The played move's score is that move's MultiPV line when present. Otherwise it is the negated
    evaluation of the position *after* the move. Calibration against Chess.com confirmed this choice: a
    search of the parent position restricted to the played move matched worse.
  - Every search starts from a cleared hash (`ucinewgame`, Clear Hash) with one thread, so a review is
    reproducible run to run.
  - Internally every score is stored from White's perspective and converted to the mover's perspective only
    inside the classification functions.
  - **Expected difference:** the engine version and depth differ from the original, so classifications can
    differ near thresholds.

## 5. Move classification (classification v3)

### 5.1 Expected points (win probability) — Confirmed
From `TEP::centipawns_to_expected_points(Value, int)` [`0x11389d4`]:

```
k(R) = 0.004 · (0.0685·R − 12) / 100
EP(cp, R) = 1 / (1 + exp(−k(R) · cp))
```
The inverse, `expected_points_to_centipawns` [`0x1138a3c`], is `cp = ln(1/EP − 1) / (−k(R))`.

- **Rating R** (`node_lib::elo_rating_for_expected_points` [`0x1310a34`]) is `max(WhiteElo, BlackElo)`,
  clamped to `[1000, 2500]`.
  - **This project (calibrated).** 200 is added before the clamp (`rating_offset`): Chess.com's grades
    match a rating above the PGN's game-time ratings (see `parity.md`). Set it to 0 for the recovered rule.
  - **This project (calibrated).** The upper clamp is 3000 (`rating_max`), not 2500: applied to
    Chess.com's own captured scores, the 2500 cap grades titled games too leniently (81% → 88% of
    labels reproduced; `calibration/log.md`). Set it to 2500 for the recovered rule.
  - **This project (calibrated, 2026-10-23).** The lower clamp is 1200 (`rating_min`), not 1000:
    Chess.com grades games below 1000 as if rated about 1200, Blunders above all
    (`calibration/great-blunder-analysis.md` §3.2). Set it to 1000 for the recovered rule.
  - Missing ratings count as 0 and therefore become the lower clamp (recovered: **1000**).
  - With no game context at all, R is **2000**.
- **EP of a node** (`node_lib::expected_points` [`0x130c9c8`]) is `0.5` if the position is a draw by
  rule. Otherwise it is `EP(score, R)` from the mover's perspective. Mate scores saturate to about 1 or 0.
- **Expected points lost** (`node_lib::expected_points_lost` [`0x13118f4`]) is
  `EP(best alternative) − EP(played)`.

### 5.2 Expected-outcome buckets — Confirmed
`TEP::expected_outcome(Value, int)` [`0x1139e70`] compares the score with `cp(EP_i, R)` for these
default thresholds, found in read-only data: `[0.10, 0.20, 0.35, 0.65, 0.80, 0.90]`.

| Bucket | EP range | Meaning |
|---|---|---|
| 0 | < 0.10 | lost |
| 1 | 0.10–0.20 | losing |
| 2 | 0.20–0.35 | worse |
| 3 | 0.35–0.65 | equal |
| 4 | 0.65–0.80 | better |
| 5 | 0.80–0.90 | winning |
| 6 | ≥ 0.90 | completely winning |

- `is_losing` is bucket < 2.
- `is_completely_winning` is bucket 6, optionally also requiring a material lead of at least 300 cp.

### 5.3 Precision grade — Confirmed
From `MovePrecisionV3Registry::compute` [`0x110466c`], with thresholds from read-only data
`[0.02, 0.05, 0.10, 0.20]`:

| Condition | Grade |
|---|---|
| played score == best score | Best |
| EP lost ≤ 0.02 | Excellent |
| ≤ 0.05 | Good |
| ≤ 0.10 | Inaccuracy |
| ≤ 0.20 | Mistake |
| > 0.20 | Blunder |

The mate override (§5.6) is applied on top of this grade.

### 5.4 Classification decision tree — Confirmed (structure), partly Inferred (detectors)
From `MoveClassificationV3Registry::compute` [`0x1104844`]. The first rule that matches wins:

1. Opening-book move → **Book**.
2. Forced move → **Forced**.
3. The move carries a *brilliant* board event → **Brilliant** (see §5.5).
4. The move carries a *tricky* event and option 21 (`AllowTrickyClassification`) is on → **Tricky**.
   The Android client maps Tricky to nothing, so it is **disabled by default** here.
5. The move carries a *great find* event → **Great Find** (see §5.5).
6. Otherwise `c = precision`, then:
   - a. If `c == Blunder` and the move does not actually lose material or allow mate → **Mistake**.
   - b. If `c ∈ {Excellent, Good, Inaccuracy}`, the mover is losing (EP < 0.2), the move loses more
     material than the best move, and material lost ≥ 200 cp → **Mistake**.
   - c. If the *precision* is Mistake or Blunder, the miss checks run in order. Let
     **A** = "the played move itself drops material" and **B** = "EP lost > 2 × the opponent's previous EP lost":

     | Condition | Result |
     |---|---|
     | ¬A ∧ best move takes a free piece | MissedFreePiece |
     | ¬A ∧ best move wins by a tactic | MissedTactic |
     | ¬A ∧ ¬B ∧ best move was winning | MissedWin |
     | ¬A ∧ ¬B ∧ best move was a comeback | MissedComeback |
     | ¬B ∧ best move was brilliant | MissedBrilliant |
     | ¬A ∧ ¬B ∧ best move punished the opponent's error | MissedOpportunity |

     All miss subtypes are reported to the UI as **Miss** (`classification_v3::classification_external_name`
     returns `"miss"` for ids 10 and 12–18).
7. The **mate override** (§5.6) may replace the result of step 6. Steps 3–5 return early, so
   Brilliant, Tricky and Great Find are never overridden.
8. If the node or its parent has no reliable score: **Best** if the move has no siblings, otherwise no
   classification.

Internal enum (Confirmed, from `move_cls_to_pb` and `speech::get_classification_id_lookup`):

| Id | Class | Id | Class |
|---|---|---|---|
| 0 | Book | 10 | MissedWin |
| 1 | Brilliant | 11 | Forced |
| 2 | GreatFind | 12 | MissedFasterMate |
| 3 | Tricky | 13 | MissedMate |
| 4 | Best | 14 | MissedFreePiece |
| 5 | Excellent | 15 | MissedTactic |
| 6 | Good | 16 | MissedComeback |
| 7 | Inaccuracy | 17 | MissedBrilliant |
| 8 | Mistake | 18 | MissedOpportunity |
| 9 | Blunder | 19 | none |

### 5.5 Board-event detectors
The reference engine attaches "board events" (about 250 tactical/strategic tags) to moves.
Brilliant, Tricky and Great Find are events in circumstances 13, 14 and 15 (`TEP::get_circumstance_id`).

**Brilliant** (`compute_board_event<13>` [`0x1074d74`]):
- **Confirmed.** It requires a sacrifice event, computed via `node_lib::is_sacrifice` /
  `sacrifice_board_event`.
- **Confirmed.** In the endgame it additionally requires either a specific base event or a maximum material
  gain of at least 200 cp.
- **Confirmed.** It is gated by the mover's material balance after the move compared with the value of the
  relevant piece. Piece values: P 100, N 300, B 300, R 500, Q 900, K 99999.
- **Confirmed.** If that gate fails, the event is still allowed when the opponent was not already lost
  (EP ≥ 0.10 at R = 2000).
- **Inferred.** The exact sacrifice definition was not decoded.
- **Published.** Chess.com's help article ("How are moves classified?", Classification V2): a Brilliant
  move is the best or nearly best move and "a good piece sacrifice"; the player must not be in a bad
  position after it and must not be completely winning even without it; the sacrifice test is more
  generous for newer players.
- **This project.** The published conditions with a static sacrifice (static exchange evaluation, not a
  line walk). The move is the engine's best move and gives up at least 100 cp net: the moved piece
  (knight, bishop, rook or queen, or a pawn when both players are below 1000), or a piece it leaves newly
  en prise (castling included), can be won by exchange for more than the move captured. The mover's EP
  after the move is at least 0.50, and the second-best move is not completely winning (EP < 0.90; a
  forced mate there does not count). No gap to the second-best move is required, and mating sacrifices
  qualify. See `implementation-notes.md`.
- **Calibrated.** Against Chess.com's Stockfish reviews of 60 games (October 2026): the earlier rule
  (second-best ≥ 0.10 EP worse, EP before in [0.10, 0.90), moved piece only, no mating moves) found 2 of
  the 9 Brilliants; this rule finds 7 of 9 and gives 5 others (see `calibration/log.md`). The earlier
  line-walk test gave 60 Brilliants for the app's 3.

**Great Find** (`is_candidate<15>`, `is_great_find_candidate_core` [raw `0x11d652c` in APK 4.10.15],
`compute_board_event<15>`; decompiled again 2026-10-23, `calibration/great-blunder-analysis.md` §2.1):
- **Confirmed.** A move is Great when it is a candidate and one of the eligible tags fires.
- **Confirmed.** Candidate: precision is Best or Excellent, the move is not "easy to find", and it is not
  an obvious quiet retreat. In a high-rated game (`TEP::is_high_rated`: `max(WhiteElo, BlackElo) > 999`)
  it is also not a simple recapture after an even trade, not a mating move, and does not take the
  attacker in an even exchange. If the same side's previous move was a candidate with a tag, this move
  is neither a capture nor a passed-pawn push.
- **Confirmed.** "Easy to find", in order: castling never; a hard position by the position-difficulty
  model never; a safe promotion; the piece's only safe square; and, only when high-rated, an obvious
  recapture or a free piece.
- **Confirmed.** The tags:
  - key moments, after an opponent's move graded Mistake or Blunder (or a missed mate, or ungraded),
    when the mover's EP after the move is ≥ 0.47, the mover was not completely winning after their
    own previous move, and the move is not a recapture: it forces mate in ≤ 4 (from ≤ 1499 cp after
    the mover's previous move); it wins more than 100 cp along the line (not a free piece, and not
    already won by the mover's previous move); or, below the high-rated mark only, it takes a free
    piece;
  - critical: the best move, EP(best) ≥ 0.35, the second line's EP < 0.80 and at least 0.10 below
    (an interposition with a piece that is lost there does not count), and not an obvious recapture;
  - winning: from the opponent's equal-or-better before the mover's previous move to the mover's
    winning now;
  - comeback: from the opponent's winning then to the mover's equal now.
- **Unknown.** The position-difficulty model is machine-learned; it only makes a position "hard" and
  so never easy. The gates once attributed to Great here (time trouble, the Brilliant endgame gate,
  move probability) belong to other events.
- **This project.** The recovered structure without the difficulty model. Three readings differ from the
  decompile, each because the calibration games disagreed with it:
  - an immediate recapture is never critical, whether or not our exchange test calls the square safe;
  - the only-safe-square test needs a threatened piece other than a pawn;
  - material gain is our line walk.
- **Calibrated.** On 142 Chess.com reviews, precision 0.81 and recall 0.74 (holdout 0.84 / 0.75),
  against 0.62 / 0.05 for the earlier gap proxy.

**Tricky** (`compute_board_event<14>`):
- **Confirmed.** It depends on the position-difficulty and move-probability models.
- **This project.** Not implemented; disabled.

### 5.6 Mate override — Confirmed
From the local helper at [`0x1104c28`]. Scores are seen from the mover's perspective after the move. A
mate distance `md` counts the mover's remaining moves to mate (0 = checkmate on the board).

- **Best line mates, played move does not (or the sign flips):**
  - Played move still completely winning (bucket 6) and the best mate is longer than 2 moves → **Good**.
  - Otherwise → **MissedMate**.
- **Both lines mate for the mover:**
  - best `md = 0` and played `md > 1`, or best 1 and played > 3 → **MissedFasterMate**.
  - best 1 and played > 2, best 2 and played > 4, or best 3 and played > 6 → **Good**.
  - Otherwise no override.
- **Both lines get mated:** best mated in > 2 but played mated in 1, or best > 4 but played 2 → **Inaccuracy**.
- **Played move allows mate but the best line does not:** applies only if the best line was already lost
  (bucket 0). Then mated within 3 moves → **Mistake**; best score > −1501 cp → **Inaccuracy**; otherwise
  **Good**.

### 5.7 When a best move is shown — Confirmed
- `api::should_attach_best_alternative_move` attaches the best alternative for every class except Book,
  Brilliant, Great Find, Best and Forced. The client uses the same predicate.
- The client offers "Retry" when the user's move is not in
  {Brilliant, Great, Best, Book, Excellent, Good}.

## 6. Best alternative selection
- **Confirmed.** The best alternative is the parent's best child (the engine's top line). The suggested
  continuation is that line's principal variation.
- **This project.** MultiPV=3 (configurable). Line 1 is the best move, lines 2–3 are alternatives, and each
  line carries its PV in SAN.

## 7. Win-probability changes
Per ply, the EP before the move, the EP after, and the EP lost (§5.1) are all reported. The UI shows
White-perspective values for the graph and mover-perspective values in the move panel.

## 8. Accuracy (CAPS2) and aggregation — Confirmed
From `CAPS2ImplRegistry::compute_child` [`0x10ea314`] and `compute_caps_for_move_nodes` [`0x10e96f8`].

**Per-move score.** Let `p` be the played eval and `b` the best eval, both mover-perspective, in pawns
(`to_score`). Let `Δ = b − p` and `x = min(|p|, 20)`.

```
t1 = 0.579 − 0.138·x + 0.0187·x²
t2 = 1.5   − 0.0699·x + 0.0265·x²
t3 = 3.57  + 0.0291·x + 0.0279·x²
Δ ≤ 0      → 100
Δ ≤ t1     → 100 − 20·Δ/t1
Δ ≤ t2     → 80 − 50·(Δ − t1)/(t2 − t1)
Δ ≤ t3     → 30 − 80·(Δ − t2)/(t3 − t2)
Δ > t3     → max(F, −50 − ((Δ − t3)/(2.1401·(t3 − t2)))·(50 + F))
```

**Floor F (per colour).**
- Initial state: F = −100, G = −50.
- Each "very bad" event first increments a counter. From the second event onward,
  `F ← min(F + (|F| − |G|)·0.25, G)`. Repeated disasters therefore cost progressively less, with F
  converging toward −50.

**Clamps by played eval p** (pawns), checked in this order:

| Condition | Effect |
|---|---|
| p ≥ 30 | max(s, 30) |
| 10 ≤ p < 30 | max(s, 80) |
| 6 ≤ p < 10 | max(s, 30) |
| 5 ≤ p < 6, or (p ≤ −25 and b ≥ −10) | max(s, −50) |
| p ≤ −20 and b ≥ −15 | max(s, 30) |
| −30 < p | unchanged |
| otherwise | max(s, 0) |

**Special cases.**

| Situation | Score |
|---|---|
| Book move | 100 |
| Checkmate delivered | 100 |
| Forced move | not scored |
| Both mate, same score | 100 |
| Had a mate, now getting mated | F |
| Both mate, slower | 80 if the extra moves are ≤ 1 (when the best mate is ≤ 1 move) or ≤ 2 (otherwise); else 70 |
| Played allows mate, best not mate: b ≤ −50 | 70 |
| Played allows mate, best not mate: −50 < b ≤ −10 | 30 |
| Played allows mate, best not mate: b > −10 | F |
| Best mated, played escapes | 100 |
| Missed own mate: p ≥ 50 | 70 |
| Missed own mate: 10 ≤ p < 50 | 30 |
| Missed own mate: p < 10 | F |

**Aggregation.**
- Accuracy per colour is the mean of the per-move scores, clamped to ≥ 0.
- It is also computed per game phase and per moved-piece type.
- Moves made when the mover was already completely lost (the opponent was completely winning with a material
  lead of at least 300) are excluded.
- **Unknown.** The display rounding on the server. The client formats it as `%.1f`.

## 9. Game phases
- **Confirmed.** Phases are opening, middlegame and endgame. They are computed per position by a
  hand-tuned heuristic (`TEP::compute_game_phase`) that uses major/minor piece counts per side,
  piece-square-weighted material, development and castling rights. Phases are made monotonic over the game
  (`node_lib::monotonic_phase_transitions`).
- **Unknown.** The exact weights and thresholds of that heuristic.
- **This project.** A documented, configurable approximation (monotonic):
  - Endgame when there are ≤ 6 non-pawn, non-king pieces on the board.
  - Middlegame when there are ≤ 10 such pieces, or either side has ≤ 3 pieces left on its back rank, or
    from ply 40. (Castling is not used as a trigger; it started the middlegame unrealistically early.)

## 10. Special situations
| Situation | Handling |
|---|---|
| Checkmate on board | Terminal. Score = mate 0. CAPS2 gives 100. The mate rules apply. |
| Stalemate / insufficient material / 50-move / threefold | EP = 0.5 (Confirmed: draw → 0.5). Eval 0. |
| Castling, en passant, promotion | Handled by the rules library. Promotion counts as a material change. |
| Resignation / agreement / timeout | Taken from the PGN `Result` and termination. Reported, not classified. |
| Only one legal move | Forced (Inferred: the exact `is_forced` definition was not decoded). |

## 11. Summary, annotations and metrics
- **Confirmed (client).**
  - Accuracy per player is shown with one decimal.
  - The tally shows classes per player, with **Forced counted under Best**.
  - Key moments are flagged per move.
  - The coach text appears only when permitted.
  - The game rating ("effective Elo") is shown only when both players have one.
- **Key moments.**
  - **Confirmed:** the candidate filter (`is_key_moment_candidate`): scored, not forced, not already in a
    bad position, precision Best or Excellent, the mover was not already completely winning, not a
    recapture.
  - **Inferred:** a candidate becomes a key moment when it wins material, forces mate, takes a free piece
    or promotes.
  - **This project** also marks critical moments, defined as moves classified Blunder, Mistake, Miss,
    Brilliant or Great Find.
- **Unknown:** the effective game rating formula, the 250-tag tactical explanation system, and the coach
  speech. This project generates explanations only from engine facts:
  - eval change,
  - best move,
  - mate distances,
  - material lost along the principal variation.

  These are labelled as generated, and no tactical motif is claimed unless it is computed.

## 12. Presentation and workflow (reference client)
- **Confirmed.** Overview with accuracy, game rating, tallies and an evaluation graph. Move-by-move
  review with board arrows and highlights, a classification badge, coach text and the best move (when the
  predicate in §5.7 allows). Retry for weak moves. Key-moment navigation.
- **This project.** Board with arrows, eval bar, move list with badges, a move panel (played versus best,
  EP change, lines), a summary (accuracy, phase accuracy, tallies), an evaluation graph, and filters (all /
  needs attention / key moments / phase). No account or paywall logic.
