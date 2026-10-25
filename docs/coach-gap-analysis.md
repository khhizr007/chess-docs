# Coach gap analysis after phases 0–3

October 2026. This asks where our coach stands against Chess.com's after phases 0–3, which
differences remain, and whether the planned later phases close them. The design is in
[`coach-analysis.md`](coach-analysis.md), the measuring method in
[`calibration/coach-log.md`](calibration/coach-log.md).

## 1. Summary

**Measured.**

- Run `coach-main-e4ead28`: current `main` with phases 1, 2 and 3 and the Rxd7 fix, on all 142
  calibration games (8,638 plies). The engine is Stockfish 18, depth 18, MultiPV 3, with the default
  threat search.
- Our move labels are identical to the Phase 0 run (68.7% exact, 88.7% within one step). Every change
  below is the coach's.
- The reference is the main event of Chess.com's own speech (Stockfish 18 reviews), captured in
  Phase 0. The full report is
  [`runs/coach-main-e4ead28/coach-report.md`](../tests/calibration/runs/coach-main-e4ead28/coach-report.md).

**Where we stand.** The table compares the event we say first with the one Chess.com says first.

| | Phase 1 (`f5f0b35`) | now (`e4ead28`) |
|---|---:|---:|
| Bad moves both apps label bad (1,641): same tag and circumstance | 22.9% | 22.6% |
| … same tag, any circumstance | 24.1% | 24.7% |
| … they explain, we say nothing | 21.4% | 18.3% |
| Good moves both apps label good (5,349): same tag and circumstance | 0% | **23.1%** |
| … they explain, we say nothing | about 85% (we said nothing on good moves) | 30.1% |
| Best-move sentence on bad moves: same as theirs | not measured | 11.9% |
| … they explain, we say nothing | not measured | 60.5% |
| Forced moves explained (they explain 100%) | 0% | 0% |
| Book moves explained (they explain 30%) | 0% | 5% (only those we label non-book) |

What these numbers say:

1. **Phase 2 brought good moves from nothing to about a quarter agreement.** It also explains about
   50 more bad moves. On bad moves, though, it added events that mostly *differ* from Chess.com's: a
   threat of the played move, where Chess.com speaks about the best move.
2. **Agreement on bad moves did not improve.** The five fixes Phase 0 recommended were never applied,
   because Phase 2 was built at the same time. They are still the cheapest gain.
3. **Most remaining differences are missing vocabulary, not wrong detection.** We have an equivalent
   for 69% of the tags Chess.com uses on bad moves, but only 39% of those it uses on good moves
   (§3.1).

   The largest gaps:
   - trades and recaptures: about 940 good moves;
   - development, castling and structure: about 1,260 good and 325 bad;
   - escaping check: about 290;
   - "kicking" a piece to gain time: about 200;
   - what the *best* move would have done when it is a defence or a threat, not a material gain:
     about 550 bad moves.
4. **Only the positional gap is in a planned phase (Phase 4).** Phase 5 (LLM wording) changes no
   facts. The rest needs a new phase, called Phase 2b below, plus some small quick fixes.
5. **About 300 plies contradict Chess.com's verdict.** On 177 we praise a move Chess.com calls bad
   (134 of them Inaccuracies), and on 120 we criticise one it calls good. This comes from the label
   calibration, not the coach. It is the most visible disagreement for a user, and only the label
   track can close it (§4.7).

**Realistic target.** These are rough estimates from the sizes in §3, assuming about half of each
gap converts.

| | now | after quick fixes and Phase 2b | after Phase 4 |
|---|---:|---:|---:|
| bad, exact | 23% | about 35% | about 40–45% |
| good, exact | 23% | about 35% | about 45–50% |

The ceiling is well below 100%:

- Chess.com's speech is unmatched or generic on about 9% of bad and 14% of good moves.
- About 17% of its bad moves are labelled differently by us.
- Some of its choices are a matter of taste, where we deliberately say more (§4.8).

## 2. What changed since Phase 0

**Bad moves.**

| category (1,641 plies both label bad) | Phase 1 | now | change |
|---|---:|---:|---:|
| exact | 376 | 371 | −5 |
| same tag, other circumstance | 19 | 34 | +15 |
| same family | 76 | 78 | +2 |
| different | 687 | 725 | +38 |
| they explain, we don't | 351 | 301 | −50 |
| we explain, they don't | 81 | 86 | +5 |
| neither | 51 | 46 | −5 |

