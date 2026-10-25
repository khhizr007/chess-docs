# Calibration report: depth-16

- Generated: 2026-10-18T07:37:27+00:00
- Commit: `2703019df381` + uncommitted backend changes (diff sha256 `fa559f3352d9`)
- Engine: Stockfish 17.1; depth 16, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 68.7% (588/856) |
| Within one step | 88.9% (761/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.57 / 0.15 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 0.82 |
| Accuracy mean abs. difference | 2.99 (n=28, max 8.04) |
| Accuracy bias (ours - app) | +2.64 |
| Best move = app's suggestion | 78.8% (108/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | . | . | 1 | . | . | . | 3 |
| **great** | . | **4** | 21 | . | 1 | . | . | . | . | . | 26 |
| **best** | . | 3 | **268** | 39 | 5 | . | . | 1 | . | . | 316 |
| **excellent** | . | . | 38 | **69** | 15 | 1 | 3 | . | 1 | . | 127 |
| **good** | . | . | 9 | 28 | **57** | . | 8 | . | 1 | . | 103 |
| **book** | . | . | 10 | 6 | 2 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 4 | 4 | 25 | 1 | **56** | 1 | 1 | . | 92 |
| **mistake** | . | . | . | . | 2 | . | 12 | **24** | 2 | 4 | 44 |
| **miss** | . | . | . | . | . | . | 6 | 4 | **16** | 1 | 27 |
| **blunder** | . | . | . | . | . | . | . | 3 | 4 | **14** | 21 |
| **total** | 1 | 7 | 351 | 146 | 107 | 81 | 86 | 33 | 25 | 19 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 7 | 4 | 0.571 | 0.154 | 0.242 |
| best | 316 | 351 | 268 | 0.764 | 0.848 | 0.804 |
| excellent | 127 | 146 | 69 | 0.473 | 0.543 | 0.505 |
| good | 103 | 107 | 57 | 0.533 | 0.553 | 0.543 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 86 | 56 | 0.651 | 0.609 | 0.629 |
| mistake | 44 | 33 | 24 | 0.727 | 0.545 | 0.623 |
| miss | 27 | 25 | 16 | 0.640 | 0.593 | 0.615 |
| blunder | 21 | 19 | 14 | 0.737 | 0.667 | 0.700 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 80.6 | +6.9 |
| 1034847688 | black | 65.0 | 73.0 | +8.0 |
| 1041474766 | white | 98.0 | 97.0 | -1.0 |
| 1041474766 | black | 83.8 | 84.9 | +1.1 |
| 184759554082 | white | 81.2 | 85.1 | +3.9 |
| 184759554082 | black | 87.7 | 90.5 | +2.8 |
| 185209623352 | white | 72.7 | 73.7 | +1.0 |
| 185209623352 | black | 72.6 | 74.5 | +1.9 |
| 185324357184 | white | 73.0 | 76.0 | +3.0 |
| 185324357184 | black | 62.4 | 66.4 | +4.0 |
| 185436488062 | white | 98.6 | 97.7 | -0.9 |
| 185436488062 | black | 38.5 | 42.3 | +3.8 |
| 185437323918 | white | 69.5 | 71.5 | +2.0 |
| 185437323918 | black | 75.7 | 74.8 | -0.9 |
| 185438343298 | white | 46.9 | 47.4 | +0.5 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 75.7 | -2.1 |
| 185438707002 | black | 83.0 | 83.7 | +0.7 |
| 185456088510 | white | 78.4 | 82.6 | +4.2 |
| 185456088510 | black | 82.2 | 85.2 | +3.0 |
| 185468039834 | white | 80.0 | 84.0 | +4.0 |
| 185468039834 | black | 87.5 | 89.0 | +1.5 |
| 185468614210 | white | 70.8 | 76.0 | +5.2 |
| 185468614210 | black | 77.1 | 82.8 | +5.7 |
| 185475865432 | white | 78.1 | 82.2 | +4.1 |
| 185475865432 | black | 66.1 | 72.2 | +6.1 |
| 185962590893 | white | 90.8 | 93.4 | +2.6 |
| 185962590893 | black | 90.9 | 93.4 | +2.5 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 61.2% | 83.7% | reviewed | 40.4 |
| 1041474766 | 25 | 25 | 72.0% | 80.0% | reviewed | 18.1 |
| 184759554082 | 62 | 62 | 67.7% | 85.5% | reviewed | 46.0 |
| 185209623352 | 155 | 155 | 64.5% | 89.7% | reviewed | 46.6 |
| 185324357184 | 55 | 55 | 80.0% | 94.5% | reviewed | 29.4 |
| 185436488062 | 13 | 13 | 84.6% | 92.3% | reviewed | 5.6 |
| 185437323918 | 108 | 103 | 62.1% | 87.4% | reviewed | 18.3 |
| 185438343298 | 20 | 20 | 85.0% | 90.0% | reviewed | 5.6 |
| 185438707002 | 95 | 91 | 64.8% | 90.1% | reviewed | 46.5 |
| 185456088510 | 60 | 60 | 65.0% | 86.7% | reviewed | 40.6 |
| 185468039834 | 38 | 38 | 76.3% | 92.1% | reviewed | 31.9 |
| 185468614210 | 54 | 54 | 72.2% | 85.2% | reviewed | 27.7 |
| 185475865432 | 53 | 53 | 71.7% | 92.5% | reviewed | 25.7 |
| 185962590893 | 78 | 78 | 74.4% | 92.3% | reviewed | 24.1 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label equals the collector's guess for 0 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | good | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | miss | mate_override |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (268)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 253 | best -> excellent x39, excellent -> best x38, good -> excellent x28, inaccuracy -> good x25, great -> best x21, excellent -> good x15 |
| `miss_detector` | 8 | blunder -> miss x4, mistake -> miss x2, inaccuracy -> miss x1, excellent -> miss x1 |
| `great_find_event` | 3 | best -> great x3 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `mate_override` | 1 | good -> miss x1 |
| `blunder_softened` | 1 | miss -> mistake x1 |

### `precision` (253)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 9 | 5. c4 | inaccuracy | good | precision | good | 0.0394 | 0.499 | no | Bd3 | Bd3 | -0.52 | -0.43 |
| 1034847688 | 11 | 6. b3 | good | excellent | precision | excellent | 0.0102 | 0.451 | no | Nb1 | - | -0.89 | -0.63 |
| 1034847688 | 12 | 6... c5 | inaccuracy | good | precision | good | 0.0458 | 0.559 | no | e5 | e5 | -0.10 | -0.14 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0122 | 0.487 | no | Be2 | - | -0.10 | -0.17 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0413 | 0.528 | no | a3 | - | +0.12 | -0.14 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0522 | 0.572 | no | cxb5 | - | +0.24 | +0.21 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0683 | 0.620 | no | cxb5 | cxb5 | +0.44 | +0.43 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.474 | yes | h6 | - | +0.90 | +0.47 |
| 1034847688 | 27 | 14. Ndf3 | mistake | inaccuracy | precision | inaccuracy | 0.0966 | 0.544 | no | g4 | h5 | -0.60 | -0.56 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0741 | 0.552 | no | bxc4 | Qd7 | +0.53 | +0.23 |
| 1034847688 | 37 | 19. Rh4 | mistake | inaccuracy | precision | inaccuracy | 0.0984 | 0.556 | no | Rh6 | Rh6 | -0.10 | -0.45 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.542 | yes | Nxf3 | - | -0.10 | -0.43 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.535 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.00 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0487 | 0.500 | no | fxe6 | - | +0.46 | +0.68 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.564 | yes | exf7+ | - | +0.09 | +0.74 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | excellent | precision | excellent | 0.0074 | 0.431 | no | Rxf7 | Rxf7 | +0.92 | +0.83 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 0.977 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0362 | 0.573 | no | d4 | - | +0.37 | +0.41 |
| 1041474766 | 8 | 4... Nf6 | book | best | precision | best | 0.0000 | 0.463 | yes | Nf6 | - | +0.38 | +0.50 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.545 | no | Nf3 | - | +0.34 | +0.38 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0018 | 0.466 | no | Nc6 | - | +0.59 | +0.40 |
| 1041474766 | 11 | 6. Nge2 | book | excellent | precision | excellent | 0.0089 | 0.536 | no | Nf3 | - | +0.17 | +0.30 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.523 | yes | O-O | - | +0.28 | +0.28 |
| 1041474766 | 16 | 8... Bb4 | good | inaccuracy | precision | inaccuracy | 0.0522 | 0.479 | no | Be7 | - | +0.76 | +0.78 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0223 | 0.532 | no | d5 | - | +0.08 | +0.01 |
| 184759554082 | 9 | 5. h4 | inaccuracy | good | precision | good | 0.0254 | 0.541 | no | Nf3 | Be2 | -0.11 | +0.10 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0191 | 0.484 | no | Nc3 | - | -0.25 | -0.22 |
| 184759554082 | 15 | 8. hxg6 | good | excellent | precision | excellent | 0.0032 | 0.513 | no | Nc3 | - | -0.21 | -0.10 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.516 | yes | hxg6 | - | -0.13 | -0.02 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0703 | 0.691 | no | d5 | d5 | -0.52 | -0.47 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.577 | yes | d5 | - | -0.52 | -0.38 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.785 | yes | Qxg5 | - | -1.98 | -1.82 |
| 184759554082 | 33 | 17. Qc2 | best | excellent | precision | excellent | 0.0156 | 0.342 | no | Qc1 | - | -0.96 | -1.25 |
| 184759554082 | 34 | 17... Qg5 | excellent | inaccuracy | precision | inaccuracy | 0.0555 | 0.689 | no | Bg4 | - | -0.88 | -0.86 |
| 184759554082 | 35 | 18. O-O-O | good | inaccuracy | precision | inaccuracy | 0.0514 | 0.366 | no | Qb2+ | - | -1.01 | -1.25 |
| 184759554082 | 37 | 19. Kb1 | good | best | precision | best | 0.0000 | 0.343 | yes | Kb1 | - | -1.19 | -1.23 |
| 184759554082 | 38 | 19... Bf5 | excellent | good | precision | good | 0.0411 | 0.686 | no | Rh8 | - | -1.10 | -0.94 |
| 184759554082 | 44 | 22... Rd6 | excellent | best | precision | best | 0.0000 | 0.716 | yes | Rd6 | - | -1.28 | -1.31 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0013 | 0.303 | no | Ka1 | - | -1.28 | -1.31 |
| 184759554082 | 47 | 24. Ka1 | best | excellent | precision | excellent | 0.0115 | 0.282 | no | Rh1 | - | -1.28 | -1.56 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.730 | yes | a5 | - | -1.16 | -1.58 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0050 | 0.268 | no | Qc3 | f3 | -1.61 | -1.67 |
| 184759554082 | 52 | 26... Rh8 | good | inaccuracy | precision | inaccuracy | 0.0641 | 0.760 | no | Bd5 | - | -1.41 | -1.30 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0489 | 0.555 | no | dxc6 | - | -0.08 | +0.11 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.499 | yes | Nf3 | - | -0.16 | +0.00 |
| 185209623352 | 14 | 7... Qd6 | inaccuracy | good | precision | good | 0.0380 | 0.471 | no | Rc8 | Bd7 | +1.28 | +1.19 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.774 | yes | Nxe4 | - | +5.09 | +5.42 |
| 185209623352 | 20 | 10... dxe4 | mistake | good | precision | good | 0.0218 | 0.227 | no | Qxe5 | - | +6.16 | +5.99 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0747 | 0.795 | no | Nxc6 | Nxc6 | +4.00 | +4.09 |
| 185209623352 | 22 | 11... Qxd4 | excellent | best | precision | best | 0.0000 | 0.284 | yes | Qxd4 | - | +4.04 | +4.22 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0073 | 0.722 | no | Bxc6 | - | +4.04 | +4.07 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0394 | 0.706 | no | O-O-O | O-O-O | +3.00 | +3.38 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0369 | 0.318 | no | e5 | - | +4.18 | +4.16 |
| 185209623352 | 33 | 17. Bd7+ | best | excellent | precision | excellent | 0.0149 | 0.717 | no | Bb3 | - | +4.22 | +4.26 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.276 | yes | Kc7 | - | +4.76 | +4.66 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1803 | 0.721 | no | Bxe6 | - | +0.61 | +0.73 |
| 185209623352 | 42 | 21... Nf4 | miss | mistake | precision | mistake | 0.1302 | 0.459 | no | Bh6+ | Bh6+ | +3.32 | +3.16 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.671 | yes | Rc5+ | - | +3.32 | +3.09 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.439 | yes | Nd3+ | - | +0.92 | +1.20 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.567 | yes | Nxd3 | Rxd3 | -0.61 | -0.54 |
| 185209623352 | 49 | 25. Rb5+ | excellent | best | precision | best | 0.0000 | 0.707 | yes | Rb5+ | - | +3.97 | +3.85 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0139 | 0.295 | no | Ka6 | - | +3.97 | +4.29 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0090 | 0.731 | no | Rd5 | - | +3.97 | +4.04 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0168 | 0.286 | no | Bc3 | - | +4.48 | +4.41 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0098 | 0.736 | no | Kc3 | - | +4.14 | +4.32 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0342 | 0.292 | no | Kf5 | - | +4.38 | +4.70 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.743 | yes | Kc2 | - | +4.38 | +4.56 |
| 185209623352 | 70 | 35... Rxc4 | excellent | best | precision | best | 0.0000 | 0.257 | yes | Rxc4 | - | +4.77 | +4.64 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0299 | 0.675 | no | Kd3 | - | +2.98 | +2.41 |
| 185209623352 | 77 | 39. Kb1 | inaccuracy | good | precision | good | 0.0323 | 0.640 | no | Rh5 | g4 | +1.67 | +1.93 |
| 185209623352 | 78 | 39... Rb2+ | good | excellent | precision | excellent | 0.0086 | 0.393 | no | Rf2 | - | +2.15 | +2.01 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.612 | yes | Kc1 | - | +2.15 | +2.34 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0686 | 0.267 | no | Kd5 | - | +6.01 | +6.18 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1533 | 0.657 | no | Rhxe7 | Rhxe7 | -0.08 | -0.12 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1914 | 0.500 | no | Kf7 | - | +3.73 | +3.57 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.691 | yes | Rf1+ | - | +3.73 | +3.46 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.752 | yes | Kxb2 | - | +5.17 | +4.98 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0146 | 0.210 | no | b5 | - | +6.38 | +6.25 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0018 | 0.803 | no | Ra7 | - | +6.33 | +6.36 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.807 | yes | R7xb5 | - | +6.30 | +6.39 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0014 | 0.811 | no | Rb6 | - | +6.59 | +6.41 |
| 185209623352 | 108 | 54... Kh5 | excellent | best | precision | best | 0.0000 | 0.190 | yes | Kh5 | - | +6.70 | +6.53 |
| 185209623352 | 112 | 56... Bxe5 | excellent | best | precision | best | 0.0000 | 0.188 | yes | Bxe5 | - | +6.75 | +6.46 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.194 | yes | Kf6 | - | +7.19 | +6.95 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0022 | 0.088 | no | Ke7 | Ke7 | +10.6 | +9.00 |
| 185209623352 | 117 | 59. h5 | good | excellent | precision | excellent | 0.0009 | 0.884 | no | Kc3 | - | +8.42 | +8.40 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | +8.73 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg5 | - | M3 | M6 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 142 | 71... Kb5 | good | excellent | precision | excellent | 0.0000 | 0.082 | no | Kb7 | - | M8 | +10.05 |
| 185209623352 | 145 | 73. g6 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kb2 | - | M5 | M7 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ka6 | - | M5 | M6 |
| 185209623352 | 153 | 77. Qc7 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qc7 | - | M3 | M3 |
| 185324357184 | 6 | 3... Bc5 | blunder | mistake | precision | mistake | 0.1893 | 0.513 | no | d5 | - | +3.27 | +3.23 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0118 | 0.296 | no | d4 | - | -4.03 | -4.02 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0322 | 0.600 | no | Ng3 | Ng3 | -0.98 | -1.06 |
| 185324357184 | 19 | 10. Ne2 | good | excellent | precision | excellent | 0.0179 | 0.440 | no | Qd4 | - | -1.32 | -1.38 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0691 | 0.578 | no | Na6 | - | +0.29 | +0.42 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.524 | yes | Qg1 | - | +0.29 | +0.13 |
| 185324357184 | 34 | 17... Rxe2 | good | excellent | precision | excellent | 0.0182 | 0.357 | no | d4 | - | +3.07 | +2.93 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.677 | yes | Re1 | - | +3.07 | +3.21 |
| 185324357184 | 46 | 23... b5 | excellent | best | precision | best | 0.0000 | 0.491 | yes | b5 | - | +0.26 | +0.26 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0091 | 0.515 | no | b3 | - | +0.26 | +0.15 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0233 | 0.554 | no | d4 | - | +0.65 | +0.52 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.602 | yes | Nxe5 | - | +1.74 | +1.98 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0938 | 0.300 | no | d4 | d3 | -5.55 | -5.79 |
| 185437323918 | 17 | 9. Qd3 | excellent | best | precision | best | 0.0000 | 0.217 | yes | Qd3 | - | -5.63 | -5.90 |
| 185437323918 | 18 | 9... Nxd5 | good | best | precision | best | 0.0000 | 0.798 | yes | Nxd5 | - | -5.16 | -5.58 |
| 185437323918 | 20 | 10... d6 | excellent | inaccuracy | precision | inaccuracy | 0.0549 | 0.808 | no | g4 | - | -4.94 | -4.78 |
| 185437323918 | 28 | 14... g6 | good | excellent | precision | excellent | 0.0143 | 0.817 | no | Kg8 | - | -6.13 | -6.03 |
| 185437323918 | 31 | 16. Nd2 | excellent | best | precision | best | 0.0000 | 0.197 | yes | Nd2 | - | -6.16 | -5.98 |
| 185437323918 | 34 | 17... Qe7 | best | good | precision | good | 0.0215 | 0.816 | no | Kg7 | - | -6.58 | -5.81 |
| 185437323918 | 35 | 18. Bb2 | mistake | blunder | precision | blunder | 0.2051 | 0.205 | no | Nf3 | - | -M2 | -M2 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.777 | no | Qe2 | - | -5.96 | -6.02 |
| 185437323918 | 42 | 21... gxf3 | brilliant | inaccuracy | precision | inaccuracy | 0.0651 | 0.739 | no | Qf4 | - | -3.59 | -2.84 |
| 185437323918 | 49 | 25. a4 | miss | blunder | precision | blunder | 0.2485 | 0.482 | no | g4 | g4 | -5.00 | -5.10 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0125 | 0.772 | no | b6 | - | -4.41 | -4.93 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.787 | yes | Be4 | - | -5.61 | -5.68 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0082 | 0.826 | no | Rf8 | - | -6.21 | -6.35 |
| 185437323918 | 64 | 32... Kxg5 | good | excellent | precision | excellent | 0.0087 | 0.802 | no | e4 | - | -5.64 | -5.61 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | good | precision | good | 0.0247 | 0.227 | no | Kg2 | Kg2 | -6.13 | -5.75 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0484 | 0.793 | no | e4 | e4 | -5.01 | -4.58 |
| 185437323918 | 71 | 36. Kg3 | excellent | best | precision | best | 0.0000 | 0.218 | yes | Kg3 | - | -5.97 | -5.86 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.231 | yes | Kf3 | - | -6.12 | -5.70 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0000 | 0.791 | no | e4+ | - | -6.12 | -6.12 |
| 185437323918 | 75 | 38. Ke4 | best | excellent | precision | excellent | 0.0152 | 0.194 | no | Ke2 | - | -6.12 | -5.55 |
| 185437323918 | 76 | 38... Rf4+ | best | excellent | precision | excellent | 0.0096 | 0.785 | no | Bc3 | - | -6.12 | -6.41 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0122 | 0.847 | no | Bg3 | - | -7.28 | -8.02 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.134 | yes | Kxc7 | - | -8.05 | -7.20 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0028 | 0.843 | no | Bg3+ | - | -8.05 | -8.63 |
| 185437323918 | 89 | 45. c5 | excellent | best | precision | best | 0.0000 | 0.115 | yes | c5 | - | -8.94 | -7.96 |
| 185437323918 | 91 | 46. Kxb7 | excellent | best | precision | best | 0.0000 | 0.102 | yes | Kxb7 | - | -9.64 | -8.36 |
| 185437323918 | 93 | 47. d7 | excellent | good | precision | good | 0.0323 | 0.099 | no | Kc6 | - | -11.0 | -11.33 |
| 185437323918 | 94 | 47... Qb2+ | excellent | best | precision | best | 0.0000 | 0.933 | yes | Qb2+ | - | -9.07 | -10.51 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.079 | yes | Kc6 | Ka6 | -M17 | -10.77 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0136 | 0.925 | no | Qh8 | - | -M16 | -11.08 |
| 185437323918 | 97 | 49. Kd5 | best | good | precision | good | 0.0276 | 0.070 | no | d8=Q | - | -M16 | -10.27 |
| 185437323918 | 98 | 49... Qb7+ | good | excellent | precision | excellent | 0.0182 | 0.916 | no | Qg8+ | - | -8.99 | -9.34 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0065 | 0.910 | no | Qb6 | - | -10.7 | -10.01 |
| 185437323918 | 101 | 51. Ke6 | good | best | precision | best | 0.0000 | 0.088 | yes | Ke6 | - | -M6 | -12.17 |
| 185437323918 | 105 | 53. Ke7 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kf8 | - | -M3 | -M10 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2310 | 0.231 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0154 | 0.508 | no | Nf3 | - | -0.01 | -0.13 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.508 | yes | h6 | - | -0.01 | -0.19 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.489 | yes | Bh4 | - | -0.01 | -0.13 |
| 185438707002 | 15 | 8. h3 | inaccuracy | good | precision | good | 0.0479 | 0.548 | no | h4 | h4 | -0.33 | -0.48 |
| 185438707002 | 19 | 10. Nf3 | excellent | best | precision | best | 0.0000 | 0.477 | yes | Nf3 | - | -0.52 | -0.34 |
| 185438707002 | 20 | 10... Be6 | inaccuracy | good | precision | good | 0.0480 | 0.520 | no | g4 | g4 | +0.37 | +0.47 |
| 185438707002 | 26 | 13... O-O-O | miss | inaccuracy | precision | inaccuracy | 0.0783 | 0.631 | no | Rg8 | Rg8 | -0.69 | -0.58 |
| 185438707002 | 30 | 15... Nxf3+ | good | inaccuracy | precision | inaccuracy | 0.0528 | 0.456 | no | Qg7 | - | +1.28 | +1.66 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.574 | yes | c3 | - | +1.35 | +1.39 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0828 | 0.418 | no | Bb6 | - | +2.65 | +2.88 |
| 185438707002 | 40 | 20... Rxh8 | best | excellent | precision | excellent | 0.0023 | 0.261 | no | e5 | - | +3.97 | +4.27 |
| 185438707002 | 42 | 21... Nb6 | good | excellent | precision | excellent | 0.0143 | 0.285 | no | Ne5 | - | +3.99 | +4.18 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0300 | 0.729 | no | Kb1 | - | +3.74 | +3.56 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0126 | 0.722 | no | Rd2 | - | +3.82 | +3.67 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0599 | 0.295 | no | Rg8 | - | +4.87 | +4.97 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0487 | 0.765 | no | Qf6 | Qf6 | +3.70 | +3.90 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.292 | yes | a6 | - | +3.78 | +3.94 |
| 185438707002 | 54 | 27... Rf8 | mistake | inaccuracy | precision | inaccuracy | 0.0938 | 0.293 | no | Re8 | Rh7 | +5.73 | +5.86 |
| 185438707002 | 55 | 28. Rd8+ | miss | inaccuracy | precision | inaccuracy | 0.0850 | 0.801 | no | Qxf8+ | Qxf8+ | +3.74 | +3.97 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.720 | yes | Qxd8+ | - | +3.69 | +3.91 |
| 185438707002 | 59 | 30. Qxh4 | excellent | good | precision | good | 0.0217 | 0.703 | no | Qd2 | - | +3.68 | +3.21 |
| 185438707002 | 61 | 31. Qg3 | inaccuracy | mistake | precision | mistake | 0.1054 | 0.709 | no | b4 | a4 | +2.58 | +1.77 |
| 185438707002 | 63 | 32. b4 | good | excellent | precision | excellent | 0.0137 | 0.646 | no | Rd2 | - | +1.87 | +1.64 |
| 185438707002 | 68 | 34... Qb2+ | great | good | precision | good | 0.0217 | 0.715 | no | Qa2+ | - | -3.65 | -3.74 |
| 185438707002 | 74 | 37... Qxd5 | excellent | best | precision | best | 0.0000 | 0.721 | yes | Qxd5 | - | -3.38 | -3.49 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0388 | 0.671 | no | Qe2 | - | -2.36 | -2.28 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0113 | 0.876 | no | e4 | - | -8.73 | -7.81 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.136 | yes | g4 | - | -8.80 | -7.88 |
| 185438707002 | 89 | 45. g3 | inaccuracy | good | precision | good | 0.0334 | 0.136 | no | b5 | g5 | -M7 | -9.15 |
| 185438707002 | 90 | 45... e3 | best | excellent | precision | excellent | 0.0156 | 0.898 | no | Qf1+ | - | -M6 | -8.99 |
| 185438707002 | 91 | 46. Kh4 | best | mistake | precision | mistake | 0.1060 | 0.106 | no | g5 | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | good | precision | good | 0.0416 | 0.392 | no | e6 | e6 | +1.09 | +0.97 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0146 | 0.650 | no | Nc3 | - | +0.96 | +0.85 |
| 185456088510 | 7 | 4. Nf3 | best | excellent | precision | excellent | 0.0015 | 0.644 | no | Nc3 | - | +1.01 | +1.10 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0042 | 0.332 | no | d5 | - | +1.01 | +1.08 |
| 185456088510 | 10 | 5... g6 | good | excellent | precision | excellent | 0.0000 | 0.342 | no | Nc6 | - | +1.14 | +0.99 |
| 185456088510 | 11 | 6. h4 | good | best | precision | best | 0.0000 | 0.653 | no | Bf4 | - | +0.95 | +0.99 |
| 185456088510 | 15 | 8. Be3 | good | best | precision | best | 0.0000 | 0.628 | yes | Be3 | - | +0.81 | +0.87 |
| 185456088510 | 18 | 9... Ngf6 | best | excellent | precision | excellent | 0.0045 | 0.387 | no | Bg7 | - | +0.65 | +0.88 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.637 | yes | Ng3 | - | +0.65 | +0.59 |
| 185456088510 | 20 | 10... Ng4 | excellent | good | precision | good | 0.0289 | 0.407 | no | h5 | - | +0.74 | +0.92 |
| 185456088510 | 21 | 11. Bd2 | excellent | best | precision | best | 0.0000 | 0.642 | yes | Bd2 | - | +0.70 | +0.82 |
| 185456088510 | 23 | 12. c3 | inaccuracy | good | precision | good | 0.0478 | 0.674 | no | h5 | h5 | +0.70 | +0.75 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.678 | yes | h5 | - | +1.12 | +1.23 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.757 | yes | exd6 | - | +1.55 | +1.52 |
| 185456088510 | 33 | 17. Ne4 | mistake | blunder | precision | blunder | 0.2162 | 0.739 | no | Qe2 | Qe2 | +0.65 | +0.14 |
| 185456088510 | 37 | 19. dxc5 | excellent | inaccuracy | precision | inaccuracy | 0.0521 | 0.829 | no | Nh4 | - | +1.72 | +1.79 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0558 | 0.154 | no | Rd6 | - | +2.89 | +3.49 |
| 185456088510 | 47 | 24. b4 | best | good | precision | good | 0.0276 | 0.902 | no | a5 | - | +2.89 | +3.05 |
| 185456088510 | 49 | 25. Be3 | inaccuracy | good | precision | good | 0.0410 | 0.864 | no | a5 | a5 | +1.93 | +2.41 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.913 | yes | Nxe3 | - | -4.25 | -3.96 |
| 185456088510 | 59 | 30. b5 | excellent | good | precision | good | 0.0335 | 0.052 | no | Qb5 | - | -6.85 | -6.27 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0138 | 0.456 | no | Na4 | - | -0.94 | -0.95 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0163 | 0.488 | no | Ne5 | - | +0.60 | +0.49 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0358 | 0.472 | no | Kf8 | - | +0.61 | +1.10 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | excellent | precision | excellent | 0.0063 | 0.426 | no | dxe5 | dxe5 | +1.53 | +1.57 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.590 | yes | Qh5 | - | +1.48 | +1.30 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1908 | 0.624 | no | Nxc7+ | Nxc7+ | -0.91 | -1.16 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0068 | 0.433 | no | b4 | - | -1.28 | -1.14 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.698 | yes | Rf8 | - | -3.36 | -3.45 |
| 185468039834 | 31 | 16. b4 | excellent | best | precision | best | 0.0000 | 0.309 | no | Qh3 | - | -3.61 | -3.50 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0064 | 0.513 | no | d3 | - | +0.15 | +0.13 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.492 | yes | exd4 | - | +0.15 | +0.17 |
| 185468614210 | 11 | 6. cxd4 | book | best | precision | best | 0.0000 | 0.510 | yes | cxd4 | - | 0.00 | -0.08 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.505 | yes | Bb4+ | - | 0.00 | +0.06 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0181 | 0.504 | no | Bd2 | - | -0.35 | -0.49 |
| 185468614210 | 15 | 8. d5 | excellent | good | precision | good | 0.0284 | 0.558 | no | Bg5 | - | +0.51 | +0.46 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0456 | 0.473 | no | Nxe4 | Nxe4 | +1.21 | +1.32 |
| 185468614210 | 25 | 13. Bd3 | good | excellent | precision | excellent | 0.0140 | 0.484 | no | Bxd6 | - | -0.61 | -0.54 |
| 185468614210 | 28 | 14... Nxd5 | excellent | best | precision | best | 0.0000 | 0.489 | yes | Nxd5 | - | +0.25 | +0.15 |
| 185468614210 | 31 | 16. Qxd5 | best | excellent | precision | excellent | 0.0006 | 0.509 | no | Ng5+ | - | +0.25 | +0.25 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0302 | 0.485 | no | Kg8 | Kg8 | +1.21 | +0.77 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0326 | 0.545 | no | Qh5+ | Qh5+ | +0.18 | +0.24 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.486 | yes | Kg8 | - | +0.18 | +0.20 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0116 | 0.549 | no | d4 | - | +0.74 | +0.59 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.466 | yes | Bb7 | - | +0.74 | +0.59 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.534 | yes | Nc3 | - | +0.74 | +0.68 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.460 | yes | e6 | - | +0.74 | +0.61 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0046 | 0.466 | no | d5 | - | +0.55 | +0.66 |
| 185475865432 | 11 | 6. Bb3 | inaccuracy | good | precision | good | 0.0407 | 0.538 | no | Bd3 | - | -0.37 | -0.05 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0980 | 0.563 | no | Ng3 | Ng3 | -0.76 | -0.60 |
| 185475865432 | 23 | 12. Bf4 | inaccuracy | good | precision | good | 0.0466 | 0.469 | no | Qxd8+ | - | -1.49 | -1.35 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0000 | 0.412 | no | Ned4 | - | -1.49 | -1.51 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0181 | 0.427 | no | hxg3 | - | -1.52 | -1.75 |
| 185475865432 | 30 | 15... Nxe5 | best | excellent | precision | excellent | 0.0011 | 0.600 | no | Qxd1 | - | -1.52 | -1.69 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0152 | 0.598 | no | Bd6 | - | -1.25 | -1.51 |
| 185475865432 | 34 | 17... Rxd8 | inaccuracy | good | precision | good | 0.0498 | 0.608 | no | Kxd8 | Kxd8 | -0.89 | -0.93 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0784 | 0.670 | no | Rxe6 | Rxe6 | +1.47 | +1.60 |
| 185475865432 | 51 | 26. a7 | excellent | good | precision | good | 0.0228 | 0.734 | no | Rxe6 | - | +3.79 | +3.99 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0564 | 0.629 | no | Bc4 | - | +0.50 | +0.46 |
| 185962590893 | 12 | 6... Bxf3 | excellent | best | precision | best | 0.0000 | 0.390 | yes | Bxf3 | - | +0.82 | +0.71 |
| 185962590893 | 14 | 7... Nd7 | best | excellent | precision | excellent | 0.0030 | 0.375 | no | Nf6 | - | +0.82 | +0.76 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.410 | yes | e5 | - | +0.67 | +0.73 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.427 | yes | Be7 | - | +0.55 | +0.40 |
| 185962590893 | 21 | 11. O-O-O | excellent | best | precision | best | 0.0000 | 0.563 | yes | O-O-O | - | +0.44 | +0.36 |
| 185962590893 | 23 | 12. Ne3 | inaccuracy | good | precision | good | 0.0329 | 0.638 | no | Ba5 | Ba5 | +0.66 | +0.46 |
| 185962590893 | 24 | 12... O-O | best | good | precision | good | 0.0232 | 0.427 | no | Nc5 | - | +0.66 | +0.61 |
| 185962590893 | 27 | 14. Nxe7+ | miss | inaccuracy | precision | inaccuracy | 0.0548 | 0.713 | no | Bh6 | Bh6 | +1.01 | +1.36 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0329 | 0.291 | no | Nf8 | Ne8 | +1.62 | +1.66 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0668 | 0.742 | no | Rxd8+ | Rxd8+ | +0.96 | +0.97 |
| 185962590893 | 35 | 18. g5 | best | good | precision | good | 0.0417 | 0.648 | no | Rxd7 | - | +0.96 | +0.90 |
| 185962590893 | 43 | 22. Bd2 | good | excellent | precision | excellent | 0.0059 | 0.645 | no | Qe2 | - | +0.86 | +0.90 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0196 | 0.396 | no | Nd7 | - | +0.86 | +0.79 |
| 185962590893 | 47 | 24. h4 | best | excellent | precision | excellent | 0.0030 | 0.623 | no | Qc3 | - | +0.86 | +0.81 |
| 185962590893 | 48 | 24... Nd7 | best | excellent | precision | excellent | 0.0177 | 0.374 | no | h6 | - | +0.86 | +0.83 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.607 | yes | Qe3 | Qf3 | +0.47 | +0.78 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0688 | 0.378 | no | Nf4 | Nf4 | +1.15 | +1.15 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2497 | 0.675 | no | f4 | - | -0.39 | -0.47 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `miss_detector` (8)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (tactic) | miss_detector | mistake | 0.1478 | 0.648 | no | g4 | - | -0.01 | -0.01 |
| 184759554082 | 27 | 14. cxd5 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1383 | 0.239 | no | Bb2 | Bb2 | -3.24 | -3.43 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1992 | 0.802 | no | Rxf6+ | Rxf6+ | +2.74 | +2.66 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.4039 | 0.764 | no | Rxf6+ | - | -2.81 | -2.55 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | mistake | 0.1995 | 0.718 | no | Kg7 | - | -0.17 | -0.31 |
| 185437323918 | 107 | 54. Ke8 | excellent | miss (opportunity) | miss_detector | mistake | 0.1091 | 0.109 | no | Kf6 | - | -M1 | -M1 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (opportunity) | miss_detector | blunder | 0.2348 | 0.235 | no | Kd2 | - | -M1 | -M1 |
| 185468614210 | 7 | 4. c3 | mistake | miss (tactic) | miss_detector | mistake | 0.1257 | 0.584 | no | Nxe5 | Nxe5 | -0.88 | -0.71 |

### `great_find_event` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.520 | yes | Bxe5 | - | +0.18 | +0.31 |
| 185438343298 | 15 | 8. g3 | best | great | great_find_event | best | 0.0000 | 0.218 | yes | g3 | - | -5.11 | -5.58 |
| 185438707002 | 84 | 42... Nxg3 | best | great | great_find_event | best | 0.0000 | 0.841 | yes | Nxg3 | - | -7.11 | -6.94 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0118 | 0.461 | no | Nf6 | - | +0.82 | +0.98 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | good | 0.0437 | 0.523 | no | Nxe5 | Nxe5 | -0.62 | -0.36 |

### `mate_override` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M7 |

### `blunder_softened` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2083 | 0.576 | no | Qxg3+ | Qxg3+ | +2.48 | +2.37 |

