# Where we still differ from Chess.com, label by label (2026-10-24)

All 575 calibration games, 42,049 scored plies, measured on `main` plus the pinned-capture fix of §5.
New evidence in this round:

- **Chess.com's own code, run.** WSL `~/work/cee-emu` loads the shipped `libcee.so` 4.10.15 in the
  Unicorn CPU emulator and calls its own `Position::from_fen` and `collect_eval_terms`. Every
  per-square threat table can now be compared with ours on any position.
- **Chess.com's opening book**, extracted from the same library (§3).
- **Engine re-runs** at Chess.com's reported depth with three Stockfish versions (§1).
- **A web survey** of every public source on Chess.com's classification (§7). The source list is
  kept locally, outside the repo.

Nothing from Chess.com is committed (THIRD_PARTY.md): the library, the book and the captures stay in
WSL `~/work` as local oracles only.

## 0. Agreement per label

| Label | Chess.com count | P / R | Holdout P / R |
|---|---|---|---|
| Book | 3,605 | 0.95 / 0.80 | 0.94 / 0.79 |
| Brilliant | 98 | 0.74 / 0.83 | 0.73 / 0.73 |
| Great | 1,618 | 0.84 / 0.76 | 0.85 / 0.77 |
| Best | 13,429 | 0.78 / 0.83 | 0.78 / 0.83 |
| Excellent | 7,609 | 0.53 / 0.58 | 0.53 / 0.59 |
| Good | 5,699 | 0.55 / 0.52 | 0.53 / 0.52 |
| Inaccuracy | 4,123 | 0.61 / 0.58 | 0.62 / 0.59 |
| Mistake | 3,188 | 0.69 / 0.65 | 0.70 / 0.64 |
| Miss | 1,638 | 0.78 / 0.64 | 0.75 / 0.63 |
| Blunder | 1,042 | 0.78 / 0.79 | 0.77 / 0.77 |

Exact agreement 69.0%. Tuning and holdout agree on every label, so none of the rules is overfitted.

## 1. Most disagreement is the engine, not the rules

**Test.** Apply our precision rule (Best, then EP-lost cut-offs 0.02 / 0.05 / 0.10 / 0.20) to
Chess.com's **own** scores of the played and best moves, from its review data.

