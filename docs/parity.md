# Behavioural parity

## What could be compared

The reference application's full review runs on its vendor's servers, and its on-device engine is
an Android arm64 library (`libcee.so`). **Neither can be executed on this machine**, so no
side-by-side output comparison was possible. Parity was established at two levels instead.

### 1. Formula level (exact)

Every recovered constant and rule is pinned by a unit test in `backend/crates/review-core`. The values
were checked by hand against the decompiled code.

| Rule | Recovered source (libcee.so, `nm` address) | Test |
|---|---|---|
| EP curve `1/(1+e^(−k·cp))`, `k = 0.004·(0.0685R−12)/100` | `centipawns_to_expected_points` `0x11389d4` | `expected_points::recovered_curve_values`, `inverse_round_trips` |
| Rating = max(Elo) clamped 1000–2500 | `elo_rating_for_expected_points` `0x1310a34` | `rating_rule_uses_higher_rating_and_clamps` |
| Outcome buckets `[.10,.20,.35,.65,.80,.90]` | `expected_outcome` `0x1139e70` + `.rodata` | `outcome_buckets_follow_recovered_thresholds` |
| Precision thresholds `[.02,.05,.10,.20]` | `MovePrecisionV3Registry::compute` `0x110466c` + `.rodata 0x7596b8` | `precision_thresholds_are_recovered_values` |
| Decision tree order, blunder softening, losing-material hardening, miss guards A/B | `MoveClassificationV3Registry::compute` `0x1104844` | `classification::tests::*` |
| Mate rules | helper `0x1104c28` | `missing_a_mate…`, `slower_mates`, `hastening_defeat…`, `walking_into_mate…` |
| Best-move predicate (bitmask `0x7e8`) | `should_attach_best_alternative_move` | `best_move_predicate_matches_reference` |
| Mate encoding / `to_score` | `to_score` `0x1138938` | `value::tests::*` |
| CAPS2 bands, floor decay, clamps, mate cases, aggregation | `CAPS2ImplRegistry::compute_child` `0x10ea314`, `compute_caps_for_move_nodes` `0x10e96f8` | `caps2::tests::*` |
| Forced counted as Best in tallies | client tally mapper | `summary::tests::forced_counts_as_best` |

### 2. Behaviour level (with Stockfish 19)

The fixture corpus was reviewed end to end (depth 14, MultiPV 3) and each special situation was
checked against what the recovered rules predict.

| Fixture | Observed | Rule exercised |
|---|---|---|
| `opera_game.pgn` | 10.Nxb5 → **Brilliant**; 16…Nxb8 **Forced**; 17.Rd8# **Best**; 6…Nf6 **Mistake** (best 6…Qf6); White accuracy > Black. Since the calibration rebuild, 13.Rxd7 and 16.Qb8+ are **Best**: at this rating the quiet alternatives (13.Rd5 +3.99, 16.Qc3 +3.53 with Stockfish 18 at depth 18) already leave White completely winning, which Chess.com's Brilliant definition excludes. The earlier line-walk detector called all three Brilliant. | Sacrifice detector + gates; forced; precision |
| `scholars_mate.pgn` | 3…Nf6 **Blunder**; 4.Qxf7# **Best**, CAPS2 100 | Mate against the mover; mate delivered = 100 |
| `missed_mate.pgn` | 4.Qf3 **Miss (mate)** with "Qxf7# forces mate in 1 move" | Mate rule: missed mate |
| `back_rank.pgn` (FEN start) | 1.Rd7 **Miss (mate)**; …Kh7 **Forced** | Mate rule; forced |
| `stalemate.pgn` | 10.Qe6 (stalemate instead of mate) **Miss (mate)**; 9…Kg6 into mate when lost → **Mistake** (softened) | "Walking into mate when lost" rule; draw EP = 0.5 |
| `special_moves.pgn` | En passant, promotion and castling reviewed; 4…Ke7 **Blunder** | Move flags; material facts |
| `chess960.pgn` | Reviewed with `UCI_Chess960` | Chess960 support |
| `sparse_metadata.pgn` | Rating 1000 (reference behaviour for missing ratings); Great uses the low-rated branch | Rating rule; `is_high_rated` branch |

