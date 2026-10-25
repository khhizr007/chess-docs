# Coach log: agreement with Chess.com's coach (Phase 0)

This is Phase 0 of [`coach-analysis.md`](../coach-analysis.md) (§7 row 0, §8 item 2). It asks, per
ply, whether our coach picks the same explanation as Chess.com's coach: the same board-event tag in
the same circumstance. The label calibration in [`log.md`](log.md) asks the same question about
move labels.

**No Chess.com text is in this repository.** The captured speech and the decoded text asset stay in
WSL under `~/work/chesscom/oracle/` (see [`THIRD_PARTY.md`](../../THIRD_PARTY.md)). The comparison
reads tag and circumstance names only, which are generic chess terms. The descriptions below are
our own paraphrases.

## Runs

| date | measured commit | games | plies | engine (ours / theirs) | report |
|---|---|---:|---:|---|---|
| 2026-10-20 | `f5f0b35` (main, phase 1 coach) | 142 | 8,638 | Stockfish 18 depth 18 MultiPV 3 / Stockfish 18 (CEE 1.198.16) | [`runs/coach-phase0/coach-report.md`](../../tests/calibration/runs/coach-phase0/coach-report.md) |
| 2026-10-20 | `e4ead28` (main, phases 1–3) | 142 | 8,638 | same | [`runs/coach-main-e4ead28/coach-report.md`](../../tests/calibration/runs/coach-main-e4ead28/coach-report.md) |
| 2026-10-20 | `cb1b475` (quick fixes of `coach-gap-analysis.md` §4.1) | 142 | 8,638 | same | [`runs/coach-quickfix/coach-report.md`](../../tests/calibration/runs/coach-quickfix/coach-report.md) |
| 2026-10-20 | `14186c4` (quick fixes + Phase 2b) | 142 | 8,638 | same | [`runs/coach-phase2b/coach-report.md`](../../tests/calibration/runs/coach-phase2b/coach-report.md) |
| 2026-10-20 | `118a076` (Phase 4) | 142 | 8,638 | same | [`runs/coach-phase4/coach-report.md`](../../tests/calibration/runs/coach-phase4/coach-report.md) |
| 2026-10-21 | `0a8971a` (detector fixes from the lichess puzzle check) | 142 | 8,638 | same | [`runs/coach-detector-check/coach-report.md`](../../tests/calibration/runs/coach-detector-check/coach-report.md) |

The quick fixes alone were measured twice in run `coach-quickfix`: a first pass at `d25b1b7`
(29.0%, the figure quoted in "Results: Phase 2b") and the committed run at `cb1b475`, which adds the
taken-back rule (29.6%). Both are without Phase 2b.

The second run adds:

- good moves and the best-move sentence to the report;
- the Phase 2 tags to the mapping.

Its results and the remaining gaps are analysed in [`coach-gap-analysis.md`](../coach-gap-analysis.md).

Repeat with the same commands (below) and a new run name. The captures do not need to be taken
again.

## Method

### 1. Capture (local only)

- The review page receives the whole review from `/v2/game-review` as one `GameReview` message
  ([`chesscom-review-protocol.md`](chesscom-review-protocol.md)). Per ply it holds the played
  move's speech (sentences of fragments, each with its arrows and squares), the best alternative's
  speech, the show-moves buttons and the board markings.
- [`tools/calibrate/coach_capture.js`](../../tools/calibrate/coach_capture.js) runs on a signed-in
  analysis page. It opens each game's review page in a hidden same-origin iframe, wraps that frame's
  `WebSocket` before the app starts, and keeps the request and the response frames. Games are
  opened one at a time with a 3 s pause. Nothing is sent beyond what opening the review page sends.
- The account's Game Review engine must be **Stockfish**. This profile had Torch (the site default)
  and was switched with the owner's permission. The first two captures came back from Torch and
  were discarded. Every kept capture asks for engine 10, and all its scores come from engine 13
  (Stockfish 18).
