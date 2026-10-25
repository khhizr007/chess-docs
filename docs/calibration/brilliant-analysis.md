# Brilliant: why we differ from Chess.com, and the plan

Analysis of commit `62704b1` (run `br-v3`) against Chess.com on all 575 calibration games
(42,049 scored plies, 98 Chess.com Brilliants). Written 2026-10-24, before any further change.

## 1. Summary

| | Count |
|---|---|
| Chess.com Brilliants | 98 |
| Ours | 151 |
| Both (right) | 77 |
| Missed | 21 |
| Extra (wrong) | 74 |

Precision 0.51, recall 0.79. The differences have four sources:

| Source | Missed | Extra | Fixable? |
|---|---|---|---|
| Our "threatened" is weaker than Chess.com's "strongly threatened" | 0 | 14 | Yes, decoded (§4.1) |
| Our safe-square test is stricter than Chess.com's | 6–8 | ? | Yes, decoded (§4.2) |
| Pieces left standing: `is_sacrifice_of_not_moved` and the walk-back are only approximated | 4 | 46 | Partly, needs decoding (§4.4) |
| High-rated branch, material gate, saved pieces: approximations | 7 | ? | Needs decoding (§4.5–4.7) |
| Engine differences (our Stockfish 18 at depth 18 vs Chess.com's engine) | 3 | 7 | No (§5) |

The engine-noise floor is about 10 of 172 disagreeing or shared cases. Everything else is a rule
difference that the decompile can settle. No rule below was chosen by fitting thresholds to labels.

## 2. Evidence used

1. **Our trace.** A copy of the backend (never committed, `~/work/brtrace`) logs every Brilliant gate
   and every sacrifice candidate with the reason it was rejected. The traced run reproduces `br-v3`
   exactly (P 0.51, R 0.79).
2. **Chess.com's labels and scores** (`tests/calibration/cc-reviews/*.sf.txt`).
3. **Chess.com's coach tags** (local oracle, `~/work/chesscom/oracle/captures/*.keys.json`, never
   committed). Each Brilliant carries the base tag that made it one, with the piece, e.g.
   `IgnoresThreat/rook[Brilliant]`. This tells us which sacrifice Chess.com saw.
4. **The libcee 4.10.15 decompile** (Ghidra project `~/work/chesscom/ghidra`, scripts
   `~/work/re-great`). New this round: `is_sacrifice`, `is_safe`, `Piece::safe_squares`,
   `ignored_threats`, the `StaticAnalysis` layout and `collect_eval_terms`.

## 3. What the data shows

### 3.1 Which sacrifice Chess.com saw, and whether we found it

| Chess.com tag | Found | Missed |
|---|---|---|
| DirectSacrificeCapture (moved piece, captures) | 41 | 8 |
| DirectSacrificeEnprise (moved piece, no capture) | 15 | 3 |
| IgnoresThreat | 15 | 4 |
| IndirectSacrifice | 3 | 1 |
| …Mate variants | 1 | 2 |
| ForkIfCaptured | 1 | 0 |
| no tag decoded | 1 | 3 |

Our sacrifice kind agrees with Chess.com's tag on every found Brilliant except one.

### 3.2 Chess.com Brilliants are not always its best move

Chess.com hides the best move for a Brilliant. Using its previous-ply score instead: 80 of 98
Brilliants lose nothing, 12 lose up to 0.02 and 6 lose 0.02–0.05. Its "Best" moves always lose
nothing. So the decompile's "Good or better" rule (`near_best`) is real.

### 3.3 Why we missed 21 (from the trace)

| Reason | Count | Cases |
|---|---|---|
| Moved piece "had no safe square" | 6 | Qxc7, Rxg6+, Nd6+, Rxf6, Nxf6+, Rxd7 |
| Ignored threat rejected by our `counter_threat` exclusion | 2 | Rac1, Re8 |
| Ignored threat "could not be saved" (no safe square) | 2 | Bxc3, Bxf3 |
| High-rated "disguised trade": discovered attack counted | 2 | Nfg4+, Qxd4 |
| Material gate | 3 | Rxc6, Bxh2+, O-O-O |
| Moved piece: mutual threat / saves pieces | 2 | Bxf7+, Bxe3+ |
| Endgame gate | 1 | Bxe4 |
| Engine: we grade the move Inaccuracy | 2 | Nf3, gxf3 |
| Engine: our EP after is just under 0.47 | 1 | Rxd5 |