- The 50 plies we now explain come from Phase 2's THREATENS fallback ("Better was …" after a threat
  of the played move).
- Chess.com usually explains those by the best move instead, so most of them land in "different".
- The −5 exact most likely comes from two Phase 2 changes: gains are now placed on the winner's
  last capture, and the defence tags now compete in the bad-move path. I did not trace this ply by
  ply.

**Good moves.**

| Chess.com class | plies | exact | they explain, we don't |
|---|---:|---:|---:|
| Great Find | 321 | 42.4% | 10.3% |
| Best | 2,621 | 23.5% | 27.4% |
| Excellent | 1,473 | 20.6% | 36.7% |
| Good | 1,116 | 16.1% | 34.2% |
| Brilliant | 25 | 0% | 20% |

- **Great Find works best.** Chess.com's most common Great Find explanation is a free piece (51 of
  321), which we detect.
- **Brilliant gets 0%.** Chess.com explains Brilliants as sacrifices (IgnoresThreat,
  DirectSacrificeCapture/EnPrise). We explain the tactic the sacrifice leads to. We have no sacrifice
  tags.

**Phase 3 (UI)** cannot be measured this way. Against Chess.com's client (`coach-analysis.md` §3.1)
we now have:

- per-fragment highlights;
- Show/Hide lines with per-move narration;
- avatar mood;
- a hint ladder in Retry;
- takeaways.

What is still missing on the presentation side is listed in §4.9.

## 3. Remaining differences, by cause

### 3.1 Vocabulary coverage

This counts the share of Chess.com's main events whose tag has an equivalent in our `Tag` enum,
over all 142 games:

| | plies with a main event | we have the tag |
|---|---:|---:|
| bad moves | 1,802 | 68.6% |
| good moves | 4,770 | 39.4% |
| best-move sentence on bad moves | 1,620 | 40.2% |

The tags we lack, by how often Chess.com uses them:

| family | most frequent missing tags | good | bad |
|---|---|---:|---:|
| trades and recaptures | ObviousRecapture, EqualTrade, ImmediateRecapture, PileTrade, DevelopsRecapture, OffersTrade | ~940 | ~55 |
| development, opening, structure and activity | DevelopsCenter, PreparesToCastleKingside, PreparesBishopDevelopment, CastlesKingSide / SameSide, PutsPawnInCenter, StrikesAtCenter, ConnectsRooks, MovesSamePieceInOpening, TooEarlyQueenDevelopment, MovesPawnInFrontOfKing, ForcesDoubled / IsolatedPawn, PushesPassedPawn*, MovesToActiveSquare, TakesOpenFile, AttacksPawnChain, PassiveRetreat | ~1,260 | ~325 |
| check and tempo | EvadesCheck, Kicks, WinsTempo | ~470 | ~30 |
| game-level | Critical (the only good move), evaluation transitions (EqualToWorse…) | ~25 | ~80 |
| sacrifice | DirectSacrificeCapture / EnPrise, IgnoresThreat (Brilliant) | ~30 | ~33 |

### 3.2 Bad moves: disagreements in detail

These are the largest patterns on the 1,641 plies both apps label bad. The examples are in the run
report.

| # | Chess.com says | we say | plies | cause | closed by |
|---|---|---|---:|---|---|
| B1 | the best move threatened to win material (`misses>CaptureThreat`) | nothing (53), a material gain on B's line (17), a threat of the played move (13), others | 206 (all bad) | No threat search after the best move B: Phase 2 searches after P and before P only | **Phase 2b** |
| B2 | allows a free piece (`permits>FreePiece`) | `ignores_threat` / `bad_trade` | 69 | Priority: the BASE error tag outranks the PERMITS free piece. We detect theirs on 56 | **Quick fix** (Phase 0 item 1) |
| B3 | allows the opponent to win material (`permits>LosesMaterial`) | a named tactic further down R's line (fork 23, removes defender 13, discovered attack 9, …) | ~70 of 195 | We name any tactic up to the gain ply; Chess.com names one only when the reply itself carries it | **Quick fix** (Phase 0 item 3) |
| B4 | the best move would have defended: retreat, defend, escape, evade check, block, recapture | nothing | 94 main events; 346 best-move sentences | Our Misses block only looks for mate or material on B; B never gets the good-move analysis | **Phase 2b** |
| B5 | the only good move was … (`misses>Critical`) | nothing | 42 | No "only move" event | **Phase 2b** |
| B6 | an opening or structure error (moves the same piece, pawn in front of the king, development) | nothing | ~325 (all bad) | No positional tags | **Phase 4** |
| B7 | a mate further away (`permits>ForcesMate`) | `back_rank_mate` | 12 | We name the mate pattern for the whole line, not only the mating move | **Quick fix** (Phase 0 item 5) |
| B8 | hangs the moved piece (`HangsPiece`) | `permits>free_piece` | 8 | The "base outweighed" filter compares the whole line's gain | **Quick fix** (Phase 0 item 4) |
| B9 | the position slid from equal to worse (`EqualToWorse` …) | nothing | 36 | No evaluation-transition remark | **Phase 2b** (small) |
| B10 | a capture loses a trade (`permits>wins_material>PileTrade`) | `free_piece` / nothing | 22 | No trade tags | **Phase 2b** |

