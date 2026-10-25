# Detector check: our tactic tags against the lichess puzzle themes

Our coach detectors (`backend/crates/review-server/src/coach/detect/`) were tuned only against
Chess.com's coach on 142 games from one account ([`coach-log.md`](coach-log.md)). This is the
independent check of [`coach-analysis.md`](../coach-analysis.md) §8 item 1, step 2 of
[`coach-gap-analysis.md`](../coach-gap-analysis.md) §7.2: run them on lichess
puzzles, whose themes are labelled independently of us, and report precision and recall per theme.
The target was precision ≥ 0.9 on fork, pin, skewer, hanging piece and discovered attack.

**Summary.**

- Seven detector bugs were fixed (§4).
- Fork now meets the target: what the coach says is a lichess fork 95% of the time (was 65%).
- Skewer, pin and discovered attack rose to 0.71–0.88 against the lichess labels; hanging piece is
  unchanged at 0.86 (0.78 on the random set). They stay below 0.9 against those labels, but the
  labels are narrower than the tags. By hand,
  10/10 printed skewer, 10/10 hanging-piece, 9/10 pin and 7/10 discovered-attack "false positives"
  are the motif, and are what wins the material (§6).
- Chess.com agreement did not drop; it rose. Bad moves 39.2% → 40.5% exact, good moves 58.3% →
  58.8%, Blunders 138 → 140 of 228, best-move sentence unchanged at 46.0%, labels unchanged at
  68.7% (§5).

## 1. Data and sample

- **Database:** `lichess_db_puzzle.csv.zst` from <https://database.lichess.org/#puzzles> (CC0),
  downloaded 2026-10-21 (307,234,795 bytes). It stays outside the repository, in WSL
  (`~/work/lichess-puzzles`).
- **Filter:** NbPlays ≥ 100 and Popularity ≥ 50, to drop puzzles whose themes few players have
  voted on. 4,808,704 puzzles pass.
- **Strata:** 300 puzzles at random from each of 14 themes, plus 10,000 at random from the whole
  database:
  - fork, pin, skewer, hangingPiece, discoveredAttack, doubleCheck, trappedPiece;
  - backRankMate, mateIn1, mateIn2, attraction, deflection, capturingDefender, promotion.

  Reservoir sampling, seed 20261021. The strata overlap a little: 14,190 distinct puzzles, of which
  14,131 were checked.
  59 were skipped: their solution is longer than the 12 plies the coach reads from a line.
- **Committed:** only the ids, [`tools/calibrate/puzzle_ids.tsv`](../../tools/calibrate/puzzle_ids.tsv)
  (id and strata). `puzzle_check.py sample --from-ids` rebuilds the identical sample from the
  database (checked byte for byte). The FENs and moves quoted in §7 are lichess data (CC0).

Precision is given twice:

- on the whole sample, which is rich in the 14 themes;
- on the 10,000 random puzzles alone ("random"), the unbiased estimate.

## 2. What is measured

A lichess puzzle is the opponent's move (the first of `Moves`) and then the solution: the solver's
moves and the forced replies. The example `puzzle_tags` (review-server) plays the opponent's move
and reads the solution as a line, the way `coach/circ.rs` reads an engine line. A line that ends in
mate gets `mate_in` from its length, as an engine mate score would give it.

Three readings:

| reading | what it is | coach code |
|---|---|---|
| **said** (MISSES) | The one event the coach says for the line as a best move: a mate, else the highest-priority tactic behind the material the line wins, at any solver move up to the gain (WINS_MATERIAL on the first move, LEADS_TO later), else a tactic of the first move. | `circ::line_event` with `Circ::Misses` |
| **permits** (PERMITS) | The same line as the reply that the opponent's move allowed: a tactic is named on the first move only (or the second after a quiet check), plus the free-piece rules of `circ::permits`. | `circ::permits` |
| **fired** | Every tactic any detector finds on any solver move. | `detect::tactics` |

"Said" is what a user reads, so it carries the targets. "Fired" shows the detectors on their own.

### Mapping of lichess themes to our tags

| lichess theme | our tags | note |
|---|---|---|
| fork | `fork`, `royal_fork` | |
| pin | `pin`, `exploits_pin` | lichess tags a pin only when it stops an attack or an escape |
| skewer | `skewer` | lichess tags a skewer only once the piece behind is taken |
| hangingPiece | `free_piece`; `free_piece:hanging` | `free_piece:hanging` is the like-for-like subset: a non-pawn taken undefended |
| discoveredAttack | `discovered_attack`, `discovered_check` | |
| doubleCheck | `double_check` | |
| trappedPiece | `trapped_piece` | |
| backRankMate | `back_rank_mate` | |
| mateIn1 | `checkmate` (said); `checkmate`, `back_rank_mate` (fired) | |
| mateIn2–5 | `forced_mate` (said) | fired: the mating move of any mate is `checkmate` (theme `mate`) |
| attraction | `attraction` | |
| deflection | `overloaded` | closest only: our overloaded defender takes back and drops the other piece |
| capturingDefender | `removes_defender` | |
| promotion | `promotion` | |

Our `free_piece` is wider than lichess's hangingPiece:

- it counts pawns;
- it counts pieces that are defended too little to be won back;
- it never counts taking back on the square where the opponent just captured.

Lichess counts a recapture as hanging when the opponent's capture took less than the piece it puts
there.

## 3. Results (said, MISSES)

Before = main `582bdd9`; after = this branch. "n" is how often the tag is said.

| our tag | lichess theme | n before | precision before | n after | precision after | random n after | random precision before → after |
|---|---|---:|---:|---:|---:|---:|---:|
| **fork** | fork | 1,677 | 0.65 | 1,136 | **0.95** | 834 | 0.66 → **0.95** |
| royal_fork | fork | 412 | 0.87 | 409 | 0.89 | 289 | 0.87 → 0.89 |
| **skewer** | skewer | 556 | 0.60 | 457 | **0.88** | 204 | 0.43 → 0.77 |
| **pin** | pin | 333 | 0.53 | 238 | **0.76** | 164 | 0.48 → 0.71 |
| exploits_pin | pin | 277 | 0.48 | 344 | 0.48 | 243 | 0.41 → 0.41 |
| **discovered_attack** | discoveredAttack | 619 | 0.67 | 564 | **0.76** | 359 | 0.59 → 0.71 |
| discovered_check | discoveredAttack | 103 | 1.00 | 96 | 1.00 | 52 | 1.00 → 1.00 |
| **free_piece:hanging** | hangingPiece | 421 | 0.86 | 421 | **0.86** | 227 | 0.78 → 0.78 |
| free_piece (all) | hangingPiece | 1,116 | 0.33 | 1,116 | 0.33 | 775 | 0.23 → 0.23 |
| trapped_piece | trappedPiece | 394 | 0.90 | 380 | 0.94 | 122 | 0.74 → 0.82 |
| double_check | doubleCheck | 85 | 1.00 | 55 | 1.00 | 9 | 1.00 → 1.00 |
| back_rank_mate | backRankMate | 519 | 0.26 | 208 | 0.64 | 101 | 0.16 → 0.53 |
| checkmate | mateIn1 | 1,431 | 1.00 | 1,742 | 1.00 | 1,375 | 1.00 → 1.00 |
| forced_mate | mateIn2–5 | 2,755 | 1.00 | 2,755 | 1.00 | 1,769 | 1.00 → 1.00 |
| removes_defender | capturingDefender | 801 | 0.19 | 287 | 0.67 | 110 | 0.04 → 0.28 |
| overloaded | deflection | 58 | 0.21 | 69 | 0.32 | 45 | 0.07 → 0.13 |
| attraction | attraction | 122 | 0.99 | 179 | 0.99 | 89 | 0.98 → 0.99 |
| promotion | promotion | 215 | 1.00 | 273 | 1.00 | 113 | 0.99 → 0.99 |