### 3.4 Why we gave 74 extras

Chess.com's label for the move: 32 Best, 15 Excellent, 10 Great, 9 Good, 6 Inaccuracy, 2 Book.
So in 66 of 74 cases Chess.com also judged the move good enough. It just did not see a sacrifice.

| Our sacrifice kind | Right | Wrong |
|---|---|---|
| Moved piece | 58 | 28 |
| Ignored threat | 15 | 39 |
| Left en prise | 4 | 7 |

Ignored threats are the weakest part. Many wrong ones repeat the same piece over several moves
(five in game 185339193636, two in 185743721678).

### 3.5 Label consistency

Only one position and move appears twice: the Traxler 8...Nxg3. Chess.com calls it Brilliant at
max Elo 949 and Best at 1034. That is no noise: 1000 is the `is_high_rated` boundary, and above it
the discovered attack on c4 makes the move a "disguised trade". The decompile predicts both labels.

## 4. What the decompile says

### 4.1 "Strongly threatened" means the exchange wins at least 200

`collect_eval_terms` tries every capture of every piece, scores it with `Position::see_gain`, and
writes three sets:

| SEE of the capture | Set | StaticAnalysis field |
|---|---|---|
| ≥ 0 | the attacker's safe squares | `safe_squares` (+0x4e0) |
| ≥ 100 | "SEE threatened" | `see_threats_against` (+0xb0) |
| ≥ 200 | "strongly SEE threatened" | `strong_see_threats_against` (+0x4d0) |

`is_sacrifice`, `ignored_threats` and `is_indirect_sacrifice` all use the strong set. Our
`min_threat_cp` is 100. With 200, 14 extras go and no right Brilliant is lost. This also explains
why pawns never count: capturing a pawn can never win 200.

### 4.2 A safe square is a move whose own exchange does not lose

`Piece::safe_squares` reads the same table: destinations where the move's own SEE is ≥ 0. An even
trade (rook takes a defended rook) is therefore safe. Ours asks whether the opponent can win material
after the move, ignoring what the move captured, so an even trade counts as unsafe. That is the
likely cause of the six "no safe square" misses, and of the two ignored-threat ones.

`is_safe(n)` (the move itself) is the same test on the played destination. Our `moved_net_loss`
(gain > captured) already approximates it, so it is now decompile-backed.

### 4.3 `is_sacrifice` (moved piece), confirmed

In order: not castling, not game over, `!is_safe(n)`, the moved piece is strongly threatened after
the move, and it had at least one safe square before. If it was strongly threatened before, no
other own strongly threatened piece and no strongly threatened opponent piece may be worth at least
as much. Then `saved_pieces` is computed (its use is still unclear). Then, for high-rated games
only: the piece has a non-pinned threatener, the move is no deflection, and captured value plus the
greatest discovered attack is below the piece's value. Low-rated games return true straight away.

### 4.4 Pieces left standing (`ignored_threats`, `is_indirect_sacrifice`)

- No sacrifice when in check, after a check evasion, at ply 1, with a PROMOTION event, or for a
  mate evasion.
- **Ignored threat:** the most valuable piece strongly threatened both before and after the move.
  There is no safe-square requirement here: our "could have been saved" test is ours, not
  Chess.com's.
- **Walk-back:** go back two plies at a time while the same piece (by piece id) stays SEE-threatened.
  If an earlier node already holds a base IGNORES_THREAT event on that piece, there is no new event.
  Ours checks only the previous own move.
- Then `is_sacrifice_of_not_moved(n, square, true)`: not trapped, not absolutely pinned, relatively
  pinned only if `defensible_by_alternative`, plus checks on pinned or overloaded attackers, safe
  promotion squares, newly created strong threats and the most valuable piece the move threatens.
  Still only partly decoded. Our `counter_threat_excludes` and `standing_trade_excludes` are
  data-driven stand-ins for these checks, and `counter_threat` wrongly rejects two right Brilliants.
