# Calibration report: r-off250-hr0

- Generated: 2026-10-18T08:02:00+00:00
- Commit: `02f0952c30a0` + uncommitted backend changes (diff sha256 `dfcec51fd48f`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: `{"great_find":{"require_high_rated":false},"rating_offset":250}`
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 71.6% (613/856) |
| Within one step | 89.5% (766/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.78 / 0.27 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 1.05 |
| Accuracy mean abs. difference | 3.05 (n=28, max 8.18) |
| Accuracy bias (ours - app) | +2.93 |
| Best move = app's suggestion | 81.0% (111/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | 1 | . | . | . | . | . | 3 |
| **great** | . | **7** | 19 | . | . | . | . | . | . | . | 26 |
| **best** | . | 2 | **269** | 37 | 6 | . | 2 | . | . | . | 316 |
| **excellent** | . | . | 36 | **64** | 22 | 1 | 3 | 1 | . | . | 127 |
| **good** | . | . | 5 | 25 | **65** | . | 7 | . | 1 | . | 103 |
| **book** | . | . | 8 | 6 | 4 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 6 | 3 | 13 | 1 | **62** | 7 | . | . | 92 |
| **mistake** | . | . | . | . | 4 | . | 3 | **34** | 2 | 1 | 44 |
| **miss** | . | . | . | . | 1 | . | 4 | 4 | **16** | 2 | 27 |
| **blunder** | . | . | . | . | . | . | . | 2 | 3 | **16** | 21 |
| **total** | 1 | 9 | 344 | 135 | 116 | 81 | 81 | 48 | 22 | 19 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 9 | 7 | 0.778 | 0.269 | 0.400 |
| best | 316 | 344 | 269 | 0.782 | 0.851 | 0.815 |
| excellent | 127 | 135 | 64 | 0.474 | 0.504 | 0.489 |
| good | 103 | 116 | 65 | 0.560 | 0.631 | 0.594 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 81 | 62 | 0.765 | 0.674 | 0.717 |
| mistake | 44 | 48 | 34 | 0.708 | 0.773 | 0.739 |
| miss | 27 | 22 | 16 | 0.727 | 0.593 | 0.653 |
| blunder | 21 | 19 | 16 | 0.842 | 0.762 | 0.800 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.4 | +5.7 |
| 1034847688 | black | 65.0 | 73.2 | +8.2 |
| 1041474766 | white | 98.0 | 97.3 | -0.7 |
| 1041474766 | black | 83.8 | 86.0 | +2.2 |
| 184759554082 | white | 81.2 | 86.3 | +5.1 |
| 184759554082 | black | 87.7 | 90.7 | +3.0 |
| 185209623352 | white | 72.7 | 75.0 | +2.3 |
| 185209623352 | black | 72.6 | 73.5 | +0.9 |
| 185324357184 | white | 73.0 | 76.4 | +3.4 |
| 185324357184 | black | 62.4 | 64.1 | +1.7 |
| 185436488062 | white | 98.6 | 97.6 | -1.0 |
| 185436488062 | black | 38.5 | 41.6 | +3.1 |
| 185437323918 | white | 69.5 | 71.6 | +2.1 |
| 185437323918 | black | 75.7 | 75.9 | +0.2 |
| 185438343298 | white | 46.9 | 47.0 | +0.1 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 80.5 | +2.7 |
| 185438707002 | black | 83.0 | 84.1 | +1.1 |
| 185456088510 | white | 78.4 | 83.3 | +4.9 |
| 185456088510 | black | 82.2 | 85.6 | +3.4 |
| 185468039834 | white | 80.0 | 84.4 | +4.4 |
| 185468039834 | black | 87.5 | 91.0 | +3.5 |
| 185468614210 | white | 70.8 | 76.5 | +5.7 |
| 185468614210 | black | 77.1 | 82.4 | +5.3 |
| 185475865432 | white | 78.1 | 82.4 | +4.3 |
| 185475865432 | black | 66.1 | 72.4 | +6.3 |
| 185962590893 | white | 90.8 | 92.5 | +1.7 |
| 185962590893 | black | 90.9 | 93.3 | +2.4 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 61.2% | 77.6% | reviewed | 0.5 |
| 1041474766 | 25 | 25 | 72.0% | 80.0% | reviewed | 0.5 |
| 184759554082 | 62 | 62 | 69.4% | 87.1% | reviewed | 0.5 |
| 185209623352 | 155 | 155 | 67.7% | 91.0% | reviewed | 0.5 |
| 185324357184 | 55 | 55 | 81.8% | 96.4% | reviewed | 0.5 |
| 185436488062 | 13 | 13 | 76.9% | 92.3% | reviewed | 0.5 |
| 185437323918 | 108 | 103 | 64.1% | 85.4% | reviewed | 0.5 |
| 185438343298 | 20 | 20 | 95.0% | 95.0% | reviewed | 0.5 |
| 185438707002 | 95 | 91 | 76.9% | 93.4% | reviewed | 0.5 |
| 185456088510 | 60 | 60 | 70.0% | 90.0% | reviewed | 0.5 |
| 185468039834 | 38 | 38 | 65.8% | 92.1% | reviewed | 0.5 |
| 185468614210 | 54 | 54 | 74.1% | 87.0% | reviewed | 0.5 |
| 185475865432 | 53 | 53 | 73.6% | 92.5% | reviewed | 0.5 |
| 185962590893 | 78 | 78 | 78.2% | 91.0% | reviewed | 0.5 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label is one of the collector's candidates for 9 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | excellent | precision |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | best | precision |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (243)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 222 | best -> excellent x37, excellent -> best x36, good -> excellent x25, excellent -> good x22, great -> best x19, inaccuracy -> good x13 |
| `mate_override` | 6 | excellent -> inaccuracy x2, best -> inaccuracy x2, good -> miss x1, good -> inaccuracy x1 |
| `miss_detector` | 5 | blunder -> miss x3, mistake -> miss x2 |
| `blunder_softened` | 4 | miss -> mistake x3, blunder -> mistake x1 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `great_find_event` | 2 | best -> great x2 |
| `losing_material_hardened` | 2 | inaccuracy -> mistake x1, excellent -> mistake x1 |

### `precision` (222)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 4 | 2... Nf6 | excellent | best | precision | best | 0.0000 | 0.478 | yes | Nf6 | - | +0.33 | +0.31 |
| 1034847688 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0011 | 0.504 | no | c5 | - | +0.13 | +0.12 |
| 1034847688 | 13 | 7. Bb2 | best | good | precision | good | 0.0211 | 0.488 | no | Be2 | - | -0.10 | -0.21 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0389 | 0.524 | no | Be2 | - | +0.12 | -0.13 |
| 1034847688 | 18 | 9... b5 | good | inaccuracy | precision | inaccuracy | 0.0577 | 0.514 | no | Bf5 | - | +0.38 | +0.39 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0550 | 0.576 | no | cxb5 | - | +0.24 | +0.19 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0942 | 0.653 | no | cxb5 | cxb5 | +0.44 | +0.35 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.461 | yes | h6 | - | +0.90 | +0.53 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0908 | 0.561 | no | bxc4 | Qd7 | +0.53 | +0.27 |
| 1034847688 | 30 | 15... Nh5 | miss | blunder | precision | blunder | 0.3172 | 0.640 | no | a4 | a4 | +1.64 | +1.67 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.545 | yes | Nxf3 | - | -0.10 | -0.44 |
| 1034847688 | 40 | 20... Nf5 | inaccuracy | excellent | precision | excellent | 0.0111 | 0.511 | no | Nh5 | f5 | +0.50 | +0.38 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.542 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.29 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0374 | 0.468 | no | fxe6 | - | +0.46 | +0.77 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.585 | yes | exf7+ | - | +0.09 | +0.89 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.402 | yes | Kxf7 | Rxf7 | +0.92 | +1.24 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0324 | 0.581 | no | d4 | - | +0.37 | +0.46 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0053 | 0.451 | no | e5 | - | +0.38 | +0.50 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.553 | yes | Bg2 | - | +0.34 | +0.43 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0032 | 0.454 | no | Nc6 | - | +0.59 | +0.46 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0307 | 0.549 | no | Nf3 | - | +0.17 | +0.17 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.522 | no | d4 | - | +0.28 | +0.29 |
| 1041474766 | 20 | 10... O-O | excellent | best | precision | best | 0.0000 | 0.463 | yes | O-O | - | +0.40 | +0.27 |
| 184759554082 | 6 | 3... a6 | book | excellent | precision | excellent | 0.0191 | 0.537 | no | d5 | - | +0.08 | +0.04 |
| 184759554082 | 8 | 4... g6 | good | excellent | precision | excellent | 0.0175 | 0.484 | no | d5 | - | +0.32 | +0.34 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0079 | 0.475 | no | Nc3 | - | -0.25 | -0.21 |
| 184759554082 | 12 | 6... Bg7 | good | excellent | precision | excellent | 0.0191 | 0.533 | no | d5 | - | 0.00 | +0.09 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0398 | 0.505 | no | Nxh5 | - | +0.03 | +0.11 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0932 | 0.689 | no | d5 | d5 | -0.52 | -0.47 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.585 | yes | d5 | - | -0.52 | -0.57 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1362 | 0.410 | no | cxd5 | cxd5 | -1.98 | -2.01 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.835 | yes | Qxg5 | - | -1.98 | -2.62 |
| 184759554082 | 34 | 17... Qg5 | excellent | good | precision | good | 0.0421 | 0.670 | no | Bg4 | - | -0.88 | -0.82 |
| 184759554082 | 37 | 19. Kb1 | good | excellent | precision | excellent | 0.0181 | 0.333 | no | Qb2 | - | -1.19 | -1.22 |
| 184759554082 | 38 | 19... Bf5 | excellent | inaccuracy | precision | inaccuracy | 0.0574 | 0.685 | no | Rh8 | - | -1.10 | -0.82 |
| 184759554082 | 44 | 22... Rd6 | excellent | best | precision | best | 0.0000 | 0.713 | no | a5 | - | -1.28 | -1.33 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0119 | 0.300 | no | Rh1 | - | -1.28 | -1.38 |
| 184759554082 | 47 | 24. Ka1 | best | excellent | precision | excellent | 0.0000 | 0.295 | no | b4 | - | -1.28 | -1.34 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.701 | yes | a5 | - | -1.16 | -1.56 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0062 | 0.270 | no | f3 | f3 | -1.61 | -1.73 |
| 184759554082 | 56 | 28... Ree8 | good | excellent | precision | excellent | 0.0152 | 0.765 | no | Rxh1 | - | -1.61 | -1.58 |
| 185209623352 | 8 | 4... Nc6 | best | excellent | precision | excellent | 0.0007 | 0.496 | no | Nf6 | - | -0.08 | +0.02 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.501 | yes | Nf3 | - | -0.16 | +0.00 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.838 | yes | Nxe4 | - | +5.09 | +5.67 |
| 185209623352 | 20 | 10... dxe4 | mistake | good | precision | good | 0.0208 | 0.159 | no | Qxe5 | - | +6.16 | +6.23 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0767 | 0.861 | no | Nxc6 | Nxc6 | +4.00 | +4.36 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0090 | 0.787 | no | Bxc6 | - | +4.04 | +4.19 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0484 | 0.785 | no | O-O-O | O-O-O | +3.00 | +3.64 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0406 | 0.256 | no | b5 | - | +4.18 | +4.41 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.228 | yes | Kc7 | - | +4.76 | +4.53 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0442 | 0.790 | no | Nd8 | Nd8 | +3.29 | +3.68 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.412 | no | Bxe5 | - | +0.92 | +1.22 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.588 | yes | Nxd3 | Rxd3 | -0.61 | -0.51 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0141 | 0.226 | no | Ka6 | - | +3.97 | +4.15 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0051 | 0.780 | no | Rd5 | - | +3.97 | +4.09 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.796 | yes | Kb2 | - | +4.39 | +4.46 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0067 | 0.799 | no | Rh5 | - | +4.14 | +4.56 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0144 | 0.825 | no | Rh5 | - | +4.64 | +4.97 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0339 | 0.826 | no | Rh5 | - | +4.51 | +4.86 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0349 | 0.240 | no | Kf5 | - | +4.38 | +4.39 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.784 | yes | Kc2 | - | +4.38 | +4.63 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0443 | 0.722 | no | Kd3 | - | +2.98 | +2.43 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.653 | yes | Kc1 | - | +2.15 | +2.41 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.825 | yes | Kxb2 | - | +5.17 | +5.33 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0169 | 0.173 | no | Bxf4 | - | +5.65 | +5.75 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0099 | 0.145 | no | b5 | - | +6.38 | +6.33 |
| 185209623352 | 101 | 51. Rb4 | excellent | best | precision | best | 0.0000 | 0.866 | yes | Rb4 | - | +6.27 | +6.30 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0007 | 0.866 | no | Rc7 | - | +6.33 | +6.54 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0026 | 0.128 | no | Bd8 | - | +6.33 | +6.47 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.870 | yes | R7xb5 | - | +6.30 | +6.66 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0000 | 0.877 | no | Rc4 | - | +6.59 | +6.71 |
| 185209623352 | 110 | 55... Kg6 | excellent | best | precision | best | 0.0000 | 0.125 | no | Bg7 | - | +6.54 | +6.65 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0000 | 0.875 | no | Rb6 | - | +6.54 | +6.77 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.078 | yes | Kf6 | - | +7.19 | +8.34 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0087 | 0.042 | no | Ke7 | Ke7 | +10.6 | +11.15 |
| 185209623352 | 117 | 59. h5 | good | excellent | precision | excellent | 0.0157 | 0.963 | no | Kc3 | - | +8.42 | +13.12 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | +12.25 |
| 185209623352 | 124 | 62... Kf6 | excellent | best | precision | best | 0.0000 | 0.000 | no | Ke6 | - | M6 | M9 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | - | M5 | M11 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg5 | - | M3 | M6 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M9 |
| 185324357184 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0036 | 0.570 | no | O-O | - | -1.29 | -1.17 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0102 | 0.243 | no | d4 | - | -4.03 | -4.09 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.521 | yes | Qg1 | - | +0.29 | +0.15 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0378 | 0.300 | no | Qh5 | - | +3.38 | +3.51 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0045 | 0.517 | no | Rh2 | - | +0.11 | +0.03 |
| 185324357184 | 44 | 22... Bf3 | excellent | good | precision | good | 0.0208 | 0.498 | no | c5 | - | +0.19 | +0.31 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.516 | no | b3 | - | +0.26 | +0.40 |
| 185324357184 | 51 | 26. Bxc3 | excellent | good | precision | good | 0.0258 | 0.472 | no | bxc3 | - | -0.68 | -0.77 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0316 | 0.565 | no | d4 | - | +0.65 | +0.50 |
| 185436488062 | 8 | 4... a6 | inaccuracy | mistake | precision | mistake | 0.1066 | 0.463 | no | Nf6 | - | +1.74 | +1.99 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.644 | yes | Nxe5 | - | +1.74 | +1.97 |
| 185437323918 | 10 | 5... Kf8 | good | inaccuracy | precision | inaccuracy | 0.0526 | 0.439 | no | Ke7 | - | +1.39 | +1.52 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0377 | 0.267 | no | Nh7+ | - | -3.51 | -4.01 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0081 | 0.854 | no | g4 | - | -5.16 | -5.46 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0467 | 0.856 | no | g4 | - | -4.94 | -4.80 |
| 185437323918 | 23 | 12. Qg3 | mistake | good | precision | good | 0.0456 | 0.162 | no | Qe3 | - | -6.88 | -6.71 |
| 185437323918 | 33 | 17. bxc3 | good | best | precision | best | 0.0000 | 0.138 | yes | bxc3 | - | -6.58 | -6.37 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0000 | 0.872 | no | Rxh2+ | - | -6.58 | -6.48 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.855 | no | Qe2 | - | -5.96 | -5.97 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0447 | 0.804 | no | Qf4 | - | -3.59 | -3.86 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0994 | 0.238 | no | hxg3 | hxg3 | -5.85 | -6.02 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0153 | 0.831 | no | b6 | - | -4.41 | -4.93 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0375 | 0.717 | no | Bc2 | - | -2.41 | -2.79 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.855 | yes | Be4 | - | -5.61 | -6.12 |
| 185437323918 | 59 | 30. g5+ | good | excellent | precision | excellent | 0.0181 | 0.136 | no | Rg3 | - | -6.55 | -6.66 |
| 185437323918 | 65 | 33. Rg3+ | excellent | best | precision | best | 0.0000 | 0.154 | yes | Rg3+ | - | -5.91 | -6.04 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0074 | 0.861 | no | Kf5 | - | -5.11 | -5.84 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | best | precision | best | 0.0000 | 0.147 | yes | Kh2 | Kg2 | -6.13 | -6.15 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0455 | 0.865 | no | e4 | e4 | -5.01 | -5.01 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0000 | 0.862 | no | Bb4 | - | -6.12 | -6.39 |
| 185437323918 | 75 | 38. Ke4 | best | good | precision | good | 0.0285 | 0.127 | no | Ke2 | - | -6.12 | -6.33 |
| 185437323918 | 76 | 38... Rf4+ | best | good | precision | good | 0.0206 | 0.871 | no | Bc3 | - | -6.12 | -6.94 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0086 | 0.103 | no | d6 | - | -7.11 | -7.49 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0042 | 0.922 | no | Bb4 | - | -7.28 | -8.41 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.073 | yes | Kxc7 | - | -8.05 | -8.68 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0010 | 0.932 | no | Bg3+ | - | -8.05 | -9.10 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.060 | yes | d6 | - | -8.99 | -9.08 |
| 185437323918 | 94 | 47... Qb2+ | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qb2+ | - | -9.07 | -M19 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kc6 | Ka6 | -M17 | -M20 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -12.43 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.015 | no | Kd4 | - | -10.7 | -12.77 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0047 | 0.979 | no | Qb3+ | - | -10.7 | -12.88 |
| 185437323918 | 101 | 51. Ke6 | good | excellent | precision | excellent | 0.0045 | 0.020 | no | Kd4 | - | -M6 | -M13 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0107 | 0.514 | no | Nf3 | - | -0.01 | +0.04 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.497 | yes | h6 | - | -0.01 | -0.07 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.495 | yes | Bh4 | - | -0.01 | -0.02 |
| 185438707002 | 28 | 14... Nd4 | inaccuracy | mistake | precision | mistake | 0.1020 | 0.537 | no | Rhg8 | Rhg8 | +0.82 | +0.85 |
| 185438707002 | 30 | 15... Nxf3+ | good | inaccuracy | precision | inaccuracy | 0.0585 | 0.442 | no | Rhg8 | - | +1.28 | +1.55 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.613 | yes | c3 | - | +1.35 | +1.31 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0228 | 0.772 | no | Rd2 | - | +3.74 | +3.57 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.776 | yes | Rxd4 | - | +3.82 | +3.88 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0658 | 0.246 | no | Rg8 | - | +4.87 | +4.95 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0438 | 0.820 | no | Qf6 | Qf6 | +3.70 | +4.06 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.243 | yes | a6 | - | +3.78 | +3.80 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0006 | 0.762 | no | Qf3 | - | +3.78 | +3.79 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.781 | yes | Qxd8+ | - | +3.69 | +3.97 |
| 185438707002 | 63 | 32. b4 | good | excellent | precision | excellent | 0.0151 | 0.697 | no | Rd2 | - | +1.87 | +1.72 |
| 185438707002 | 65 | 33. Rd5 | excellent | good | precision | good | 0.0268 | 0.688 | no | Rd8 | - | +1.84 | +2.23 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.761 | yes | Qb2+ | - | -3.65 | -3.92 |
| 185438707002 | 75 | 38. Kg1 | best | excellent | precision | excellent | 0.0022 | 0.237 | no | f3 | - | -3.38 | -3.91 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0345 | 0.719 | no | Qc2 | - | -2.36 | -2.54 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0000 | 0.928 | no | Qd1 | - | -8.73 | -8.64 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.067 | yes | g4 | - | -8.80 | -8.28 |
| 185456088510 | 4 | 2... h6 | mistake | good | precision | good | 0.0446 | 0.395 | no | e6 | e6 | +1.09 | +0.97 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0146 | 0.650 | no | Nc3 | - | +0.96 | +0.84 |
| 185456088510 | 6 | 3... e6 | excellent | good | precision | good | 0.0363 | 0.369 | no | d6 | - | +1.01 | +0.99 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0071 | 0.334 | no | d5 | - | +1.01 | +1.15 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0377 | 0.343 | no | Ne7 | Bg7 | +1.25 | +1.29 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0030 | 0.631 | no | Qe2 | - | +0.81 | +0.75 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0045 | 0.383 | no | Bg7 | - | +0.81 | +0.98 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.614 | yes | Ng3 | - | +0.65 | +0.66 |
| 185456088510 | 20 | 10... Ng4 | excellent | good | precision | good | 0.0241 | 0.396 | no | h5 | - | +0.74 | +0.89 |
| 185456088510 | 21 | 11. Bd2 | excellent | best | precision | best | 0.0000 | 0.638 | yes | Bd2 | - | +0.70 | +0.77 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.680 | yes | h5 | - | +1.12 | +1.18 |
| 185456088510 | 29 | 15. e5 | inaccuracy | mistake | precision | mistake | 0.1179 | 0.839 | no | Qe2 | Qe2 | +1.58 | +1.49 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.748 | yes | exd6 | - | +1.55 | +1.32 |
| 185456088510 | 34 | 17... Qe7 | miss | mistake | precision | mistake | 0.1876 | 0.375 | no | Bxe4 | Bxe4 | +1.83 | +2.30 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0450 | 0.821 | no | Nh4 | - | +1.72 | +1.79 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0000 | 0.875 | no | a5 | - | +2.89 | +3.36 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.927 | yes | Nxe3 | - | -4.25 | -5.02 |
| 185468039834 | 11 | 6. Nd5 | best | good | precision | good | 0.0237 | 0.451 | no | Na4 | - | -0.94 | -1.10 |
| 185468039834 | 12 | 6... d6 | inaccuracy | mistake | precision | mistake | 0.1055 | 0.582 | no | h6 | h6 | 0.00 | +0.31 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0150 | 0.485 | no | Ne5 | - | +0.60 | +0.50 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0350 | 0.467 | no | Kf8 | - | +0.61 | +0.91 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0323 | 0.407 | no | dxe5 | dxe5 | +1.53 | +1.54 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.614 | yes | Qh5 | - | +1.48 | +1.58 |
| 185468039834 | 23 | 12. Qf3 | miss | blunder | precision | blunder | 0.2612 | 0.656 | no | Nxc7+ | Nxc7+ | -0.91 | -1.42 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.605 | yes | c6 | - | -0.83 | -1.10 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0168 | 0.418 | no | b4 | - | -1.28 | -1.39 |
| 185468039834 | 27 | 14. Bxe6 | best | excellent | precision | excellent | 0.0108 | 0.397 | no | b3 | - | -1.28 | -1.44 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.741 | yes | Rf8 | - | -3.36 | -3.55 |
| 185468039834 | 32 | 16... Rxf6 | excellent | best | precision | best | 0.0000 | 0.743 | yes | Rxf6 | - | -3.39 | -3.58 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0006 | 0.254 | no | Qg3 | - | -3.39 | -3.70 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0151 | 0.518 | no | b4 | - | +0.15 | +0.09 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.493 | yes | exd4 | - | +0.15 | +0.07 |
| 185468614210 | 11 | 6. cxd4 | book | excellent | precision | excellent | 0.0068 | 0.505 | no | e5 | - | 0.00 | -0.06 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.505 | yes | Bb4+ | - | 0.00 | +0.07 |
| 185468614210 | 13 | 7. Nc3 | book | good | precision | good | 0.0234 | 0.505 | no | Bd2 | - | -0.35 | -0.42 |
| 185468614210 | 26 | 13... Re8 | good | inaccuracy | precision | inaccuracy | 0.0520 | 0.542 | no | Nxd5 | - | +0.15 | +0.13 |
| 185468614210 | 28 | 14... Nxd5 | excellent | best | precision | best | 0.0000 | 0.484 | yes | Nxd5 | - | +0.25 | +0.18 |
| 185468614210 | 31 | 16. Qxd5 | best | excellent | precision | excellent | 0.0015 | 0.510 | no | Ng5+ | - | +0.25 | +0.24 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0405 | 0.482 | no | Kg8 | Kg8 | +1.21 | +0.78 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0420 | 0.559 | no | Qh5+ | Qh5+ | +0.18 | +0.20 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.485 | yes | Kg8 | - | +0.18 | +0.13 |
| 185468614210 | 38 | 19... Qf6 | good | excellent | precision | excellent | 0.0181 | 0.524 | no | b6 | - | -0.09 | -0.08 |
| 185468614210 | 40 | 20... Rxd6 | excellent | good | precision | good | 0.0257 | 0.516 | no | cxd6 | - | +0.14 | +0.09 |
| 185475865432 | 3 | 2. Nf3 | book | good | precision | good | 0.0208 | 0.569 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.448 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.548 | yes | Nc3 | - | +0.74 | +0.67 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.450 | yes | e6 | - | +0.74 | +0.68 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0105 | 0.458 | no | Bb4 | - | +0.55 | +0.70 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0071 | 0.389 | no | c3 | - | -1.49 | -1.60 |
| 185475865432 | 27 | 14. Ng3 | inaccuracy | good | precision | good | 0.0475 | 0.403 | no | Qxd8+ | Qxd8+ | -1.91 | -1.97 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0432 | 0.644 | no | Qxd1 | Qxd1 | -1.24 | -1.16 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0178 | 0.625 | no | Bd6 | - | -1.25 | -1.48 |
| 185475865432 | 37 | 19. Rad1 | excellent | best | precision | best | 0.0000 | 0.618 | yes | Rad1 | - | +1.50 | +1.68 |
| 185475865432 | 44 | 22... Rc8 | excellent | best | precision | best | 0.0000 | 0.386 | yes | Rc8 | - | +1.57 | +1.73 |
| 185475865432 | 48 | 24... Be2 | inaccuracy | mistake | precision | mistake | 0.1047 | 0.379 | no | Rb8 | Rb8 | +3.18 | +3.23 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0976 | 0.726 | no | Rxe6 | Rxe6 | +1.47 | +1.74 |
| 185475865432 | 51 | 26. a7 | excellent | best | precision | best | 0.0000 | 0.784 | yes | a7 | - | +3.79 | +3.91 |
| 185962590893 | 8 | 4... Qc7 | inaccuracy | mistake | precision | mistake | 0.1024 | 0.478 | no | Qxd1+ | Qxd1+ | +0.72 | +0.76 |
| 185962590893 | 14 | 7... Nd7 | best | excellent | precision | excellent | 0.0060 | 0.377 | no | Nf6 | - | +0.82 | +0.77 |
| 185962590893 | 16 | 8... Ngf6 | inaccuracy | good | precision | good | 0.0463 | 0.437 | no | b5 | b5 | +0.82 | +0.79 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.424 | yes | e5 | - | +0.67 | +0.59 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.432 | yes | Be7 | - | +0.55 | +0.48 |
| 185962590893 | 25 | 13. Nf5 | excellent | best | precision | best | 0.0000 | 0.579 | yes | Nf5 | - | +0.64 | +0.52 |
| 185962590893 | 27 | 14. Nxe7+ | miss | good | precision | good | 0.0465 | 0.752 | no | Bh6 | Bh6 | +1.01 | +1.44 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0388 | 0.303 | no | Nf8 | Ne8 | +1.62 | +1.61 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0805 | 0.736 | no | Rxd8+ | Rxd8+ | +0.96 | +1.01 |
| 185962590893 | 35 | 18. g5 | best | good | precision | good | 0.0263 | 0.656 | no | Rxd7 | - | +0.96 | +0.87 |
| 185962590893 | 40 | 20... Nfd7 | best | good | precision | good | 0.0252 | 0.380 | no | Ne8 | - | +0.96 | +1.12 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0167 | 0.401 | no | Nd7 | - | +0.86 | +0.74 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.634 | yes | Qe3 | Qf3 | +0.47 | +0.78 |
| 185962590893 | 52 | 26... Nd4 | mistake | good | precision | good | 0.0424 | 0.378 | no | Nf4 | Nf4 | +1.15 | +1.23 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2747 | 0.686 | no | f4 | - | -0.39 | -0.56 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | b4 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `mate_override` (6)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M7 |
| 185209623352 | 142 | 71... Kb5 | good | inaccuracy | mate_override | inaccuracy | 0.0184 | 0.018 | no | Ka7 | - | M8 | M11 |
| 185437323918 | 93 | 47. d7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0275 | 0.028 | no | Kb6 | - | -11.0 | -M21 |
| 185437323918 | 97 | 49. Kd5 | best | inaccuracy | mate_override | inaccuracy | 0.0230 | 0.023 | no | d8=Q | - | -M16 | -M18 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |
| 185438707002 | 91 | 46. Kh4 | best | inaccuracy | mate_override | inaccuracy | 0.0635 | 0.064 | no | g5 | - | -M6 | -M6 |

### `miss_detector` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (tactic) | miss_detector | mistake | 0.1731 | 0.678 | no | g4 | - | -0.01 | +0.12 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1848 | 0.864 | no | Rxf6+ | Rxf6+ | +2.74 | +2.69 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.5210 | 0.834 | no | Rxf6+ | - | -2.81 | -2.68 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | mistake | 0.1458 | 0.146 | no | Kd2 | - | -M1 | -M1 |
| 185456088510 | 33 | 17. Ne4 | mistake | miss (tactic) | miss_detector | mistake | 0.1271 | 0.752 | no | Qe2 | Qe2 | +0.65 | +0.80 |

### `blunder_softened` (4)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2058 | 0.902 | no | Qxg2 | Qxg2 | -0.96 | -1.06 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | blunder_softened | blunder | 0.2358 | 0.775 | no | Bxe6 | - | +0.61 | +0.53 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | blunder_softened | blunder | 0.2152 | 0.712 | no | Rhxe7 | Rhxe7 | -0.08 | -0.10 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2724 | 0.589 | no | Qxg3+ | Qxg3+ | +2.48 | +2.59 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0065 | 0.447 | no | Nf6 | - | +0.82 | +1.00 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0611 | 0.532 | no | d4 | Nxe5 | -0.62 | -0.38 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 51 | 26. Bxf5 | best | great | great_find_event | best | 0.0000 | 0.771 | yes | Bxf5 | - | +3.97 | +4.36 |
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.502 | yes | Bxe5 | - | +0.18 | -0.08 |

### `losing_material_hardened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185324357184 | 40 | 20... Be4 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0723 | 0.262 | no | Qxg3 | Qxg3 | +4.45 | +4.88 |
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | excellent | 0.0182 | 0.058 | no | Kd7 | - | -8.94 | -8.54 |