- The browser pane blocks requests from chess.com to localhost. So `coachPull()` returns the frames
  as the tool result, which is saved to disk. `coach_oracle.py ingest` splits it into
  `captures/raw/<id>.json`.
- Coverage: **all 142 calibration games** (99 tuning + 43 holdout, the 59 of batches 1–3 included).
  2 games timed out on the first pass and were captured on a retry. As a sanity check, the decoded
  labels equal the earlier `cc-reviews/*.sf.txt` captures on 8,636 of 8,638 plies, and every move
  matches.

### 2. Sentences to keys

[`tools/calibrate/coach_oracle.py`](../../tools/calibrate/coach_oracle.py) runs `decode`, then
`match`.

**`decode`** reads the frames with a small protobuf wire decoder. The field numbers come from the
recovered schemas.

**`match`** maps each sentence to the key it came from in the embedded English asset
(`[Circumstance-[Child-]]Tag[Piece]-Style-N`):

- **Normalisation:** emphasis marks removed, quotes unified, case and final punctuation ignored, and
  the colour placeholders filled both ways. Where needed, piece names are generalised to "piece".
- **full:** the whole sentence equals an asset entry. When several keys share the text, the
  highest-priority tag wins and the record is marked ambiguous.
- **composed:** the sentence ends with an `InPlace<Tag><Piece>` verb phrase. The rest is a
  circumstance prefix, read with generic keyword rules:
  - miss / best / better / opportunity → Misses;
  - allow / permit / chance / able → Permits;
  - threat → Threatens;
  - force → Forces;
  - prevent / stop → Prevents.
- **pattern:** the live asset (CEE 1.198.16) is newer than the embedded one (app 4.10.15), so some
  verb phrases have no key. For these, a short list of generic chess words picks the tag, for example
  threaten plus capture → CaptureThreat, trapping → AttacksTrappedPiece and danger → EscapesThreat.

The output is `captures/<id>.keys.json`: keys and parsed tags only. Coverage on 142 games:

| speech | sentences | full key | composed | pattern | unmatched |
|---|---:|---:|---:|---:|---:|
| played move | 9,150 | 78.3% | 15.0% | 4.8% | 1.9% |
| best alternative | 3,718 | 95.5% | 1.8% | 1.6% | 1.1% |

The unmatched sentences are mostly encouragement, evaluation-swing remarks and opening comments for
positions the embedded asset does not have.

**Their main event** is the first sentence of the played move's speech that names a board event. The
following are skipped:

- classification remarks (keys `<Class>-Classification`);
- opening remarks (FEN-keyed);
- "only good move" framing (`Critical`), unless nothing else is said.

### 3. Our tags to theirs

[`tools/calibrate/coach_tags.py`](../../tools/calibrate/coach_tags.py) maps each of our `Tag`s to
the Chess.com tag names that say the same thing, and to a family:

- the nine families of §6.4 of `coach-analysis.md`;
- plus sacrifice, trade, evaluation, game and other, for Chess.com tags we have no counterpart for.

Chess.com tags that we do not have get a family by hand, or else from their priority range.