### 3.3 Good moves: disagreements in detail

| # | Chess.com says | we say | plies | cause | closed by |
|---|---|---|---:|---|---|
| G1 | a recapture or an equal trade | nothing (388), "stops X winning a piece" (139), free piece (81), removes defender (66) | 941 | No trade or recapture tags. A recapture is then explained as preventing a free piece, which is true but odd | **Phase 2b** |
| G2 | the development, castling and centre move it is | nothing | ~800 | No positional tags | **Phase 4** |
| G3 | the king steps out of check (`EvadesCheck`) | nothing | 265 | We have BlocksCheck but no king evasion or capture of the checker | **Phase 2b** |
| G4 | kicks a piece / wins a tempo (`Kicks`, `WinsTempo`) | "threatens to win the piece" (147) | 206 | Our threat test passes any attack the opponent must answer. Chess.com calls a threat that is answered just by moving the piece a *kick*, not a threat. Our wording overstates it | **Phase 2b** |
| G5 | Brilliant: a sacrifice | the tactic it leads to | 23 | No sacrifice tags | **Phase 2b** (small) |
| G6 | the only good move (`Critical`) | something else | 24 on Great Find | No "only move" event | **Phase 2b** |
| G7 | — (no event) | free piece, material gain, threat | 279 | Chess.com stays quiet on many routine captures. Harmless; candidate for rating gates | Phase 4 (gates) |

### 3.4 Moves we leave empty

- **Forced moves** (114): Chess.com always says "this was forced". We send an empty note. A one-line
  fix.
- **Book moves** (980):
  - Chess.com explains 30%, mostly with development tags (DevelopsCenter 49, PreparesToCastle 44,
    PreparesBishopDevelopment 35).
  - Phase 4's development tags cover those.
  - Its FEN-specific opening remarks (9,800 entries in its asset) would need an opening-ideas corpus
    of our own. That is a separate, mostly editorial task.

## 4. What closes each gap

### 4.1 Quick fixes: no new phase, about 2–4 days

These are the Phase 0 top-5, still valid:

1. **B2.** In `priority.rs`, rank the PERMITS free-piece event above `ignores_threat` and
   `bad_trade`. Keep the base tag only when the piece is lost to an exchange, and word it as losing
   material.
2. **B3.** Name a tactic only when it is R's first move, or within a short forcing line. Otherwise use
   `material_gain`, worded as "allows … to win material". Tighten Fork so each target is worth more
   than the forker or is undefended.
3. **B7.** Name a mate pattern only for the mating move. Longer mates are `forced_mate`.
4. **B8.** Keep `HangsPiece` when the PERMITS event wins that same piece.
5. **Forced moves:** say "the only legal move", from the existing text.

Expected gain: about +130 exact on bad moves (+8 points). Measure it with the existing harness.

### 4.2 Phase 2b (new): best-move speech, trades, check, tempo, about 2–3 weeks

This is the largest gain, and no planned phase covers it.