**Recall per theme (said):** the share of the theme's puzzles where the coach says one of its tags.

| lichess theme | puzzles | before | after | why the rest is missed |
|---|---:|---:|---:|---|
| fork | 1,979 | 0.73 | 0.73 | a free piece taken by the forking move is said first (FreePiece outranks Fork) |
| pin | 1,081 | 0.29 | 0.32 | mates and other tactics outrank it |
| skewer | 550 | 0.61 | 0.73 | |
| hangingPiece | 732 | 0.50 | 0.50 | mates said first; taking back is never a free piece for us |
| discoveredAttack | 944 | 0.55 | 0.56 | |
| doubleCheck | 402 | 0.21 | 0.14 | most double-check puzzles are mates, said as mates |
| trappedPiece | 423 | 0.84 | 0.84 | |
| backRankMate | 695 | 0.19 | 0.19 | a longer mate is `forced_mate` whatever its last move (by design) |
| mateIn1 | 1,950 | 0.73 | 0.89 | the rest are `back_rank_mate` |
| mateIn2 | 2,086 | 1.00 | 1.00 | |
| attraction | 921 | 0.13 | 0.19 | the fork or mate it sets up is said |
| deflection | 916 | 0.01 | 0.02 | no tag of ours means deflection |
| capturingDefender | 383 | 0.39 | 0.50 | |
| promotion | 582 | 0.37 | 0.47 | |

**Fired** (every detector on every solver move), precision after (before) on the whole sample:

- fork 0.70 (0.41), skewer 0.46 (0.34), pin 0.68 (0.44), discovered attack 0.63 (0.55);
- free_piece:hanging 0.91 (0.91), back_rank_mate 0.74 (0.38), removes_defender 0.52 (0.10).

Recall when fired: fork 0.98, skewer 0.95, trapped piece 0.92, discovered attack 0.82, hanging
piece 0.77, pin 0.61. The detectors find almost every lichess fork and skewer somewhere in the
line. The lower numbers when said are mostly priority between tags, not detection.

**Permits** (the reply line; tactics named on its first move only), after (before):

- fork 0.95 (0.70), skewer 0.86 (0.60), pin 0.74 (0.64);
- discovered attack 0.77 (0.70), free_piece:hanging 0.78 (0.78).

### Confusion: what the coach says for each sampled theme (after, said)

The share of each 300-puzzle stratum; the five most common events.

| stratum | events |
|---|---|
| fork | fork 59%, royal_fork 15%, free_piece 13%, forced_mate 5%, none 4% |
| pin | pin 21%, none 15%, exploits_pin 14%, forced_mate 11%, material_gain 10% |
| skewer | skewer 76%, none 8%, free_piece 7%, fork 4%, material_gain 2% |
| hangingPiece | free_piece 55%, material_gain 16%, checkmate 10%, back_rank_mate 10%, forced_mate 7% |
| discoveredAttack | discovered_attack 48%, discovered_check 11%, forced_mate 10%, material_gain 8%, free_piece 7% |
| doubleCheck | forced_mate 56%, double_check 13%, checkmate 12%, free_piece 6%, fork 4% |
| trappedPiece | trapped_piece 85%, free_piece 6%, discovered_attack 3%, material_gain 2%, none 2% |
| backRankMate | forced_mate 82%, back_rank_mate 18% |
| mateIn1 | checkmate 94%, back_rank_mate 6% |
| mateIn2 | forced_mate 100% |
| attraction | forced_mate 32%, attraction 20%, fork 15%, royal_fork 12%, none 7% |
| deflection | material_gain 38%, forced_mate 15%, none 12%, free_piece 5%, skewer 5% |
| capturingDefender | removes_defender 52%, exploits_pin 10%, fork 7%, free_piece 6%, material_gain 5% |
| promotion | promotion 54%, none 18%, forced_mate 12%, free_piece 4%, attraction 2% |
| random (9,968) | forced_mate 18%, material_gain 16%, none 15%, checkmate 14%, fork 8% |

## 4. What was wrong, and the fixes

Each fix follows chess semantics. Each has a unit test in `tests/coach_detect.rs`.

1. **Back-rank mate** (`detect/mate.rs`): the mate counted when every square in front of the king
   was covered by the attacker or held by its own pieces, with at least one own piece. That called
   a queen-and-rook mate with one pawn in front a back-rank mate.
   - Now every square in front must hold one of the king's own pieces.
   - Said precision 0.26 → 0.64.
2. **Fork** (`detect/double.rs`): an undefended pawn counted as a fork target. So a check that also
   hits a loose pawn was called a fork.
   - Now pawns never count.
   - Said precision 0.65 → 0.95.
3. **Discovered attack** (`detect/double.rs`): a target that can simply take the uncovered piece
   (an unguarded attacker, or a cheaper one) was counted. For example, a recapture opens a file and
   the rook at the end of it just takes ours.
   - Now such targets are dropped, using the legal replies, so a check or pin that stops the
     capture still counts.
   - Said precision 0.67 → 0.76, recall unchanged.
4. **Pin** (`detect/lines.rs`): pins of pawns were said as the tactic behind the material. In a
   first, smaller sample (6,169 puzzles), 12 of the 15 pawn pins said carried no lichess pin.
   - Now pawns are skipped. A pinned pawn that cannot take back is still `exploits_pin`.
   - Said precision, with fixes 5 and 7: 0.53 → 0.76.
5. **Skewer** (`detect/lines.rs`): the detector was static, so it fired when the front piece could
   interpose, or when the line did something else.
   - Now, when the line goes on, the front piece must step off the line and the mover must take the
     piece behind on its next move. A line that ends right after the skewer still gets it.
   - Said precision 0.60 → 0.88.