| our tag | family | Chess.com tags counted as the same |
|---|---|---|
| `back_rank_mate` | mate | BackRankMate |
| `checkmate` | mate | Checkmate, LadderMate, KingQueenMate, KingRookMate, DoubleCheckMate, StillMate, BackRankMate |
| `forced_mate` | mate | ForcesMate, MateThreat, MaintainedMate, NmpMateInXThreat, SlowerMate, KeymomentGoodFasterMate, KeymomentBadFasterMate |
| `free_piece` | free material | FreePiece, FreePieceFromDistance, QuasiFreePiece |
| `trapped_piece` | free material | AttacksTrappedPiece |
| `double_check` | double attack | DoubleCheck |
| `royal_fork` | double attack | RoyalFork, Fork, ForkWithMate |
| `fork` | double attack | Fork, ForkWithMate, PseudoFork, MultiAttack, RoyalFork |
| `discovered_check` | double attack | DiscoveredCheck, DiscoveredCheckAttack, DiscoveredAttackCheck, DiscoveredCheckCapture |
| `discovered_attack` | double attack | DiscoveredAttack, DiscoveredAttackCapture, DiscoveredAttackCheck, DiscoveredCheckAttack |
| `skewer` | line tactic | Skewer |
| `exploits_pin` | line tactic | ExploitsPinnedDefender, ThreatensPinned, PressuresPinnedPiece |
| `pin` | line tactic | Pin, RelativePin, PinsDefender, PinsAttacker |
| `removes_defender` | defender tactic | RemovesDefender, CapturesMateDefender, RemovesMateDefender, KicksDefender, KicksMateDefender, ChecksAwayDefender |
| `overloaded` | defender tactic | ExploitsOverloadedDefender |
| `attraction` | defender tactic | Attraction, Decoy |
| `promotion` | promotion | Promotion, Underpromotion |
| `moves_pinned_piece` | bad-move base | MovesPinnedPiece |
| `did_not_recapture` | bad-move base | DidNotRecapture |
| `ignores_threat` | bad-move base | IgnoresAttackedPiece, IgnoresAttackedPawn |
| `removes_own_defender` | bad-move base | RemovesOwnDefender |
| `bad_trade` | bad-move base | InferiorTrade, BadTrade, BadCaptureChoice |
| `hangs_piece` | bad-move base | HangsPiece |
| `hangs_pawn` | bad-move base | HangsPawn |
| `material_gain` | free material | WinsMaterial, WinsMaterialNotFree, LosesMaterial, PickUpPieceInTactic, Loses/MissesMaterial{Losing,Winning}Position |

**Circumstances.** Ours map one to one: BASE is the empty chain, and MISSES_SAME counts as MISSES.
Two normalisations make chains comparable:

- Chess.com's `LosesMaterial` is said about the move itself, but it means "allows winning material
  through no named tactic", so it counts as PERMITS.
- A step the tag already implies is dropped on both sides: "wins material" for free and trapped
  pieces; "wins material" and "leads to" for the bare material tags.

### 4. Our review and the comparison

- **Our review:** `compare.py` on all 142 games, run `coach-phase0` (Stockfish 18, depth 18,
  MultiPV 3, default rules).
- **Label agreement:** 68.7% exact and 88.7% within one step, in line with `log.md`.
- **The comparison:**
  [`tools/calibrate/coach_compare.py`](../../tools/calibrate/coach_compare.py) aligns plies by index,
  checks every UCI move and puts each ply into one category:
  - exact (tag and chain);
  - same tag, other circumstance;
  - same family;
  - different;
  - they explain and we don't, we explain and they don't, or neither.

```
# WSL; ~/work/chesscom/oracle holds coach_en_us.raw, tag_names.txt and captures/
python3 tools/calibrate/compare.py --url http://127.0.0.1:8095 --run-name <run> --games <all ids>
python3 tools/calibrate/coach_oracle.py decode
python3 tools/calibrate/coach_oracle.py match --report
python3 tools/calibrate/coach_compare.py --run tests/calibration/runs/<run> \
    --out tests/calibration/runs/<run>/coach-report.md
```

## Results (`f5f0b35`, 142 games)

Phase 1 explains only bad moves, so the headline is the 1,988 plies that Chess.com labels
Inaccuracy, Mistake, Blunder or Miss.

| category | all 1,988 bad plies | 1,641 plies both apps label bad |
|---|---:|---:|
| exact | 376 (18.9%) | 376 (22.9%) |
| same tag, other circumstance | 19 (1.0%) | 19 (1.2%) |
| same family | 76 (3.8%) | 76 (4.6%) |
| different | 687 (34.6%) | 687 (41.9%) |
| they explain, we don't | 644 (32.4%) | 351 (21.4%) |
| we explain, they don't | 81 (4.1%) | 81 (4.9%) |
| neither | 105 (5.3%) | 51 (3.1%) |

Where both name an event (1,158 plies):

