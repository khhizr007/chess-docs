# Calibration report: sf16-off200

- Generated: 2026-10-18T08:18:33+00:00
- Commit: `52ae25250d63` + uncommitted backend changes (diff sha256 `d19c6b081992`)
- Engine: Stockfish 16; depth 18, multipv 3; config override: `{"rating_offset":200}`
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 70.8% (606/856) |
| Within one step | 88.8% (760/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.71 / 0.19 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 0.82 |
| Accuracy mean abs. difference | 2.68 (n=28, max 6.27) |
| Accuracy bias (ours - app) | +2.23 |
| Best move = app's suggestion | 80.3% (110/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | . | . | 1 | . | . | . | 3 |
| **great** | . | **5** | 21 | . | . | . | . | . | . | . | 26 |
| **best** | . | 2 | **267** | 38 | 7 | . | 2 | . | . | . | 316 |
| **excellent** | . | . | 29 | **74** | 17 | 1 | 2 | 4 | . | . | 127 |
| **good** | . | . | 5 | 25 | **63** | . | 8 | 1 | 1 | . | 103 |
| **book** | . | . | 10 | 5 | 3 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 5 | 3 | 16 | 1 | **58** | 7 | 2 | . | 92 |
| **mistake** | . | . | . | 1 | 1 | . | 9 | **28** | 3 | 2 | 44 |
| **miss** | . | . | . | . | 1 | . | 3 | 3 | **18** | 2 | 27 |
| **blunder** | . | . | . | . | . | . | 1 | 3 | 4 | **13** | 21 |
| **total** | 1 | 7 | 338 | 146 | 108 | 81 | 84 | 46 | 28 | 17 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 7 | 5 | 0.714 | 0.192 | 0.303 |
| best | 316 | 338 | 267 | 0.790 | 0.845 | 0.817 |
| excellent | 127 | 146 | 74 | 0.507 | 0.583 | 0.542 |
| good | 103 | 108 | 63 | 0.583 | 0.612 | 0.597 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 84 | 58 | 0.690 | 0.630 | 0.659 |
| mistake | 44 | 46 | 28 | 0.609 | 0.636 | 0.622 |
| miss | 27 | 28 | 18 | 0.643 | 0.667 | 0.655 |
| blunder | 21 | 17 | 13 | 0.765 | 0.619 | 0.684 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 80.0 | +6.3 |
| 1034847688 | black | 65.0 | 68.0 | +3.0 |
| 1041474766 | white | 98.0 | 97.1 | -0.9 |
| 1041474766 | black | 83.8 | 84.4 | +0.6 |
| 184759554082 | white | 81.2 | 85.6 | +4.4 |
| 184759554082 | black | 87.7 | 91.1 | +3.4 |
| 185209623352 | white | 72.7 | 73.7 | +1.0 |
| 185209623352 | black | 72.6 | 70.8 | -1.8 |
| 185324357184 | white | 73.0 | 77.5 | +4.5 |
| 185324357184 | black | 62.4 | 66.4 | +4.0 |
| 185436488062 | white | 98.6 | 98.3 | -0.3 |
| 185436488062 | black | 38.5 | 44.8 | +6.3 |
| 185437323918 | white | 69.5 | 69.8 | +0.3 |
| 185437323918 | black | 75.7 | 74.6 | -1.1 |
| 185438343298 | white | 46.9 | 46.9 | -0.0 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 75.8 | -2.0 |
| 185438707002 | black | 83.0 | 82.8 | -0.2 |
| 185456088510 | white | 78.4 | 81.4 | +3.0 |
| 185456088510 | black | 82.2 | 84.0 | +1.8 |
| 185468039834 | white | 80.0 | 80.8 | +0.8 |
| 185468039834 | black | 87.5 | 88.7 | +1.2 |
| 185468614210 | white | 70.8 | 76.1 | +5.3 |
| 185468614210 | black | 77.1 | 82.1 | +5.0 |
| 185475865432 | white | 78.1 | 84.4 | +6.3 |
| 185475865432 | black | 66.1 | 72.0 | +5.9 |
| 185962590893 | white | 90.8 | 93.6 | +2.8 |
| 185962590893 | black | 90.9 | 93.7 | +2.8 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 63.3% | 83.7% | reviewed | 0.5 |
| 1041474766 | 25 | 25 | 76.0% | 80.0% | reviewed | 0.5 |
| 184759554082 | 62 | 62 | 80.6% | 90.3% | reviewed | 0.5 |
| 185209623352 | 155 | 155 | 61.9% | 86.5% | reviewed | 0.5 |
| 185324357184 | 55 | 55 | 87.3% | 96.4% | reviewed | 0.5 |
| 185436488062 | 13 | 13 | 84.6% | 92.3% | reviewed | 0.5 |
| 185437323918 | 108 | 103 | 66.0% | 87.4% | reviewed | 0.5 |
| 185438343298 | 20 | 20 | 95.0% | 95.0% | reviewed | 0.5 |
| 185438707002 | 95 | 91 | 67.0% | 86.8% | reviewed | 0.5 |
| 185456088510 | 60 | 60 | 66.7% | 88.3% | reviewed | 0.5 |
| 185468039834 | 38 | 38 | 65.8% | 94.7% | reviewed | 0.5 |
| 185468614210 | 54 | 54 | 75.9% | 85.2% | reviewed | 0.5 |
| 185475865432 | 53 | 53 | 69.8% | 92.5% | reviewed | 0.5 |
| 185962590893 | 78 | 78 | 76.9% | 92.3% | reviewed | 0.5 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label is one of the collector's candidates for 9 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | best | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | best | precision |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (250)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 222 | best -> excellent x38, excellent -> best x29, good -> excellent x25, great -> best x21, excellent -> good x16, inaccuracy -> good x15 |
| `miss_detector` | 9 | blunder -> miss x4, mistake -> miss x3, inaccuracy -> miss x2 |
| `mate_override` | 6 | best -> good x3, inaccuracy -> good x1, good -> miss x1, excellent -> good x1 |
| `losing_material_hardened` | 5 | excellent -> mistake x4, inaccuracy -> mistake x1 |
| `blunder_softened` | 4 | blunder -> mistake x2, inaccuracy -> mistake x1, miss -> mistake x1 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `great_find_event` | 2 | best -> great x2 |

### `precision` (222)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 7 | 4. Nbd2 | good | excellent | precision | excellent | 0.0183 | 0.531 | no | c4 | - | +0.13 | +0.12 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0097 | 0.492 | no | Be2 | - | -0.10 | -0.19 |
| 1034847688 | 16 | 8... Nb8 | best | excellent | precision | excellent | 0.0032 | 0.473 | no | Na5 | - | +0.28 | +0.27 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0237 | 0.529 | no | h3 | - | +0.12 | +0.05 |
| 1034847688 | 22 | 11... a5 | mistake | inaccuracy | precision | inaccuracy | 0.0996 | 0.474 | no | Nbd7 | Nbd7 | +1.29 | +1.19 |
| 1034847688 | 23 | 12. Ng5 | miss | mistake | precision | mistake | 0.1061 | 0.625 | no | cxb5 | cxb5 | +0.44 | +0.18 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.490 | yes | h6 | - | +0.90 | +0.19 |
| 1034847688 | 27 | 14. Ndf3 | mistake | inaccuracy | precision | inaccuracy | 0.0900 | 0.520 | no | cxb5 | h5 | -0.60 | -0.65 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0857 | 0.570 | no | a4 | Qd7 | +0.53 | +0.15 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.547 | yes | Nxf3 | - | -0.10 | -0.21 |
| 1034847688 | 42 | 21... e5 | best | good | precision | good | 0.0258 | 0.500 | no | f6 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.00 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0376 | 0.500 | no | fxe6 | - | +0.46 | +0.61 |
| 1034847688 | 45 | 23. exf7+ | good | excellent | precision | excellent | 0.0096 | 0.565 | no | Qc3 | - | +0.09 | +0.04 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0386 | 0.578 | no | d4 | - | +0.37 | +0.38 |
| 1041474766 | 8 | 4... Nf6 | book | best | precision | best | 0.0000 | 0.461 | yes | Nf6 | - | +0.38 | +0.64 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.566 | yes | Bg2 | - | +0.34 | +0.28 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0184 | 0.471 | no | e5 | - | +0.59 | +0.46 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0349 | 0.547 | no | Nf3 | - | +0.17 | +0.12 |
| 1041474766 | 12 | 6... Nbd7 | excellent | good | precision | good | 0.0267 | 0.488 | no | e5 | - | +0.37 | +0.46 |
| 184759554082 | 6 | 3... a6 | book | excellent | precision | excellent | 0.0080 | 0.518 | no | d5 | - | +0.08 | +0.08 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0191 | 0.487 | no | Nc3 | - | -0.25 | -0.25 |
| 184759554082 | 14 | 7... O-O | excellent | best | precision | best | 0.0000 | 0.505 | yes | O-O | - | +0.03 | +0.04 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.524 | yes | hxg6 | - | -0.13 | -0.08 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0545 | 0.684 | no | d5 | d5 | -0.52 | -0.35 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.642 | yes | d5 | - | -0.52 | -0.99 |
| 184759554082 | 23 | 12. Nxd5 | blunder | inaccuracy | precision | inaccuracy | 0.0822 | 0.347 | no | cxd5 | cxd5 | -1.98 | -2.08 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.777 | yes | Qxg5 | - | -1.98 | -1.79 |
| 184759554082 | 36 | 18... Qf6 | best | excellent | precision | excellent | 0.0014 | 0.661 | no | Re5 | - | -1.01 | -0.91 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.722 | yes | Re6 | - | -1.31 | -1.42 |
| 184759554082 | 59 | 30. Rxh8 | inaccuracy | good | precision | good | 0.0455 | 0.309 | no | Rhf1 | Rhd1 | -1.74 | -1.61 |
| 185209623352 | 7 | 4. d4 | best | excellent | precision | excellent | 0.0007 | 0.499 | no | Nf3 | - | -0.08 | +0.00 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.499 | yes | Nf3 | - | -0.16 | -0.07 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.856 | yes | Nxe4 | - | +5.09 | +6.24 |
| 185209623352 | 20 | 10... dxe4 | mistake | excellent | precision | excellent | 0.0076 | 0.149 | no | Bxe4 | - | +6.16 | +6.46 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0797 | 0.859 | no | Nxc6 | Nxc6 | +4.00 | +4.30 |
| 185209623352 | 23 | 12. Qxd4 | best | good | precision | good | 0.0215 | 0.798 | no | Bxc6 | - | +4.04 | +4.12 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0409 | 0.254 | no | e5 | - | +4.18 | +4.68 |
| 185209623352 | 29 | 15. Nf7 | excellent | best | precision | best | 0.0000 | 0.714 | yes | Nf7 | - | +2.76 | +3.10 |
| 185209623352 | 32 | 16... Ne6 | inaccuracy | mistake | precision | mistake | 0.1099 | 0.296 | no | Kc7 | Nxg2 | +4.22 | +5.28 |
| 185209623352 | 34 | 17... Kc7 | good | excellent | precision | excellent | 0.0071 | 0.186 | no | Kb8 | - | +4.76 | +4.90 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.698 | yes | Rc5+ | - | +3.32 | +3.25 |
| 185209623352 | 46 | 23... Nd3+ | excellent | good | precision | good | 0.0211 | 0.429 | no | Bxe5 | - | +0.92 | +1.17 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.581 | yes | Nxd3 | Rxd3 | -0.61 | +1.25 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0084 | 0.234 | no | Ka6 | - | +3.97 | +4.01 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0151 | 0.771 | no | Rd5 | - | +3.97 | +4.07 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.792 | no | Kb1 | - | +4.39 | +4.78 |
| 185209623352 | 56 | 28... d2 | excellent | best | precision | best | 0.0000 | 0.208 | yes | d2 | - | +4.65 | +4.86 |
| 185209623352 | 57 | 29. Rf7 | good | best | precision | best | 0.0000 | 0.795 | yes | Rf7 | - | +4.14 | +5.03 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0099 | 0.825 | no | Kc2 | - | +4.64 | +5.30 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0331 | 0.229 | no | Kf5 | - | +4.38 | +5.06 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.804 | yes | Kc2 | - | +4.38 | +4.80 |
| 185209623352 | 70 | 35... Rxc4 | excellent | best | precision | best | 0.0000 | 0.196 | yes | Rxc4 | - | +4.77 | +5.02 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0297 | 0.708 | no | Kd3 | - | +2.98 | +2.97 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.660 | yes | Kc1 | - | +2.15 | +2.04 |
| 185209623352 | 80 | 40... a5 | mistake | blunder | precision | blunder | 0.2134 | 0.361 | no | Rb4 | - | +5.81 | +6.27 |
| 185209623352 | 81 | 41. Re1+ | inaccuracy | good | precision | good | 0.0333 | 0.852 | no | Rxf6+ | Rxf6+ | +4.65 | +5.44 |
| 185209623352 | 82 | 41... Kf7 | mistake | good | precision | good | 0.0465 | 0.179 | no | Kd7 | - | +6.01 | +6.71 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1739 | 0.680 | no | Rhxe7 | Rhxe7 | -0.08 | +0.00 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.771 | yes | Rf1+ | - | +3.73 | +4.62 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.831 | yes | Kxb2 | - | +5.17 | +5.70 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0111 | 0.169 | no | Bxf4 | - | +5.65 | +6.25 |
| 185209623352 | 97 | 49. Kc2 | best | excellent | precision | excellent | 0.0077 | 0.864 | no | Kb1 | - | +5.89 | +6.50 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0007 | 0.140 | no | b5 | - | +6.38 | +6.56 |
| 185209623352 | 99 | 50. Rh7 | best | excellent | precision | excellent | 0.0034 | 0.862 | no | Rah4 | - | +6.38 | +6.61 |
| 185209623352 | 100 | 50... b5 | best | excellent | precision | excellent | 0.0033 | 0.136 | no | b6 | - | +6.38 | +6.71 |
| 185209623352 | 101 | 51. Rb4 | excellent | best | precision | best | 0.0000 | 0.867 | no | Ra6 | - | +6.27 | +6.71 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0003 | 0.864 | no | Rc7 | - | +6.33 | +6.59 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0071 | 0.137 | no | Bg5 | - | +6.33 | +6.79 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0157 | 0.887 | no | Rb6 | - | +6.59 | +6.85 |
| 185209623352 | 108 | 54... Kh5 | excellent | good | precision | good | 0.0462 | 0.129 | no | e4 | - | +6.70 | +8.63 |
| 185209623352 | 110 | 55... Kg6 | excellent | best | precision | best | 0.0000 | 0.099 | yes | Kg6 | - | +6.54 | +35.57 |
| 185209623352 | 111 | 56. Rbxe5 | best | inaccuracy | precision | inaccuracy | 0.0877 | 1.000 | no | Rb6 | - | +6.54 | +8.38 |
| 185209623352 | 114 | 57... Kf6 | excellent | inaccuracy | precision | inaccuracy | 0.0850 | 0.085 | no | Kf7 | - | +7.19 | +34.41 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | no | Kf7 | Ke7 | +10.6 | +34.57 |
| 185209623352 | 117 | 59. h5 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Kb1 | - | +8.42 | +34.58 |
| 185209623352 | 120 | 60... Kf6 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke6 | - | M9 | M9 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg5 | - | M3 | M3 |
| 185209623352 | 133 | 67. Re8+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kd3 | - | M2 | M2 |
| 185209623352 | 141 | 71. g4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Rc3 | - | +10.4 | +39.51 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb6 | - | M5 | M5 |
| 185209623352 | 152 | 76... Kb5 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb7 | - | M3 | M3 |
| 185324357184 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0042 | 0.572 | no | O-O | - | -1.29 | -0.94 |
| 185324357184 | 19 | 10. Ne2 | good | excellent | precision | excellent | 0.0000 | 0.441 | no | Qe3 | - | -1.32 | -0.67 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0509 | 0.547 | no | Na6 | - | +0.29 | +0.10 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.507 | yes | Qg1 | - | +0.29 | +0.24 |
| 185324357184 | 49 | 25. c3 | good | inaccuracy | precision | inaccuracy | 0.0524 | 0.527 | no | b3 | - | -0.53 | -0.36 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0211 | 0.557 | no | d4 | - | +0.65 | +0.51 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.619 | yes | Nxe5 | - | +1.74 | +1.81 |
| 185437323918 | 20 | 10... d6 | excellent | best | precision | best | 0.0000 | 0.839 | yes | d6 | - | -4.94 | -5.75 |
| 185437323918 | 31 | 16. Nd2 | excellent | best | precision | best | 0.0000 | 0.106 | yes | Nd2 | - | -6.16 | -7.67 |
| 185437323918 | 33 | 17. bxc3 | good | excellent | precision | excellent | 0.0164 | 0.112 | no | g4 | - | -6.58 | -7.79 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0132 | 0.904 | no | Kg7 | - | -6.58 | -7.29 |
| 185437323918 | 37 | 19. Nf3 | best | excellent | precision | excellent | 0.0006 | 0.060 | no | c4 | - | -5.96 | -9.16 |
| 185437323918 | 40 | 20... g4 | inaccuracy | mistake | precision | mistake | 0.1319 | 0.939 | no | Rh5 | - | -4.32 | -4.98 |
| 185437323918 | 42 | 21... gxf3 | brilliant | inaccuracy | precision | inaccuracy | 0.0829 | 0.803 | no | Qf4 | - | -3.59 | -3.83 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0054 | 0.809 | no | e4 | - | -4.41 | -4.90 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0325 | 0.719 | no | Bc2 | - | -2.41 | -2.31 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.834 | yes | Be4 | - | -5.61 | -5.84 |
| 185437323918 | 64 | 32... Kxg5 | good | excellent | precision | excellent | 0.0141 | 0.864 | no | e4 | - | -5.64 | -6.03 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0144 | 0.835 | no | Kh5 | - | -5.11 | -5.28 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | excellent | precision | excellent | 0.0091 | 0.179 | no | Kg2 | Kg2 | -6.13 | -5.82 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | excellent | precision | excellent | 0.0126 | 0.842 | no | e4 | e4 | -5.01 | -5.50 |
| 185437323918 | 69 | 35. Rg4+ | good | excellent | precision | excellent | 0.0122 | 0.170 | no | Rxg6 | - | -5.79 | -5.81 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0011 | 0.852 | no | Bb4 | - | -6.12 | -6.03 |
| 185437323918 | 77 | 39. Kxe5 | best | excellent | precision | excellent | 0.0044 | 0.126 | no | Rxf4 | - | -6.12 | -6.54 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0121 | 0.125 | no | c5 | - | -7.11 | -7.16 |
| 185437323918 | 82 | 41... a5 | best | excellent | precision | excellent | 0.0059 | 0.887 | no | Bg3 | - | -7.11 | -7.27 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0000 | 0.871 | no | Bg3 | - | -7.28 | -6.64 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.129 | yes | Kxc7 | - | -8.05 | -7.66 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0102 | 0.901 | no | Bb4 | - | -8.05 | -34.94 |
| 185437323918 | 88 | 44... Bg3 | excellent | best | precision | best | 0.0000 | 1.000 | no | a2 | - | -8.13 | -35.79 |
| 185437323918 | 93 | 47. d7 | excellent | best | precision | best | 0.0000 | 0.000 | yes | d7 | - | -11.0 | -M18 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | no | Ka6 | Ka6 | -M17 | -M23 |
| 185437323918 | 98 | 49... Qb7+ | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qg8+ | - | -8.99 | -M17 |
| 185437323918 | 105 | 53. Ke7 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Ke7 | - | -M3 | -M5 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0124 | 0.509 | no | Nf3 | - | -0.01 | -0.05 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.504 | yes | h6 | - | -0.01 | +0.00 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.500 | yes | Bh4 | - | -0.01 | +0.01 |
| 185438707002 | 12 | 6... g5 | good | excellent | precision | excellent | 0.0146 | 0.499 | no | a5 | - | +0.33 | +0.21 |
| 185438707002 | 14 | 7... h5 | good | inaccuracy | precision | inaccuracy | 0.0566 | 0.495 | no | d6 | - | +0.95 | +0.85 |
| 185438707002 | 28 | 14... Nd4 | inaccuracy | mistake | precision | mistake | 0.1167 | 0.533 | no | Rdg8 | Rhg8 | +0.82 | +1.16 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.599 | yes | c3 | - | +1.35 | +1.52 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0858 | 0.391 | no | Bb6 | - | +2.65 | +2.59 |
| 185438707002 | 41 | 21. O-O-O | excellent | good | precision | good | 0.0292 | 0.793 | no | O-O | - | +3.58 | +3.91 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0201 | 0.781 | no | Qe2 | - | +3.74 | +3.96 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.779 | yes | Rxd4 | - | +3.82 | +4.16 |
| 185438707002 | 46 | 23... e5 | best | excellent | precision | excellent | 0.0005 | 0.229 | no | Kb8 | - | +3.82 | +4.07 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0155 | 0.766 | no | Rd2 | - | +3.82 | +3.66 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0764 | 0.256 | no | Rf8 | - | +4.87 | +5.21 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0277 | 0.821 | no | Rhd1 | Qf6 | +3.70 | +4.60 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.257 | yes | a6 | - | +3.78 | +4.09 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0068 | 0.768 | no | Qf3 | - | +3.78 | +3.84 |
| 185438707002 | 55 | 28. Rd8+ | miss | inaccuracy | precision | inaccuracy | 0.0993 | 0.856 | no | Qxf8+ | Qxf8+ | +3.74 | +4.06 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.774 | yes | Qxd8+ | - | +3.69 | +4.00 |
| 185438707002 | 61 | 31. Qg3 | inaccuracy | mistake | precision | mistake | 0.1001 | 0.772 | no | b4 | a4 | +2.58 | +2.45 |
| 185438707002 | 63 | 32. b4 | good | best | precision | best | 0.0000 | 0.693 | yes | b4 | - | +1.87 | +2.64 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.762 | yes | Qb2+ | - | -3.65 | -2.85 |
| 185438707002 | 69 | 35. Kd1 | best | inaccuracy | precision | inaccuracy | 0.0580 | 0.303 | no | Kd3 | - | -3.65 | -3.42 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0400 | 0.717 | no | Qe2 | - | -2.36 | -2.54 |
| 185438707002 | 81 | 41. h5 | blunder | mistake | precision | mistake | 0.1571 | 0.347 | no | Qg4 | - | -7.11 | -4.96 |
| 185438707002 | 85 | 43. fxg3 | good | mistake | precision | mistake | 0.1667 | 0.167 | no | Kxg3 | - | -8.73 | -M10 |
| 185438707002 | 89 | 45. g3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | h6 | g5 | -M7 | -M7 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0588 | 0.415 | no | e6 | e6 | +1.09 | +0.93 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0177 | 0.644 | no | Nf3 | - | +0.96 | +0.81 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0087 | 0.358 | no | c5 | - | +1.01 | +0.93 |
| 185456088510 | 10 | 5... g6 | good | best | precision | best | 0.0000 | 0.358 | yes | g6 | - | +1.14 | +1.02 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0409 | 0.377 | no | Nc6 | Bg7 | +1.25 | +1.07 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0138 | 0.415 | no | Bg7 | - | +0.81 | +0.69 |
| 185456088510 | 17 | 9. Ne2 | good | excellent | precision | excellent | 0.0107 | 0.608 | no | d5 | - | +0.65 | +0.62 |
| 185456088510 | 18 | 9... Ngf6 | best | excellent | precision | excellent | 0.0046 | 0.403 | no | Bg7 | - | +0.65 | +0.75 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.617 | yes | Ng3 | - | +0.65 | +0.73 |
| 185456088510 | 22 | 11... Bg7 | inaccuracy | good | precision | good | 0.0341 | 0.386 | no | h5 | h5 | +1.10 | +0.98 |
| 185456088510 | 23 | 12. c3 | inaccuracy | good | precision | good | 0.0295 | 0.651 | no | h5 | h5 | +0.70 | +0.81 |
| 185456088510 | 24 | 12... c5 | inaccuracy | good | precision | good | 0.0350 | 0.374 | no | h5 | h5 | +1.12 | +1.05 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.661 | yes | h5 | - | +1.12 | +1.05 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.752 | yes | exd6 | - | +1.55 | +1.71 |
| 185456088510 | 34 | 17... Qe7 | miss | blunder | precision | blunder | 0.2337 | 0.419 | no | Bxe4 | Bxe4 | +1.83 | +2.32 |
| 185456088510 | 37 | 19. dxc5 | excellent | inaccuracy | precision | inaccuracy | 0.0782 | 0.826 | no | Nh4 | - | +1.72 | +1.55 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0895 | 0.179 | no | Rd6 | - | +2.89 | +3.64 |
| 185456088510 | 47 | 24. b4 | best | good | precision | good | 0.0237 | 0.910 | no | a5 | - | +2.89 | +3.04 |
| 185456088510 | 48 | 24... Qc7 | excellent | best | precision | best | 0.0000 | 0.126 | yes | Qc7 | - | +3.01 | +3.34 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.946 | yes | Nxe3 | - | -4.25 | -4.87 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0092 | 0.443 | no | Na4 | - | -0.94 | -0.88 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0385 | 0.475 | no | Rg8 | - | +0.61 | +0.89 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0223 | 0.425 | no | dxe5 | dxe5 | +1.53 | +1.55 |
| 185468039834 | 22 | 11... Be6 | good | inaccuracy | precision | inaccuracy | 0.0709 | 0.424 | no | c6 | - | +1.84 | +2.04 |
| 185468039834 | 23 | 12. Qf3 | miss | blunder | precision | blunder | 0.2330 | 0.643 | no | Nxc7+ | Nxc7+ | -0.91 | -1.27 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.590 | yes | c6 | - | -0.83 | -1.16 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0084 | 0.417 | no | b4 | - | -1.28 | -1.34 |
| 185468039834 | 27 | 14. Bxe6 | best | excellent | precision | excellent | 0.0111 | 0.410 | no | Bb3 | - | -1.28 | -1.25 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.754 | yes | Rf8 | - | -3.36 | -3.80 |
| 185468039834 | 31 | 16. b4 | excellent | good | precision | good | 0.0441 | 0.251 | no | Qb3 | - | -3.61 | -4.53 |
| 185468039834 | 32 | 16... Rxf6 | excellent | best | precision | best | 0.0000 | 0.786 | yes | Rxf6 | - | -3.39 | -4.39 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0112 | 0.220 | no | Qg3 | - | -3.39 | -4.62 |
| 185468039834 | 36 | 18... a5 | good | inaccuracy | precision | inaccuracy | 0.0686 | 0.805 | no | a6 | - | -2.75 | -3.58 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0166 | 0.517 | no | d3 | - | +0.15 | +0.00 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.500 | yes | exd4 | - | +0.15 | +0.00 |
| 185468614210 | 11 | 6. cxd4 | book | best | precision | best | 0.0000 | 0.500 | yes | cxd4 | - | 0.00 | +0.00 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.500 | yes | Bb4+ | - | 0.00 | +0.00 |
| 185468614210 | 13 | 7. Nc3 | book | good | precision | good | 0.0431 | 0.500 | no | Bd2 | - | -0.35 | -0.57 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0434 | 0.468 | no | Nxe4 | Nxe4 | +1.21 | +1.18 |
| 185468614210 | 18 | 9... Ne7 | excellent | good | precision | good | 0.0277 | 0.415 | no | Na5 | - | +1.36 | +1.42 |
| 185468614210 | 26 | 13... Re8 | good | inaccuracy | precision | inaccuracy | 0.0568 | 0.545 | no | Nxd5 | - | +0.15 | +0.17 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0359 | 0.486 | no | Kg8 | Kg8 | +1.21 | +0.69 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0344 | 0.550 | no | Qh5+ | Qh5+ | +0.18 | +0.20 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.486 | yes | Kg8 | - | +0.18 | +0.19 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0064 | 0.562 | no | d4 | - | +0.74 | +0.63 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.455 | yes | Bb7 | - | +0.74 | +0.70 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.550 | yes | Nc3 | - | +0.74 | +0.61 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.456 | yes | e6 | - | +0.74 | +0.66 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0078 | 0.574 | no | Ng3 | - | +0.82 | +0.92 |
| 185475865432 | 20 | 10... Nf6 | best | excellent | precision | excellent | 0.0042 | 0.434 | no | Na6 | - | +0.82 | +0.86 |
| 185475865432 | 23 | 12. Bf4 | inaccuracy | good | precision | good | 0.0432 | 0.460 | no | Qxd8+ | - | -1.49 | -1.17 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0104 | 0.415 | no | Re1 | - | -1.49 | -1.51 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0371 | 0.642 | no | Qxd1 | Qxd1 | -1.24 | -1.45 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0048 | 0.397 | no | hxg3 | - | -1.52 | -1.51 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0179 | 0.613 | no | Bd6 | - | -1.25 | -1.42 |
| 185475865432 | 42 | 21... Bxb2 | best | excellent | precision | excellent | 0.0014 | 0.389 | no | Rc8 | - | +1.50 | +1.42 |
| 185475865432 | 44 | 22... Rc8 | excellent | best | precision | best | 0.0000 | 0.390 | yes | Rc8 | - | +1.57 | +1.65 |
| 185475865432 | 48 | 24... Be2 | inaccuracy | mistake | precision | mistake | 0.1157 | 0.389 | no | Rb8 | Rb8 | +3.18 | +3.40 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0967 | 0.727 | no | Rxe6 | Rxe6 | +1.47 | +1.85 |
| 185475865432 | 51 | 26. a7 | excellent | best | precision | best | 0.0000 | 0.785 | yes | a7 | - | +3.79 | +4.57 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0632 | 0.619 | no | Qd4 | - | +0.50 | +0.35 |
| 185962590893 | 12 | 6... Bxf3 | excellent | best | precision | best | 0.0000 | 0.406 | yes | Bxf3 | - | +0.82 | +0.75 |
| 185962590893 | 15 | 8. Nc4 | inaccuracy | good | precision | good | 0.0433 | 0.605 | no | b3 | - | +0.40 | +0.39 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.424 | yes | e5 | - | +0.67 | +0.55 |
| 185962590893 | 19 | 10. Bd2 | good | best | precision | best | 0.0000 | 0.587 | yes | Bd2 | - | +0.50 | +0.44 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.430 | yes | Be7 | - | +0.55 | +0.47 |
| 185962590893 | 21 | 11. O-O-O | excellent | best | precision | best | 0.0000 | 0.574 | yes | O-O-O | - | +0.44 | +0.35 |
| 185962590893 | 27 | 14. Nxe7+ | miss | good | precision | good | 0.0293 | 0.716 | no | Bh6 | Bh6 | +1.01 | +1.14 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0982 | 0.735 | no | Rxd8+ | Rxd8+ | +0.96 | +0.88 |
| 185962590893 | 43 | 22. Bd2 | good | excellent | precision | excellent | 0.0117 | 0.645 | no | Qh1 | - | +0.86 | +0.64 |
| 185962590893 | 44 | 22... Ne6 | excellent | best | precision | best | 0.0000 | 0.399 | yes | Ne6 | - | +0.92 | +0.77 |
| 185962590893 | 48 | 24... Nd7 | best | good | precision | good | 0.0241 | 0.398 | no | h6 | - | +0.86 | +0.80 |
| 185962590893 | 49 | 25. Bg4 | excellent | good | precision | good | 0.0458 | 0.625 | no | Qc3 | - | +0.82 | +0.50 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.584 | yes | Qe3 | Qf3 | +0.47 | +0.62 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0680 | 0.403 | no | Nf4 | Nf4 | +1.15 | +1.10 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2395 | 0.668 | no | f4 | - | -0.39 | -0.45 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | -0.07 |
| 185962590893 | 78 | 39... Qd1+ | best | excellent | precision | excellent | 0.0111 | 0.511 | no | g6 | - | 0.00 | +0.00 |

### `miss_detector` (9)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1520 | 0.655 | no | g4 | - | -0.01 | +0.07 |
| 1034847688 | 37 | 19. Rh4 | mistake | miss (opportunity) | miss_detector | mistake | 0.1049 | 0.627 | no | Rh6 | Rh6 | -0.10 | -0.44 |
| 184759554082 | 27 | 14. cxd5 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1468 | 0.242 | no | Bb2 | Bb2 | -3.24 | -3.49 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1839 | 0.867 | no | Rxf6+ | Rxf6+ | +2.74 | +2.95 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.5232 | 0.846 | no | Rxf6+ | - | -2.81 | -2.65 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2792 | 0.779 | no | Kg7 | - | -0.17 | +0.00 |
| 185437323918 | 54 | 27... a6 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1094 | 0.803 | no | e4 | e4 | -2.64 | -2.83 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (opportunity) | miss_detector | mistake | 0.1756 | 0.176 | no | Kd2 | - | -M1 | -M1 |
| 185468614210 | 7 | 4. c3 | mistake | miss (tactic) | miss_detector | mistake | 0.1471 | 0.595 | no | Nxe5 | Nxe5 | -0.88 | -0.73 |

### `mate_override` (6)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 118 | 59... Kf7 | inaccuracy | good | mate_override | good | 0.0001 | 0.000 | no | Kf6 | Kf6 | M10 | +46.51 |
| 185209623352 | 123 | 62. Rg8 | best | good | mate_override | good | 0.0000 | 1.000 | no | Rh4 | - | M7 | M9 |
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M4 |
| 185437323918 | 94 | 47... Qb2+ | excellent | good | mate_override | good | 0.0000 | 1.000 | no | Qa5 | - | -9.07 | -45.40 |
| 185437323918 | 96 | 48... Qb8 | best | good | mate_override | good | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -M20 |
| 185438707002 | 86 | 43... Qf7 | best | good | mate_override | good | 0.0000 | 1.000 | no | e4 | - | -8.73 | -M16 |

### `losing_material_hardened` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 22 | 11... Qxd4 | excellent | mistake | losing_material_hardened | good | 0.0347 | 0.231 | no | Qd5 | - | +4.04 | +4.92 |
| 185324357184 | 40 | 20... Be4 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0792 | 0.274 | no | Qxg3 | Qxg3 | +4.45 | +5.01 |
| 185437323918 | 61 | 31. Rf1 | excellent | mistake | losing_material_hardened | good | 0.0494 | 0.142 | no | Rg3 | - | -7.00 | -7.91 |
| 185437323918 | 87 | 44. d6 | excellent | mistake | losing_material_hardened | excellent | 0.0000 | 0.000 | no | Kd6 | - | -8.99 | -36.40 |
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | excellent | 0.0000 | 0.000 | no | Kxb7 | - | -8.94 | -38.45 |

### `blunder_softened` (4)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 36 | 18... Ne5 | inaccuracy | mistake | blunder_softened | blunder | 0.2717 | 0.669 | no | a4 | a4 | +0.86 | +1.21 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | blunder_softened | blunder | 0.2261 | 0.769 | no | Bxe6 | - | +0.61 | +0.62 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2355 | 0.570 | no | Qxg3+ | Qxg3+ | +2.48 | +2.43 |
| 185438707002 | 67 | 34. Kc2 | blunder | mistake | blunder_softened | blunder | 0.4543 | 0.713 | no | Kd1 | - | -3.65 | -3.98 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0035 | 0.452 | no | Nf6 | - | +0.82 | +0.82 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0597 | 0.534 | no | Nxe5 | Nxe5 | -0.62 | -0.36 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.525 | yes | Bxe5 | - | +0.18 | +0.49 |
| 185438707002 | 50 | 25... Kb8 | best | great | great_find_event | best | 0.0000 | 0.207 | yes | Kb8 | - | +3.70 | +4.53 |