- **Indirect sacrifice:** pieces strongly threatened after the move and not SEE-threatened before;
  the most valuable goes through `is_sacrifice_of_not_moved(n, square, false)`.

### 4.5 High-rated branch

`piece_value_of_greatest_discovered_attack` reads `discovered_attack_profile`, not "any piece newly
attacked". Ours counts any newly attacked piece, which wrongly turned Nfg4+ and Qxd4 into disguised
trades. To decode: `discovered_attack_profile`, `has_non_pinned_threatener`, `is_deflection`.

### 4.6 Material gate

Three misses fail it, including a mating sacrifice (Bxh2+). The earlier reading ("opponent's EP
before the move below 0.10 at rating 2000") may have the perspective or the material term wrong.
To decode: the gate's instructions in `compute_board_event<13>` and `material_difference`.

### 4.7 Not yet looked at

`saved_pieces`, the endgame gate's `max_material_gain`, `ForkIfCaptured`.

## 5. What cannot be matched

Ten cases depend on the engine: 3 misses (we grade the move Inaccuracy, or EP after is 0.469) and
7 extras (Chess.com grades the move Inaccuracy, or calls it Book). Chess.com's engine and depth
differ from ours, so these stay. With every rule matched, the best reachable is about 95 of 98 found
with about 7 extras. "Exactly the same as Chess.com" is not reachable while the engines differ.

## 6. Plan

Each step is a rule read from the decompile, not a threshold fitted to labels. Each is measured
alone, on tuning and holdout separately.

1. **Strong threats at 200** for all three sacrifice kinds (§4.1). Expected: −14 extras, no loss.
2. **Chess.com's safe squares** (§4.2): a destination is safe when the move's own SEE is ≥ 0. Use it
   for "had a safe square" and drop the ignored-threat safe-square test. Expected: up to +8 found.
3. **Walk-back by piece** (§4.4): no new ignored threat if an earlier node, while the piece stayed
   threatened, already had one on it.
4. **Decode `is_sacrifice_of_not_moved`** fully, implement it, and remove `counter_threat_excludes`
   and `standing_trade_excludes`. This targets the 39 wrong ignored threats.
5. **Decode the high-rated branch and the material gate** (§4.5, §4.6).
6. Re-check `pawns`: with strong threats it should make no difference, so drop the flag.

## 7. Guarding against overfitting

- **Source of each rule.** Only decompiled logic goes in. A data-driven rule is allowed only if it
  improves both tuning and holdout, and it is named as such in the docs. The two current ones
  (`counter_threat_excludes`, `standing_trade_excludes`) are to be replaced, not tuned.
- **No threshold search.** Constants come from the binary (100, 200, 0.47, 0.10).
- **Holdout.** Tuning and holdout are reported for every step; holdout is never looked at to choose a
  rule.
- **A second, independent test set.** Chess.com also explains its own best move when the player
  missed it. In 255 positions that best move is tagged as a Brilliant sacrifice, and in thousands of
  others it is not. None of these moves was played, so they were never used for tuning. Our rule,
  applied to Chess.com's best move (the same as ours in 225 of the 255), must agree there too.
- **Per-case check.** Every remaining difference is listed with its trace reason, so a change that
  only moves numbers without fixing a named cause shows up.


## 8. Result (2026-10-24, after the plan)

Each step was a rule read from the decompile (reports 2 and 3 in WSL `~/work/claude-scratchpad`),
measured alone on top of the previous one. No threshold was searched.

| Step | Rule | All P / R | Tuning P / R | Holdout P / R | Best-move set, tuning P / R | holdout P / R |
|---|---|---|---|---|---|---|
| start (`62704b1`) | | 0.51 / 0.79 | 0.53 / 0.81 | 0.45 / 0.73 | 0.61 / 0.88 | 0.49 / 0.87 |
| 1 | strong threats, SEE ≥ 200 | 0.56 / 0.79 | 0.60 / 0.81 | 0.47 / 0.73 | 0.63 / 0.88 | 0.54 / 0.87 |
| 2 | reference safe squares | 0.56 / 0.82 | 0.59 / 0.83 | 0.49 / 0.77 | 0.63 / 0.90 | 0.54 / 0.87 |
| 3+4 | `ignored_threats` with walk-back, `is_indirect_sacrifice`, `is_sacrifice_of_not_moved` | 0.60 / 0.83 | 0.62 / 0.85 | 0.56 / 0.77 | 0.66 / 0.94 | 0.59 / 0.91 |
| 5 | moved piece: strong mutual and saved-piece tests, reference discovered attack | **0.61 / 0.85** | 0.62 / 0.88 | 0.56 / 0.77 | 0.65 / 0.95 | 0.59 / 0.93 |

Every step moved tuning, holdout and the independent best-move set (§7) the same way. Exact
agreement (68.9%) and Great (0.84 / 0.76) are unchanged.

**The best-move set** holds Chess.com's own best move in positions where the player did not play it,
its EP after that move is at least 0.47, and Chess.com explained it: 255 tagged as a Brilliant
sacrifice, 11,284 with no sacrifice tag. It was never used to choose a rule. Our sacrifice kind
agrees with Chess.com's tag on all but 4 of the 240 we find.

**New facts from the code.**
- `ignored_threats` picks the single most valuable piece strongly threatened both before and after
  the move; with a tie of equal value there is no ignored threat. It has no safe-square test. Its
  walk-back steps back two plies at a time while that piece stays SEE-threatened on its square, and
  stops the event if an earlier move already carried IGNORES_THREAT on the same piece.
- `is_sacrifice_of_not_moved` rejects the piece when the move saved a piece worth as much, when the
  moved piece was itself threatened and worth as much, when what the piece loses is no more than what
  the move captured plus the best new strong threat it creates, and when the moved piece hits back
  at something at least as valuable that is not the piece's own attacker. Only when ignoring a
  threat: the piece must not be trapped or pinned to its king.
- A discovered attack is a new strong threat by a slider the move uncovers.
- The material gate (§4.6) was re-read in the assembly: it rejects when the mover is ahead by at
  least the piece's value and the parent node's `score()` is below `EP_to_cp(0.10, 2000)`. Both
  decompile reports agree on the comparisons; they disagree on the score's point of view. The
  opponent's view rejects 34 moves Chess.com did not call Brilliant and 3 it did; the mover's view
  rejects none. We keep the opponent's view. The 4 Brilliants it still rejects all have the mover
  ahead by exactly the piece's value.

**Left (15 missed, 54 extra).** Missed: 4 by the material gate at equality (above), 3 engine grade or
EP differences, 1 endgame gate, 7 where we find no sacrifice (three have no Chess.com tag decoded).
Extras: Chess.com called 20 of them Best, 13 Great, 12 Excellent; it saw no sacrifice in any. The
parts still not modelled are `has_pinned_attacker`, `has_overloaded_attacker` (deflection),
`defensible_by_alternative`, the safe-promotion test, `ForkIfCaptured` and the endgame gate's
`max_material_gain` (`moves_better_than(n, 6)`).


## 9. Attacker checks (2026-10-24, second round)

Decompile report 4 (WSL `~/work/claude-scratchpad/brilliant-decompile-report-4.md`) decoded the
attacker checks of `is_sacrifice_of_not_moved` and the high-rated branch of `is_sacrifice`. One claim
was corrected against the code: `overloaded_attacker_profile` requires exactly one SEE-threatener
(`popcount == 1`), not "the first".

| Check | Config | All P / R | Tuning P / R | Holdout P / R | Best-move set, tuning / holdout P |
|---|---|---|---|---|---|
| before (`028eff4`) | | 0.61 / 0.85 | 0.62 / 0.88 | 0.56 / 0.77 | 0.65 / 0.59 |
| attacker pinned (relative or absolute) | `ref_pinned_attacker` | 0.64 / 0.85 | 0.65 / 0.88 | 0.61 / 0.77 | 0.66 / 0.62 |
| attacker overloaded | `ref_overloaded` | 0.62 / 0.85 | 0.64 / 0.88 | 0.57 / 0.77 | 0.66 / 0.59 |
| safe promotion lost | `ref_promotion` | no change | | | no change |
| trapped (threatened, no safe square) | `ref_trapped` | no change | | | no change |
| high rated: non-pinned capturer, no deflection | `ref_deflection` | 0.66 / 0.82 | 0.67 / 0.85 | 0.61 / 0.73 | 0.70 / 0.63 |
| **all five** | | **0.71 / 0.83** | 0.72 / 0.86 | 0.68 / 0.73 | 0.71 / 0.66 |

Best-move set recall stays at 0.94 (tuning) and 0.91 (holdout). Exact agreement 69.0%, Great unchanged.

**Inferred, not decoded:** the pin themes (8, 9) and the trapped theme (31) are built inside
`get_profiles<N>`, which was not decompiled. We use the standard definitions: a pin is an enemy slider
on a line through the piece with a piece of the same side behind it that is the king, worth more than
the pinner, or undefended. A pin by the threatened piece itself does not stop its capture. Trapped
means threatened with no safe square.

**Not modelled yet:** `defensible_by_alternative` (needs the sibling moves' material loss; a relatively
pinned piece always passes), `ForkIfCaptured` (tag 19) and the endgame gate's
`moves_better_than(n, 6)`.


## 10. Pin, trap and alternative-defence rules (2026-10-24, third round)

Decompile report 5 (WSL `~/work/claude-scratchpad/brilliant-decompile-report-5.md`) located the theme
builders: `ThemeProfilesRegistry::compute` → `collect_profiles` → `collect_pieces_profiles<Type,
Color>`. The report's reading of the relative pin swapped the front and back pieces; the rules below
were re-read from the rook collector (`out/dr5b/clean/011a2bd4.c`).

- **Relative pin (theme 9):** a slider sees an enemy piece B behind exactly one enemy piece A; B is
  not a pawn and not the king; with A removed, the slider's capture of B wins at least 100 (SEE); A
  cannot capture the slider losing at most 100; A has a pseudo-legal move off the line; and
  value(A) ≤ value(B). Stored under the pinner's colour.
- **Absolute pin (theme 8):** A is the only piece between the slider and A's king.
- **Trapped (theme 31):** SEE-threatened; no escape (unpinned: no destination with own SEE ≥ 0;
  pinned: none with SEE ≥ −100); no threatener is itself SEE-threatened; the most valuable threatener
  it attacks back, if any, is worth less than 500.
- **`defensible_by_alternative`:** another candidate graded Good or better whose line loses no
  material (`material_lost < 1`). We use the engine's other MultiPV lines. Not modelled: the
  pawn-tension exception (a loss of exactly 100 that only resolves pawn tension counts as 0).

| Rule | Config | All P / R | Tuning P / R | Holdout P / R | Best-move set, holdout P |
|---|---|---|---|---|---|
| before (`70ec97a`) | | 0.71 / 0.83 | 0.72 / 0.86 | 0.68 / 0.73 | 0.66 |
| decoded pins | `ref_decoded_pins` | **0.72 / 0.83** | 0.73 / 0.86 | 0.70 / 0.73 | 0.68 |
| decoded trapped | `ref_decoded_trapped` | no change | | | no change |
| relative pin needs an alternative defence | `ref_relative_pin_defensible` | no change | | | not measurable |

Only `ref_decoded_pins` improved all three, so only it is on by default. The other two stay off: they
are decoded rules, but they change no result.

**Why precision stops near 0.72.** In all 31 remaining wrong Brilliants, Chess.com attaches no
sacrifice tag at all. Its sacrifice detector does not fire where ours does. Every check named in its
code is now built, so the remaining differences sit inside the shared primitives: `see_gain` and
`see_greater_equal` (x-rays, pins and king captures inside the exchange), the per-square threat
tables of `collect_eval_terms`, and `most_valuable_pieces` ties. Comparing those needs Chess.com's
values for the same positions; the next step is to run the shipped `libcee.so` on the 31 positions
and compare its threat tables with ours.

## 11. Threat tables checked against Chess.com's own code (2026-10-24)

Chess.com's `collect_eval_terms` was run in an emulator (WSL `~/work/cee-emu`, not committed) and its
per-square threat tables were compared with ours (details in `mismatch-analysis.md` §5). One
difference was found and fixed: a piece pinned to its own king does not threaten captures off its
pin line (`violates_pin`). After the fix, 99.4% of 2,000 random positions have identical
`see_threats_to` and 99.8% identical strong-threat sets.

| Run | All P / R | Tuning P / R | Holdout P / R |
|---|---|---|---|
| before (`c783bf8`) | 0.72 / 0.83 | 0.73 / 0.86 | 0.70 / 0.73 |
| pinned-capture fix | **0.74 / 0.83** | 0.74 / 0.86 | 0.73 / 0.73 |

The threat tables are no longer the cause of the remaining wrong Brilliants. Those come from the
engine-line parts of the decision and from engine score differences.


## 12. Whole-move Brilliant run inside Chess.com's own code (2026-10-25)

§11 left the threat tables matching Chess.com and the remaining differences "in the
engine-line parts of the decision". This section runs those parts -- Chess.com's actual
`compute_board_event<13>`, `is_candidate<13>`, `is_sacrifice`, `ignored_threats`,
`is_sacrifice_of_not_moved` and `is_indirect_sacrifice` -- inside the Unicorn emulator, on
the positions behind our 29 wrong and 17 missed Brilliants, and traces each disagreement to
the exact predicate that differs.

### 12.1 What was built

The emulator (`~/work/cee-emu`, not committed) previously ran only `from_fen` +
`collect_eval_terms` (threat tables). It now builds a full Chess.com `Game`/`Tree`/`Node`
for a whole game from the local coach capture and calls the real Brilliant decision:

- `make_game` + `Conf::set<48/50>` (WhiteElo/BlackElo) build the tree with the game's ratings.
- Each ply's Chess.com best line and played line (the "Show Follow-Up" moves) are attached as
  scored variations via `Tree::set_analysis_root` + `Tree::var(line, ScoreWithDepth)`, using
  Chess.com's own cp/mate scores (mate `n` -> `+-(32001-2n)`, mate-0 -> 32000).
- `classification::classification(node)` then returns Chess.com's own label for the move.

Four library facilities had to be supplied before the decision would run: real `libm`
(`exp`/`log`/`pow`/... were stubbed to 0, which broke `expected_points`); an in-run
`pthread_once` trampoline (a nested `emu_start` ended the outer call); the score-sign
convention (`Node::score` is the mover's view); and a substitute for `Position::static_eval`,
which asks the embedded Komodo engine over a thread pool that cannot run here --
`material_difference_stm` is used instead. That substitute only feeds the line-cutoff
equities in `get_equities`, so it affects internal-node scores but not the position-only
predicates (SEE, safe squares, sacrifice shape).

### 12.2 Fidelity

On the 127 plies behind every Chess.com or our Brilliant (110 games), the emulated final
label matches Chess.com's on **97** (76%). It reproduces Chess.com's Brilliant on 84 of its
Brilliants and correctly declines 25 of our extras. The 30 misses are where the
`static_eval` substitute or the attached (rather than searched) engine lines change an
internal score or a precision grade; those are exactly the engine-bound cases §5 predicted.

So the emulator is an exact oracle for the **position-only** predicates and an approximate
one for anything that reads an internal node's score.

### 12.3 Where each disagreement comes from

Tracing every call of Chess.com's predicates on the 46 cases (`~/work/cee-emu/probes/`):

**Extras we should drop (Chess.com's own position-only predicates reject them).**
- *Created threat outweighs the piece left* (`is_sacrifice_of_not_moved` net-value gate
  `v_sq <= cap + v1`): Rc1, Bc2, a4, Rc8, Bf4, Bg4, Nd4 (x2), Bf5, Bd6, Be6, Ra7. The move
  leaves a piece en prise but creates a strong threat worth more (e.g. Rc1 leaves the bishop,
  value 300, but threatens the queen on c3, value 900 -> `v1 = 900`, so `300 <= 900` and it is
  no sacrifice). Our `sacrifice_of_not_moved` computes a smaller `v1` than Chess.com's
  `created_strong_see_threats_against` and so lets these through.
- *The moved piece is actually safe by Chess.com's SEE* (`is_safe` true): Qb8, Qd8+, Qa6, Qxf3.
  Chess.com's `see_gain` differs from ours in two decompile-confirmed ways -- it counts a pawn
  **promoting on the recapture** (Qb8/Qd8: `see_gain = 0` because a `c7` pawn recaptures and
  queens), and it **frees a piece pinned to its king once the pinner is the capturer** (Qxf3:
  `see_gain = 300`). Our SEE ignores promotions mid-exchange and never lets a pinned piece
  capture off its pin line.

**Extras that are engine/grade-bound (not fixable without Chess.com's engine).** Nxc7+, Rxh2
(Chess.com grades the move Inaccuracy, precision 7, so `is_candidate` fails); Qxf3, Qxe7, Qxg7
(check evasions whose status depends on the searched line); Bxb6, Nxe5, Bxc4, Qxd4 (the
emulator itself calls them Brilliant -- the difference is Chess.com's grade/score, not a rule).

**Missed Brilliants, position-only (recoverable).**
- Low-rated direct sacrifices Chess.com accepts on its generous `!is_high_rated` branch, which
  skips the deflection and net-material tests: Bxc5, Nd6+, Bxe4, Nxf6+ (all under ~1000 Elo).
  The emulator confirms `is_sacrifice = 1` for these; our detector rejects them, so our
  low-rated branch is stricter than Chess.com's.

**Missed Brilliants, engine/score-bound (not fixable).** Rac1, Bxf3, gxf3, Qxe3, Rxc6, Rxd5,
Qxd4(62), Rxg6+, Rd1+, O-O-O, Bxh2+ -- these need an internal node's score (the material gate
reads `parent.score() < EP_to_cp(0.10, 2000)`, and the emulator's substituted scores cannot
settle the gate), the discovered-attack/deflection branch on a searched line, or the mate-tag
path, all of which depend on Chess.com's engine output rather than the position.

### 12.4 Result

The first position-only fix from §12.3 is implemented: in `is_sacrifice_of_not_moved`, the
threats the move created now exclude only the SEE-threateners of the sacrificed square
(`see_threateners`, = Chess.com's `see_threats_to`) instead of every geometric attacker, behind
`ref_created_see_threats` (on by default). A piece that attacks the square but cannot capture it
without losing material (e.g. the c3 queen "attacking" the c4 bishop after Rc1) now counts as a
created threat worth more than the piece left behind, so the move is correctly not a sacrifice.

Measured alone against `7353401`, on all 575 calibration games:

| Set | Before P / R | After P / R |
|---|---|---|
| tuning (all) | 0.74 / 0.86 | **0.81 / 0.86** |
| holdout (all) | 0.73 / 0.73 | **0.83 / 0.73** |
| best-move set (tuning) | 0.73 / 0.94 | 0.73 / 0.94 |
| best-move set (holdout) | 0.70 / 0.91 | 0.70 / 0.91 |

Tuning precision rose 0.74 -> 0.81 (seven fewer extras) and holdout 0.73 -> 0.83 (three fewer),
with recall, true positives and the independent best-move set all unchanged -- the rule removes
false sacrifices without dropping a real one and does not overfit. It is a rule read from
`is_sacrifice_of_not_moved`, not a threshold fitted to labels.

The whole-move emulation settles the §11 question: of the 46 remaining differences, **about a
dozen extras and four misses are position-only** and Chess.com's own code shows exactly which
predicate differs; **the rest are bound to Chess.com's engine scores or grades** and match the
§5 noise floor -- they cannot be closed while the engines differ. Two further position-only
fixes remain identified for later rounds, each to go behind its own `BrilliantConfig` flag and
be kept only if tuning, holdout and the best-move set all hold or improve: Chess.com's SEE rules
(promotion on the recapture; a piece pinned to its king freed once its pinner captures), which
remove the four remaining `is_safe` extras, and the more generous low-rated `is_sacrifice`
branch, which recovers the four low-rated direct-sacrifice misses.