- **32.5%** are exact;
- **34.1%** have the same tag;
- **40.7%** are in the same family or better.

Of the 347 bad plies we do not label bad, 245 are our Good and 65 our Excellent. The label
calibration covers those.

**By Chess.com classification (all 1,988 bad plies).** Bigger mistakes agree better, because they
are explained by material and Phase 1 is about material:

| class | plies | exact | same tag, other circ. | same family | different | they only | we only | neither |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Inaccuracy | 825 | 7.0% | 0.5% | 2.1% | 24.5% | 49.9% | 5.0% | 11.0% |
| Mistake | 616 | 18.5% | 0.2% | 4.7% | 41.6% | 28.4% | 4.5% | 2.1% |
| Blunder | 228 | 46.5% | 1.8% | 6.1% | 41.7% | 2.6% | 1.3% | 0.0% |
| Miss | 319 | 30.7% | 3.1% | 5.0% | 42.0% | 16.0% | 2.8% | 0.3% |

**By phase.** Agreement is lowest in the opening (14.6% exact):

- Chess.com explains 43% of the opening's bad moves with something we say nothing about;
- its most common family there is positional (development and structure, 164 of 602 plies), which
  we do not have yet.

| phase | plies | exact | same tag, other circ. | same family | different | they only | we only | neither |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| opening | 602 | 14.6% | 0.2% | 2.7% | 29.7% | 43.2% | 3.7% | 6.0% |
| middlegame | 921 | 21.7% | 1.0% | 5.1% | 36.9% | 27.5% | 3.9% | 3.9% |
| endgame | 465 | 18.9% | 1.9% | 2.8% | 36.1% | 28.2% | 4.9% | 7.1% |

**Good moves.** Chess.com explains:

- 89% of its Best moves;
- 82% of its Excellent moves;
- 79% of its Good moves;
- every Great, Forced and (bar one) Brilliant move.

We explain none of them: Phase 2 adds good moves.

**What Chess.com says about bad moves.** Its main events, by family:

| family | share |
|---|---:|
| bad-move base | 18.8% |
| positional | 17.3% |
| defence | 17.0% |
| free material | 11.0% |
| nothing matched | 9.4% |
| double attack | 6.8% |
| mate | 5.9% |
| trade | 3.4% |
| line tactic | 3.2% |
| other | rest |

Its most frequent main events are:

- PERMITS LosesMaterial (235);
- MISSES CaptureThreat (206);
- PERMITS FreePiece (97);
- MISSES FreePiece (89);
- PERMITS WinsMaterial Fork (50);
- PERMITS ForcesMate (49);
- HangsPiece (48).

On the plies both apps label bad, **44% (719) of Chess.com's main events are about what the best
move would have done (MISSES)**. Most of them are not about material:

| family of those MISSES events | plies |
|---|---:|
| defence | 247 |
| positional | 155 |
| free material | 89 |

### Top 5 actionable disagreements

These are counted on the 1,641 plies both apps label bad. The full pattern table, with ply
references, is in the report.

1. **A piece left en prise is "allowed free piece", not "ignored the threat".**
   - *Counts:* 56 plies where Chess.com says PERMITS FreePiece and we say `ignores_threat` (we
     detected their event on 55). Another 22 where it says PERMITS LosesMaterial (the piece is lost
     to an exchange) and we say `ignores_threat`.
   - *Also:* 13 more where a capture gives up the capturing piece. It says PERMITS FreePiece and we
     say `bad_trade`.
   - *Ratio:* across all 1,988 bad plies, Chess.com leads with IgnoresAttackedPiece/Pawn 18 times;
     we lead with `ignores_threat` 142 times.
   - *Fix:* in `priority.rs`, drop `ignores_threat` and `bad_trade` below the PERMITS free-piece
     event, or keep them only when the piece is lost to an exchange and then word it as losing
     material. Examples: 1041474766 12...Nxd5, 142873206408 12...O-O-O, 142849919300 7...Nxd5.
   - *Potential:* about +4 points of exact agreement.
