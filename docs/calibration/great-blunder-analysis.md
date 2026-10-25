# Great and Blunder: where we differ from Chess.com, and the plan

Date: 2026-10-23. Analysis only: no code changed.

**Data.** All 142 games that have a captured Chess.com Stockfish review (`tests/calibration/cc-reviews/*.sf.txt`), against our latest full run, `runs/coach-main-582bdd9`. Classification code has only been refactored since that run (moved into `analysis/facts.rs`). The games contain 8,638 scored plies. 106 of them are khhizr7's, with 2,982 of his moves.

**Sources.**
- Chess.com's help article ["How are moves classified?"](https://support.chess.com/en/articles/8572705-how-are-moves-classified-what-is-a-blunder-or-brilliant-etc).
- A fresh decompile of `libcee.so` (APK 4.10.15) in WSL `~/work/re-great/` (Ghidra headless).
- Maia-2, run on 2,343 positions.

Scratch scripts and Maia outputs are kept in WSL `~/work/gb-analysis/` (`gb.js`, `great*.js`, `blunder*.js`, `ratingscan.js`, `maia*.js`). Run `node gb.js <repo> coach-main-582bdd9` first: it writes the rows file the other scripts read. Phase 0 below moves them into `tools/calibrate`.

## 1. Summary

| class | Chess.com | ours | both | precision | recall |
|---|---:|---:|---:|---:|---:|
| Great | 321 | 26 | 16 | 0.62 | **0.05** |
| Blunder | 228 | 209 | 177 | 0.85 | 0.78 |
| (khhizr7's moves) Great | 125 | 10 | 6 | | |
| (khhizr7's moves) Blunder | 101 | 89 | 79 | | |

Overall exact agreement is 68.7%.

- **Great** is the big gap: Chess.com gives about 2.3 per game, we give 0.2. The engine is not the cause. Chess.com's Great is our engine's best move in 307 of 321 cases, and we rate 286 of them plain Best. Our *rule* is wrong in three ways:
  1. **Inverted rating gate.** We block Great when both players are under 1000. In Chess.com's code that flag *selects the more generous branch* for new players. This alone blocks 206 of the 321 Chess.com Greats, because most of our games are under 1000.
  2. **Wrong trigger.** We look for a 0.20 EP "only move" gap. Chess.com has six triggers, and half of them are about *punishing the opponent's mistake*:
     - Chess.com rates 61% of the best replies to a Blunder Great, and 31% of the best replies to a Mistake;
     - after other moves it rates about 5% Great.
  3. **Wrong exclusion.** We exclude moves in already-won positions. Chess.com gives 45 Greats there, mostly the mate or finishing blow after an opponent's blunder.

  The recovered structure, approximated on our run output, finds **89% of Chess.com's Greats** (285 of 321). It also gives 594 extras (precision 0.32), which the "easy to find" exclusions are meant to remove (§2.4).
- **Blunder** is close. The remaining differences have four causes:
  - the rating used for low-rated games;
  - Miss winning over Blunder where it should not;
  - "walking into mate" leniency;
  - engine noise.

  Each is small. Together they are worth about +4 to +5 points of Blunder precision and recall.

## 2. Great

### 2.1 What Chess.com's code does (libcee 4.10.15, confirmed by decompile)

Our spec cites `0x1071764`, which comes from another binary. `is_great_find_candidate_core` is at raw `0x11d652c`. The spec also attributed gates from other events to Great: "not in time trouble", the Brilliant endgame gate and move probability. None of them belong to it.

A move is Great when `is_candidate<15>` holds and **one of these tags** fires:

| tag | trigger | extra condition |
|---|---|---|
| 38 forces-mate key moment | the move forces mate | opponent's previous move was a **Mistake or Blunder**, plus the key-moment gates below |
| 220 wins-material key moment | material gain in the line > 100, and not just a free piece | same |
| 55/56 free-piece key moment | takes a free piece | same, **and only when NOT high-rated** (both players under 1000) |
| 210 critical | best move; EP(best) ≥ 0.35; second line EP < 0.80 or loses ≥ 0.10 EP; not blocking check with a hanging piece | no obvious recapture |
| 211 winning | three plies back the mover was equal or better; now winning (bucket 5–6) | |
| 212 comeback | three plies back the mover was losing; now equal (bucket 3–4) (direction inferred) | |

The key-moment gates (`is_key_moment_candidate`) are all of these:
- the opponent's move was not forcing (not check);
- EP after the move ≥ **0.47**;
- precision is Best or Excellent;
- the mover was not completely winning after their own previous move;
- the move is not a recapture.

The candidate itself (`core`) needs all of these:
- the parent and grandparent are scored;
- precision is Best or Excellent;
- not `is_easy_to_find`;
- not an obvious quiet retreat (tag 125, gain < 200).

**High-rated players only** (max Elo > 999) are also excluded for:
- a simple recapture;
- checkmate on the board;
- removing an attacker in an equal trade.

There is one more rule. If the previous move by the same side (the grandparent) was a candidate with a Great tag, this move must not be a capture or a passed-pawn push.

`is_easy_to_find` runs these tests in order:
1. Castling is never easy.
2. If the position-difficulty model (an ML "charm" model) rates the position hard → not easy.
3. A promoting or promotion-threatening pawn → easy.
4. The moved piece's only safe square → easy.
5. A free piece or an obvious recapture → easy, **high-rated only**.

Without the model data, step 2 is skipped. That heuristic fallback is all we can build. `move_probability` is used only by Tricky, not by Great.

### 2.2 What the data says (independent of the decompile)

- **The rating gate.** Chess.com Greats per move, by max Elo:
  - under 1000: 4.8% (206 Greats in 85 games);
  - 1000–1499: 2.9%;
  - 2000+: 4.0%.

  Greats are frequent below 1000, where we give none.
- **The opponent's previous move.** The share of best replies that are Great, by the opponent's previous label:

  | opponent's previous label | share Great |
  |---|---:|
  | Blunder | 61% |
  | Mistake | 31% |
  | Miss | 20% |
  | anything else | 3–6% |

  215 of the 321 Greats follow an opponent Inaccuracy or worse.
- **Losing positions.** Greats almost never come from losing positions: 3 of 321 have EP before < 0.35.
- **Our gap rule.** It separates Greats poorly:
  - 46 of Chess.com's Greats have a gap under 0.05 to our second line;
  - 221 non-Great best moves have a gap ≥ 0.20.
- **Human-move models.** Maia-2 move probability adds almost nothing. Chess.com's median Great has P(played) = 0.64. A cross-validated logistic model on gap, opponent's loss, buckets, move kind and rating band reaches F1 ≈ 0.60 with or without Maia. This agrees with the decompile: Great uses no move-probability model.

### 2.3 Our current rule against the recovered one

| our rule (`facts.rs` `great_find`) | Chess.com | effect |
|---|---|---|
| `require_high_rated`: max Elo ≥ 1000 required | branch selector; low-rated is *more* generous | blocks 206 / 321 |
| EP gap to line 2 ≥ 0.20 | six tag triggers (above) | blocks 203 / 321 |
| not completely winning before | only the key-moment tags check this, and against the mover's *previous* move | blocks 45 / 321 |
| no recapture (all ratings) | high-rated only, and narrower ("simple recapture") | blocks some low-rated Greats |
| free capture is "easy" (all ratings) | high-rated only | same |
| no notion of the opponent's previous error | the key-moment tags need it | most of the missing recall |

### 2.4 Approximate check of the recovered rule on our run

This approximation leaves out `is_easy_to_find`, the grandparent rule, the retreat and simple-recapture exclusions, and the PD model. It is a recall check, not a precision estimate:

| variant | true positives | false positives | missed | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| current rule | 16 | 10 | 305 | 0.62 | 0.05 | 0.09 |
| recovered triggers; opponent's label from Chess.com | 285 | 594 | 36 | 0.32 | 0.89 | 0.48 |
| recovered triggers; opponent's label from our review | 280 | 588 | 41 | 0.32 | 0.87 | 0.47 |

The triggers behind the true positives:

| trigger | count |
|---|---:|
| critical | 219 |
| wins material | 116 |
| winning | 57 |
| comeback | 34 |
| forces mate | 27 |
| free piece | 10 |

Tightening the critical gap to 0.15 or 0.20 leaves precision at 0.32 and only costs recall. So the false positives come from the missing exclusions, not from thresholds. Building them properly is the main work of Phase 1.

## 3. Blunder

### 3.1 Where the 92 differences come from

**Chess.com says Blunder, we say Mistake (32).**
- 14 are engine noise: Chess.com's *own* scores give a Blunder grade by our thresholds.
- 18 are graded Blunder although Chess.com's displayed score loses only 0.157–0.200 EP. Almost all are in games under 1250, and all lose material. The decompile shows **no rule that hardens a move to Blunder**, so the cause is the rating fed into the EP curve (§3.2).
- 5 of the 32 are our `blunder_softened`.

**Chess.com says Blunder, we say Miss (19).**
- 4 walk into a forced mate. Chess.com never calls a mate-allowing move a Miss: 1 of 319 Misses walks into mate, against 34 of 228 Blunders.
- The rest are our Miss detectors (tactic, free piece, opportunity) firing although the opponent did not err. 147 of Chess.com's 228 Blunders follow an opponent move that lost < 0.05 EP. 218 of its 319 Misses follow one that lost ≥ 0.10.

**We say Blunder, Chess.com says Mistake (20).**
- 4 walk into mate from about −5 or worse. Chess.com's threshold is sharp: best score ≤ −494 cp gives Mistake, ≥ −463 gives Blunder (§3.3).
- 11 lose exactly a pawn by our line walk. Chess.com is split on pawn-only losses: of our pawn-only Blunders it calls 16 Blunder, 11 Mistake and 6 Miss.
- The rest are engine noise.

**We say Blunder, Chess.com says Miss (12).** The opponent had just erred: 10 of 12 follow an opponent loss ≥ 0.15. Our Miss detectors did not fire, or guard A blocked them because the move also dropped material.

### 3.2 Rating for low-rated games

The test grades Chess.com's own scores by our thresholds and counts precision labels only:

| band | current (max + 200, floor 1000) | best variant |
|---|---:|---:|
| max Elo < 1000 | 82.0% | 83.8% (floor 1200) / 83.3% (+300) |
| 1000–1499 | 83.6% | 84.2% (floor 1300) |
| 2000+ | 85.0% | no change |

On Blunder alone, using Chess.com's scores:

| floor | Blunder precision | Blunder recall |
|---:|---:|---:|
| 1000 | 0.896 | 0.833 |
| 1200 | 0.926 | 0.882 |

The decompiled `TEP::is_high_rated` and `side_to_move_rating` read the PGN Elos. But an `api::override_merge_game_metadata` exists, so the server may substitute other ratings. That is unproven. A floor of about 1200 is the cheapest stand-in.

### 3.3 Mate and material facts

Recovered `is_losing_material_or_getting_mated` is true when any of these holds:
- a LOSES_MATERIAL event;
- PERMITS+LEADS_TO or PERMITS+WINS_MATERIAL;
- a mate score against the mover with the mover's bucket ≤ 1, **unless the best move was also mated** with bucket ≤ 1.

Our fallback is "material lost ≥ 100 within 6 PV plies, or mated". It is coarser.

At rating 1200, the "bucket ≤ 1" boundary sits at about −494 cp, which is exactly the mate-leniency edge seen in §3.1. This is a second sign that the floor is about 1200.

## 4. Plan (nothing implemented yet)

Measure every step on the 142 games, using the disk-cached engine run (about 1 minute; see the memory note on fast re-runs). Report per-class precision and recall, the tuning and holdout splits, and `coach_verify` = 0. Classification goes through `facts::judge_move`, so the review and explored sidelines stay identical.

### Phase 0: tooling (small)
- Move the scratch scripts into `tools/calibrate/` (as Python, like the existing tools):
  - `class_confusion` (per-class precision and recall, and mismatch lists);
  - `great_triggers` (which trigger or gate fired);
  - the rating scan.
- Add Great and Blunder precision and recall per Elo band to the harness `report.md`.

### Phase 1: rebuild Great on the recovered structure (largest gain)
1. **Rating as a branch.** Remove `great_find.require_high_rated` as a requirement and add `high_rated = max(Elo) > 999` as a branch. When it is false:
   - skip the recapture, checkmate and removes-attacker exclusions;
   - do not treat free captures or obvious recaptures as easy;
   - enable the free-piece key moment.
2. **Context.** `MoveInput` needs the opponent's previous move's precision (not only its EP lost), whether that move was forcing, the mover's EP after their own previous move, and the outcome bucket three plies back. The sideline judge (`analysis/sideline.rs`) must pass the same context, or fall back to "no key moment".
3. **Triggers.** Implement them as separate, traceable facts: forces mate, wins material (gain > 100, not a free piece), free piece (low-rated only), critical, winning and comeback. Record which trigger fired in `rule` for the report and the coach. Gate the key-moment ones on `is_key_moment_candidate`: opponent's move not forcing, EP after ≥ 0.47, Best or Excellent, not completely winning after own previous move, not a recapture.
4. **Remove our proxies.** Drop the 0.20 gap and the "completely winning before" exclusion.
5. **Recovered exclusions.**
   - `is_easy_to_find` in the recovered order (castling never easy; promotion; only safe square; free piece or obvious recapture for high-rated only);
   - the obvious quiet retreat (exists);
   - the simple recapture (high-rated only);
   - the grandparent rule (no capture or passed-pawn push right after a Great-tag move by the same side).

   This is where precision comes from. Measure each exclusion's effect separately.
6. **Optional.** Stand in for the position-difficulty "hard" label (it only *un-excludes* moves). Maia-2's distribution over moves, scored by our engine lines, gives an expected error comparable to the charm model's P(blunder) + 0.75·P(mistake) + 0.25·P(inaccuracy). Only add it if step 5 leaves recall noticeably below 0.85.
7. **Targets.** Recall ≥ 0.80 and precision ≥ 0.60 on tuning, with holdout no more than 5 points worse. Check that Brilliant precedence and recall do not change.
8. **Docs.** Correct `functional-spec.md` §5.5 (address, misattributed gates, the rating gate), `open-questions.md` #5 and #16, and `parity.md`.

### Phase 2: Blunder
1. **Rating floor.** Add `rating_floor` (default 1000; try 1100–1300) applied after the +200 offset. It affects every precision grade, so take it only if overall exact agreement holds on the holdout as well as the low-rated bands. Optionally capture one low-rated review with its `/v2/game-review` metadata to see which ratings Chess.com used (`override_merge_game_metadata`).
2. **Mate-allowing moves.** Never a Miss: add "played move gets mated" to guard A in `classification.rs`. Expected: 4 Blunders right, almost no regressions (1 Chess.com Miss in 319 walks into mate).
3. **Getting-mated softening.** Use the recovered rule: soften a mate-allowing Blunder to Mistake only when the best move was also losing (bucket ≤ 1). This is mostly covered by step 1; verify it separately.
4. **Material fact.** Replace the 100 cp line-walk fallback for `loses_material_or_mated` with the coach's own board events (`coach/` already detects Permits, LeadsTo and WinsMaterial). This is the recovered definition and should settle the pawn-only coin flips. Measure the pawn-only cases separately.
5. **Opponent's error in Miss detectors (coordinate with Miss).** Most Chess.com Misses follow an opponent error, and most Blunders do not. Before letting tactic, free piece or opportunity turn a Blunder into a Miss, require an opponent error (≥ Mistake, as in the recovered key moments). This touches Miss labels, which are currently fine (precision and recall about 0.70), so accept it only if Miss precision and recall do not drop.
6. **Engine noise** (about 14 Blunders and a similar number of Mistakes) remains the known floor; the earlier conclusion still holds (Stockfish 18 is already used).

### Expected outcome

| | now | after the plan (estimate) |
|---|---|---|
| Great precision / recall | 0.62 / 0.05 | about 0.6 / about 0.8 |
| Blunder precision / recall | 0.85 / 0.78 | about 0.88–0.92 / about 0.83–0.87 |
| Overall exact agreement | 68.7% | +2 to +3 points (most of it from 286 Best → Great) |

### Risks
- The decompile is of APK 4.10.15. The web server may run a newer build. The 89% recall on current web reviews suggests the structure still holds.
- The comeback direction and some argument meanings ("Color 2", `includes(c, 0, 0)`) are inferred. Settle them on the data during Phase 1.
- The position-difficulty model cannot be replicated. Some Greats that depend on it ("hard position", so not easy) will stay out of reach.

## 5. Phase 1 result: Great rebuilt (2026-10-23)

Built on branch `claude/great-recovered`; rules in `implementation-notes.md` ("Great Find"),
measurements in `log.md` ("Great rebuilt on the recovered structure").

| | before | after | tuning | holdout |
|---|---:|---:|---:|---:|
| Great precision | 0.62 | **0.81** | 0.79 | 0.84 |
| Great recall | 0.05 | **0.74** | 0.73 | 0.75 |
| Overall exact agreement | 68.7% | **70.9%** | 70.6% | 71.4% |
| khhizr7's Greats (Chess.com 125) | 10 given, 6 right | 121 given, 99 right | | |

**Departures from the decompile.** Three, each because the data disagreed:
- an immediate recapture is never critical, whether or not our exchange test calls it safe;
- the only-safe-square exclusion applies only to threatened pieces other than pawns;
- material gain is our line walk.

**Sidelines.** These share the rule. For a sideline's own earlier moves they know only the loss the
browser sends.

**Not done in Phase 1:** the position-difficulty model (§4 Phase 1 step 6). Recall is 0.74, just
under the 0.80 target. Most remaining misses come from our engine grading the opponent's move one
step milder than Chess.com, or from a second line 0.05–0.10 behind. The difficulty model would not
fix those.

## 6. Phase 2 result: Blunder (2026-10-23)

Rules and measurements: `implementation-notes.md` (Miss subtypes, the mate rule) and `log.md`
("Blunder fixes").

| | before | after | tuning | holdout |
|---|---:|---:|---:|---:|
| Blunder precision / recall | 0.85 / 0.78 | **0.86 / 0.83** | 0.85 / 0.82 | 0.88 / 0.87 |
| Miss precision / recall | 0.71 / 0.70 | **0.79 / 0.68** | 0.78 / 0.68 | 0.79 / 0.69 |
| Mistake recall | 0.61 | 0.69 | 0.69 | 0.70 |
| Overall exact agreement | 70.9% | **71.7%** | 71.3% | 72.5% |

**Built** (plan §4 Phase 2):
- step 1: rating floor 1200;
- steps 2–3: a move into forced mate is never a Miss, and the recovered getting-mated softening;
- step 5: a missed tactic or free piece needs the opponent's error, at least an Inaccuracy's loss.

**Not built:** step 4, the coach's events as the material fact. It changes at most 17 plies, which
Chess.com itself splits about evenly.

**Side effect:** Brilliant recall 0.52 → 0.48 (one fewer correct Brilliant).

## 7. Check on batch 5 (2026-10-24)

435 new Chess.com reviews from ratings below 700 to 2200+ (`log.md`, "Batch 5 check"), measured
with the rules unchanged:
- **Great** holds on new data. In the random sample, precision 0.84 and recall 0.73 (was 0.77 /
  0.10); on the holdout games 0.85 / 0.74. Recall is at least 0.65 in every rating band.
- **Blunder recall** improves everywhere (random sample 0.70 → 0.77). **Blunder precision** stays at
  0.74: Chess.com softens many more Blunders that do not lose material by its definition than the
  142 games showed.
- **Next step:** the coach-event material fact (§4 Phase 2 step 4), now that it has enough examples.


## 8. Brilliant rebuilt (2026-10-24)

### 8.1 What Chess.com's code does (libcee 4.10.15, circumstance 13)

- Brilliant is checked before Tricky and Great, so it always wins.
- Eligible base tags are 15–25: a direct sacrifice (capture or en prise), an ignored threat, an
  indirect sacrifice, their `_MATE` forms, fork-if-captured and underpromotion.
- `is_candidate<13>`: not book; EP after the move ≥ 0.47; no capture of a pawn about to promote and
  no promotion threat; when answering check, the second line must not get mated; and the move is
  Best, or graded Good or better while the best move does not force mate.
- Gates: in the endgame the position must be critical (as for Great) or the line must win ≥ 200; the
  move is rejected when the mover is already ahead by the sacrificed piece's value and the opponent's
  EP before it, at rating 2000, is below 0.10.
- `is_sacrifice` concerns the moved piece: its square is not safe, it is strongly threatened after
  the move, it had a safe square, and in high-rated games (max Elo ≥ 1000) it is worth more than what
  the move captured plus the best piece it newly attacks by discovery. Pieces left standing go through
  `is_sacrifice_of_not_moved`, only partly decoded.

### 8.2 Departures from the decompile (data-driven)

Each was found by tallying our hits against Chess.com's labels on all 575 games.

| Change | Config | Why |
|---|---|---|
| A moved piece must lose material in its own exchange (SEE gain > captured) | `moved_net_loss` | `is_safe(n)` rejects trades; without it trades fired at every rating |
| A piece left standing does not count when the move threatens an opponent piece worth as much | `counter_threat_excludes` | an exchange of threats, not a sacrifice |
| A piece left standing does not count when the move captured a piece worth as much | `standing_trade_excludes` | 0 of 22 such hits were Chess.com Brilliants |
| Moved pawns do not count | `pawns` off | 0 of 84 pawn hits across two runs were Chess.com Brilliants |

The last three are probably parts of `is_sacrifice_of_not_moved` and `strong_see_threats_against`
that the decompile did not reach.

### 8.3 Results (all 575 games, 98 Chess.com Brilliants)

| Run | Rule | Brilliant P / R | Tuning P / R | Holdout P / R | Exact |
|---|---|---|---|---|---|
| br-base | old rule | 0.53 / 0.55 | 0.56 / 0.53 | 0.47 / 0.62 | 68.9% |
| br-v1 | decompile as read | 0.14 / 0.79 | 0.15 / 0.82 | 0.10 / 0.69 | 68.1% |
| br-v2 | + net loss, counter-threat | 0.41 / 0.78 | | | 68.8% |
| br-v3 | + standing trade, no pawns | 0.51 / 0.79 | 0.53 / 0.81 | 0.45 / 0.73 | 68.9% |

Great is unchanged (P 0.84, R 0.76). The remaining extras are mostly pieces left en prise (19 right,
44 wrong in br-v3) and Excellent or Good moves (14 right, 30 wrong); moved-piece sacrifices by the best
move are right 3 times in 4.