## Mismatch found and fixed during parity work

The first Stockfish run graded 12…Rd8 and 13…Rxd7 in the Opera Game as **Mistake** while they lost
≈0 EP. The cause was the "losing side drops ≥ 200 cp → Mistake" rule (recovered) firing on a material
count taken in the middle of an exchange.

Three changes fixed it:
- the material walk now extends past its horizon until the position is quiet;
- material is ignored when the played move's score is already a forced mate.

- "loses more material than best" now needs a 200 cp margin. A rerun showed 12…Rd8 flipping between
  Excellent and Mistake as multi-process search returned slightly different PVs.

All three are implementation-side fixes. The recovered rule itself is unchanged.

## Live comparison with Chess.com Game Review (calibration, 2026-10)

Twenty games were reviewed on Chess.com (engine Stockfish, strength Fast) and compared move by
move with this app; see `docs/calibration/log.md` and `tests/calibration/README.md`. The Confirmed
constants (EP curve, precision thresholds, outcome buckets, CAPS2) were **not** changed. Two
findings bear on recovered rules:

- **Great Find's high-rated gate (resolved 2026-10-23).** `TEP::is_high_rated` (`max(WhiteElo,
  BlackElo) > 999`) was read as a requirement for Great. In game 185209623352 (tuning set) both
  players are rated below 1000 (995 and 980), yet the app gives six Great moves. A new decompile
  showed that the flag *chooses* between two branches, and the low-rated one is more generous, as
  Chess.com's help article says. Great was rebuilt on the recovered structure; see
  `docs/calibration/great-blunder-analysis.md`.
- **Accuracy bias.** Our per-player accuracy is higher than the app's by about +2.8 on average
  (tuning set, higher in 24 of 28 player-games; holdout +1.7, 9 of 12). No detector touches CAPS2, so the
  likely causes are the engine (we use Stockfish 17.1, the app Stockfish 16) and search details,
  not the formula. Not changed; see the open question on engine version.

## Expected (non-algorithmic) differences

These differences come from the environment, not the algorithm:
- **Engine and depth.** The reference uses Stockfish 16.1 NNUE (or a "human" Torch net) at an unknown
  depth per preset. Classifications near a threshold, such as an EP loss of about 0.05 or 0.10, can
  differ between versions and depths. They no longer differ between runs: every search now starts
  from a cleared hash with one thread. On the calibration games most remaining mismatches are one
  step apart on the precision scale (`docs/calibration/log.md`).
- **Book.** A different opening database, so the number of Book moves can differ.
- **Detectors.** Brilliant, Great Find and Miss subtypes use heuristics (see
  `implementation-notes.md`), so their frequency can differ. The surrounding decision tree is exact.

## Not reproduced

- The effective game rating.
- The 250-tag coach explanations.
- The Tricky class.

See `open-questions.md`.

### Rating input to the EP curve

The recovered rule feeds `max(WhiteElo, BlackElo)` (clamped to 1000–2500) into the EP curve. Using
the app's own evals, the app's grades are reproduced best with that rating raised by about 200
(86.5% → 89.0% on tuning, 85.8% → 88.4% on holdout), and the full pipeline agrees 1.3 (tuning) and
1.9 (holdout) points more often with `rating_offset: 200`. This suggests the reference reads a
higher rating than the PGN's game-time ratings, for example the players' current ratings. At the owner's decision `rating_offset` defaults to 200; set
it to 0 for the recovered rule. For the same reason the lower clamp `rating_min` is 1200 (recovered
1000) since 2026-10-23: below 1000, Chess.com's own scores are graded as if rated about 1200
(`docs/calibration/great-blunder-analysis.md` §3.2, §6).

### Search noise is the main remaining gap

Stockfish 16 and 16.1 (the reference's family) did not match better than 17.1 (70.8% and 68.9% vs
71.7% with the +200 rating, tuning set), and their evals are no closer to the app's. At every
depth tried (14–20) and with every version, our evals differ from the app's by a median of 12–16
cp. That difference alone flips about 15% of precision grades; the app's search (probably
multi-threaded and time-limited on its servers) cannot be reproduced exactly.
