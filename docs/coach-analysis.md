# Building a real move coach: how Chess.com's coach works and how to build ours

October 2026. Sources: reverse engineering of the Chess.com Android app 4.10.15 and the Chess.com web
client, plus published research and products. This is an analysis and design document. Phase 1
(§7) is implemented in `backend/crates/review-server/src/coach/`; see `implementation-notes.md`, "Coach".

## 1. Summary

**Where we are.** Today [`explain.rs`](../backend/crates/review-server/src/analysis/explain.rs) and
[`lib/coach.ts`](../frontend/src/lib/coach.ts) produce text from three inputs: the classification, the
change in winning chances, and the engine's best move. So every Blunder reads roughly the same:
"A serious error. This hands the opponent a big advantage. Nf3 was the move to play." The text
says *that* a move was bad, but never *why*. It names no piece, threat or tactic, and shows no
line that proves the point.

**What Chess.com does.** Its coach is not a language model, and it does not paraphrase engine
lines. It is a deterministic pipeline inside the native library `libcee.so` (C++, namespace
`TEP`) with four stages:

1. **Board events.** About 280 detectors ("tags", such as Fork, HangsPiece, PinsDefender,
   DevelopsWithTempo or DoublesPawns) run on the nodes of a small game tree. Those nodes are the
   played move, the best alternative, the second-best alternative, the opponent's best reply, a
   null-move "threat" search, and the moves of the principal variation.
2. **Circumstances.** Each tag is combined with one of about 20 circumstances that say *whose*
   idea it is and *when* it happens. Examples: BASE (this move does it), THREATENS (it threatens
   it next move), PREVENTS (it stops the opponent's threat), PERMITS (it allows the opponent to do
   it), MISSES (the best move would have done it), LEADS_TO (it happens later in the line) and
   WINS_MATERIAL (the tactic wins material). Circumstances chain, as in "permits → wins
   material → fork".
3. **Prioritisation.** A hand-written decision procedure picks the one or two events worth saying.
   It branches on classification (good or bad move), on forced moves, mates and game over. Events
   are ranked by the order of the Tag enum.
4. **Text.** The chosen event becomes a key such as `Permits-WinsMaterial-ForkKnight-Personal`.
   The key is looked up in a 32,005-entry text table. Each entry has rating gates, several
   wordings and different voices (talking to you, about the opponent, neutral). If no full
   sentence exists, a circumstance prefix is joined to a verb phrase for the tag. The result is a
   `Speech` made of sentence fragments, and each fragment carries its own board arrows and
   highlighted squares. Alongside it come "Show fork / Show lost piece" buttons, which replay the
   line move by move with a sentence per move.

**What to build.** The same architecture, built in Rust on what we already have, with our own
vocabulary and our own text, and a few improvements Chess.com doesn't make:

- concrete squares and moves in the sentences, not only on the board;
- a safety-check framing for blunders ("before …Nf6, check White's captures");
- rating-aware difficulty from a human-move model (Maia-2);
- a retry mode with a hint ladder.

Research and other products agree on the core rule: **analysis first, language second.** Every
chess fact comes from the engine and from deterministic detectors. Templates, or optionally an LLM
held to a fact list, only turn those facts into words (§5).

The rest of this document gives:

- the evidence (§2);
- the recovered system in detail (§3);
- the gap against our app (§4);
- what the research adds (§5);
- the proposed design (§6);
- a phased plan with an evaluation method (§7–8);
- legal notes (§9).

## 2. Evidence base

| Artifact | Identity | What it gave |
|---|---|---|
| Chess.com Android app 4.10.15 (`com.chess`, versionCode 280060), APKMirror bundle: base plus 35 splits | 214,544,468 bytes, matches the size APKMirror lists | Kotlin client (JADX 1.5.6), assets |
| `lib/arm64-v8a/libcee.so` (Chess Explanation Engine) | SHA-256 `8a73b525…c7ad35`, 36.9 MB, 34,585 dynamic symbols | Coach logic, protobuf schemas, embedded coach text |
| `libcee_driver.so`, `libcee-wrapper.so` | SHA-256 `3f0ab5fd…`, `7139e4df…` | JNI bridge |
| Chess.com web client `analysis/2026.10.2` | JS bundles loaded on the analysis page, not signed in | How the review UI renders speech |
| Published research and products | See §5 | Design evidence |

Methods:

- I parsed the ELF symbol and relocation tables myself.
- I recovered **228 `.proto` schemas** from the serialized `FileDescriptorProto`s embedded in
  `libcee.so`.
- I inflated the embedded data blobs (an 8-byte size header followed by zlib).
- I disassembled and decompiled the relevant functions with Ghidra 12.1.4 headless, after defining
  each function from its exact ELF symbol size and resolving all 13,121 PLT stubs.
- Nothing was executed, and no request was sent to Chess.com apart from loading its public
  analysis page.

The extracted material stays in the session scratchpad. It is **not** committed to this
repository (§9).

Evidence tags used below:

- **Confirmed:** read from code, schemas or data.
- **Inferred:** strongly suggested by names and call structure.
- **Unknown.**

Function addresses are virtual addresses in `libcee.so`. Ghidra rebases them by +0x100000.

## 3. How Chess.com's coach works

### 3.1 Where it runs

- **Confirmed.** The same C++ engine (`libcee.so`, with protobuf API
  `chesscom.explanation_engine.v1`) exists on device and in the cloud.
  - The full Game Review response from `wss://analysis.chess.com/v2/game-review` is a
    `GameReview` message whose moves already carry `Speech`. So the web and the app only render
    text the server produced.
  - On device the library generates coach text for the play-against-coach mode (hints, "retry
    your mistake" offers) and for bot chat.
- **Confirmed (web).** The analysis page loads no CEE WebAssembly. It does load
  `stockfish-19-lite-single`, but only for interactive analysis. The review tab
  (`tab-review` / `shared.eager` chunks) maps protobuf fields to UI:
  - `sentenceFragments[].fragment` are joined into each sentence;
  - the first fragment that carries `arrowsAndSquares` drives the board overlay;
  - `showMovesButtons[]` become Show/Hide buttons, each with `movesToShow` and an explanation per
    move;
  - `coachEmotion` sets the avatar expression and the speech delay;
  - `audioUrlHash` plays pre-recorded voice lines.

### 3.2 What a reviewed move carries (`game_review.proto`, Confirmed)

```
PlayedMove {
  is_key_moment
  played_move:            Move        // the move actually played
  best_alternative_move:  Move?       // only when the played move was not the engine's
  moved_color, coach_emotion          // IDLE, SURPRISED, HAPPY, IMPRESSED, SHOCKED, THINKING, CONCERNED, SAD
  skills_earned
  explain_line:           PlayedMove[]  // the line, each node with its own speech and score
  best_next_move:         chess.Move?
}
Move {
  move, move_classification, score
  speech:             Speech          // sentences → fragments(text, arrows_and_squares)
  show_moves_buttons: ShowMoves[]     // { moves_to_show[], show_text, hide_text }
  board_markings:     BoardMarkings
}
```

Both the played move and the best alternative get their own speech. That gives the UI two
explanations: "what your move did" and "what the best move would have done".

### 3.3 The event model

A **board event** is `BoardEvent { circumstance, child_circumstance, analysis_type (tag),
arrows_and_squares, piece }` (`v1alpha/board_events.proto`). Its detailed form,
`BoardEventDetails.profile`, records the event's geometry. The geometry types are:

| Profile | Meaning (inferred from names and fields) |
|---|---|
| `TargetFan { source, targets[] }` | one piece attacking several (forks, multi-attacks) |
| `ConvergingFan { target, sources[], role: ATTACKERS/DEFENDERS }` | pile-up on a square or piece |
| `XRayAttack { attacker, front, behind }` | pins, skewers, x-rays |
| `PinExploitation { xray, exploited, direction }` | exploiting a pinned piece |
| `DefenseTriangle { defended, defender, attacker }` | overloaded or removed defender |
| `DirectedRelation { origin, target, relation }` | ATTACK, SACRIFICE, DISCOVERY, CHECK, DEFENSE, DEFENDER_REMOVAL, KING_ESCAPE, PIN_BREAK, DEVELOPMENT, BLOCKED_ADVANCE, PROMOTION_RUN |
| `SpecialMove { move, role }` | MATING_MOVE, THREAT, REPLY, CONTINUATION, ALTERNATIVE, REFUTATION, PAWN_STORM_ADVANCE |
| `KingPair`, `RookLine`, `FixedGeometry{waypoints, PATH/LOOP}`, `RangeWithPieces`, `LocationSet`, `MarkedSquare`, `WonSequence{game_point_ids}` | opposition, rook doubling and lifts, manoeuvres, pawn chains, outposts, winning sequences |

The geometry is what produces the arrows. A fork, for example, draws an arrow from the forking
piece to each target. **This is the key UI idea: every claim in the text is backed by a drawing on
the board.**

**Circumstances** (`Circumstance` enum, Confirmed), with what each combinator computes (Inferred
from the callees of `compute_board_event<C>`):

| Circumstance | Evaluated on | Callees seen |
|---|---|---|
| BASE | the move itself | the base detectors |
| THREATENS | **null-move search** after the move: what we would play if the opponent passed | `Node::null_move`, `Node::best` |
| PREVENTS | the opponent's null-move threat *before* our move, which our move stops | `prevents_pushing_passed_pawn`, `prevents_rook_on_seventh`, `prevents_central_push`, `is_free_piece` |
| PERMITS | the opponent's best reply after our move, plus material along the line | `best_alternate`, `primary_continuation`, `loses_material_sequence`, `hist_line_lib::material_gain` |
| MISSES / MISSES_SAME | our best (and second-best) alternative; "same" means we missed the very piece the opponent just left hanging | `best_alternate`, `second_best_alternate`, `captures_free_piece` |
| LEADS_TO | a later move of the principal variation does it | `primary_continuation`, `is_best`, `obvious_sequence` |
| WINS_MATERIAL | the tactic ends in a material gain (capture ply found on the line) | `HistLine::capture_ply`, `obvious_sequence` |
| MATE, FORCES, GAME_OVER, GAME_STATUS, ENDGAME | mating nets, forced sequences, results, phase remarks | |
| BRILLIANT, GREAT_FIND, TRICKY | the special classifications are events too | |
| LONG_THINK, SHORT_THINK, TIME_TROUBLE | clock-based variants ("in time trouble you allowed…") | |

### 3.4 The tag vocabulary

The public enum `AnalysisType` (v1alpha) has 301 values besides UNSPECIFIED. The internal enum
`TEP::Tag` has 282 values (0–281), and each has a detector template `compute_base_event<Tag N>`. I
recovered the mapping from the lookup table behind `TEP::api::tag_from_pb` (`0x12cab24`); it names
276 of the 282 tags. **The internal order is the priority
order** (§3.5). Grouped in that order:

| Tag range | Group | Examples |
|---|---|---|
| 0–13 | Draws, time, forced | STALEMATE_WHEN_WINNING_BLUNDERED, REPETITION, FORCED |
| 14–25 | Sacrifices (Brilliant support) | DIRECT_SACRIFICE_CAPTURE, IGNORES_THREAT, UNDERPROMOTION |
| 26–44 | Mates | BACK_RANK_MATE, LADDER_MATE, FORCES_MATE, STILL_MATE |
| 45–78 | **Winning tactics** | FREE_PIECE, FORK_WITH_MATE, ROYAL_FORK, FORK, SKEWER, REMOVES_DEFENDER, DOUBLE_CHECK, DISCOVERED_ATTACK, ATTACKS_TRAPPED_PIECE, EXPLOITS_PINNED_DEFENDER, EXPLOITS_OVERLOADED_DEFENDER |
| 79–104 | Trades and recaptures | PILE_TRADE, TRADE_TO_WON_PAWN_ENDGAME, EQUAL_TRADE, OBVIOUS_RECAPTURE, DESPERADO, ZWISCHENZUG_BEFORE_RECAPTURE |
| 105–139 | Defence and threats | REMOVES_ATTACKER, BLOCKS_ATTACKER, UNPINS_WITH_DEFENSE, PIN, RELATIVE_PIN, KICKS, RETREAT, ESCAPES_THREAT, DEFENDS_PIECE |
| 140–209 | **Positional and development** | STRIKES_AT_CENTER, PAWN_STORM, DEVELOPS_WITH_TEMPO, TAKES_OUTPOST, ROOK_ON_SEVENTH, TAKES_OPEN_FILE, DOUBLES_ROOKS, CASTLES_*, DEVELOPS, BLOCKADE, GAINS_*_SPACE |
| 210–222 | Game-level | CRITICAL, WINNING, COMEBACK, BLUNDER_PUNISH, TAKES_OPPORTUNITY, WINS_MATERIAL |
| 223–267 | **Bad-move tags** | MOVES_PINNED_PIECE, DID_NOT_RECAPTURE, IGNORES_ATTACKED_PIECE, HANGS_PIECE, HANGS_PAWN, LOSES_MATERIAL, BAD_TRADE_*, DOUBLES_PAWNS, ISOLATES_PAWN, NEVER_PLAY_F3, TOO_EARLY_QUEEN_DEVELOPMENT, MOVES_SAME_PIECE_IN_OPENING, PASSIVE_RETREAT, CASTLES_INTO_ATTACK |
| 268–277 | Evaluation transitions | WINNING_TO_EQUAL, BETTER_TO_LOSING, … |
| 278–281 | Fallbacks | PUNISH_MOVE_REFUTED_BY, PUZZLE_HINT_FALLBACK |

**Rating gates.** The embedded `rating_ranges` table (297 keys) holds a `MinRating` for each tag or
circumstance-and-tag. Some approximate values:

- 300–500: DoublesRooks, BishopGainsScope, Kicks, LosesCastlingRights.
- 550–650: WinsMaterial-Fork, Pin, RookOnSeventh, TakesOutpost, Permits-WinsMaterial-Fork.
- 700–900: the Brilliant sacrifice speech, Fianchetto, pawn-chain ideas, DevelopsWithTempo.
- 900–1100: backward, isolated and doubled-pawn structure, opposition, exchange sacrifices,
  Blockade.

So a beginner is told about hanging pieces and forks, and only stronger players hear about pawn
structure. We should copy this behaviour.

### 3.5 Prioritisation (Confirmed from disassembly)

`GameReviewPrioritizedBoardEvents::get` (`0x1416ab8`) returns at most a few events, in this order:

1. If the move was forced, say FORCED (or "forced into stalemate while winning").
2. If the move continues a forced mate, say so (FORCES → MAINTAINED_MATE).
3. If the game ended, give a GAME_OVER event.
4. Otherwise branch on `node_lib::is_bad_classification`:
   - **Good move → `add_good`** (`0x14163d4`). Take the first that exists:
     - BRILLIANT event (unless suppressed);
     - GREAT_FIND (behind a config flag);
     - MATE;
     - favourable queen trades;
     - FORCES → WINS_MATERIAL_NOT_FREE;
     - **wins material, or leads to winning material** (via the highest-priority tactic: "wins
       material with a fork");
     - THREATENS → MATE, or a sacrifice to stop mate;
     - PREVENTS → MATE;
     - CREATES_KING_FLIGHT_SQUARE;
     - think-time remarks;
     - any BASE event with a "good" move class;
     - otherwise any THREATENS, then any PREVENTS event.
   - **Bad move → `add_bad`** (`0x1416850`). GREAT_FIND first (flag), then two blocks whose order
     depends on the classification (the Miss subtypes put "misses" first):
     - **`add_permits_significant`** (`0x158df58`): PERMITS → MATE; then BASE MOVES_PINNED_PIECE,
       DID_NOT_RECAPTURE, IGNORES_ATTACKED_PIECE / _PAWN, REMOVES_OWN_DEFENDER, INFERIOR_TRADE,
       HANGS_PIECE, HANGS_PAWN; then **PERMITS → WINS_MATERIAL / LEADS_TO via the
       highest-priority tactic**; then time-trouble variants; then PERMITS FREE_PIECE and
       QUASI_FREE_PIECE.
     - **`add_misses_significant`** (`0x158dd28`): MISSES → MATE, a missed faster mate, a missed
       defence against mate; MISSES_SAME free piece (you missed the piece they just hung); MISSES →
       WINS_MATERIAL / LEADS_TO via a tactic; MISSES FREE_PIECE; time-trouble "missed critical".
     - Then a BASE event with a "bad" move class, Miss-specific extras (TAKES_OPPORTUNITY), any
       other MISSES or PERMITS event, then GAME_STATUS.
5. An ENDGAME remark is appended last when it applies.

Inside each slot, `get_highest_priority_core` walks the node's events with
`BoardEvents::for_each_in_tag_order` and takes the first valid one. `find_priority_override` /
`effective_priority_tag` handle a few overrides. Filters:

- `allow_board_event` drops an event the best-move speech already says
  (`includes_similar_board_event`).
- It also suppresses pawn-structure praise on recaptures.
- It checks static threats (`StaticAnalysis::see_threats_to`) before praising a piece's move.
- `is_high_frequency_board_event` limits repetitive events (WINS_MATERIAL, CRITICAL…).

What this tells us:

- **A bad move is explained first by what it allows** (the opponent's best reply and the tactic it
  enables), and only then by what was missed.
- **The tactic shown is the most forcing one on the line**, ranked by fixed priority: mate before
  free piece before fork before pin before positional points.
- **One main reason per move.** That matches the teaching advice in §5.4.

### 3.6 The text layer (Confirmed from the embedded English asset)

`libcee.so` embeds a "generic coach asset" for each of 12 locales (`embedded_generic_coach_asset_*`,
about 400–550 KB zlib each; English inflates to 3.55 MB of JSON). Coach personalities fetch
overrides from `https://text-and-audio.chess.com/text_prod/released/<coachTextId>/<locale>/cee_asset_v2.json.bzp`
(`SpeechAssetsRepositoryImpl`, Confirmed in the decompiled app). The asset has three parts:

- `speech_map`, with 32,005 entries:
  - 9,791 are keyed by FEN plus move (opening-specific remarks);
  - about 21,000 are tag sentences;
  - the rest are puzzles, bot chat, takeaways and UX strings.
- `rating_ranges`.
- `coach_bot_asset.triggers_metadata` (124 chat triggers, each with `tier` and `plyLimit`).

**Key grammar:** `[Circumstance-[ChildCircumstance-]]Tag[Piece]-Style-N`. Examples of the shapes:

- `HangsPieceKnight-Personal-1`;
- `WinsMaterial-ForkQueen-OpposingPersonal-2`;
- `Permits-WinsMaterial-Fork-PersonalCoach-1`;
- `LeadsTo-Pin-Explain-1`;
- the button labels `Fork-ShowPermits-1` and `Fork-HideBase-1`.

| Style | Use |
|---|---|
| Personal / OpposingPersonal | talking to the player about their own move / the opponent's move |
| Impersonal | neutral commentary |
| PersonalCoach / Self / Play | the play-with-coach voices |
| Explain | the per-move narration of `explain_line` |
| Punish | the opponent's refutation ("punish move") |
| Hint / PuzzleHint | hint ladder |
| ShowX / HideX | button labels per circumstance |
| Takeaway | end-of-game lessons |

Writing conventions:

- Sentences are short: median 10 words, 90th percentile 16.
- They are mostly generic ("you allow a fork that wins material"). The board arrows supply the
  concrete squares.
- `*word*` marks an emphasised or glossary term (in 3,890 entries).
- `%color%` and `%opposingcolor%` are the only placeholders.
- About 60% of keys have one wording; others have 2 to 20 variants. `SpeechUsageState` and
  `mark_label_as_used` avoid repeating one.
- Piece-specific variants exist for most tags (`ForkKnight`, `HangsPieceQueen`), and
  `replace_piece_name` fills the piece in otherwise.
- **Composition:** about 570 `InPlace<Tag><Piece>` entries are verb phrases ("attack a trapped
  bishop."). `build_inplace_prefix_key(circumstance, personality)` supplies the front part. So one
  verb phrase per tag covers every circumstance, which is how 32k entries cover the whole
  combination space.

### 3.7 Other coach features found

- **CHARM.** A neural human-move model (`assets/distilled_eakd_a07.bin.q8mix`, 12 MB, quantised).
  Its `CharmInferenceResult` gives, for a rating, move probabilities, expected points, a
  win/draw/loss split and time-taken distributions. It drives the Tricky classification and the
  game rating. It is the same idea as Maia-2 (§5.3).
- **Takeaways and report card.** Per-category end-of-game lessons
  (`TakeawayClassification`: BUILDING_STRENGTH, BE_AWARE, MAKING_PROGRESS, LEARNING_OPPORTUNITY),
  backed by counts such as FoundForks or AllowedFreePieces.
- **Play-coach.** `generate_hint_speech`, `generate_retry_mistake_offer`,
  `generate_retry_miss_offer` and `generate_flip_board_mistake_offer` build hints that point at the
  key piece first, then name the motif, then give the move. Retry offers follow mistakes and misses.
- **Punish move.** `generate_punish_move_speech` explains the opponent's refuting reply:
  PUNISH_MOVE_REFUTED_BY, or a fallback.

## 4. Gap analysis: our app against the recovered system

| Capability | Chess.com | Us today |
|---|---|---|
| Classification | yes | yes; we match about 70% of labels (see `docs/calibration/log.md`) |
| Engine lines | yes | yes, MultiPV per position |
| Opponent's refutation line | used for "permits" | **computed** (the next position's PV) **but never explained** |
| Best-alternative line | used for "misses" | computed, shown as raw moves only |
| Threat search (null move) | THREATENS / PREVENTS | **missing** |
| Tactic detectors | ~280 tags | only material-on-line, SEE, sacrifice and recapture helpers in `detectors.rs` |
| Choosing one reason | prioritiser | none: all facts are listed |
| Text | 32k entries, styles, rating gates, piece variants | about 15 fixed sentences by classification |
| Arrows tied to sentences | yes, per fragment | best-move arrow only |
| "Show the line" with per-move narration | yes | line preview without words |
| Rating adaptivity | rating gates, CHARM | no |
| Retry / hints | yes | Retry exists, without hints |

Most of the raw material is already there: we search every position with MultiPV, so the
opponent's best reply and the best alternative are available for every move. What is missing is
the layer that turns lines into named, prioritised events.

## 5. What the research adds

Full notes with all sources are in [`coach-research-notes.md`](coach-research-notes.md); items it
could not confirm are marked [UNVERIFIED] there. Highlights, with the key ones checked against the
primary source:

1. **Analysis first, language second.**
   - Take Take Take (Magnus Carlsen's app) described its coach at AI Engineer Europe 2026 (talk page
     checked). The pipeline is Stockfish, tactical and positional detectors, Maia, a JSON fact
     list, and then Gemini 3 Flash only *verbalises* (about 3 s). They test it on 16 scenarios with
     an LLM judge that checks the supplied facts were used.
   - "Hallucinations on the Board" (Hebbar et al., arXiv 2608.04240, Aug 2026, checked) found
     GPT-5.4 makes wrong sub-claims 22% of the time without tools. Smaller open models are above
     40%.
   - The concept-guided commentary paper (Kim et al., NAACL 2025) reports that feeding detected
     concepts and the list of existing attacks to GPT-4o cut references to illegal moves or absent
     pieces from 0.46 to 0.20, and tactical errors from 0.46 to 0.26. Positional errors did not
     improve.

   **Conclusion:** an LLM is optional polish. It must never be the source of chess facts.
2. **Tactic detectors.**
   - The lichess puzzle tagger (`lichess-puzzler/tagger/cook.py`, **AGPL-3.0**) is the best open
     reference. It covers fork, pin, skewer, discovered attack, double check, hanging piece, trapped
     piece, attraction, deflection, interference, intermezzo, capturing the defender, clearance,
     quiet move, x-ray, and about 10 named mates.
   - It runs on a forcing line, which is exactly our refutation PV or best-move PV.
   - We should **reimplement** it from its description, not port its code.
   - The **lichess puzzle database is CC0**: 5M+ positions with theme labels, a free test set for
     our detectors.
3. **Rating awareness.**
   - **Maia-2** (NeurIPS 2024, **MIT**) gives P(move | rating). It separates "the best move was
     hard to find at your level" from "this natural-looking move loses".
   - Maia-3 exists but is AGPL.
4. **Teaching.**
   - Give one main reason, name the motif *and* show the concrete line. Motif names alone barely
     help (Cui et al. 2026).
   - Frame blunders as a missed safety check of the opponent's checks, captures and threats
     (Heisman).
   - Be more directive for beginners (Shute 2008).
   - End with a habit to carry forward (Hattie and Timperley 2007).
   - Retry with self-explanation beats watching (de Bruin et al. 2007).
   - Use a hint ladder: point to the area, then name the motif, then give the move.
   - Don't over-flag: about 3–6 key moments per game.
   - Measure learning (retry success, the same motif error recurring), not satisfaction.
5. **Positional explanations.**
   - Stockfish's old classical evaluation terms (mobility, king safety, threats, passed pawns,
     space, outposts, bad bishop, weak pawns) are the accepted positional vocabulary.
   - Stockfish 16+ no longer computes them, so we would compute a subset ourselves in Rust.

## 6. Proposed design

### 6.1 Principles

- **Facts come from code; words come from templates.** Every sentence is backed by an event with
  a geometry (pieces and squares) and, where relevant, a line that proves it.
- **One reason per move, chosen by a fixed priority**, as Chess.com does. Supporting detail sits
  behind "Show line".
- **Explain bad moves by what they allow first**, then by what was better.
- **Be concrete.** Unlike Chess.com, our sentences name the squares and moves. They can, because
  we generate them from facts, and research says concrete lines teach better than motif names.
- **Adapt to the player's rating**: hide concepts above their level, and soften "missed" remarks
  when the idea was hard to find.

### 6.2 Pipeline

```
           already have                                       new
┌────────────────────────────┐   ┌───────────────────────────────────────────────────────────┐
│ Stockfish: every position, │   │ 1. Position facts   attacks/defenders, SEE, pins, x-rays, │
│ MultiPV, PVs, evals        │──▶│    (per position)   hanging & trapped pieces, king zone,  │
│ classification, EP, CAPS2  │   │                     pawn structure, development           │
└────────────────────────────┘   │ 2. Threat search    null-move search (new engine call)    │
                                 │ 3. Base detectors   tag events for one move in one pos.   │
                                 │ 4. Circumstances    BASE / THREATENS / PREVENTS / PERMITS │
                                 │                     / MISSES / LEADS_TO / WINS_MATERIAL   │
                                 │ 5. Prioritiser      pick 1 main + ≤1 supporting event     │
                                 │ 6. Realiser         templates → sentences + arrows        │
                                 │ 7. Show-lines       refutation / best line, per-move text │
                                 └───────────────────────────────────────────────────────────┘
```

**New module:** `backend/crates/review-server/src/coach/`, with `facts.rs`, `detect/`, `circ.rs`,
`priority.rs`, `realise.rs` and `text/en.toml`. It stays pure, like `review-core`, so it is
unit-testable without an engine.

**Game-tree nodes per played move** (all but one already computed):

| Node | Source |
|---|---|
| P: the played move, in the position before it | the game |
| R: the opponent's best reply to P, with its PV | the next position's engine line #1 (have) |
| B: the best alternative, with its PV | this position's engine line #1 (have) |
| B2: the second-best alternative | engine line #2 (have) |
| N: the null-move threat after P (and before P, for PREVENTS) | **new:** a shallow search (depth 10–12, MultiPV 1) on the position with the side to move flipped. Skip it when in check. Costs about +25–35% engine time; can run only for plies whose class is not Best or Book. |

### 6.3 Event model (Rust, serialised to the frontend via ts-rs)

```rust
pub enum Circ { Base, Threatens, Prevents, Permits, Misses, MissesSame, LeadsTo, WinsMaterial,
                Forces, Mate, GameOver }
pub struct Event {
    pub chain: Vec<Circ>,          // e.g. [Permits, WinsMaterial]
    pub tag: Tag,                  // our own enum; declaration order = priority
    pub piece: Option<Role>,       // the piece in focus, for "…your knight"
    pub actor: Side,               // whose idea it is
    pub geometry: Geometry,        // Fan{src,targets} | XRay{attacker,front,behind} | Relation{from,to,kind} | Squares{..}
    pub line: Option<Vec<String>>, // UCI moves that demonstrate it (from R or B PV)
    pub gain_cp: i32,              // material at stake along the line
}
pub struct CoachNote {
    pub sentences: Vec<Sentence>,  // each: Vec<Fragment{ text, arrows, squares }>
    pub emotion: CoachEmotion,
    pub show_lines: Vec<ShowLine>, // { label: "Show the fork", moves: [MoveRef], narration: [String] }
    pub events: Vec<Event>,        // all detected events, for the debug view and tests
}
```

`PlyReview.explanation: Vec<String>` becomes `PlyReview.coach: CoachNote`. The old factual
sentences can stay in a "details" drawer.

### 6.4 Tag set for version 1 (our own vocabulary, in priority order)

Start with the tags that explain most blunders and misses. The lichess and Chess.com evidence
agrees on these:

1. **Mates:** `Checkmate`, `MateThreat`, `AllowsMate`, `BackRankMate`, `MissedMate`.
2. **Free material:** `HangsPiece`, `HangsPawn`, `FreePiece` (captures an undefended or
   under-defended piece, judged by SEE), `TrappedPiece`.
3. **Double attacks:** `Fork` (and royal fork), `DoubleCheck`, `DiscoveredAttack`,
   `DiscoveredCheck`.
4. **Line tactics:** `Pin` (absolute or relative), `ExploitsPin` (attacking or capturing a pinned
   piece), `Skewer`.
5. **Defender tactics:** `RemovesDefender`, `Overloaded` (deflection), `Attraction`.
6. **Promotion:** `Promotion`, `UnstoppablePawn`.
7. **Bad-move bases:** `MovesPinnedPiece`, `IgnoresThreat` (a threatened piece was left
   attacked), `DidNotRecapture`, `RemovesOwnDefender`, `BadTrade` (by SEE), `LosesCastling`.
8. **Defence:** `DefendsPiece`, `EscapesThreat`, `BlocksCheck`, `CounterThreat`.
9. **Development and structure** (version 2): `Develops`, `Castles`, `TakesOpenFile`,
   `RookOnSeventh`, `Outpost`, `DoubledPawns`, `IsolatedPawn`, `PassedPawn`, `EarlyQueen`,
   `MovesPieceTwice`. All are rating-gated.

Detector notes:

- Fork, pin, skewer and discovered attack are evaluated on the **first move of a line** (for
  BASE), and on the move inside a PV where material is won (for LEADS_TO and WINS_MATERIAL).
  `walk_line` already finds the material swing; extend it to report the ply where the gain starts.
- "Hanging" uses the existing SEE (`see.rs`): attacked, and SEE for the opponent > 0.
- "Trapped": every legal move of the piece lands on a square where SEE is lost. This is the lichess
  definition.

### 6.5 Prioritiser (adapting §3.5)

```
if forced                        → Forced
if continues/creates mate        → Mate events
bad move (Inaccuracy…Blunder, Miss):
    if Miss: Misses block first, else Permits block first
    Permits block:  Permits→Mate › bad BASE tags (HangsPiece, MovesPinnedPiece, IgnoresThreat…)
                    › Permits→WinsMaterial/LeadsTo via the highest-priority tactic in R's PV
    Misses block:   Misses→Mate › MissesSame free piece › Misses→WinsMaterial/LeadsTo via tactic in B's PV
good move:
    Brilliant/Great › Mate › WinsMaterial/LeadsTo via tactic › Threatens→Mate › Prevents→Mate
    › good BASE tag › Threatens › Prevents
then: drop events already said for the best move; drop tags above the player's rating gate
```

### 6.6 Realiser and text

- **Our own corpus** in `text/en.toml`, keyed like `[permits.wins_material.fork]` with the styles
  `you`, `opponent` and `neutral`. Each entry has 2–3 variants and a `min_rating`.
- **Composition:** a circumstance prefix plus a tag verb phrase. This keeps the corpus small:
  about 60 tags × 1–3 phrases, plus about 10 prefixes × 3 styles.
- **Placeholders** resolved from the event: `{piece}`, `{square}`, `{targets}` ("your queen and
  rook"), `{move}` (SAN), `{gain}` ("a knight"), `{opponent}`.
- **Fragments.** The fragment naming a piece or square carries that event's arrows, so hovering or
  tapping it highlights the board (the Chess.com interaction).
- **Sentence plan for a blunder:**
  1. **What happens:** "Nf6 allows Bxf6, and after …gxf6 your king is exposed."
  2. **Why** (motif plus geometry): "The bishop on g5 pins the knight to your queen."
  3. **What was better** (best alternative's event): "…h6 first would have kicked the bishop."
  4. *(optional, rating-gated)* **Habit:** "Before moving a pinned piece's neighbours, check what
     the pin holds."
- **Show-line buttons** come from the event's `line`. Each move gets a short narration from the
  detectors run on that ply ("Bxf6: removes the defender", "…gxf6: forced recapture", "Qg4+:
  forks king and rook").

### 6.7 Rating and difficulty (version 2)

- **Rating gates** on tags, as in §3.4.
- **Maia-2 (MIT)**, served as ONNX through `ort` in the Rust backend, or as a small Python sidecar:
  - P(best move | rating) low means "a hard move to find at your level", and the Miss text is
    softened.
  - P(played move | rating) high and the move is a blunder means "a natural-looking move, but…".
    Lead with the safety check.
  - It can also replace the current Tricky and Great Find heuristics.

### 6.8 Frontend

- `Coach.tsx`:
  - render `sentences[].fragments`, with tap/hover wired to board arrows and squares;
  - add a Show/Hide button per `show_line`, which steps through the line and shows the narration
    under the board;
  - set the avatar expression from `emotion`.
- Retry mode gets a hint ladder (area, then motif, then move) built from the same events. Accept any
  move within about 0.04 winning chance of the best, as lichess does.
- End of game: 2–4 takeaways aggregated from events, such as "you allowed 3 forks", each linking to
  its moves.

### 6.9 Optional LLM layer (later, behind a flag)

Pass a JSON fact contract (the event list, SAN lines, side, rating) to an LLM with an instruction
to only rephrase. Then **verify** the output:

- every square, piece and move it mentions must appear in the facts;
- SAN must be legal.

If verification fails, fall back to the template. This follows Take Take Take and CCC. Only worth
doing after the template coach is good, and it adds a runtime dependency and cost per review.

## 7. Plan

| Phase | Scope | Rough effort | Outcome |
|---|---|---|---|
| 0. Measurement | Extend the Chess.com capture protocol to record `speech`, `show_moves_buttons` and `board_markings` for the 59 calibration games. Build a local tool that maps each captured sentence back to its (circumstance, tag, piece, style) key through the decoded `speech_map`. It stays local and is never committed. | 2–3 days | Ground-truth event labels for about 4,000 plies |
| 1. Bad-move coach | `facts.rs`, detectors for tags 1–7 in §6.4, Permits/Misses/LeadsTo/WinsMaterial over R and B lines, prioritiser for bad moves, about 40 templates, `CoachNote` API | 2–3 weeks | Every Inaccuracy, Mistake, Blunder and Miss explained by motif plus line |
| 2. Threats and good moves | Null-move search; Threatens and Prevents; good-move path; defence tags; arrows per fragment; Show-line narration | 2 weeks | Brilliant, Great and Best moves get reasons; "you stopped their threat" |
| 3. UI | Fragment highlighting, Show/Hide lines, avatar emotion, hint ladder in Retry, takeaways | 1–2 weeks | The Chess.com coach experience, with concrete moves |
| 4. Positional and rating | Development and structure tags with rating gates; Maia-2 difficulty; habit sentences | 2–3 weeks | Rating-appropriate advice beyond tactics |
| 5. Optional LLM verbaliser | Fact contract, verifier, fallback | 1 week | More natural wording |

## 8. How to judge the coach

1. **Detector accuracy.**
   - Run the detectors on lichess puzzles (CC0, theme-labelled) with the solution line as the PV.
     Report precision and recall per theme. Target ≥ 0.9 precision on fork, pin, skewer and
     hanging piece before the text uses them.
   - Add unit tests with hand-built positions per tag, in the style of the existing
     `tests/brilliant.rs`.
2. **Agreement with Chess.com on what to say.** For the captured calibration games (Phase 0),
   compare our chosen main event (tag and circumstance) with theirs per ply. Report:
   - exact match;
   - same tag with a different circumstance;
   - different tag in the same family (tactic, material, positional);
   - and inspect the disagreements by hand. The same approach `docs/calibration/` uses for labels.
3. **Fact checking** (built: `coach/verify.rs`, see `implementation-notes.md`). An automatic
   verifier checks that every square, piece and SAN in a generated sentence exists in the position
   or line. This mirrors the ACT-Eval rules, such as using the pre-move position for "was" claims
   and the post-move position for "creates".
4. **Usefulness.** A small rubric (correct / relevant / specific / actionable) on about 100 sampled
   moves across 600–2000 ratings. Later, learning metrics: retry success, and whether the same motif
   error recurs in later games.

## 9. Legal and IP notes

- We reuse **ideas and architecture**: an event model, circumstances, priority-ordered selection,
  rating gates and composed templates. Those are not protected expression.
- We must not ship Chess.com's **text**:
  - none of the 32k coach sentences;
  - no opening remarks, bot chat or button labels;
  - not their embedded books or models.

  Our corpus must be written from scratch. Their tag *names* are generic chess terms; we keep our
  own enum and wording anyway.
- Using their decoded asset as a local **evaluation oracle** (Phase 0) is comparable to the label
  calibration this project already does. Keep it out of the repository and out of the build.
  [`THIRD_PARTY.md`](../THIRD_PARTY.md) already states that no data from the reference app is
  included, and that must stay true.
- `lichess-puzzler` and Maia-3 are AGPL-3.0. Our project is GPL-3.0-or-later; GPLv3 §13 permits
  combining with AGPLv3 code, but that would bring network-use obligations. Reimplement from the
  described behaviour instead.
- Maia-2 (MIT) and the lichess puzzle data (CC0) can be used directly. Add them to
  `THIRD_PARTY.md` if adopted.
- Don't call Chess.com's servers from the product.

## 10. Open questions

- **Exact detector definitions.** The 282 `compute_base_event<Tag>` bodies were not decoded one by
  one. We define ours from chess semantics and the lichess tagger, then calibrate against the Phase 0
  labels. Decoding specific ones (e.g. `FORK`, `HANGS_PIECE`) remains possible with the same Ghidra
  workflow if a disagreement needs it.
- **Null-move search depth.** Chess.com's search depth for the threat search is unknown. Start with
  depth 10–12 and measure the cost.
- **Number of sentences.** The first event usually yields one or two sentences. Chess.com appends
  an ENDGAME remark and sometimes a second event. Start with one main event plus the best-move
  sentence.
