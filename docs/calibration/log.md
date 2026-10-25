# Calibration log

Each row is one harness run on the **tuning** set (14 games, 856 scored plies) unless marked
holdout. Settings for every run: Stockfish 17.1 (our engine), depth 18, MultiPV 3. The reference
labels come from Chess.com Game Review with engine Stockfish (`stockfish16 nnue`) at Fast (depth 18);
see `tests/calibration/README.md`. Reports are in `tests/calibration/runs/<run>/report.md`.

Exact = labels equal after normalisation; within-one = at most one step apart on
best > excellent > good > inaccuracy > mistake > blunder (book, brilliant, great and miss must match).
P / R = precision / recall. Acc MAD = mean absolute difference from the app's per-player accuracy
(bias in brackets, ours minus app).

| date | commit | run | change | exact | within-one | Brilliant P / R | Great P / R | acc MAD (bias) | conclusion |
|---|---|---|---|---:|---:|---|---|---|---|
| 2026-10-18 | `9ddf4a5` | `baseline` | none (code as of `5bc590e`) | 64.6% | 84.1% | 0.03 / 0.67 | 0.75 / 0.12 | 3.24 (+2.73) | Brilliant fires 60 times against the app's 3; Great Find almost never fires (4 vs 26). |
| 2026-10-18 | `c76a4ce` | `fix1-brilliant` | Fix 1: Brilliant needs the engine's best move, a clearly worse second-best move, a static sacrifice (new SEE), the EP window and the recovered gates | 68.2% | 89.6% | 1.00 / 0.33 | 0.71 / 0.19 | 2.96 (+2.79) | Kept: 59 false Brilliants gone and Great Find no longer pre-empted. Of the app's 3, 1 matches; 5.Nxe5 fails the second-best gap (0.067 EP at rating 1010) and 21...gxf3 is not our engine's best move. |
| 2026-10-18 | `c76a4ce` | `fix1-brilliant-hanging` | variant: also count a piece left en prise (`count_pieces_left_hanging`) | 68.2% | 89.6% | 1.00 / 0.33 | 0.71 / 0.19 | 2.96 (+2.79) | No effect on the tuning set; left off (the spec's definition) and revisited in Fix 6. |
| 2026-10-18 | (not kept) | `fix2-material` | Fix 2 as specified: material loss = immediate SEE exposure | 68.0% | 88.7% | 0.50 / 0.33 | 0.67 / 0.15 | 3.16 (+3.03) | Inconclusive: between two server runs the engine numbers changed on 799 of 865 plies and about 120 labels flipped each way, far above the effect being measured. Set aside until searches are deterministic; it also softened 4 real Blunders to Mistake. |
| 2026-10-18 | `b9f8aad` | `fix3a-deterministic` | Fix 3, determinism part, done before Fix 2: `ucinewgame` + Clear Hash before every search (Threads=1) | 70.4% | 89.1% | 1.00 / 0.33 | 0.56 / 0.19 | 3.19 (+2.79) | Kept. Labelling rules are as in Fix 1, so the change from `fix1-brilliant` is engine noise, not an improvement. This is the reference run for later changes. |
| 2026-10-18 | `b9f8aad` | `fix3a-deterministic-repeat` | the same code on a fresh server | 70.4% | 89.1% | 1.00 / 0.33 | 0.56 / 0.19 | 3.19 (+2.79) | Identical ply for ply (0 of 865 plies differ), so later runs can be compared exactly. |
| 2026-10-18 | (reverted) | `fix2-material-det` | Fix 2 as specified, now on the deterministic engine | 69.9% | 89.1% | 1.00 / 0.33 | 0.56 / 0.19 | 3.19 (+2.79) | 13 labels change, 4 better and 7 worse. Blunder softening hurts most: 4 of the app's Blunders lose material through a later tactic, not an immediate exchange, and become Mistakes. |
| 2026-10-18 | (reverted) | `fix2-material-adj` | adjusted once: blunder softening also counts the engine line; the rest exchange-based | 70.2% | 89.1% | 1.00 / 0.33 | 0.56 / 0.19 | 3.19 (+2.79) | Reverted: 2 better, 4 worse. Hardening of Best/Excellent/Good moves, the problem this fix targets, occurs once on the tuning set after Fix 1 (vs 16 of 25 Mistakes in the original audit), so there is little left to gain. |
| 2026-10-18 | (reverted) | `fix3b-searchmoves` | Fix 3, scoring part: a played move outside the MultiPV lines is scored by a search of the same position restricted to it (`searchmoves`) instead of the next position's search | 68.8% | 89.0% | 1.00 / 0.33 | 0.56 / 0.19 | 3.25 (+2.82) | Reverted: 212 plies get new scores, 12 labels better, 26 worse. The restricted search rates the played move higher (many app Inaccuracies become our Good), so the app's grades match the next-position search, which finds the refutation at full depth. `searchmoves` stays available in the engine layer. |
| 2026-10-18 | (variant) | `fix4-greatfind` | Fix 4: Great Find exclusions (only escape, free capture by SEE, promoting pawn, quiet retreat with < 200 at stake) plus the shallow-search proxy at depth 4 | 70.2% | 88.9% | 1.00 / 0.33 | 0.00 / 0.00 | 3.19 (+2.79) | The proxy removes every Great Find: a depth-4 search already finds these only-moves. Depths 6 and 8 (`fix4-easy6`, `fix4-easy8`) behave the same. |
| 2026-10-18 | `32b5149` | `fix4-easy0` | adjusted once: the exclusions without the shallow-search proxy (`easy_search_depth` 0, now the default) | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 | 3.19 (+2.79) | Kept as the recovered structure; on its own it is neutral (Bxh8 rightly dropped, Qxg5 wrongly dropped by the free-capture rule). It matters once Fix 6 lowers the gap threshold. |
| 2026-10-18 | `32b5149` | `holdout-1` | **holdout check** after Fix 1, 3a and 4 (6 games, 310 plies) | 65.5% | 85.2% | - / 0.00 | - / 0.00 | 2.93 (+1.65) | 4.9 points below tuning (70.4%), inside the 5-point limit. Nothing had been tuned yet, so this is the spread between game sets. We give no Brilliant or Great Find on the holdout games. |
| 2026-10-18 | (reverted) | `fix5-miss` | Fix 5: Miss tactic needs a capture or check first and the gain within 3 plies; opportunity needs the best move to keep 70% of the opponent's loss and the played move not to; free piece by SEE | 70.3% | 89.0% | 1.00 / 0.33 | 0.57 / 0.15 | 3.19 (+2.79) | 1 better, 2 worse. The SEE free-piece test turns 5...Bxd1 in Legal's trap (app: Blunder) into a Miss. Variants on the same code: `fix5-regain50` (share 0.5) identical; `fix5-tactic5` (5 plies) 70.4%. |
| 2026-10-18 | (reverted) | `fix5-miss-adj` | adjusted once: free piece back to the line test, tactic and opportunity kept | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 | 3.19 (+2.79) | Reverted: 1 better (Ne4, app Mistake), 1 worse (exd3, app Miss). No net gain. |
| 2026-10-18 | (reverted) | `fix6-tuned` | Fix 6: tuned defaults from the trials below: Great Find gap 0.20 → 0.13; Brilliant gap 0.10 → 0.05 and `count_pieces_left_hanging` on | 70.8% | 89.5% | 1.00 / 0.67 | 0.64 / 0.27 | 3.19 (+2.79) | Best tuning-set result: +3 Great Find and +1 Brilliant (Legal's trap 5.Nxe5) labels. |
| 2026-10-18 | (reverted) | `holdout-2` | **holdout check** of `fix6-tuned` | 64.8% | 84.5% | - / 0.00 | 0.25 / 0.10 | 2.93 (+1.65) | 6.0 points below tuning, over the 5-point limit, and below `holdout-1` (65.5%): the lower Great Find gap gives 4 Great Finds on holdout, 1 right. Overfitting, so the Fix 6 tuning is undone; the final code is `32b5149` and `holdout-1` is its holdout report. |

**Stopped** after Fix 6: three iterations in a row (Fix 4, Fix 5, Fix 6) brought no lasting improvement.
Holdout Brilliant precision is undefined (we give no Brilliant on the 6 holdout games; the app gives 1).

### Fix 6 trials (tuning set, one server, one parameter at a time)

All rows use the code of `32b5149` with the given override merged over the defaults. `t2-*` and
`t3-*` start from the best Great Find gap of the first batch.

| trial | config override | exact | within-one | Brilliant P / R | Great P / R |
|---|---|---:|---:|---|---|
| `t-ref` | none | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-gf-gap10` | `{"great_find":{"min_gap_to_second_best":0.1}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.53 / 0.31 |
| `t-gf-gap12` | `{"great_find":{"min_gap_to_second_best":0.12}}` | 70.7% | 89.4% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t-gf-gap15` | `{"great_find":{"min_gap_to_second_best":0.15}}` | 70.6% | 89.3% | 1.00 / 0.33 | 0.60 / 0.23 |
| `t-gf-gap17` | `{"great_find":{"min_gap_to_second_best":0.17}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-gf-gap25` | `{"great_find":{"min_gap_to_second_best":0.25}}` | 70.3% | 89.0% | 1.00 / 0.33 | 0.50 / 0.04 |
| `t-br-gap05` | `{"brilliant":{"min_gap_to_second_best":0.05}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-br-gap07` | `{"brilliant":{"min_gap_to_second_best":0.07}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-br-gap15` | `{"brilliant":{"min_gap_to_second_best":0.15}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-br-hanging` | `{"brilliant":{"count_pieces_left_hanging":true}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-br-maxep95` | `{"brilliant":{"max_ep_before":0.95}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-br-maxep85` | `{"brilliant":{"max_ep_before":0.85}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-br-mateok` | `{"brilliant":{"exclude_mating_moves":false}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-horizon4` | `{"material_horizon_plies":4}` | 70.4% | 89.4% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-horizon8` | `{"material_horizon_plies":8}` | 70.2% | 88.9% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-blunder200` | `{"blunder_material_threshold_cp":200}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-miss-opp15` | `{"miss":{"opportunity_min_opponent_ep_lost":0.15}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-miss-tactic300` | `{"miss":{"tactic_min_gain_cp":300}}` | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t-miss-free100` | `{"miss":{"free_piece_min_value_cp":100}}` | 70.6% | 89.3% | 1.00 / 0.33 | 0.57 / 0.15 |
| `t2-gf11` | `{"great_find":{"min_gap_to_second_best":0.11}}` | 70.7% | 89.4% | 1.00 / 0.33 | 0.62 / 0.31 |
| `t2-gf12` | `{"great_find":{"min_gap_to_second_best":0.12}}` | 70.7% | 89.4% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-gf13` | `{"great_find":{"min_gap_to_second_best":0.13}}` | 70.7% | 89.4% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-gf14` | `{"great_find":{"min_gap_to_second_best":0.14}}` | 70.7% | 89.4% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-free100` | `{"great_find":{"min_gap_to_second_best":0.12},"miss":{"free_piece_min_value_cp":100}}` | 70.8% | 89.5% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-free200` | `{"great_find":{"min_gap_to_second_best":0.12},"miss":{"free_piece_min_value_cp":200}}` | 70.7% | 89.4% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-h4` | `{"great_find":{"min_gap_to_second_best":0.12},"material_horizon_plies":4}` | 70.7% | 89.6% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-h5` | `{"great_find":{"min_gap_to_second_best":0.12},"material_horizon_plies":5}` | 70.7% | 89.6% | 1.00 / 0.33 | 0.64 / 0.27 |
| `t2-br-hang05` | `{"great_find":{"min_gap_to_second_best":0.12},"brilliant":{"count_pieces_left_hanging":true,"min_gap_to_second_best":0.05}}` | 70.8% | 89.5% | 1.00 / 0.67 | 0.64 / 0.27 |
| `t2-br-hang03` | `{"great_find":{"min_gap_to_second_best":0.12},"brilliant":{"count_pieces_left_hanging":true,"min_gap_to_second_best":0.03}}` | 70.8% | 89.5% | 1.00 / 0.67 | 0.64 / 0.27 |
| `t2-gf12-hr0` | `{"great_find":{"min_gap_to_second_best":0.12,"require_high_rated":false}}` | 70.8% | 89.4% | 1.00 / 0.33 | 0.60 / 0.35 |
| `t3-final` | `{"great_find":{"min_gap_to_second_best":0.13},"brilliant":{"count_pieces_left_hanging":true,"min_gap_to_second_best":0.05}}` | 70.8% | 89.5% | 1.00 / 0.67 | 0.64 / 0.27 |
| `t3-final-free100` | `{"great_find":{"min_gap_to_second_best":0.13},"brilliant":{"count_pieces_left_hanging":true,"min_gap_to_second_best":0.05},"miss":{"free_piece_min_value_cp":100}}` | 70.9% | 89.6% | 1.00 / 0.67 | 0.64 / 0.27 |

### Optional: search depth (final code `32b5149`, tuning set)

| run | depth | exact | within-one | Brilliant P / R | Great P / R | acc MAD (bias) |
|---|---:|---:|---:|---|---|---|
| `depth-14` | 14 | 66.5% | 87.7% | 1.00 / 0.33 | 0.60 / 0.12 | 3.04 (+2.65) |
| `depth-16` | 16 | 68.7% | 88.9% | 1.00 / 0.33 | 0.57 / 0.15 | 2.99 (+2.64) |
| `fix4-committed` | 18 | 70.4% | 89.1% | 1.00 / 0.33 | 0.57 / 0.15 | 3.19 (+2.79) |
| `depth-20` | 20 | 68.2% | 89.8% | 1.00 / 0.33 | 0.60 / 0.12 | 2.71 (+2.57) |

Depth 18, the app's "Fast" setting, gives the best exact agreement; depth 20 is slightly closer on
within-one agreement and accuracy. The default stays 18. Stockfish 16.1 (the reference's engine) was
not tried: it needs a download that is the owner's call.

### Where the remaining disagreement comes from (oracle check, after `c9aec9f`)

The app's dataset records its eval after every move, and the eval before a move is the value of
the app's best move. Feeding those evals through our recovered rules reproduces the app's label
on **86.5%** of the 688 tuning plies with a precision-type label (holdout 85.8%), against 71% with
our engine's evals. Our evals differ from the app's by a median of 13 cp (90th percentile 45 cp).
So about 15 points of disagreement come from the engine, not the rules.

The rest is one-directional: with its own evals the app is one step harsher than our rules
(Inaccuracy→Good 22, Good→Excellent 21, Mistake→Inaccuracy 13). A higher rating input to the
EP curve reproduces this: max(Elo) + 100…350 gives 88.7–89.2% on tuning and 87.1–88.4% on
holdout (+200: 89.0% / 88.4%). A fixed rating does worse.

| date | commit | run | change | exact | within-one | Brilliant P / R | Great P / R | acc MAD (bias) | conclusion |
|---|---|---|---|---:|---:|---|---|---|---|
| 2026-10-18 | (rating offset) | `r-off200` | experimental `rating_offset` +200 (tuning; +150 equal, +250 71.5%, +300 70.7%) | 71.7% | 89.3% | 1.00 / 0.33 | 0.71 / 0.19 | 3.05 (+2.93) | +1.3 points and better Great Find precision. Chosen on tuning. |
| 2026-10-18 | (rating offset) | `holdout-r-off200` | **holdout check** of +200 | 67.4% | 85.2% | - / 0.00 | 0.50 / 0.10 | 2.74 (+0.92) | Generalises: +1.9 points over `holdout-r-off0` (65.5%), accuracy bias halved. Left at default 0 pending the owner's decision (it changes a recovered rule's input). |
| 2026-10-18 | (engine) | `sf16-off200` | Stockfish 16 instead of 17.1 (official build), rating +200 | 70.8% | 88.8% | 1.00 / 0.33 | 0.71 / 0.19 | 2.68 (+2.23) | Not better than 17.1 (71.7%); `sf16-off0` 70.1%. Evals no closer to the app's (median 15 cp vs 13). |
| 2026-10-18 | (engine) | `sf16.1-off200` | Stockfish 16.1, rating +200 | 68.9% | 89.0% | 1.00 / 0.33 | 0.80 / 0.15 | 3.18 (+3.06) | Worse; `sf16.1-off0` 67.5%. Engine version is not the cause; the median eval gap to the app is 12–16 cp for every version and depth. Stockfish 17.1 kept. |
| 2026-10-18 | (book) | `book-anywhere` | rating +200 (now default) and a move is Book whenever its position is in the book, even after leaving it (`book_requires_unbroken` false) | 72.2% | 89.7% | 1.00 / 0.33 | 0.71 / 0.19 | 3.14 (+3.02) | Kept as default: 5 better, 1 worse; the app marks transpositions back into the book as Book. Reference for the defaults. |
| 2026-10-18 | (book) | `holdout-book-anywhere` | **holdout check** of the new defaults | 68.1% | 85.8% | - / 0.00 | 0.50 / 0.10 | 2.72 (+0.94) | +0.7 over the +200 rating alone (67.4%), +2.6 over `holdout-1`. Tuning–holdout gap 4.1 points. |

### Batch 2: 59 games (tuning 41 games / 2,833 scored moves, holdout 18 / 1,248), code `27fafb5`

| run | change | exact | within-one | Brilliant P / R | Great P / R | acc MAD (bias) | conclusion |
|---|---|---:|---:|---|---|---|---|
| `b2-default` | current defaults (rating +200, transposition book) | 67.4% | 89.4% | 0.50 / 0.25 | 0.60 / 0.12 | 3.66 (+3.44) | Reference for the larger set. Club games 69.8% exact, titled 64.1%. |
| `b2-off0` | rating offset 0 (recovered rule) | 66.1% | 89.2% | 0.50 / 0.25 | 0.50 / 0.10 | 3.50 (+3.19) | The +200 offset still gains 1.3 points on new data. |
| `b2-*` (16 trials) | rating 100/300; Great Find gap 0.10–0.25; high-rated gate off; Brilliant gap, hanging pieces, mating moves, EP window; free piece 100; horizon 4; blunder threshold 200; opportunity 0.15 | 67.0–67.5% | 89.2–89.6% | | | | All within ±0.1 point of the reference (about 3 labels): nothing left to tune in the rules. |
| `holdout-b2` | **holdout check** of the defaults | 65.7% | 88.0% | 0.50 / 0.33 | 0.78 / 0.17 | 3.14 (+1.93) | 1.7 points below tuning: no overfitting. Club games 70.0% exact, titled 59.1%. |

On the larger set the app-eval oracle (our rules on Chess.com's own evals) reproduces 85.3% of
tuning labels (87.6% with the +200 rating) against 67% with our engine's evals, so the remaining gap
is still the engine's search noise, larger in titled games, where the steep EP curve at rating 2500
turns small eval differences into grade changes.

### Exact Chess.com review data (2026-10-18)

The review page's own `/v2/game-review` responses were captured for all 59 games
(`tests/calibration/cc-reviews/`, protocol in `chesscom-review-protocol.md`). They give, per move,
Chess.com's played-move score, best move and best-move score, with the engine and depth of each score.
Findings:

- The dataset is the Stockfish review: all 4,081 scored labels match the captures exactly (the 9
  `uncertain` labels are now filled from them, `label_source: "chesscom-capture"`).
- **"Stockfish 16" is scored by Stockfish 18** (`Score.engine` = `ENGINE_SF18_NNUE`). The site
  default engine is Torch (`ENGINE_TORCH_3` scores), which a Stockfish clone cannot match.
- **Best = the engine's move**: a best alternative is attached exactly when the played move is not
  the engine's choice.
- Search: fresh searches reach depth 12-23 (mean 17.4), so "Fast" is a node or time budget; positions
  on an earlier principal variation inherit its score one ply shallower; opening positions carry
  cached depth 26-35 scores.

**Decomposition of our disagreement** (`b2-default` + `holdout-b2`, 4,090 plies, 66.9% exact):
precision grade 14.3 points, best-move identity 11.2 (our best move equals Chess.com's on 70% of
plies), Great/Brilliant 2.9, Book 2.4, Miss 1.9. Median score difference 11 cp (p90 46).

**Exact-score oracle** (`tools/calibrate/cc_oracle.py`): our precision rules applied to Chess.com's
own scores reproduce 82.0% of Excellent…Blunder labels with the recovered rating rule (max Elo,
1000-2500), 85.1% with the calibrated +200, and **87.4-87.8%** with +100…+200 and the upper clamp
raised to 3000 (titled games 81.2% → 88.1%). Thresholds 0.02/0.05/0.10 are confirmed; no rating,
per-game rating, curve family (Stockfish WDL, material-scaled logistic) or threshold change gets
above about 88%. The remaining errors go both ways within a game, so the displayed scores are not
exactly the inputs Chess.com graded: about one graded label in eight cannot be reproduced even
with Chess.com's own numbers.

**Search emulation** (`tools/calibrate/emulate_search.py`, 59 games, precision labels):

| engine / procedure | best move = Chess.com | score error med / p90 | precision-label agreement |
|---|---:|---:|---:|
| SF 17.1, depth 18 (as now) | 70.4% | 11 / 43 cp | 66.9% |
| SF 18, depth 18 | 73.1% | 9 / 37 | 68.5% (68.8% clamp 3000) |
| SF 18, PV-inheriting tree, depth 18 | 72.7% | 9 / 37 | 69.5% (clamp 3200) |
| SF 18, tree, 400k nodes (median depth 18) | 73.2% | 9 / 32 | 69.5% (clamp 3200) |

**Full pipeline with Stockfish 18** (runs `sf18-b2`, `holdout-sf18-b2`, `*-rmax3000`):

| run | change | exact | within-one | Brilliant P / R | Great P / R | acc MAD (bias) |
|---|---|---:|---:|---|---|---|
| `sf18-b2` | Stockfish 18, defaults | 66.8% | 89.7% | 1.00 / 0.25 | 0.54 / 0.09 | 3.73 (+3.19) |
| `holdout-sf18-b2` | holdout | 68.0% | 87.9% | 0.50 / 0.33 | 0.71 / 0.12 | 3.65 (+2.63) |
| `sf18-b2-rmax3000` | + `rating_max` 3000 | 67.2% | 89.9% | 1.00 / 0.25 | 0.65 / 0.14 | 3.72 (+3.18) |
| `holdout-sf18-b2-rmax3000` | holdout | 68.8% | 88.1% | 0.50 / 0.33 | 0.71 / 0.12 | 3.64 (+2.62) |

All 59 games: 66.9% (SF 17.1) → 67.2% (SF 18) → 67.7% (SF 18 + clamp 3000). `rating_max` is now
3000 by default. Re-labelling the cached outputs with other rule ideas (Great: no captures and gap
≥ 0.13; Brilliant without the bucket shortcut; no Book for Inaccuracy or worse) moved agreement by at
most ±0.2 points: with our engine's scores, rule changes are below the search noise.

**Conclusion.** 95% exact agreement is out of reach for an independent reimplementation: even fed
Chess.com's own scores, the recovered rules reproduce about 88% of graded labels, and our own search
(best move equal on about 73% of plies at best) cannot replay Chess.com's server search. Realistic
targets are about 68-70% exact and about 90% within one step, unless Chess.com's own review data is
used directly.

### Brilliant rebuilt on Chess.com's published definition (2026-10-18)

Owner report: game 185058622904 (khhizr7, Traxler counter-attack) got no Brilliant from us; Chess.com
gives two. The captured `/v2/game-review` response (`cc-reviews/185058622904.sf.txt`; the Stockfish
and Torch reviews agree) marks **8...Nxg3** and **15...d5** Brilliant. The game is now in the tuning
set (batch 3).

The old rule was stricter than Chess.com's own help article ("How are moves classified?"), which
says a Brilliant is the best move and "a good piece sacrifice", the player must not be in a bad
position after it, must not be completely winning even without it, and newer players get a more
generous sacrifice test. Against the 9 Chess.com Brilliants in the 60 games, the old rule failed on:

| move | why it was rejected |
|---|---|
| 8...Nxg3 (185058622904) | "disguised trade": leaving e4 uncovers the queen's attack on c4 |
| 15...d5 (185058622904) | a pawn, not a piece (both players about 950) |
| 5.Nxe5 (Legal's trap), 19.O-O-O | the piece given up is left behind (queen; bishop after castling), not moved |
| 5.Nxe5, 19.O-O-O, 18...Nxd4 | second-best move within 0.06 EP (rule asked for 0.10) |
| 20...Bxh2+ | mating move, EP before 1.0 |
| 21...gxf3 | not our engine's best move |

New rule (`implementation-notes.md`): engine's best move; net material given up ≥ 100 by exchange and
the exchange wins ≥ 200 (or the whole pawn); the moved piece, a piece left newly en prise (castling
included), or a moved pawn when both players are below 1000; EP after ≥ 0.50; second-best not
completely winning (EP < 0.90, mates excepted); no gap requirement; mating moves allowed.
The "missed brilliant" Miss subtype keeps its own EP threshold (0.20).

| run | change | exact | within-one | Brilliant P / R | Great P / R | acc MAD (bias) |
|---|---|---:|---:|---|---|---|
| `sf18-b2-rmax3000` | reference (41 tuning games) | 67.2% | 89.9% | 1.00 / 0.25 | 0.65 / 0.14 | 3.72 (+3.18) |
| `brilliant-v2` | new rule without the 200 exchange floor | 67.0% | 89.7% | 0.38 / 0.75 | 0.65 / 0.14 | 3.72 (+3.18) |
| `brilliant-v3` | final rule, 42 tuning games (+185058622904) | 67.3% | 89.8% | 0.62 / 0.83 | 0.65 / 0.13 | 3.66 (+3.08) |
| `holdout-sf18-b2-rmax3000` | reference holdout | 68.8% | 88.1% | 0.50 / 0.33 | 0.71 / 0.12 | 3.64 (+2.62) |
| `holdout-brilliant-v3` | **holdout check** of the final rule | 68.8% | 88.1% | 0.50 / 0.67 | 0.67 / 0.10 | 3.64 (+2.62) |

All 60 games: Chess.com 9 Brilliants; we now give 12, 7 of them right (before: 3 given, 2 right).
Exact and within-one agreement are unchanged. Both of the owner's game's Brilliants are found and
nothing else in that game. Remaining differences:

- Missed: 21...gxf3 (not our engine's best move); 20...Bxh2+ (the recovered material gate: Black is up
  exactly a bishop after it and the opponent is mated, so `balance < piece value` fails by equality).
- Extra: 12.Nd5 (1041474766), 8...Nxg3 (185438343298), 15.Bxh7+ (185468614210), 14.Bxg5 (185476493194)
  rated Best, and 20.Bh7+ (185151408586) rated Great by Chess.com. 8...Nxg3 is the same position,
  move and score as the owner's Brilliant 8...Nxg3; there the opponent declined the knight (9.d3). The
  review data does not show what separates the two.
- Rejected variants (offline, on the cached engine output): counting pieces that were already en prise
  (gives false reasons, such as a rook hanging since move 5); pawns left behind at low ratings (+4
  false); "the opponent takes the piece next move" (Chess.com Brilliants 28...Bxc2, 27...Ncxb3+ and
  19.O-O-O were not taken).

### Great rebuilt on the recovered structure (2026-10-23)

All 142 games with a captured Chess.com review (tuning 99, holdout 43; Stockfish 18, depth 18, MultiPV 3;
engine results from the local disk cache, so every run sees identical engine output). Design and
evidence: `great-blunder-analysis.md`. Intermediate runs were not kept; the code of each step is
described below.

| run | change | exact | within-one | Great P / R (tuning · holdout) | Blunder P / R |
|---|---|---:|---:|---|---|
| `gr-baseline` | `daf2d0d`: gap ≥ 0.20, Great only when max Elo ≥ 1000 | 68.7% | 88.7% | 0.62 / 0.05 (0.65 / 0.05 · 0.56 / 0.04) | 0.85 / 0.78 |
| (step 1) | recovered candidate and tags; `is_high_rated` as a branch | 70.4% | 90.3% | 0.73 / 0.67 (0.72 / 0.69 · 0.74 / 0.65) | unchanged |
| (step 2) | an immediate best-move recapture is never critical (0 of 25 were Great) | 70.7% | 90.6% | 0.79 / 0.68 | unchanged |
| (step 3) | only-safe-square exclusion: not for pawns | 70.7% | 90.6% | 0.78 / 0.71 | unchanged |
| (step 4) | only-safe-square exclusion: threatened pieces only | 70.9% | 90.8% | 0.79 / 0.75 | unchanged |
| `great-recovered` | wins material: not when the mover's previous move already won it (recovered) | 70.9% | 90.8% | **0.81 / 0.74** (0.79 / 0.73 · 0.84 / 0.75) | unchanged |
| `gr-crit-0.09` | trial: `critical_min_alternative_loss` 0.09 | 70.9% | 90.8% | 0.79 / 0.78 | unchanged |
| `gr-crit-0.08` | trial: 0.08 | 70.8% | 90.8% | 0.76 / 0.80 | unchanged |
| `gr-crit-0.07` | trial: 0.07 | 70.7% | 90.6% | 0.71 / 0.83 | unchanged |

Holdout agrees with tuning at every step, so nothing is overfitted. The threshold trials ran on all
142 games, holdout included, so the recovered 0.10 is kept. Brilliant is unchanged (P 0.54, R 0.52).
Four of Chess.com's Brilliants are now our Great instead of Best.

On khhizr7's own moves, Chess.com gives 125 Greats. We gave 10 (6 right); we now give 121 (99 right).

Remaining misses (84), by the first gate that stops them:
- 44: no tag, after an opponent move we grade below Mistake. 11 of these would be key moments
  (winning material or a free piece) if the grade were Mistake. Usually our engine grades the
  opponent's move one step milder than Chess.com, or the second line is 0.05–0.10 behind.
- 15: excluded as easy to find, or by the high-rated exclusions.
- 14: no tag at all.
- 4: Brilliant took precedence.
- 3: our grade is Good, not Best or Excellent.
- 4: other (the previous-move rule, the key-moment gates).

Remaining extras (57): 45 are Chess.com Best moves, mostly critical by our engine's gap but not by
Chess.com's.

### Blunder fixes (2026-10-23)

Same 142 games and engine cache as the Great rebuild above. Reference: `great-recovered`. Design:
`great-blunder-analysis.md` §3, §4 Phase 2.

| run | change | tuning exact | holdout exact | Blunder P / R (tuning · holdout) | Miss P / R (tuning · holdout) | Mistake P / R (tuning) |
|---|---|---:|---:|---|---|---|
| `great-recovered` | reference | 70.6% | 71.4% | 0.83 / 0.76 · 0.87 / 0.82 | 0.70 / 0.70 · 0.72 / 0.71 | 0.70 / 0.61 |
| `bl-floor-1100` | trial: `rating_min` 1100 | 71.0% | 71.8% | 0.85 / 0.76 · 0.86 / 0.83 | 0.72 / 0.71 · 0.72 / 0.71 | 0.70 / 0.63 |
| `bl-floor-1200` | trial: `rating_min` 1200 | 71.2% | 72.4% | 0.85 / 0.78 · 0.89 / 0.84 | 0.71 / 0.71 · 0.72 / 0.72 | 0.71 / 0.66 |
| `bl-floor-1300` | trial: `rating_min` 1300 | 71.2% | 72.4% | 0.82 / 0.81 · 0.88 / 0.83 | 0.70 / 0.71 · 0.70 / 0.75 | 0.70 / 0.65 |
| (step 1) | `rating_min` 1200; a move into forced mate is never a Miss; recovered getting-mated softening | 71.2% | 72.4% | 0.85 / 0.80 · 0.89 / 0.86 | 0.72 / 0.70 · 0.72 / 0.72 | 0.71 / 0.66 |
| `blunder-phase2` | + missed tactic and free piece need an opponent move that lost ≥ 0.05 EP | **71.3%** | **72.5%** | **0.85 / 0.82 · 0.88 / 0.87** | **0.78 / 0.68 · 0.79 / 0.69** | 0.70 / 0.69 |
| `bl-miss-0.02` … `-0.10` | trials of that threshold: 0.02, 0.03, 0.08, 0.10 | 71.3–71.4% | | 0.85 / 0.82 | 0.78–0.81 / 0.68–0.65 | |

**Picks.**
- `rating_min` 1200 ties 1300 on tuning exact agreement, with better Blunder precision. It is also the
  floor that Chess.com's own scores pointed to beforehand (§3.2).
- The Miss threshold barely matters between 0.02 and 0.10. 0.05, the Inaccuracy bound, says "after at
  least an Inaccuracy".

**All 142 games** (reference → final):
- Blunder 0.85 / 0.78 → **0.86 / 0.83**;
- Miss 0.71 / 0.70 → **0.79 / 0.68**;
- Mistake recall 0.61 → 0.69;
- exact agreement 70.9% → **71.7%**, within-one 90.8% → 91.2%;
- Great is unchanged (0.81 / 0.74). Brilliant loses one (P 0.55, R 0.48): the floor raises the EP of
  a sub-1000 sacrifice's alternative.

On khhizr7's own moves:
- Blunder: Chess.com 101; ours 89 (79 right) → 98 (87 right);
- Miss: Chess.com 122; ours 118 (83 right) → 96 (78 right).

**Not done.**
- Replacing the material fact with the coach's board events (Permits + WinsMaterial). It touches at
  most 17 plies, mostly pawn-only losses that Chess.com splits about evenly. The line walk already
  measures the reply's gain.

**What remains for Blunder** (38 missed, 31 extra). Among the 43 Blunder/Mistake swaps:
- 21 are engine noise: Chess.com's own score grades the move as Chess.com labels it, and ours does
  not.
- 22 are labels Chess.com's own displayed score does not support: 9 Blunders that score as a
  Mistake, and 13 Mistakes that score as a Blunder. No rule on that score reproduces them.

The rest: 12 Chess.com Blunders are our Miss, and 14 Chess.com Misses are our Blunder. Both are the
Miss detectors' heuristics.

### Batch 5 check of the Great and Blunder rules (2026-10-24)

The rules above were tuned on the 142 older games and are checked here on batch 5 without any change:
435 new reviews (`batch5-tuning.txt` / `batch5-holdout.txt`).
- 2 games were skipped (engine timeouts in both runs), so 433 games and 33,411 plies are compared.
- Both runs turned the coach's threat searches off (`coach.threat_search_depth` 0); they do not
  affect labels.
- `b5-base` is `main` at `daf2d0d`; `b5-current` is this branch.
- "strat" games are a random sample by rating band. "sac" games were chosen for sacrifices and are
  kept apart.

Precision / recall (Chess.com's count):

| split | run | exact | Great | Blunder | Miss | Mistake | Brilliant |
|---|---|---:|---|---|---|---|---|
| tuning strat | base | 65.2% | 0.75 / 0.10 (527) | 0.75 / 0.71 (337) | 0.71 / 0.66 (559) | 0.68 / 0.57 | 0.46 / 0.48 (25) |
| | current | 67.7% | **0.83 / 0.73** | 0.75 / **0.80** | **0.79** / 0.65 | 0.68 / 0.62 | 0.48 / 0.48 |
| holdout strat | base | 65.0% | 0.81 / 0.09 (242) | 0.73 / 0.67 (155) | 0.71 / 0.63 (292) | 0.68 / 0.58 | 0.36 / 0.50 (8) |
| | current | 67.6% | **0.85 / 0.74** | 0.70 / **0.72** | **0.75** / 0.60 | 0.68 / 0.61 | 0.42 / 0.63 |
| tuning sac | base | 64.6% | 0.76 / 0.08 (389) | 0.77 / 0.68 (229) | 0.69 / 0.64 (321) | 0.71 / 0.59 | 0.62 / 0.58 (31) |
| | current | 68.8% | **0.86 / 0.81** | 0.78 / **0.78** | **0.81** / 0.61 | 0.70 / 0.70 | 0.64 / 0.58 |
| holdout sac | base | 65.7% | 0.81 / 0.09 (139) | 0.81 / 0.71 (93) | 0.64 / 0.70 (147) | 0.71 / 0.55 | 0.47 / 0.78 (9) |
| | current | 69.5% | **0.87 / 0.80** | 0.78 / **0.77** | **0.72** / 0.64 | 0.71 / 0.64 | 0.47 / 0.78 |

Random sample by rating band (max Elo of the game), current rules:

| band (max Elo) | exact (base → current) | Great P / R (base → current) | Blunder P / R (base → current) |
|---|---|---|---|
| 0 (≤ 851) | 64.3% → 69.6% | 0.00 / 0.00 → 0.87 / 0.84 | 0.80 / 0.64 → 0.80 / 0.79 |
| 1 (702–1081) | 64.8% → 67.9% | 0.00 / 0.00 → 0.82 / 0.75 | 0.85 / 0.71 → 0.79 / 0.80 |
| 2 (1010–1356) | 68.5% → 70.0% | 0.73 / 0.11 → 0.81 / 0.71 | 0.80 / 0.73 → 0.78 / 0.77 |
| 3 (1316–1611) | 66.9% → 68.8% | 0.77 / 0.17 → 0.90 / 0.73 | 0.73 / 0.74 → 0.73 / 0.77 |
| 4 (1607–1941) | 65.3% → 67.1% | 0.81 / 0.12 → 0.85 / 0.70 | 0.64 / 0.74 → 0.65 / 0.79 |
| 5 (1913–3103) | 63.7% → 65.2% | 0.72 / 0.14 → 0.74 / 0.65 | 0.66 / 0.63 → 0.66 / 0.63 |
| 6 (2260–3299) | 61.5% → 64.0% | 0.79 / 0.18 → 0.86 / 0.72 | 0.56 / 0.68 → 0.58 / 0.75 |

**Findings.**
- **Great generalises.** Precision is 0.83–0.87 and recall 0.73–0.81 on every split, with holdout as
  good as tuning, against recall about 0.10 before. It is strong in every rating band, including
  2000+ games, which the 142 old games barely had. Below 1000 the old gate gave no Great at all.
- **Blunder recall rises on every split** (strat 0.70 → 0.77). Precision is flat (strat 0.74) and
  lower than on the 142 games, above all from 1600 up.
  - Of the 136 extra Blunders in the random sample, 61 are moves Chess.com labels Mistake although
    its own score grades them Blunder. Chess.com softens them because they do not lose material by
    its definition; our line walk says they do.
  - 42 are Chess.com Misses that our Miss detectors did not catch.
  - Only 31 are engine noise.
  - The material fact (`is_losing_material_or_getting_mated` from the coach's board events, plan
    Phase 2 step 4) was skipped on the 142 games, where it touched at most 17 moves. On batch 5 it
    is the largest Blunder error and worth building.
- **Miss precision rises on every split** (strat 0.71 → 0.77) for about 2 points of recall.
- **Exact agreement** rises 2.5–3.8 points on every split, and Brilliant is unchanged.