| | Agreement with Chess.com's grade |
|---|---|
| Our grade (our engine's scores) | 66.9% |
| Our rule on Chess.com's scores | **89.5%** |

So 22.6 of the 33 points of disagreement on the six precision grades come from score differences,
not from the rules. The rules themselves are confirmed by the decompile: `classification::precision`
uses exactly 0.02 / 0.05 / 0.10 / 0.20 (read from the binary), the curve is
`centipawns_to_expected_points` with slope `−0.004 · (0.0685 · R − 12) / 100`, and the mate override
(`FUN_0136c1f4`) is the one we implement.

**Can the engine gap be closed?** 1,500 random positions after the played move, re-searched single
thread at Chess.com's reported depth (its depths are 14–21, mostly 17–19):

| Engine | Median abs. cp difference | 90th percentile | Same score exactly |
|---|---|---|---|
| Our run (SF 18, depth 18, MultiPV 3) | 11 | 52 | — |
| SF 18 at Chess.com's depth | 10 | 45 | 4.9% |
| SF 16.1 at Chess.com's depth | 13 | 62 | 4.0% |
| SF 16 at Chess.com's depth | 19 | 90 | 3.8% |

Chess.com's setting is labelled "Stockfish 16 NNUE", but SF 16 is the furthest away, and no version
reproduces its scores (under 5% exact). Its scores come from its own server setup (threads, hash and
search history), which cannot be replicated. A median 10 cp difference is about 0.007 EP, a third of
the narrowest cut-off. This is the floor for Best / Excellent / Good / Inaccuracy. **Small gain
available:** searching at Chess.com's depth instead of 18 (11 → 10 cp).

## 2. Rating used by the expected-points curve (unresolved)

- The decompile (`node_lib::elo_rating_for_expected_points`): `clamp(max(WhiteElo, BlackElo),
  1000, 2500)`, or 2000 when there is no game. The app sends the ratings to the library as UCI
  options (`setoption name WhiteElo/BlackElo`, `ChessExplanationEngineImpl`).
- Our setting, calibrated earlier: max Elo + 200, clamped to 1200..3000.
- On Chess.com's own scores, ours reproduces its grades better (83.3% of non-mate cases) than the
  decompiled rule (78.8%). Per game, the rating that best reproduces Chess.com's grades is about
  1,200 for players under 1,000, and about max Elo + 300–400 above 1,500.

So the rating Chess.com feeds in is not the PGN Elo. A plausible input is the player's current or
peak rating, or a server-side estimate, but the review data does not carry it. We keep the
calibrated setting. Fitting a per-band rating would be tuning to labels and is not done.

## 3. Book: Chess.com uses its own 53,972-position book

`TEP::Book::load_embedded_blob` reads `embedded_book` (2.6 MB in `.rodata`): an 8-byte size, then
zlib. Inside are 53,972 records of 32 bytes keyed by the **Polyglot hash**, plus move lists and
names. Checked on every ply of the 575 games:

| Rule | Agreement | Book P / R |
|---|---|---|
| Ours (lichess `chess-openings` lines) | — | 0.95 / 0.80 |
| Position after the move is in Chess.com's book | 99.50% | 0.945 / 1.000 |
| Positions before **and** after the move are in it | **99.67%** | 0.963 / 1.000 |

So Book is fully explained: same rule, bigger book. We cannot ship Chess.com's book. **Fix to
build:** a book of our own from public games (lichess database, CC0). The records carry game counts
(e.g. 1,333 / 1,490 for the first entry), which suggests a "played often enough" criterion. Measure
on the 575 games before switching.

## 4. Miss

Chess.com's Misses: 1,638. We find 1,048 and add 301.

- **Missed (590):** we call them Mistake (257), Inaccuracy (176), Blunder (95) or Good (33).
  Chess.com's coach tags on these moves name what was missed: FreePiece (128 + QuasiFreePiece 10),
  CaptureThreat (65), TakesOpportunity (42), Critical (36), Fork (37), PileTrade (21), StillMate (17).
- With Chess.com's scores, its Misses lose 0.09–0.26 EP (median 0.17): Mistake or Blunder strength,
  as our rule requires.
- **Next step:** decode Chess.com's Miss circumstance the way Brilliant and Great were. The free-piece
  and capture-threat misses use the same threat tables now checked in §5, so they can be compared
  directly with the emulator.

## 5. Brilliant: Chess.com's threat tables, compared square by square

The emulator dumps Chess.com's `see_threats_to[sq]`, `see_threats_against[colour]` and
`strong_see_threats_against[colour]`. Ours come from the same SEE code the sacrifice test uses.

Two harness issues were fixed first:
- the slider attack tables are built by `clueInit`, `TEP::init_magics` and `init_super_inc_tables`,
  not by the static constructors;
- `rand` needed a real generator.

After that, seven hand-made positions agreed exactly.

| 2,000 random positions | see_threats_to identical | strong threats identical |
|---|---|---|
| Before the fix | 98.0% | 99.0% |
| After the fix | **99.4%** | **99.8%** |

**The difference found:** our per-capture SEE let a piece pinned to its own king capture off the pin
line. `collect_eval_terms` skips those captures (`violates_pin`). Fixed in `detectors::capture_see`.

| Brilliant (575 games) | P / R | Tuning P / R | Holdout P / R |
|---|---|---|---|
| Before | 0.72 / 0.83 | 0.73 / 0.86 | 0.70 / 0.73 |
| Pinned-capture fix | **0.74 / 0.83** | 0.74 / 0.86 | 0.73 / 0.73 |

Exact agreement is unchanged at 69.0%, and Great is unchanged.

**What is left in the threat tables (0.6% of positions):**
- an attacker whose capture is legal but whose exchange we score differently when kings take part
  (`to[h2] ours+f3`);
- promotion squares (`to[b8]`, `to[d8]` with a pawn on the seventh rank);
- a few x-ray cases.

They are too rare to explain most of the 29 remaining wrong Brilliants. Those come from the parts of
the Brilliant decision that read engine lines (`saved_pieces`, `defensible_by_alternative`, the
material and score gates, the critical-position test) and from engine score differences (§1). The
next comparison is whole-move: the emulator can call `node_lib::is_sacrifice` and the other
predicates once a `Node` can be built. That needs the game tree (`Tree`, `Node`, scores) set up in
emulated memory, which is the next harness step.

## 6. Great and Blunder

- **Great:** P / R 0.84 / 0.76 on both splits (great-blunder-analysis.md §2).
- **Blunder:** 0.78 / 0.79. Of Chess.com's 1,042 Blunders, we call 158 Mistakes and 54 Misses.
- Both depend on EP loss and line material, so they inherit the engine floor of §1.

## 7. What public sources say

The full survey (17 sources, quoted) is kept locally in
`C:\Users\khhizr\.kiro\crew\workspace\scratch\classification-sources.md`.

- Chess.com's help article gives the same EP cut-offs (0.02 / 0.05 / 0.10 / 0.20) and says EP
  depends on rating.
- Game Review V2 (2023): a Blunder must lose material or allow mate. Already modelled.
- A staff article (NM Kane): "in the endgame a Brilliant sacrifice must be the only good move".
  This matches our endgame gate (critical position, or a line that wins at least 200).
- Every open-source reimplementation found uses a centipawn-loss model, not expected points, and a
  simple hanging-piece test for Brilliant. None claims measured agreement with Chess.com.
- No public source gives the engine settings, the rating input, the book or the CAPS2 accuracy
  formula. The only new item is the book's source data (§3), and that comes from the binary, not
  from an article.

## 8. Plan

| Step | Label | Expected effect | Overfitting risk |
|---|---|---|---|
| Build our own book from public games, matching the extracted book's criterion | Book | recall 0.80 → about 0.97 | none: measured against the book, not labels |
| Search at Chess.com's reported depth | all grades | 11 → 10 cp median | none |
| Decode the Miss circumstance; compare its threat inputs with the emulator | Miss | part of 590 misses | none: decompile only |
| Emulate whole-move predicates (`is_sacrifice`, `ignored_threats`) on the remaining Brilliant cases | Brilliant | shows each remaining rule difference | none |
| Rating input | all | unknown | needs Chess.com's actual input; not tuned |