6. **Removes defender, overloaded** (`detect/defender.rs`): both were static ("the guarded piece can
   now be won"). They fired on almost any capture of a defender, 0.04 precision on the random set.
   - Now the line must win the guarded piece with one of the mover's next two moves.
   - For overloaded, the defender must take back first.
   - Removes defender: said precision 0.19 → 0.67.
7. **The capture that settles the gain** (`circ.rs`, `Tag::threatens_material`): a fork, pin, skewer
   or discovered attack made by the capture that completes a line's gain was named as the reason for
   that gain. The fork made by the last capture of a deflection line is one example. That capture
   is now explained by what it takes, so the earlier move's tactic, or MaterialGain, is said.
   Applied only when the gain is not on the first move.

**Not changed (definitions differ, not bugs):**

- `free_piece` keeps pawns and defended-too-little pieces, and never counts a recapture.
- A longer mate stays `forced_mate`.
- We have no deflection tag.
- FreePiece still outranks Fork when one capture does both. This is the main fork recall gap; see
  §8.

## 5. Chess.com agreement (run `coach-detector-check`)

Measured on the 142 calibration games at commit `0a8971a`, the same way as `coach-main-582bdd9`
(Stockfish 18, depth 18, MultiPV 3). Both runs read the same engine results from a local disk cache
of the server's engine pool (a patch that is not committed). The coach is pure, so only engine
results are cached and the tags are what a fresh search gives.

| | main `582bdd9` (and `25a2a6a`, same figures) | this branch | change |
|---|---:|---:|---:|
| bad moves exact (1,641 plies both apps label bad) | 643 (39.2%) | 665 (40.5%) | +22 |
| good moves exact (5,349) | 3,116 (58.3%) | 3,144 (58.8%) | +28 |
| Blunders exact (228) | 138 | 140 | +2 |
| opening-phase bad, report style (602) | 34.4% | 35.5% | |
| best-move sentence (exact) | 46.0% | 46.0% | |
| label agreement | 68.7% | 68.7% | |

Per ply, 100 plies became exact and 48 stopped being exact.

- **Gains:**
  - a pinned pawn no longer said as a pin: Chess.com says the development, defence or recapture;
  - removes-defender lines now said as the trade;
  - back-rank mates now plain checkmates.
- **Losses:** 7 PERMITS forks of a king and a loose pawn (now material gain), and a few forks now
  said as the positional idea. Chess.com calls some king-and-pawn checks forks; lichess and the
  textbook do not.

## 6. Checked by hand

Precision against lichess undercounts, because lichess labels only some of the motifs that are
there:

- skewer only once the piece behind is taken;
- pin only when it stops an attack or an escape;
- back-rank mate not when the mating piece also covers a square in front;
- hanging piece with its own exclusions, and with themes crowd-voted.

To estimate real precision, the ten printed "false positives" of each target tag were checked by
hand. They are a random draw from each list; all are listed in §7.

| tag | real motif, and what wins | real but incidental | wrong |
|---|---:|---:|---:|
| fork | 10 | 0 | 0 |
| hanging piece (`free_piece:hanging`) | 10 | 0 | 0 |
| skewer | 10 | 0 | 0 |
| pin | 9 | 0 | 1 (doubtful: the pinned rook may take the pinner along the line) |
| discovered attack | 7 | 3 | 0 |
| back-rank mate | 10 | 0 | 0 |

Counting only the first column as right, real precision is estimated as the lichess precision plus
the share of its false positives that were real:

- fork 0.95 + 0.05 × 10/10 ≈ 1.0;
- skewer 0.88 + 0.12 × 10/10 ≈ 1.0;
- hanging piece 0.86 + 0.14 × 10/10 ≈ 1.0;
- pin 0.76 + 0.24 × 9/10 ≈ 0.98;
- discovered attack 0.76 + 0.24 × 7/10 ≈ 0.93.

Only discovered attack still names an uncovered attack that is not what wins, 3 of 10 times. With
10 cases per tag these are estimates, not measurements.

## 7. Examples

Each table is a random draw of ten from the list in its heading. The FEN is lichess's: the
position before the opponent's move. The moves are UCI: the opponent's move first, then the
solution. Themes are lichess's, without the length, phase and evaluation themes. "We say" is the
coach's event: tag, circumstance chain and the solver move (ply) it is on.

### 7.1 Said, lichess theme absent

**`fork`: said, lichess theme absent (52 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [2vcCQ](https://lichess.org/training/2vcCQ) | `r7/p5rk/2n4p/8/2p1NP2/2Pn4/P6P/R5RK b - - 2 36` | a8e8 e4f6 h7h8 g1g7 h8g7 f6e8 | - | fork misses/wins_material @0 | fork: Nf6+ hits Kh7 and Re8 |
| [zGpZo](https://lichess.org/training/zGpZo) | `6k1/pp3ppp/8/8/1BP3n1/4P1P1/Pr3PKP/R7 w - - 1 25` | a1d1 g4e3 g2f3 e3d1 | pin | fork misses/wins_material @0 | fork: Ne3+ hits Kg2 and Rd1 |
| [HIkQZ](https://lichess.org/training/HIkQZ) | `8/1p4kp/pqbp1r2/6p1/2P1P3/1PN4Q/P1B1N2K/2R5 w - - 0 28` | c3d5 b6f2 h2h1 f6h6 h3h6 g7h6 | - | fork misses/wins_material @0 | fork: Qf2+ hits Kh2 and the loose Ne2 |
| [j4iYD](https://lichess.org/training/j4iYD) | `2r4k/1b2b1pp/ppq1Np2/4p3/7N/7Q/PPP2PPP/5RK1 b - - 6 24` | f6f5 h4g6 h8g8 g6e7 | kingsideAttack pin | fork misses/wins_material @0 | fork: Ng6+ hits Kh8 and Be7 |
| [jo9CC](https://lichess.org/training/jo9CC) | `5r1k/7p/p2p2pQ/1pp1r3/2n1P2N/P1q5/5PPP/R3RK2 b - - 3 24` | f8e8 h4g6 h8g8 g6e5 | kingsideAttack pin | fork misses/wins_material @0 | fork: Ng6+ hits Kh8 and Re5 |
| [IfpPP](https://lichess.org/training/IfpPP) | `r2q4/1b3k2/p3npr1/1p1p1Q2/3P4/1P3N2/P4PP1/4R1K1 b - - 0 33` | e6d4 f3e5 f7e7 e5g6 e7d6 f5f4 | discoveredCheck doubleCheck pin | fork misses/wins_material @0 | fork: Ne5+ hits Kf7 and Rg6 |
| [ZzQKl](https://lichess.org/training/ZzQKl) | `r2q1rk1/p4ppp/8/3pP3/2pP2n1/P1B1PRb1/2QN2P1/RN5K w - - 3 21` | f3g3 d8h4 h1g1 h4h2 g1f1 h2g3 | - | fork misses/wins_material @0 | fork: Qh4+ hits Kh1 and Rg3 |
| [h8eXP](https://lichess.org/training/h8eXP) | `4N3/4R1pk/1p4r1/1Pp1P2p/5n1P/8/8/7K b - - 0 39` | g6g4 e8f6 h7g6 f6g4 | pin | fork misses/wins_material @0 | fork: Nf6+ hits Kh7 and Rg4 |
| [R2A5m](https://lichess.org/training/R2A5m) | `3q1rk1/p6p/4n3/2P3pb/8/P1Q1P3/1B3P2/R5K1 b - - 2 33` | d8e7 c3h8 g8f7 h8h7 f7e8 h7h5 | - | fork misses/leads_to @2 | fork: Qxh7+ hits the king and Bh5 |
| [krJGy](https://lichess.org/training/krJGy) | `3R4/pp3p1k/4p1pp/4b2q/4P3/6Q1/PP3P1N/6K1 w - - 0 27` | g3g2 e5h2 g2h2 h5g5 h2g3 g5d8 | - | fork misses/leads_to @2 | fork: Qg5+ hits Kg1 and Rd8 |

**`free_piece:hanging`: said, lichess theme absent (58 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [Kqqjh](https://lichess.org/training/Kqqjh) | `r4rk1/ppq2p2/5n1p/2ppb1P1/3Pp3/2P1B1P1/PP5P/R2QR1K1 b - - 0 17` | e5g3 g5f6 g3h2 g1h1 | - | free_piece misses/wins_material @0 | hanging: gxf6 takes a knight whose guard left |
| [DZ1Hs](https://lichess.org/training/DZ1Hs) | `1r4k1/5pp1/4p2p/1q1P4/p1p5/r6P/1PQ1RPPK/1R6 b - - 0 27` | e6d5 b2a3 b5b1 e2e8 b8e8 c2b1 | deflection | free_piece misses/wins_material @0 | hanging: bxa3 takes an unguarded rook |
| [ecIYe](https://lichess.org/training/ecIYe) | `1r1q1r2/6kp/p2b1ppN/1p2p1BB/2p1b3/2P1Q2P/PP3PP1/R4RK1 b - - 0 23` | g6h5 e3e4 f6g5 h6f5 f8f5 e4f5 | - | free_piece misses @0 | hanging: Qxe4 takes an unguarded bishop |
| [ugJo7](https://lichess.org/training/ugJo7) | `1r2k2r/pppqb1p1/3p3p/4p2n/P3P1bP/3PQBP1/1PnN3N/1RB2RK1 w k - 8 19` | f3g4 c2e3 g4d7 e8d7 | - | free_piece misses @0 | hanging: Nxe3 takes an unguarded queen |
| [pF5LD](https://lichess.org/training/pF5LD) | `1q2r1k1/2p2ppp/r1pp4/p1n5/4P3/P1N2P1P/1PP3P1/2KR1Q1R w - - 4 17` | c3a4 c5a4 f1a6 b8b2 | queensideAttack | free_piece misses @0 | hanging: Nxa4 takes an unguarded knight |
| [RheTp](https://lichess.org/training/RheTp) | `rnb1k2r/pp1pppbp/5np1/q2N2B1/1PPQ4/8/P3PPPP/R3KBNR b KQkq - 0 7` | f6d5 d4g7 a5b4 g5d2 | - | free_piece misses @0 | hanging: Qxg7 takes an unguarded bishop |
| [Gi3EN](https://lichess.org/training/Gi3EN) | `r1b1k2r/ppp2ppp/1q6/3pP1N1/3n1Bn1/2PB2P1/PP4K1/R2Q3R b kq - 0 16` | d4f5 d1g4 b6b2 g4e2 b2e2 d3e2 | - | free_piece misses/wins_material @0 | hanging: Qxg4, the c8 bishop's guard is blocked by Nf5 |
| [1Xlf6](https://lichess.org/training/1Xlf6) | `r4rk1/5pbp/QBqn2p1/4p3/2p1P3/2P4P/1PB2PP1/R3R1K1 w - - 3 23` | c2a4 a8a6 a4c6 a6b6 | - | free_piece misses/wins_material @0 | hanging: Rxa6 takes an unguarded queen |
| [PNYId](https://lichess.org/training/PNYId) | `4b1k1/1p3p2/4p1p1/3pP1Q1/1P6/2q1R3/rp3PP1/1R4K1 b - - 1 32` | a2a1 e3c3 a1b1 g1h2 b1h1 h2h1 | - | free_piece misses/wins_material @0 | hanging: Rxc3 takes an unguarded queen |
| [XXLZ5](https://lichess.org/training/XXLZ5) | `8/6P1/p3Nb2/8/P7/4pk2/8/5K2 w - - 0 62` | e6g5 f6g5 g7g8q e3e2 f1e1 g5h4 e1d2 e2e1q | advancedPawn exposedKing promotion | free_piece misses @0 | hanging: Bxg5 takes an unguarded knight |

**`skewer`: said, lichess theme absent (56 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [vMayN](https://lichess.org/training/vMayN) | `r4rk1/pp2bpp1/2p1p2p/4q3/Q3b2P/4B1R1/PP2PPP1/3RKB2 b - - 3 15` | e7f6 e3d4 e5f5 d4f6 f5f6 a4e4 | discoveredAttack pin | skewer misses/wins_material @0 | skewer: Bd4 hits Qe5, Bf6 behind; Qf5 Bxf6 |
| [19TxX](https://lichess.org/training/19TxX) | `6nr/1p1k3p/1ppPb1p1/1N3p2/5P2/3B4/rPP3PP/2KRR3 w - - 0 17` | e1e6 a2a1 c1d2 a1d1 d2d1 d7e6 | queensideAttack | skewer misses/wins_material @0 | skewer: Ra1+ Kd2 Rxd1 |
| [ZIaei](https://lichess.org/training/ZIaei) | `7r/p5k1/1p1Q4/4pqBp/7P/2P3K1/PP4P1/8 b - - 0 35` | h8f8 g5h6 g7h7 d6f8 f5g4 g3f2 | deflection | skewer misses/wins_material @0 | skewer: Bh6+ Kh7 Qxf8 |
| [0oifS](https://lichess.org/training/0oifS) | `7R/p7/1p6/4p1p1/1P4k1/4r3/P2K4/8 b - - 1 36` | g4f3 h8h3 f3f4 h3e3 | rookEndgame | skewer misses/wins_material @0 | skewer: Rh3+ Kf4 Rxe3 |
| [q5WmE](https://lichess.org/training/q5WmE) | `5k2/7P/2R5/1p1p3r/1P6/8/2K5/8 b - - 0 54` | h5h7 c6c8 f8g7 c8c7 g7g6 c7h7 | exposedKing rookEndgame | skewer misses/leads_to @2 | skewer: Rc7+ Kg6 Rxh7 |
| [tOdSW](https://lichess.org/training/tOdSW) | `8/7p/5R2/3k2K1/2r3P1/8/8/8 b - - 2 55` | c4c5 f6f5 d5d4 f5c5 d4c5 g5h6 | rookEndgame | skewer misses @0 | skewer: Rf5+ Kd4 Rxc5 |
| [Ep5K8](https://lichess.org/training/Ep5K8) | `r1b2rk1/1p2qp1p/p1n2np1/3p4/5P2/2PQB3/PPN1B1PP/R4RK1 w - - 0 19` | a1d1 c8f5 d3d2 f5c2 | - | skewer misses/wins_material @0 | skewer: Bf5 hits Qd3, Nc2 behind; Qd2 Bxc2 |
| [EE0ws](https://lichess.org/training/EE0ws) | `6k1/8/8/3R1p2/3P3p/4PK2/8/7r w - - 1 45` | d5f5 h1f1 f3g4 f1f5 | rookEndgame | skewer misses/wins_material @0 | skewer: Rf1+ Kg4 Rxf5 |
| [qsVgv](https://lichess.org/training/qsVgv) | `8/8/7p/6p1/8/7P/3k1QPK/2q5 b - - 23 71` | d2c3 f2c5 c3b2 c5c1 b2c1 h2g3 c1d2 g3g4 | queenEndgame | skewer misses @0 | skewer: Qc5+ Kb2 Qxc1 |
| [7Bc7Z](https://lichess.org/training/7Bc7Z) | `5r2/8/2pR1q2/p5kb/1p4p1/1P3pQ1/P1P5/1K3R2 b - - 5 45` | f6f5 f1h1 f8f6 g3h4 g5g6 d6f6 f5f6 h4h5 | fork | skewer misses/leads_to @2 | skewer: Qh4+ Kg6, Rxf6 |

**`pin`: said, lichess theme absent (56 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [wVYs5](https://lichess.org/training/wVYs5) | `r1bq1b1r/1ppnk1p1/p3pn1p/8/8/2NBBQ2/PPP2PPP/R3R1K1 b - - 1 11` | g7g5 e3d4 e7f7 e1e6 c7c5 d3c4 | discoveredAttack | pin misses/wins_material @0 | pin: Bd4 pins Nf6 to Rh8 |
| [3iPWY](https://lichess.org/training/3iPWY) | `2r2rk1/4qpn1/p2p1R1p/1p1P3P/4n1Q1/3B2P1/PPP5/5R1K w - - 0 31` | d3e4 c8c4 f6f4 f7f5 e4f5 f8f5 | fork | pin misses @0 | pin: Rc4 pins Be4 to Qg4 |
| [IGpBV](https://lichess.org/training/IGpBV) | `r4rk1/pp3ppp/1q2p3/3pP3/P2n4/1P1P1N2/5PPP/2RQ1RK1 b - - 1 17` | d4b3 c1b1 b3d4 b1b6 | - | pin misses/wins_material @0 | pin: Rb1 pins Nb3 to Qb6, then Rxb6 |
| [ytKlQ](https://lichess.org/training/ytKlQ) | `8/7k/6p1/3p3p/5Q1P/1K5q/PP6/8 w - - 1 55` | b3b4 h3g4 f4g4 h5g4 | queenEndgame | pin misses @0 | pin: Qg4 pins Qf4 to Kb4 (forces the trade) |
| [SkJtN](https://lichess.org/training/SkJtN) | `r1b1kbnr/pp3ppp/1qn1p3/3pP3/3P4/P7/1P2BPPP/RNBQK1NR b KQkq - 0 7` | c6d4 c1e3 b6a5 b2b4 f8b4 a3b4 d4c2 d1c2 | defensiveMove | pin misses/wins_material @0 | pin: Be3 pins Nd4 to Qb6 |
| [C2xYL](https://lichess.org/training/C2xYL) | `8/4k3/8/p4R2/P2b4/4p3/3r1PPP/5RK1 w - - 1 32` | f5a5 e3e2 g2g3 d2d1 f1d1 e2d1q | advancedPawn promotion | pin misses/leads_to @2 | doubtful: Rd1 pins Rf1, which may take along the line |
| [3qqOJ](https://lichess.org/training/3qqOJ) | `6r1/1Q2R1pk/4p2p/3p4/6R1/5rPK/8/q5B1 w - - 0 47` | g4g7 g8g7 e7g7 a1g7 | - | pin misses/wins_material @0 | pin: Rxg7 pins Re7 to Qb7 |
| [oI3iG](https://lichess.org/training/oI3iG) | `2r1r1k1/1p4pp/p2Bp1p1/4P3/P2nq2P/4Q3/5PP1/1R3RK1 b - - 7 27` | e4h4 b1b4 d4c2 b4h4 c2e3 f2e3 | - | pin misses/wins_material @0 | pin: Rb4 pins Nd4 to Qh4 |
| [C7Ei0](https://lichess.org/training/C7Ei0) | `3r1qk1/5p1p/p3pQn1/1pR5/1P6/P5p1/1B3PK1/8 b - - 1 32` | g3f2 c5g5 f2f1q g2f1 d8d1 f1e2 d1d2 e2d2 | - | pin misses/wins_material @0 | pin: Rg5 pins Ng6 to Kg8 |
| [TtTAR](https://lichess.org/training/TtTAR) | `1r3rk1/4Rppp/p7/P1p5/3p1Q2/5RK1/1q4PP/8 b - - 5 32` | f7f6 f4g4 f8f7 g4e6 b8f8 e7f7 b2b8 f7c7 | discoveredAttack discoveredCheck | pin misses/leads_to @2 | pin: Qe6 pins Rf7 to Kg8 |

**`discovered_attack`: said, lichess theme absent (134 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [kofx3](https://lichess.org/training/kofx3) | `r1bq1rk1/pppp1ppp/8/4P1N1/2Bn4/B1b5/P4PPP/R2Q1RK1 b - - 1 12` | c3a1 d1h5 d8g5 h5g5 | - | discovered_attack misses/wins_material @0 | incidental: Qh5 uncovers Rf1 on Ba1, but the mate threat wins |
| [uw8RH](https://lichess.org/training/uw8RH) | `rn1qk2r/4b2p/p3Rpb1/3B4/Np6/5P2/PPP3PP/R2Q2K1 b kq - 0 16` | g6f7 e6e7 d8e7 d5a8 | - | discovered_attack misses/wins_material @0 | incidental: Rxe7+ uncovers Bd5 on Bf7; Bxa8 takes a rook loose before |
| [e61Tk](https://lichess.org/training/e61Tk) | `r2qr1k1/pp3ppp/2pb1n2/3P4/8/2PQ1N1P/PP3PP1/R1B2RK1 w - - 1 15` | d5c6 d6h2 f3h2 d8d3 | - | discovered_attack misses/wins_material @0 | discovered: Bxh2+ uncovers Qd8 on Qd3 |
| [l21mG](https://lichess.org/training/l21mG) | `3r1k2/r5p1/2p5/1pq3PQ/3b1p1P/pP6/P1B2P1R/1K1R4 w - - 1 41` | h5h8 f8e7 h8d8 e7d8 | - | discovered_attack misses/wins_material @0 | discovered: Ke7 uncovers Rd8 on Qh8 |
| [dC5SE](https://lichess.org/training/dC5SE) | `2krr3/ppp2pp1/3p1q1p/4n3/4B1bP/2P2N2/PPPQ1PP1/1K1RR3 w - - 8 17` | f3e5 d6e5 d2d8 e8d8 | - | discovered_attack misses/wins_material @0 | discovered: dxe5 uncovers Rd8 on Qd2 |
| [0U3zE](https://lichess.org/training/0U3zE) | `r2qr3/5kbp/p4ppn/3b4/PpBB4/3Q1N2/1PP3PP/R4K1R b - - 5 18` | h6f5 d4b6 d5c4 d3c4 e8e6 c4e6 | - | discovered_attack misses/wins_material @0 | discovered: Bb6 uncovers Qd3 on Bd5 |
| [cFTwX](https://lichess.org/training/cFTwX) | `r4rBk/ppp1q3/2n3Qp/4N3/5p2/2N3n1/PPP2KP1/R1B5 w - - 7 21` | e5f7 f8f7 g6h6 h8g8 | - | discovered_attack misses/wins_material @0 | incidental: Rxf7 uncovers Ra8 on Bg8, which the king takes |
| [pMPsj](https://lichess.org/training/pMPsj) | `r1bq1rk1/1p1p1ppB/2n5/p1b1P2n/5B2/P1N2N2/1PP3PP/R2QK2R b KQ - 0 12` | g8h7 f3g5 d8g5 f4g5 | - | discovered_attack misses/wins_material @0 | discovered: Ng5+ uncovers Qd1 on Nh5 |
| [50jNN](https://lichess.org/training/50jNN) | `4r1k1/2r2p2/p2pP1p1/1p1P1PPp/2p4N/P5KP/1P6/4R3 b - - 0 36` | c7c5 e6f7 g8f7 f5g6 f7f8 g6g7 f8g7 e1e8 | advancedPawn attraction deflection kingsideAttack | discovered_attack misses/wins_material @0 | discovered: exf7+ uncovers Re1 on Re8 |
| [OvmHY](https://lichess.org/training/OvmHY) | `r4rk1/pp3p2/3bpPpp/3p3q/N5RB/1P3Q1P/P4P2/7K b - - 1 27` | g6g5 g4g5 h5g5 h4g5 | kingsideAttack | discovered_attack misses/wins_material @0 | discovered: Rxg5 uncovers Qf3 on Qh5 |

**`back_rank_mate`: said, lichess theme absent (74 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [LrprZ](https://lichess.org/training/LrprZ) | `5r1k/6p1/1p2Q3/p1p2B2/2Pp4/8/3q1PPP/4R1K1 w - - 1 33` | e6g6 d2e1 | hangingPiece mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [zSmYf](https://lichess.org/training/zSmYf) | `r1b2kr1/p3ppbp/2p3p1/8/4N3/1PPqB3/P2Q1PPP/R3K2R b KQ - 0 17` | d3e4 d2d8 | mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [AOXhp](https://lichess.org/training/AOXhp) | `3rr1k1/p1p2pp1/2q4p/4p3/4n3/7R/PPQ2PPP/R1B3K1 w - - 8 22` | c2c6 d8d1 | mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [ZSer3](https://lichess.org/training/ZSer3) | `3r2k1/pb2qppQ/1b2p3/2prN1p1/3P4/P6R/1P3PPP/3R2K1 b - - 3 28` | g8f8 h7h8 | mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [JWoHX](https://lichess.org/training/JWoHX) | `3r1rk1/pp2bp2/2p4p/4B1p1/1q2n3/1P3Q2/P1P2PPP/3RR1K1 w - - 0 20` | d1d8 b4e1 | hangingPiece kingsideAttack mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [tZr2S](https://lichess.org/training/tZr2S) | `3r2k1/1p3ppp/5p2/p1b1n3/2b2N2/2P4P/PP2BPP1/R1B2K2 w - - 5 19` | b2b3 d8d1 | mate mateIn1 pin | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [qDGrR](https://lichess.org/training/qDGrR) | `r1b2r1k/p3Npbp/5np1/8/8/4BP2/qPPQ2PP/2KR1B1R w - - 1 14` | e3d4 a2a1 | mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [s11b8](https://lichess.org/training/s11b8) | `3rkb1r/1Qpnpppp/p1Bq4/3N4/8/6PP/PPn2P2/R1B2K1R b k - 5 13` | d8b8 b7b8 | mate mateIn1 pin | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [jyKuR](https://lichess.org/training/jyKuR) | `6kr/ppN3pp/2np1q2/b7/2Q5/2P5/PP3PPP/4R1K1 b - - 0 26` | f6f7 e1e8 | mate mateIn1 pin | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |
| [UgLJZ](https://lichess.org/training/UgLJZ) | `3R3k/5rnp/p3pp1B/1p6/8/P7/1P3PPP/6K1 b - - 3 32` | f7f8 d8f8 | hangingPiece mate mateIn1 | back_rank_mate misses @0 | back-rank mate, boxed in by its own pieces |

**`removes_defender`: said, lichess theme absent (94 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [uh013](https://lichess.org/training/uh013) | `8/3R4/5rkp/5p2/5K2/6PP/8/8 b - - 18 103` | f6f7 d7f7 g6f7 f4f5 | rookEndgame | removes_defender misses/wins_material @0 |  |
| [newXz](https://lichess.org/training/newXz) | `r2b3k/5rpp/p4n2/1p2n3/8/4P3/PPR1NPPP/3RB1K1 b - - 5 22` | f7c7 d1d8 a8d8 c2c7 | - | removes_defender misses/wins_material @0 |  |
| [OJPwj](https://lichess.org/training/OJPwj) | `r1q1r1k1/7p/6p1/b1Pp1p2/pR1P4/P3P1P1/2QB3P/5RK1 w - - 4 31` | b4a4 a5d2 a4a8 d2e3 g1g2 c8a8 | - | removes_defender misses/wins_material @0 |  |
| [uERzZ](https://lichess.org/training/uERzZ) | `3r3k/1b1r2q1/p3Q3/1p1nP1Np/2p4P/P1P5/1P3PP1/3RR1K1 b - - 2 29` | d5f4 d1d7 f4e6 d7g7 e6g7 g5f7 h8g8 f7d8 | exposedKing fork | removes_defender misses @0 |  |
| [t3S4l](https://lichess.org/training/t3S4l) | `r1b1k2r/ppq1bppp/3p1n2/2pp2N1/2P2P2/P1BB4/6PP/R2QR1K1 b kq - 3 15` | e8g8 c3f6 e7f6 d3h7 g8h8 d1h5 | kingsideAttack | removes_defender misses/wins_material @0 |  |
| [Um8bj](https://lichess.org/training/Um8bj) | `8/p3kp2/1pp5/4P1p1/2P2PPp/1P5K/P7/8 b - - 0 49` | f7f6 e5f6 e7f6 f4g5 f6g5 b3b4 | attraction defensiveMove pawnEndgame | removes_defender misses @0 |  |
| [3bFMs](https://lichess.org/training/3bFMs) | `8/1p2k3/p1p2p2/3p1Pp1/PPPP2P1/3K4/8/8 w - - 1 44` | b4b5 d5c4 d3c4 c6b5 a4b5 e7d6 b5b6 d6c6 | attraction pawnEndgame | removes_defender misses @0 |  |
| [KT1QG](https://lichess.org/training/KT1QG) | `7k/ppqn2b1/1n4Pp/8/8/1Pp1QBP1/r4P2/B2R2K1 b - - 1 27` | c7c5 e3c5 d7c5 d1d8 g7f8 a1c3 | deflection exposedKing pin | removes_defender misses/wins_material @0 |  |
| [7qual](https://lichess.org/training/7qual) | `r2q1rk1/3bbppp/p2p1n2/1ppN4/4P3/5Q2/PPP1BPPP/R1B2RK1 b - - 1 14` | d7g4 d5f6 e7f6 f3g4 | kingsideAttack | removes_defender misses/wins_material @0 |  |
| [DI60u](https://lichess.org/training/DI60u) | `rn1q1rk1/pbp1bppp/1p2p3/6B1/3Pn3/2N2N2/PPP2PPP/R2QR1K1 w - - 0 11` | g5e7 e4c3 e7d8 c3d1 | - | removes_defender misses @0 |  |

**`exploits_pin`: said, lichess theme absent (178 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [wpYoz](https://lichess.org/training/wpYoz) | `r4r2/1bq1bppk/p3p2p/1p2P2Q/3N4/2N3R1/PPP3PP/5R1K b - - 5 20` | e7c5 g3g7 h7g7 f1f6 c7e5 h5e5 c5d4 e5d4 | sacrifice | exploits_pin misses/wins_material @0 |  |
| [TSgg3](https://lichess.org/training/TSgg3) | `1br2rk1/1pq2ppp/p4n2/8/P1Bn2b1/2P1B1P1/1PQN1P1P/R3R1K1 w - - 0 17` | c3d4 b7b5 a4b5 a6b5 | - | exploits_pin misses @0 |  |
| [j4fDd](https://lichess.org/training/j4fDd) | `3r3k/pp2Qpq1/2p3p1/5P1p/3r2P1/1B1P3P/PPP5/5RK1 b - - 0 27` | g6f5 f1f5 d4g4 h3g4 | - | exploits_pin misses/wins_material @0 |  |
| [UkcKO](https://lichess.org/training/UkcKO) | `2b1kb1r/5pp1/1q2p2p/3pPP1P/p1pP3B/2P2QPB/P1r4N/4R1K1 b k - 2 32` | b6b2 f5e6 c8e6 h3e6 f7e6 e1f1 c2g2 f3g2 | quietMove | exploits_pin misses/wins_material @0 |  |
| [mBt3S](https://lichess.org/training/mBt3S) | `5rk1/pp4q1/6r1/3pn1Qp/5PpP/P1N5/1P3BP1/2KR4 w - - 0 30` | g5e5 g7e5 f4e5 f8f2 | - | exploits_pin misses @0 |  |
| [kqvz6](https://lichess.org/training/kqvz6) | `7k/pp6/4B3/2b3pP/8/1P2PR1P/7q/4RK2 w - - 2 37` | f3f2 h2h1 f1e2 h1e4 f2f6 e4e3 | - | exploits_pin misses/leads_to @2 |  |
| [CJhbQ](https://lichess.org/training/CJhbQ) | `6r1/4Q1pk/R5b1/3pB2p/3P3P/4P3/5qPK/8 b - - 1 33` | f2e3 a6g6 h7g6 e7e6 g6h7 e6f5 | attraction fork sacrifice | exploits_pin misses @0 |  |
| [44sqv](https://lichess.org/training/44sqv) | `r2n1rk1/4bppp/4p3/1q1pN3/2pP1B2/p1P1P2P/RnQ2PP1/RN4K1 b - - 1 25` | b5b3 c2b3 c4b3 a2b2 | - | exploits_pin misses/wins_material @0 |  |
| [Tw682](https://lichess.org/training/Tw682) | `q1r3k1/4Qpbp/4b1p1/8/p7/1P2BP2/P1P3PP/2KR3R w - - 0 21` | e3b6 a4b3 d1d8 c8d8 e7d8 a8d8 b6d8 b3a2 | advancedPawn | exploits_pin misses/wins_material @0 |  |
| [aINbt](https://lichess.org/training/aINbt) | `4r1k1/4pp1p/1q3npB/2p1R3/8/PbP1Q1PB/5P1P/6K1 b - - 2 29` | f6d5 e5d5 b3d5 e3e5 b6f6 e5d5 | clearance sacrifice | exploits_pin misses/wins_material @0 |  |


### 7.2 Lichess theme present, not said

**pin: theme present, none of our tags said (733 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [xhPff](https://lichess.org/training/xhPff) | `5r1k/2p3p1/1p1pQ3/p2P2q1/5p1p/2B1nP1P/PP3RP1/6K1 b - - 0 28` | g5d5 e6h6 h8g8 h6g7 | kingsideAttack mate mateIn2 pin | forced_mate misses @0 |  |
| [lF4K3](https://lichess.org/training/lF4K3) | `r2q1r1k/4bp2/p4n1Q/1p3p2/2p2B2/N1Pp3N/PP3PPP/R5K1 b - - 4 24` | f6h7 f4e5 f7f6 h3g5 | pin | - |  |
| [h8eXP](https://lichess.org/training/h8eXP) | `4N3/4R1pk/1p4r1/1Pp1P2p/5n1P/8/8/7K b - - 0 39` | g6g4 e8f6 h7g6 f6g4 | pin | fork misses/wins_material @0 | fork: Nf6+ hits Kh7 and Rg4 |
| [l0akp](https://lichess.org/training/l0akp) | `1r3rk1/1p4p1/p1p1p3/3pPqPQ/3n1P2/7R/P5P1/4R1K1 b - - 4 32` | d4c2 g2g4 f5f4 h5h7 g8f7 e1f1 f4f1 g1f1 | fork pin | fork misses/leads_to @2 |  |
| [LT9O1](https://lichess.org/training/LT9O1) | `1R2k1r1/3rppq1/8/p1pPp3/7p/3B2PP/2PB1P2/5RK1 b - - 1 24` | d7d8 d3b5 e8f8 b8d8 | backRankMate deflection mate mateIn2 pin | forced_mate misses @0 |  |
| [66BJf](https://lichess.org/training/66BJf) | `5rk1/5ppp/Q3p3/P2pPnq1/N7/8/5PPP/4R1K1 w - - 3 24` | a4c5 f5h4 a6f1 h4f3 g1h1 f3e1 | pin | fork misses/leads_to @2 |  |
| [3hrZ4](https://lichess.org/training/3hrZ4) | `rnb3k1/p6p/4p1pb/3R2N1/1p3r1P/1B6/PPP2PP1/2K4R b - - 0 19` | f4f5 d5d8 f5f8 d8c8 f8c8 b3e6 g8f8 e6c8 | attraction capturingDefender fork pin | fork misses @0 |  |
| [7uC4Q](https://lichess.org/training/7uC4Q) | `6k1/4bpp1/4p3/2p1P2p/2Pp1P2/2rP2P1/1qNR3P/3Q2K1 w - - 3 38` | c2d4 c3c1 d2b2 c1d1 g1f2 c5d4 | pin | discovered_attack misses/wins_material @0 |  |
| [CJ26U](https://lichess.org/training/CJ26U) | `rn2r1k1/1pp2p1p/p4Qp1/3P4/5P2/5NKP/PPPBq1P1/R7 b - - 1 19` | e2e7 a1e1 e7f6 e1e8 g8g7 d2c3 f6c3 b2c3 | pin sacrifice skewer | skewer misses/wins_material @0 |  |
| [F58Xe](https://lichess.org/training/F58Xe) | `4rrk1/p5p1/1p3b1p/3p4/3N1n2/2P2N1P/PP3RP1/5RK1 w - - 9 27` | f3h2 f6d4 c3d4 f4e2 f2e2 e8e2 | kingsideAttack pin | material_gain misses/leads_to @4 |  |

**discoveredAttack: theme present, none of our tags said (418 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [P24yw](https://lichess.org/training/P24yw) | `r5rk/1p5p/p1pp3b/3n4/PP1PR2Q/5q1P/1B3P1K/2R2B2 b - - 6 30` | h6f4 e4f4 f3f4 h4f4 d5f4 d4d5 | discoveredAttack discoveredCheck sacrifice | - |  |
| [2lWtR](https://lichess.org/training/2lWtR) | `3rr1k1/p4pbp/1p2b1p1/8/3qNP2/Q4P2/PP2R1KP/4R3 b - - 1 24` | e6c4 e4f6 g7f6 e2e8 d8e8 e1e8 g8g7 a3f8 | discoveredAttack kingsideAttack mate mateIn4 | forced_mate misses @0 |  |
| [WlsLs](https://lichess.org/training/WlsLs) | `r2qk2r/1pp3pp/p4p2/3p1b1Q/4p3/4P1P1/PPPN1PP1/R3K2R b KQkq - 1 14` | f5g6 h5g6 h7g6 h1h8 e8d7 h8d8 | discoveredAttack exposedKing skewer | skewer misses/leads_to @2 |  |
| [5VsKv](https://lichess.org/training/5VsKv) | `5r1k/1p4bp/2b3p1/p3p3/P3p1Pq/1Q2B2P/1P3PK1/2RR4 w - - 6 31` | b3e6 f8f2 e3f2 e4e3 e6c6 h4f2 g2h1 b7c6 | discoveredAttack discoveredCheck intermezzo sacrifice | - |  |
| [TtTAR](https://lichess.org/training/TtTAR) | `1r3rk1/4Rppp/p7/P1p5/3p1Q2/5RK1/1q4PP/8 b - - 5 32` | f7f6 f4g4 f8f7 g4e6 b8f8 e7f7 b2b8 f7c7 | discoveredAttack discoveredCheck | pin misses/leads_to @2 | pin: Qe6 pins Rf7 to Kg8 |
| [xMIVd](https://lichess.org/training/xMIVd) | `5q2/1p1n2k1/2pp3p/8/1PPN2b1/4Q3/5rBP/6RK b - - 2 34` | f8f4 d4e6 g4e6 g2f3 | discoveredAttack discoveredCheck fork sacrifice | royal_fork misses @0 |  |
| [BvVTd](https://lichess.org/training/BvVTd) | `3k4/1p2r1b1/p2qB3/7P/6Q1/P1P5/1P4R1/1K6 b - - 0 40` | d6e6 g4e6 e7e6 g2g7 | discoveredAttack | overloaded misses @0 |  |
| [9qbtA](https://lichess.org/training/9qbtA) | `r2q2k1/pb1nbrpp/1p2ppBB/3pP2P/2p3Q1/2P1P3/PP1N1PP1/R3K2R b KQ - 3 15` | h7g6 h5g6 d7e5 g6f7 g8f7 g4g7 | advancedPawn attraction discoveredAttack kingsideAttack pin | removes_defender misses/leads_to @2 |  |
| [QxbNw](https://lichess.org/training/QxbNw) | `r6r/1pk2p2/1np1p3/2QpP1pp/8/1P6/P2q1PPP/R1R3K1 b - - 1 23` | h8e8 c5d6 c7c8 c1c6 b7c6 d6c6 c8b8 c6b6 b8c8 b6c6 | deflection discoveredAttack fork sacrifice | - |  |
| [8zcSA](https://lichess.org/training/8zcSA) | `r2q1rk1/pp2npp1/3bpn1p/4N3/1PPp4/P2Q2N1/3B1PPP/R3R1K1 w - - 0 19` | d3d4 d6e5 d4e5 d8d2 | discoveredAttack skewer | material_gain misses/leads_to @2 |  |

**hangingPiece: theme present, none of our tags said (369 puzzles).**

| puzzle | FEN (before the opponent's move) | moves | lichess themes | we say | checked by hand |
|---|---|---|---|---|---|
| [AXdHv](https://lichess.org/training/AXdHv) | `8/3RQpkp/4p1p1/8/p1p2q2/P7/1P3PPP/2R3K1 w - - 2 29` | d7d8 f4c1 d8d1 c1d1 | backRankMate hangingPiece mate mateIn2 | forced_mate misses @0 |  |
| [QnGz8](https://lichess.org/training/QnGz8) | `r3rbk1/1bp2ppp/p1nq4/1p1n2N1/3P4/NBP5/PP3PPP/R1BQR1K1 w - - 9 17` | d1h5 e8e1 | hangingPiece kingsideAttack mate mateIn1 | back_rank_mate misses @0 |  |
| [MfodQ](https://lichess.org/training/MfodQ) | `3r1k2/p4pp1/1p2p2p/3n4/5q2/5P2/PP2QP1P/K1RR4 w - - 6 32` | d1d3 f4c1 | hangingPiece mate mateIn1 | back_rank_mate misses @0 |  |
| [rLgHv](https://lichess.org/training/rLgHv) | `r2q1rk1/1p1b1pp1/p1n1p1np/3pP1N1/3P4/P2BB3/1P3PPP/R2Q1RK1 w - - 0 14` | g5f7 g8f7 d1f3 f7g8 | defensiveMove hangingPiece | material_gain misses @0 |  |
| [zTTKq](https://lichess.org/training/zTTKq) | `5r1k/2p4p/b2p2pb/2PPp3/4Bn1q/1N3P2/2Q3PP/2B1R1K1 w - - 3 28` | g1h1 h4e1 | hangingPiece kingsideAttack mate mateIn1 | back_rank_mate misses @0 |  |
| [hSBQw](https://lichess.org/training/hSBQw) | `R1r3k1/R1r2ppp/4p3/3p4/3PnP2/6PP/7K/8 b - - 5 37` | c7a7 a8c8 | backRankMate hangingPiece mate mateIn1 | back_rank_mate misses @0 |  |
| [DPxXr](https://lichess.org/training/DPxXr) | `rn2kbnr/ppq2pp1/2p4p/4p3/2B1P1b1/5N2/PPPP2PP/RNBQ1R1K w kq - 0 8` | c4f7 c7f7 f3e5 g4d1 | hangingPiece | material_gain misses/leads_to @2 |  |
| [pWKfz](https://lichess.org/training/pWKfz) | `r1bq2k1/1p1p2bp/p1n1p1p1/5r2/P1B5/2N1B3/1PP2PPP/R2QR1K1 w - - 0 13` | c4e6 d7e6 d1d8 c6d8 | hangingPiece | material_gain misses/leads_to @2 |  |
| [n8tc9](https://lichess.org/training/n8tc9) | `6k1/4rppp/1b6/8/1Pq5/5NP1/4nP1P/R2Q2KR w - - 3 30` | d1e2 c4e2 a1a8 e7e8 | hangingPiece | exploits_pin misses/wins_material @0 |  |
| [97VX7](https://lichess.org/training/97VX7) | `2kr2nr/pp2p1b1/1qp3p1/4Pp1p/2PP4/4BP2/PP1Q1P1P/RN2K2R b KQ - 2 18` | g7e5 d4e5 d8d2 e3b6 | discoveredAttack hangingPiece | discovered_attack misses/wins_material @0 |  |

## 8. Follow-ups

- **FreePiece and Fork on one capture.** When a capture takes a free piece and forks, the free piece
  is said even when the line wins more (e.g. `NRG6v`: Bxc5 takes a loose knight and hits Re7 and the
  king). It is most of the fork recall gap (13% of the fork stratum). Changing it is a priority
  change, so it needs its own Chess.com measurement.
- **Discovered attack that is not the point.** 3 of 10 checked cases name a real uncovered attack
  while the material comes from elsewhere. Requiring the uncovered piece (or the moved one) to take
  the target in the line, as skewer now does, would remove them.
- **Exploits pin** is said at 0.48 against lichess pin and was not checked by hand.
- **Deflection** has no tag of ours. `overloaded` covers only the "defender takes back" form.

## 9. How to repeat

In WSL, with the database outside the repository:

```
python3 tools/calibrate/puzzle_check.py sample --db ~/work/lichess-puzzles/lichess_db_puzzle.csv.zst \
    --out ~/work/lichess-puzzles/sample.jsonl --from-ids tools/calibrate/puzzle_ids.tsv
cargo build --release -p review-server --example puzzle_tags      # in backend/
python3 tools/calibrate/puzzle_check.py run --sample ~/work/lichess-puzzles/sample.jsonl \
    --out ~/work/lichess-puzzles/tags.jsonl
python3 tools/calibrate/puzzle_check.py report --sample ~/work/lichess-puzzles/sample.jsonl \
    --tags ~/work/lichess-puzzles/tags.jsonl --out ~/work/lichess-puzzles/report.md
```

`run` reads the example from `$CARGO_TARGET_DIR` (or `--binary`). It takes under a second for the
14,190 puzzles; `sample` takes about 30 s. Without `--from-ids`, `sample` draws a new sample
(`--per-theme`, `--random`, `--seed`) and `--ids` writes its ids. The report draws its own ten
examples per list, so they differ from the ones checked by hand above.