2. **Missed defensive and threat ideas are not explained.**
   - *Counts:* Chess.com explains a bad move through the best move's threat to capture 155 times
     (MISSES CaptureThreat). Other frequent ideas are defending a piece, stepping out of an attack,
     answering a check, retreating or recapturing (MISSES DefendsPiece / EscapesThreat / EvadesCheck
     / ObviousRetreat / ObviousRecapture, about 100 more across all bad plies). On the first kind
     alone, we say nothing on 71 plies and name some material gain instead on 17.
   - *Why:* our MISSES only looks for material or mate on B's line.
   - *Fix:* Phase 2, with static threat and defence detectors on the best move. Examples:
     1011026868 9...b5, 142873206408 6.a3, 145833178628 3...Bc5.
3. **We name a tactic where Chess.com just says "loses material".**
   - *Counts:* PERMITS LosesMaterial is Chess.com's most frequent bad-move event (195 plies both
     label bad). On 81 of them we name a tactic in the reply line instead: fork 25,
     `removes_defender` 15, `discovered_attack` 9, `forced_mate` 7, `pin` 7, `skewer` 6,
     `exploits_pin` 6.
   - *Ratio:* across all bad plies, our main event is `removes_defender`, `pin` or `exploits_pin`
     183 times, while Chess.com's line and defender tactics together come to 86.
   - *Fix:* name a tactic only when it is the reply itself or a short forcing line. Otherwise fall
     back to `material_gain`, worded as losing material. Tighten Fork (targets each worth more than
     the forker, or undefended). Examples: 147786569400 19...Nf6, 168426135116 15.Bxf6,
     184110410320 15.Kb1.
4. **Hanging the moved piece loses to the PERMITS free-piece event.**
   - *Counts:* 8 plies where Chess.com says HangsPiece and we detect `hangs_piece`, but we say
     PERMITS FreePiece.
   - *Likely cause:* the "base outweighed" filter in `select_bad` compares the reply line's whole
     gain (which includes later material) with the base event's stake.
   - *Fix:* keep the base event when the PERMITS event wins that same piece. Examples:
     142849698970 18...Qg5+, 165327199736 19.Qc2.
5. **A mate further away is "forces mate", not a named pattern.**
   - *Counts:* 12 plies where Chess.com says PERMITS ForcesMate and we name `back_rank_mate`. A
     further 7 where we announce `forced_mate` and Chess.com says LosesMaterial, apparently for long
     mates.
   - *Fix:* name the mate pattern only for the mating move itself. Measure whether a mate-distance
     cap applies before mates are announced. Examples: 166096155098 13...Bh3, 167316688806
     22...Rfxb8.

**Next:**

- Opening and structure explanations are Phase 4 work:
  - moving the same piece twice (19);
  - central development (24);
  - castling (18);
  - early queen moves;
  - pawn moves in front of the king (15);
  - evaluation-swing remarks (18).
- 81 plies are explained only by us. On those, Chess.com's speech is generic or unmatched.

## Results (`cb1b475`, quick fixes, 142 games)

Run `coach-quickfix` measures the quick fixes of
[`coach-gap-analysis.md`](../coach-gap-analysis.md) §4.1 (B2, B3, B7, B8 and the forced-move
sentence). Labels are unchanged (68.7% exact). The commands are the ones above, with the server on
port 8097.

| plies both apps label bad (1,641) | `e4ead28` | `cb1b475` |
|---|---:|---:|
| exact | 371 (22.6%) | **485 (29.6%)** |
| … tuning games (1,106) | 22.9% | 29.3% |
| … holdout games (535) | 22.1% | 30.1% |
| same tag, other circumstance | 34 | 43 |
| same family | 78 | 49 |
| different | 725 | 629 |
| they explain, we don't | 301 | 303 |
| we explain, they don't | 86 | 86 |
| neither | 46 | 46 |

Where both explain, 35.5% are exact (was 32.5% in Phase 0). Good moves (23.4%, was 23.1%) and the
best-move sentence (12.1%, was 11.9%) did not regress.