1. **Speak the best move like a played move (B1, B4, B5).**
   - Run the good-move pipeline on B: BASE tags (defence tags included), its own line, and a
     **null-move threat search after B**, to find what B threatens.
   - The Misses block then says what B *does*: "Nc3 would have defended the pawn", "a3 would have
     threatened to trap the bishop".
   - Add `OnlyMove` (Chess.com's Critical): B is the only move within the Good band, measured with the
     MultiPV lines we already have.
   - Cost: one more shallow search per bad move, about 1% of review time by the Phase 2 measurement.
2. **Trades and recaptures (G1, B10).**
   - Add tags in priority order: `Recapture` (obvious or immediate), `EqualTrade`, `WinsTrade`
     (Chess.com's PileTrade, winning on a contested square), `LosesTrade`, `OffersTrade`.
   - Recaptures then stop being phrased as preventing a free piece.
3. **Check and tempo (G3, G4).**
   - Add `EvadesCheck` (king move, or capturing the checker) next to `BlocksCheck`.
   - Add `Kicks` / `GainsTempo`: the threatened piece has a safe square, so the threat is answered by
     moving it.
   - Keep THREATENS only when the threatened piece cannot simply move away, or the threat is mate.
     This also fixes our overstatement on 147 good moves.
4. **Small events.**
   - Evaluation transitions (B9): "this let the position slide from equal to worse", for
     Inaccuracies with no tactic.
   - Sacrifice tags for Brilliant moves (G5): the moved piece is en prise and the opponent's threat is
     ignored. The existing `static_sacrifice` already decides this.

Expected gain: about +12 points on bad moves, +12 on good moves, and +25 on the best-move sentence.

### 4.3 Phase 4 (planned): positional, rating gates, Maia-2

- Closes B6, G2 and most of §3.4: development, castling, centre, pawn structure, activity, open files.
- It is the largest single family on good moves (24%) and the second on bad (17%).
- Rating gates (Chess.com hides structure ideas below 900–1100) also decide G7: when to stay quiet.
- Maia-2 changes the *framing* ("hard to find at your level"), not the tags. Agreement does not
  measure it.
- **Done** (`118a076`, run `coach-phase4`, [`calibration/coach-log.md`](calibration/coach-log.md)
  "Results: Phase 4"): good-move exact 58.3%, bad-move exact 39.2%, opening-phase bad moves 34.4%,
  best-move sentence 46.0%. The gates barely touch G7: tactics and captures have no gate, and we
  still speak on 381 of the 743 good moves where Chess.com says nothing.

### 4.4 Phase 5 (planned): optional LLM wording

It changes no facts, so it closes none of the differences above. Keep it last, as planned.

### 4.5 Voice: "you" or "White"

- Chess.com speaks to the player ("you allow…"). We use the neutral style ("White allows…") because
  the API does not know which side the user played.
- Fix: a `player_side` request field. The frontend sets it from a "this is me" choice, or by matching
  a remembered username against the PGN headers.
- The realiser already has the `you` / `opponent` styles. Small; can go with the quick fixes.

### 4.6 Things we deliberately do differently (not gaps)

- **Concrete squares and lines in the sentence.** Chess.com's sentences are generic and rely on
  arrows. Ours name the move and piece. Keep this.
- **A named tactic where Chess.com says "loses material"** is sometimes more informative. B3 narrows
  it to cases where the tactic is genuinely immediate, rather than dropping it.
- **No audio, no FEN-specific opening remarks, no bot personalities.** These are out of scope unless
  the product needs them.

### 4.7 Label contradictions: not a coach problem

On 297 plies the labels point in opposite directions:

- we praise 177 moves Chess.com calls bad (134 Inaccuracies, 39 Mistakes);
- we criticise 120 it calls good (94 of them Good).

The coach follows our label, so its tone follows too. The label track
([`calibration/log.md`](calibration/log.md)) owns this. Its documented ceiling is about 87% on the
graded labels, even with Chess.com's own scores, because Chess.com's scores come from a search tree
we cannot reproduce exactly.

Two coach-side hedges are worth doing regardless:

- For a "Good" move that lost close to the Inaccuracy threshold, don't use the praise frames: say
  what it does, neutrally.
- For an Inaccuracy close to Good, lead with the better move, not with "allows".

### 4.8 What agreement cannot tell us

Agreement measures *what* is said, not whether it is correct or useful:

- the 279 good moves where only we say something;
- the cases where we name a real but different idea.

Neither is necessarily wrong. Two checks from `coach-analysis.md` §8 should run next to this one:

- the automatic fact check (every square, piece and move in a sentence exists);
- a small human rating of sampled moves.

### 4.9 Presentation differences remaining

| Chess.com | us | plan |
|---|---|---|
| Board markings on every bad move and 42% of good moves | marked fragments when the event has geometry | follows from more events (Phase 2b, 4) |
| Show-moves buttons on 98% of bad moves | show-lines only for events with a line | Phase 2b (B's line for every best-move sentence) |
| Avatar emotion mostly "idle", "thinking" or "shocked" on errors | derived from the class | fine as is |
| Rating-gated wording | none | Phase 4 |
| Personal voice | neutral | §4.5 |
| Voice audio, opening remarks | none | out of scope |

## 5. Revised plan

| order | work | closes | effort | measure with |
|---|---|---|---|---|
| 1 | Quick fixes (§4.1) and player side (§4.5) | B2, B3, B7, B8, forced moves | 2–4 days | `coach_compare.py`, bad exact ≥ 30% |
| 2 | **Phase 2b** (§4.2) | B1, B4, B5, B9, B10, G1, G3–G6 | 2–3 weeks | best-move sentence exact ≥ 30%; good exact ≥ 35% |
| 2 (parallel) | Label-track work on near-threshold moves (§4.7) | contradictions | ongoing | `log.md` |
| 3 | Phase 4: positional tags, rating gates, Maia-2 | B6, G2, G7, book moves | 2–3 weeks | good exact ≥ 45%; opening-phase bad exact |
| 4 | Fact checker and human rating (§4.8) | quality, not agreement | 1 week | `coach-analysis.md` §8 |
| 5 | Phase 5: LLM wording (optional) | wording only | 1 week | fact-check pass rate |

Each step re-runs the comparison on the stored captures. Measuring a new commit takes about 70
minutes of review time in WSL, and needs no new Chess.com capture.

## 6. How this was measured

- **Tool changes in this run** (`tools/calibrate/`):
  - `coach_tags.py` maps the four Phase 2 defence tags to Chess.com's, and treats a THREATENS
    material event as the same tag as Chess.com's CaptureThreat (and a THREATENS / PREVENTS mate as
    its MateThreat).
  - `coach_compare.py` adds the good-move section and the best-move-sentence comparison.
- **The same commands as in `coach-log.md`**, with run `coach-main-e4ead28`. The server was built from
  `e4ead28` in WSL and run on port 8096.
- **Vocabulary and gap sizes** in §3 come from the per-ply records written by `coach_compare.py
  --records`. They are kept locally next to the captures and contain tags only.
- **No Chess.com text is in this document or the repository.** The tag names are generic chess terms.

## 7. Status after Phase 4 (main `582bdd9`, 2026-10-21)

Run `coach-main-582bdd9`: merged main (quick fixes, Phase 2b, the taken-back rule, Phase 4 and the
Maia-2 move-11 fix). It reused the depth-18 engine results of the Phase 4 run through the local disk
cache (`coach-fast-reruns`; 8 of 19,200 searches were new). The labels are unchanged (68.7% exact).
The numbers equal the Phase 4 run, as expected: the Maia-2 fix only changes wording.

| | phases 1–3 | quick fixes | Phase 2b | **now** |
|---|---:|---:|---:|---:|
| bad moves both label bad (1,641): exact | 22.6% | 29.6% | 35.4% | **39.2%** |
| … they explain, we say nothing | 18.3% | 18.5% | 7.1% | **1.5%** |
| good moves both label good (5,349): exact | 23.1% | 23.4% | 44.3% | **58.3%** |
| … they explain, we say nothing | 30.1% | 30.1% | 17.4% | **2.9%** |
| best-move sentence: exact | 11.9% | 12.1% | 37.6% | **46.0%** |
| … they explain, we say nothing | 60.5% | 60.9% | 15.1% | **3.6%** |

The quick-fix column's bad-move rows come from the `cb1b475` run (`coach-quickfix`). Its good-move and
best-move rows come from the `d25b1b7` run quoted in coach-log "Results: Phase 2b". Phase 2b was
measured on `14186c4`.

By Chess.com class (all plies, exact): Blunder 60.5%, Great 55.5%, Best 60.5%, Excellent 56.6%,
Good 46.8%, Miss 36.4%, Mistake 34.3%, Brilliant 36%, Inaccuracy 21.6%.

**Held-out games agree as well as tuning games.** The tuning set (99 games) gives bad 38.7%, good
58.4%, best-move sentence 45.8%. The holdout (43 games) gives 40.2%, 58.0% and 46.2%. The phases did
not overfit the games they were tuned on. All 142 games come from one account, though: the human
players are mostly rated 820–950 (median Elo 949), plus some bot games.

### 7.1 What is left

1. **Silence is solved; choice is not.**
   - Where Chess.com explains a move, we now nearly always say something too.
   - The remaining gap is *which* reason we pick:
     - "different" is 44.1% of bad moves and 18.9% of good moves;
     - on 345 of those bad moves and 438 good ones, Chess.com's reason is among our detected
       events, but our priority picks another.
   - The patterns form a long tail. The largest are:
     - a developing move that pins (we: pin; they: develops), 15;
     - a central pawn hit (we: kicks; they: strikes at the centre), 14;
     - a trade that doubles pawns, 11;
     - a passed-pawn push or a check evasion that we say as a mate threat, 11 each.
   - Several of ours are defensible (a mate threat outranks "evades check").
2. **We speak where Chess.com is quiet:** 383 good moves and 119 bad, mostly routine captures and
   positional remarks. The rating gates do not touch tactics.
3. **The verdict sometimes contradicts Chess.com.**
   - On 275 moves we praise what Chess.com calls bad (mostly Inaccuracies). On 167 we criticise what
     it calls good.
   - That is up from 297 after phases 1–3, because more moves now get a note. The label disagreement
     underneath is unchanged.
   - The near-threshold hedge of §4.7 is not done yet.
4. **Agreement is not correctness.**
   - Nothing yet checks that our sentences are *true* (every piece, square and line).
   - No detector has been checked against an independent labelled set (the lichess puzzle themes).
   - No human has rated the notes.
5. **Measurement limits.**
   - Forced moves get a sentence without an event, so the comparison counts them as unexplained
     (0 of 114). This is a tool artifact.
   - Rating gates and Maia-2 wording are untested above about 1000 Elo.

### 7.2 Next steps

| order | work | why | measure |
|---|---|---|---|
| 1 | **Fact checker**: verify every claim in a note against the position and line (piece on square, move legal, the stated gain occurs on the line, the threat exists). Run it on all 142 games. | Correctness is unmeasured. Required before any LLM wording | claims checked, false-claim rate (target < 1%) |
| 2 | **Independent detector check** on the lichess puzzle database (CC0, theme labels): precision and recall per tag. | Agreement with Chess.com does not prove a detector is right | precision ≥ 0.9 on fork, pin, skewer, hanging piece, discovered attack |
| 3 | **Human rating** of about 100 sampled notes across classes (correct / relevant / specific / useful) | The only measure of usefulness | mean scores; list of bad notes |
| 4 | **Second calibration set at other ratings** (1200–2200 players), captured with the Phase 0 tooling | Gates, positional tags and Maia-2 are untested above 1000 | agreement by rating band |
| 5 | **Priority tuning from data**, bounded: learn reorderings on the tuning games, keep only changes that also hold on the holdout and read well | The 345 + 438 "detected but not chosen" moves | +3–5 points expected, not more |
| 6 | **Near-threshold hedge** (§4.7) and a `Forced` event for the comparison | The 442 tone contradictions, and the 0-of-114 artifact | contradictions with a praise or blame frame |
| 7 | **Wording**: more variants per frame, no repeats within a game, then optionally Phase 5 (LLM rephrasing gated by the fact checker) | Readability; the facts are now good enough to be worth phrasing well | fact-check pass rate, human scores |

The comparison against Chess.com stays as a regression check on every change (about a minute with the
engine cache), but it is no longer the main target.

**Step 1, fact checker: done** (`4b84721`, run `coach-verify-4b84721`; `implementation-notes.md`
"Coach fact checker"). `coach/verify.rs` reads each note as text and checks 101,440 claims in the 142
games: pieces on squares, moves legal and on their line, gains, mates, geometry and arrows, show-line
narrations. At `582bdd9`, 75 of 8,884 sentences (0.84%) had a false claim, all of them an arrow (a
block drawn as a guard, the central push drawn as an attack, king-shelter marks drawn from squares
that attack nothing), and 12 of 24,274 narrations named the wrong square for an en passant capture.
After the fixes: 0 and 0. 133 mates in 7 or more are past the 12 plies the coach keeps and stay
unchecked. Changed claims are caught 97–100% of the time (mates: every one the line can show), and
the Chess.com agreement is unchanged.