**What moved** (ply counts from the per-ply records):

- **B2** gains the most: 55 plies of `ignores_threat` and 13 of `bad_trade` are now Chess.com's
  PERMITS FreePiece. 9 plies where Chess.com said IgnoresAttackedPiece/Pawn are lost.
- **B7:** 12 plies of `back_rank_mate` are now `forced_mate`, as Chess.com says ForcesMate.
- **B3:** about 16 named tactics deep in R's line are now `material_gain` (Chess.com's
  LosesMaterial). 4 deep forks that Chess.com does name are lost. The tighter Fork turns 6 forks
  into Chess.com's Skewer, because the skewer is now the best tactic on the move.
- **B8:** 8 plies of the PERMITS free piece are now `hangs_piece`, as Chess.com says.
- **Taken back or outgrown** (`cb1b475`, after a first pass at `df8a7c1` that reached 29.0%): a free
  piece the mover takes back, or that the line outgrows by more than a pawn, is `material_gain`.
  That gained 14 LosesMaterial plies and lost 4 FreePiece plies.

**Target missed by 0.4 points.** Phase 0 estimated 30% or more; this run is 8 plies short. It was not
tuned further: the two refinements already used these games, and the holdout games agree at 30.1%.
The largest remaining patterns are Phase 2b work. In 53 plies Chess.com says the best move
threatened material and we say nothing. In 17 Chess.com names the only good move.

**Forced moves.** All 114 now get the sentence "… was the only legal move". The comparison still
counts them as "they explain, we don't", because it reads events and the sentence has none.
## Results: Phase 2b (`14186c4`, 142 games)

Phase 2b of [`coach-gap-analysis.md`](../coach-gap-analysis.md) §4.2, on top of the quick fixes (§4.1).
Same labels as before. Run `coach-phase2b`, mapping in `coach_tags.py` extended with the new tags.

| | phases 1–3 (`e4ead28`) | quick fixes (`d25b1b7`) | **Phase 2b** (`14186c4`) | §5 target |
|---|---:|---:|---:|---:|
| bad moves both label bad (1,641): exact | 22.6% | 29.0% | **35.4%** | not below the quick fixes |
| … they explain, we say nothing | 18.3% | 18.5% | 7.1% | |
| good moves both label good (5,349): exact | 23.1% | 23.4% | **44.3%** | ≥ 35% |
| … they explain, we say nothing | 30.1% | 30.1% | 17.4% | |
| best-move sentence: exact | 11.9% | 12.1% | **37.6%** | ≥ 30% |
| … they explain, we say nothing | 60.5% | 60.9% | 15.1% | |

By gap (exact, Phase 2b; all were 0 before):

| gap | Chess.com says | exact |
|---|---|---:|
| G1 | a recapture (ObviousRecapture, ImmediateRecapture, DevelopsRecapture) | 412 / 475 |
| G1 | EqualTrade | 216 / 290 |
| G1 | wins a pile trade (PileTrade) | 8 / 38 |
| G3 | EvadesCheck | 234 / 265 |
| G4 | Kicks, WinsTempo | 179 / 204 |
| G5 | Brilliant | 9 / 13 |
| B1 | misses > CaptureThreat (played-move speech) | 42 / 155 |
| B4 | best move: DefendsPiece, Retreat, EscapesThreat, ObviousRetreat | 132 / 207 |
| B4 | best move: EvadesCheck | 48 / 54 |
| B4 | best move: Kicks, WinsTempo | 52 / 75 |
| B4 | best move: EqualTrade, ObviousRecapture | 55 / 87 |
| B5 | misses > Critical / best move Critical | 9 / 40 and 7 / 22 |
| B9 | an evaluation slide | 7 / 27 |
| B10 | permits > PileTrade | 0 / 20 |

- Our "threatens to win the piece" on good moves fell from 351 to 37: those are now kicks and
  tempo moves.
- By Chess.com class, bad-move exact went up for Inaccuracies (9.8% → 17.6%), Mistakes
  (26.0% → 30.7%) and Misses (31.0% → 35.7%). Blunders slipped by 3 plies (59.6% → 58.3%).
- **Mapping choice.** When the best move attacks a piece that can move away, Chess.com's played-move
  speech says "missed a capture threat" (CaptureThreat) and its best-move speech says Kicks or
  WinsTempo. Ours says `kicks` / `gains_tempo` under MISSES, mapped to both.
- **Still open:** B10 (we name the reply's free piece, not a won trade), B1 on moves where the
  best move's threat is not a tempo (we say a defence or nothing), and the positional families
  (Phase 4).
- The search after the best move ran 4,735 times (one per coached move that was not the best move,
  of 7,668). The run shared the machine with the quick-fix run, so its wall-clock time (6,957 s)
  does not measure the cost; see `implementation-notes.md` "Coach phase 2b".

## Results: Phase 4 (`118a076`, 142 games)

Phase 4 of [`coach-gap-analysis.md`](../coach-gap-analysis.md) §4.3: positional tags, rating gates
and the optional Maia-2 framing ([`implementation-notes.md`](../implementation-notes.md) "Coach
phase 4"). Run `coach-phase4`: a fresh review of every game (no engine results reused). Labels are
unchanged (68.7% exact). The column "main before" is current main (`bda974d`: Phase 2b plus the
taken-back refinement `cb1b475`), measured the same way; it is slightly above the Phase 2b run.

| | Phase 2b (`14186c4`) | main before (`bda974d`) | **Phase 4** (`118a076`) | target |
|---|---:|---:|---:|---:|
| good moves both label good (5,349): exact | 44.3% | 44.4% | **58.3%** | ≥ 52% |
| … they explain, we say nothing | 17.4% | 17.4% | 2.9% | |
| bad moves both label bad (1,641): exact | 35.4% | 36.0% | **39.2%** | |
| opening-phase bad moves (Chess.com bad, 602): exact | 26.9% | 27.6% | **34.4%** | ≥ 33% |
| … the same, both label bad (491) | 33.0% | 33.8% | 42.2% | |
| Blunders (228): exact | 58.3% (133) | 60.1% (137) | **60.5% (138)** | no drop |
| best-move sentence: exact | 37.6% | 37.6% | **46.0%** | |
| book moves (816): same event as Chess.com | 0 | 0 | 97 | |

The opening-phase row follows the report's "By phase" table (every ply Chess.com labels bad); the
row below it counts only plies both apps label bad.

By Chess.com's group of positional tags (plies where theirs is the main event; exact before → after):

| group | good moves | bad moves | best-move sentence |
|---|---|---|---|
| development and castling | 0 → 501 of 598 | 0 → 24 of 63 | 0 → 79 of 153 |
| centre (strikes, breaks, pawn in the centre, chains) | 0 → 72 of 127 | 0 → 13 of 27 | 0 → 31 of 75 |
| activity (open files, outposts, batteries, active squares, the king) | 0 → 114 of 193 | 0 → 6 of 32 | 0 → 27 of 76 |
| pawn structure (doubled, isolated, passed pawns) | 0 → 72 of 119 | 0 → 8 of 66 | 0 → 7 of 40 |
| opening errors (same piece twice, early queen, f3, king's shelter) | 0 of 19 | 0 → 10 of 64 | 0 of 15 |

- **What moved.** On good moves the development and castling ideas carry most of the gain (+501
  exact): DevelopsCenter (123), PreparesToCastleKingside (76), CastlesKingSide (63),
  PreparesBishopDevelopment (55), CastlesSameSide (53), PushesPassedPawnEndgame (42). A forced
  doubled pawn is said before the trade (30 exact, where we said `equal_trade`).
- **Mapping choice.** Chess.com splits development and castling by circumstance (toward the centre
  or not; the other king castled or not). `coach_tags.py` counts our variants as one tag with all of
  theirs. Only 12 of the 383 exact development and castling plies match across variants (mostly
  DevelopsLastPiece), so this changes the totals by about 0.2 points.
- **Rating gates.** Without `player_side`, the gate rating is `rating_used` (the higher Elo plus 200,
  at least 1000), so in this run only `backward_pawn` (1100) is ever gated; with gates off
  (`--config '{"coach": {"rating_gates": false}}'`) one bad move changes. Reviewing every game as
  White and as Black (`compare.py --player-side`, new) gates each side's moves at its own Elo, mostly
  800–1000. Then good-move exact is 57.7% (−0.6 points: 36 positional ideas fewer, mainly
  structure), bad 38.9% (−0.3), opening-phase 33.7%, Blunders unchanged. Tactics and captures have
  no gate, so the routine captures where Chess.com stays quiet (G7) are not affected: we still
  speak on 381 of the 743 good moves where Chess.com says nothing (383 without gates; 294 before
  Phase 4, the rise is positional remarks).
- **Book moves.** We now explain 716 of 816 book moves, Chess.com 147; on 97 we say its event.
  Chess.com's other book remarks are FEN-specific opening notes (§3.4 of the gap analysis).
- **Still different:** a developing move that pins (Bg5) is said as the pin, Chess.com says
  DevelopsOpening (15); pawn chains we do not name (CreatesPawnChain, 14); StrikesAtCenter where we
  say `kicks` (14); and on bad moves Chess.com's "missed a capture threat" (B1) still meets our
  best move's development idea (5).
- **Maia-2** does not change agreement: the comparison reads tags and circumstances, and the model
  only picks wordings. A run with the real model (rapid, local run `coach-p4-maia`) gives the same
  58.3% / 39.2%; its wording counts and cost are in `implementation-notes.md` "Coach phase 4".
- **Cost.** The positional detectors are static board tests. The fresh run took 2,647 s against
  2,868 s for main before on the same machine, within the noise.
- **Tuning runs** (local only, `~/work/p4/runs`): `coach-p4-a` (first pass: good 58.0%, bad 39.0%),
  then forced isolated pawns after trades, centre-pawn hits always strikes, king activity only from
  the back two ranks and the central push only in the opening (`coach-p4-b`, the committed code);
  `coach-p4-nogates`, `coach-p4-as-white` / `-as-black` for the gates. These reused the engine
  results of the main-before run through a local disk cache that is not part of the code.

## Results: detector fixes (`0a8971a`, 142 games)

The tactic detectors were checked against the lichess puzzle themes and seven of them fixed;
see [`detector-check.md`](detector-check.md). Against Chess.com (run `coach-detector-check`,
same engine results as `coach-main-582bdd9` through the local disk cache):

- bad moves exact 39.2% → 40.5% (643 → 665 of 1,641), good moves 58.3% → 58.8%;
- Blunders 138 → 140 of 228, best-move sentence 46.0% both, labels 68.7% both;
- 100 plies became exact and 48 stopped being exact (mostly king-and-pawn checks Chess.com calls forks).

## Files

| path | committed | content |
|---|---|---|
| `tools/calibrate/coach_capture.js` | yes | in-page capture |
| `tools/calibrate/coach_oracle.py` | yes | ingest, decode, match (reads local paths) |
| `tools/calibrate/coach_tags.py` | yes | the mapping table and families |
| `tools/calibrate/coach_compare.py` | yes | the comparison and report |
| `tests/calibration/runs/coach-phase0/coach-report.md` | yes | the full report (tags and ply references only) |
| `~/work/chesscom/oracle/captures/raw/<id>.json` | **never** | captured frames (Chess.com text) |
| `~/work/chesscom/oracle/captures/<id>.coach.json` | **never** | decoded speech (Chess.com text) |
| `~/work/chesscom/oracle/captures/<id>.keys.json` | no | keys and tags per ply |

`.gitignore` excludes `captures/`, `*.coach.json`, `*.keys.json` and the oracle files, in case any
of them is copied into the checkout.
