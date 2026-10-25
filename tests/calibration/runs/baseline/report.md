# Calibration report: baseline

- Generated: 2026-10-17T18:56:07+00:00
- Commit: `9ddf4a553322` (backend clean)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 64.6% (553/856) |
| Within one step | 84.1% (720/856) |
| Brilliant precision / recall | 0.03 / 0.67 |
| Great precision / recall | 0.75 / 0.12 |
| Brilliant per 100 moves (app / ours) | 0.35 / 7.01 |
| Great per 100 moves (app / ours) | 3.04 / 0.47 |
| Accuracy mean abs. difference | 3.24 (n=28, max 7.57) |
| Accuracy bias (ours - app) | +2.73 |
| Best move = app's suggestion | 84.7% (116/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **2** | . | . | . | 1 | . | . | . | . | . | 3 |
| **great** | 3 | **3** | 20 | . | . | . | . | . | . | . | 26 |
| **best** | 31 | 1 | **243** | 39 | 1 | . | 1 | . | . | . | 316 |
| **excellent** | 14 | . | 23 | **61** | 24 | 1 | 3 | 1 | . | . | 127 |
| **good** | 7 | . | 4 | 32 | **50** | . | 8 | 1 | 1 | . | 103 |
| **book** | 2 | . | 8 | 4 | 4 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 4 | 4 | 22 | 1 | **58** | 3 | . | . | 92 |
| **mistake** | 1 | . | . | . | 3 | . | 11 | **24** | 3 | 2 | 44 |
| **miss** | . | . | . | . | . | . | 2 | 4 | **21** | . | 27 |
| **blunder** | . | . | . | . | . | . | . | 3 | 6 | **12** | 21 |
| **total** | 60 | 4 | 302 | 140 | 105 | 81 | 83 | 36 | 31 | 14 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 60 | 2 | 0.033 | 0.667 | 0.063 |
| great | 26 | 4 | 3 | 0.750 | 0.115 | 0.200 |
| best | 316 | 302 | 243 | 0.805 | 0.769 | 0.786 |
| excellent | 127 | 140 | 61 | 0.436 | 0.480 | 0.457 |
| good | 103 | 105 | 50 | 0.476 | 0.485 | 0.481 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 83 | 58 | 0.699 | 0.630 | 0.663 |
| mistake | 44 | 36 | 24 | 0.667 | 0.545 | 0.600 |
| miss | 27 | 31 | 21 | 0.677 | 0.778 | 0.724 |
| blunder | 21 | 14 | 12 | 0.857 | 0.571 | 0.686 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.2 | +5.5 |
| 1034847688 | black | 65.0 | 68.2 | +3.2 |
| 1041474766 | white | 98.0 | 97.1 | -0.9 |
| 1041474766 | black | 83.8 | 85.7 | +1.9 |
| 184759554082 | white | 81.2 | 85.5 | +4.3 |
| 184759554082 | black | 87.7 | 90.4 | +2.7 |
| 185209623352 | white | 72.7 | 75.3 | +2.6 |
| 185209623352 | black | 72.6 | 73.3 | +0.7 |
| 185324357184 | white | 73.0 | 76.6 | +3.6 |
| 185324357184 | black | 62.4 | 67.2 | +4.8 |
| 185436488062 | white | 98.6 | 98.0 | -0.6 |
| 185436488062 | black | 38.5 | 42.6 | +4.1 |
| 185437323918 | white | 69.5 | 75.1 | +5.6 |
| 185437323918 | black | 75.7 | 73.9 | -1.8 |
| 185438343298 | white | 46.9 | 47.1 | +0.2 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 73.8 | -4.0 |
| 185438707002 | black | 83.0 | 83.9 | +0.9 |
| 185456088510 | white | 78.4 | 82.7 | +4.3 |
| 185456088510 | black | 82.2 | 86.2 | +4.0 |
| 185468039834 | white | 80.0 | 85.4 | +5.4 |
| 185468039834 | black | 87.5 | 89.5 | +2.0 |
| 185468614210 | white | 70.8 | 76.8 | +6.0 |
| 185468614210 | black | 77.1 | 81.8 | +4.7 |
| 185475865432 | white | 78.1 | 83.4 | +5.3 |
| 185475865432 | black | 66.1 | 73.7 | +7.6 |
| 185962590893 | white | 90.8 | 93.1 | +2.3 |
| 185962590893 | black | 90.9 | 92.7 | +1.8 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 63.3% | 81.6% | reviewed | 0.5 |
| 1041474766 | 25 | 25 | 56.0% | 64.0% | reviewed | 0.5 |
| 184759554082 | 62 | 62 | 61.3% | 80.6% | reviewed | 0.5 |
| 185209623352 | 155 | 155 | 58.7% | 85.2% | reviewed | 67.8 |
| 185324357184 | 55 | 55 | 67.3% | 83.6% | reviewed | 0.5 |
| 185436488062 | 13 | 13 | 92.3% | 100.0% | reviewed | 0.5 |
| 185437323918 | 108 | 103 | 51.5% | 82.5% | reviewed | 53.7 |
| 185438343298 | 20 | 20 | 80.0% | 85.0% | reviewed | 0.5 |
| 185438707002 | 95 | 91 | 73.6% | 92.3% | reviewed | 69.8 |
| 185456088510 | 60 | 60 | 70.0% | 86.7% | reviewed | 29.1 |
| 185468039834 | 38 | 38 | 65.8% | 81.6% | reviewed | 0.5 |
| 185468614210 | 54 | 54 | 63.0% | 70.4% | reviewed | 0.5 |
| 185475865432 | 53 | 53 | 64.2% | 81.1% | reviewed | 0.5 |
| 185962590893 | 78 | 78 | 75.6% | 93.6% | reviewed | 0.5 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label equals the collector's guess for 0 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | best | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | best | precision |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (303)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 221 | best -> excellent x39, good -> excellent x32, excellent -> good x23, excellent -> best x23, inaccuracy -> good x22, great -> best x20 |
| `brilliant_event` | 58 | best -> brilliant x31, excellent -> brilliant x14, good -> brilliant x7, great -> brilliant x3, book -> brilliant x2, mistake -> brilliant x1 |
| `miss_detector` | 9 | blunder -> miss x6, mistake -> miss x3 |
| `mate_override` | 7 | excellent -> inaccuracy x3, good -> miss x1, good -> inaccuracy x1, excellent -> good x1, best -> inaccuracy x1 |
| `blunder_softened` | 3 | miss -> mistake x2, blunder -> mistake x1 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `losing_material_hardened` | 2 | good -> mistake x1, excellent -> mistake x1 |
| `great_find_event` | 1 | best -> great x1 |

### `precision` (221)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 5 | 3. d4 | best | excellent | precision | excellent | 0.0009 | 0.524 | no | c4 | - | +0.33 | +0.27 |
| 1034847688 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0028 | 0.504 | no | c5 | - | +0.13 | -0.04 |
| 1034847688 | 9 | 5. c4 | inaccuracy | good | precision | good | 0.0468 | 0.496 | no | c3 | Bd3 | -0.52 | -0.54 |
| 1034847688 | 14 | 7... Nc6 | good | inaccuracy | precision | inaccuracy | 0.0517 | 0.523 | no | cxd4 | - | +0.28 | +0.30 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0348 | 0.529 | no | a3 | - | +0.12 | -0.06 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0512 | 0.572 | no | cxb5 | - | +0.24 | +0.22 |
| 1034847688 | 26 | 13... h6 | inaccuracy | excellent | precision | excellent | 0.0178 | 0.476 | no | a4 | - | +0.90 | +0.36 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.531 | yes | Nxf3 | - | -0.10 | -0.29 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.538 | yes | Rh3 | - | +0.39 | +0.28 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.00 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0487 | 0.500 | no | fxe6 | - | +0.46 | +0.76 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.571 | yes | exf7+ | - | +0.09 | +0.88 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.418 | yes | Kxf7 | Rxf7 | +0.92 | +0.55 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M14 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0310 | 0.560 | no | d4 | - | +0.37 | +0.32 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0027 | 0.471 | no | e5 | - | +0.38 | +0.38 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.534 | yes | Bg2 | - | +0.34 | +0.38 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0089 | 0.466 | no | e5 | - | +0.59 | +0.49 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0356 | 0.544 | no | d3 | - | +0.17 | +0.09 |
| 1041474766 | 16 | 8... Bb4 | good | excellent | precision | excellent | 0.0195 | 0.470 | no | Be7 | - | +0.76 | +0.62 |
| 1041474766 | 17 | 9. dxe5 | good | excellent | precision | excellent | 0.0168 | 0.555 | no | Bd2 | - | +0.39 | +0.39 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0302 | 0.532 | no | d5 | - | +0.08 | +0.02 |
| 184759554082 | 9 | 5. h4 | inaccuracy | good | precision | good | 0.0477 | 0.540 | no | Be2 | Be2 | -0.11 | -0.05 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0191 | 0.487 | no | Nc3 | - | -0.25 | -0.19 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0223 | 0.497 | no | Nxh5 | - | +0.03 | +0.16 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.514 | yes | hxg6 | - | -0.13 | -0.19 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.585 | yes | d5 | - | -0.52 | -0.47 |
| 184759554082 | 32 | 16... b6 | best | good | precision | good | 0.0226 | 0.680 | no | b5 | - | -0.96 | -1.08 |
| 184759554082 | 33 | 17. Qc2 | best | excellent | precision | excellent | 0.0071 | 0.334 | no | Qc1 | - | -0.96 | -0.93 |
| 184759554082 | 35 | 18. O-O-O | good | excellent | precision | excellent | 0.0030 | 0.369 | no | Qb2+ | - | -1.01 | -1.12 |
| 184759554082 | 38 | 19... Bf5 | excellent | good | precision | good | 0.0461 | 0.677 | no | Bh3 | - | -1.10 | -0.84 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.714 | yes | Re6 | - | -1.31 | -1.41 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0065 | 0.287 | no | Rh1 | - | -1.28 | -1.38 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.711 | yes | a5 | - | -1.16 | -1.49 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0089 | 0.279 | no | Rh1 | f3 | -1.61 | -1.72 |
| 184759554082 | 55 | 28. Rh1 | inaccuracy | good | precision | good | 0.0476 | 0.293 | no | Rc2 | Rg1 | -1.76 | -1.76 |
| 184759554082 | 56 | 28... Ree8 | good | excellent | precision | excellent | 0.0169 | 0.754 | no | Rxh1 | - | -1.61 | -1.53 |
| 184759554082 | 57 | 29. Ka2 | good | excellent | precision | excellent | 0.0162 | 0.274 | no | Rhd1 | - | -1.73 | -1.89 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0451 | 0.547 | no | dxc6 | - | -0.08 | +0.03 |
| 185209623352 | 11 | 6. Bb5 | excellent | good | precision | good | 0.0203 | 0.514 | no | h3 | - | 0.00 | -0.11 |
| 185209623352 | 14 | 7... Qd6 | inaccuracy | good | precision | good | 0.0436 | 0.474 | no | Bd7 | Bd7 | +1.28 | +1.24 |
| 185209623352 | 17 | 9. Qd2 | inaccuracy | good | precision | good | 0.0460 | 0.684 | no | Bxc6 | Bxc6 | +2.14 | +2.42 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.795 | yes | Nxe4 | - | +5.09 | +5.65 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0705 | 0.801 | no | Nxc6 | Nxc6 | +4.00 | +4.12 |
| 185209623352 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0088 | 0.269 | no | Rxd4 | - | +4.04 | +4.04 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0251 | 0.714 | no | O-O-O | O-O-O | +3.00 | +3.66 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0443 | 0.304 | no | Bd7 | - | +4.18 | +4.63 |
| 185209623352 | 40 | 20... Rd8 | inaccuracy | good | precision | good | 0.0435 | 0.327 | no | b6 | - | +3.82 | +4.11 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1903 | 0.717 | no | Bxe6 | - | +0.61 | +0.47 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.672 | yes | Rc5+ | - | +3.32 | +3.27 |
| 185209623352 | 46 | 23... Nd3+ | excellent | good | precision | good | 0.0393 | 0.451 | no | Bxe5 | - | +0.92 | +1.11 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.562 | yes | Nxd3 | Rxd3 | -0.61 | +1.37 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0105 | 0.286 | no | Ka6 | - | +3.97 | +4.26 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0194 | 0.285 | no | Bc3 | - | +4.48 | +4.52 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0091 | 0.747 | no | Rh5 | - | +4.14 | +4.58 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0140 | 0.766 | no | h4 | - | +4.64 | +4.91 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0246 | 0.762 | no | Rh5 | - | +4.51 | +4.44 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0313 | 0.293 | no | Kf5 | - | +4.38 | +4.51 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.735 | yes | Kc2 | - | +4.38 | +4.47 |
| 185209623352 | 70 | 35... Rxc4 | excellent | best | precision | best | 0.0000 | 0.260 | yes | Rxc4 | - | +4.77 | +4.65 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0316 | 0.659 | no | Kd3 | - | +2.98 | +2.85 |
| 185209623352 | 78 | 39... Rb2+ | good | excellent | precision | excellent | 0.0167 | 0.398 | no | Rf2 | - | +2.15 | +1.76 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.598 | yes | Kc1 | - | +2.15 | +2.14 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0784 | 0.266 | no | Kd5 | - | +6.01 | +6.47 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1508 | 0.649 | no | Rhxe7 | Rhxe7 | -0.08 | +0.00 |
| 185209623352 | 87 | 44. f5+ | excellent | good | precision | good | 0.0232 | 0.516 | no | g4 | - | 0.00 | -0.05 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.683 | yes | Rf1+ | - | +3.73 | +3.58 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.761 | yes | Kxb2 | - | +5.17 | +5.59 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0058 | 0.220 | no | Bf6+ | - | +5.65 | +5.74 |
| 185209623352 | 97 | 49. Kc2 | best | excellent | precision | excellent | 0.0026 | 0.794 | no | Kb1 | - | +5.89 | +5.89 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0141 | 0.188 | no | Bd8 | - | +6.33 | +6.68 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0000 | 0.824 | no | Kd3 | - | +6.59 | +6.87 |
| 185209623352 | 108 | 54... Kh5 | excellent | best | precision | best | 0.0000 | 0.175 | yes | Kh5 | - | +6.70 | +7.12 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0104 | 0.837 | no | Rb6 | - | +6.54 | +6.59 |
| 185209623352 | 112 | 56... Bxe5 | excellent | best | precision | best | 0.0000 | 0.184 | yes | Bxe5 | - | +6.75 | +6.84 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.110 | yes | Kf6 | - | +7.19 | +8.48 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | best | precision | best | 0.0000 | 0.069 | yes | Ke6 | Ke7 | +10.6 | M15 |
| 185209623352 | 117 | 59. h5 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | +8.42 | +8.51 |
| 185209623352 | 118 | 59... Kf7 | inaccuracy | good | precision | good | 0.0495 | 0.127 | no | Kf6 | Kf6 | M10 | M12 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | M12 |
| 185209623352 | 123 | 62. Rg8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rh4 | - | M7 | M15 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke6 | - | M5 | M10 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg7 | - | M3 | M4 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | no | Ke5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | no | Kc1 | - | M9 | M8 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb5 | - | M5 | M5 |
| 185324357184 | 6 | 3... Bc5 | blunder | mistake | precision | mistake | 0.1870 | 0.510 | no | d5 | - | +3.27 | +3.23 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0066 | 0.294 | no | d4 | - | -4.03 | -3.95 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0345 | 0.598 | no | Ng3 | Ng3 | -0.98 | -0.96 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0772 | 0.577 | no | Na6 | - | +0.29 | +0.16 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.509 | yes | Qg1 | - | +0.29 | +0.20 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0210 | 0.333 | no | Qh5 | - | +3.38 | +3.60 |
| 185324357184 | 39 | 20. Rf1 | great | best | precision | best | 0.0000 | 0.695 | yes | Rf1 | - | +3.38 | +3.58 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0006 | 0.503 | no | Rh2 | - | +0.11 | +0.00 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.509 | no | g4 | - | +0.26 | +0.31 |
| 185324357184 | 49 | 25. c3 | good | inaccuracy | precision | inaccuracy | 0.0526 | 0.525 | no | b3 | - | -0.53 | -0.49 |
| 185324357184 | 52 | 26... a5 | good | excellent | precision | excellent | 0.0194 | 0.535 | no | h6 | - | -0.29 | -0.27 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0205 | 0.547 | no | h3 | - | +0.65 | +0.50 |
| 185437323918 | 10 | 5... Kf8 | good | excellent | precision | excellent | 0.0171 | 0.435 | no | Ke7 | - | +1.39 | +1.30 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0842 | 0.289 | no | d3 | d3 | -5.55 | -5.83 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0070 | 0.793 | no | g4 | - | -5.16 | -5.88 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0281 | 0.788 | no | Qe8 | - | -4.94 | -4.95 |
| 185437323918 | 23 | 12. Qg3 | mistake | good | precision | good | 0.0410 | 0.228 | no | Qe3 | - | -6.88 | -6.88 |
| 185437323918 | 26 | 13... Nxg3+ | excellent | best | precision | best | 0.0000 | 0.832 | yes | Nxg3+ | - | -6.67 | -6.72 |
| 185437323918 | 31 | 16. Nd2 | excellent | best | precision | best | 0.0000 | 0.193 | yes | Nd2 | - | -6.16 | -6.18 |
| 185437323918 | 33 | 17. bxc3 | good | excellent | precision | excellent | 0.0037 | 0.199 | no | g4 | - | -6.58 | -6.96 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0191 | 0.835 | no | Rxh2+ | - | -6.58 | -6.39 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0004 | 0.796 | no | Qe2 | - | -5.96 | -8.78 |
| 185437323918 | 40 | 20... g4 | inaccuracy | mistake | precision | mistake | 0.1166 | 0.869 | no | Rh7 | - | -4.32 | -4.77 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0262 | 0.742 | no | Qf4 | - | -3.59 | -3.48 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0143 | 0.770 | no | e4 | - | -4.41 | -4.84 |
| 185437323918 | 53 | 27. h3 | excellent | best | precision | best | 0.0000 | 0.244 | yes | h3 | - | -4.46 | -5.11 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0471 | 0.682 | no | Bc2 | - | -2.41 | -2.71 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.791 | yes | Be4 | - | -5.61 | -5.80 |
| 185437323918 | 61 | 31. Rf1 | excellent | best | precision | best | 0.0000 | 0.167 | no | Kg2 | - | -7.00 | -6.79 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0037 | 0.830 | no | Rf8 | - | -6.21 | -6.64 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0077 | 0.807 | no | Kf4 | - | -5.11 | -5.92 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | excellent | precision | excellent | 0.0030 | 0.201 | no | Kg2 | Kg2 | -6.13 | -6.00 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0232 | 0.802 | no | e4 | e4 | -5.01 | -5.40 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.214 | yes | Kf3 | - | -6.12 | -6.11 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0018 | 0.806 | no | Bb4 | - | -6.12 | -6.63 |
| 185437323918 | 75 | 38. Ke4 | best | excellent | precision | excellent | 0.0000 | 0.176 | no | Ke2 | - | -6.12 | -6.33 |
| 185437323918 | 76 | 38... Rf4+ | best | excellent | precision | excellent | 0.0018 | 0.814 | no | Bc3 | - | -6.12 | -6.72 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0018 | 0.156 | no | Kf6 | - | -7.11 | -7.29 |
| 185437323918 | 82 | 41... a5 | best | excellent | precision | excellent | 0.0052 | 0.845 | no | Bb4 | - | -7.11 | -7.15 |
| 185437323918 | 83 | 42. Kd7 | excellent | good | precision | good | 0.0337 | 0.159 | no | c5 | - | -7.28 | -8.34 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0114 | 0.875 | no | Bg3 | - | -7.28 | -7.91 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.137 | yes | Kxc7 | - | -8.05 | -8.54 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0055 | 0.880 | no | Ba5+ | - | -8.05 | -9.92 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.090 | yes | d6 | - | -8.99 | -8.52 |
| 185437323918 | 91 | 46. Kxb7 | excellent | good | precision | good | 0.0208 | 0.074 | no | Kd7 | - | -9.64 | -9.66 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | excellent | precision | excellent | 0.0166 | 0.055 | no | Ka6 | Ka6 | -M17 | -M17 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd2 | - | -M16 | -11.08 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.051 | yes | c6 | - | -10.7 | -13.31 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0020 | 0.957 | no | Qc7 | - | -10.7 | -11.77 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2035 | 0.203 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0107 | 0.509 | no | Nf3 | - | -0.01 | -0.03 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.502 | yes | h6 | - | -0.01 | +0.13 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.508 | yes | Bh4 | - | -0.01 | -0.12 |
| 185438707002 | 26 | 13... O-O-O | miss | inaccuracy | precision | inaccuracy | 0.0934 | 0.634 | no | Rg8 | Rg8 | -0.69 | -0.46 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.574 | yes | c3 | - | +1.35 | +1.47 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0803 | 0.414 | no | Bb6 | - | +2.65 | +2.92 |
| 185438707002 | 41 | 21. O-O-O | excellent | good | precision | good | 0.0373 | 0.738 | no | O-O | - | +3.58 | +3.58 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0252 | 0.726 | no | Qe2 | - | +3.74 | +3.59 |
| 185438707002 | 44 | 22... cxd4 | excellent | good | precision | good | 0.0209 | 0.299 | no | Nc4 | - | +4.01 | +3.93 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0189 | 0.724 | no | Rd2 | - | +3.82 | +3.66 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0667 | 0.296 | no | Rf8 | - | +4.87 | +5.12 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.722 | yes | Qxd8+ | - | +3.69 | +4.11 |
| 185438707002 | 65 | 33. Rd5 | excellent | good | precision | good | 0.0275 | 0.630 | no | Rd8 | - | +1.84 | +2.52 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | good | precision | good | 0.0298 | 0.355 | no | c6 | Qb3 | +2.60 | +3.08 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.711 | yes | Qb2+ | - | -3.65 | -4.13 |
| 185438707002 | 74 | 37... Qxd5 | excellent | best | precision | best | 0.0000 | 0.719 | yes | Qxd5 | - | -3.38 | -3.64 |
| 185438707002 | 76 | 38... Qd1+ | good | inaccuracy | precision | inaccuracy | 0.0612 | 0.726 | no | b6 | - | -2.61 | -2.95 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0210 | 0.679 | no | Qe2 | - | -2.36 | -2.75 |
| 185438707002 | 79 | 40. h4 | best | excellent | precision | excellent | 0.0069 | 0.342 | no | Qg7 | - | -2.36 | -2.76 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0056 | 0.887 | no | Qe6+ | - | -8.73 | -8.47 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.118 | yes | g4 | - | -8.80 | -8.39 |
| 185438707002 | 89 | 45. g3 | inaccuracy | mistake | precision | mistake | 0.1046 | 0.105 | no | g5 | g5 | -M7 | -10.47 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0521 | 0.399 | no | e6 | e6 | +1.09 | +0.99 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0014 | 0.653 | no | Nf3 | - | +0.96 | +0.97 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0028 | 0.330 | no | d5 | - | +1.01 | +1.03 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0451 | 0.353 | no | Bg7 | Bg7 | +1.25 | +1.27 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0000 | 0.620 | no | Ne2 | - | +0.81 | +0.84 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0074 | 0.369 | no | Bg7 | - | +0.81 | +0.87 |
| 185456088510 | 17 | 9. Ne2 | good | excellent | precision | excellent | 0.0194 | 0.635 | no | d5 | - | +0.65 | +0.74 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.620 | yes | Ng3 | - | +0.65 | +0.77 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.681 | yes | h5 | - | +1.12 | +1.17 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0387 | 0.811 | no | Nh4 | - | +1.72 | +1.86 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0623 | 0.166 | no | Rd6 | - | +2.89 | +3.38 |
| 185456088510 | 50 | 25... Rf6 | inaccuracy | good | precision | good | 0.0328 | 0.165 | no | Nxe3 | Nxe3 | +2.84 | +3.08 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.939 | yes | Nxe3 | - | -4.25 | -4.50 |
| 185456088510 | 57 | 29. Nd4 | mistake | good | precision | good | 0.0265 | 0.054 | no | Qb5 | - | -4.77 | -5.61 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0092 | 0.448 | no | Na4 | - | -0.94 | -0.95 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0380 | 0.467 | no | Kf8 | - | +0.61 | +1.22 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0295 | 0.434 | no | dxe5 | dxe5 | +1.53 | +1.67 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.596 | yes | Qh5 | - | +1.48 | +1.34 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1879 | 0.626 | no | Nxc7+ | Nxc7+ | -0.91 | -1.07 |
| 185468039834 | 25 | 13. Nf6+ | good | best | precision | best | 0.0000 | 0.434 | yes | Nf6+ | - | -1.28 | -1.15 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.692 | yes | Rf8 | - | -3.36 | -3.52 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0015 | 0.309 | no | Qd3 | - | -3.39 | -3.65 |
| 185468039834 | 36 | 18... a5 | good | excellent | precision | excellent | 0.0190 | 0.697 | no | Rf7 | - | -2.75 | -3.19 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.498 | yes | exd4 | - | +0.15 | +0.02 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.506 | yes | Bb4+ | - | 0.00 | +0.01 |
| 185468614210 | 13 | 7. Nc3 | book | good | precision | good | 0.0233 | 0.501 | no | Bd2 | - | -0.35 | -0.39 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0410 | 0.471 | no | Nxe4 | Nxe4 | +1.21 | +1.27 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0233 | 0.492 | no | Kg8 | Kg8 | +1.21 | +0.54 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0215 | 0.531 | no | Qh5+ | Qh5+ | +0.18 | +0.16 |
| 185468614210 | 48 | 24... Rxc3 | best | excellent | precision | excellent | 0.0047 | 0.500 | no | g6 | - | +0.14 | +0.03 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0162 | 0.553 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.460 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.537 | yes | Nc3 | - | +0.74 | +0.67 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.461 | yes | e6 | - | +0.74 | +0.68 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0081 | 0.467 | no | Bb4 | - | +0.55 | +0.70 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0097 | 0.568 | no | e5 | - | +0.82 | +1.00 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0825 | 0.546 | no | Ng3 | Ng3 | -0.76 | -0.63 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0392 | 0.616 | no | Qxd1 | Qxd1 | -1.24 | -1.33 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0141 | 0.423 | no | hxg3 | - | -1.52 | -1.63 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0023 | 0.593 | no | Bd6 | - | -1.25 | -1.45 |
| 185475865432 | 33 | 17. Qxd8+ | good | excellent | precision | excellent | 0.0141 | 0.416 | no | Re1 | - | -1.78 | -1.70 |
| 185475865432 | 34 | 17... Rxd8 | inaccuracy | good | precision | good | 0.0420 | 0.598 | no | Kxd8 | Kxd8 | -0.89 | -0.96 |
| 185475865432 | 49 | 25. a6 | mistake | good | precision | good | 0.0452 | 0.685 | no | Rxe6 | Rxe6 | +1.47 | +2.47 |
| 185475865432 | 50 | 25... Bh5 | mistake | inaccuracy | precision | inaccuracy | 0.0932 | 0.360 | no | Be5 | - | +3.93 | +4.34 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0601 | 0.617 | no | Bc4 | - | +0.50 | +0.36 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.415 | yes | e5 | - | +0.67 | +0.62 |
| 185962590893 | 19 | 10. Bd2 | good | excellent | precision | excellent | 0.0139 | 0.597 | no | Bg5 | - | +0.50 | +0.35 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.444 | yes | Be7 | - | +0.55 | +0.47 |
| 185962590893 | 22 | 11... b5 | inaccuracy | mistake | precision | mistake | 0.1413 | 0.451 | no | O-O | O-O | +0.92 | +1.26 |
| 185962590893 | 24 | 12... O-O | best | excellent | precision | excellent | 0.0078 | 0.423 | no | Nc5 | - | +0.66 | +0.55 |
| 185962590893 | 27 | 14. Nxe7+ | miss | inaccuracy | precision | inaccuracy | 0.0599 | 0.752 | no | Bh6 | Bh6 | +1.01 | +1.20 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0364 | 0.304 | no | Nf8 | Ne8 | +1.62 | +1.58 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0612 | 0.732 | no | Rxd8+ | Rxd8+ | +0.96 | +1.12 |
| 185962590893 | 43 | 22. Bd2 | good | excellent | precision | excellent | 0.0161 | 0.651 | no | Qe2 | - | +0.86 | +0.84 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0000 | 0.386 | no | Nd7 | - | +0.86 | +0.72 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.613 | yes | Qe3 | Qf3 | +0.47 | +0.75 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0553 | 0.383 | no | Nf4 | Nf4 | +1.15 | +1.36 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2752 | 0.704 | no | f4 | - | -0.39 | -0.45 |
| 185962590893 | 55 | 28. Kb2 | mistake | inaccuracy | precision | inaccuracy | 0.0922 | 0.437 | no | Kd1 | Kd1 | -1.21 | -1.33 |
| 185962590893 | 61 | 31. f4 | best | excellent | precision | excellent | 0.0079 | 0.482 | no | h5 | - | -0.23 | -0.18 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | a6 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `brilliant_event` (58)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 25 | 13. Kxe2 | best | brilliant | brilliant_event | best | 0.0000 | 0.538 | yes | Kxe2 | - | +0.44 | +0.26 |
| 1034847688 | 35 | 18. hxg5 | best | brilliant | brilliant_event | best | 0.0000 | 0.500 | yes | hxg5 | - | 0.00 | +0.00 |
| 1041474766 | 13 | 7. O-O | excellent | brilliant | brilliant_event | excellent | 0.0018 | 0.533 | no | d4 | - | +0.28 | +0.24 |
| 1041474766 | 19 | 10. Bd2 | excellent | brilliant | brilliant_event | excellent | 0.0053 | 0.532 | no | a3 | - | +0.25 | +0.28 |
| 1041474766 | 20 | 10... O-O | excellent | brilliant | brilliant_event | excellent | 0.0027 | 0.475 | no | Qd8 | - | +0.40 | +0.47 |
| 1041474766 | 22 | 11... Be7 | best | brilliant | brilliant_event | best | 0.0000 | 0.470 | yes | Be7 | - | +0.40 | +0.32 |
| 184759554082 | 17 | 9. Nf3 | good | brilliant | brilliant_event | excellent | 0.0158 | 0.470 | no | d3 | - | -0.39 | -0.29 |
| 184759554082 | 21 | 11. Nc3 | best | brilliant | brilliant_event | best | 0.0000 | 0.432 | yes | Nc3 | - | -0.52 | -0.54 |
| 184759554082 | 34 | 17... Qg5 | excellent | brilliant | brilliant_event | excellent | 0.0044 | 0.644 | no | Bf5 | - | -0.88 | -0.84 |
| 184759554082 | 36 | 18... Qf6 | best | brilliant | brilliant_event | best | 0.0000 | 0.671 | yes | Qf6 | - | -1.01 | -1.10 |
| 184759554082 | 37 | 19. Kb1 | good | brilliant | brilliant_event | excellent | 0.0014 | 0.332 | no | Qb2 | - | -1.19 | -1.16 |
| 184759554082 | 46 | 23... c6 | best | brilliant | brilliant_event | best | 0.0000 | 0.707 | yes | c6 | - | -1.28 | -1.21 |
| 185209623352 | 9 | 5. Nf3 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.494 | yes | Nf3 | - | -0.16 | -0.19 |
| 185209623352 | 13 | 7. Ne5 | best | brilliant | brilliant_event | best | 0.0000 | 0.521 | yes | Ne5 | - | +0.38 | +0.46 |
| 185209623352 | 20 | 10... dxe4 | mistake | brilliant | brilliant_event | excellent | 0.0091 | 0.218 | no | Qb4 | - | +6.16 | +6.17 |
| 185209623352 | 22 | 11... Qxd4 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.283 | yes | Qxd4 | - | +4.04 | +4.28 |
| 185209623352 | 34 | 17... Kc7 | good | brilliant | brilliant_event | best | 0.0000 | 0.274 | yes | Kc7 | - | +4.76 | +4.89 |
| 185209623352 | 36 | 18... g6 | best | brilliant | brilliant_event | best | 0.0000 | 0.303 | yes | g6 | - | +3.29 | +3.82 |
| 185209623352 | 44 | 22... Kb6 | best | brilliant | brilliant_event | best | 0.0000 | 0.323 | yes | Kb6 | - | +3.32 | +3.18 |
| 185209623352 | 51 | 26. Bxf5 | best | brilliant | brilliant_event | best | 0.0000 | 0.724 | yes | Bxf5 | - | +3.97 | +4.33 |
| 185324357184 | 11 | 6. Nf3 | best | brilliant | brilliant_event | best | 0.0000 | 0.312 | yes | Nf3 | - | -3.32 | -3.73 |
| 185324357184 | 13 | 7. Qe2 | best | brilliant | brilliant_event | best | 0.0000 | 0.303 | yes | Qe2 | - | -3.32 | -3.83 |
| 185324357184 | 26 | 13... Nxe5 | best | brilliant | brilliant_event | best | 0.0000 | 0.435 | yes | Nxe5 | - | +1.30 | +1.57 |
| 185324357184 | 34 | 17... Rxe2 | good | brilliant | brilliant_event | excellent | 0.0113 | 0.348 | no | Bg4 | - | +3.07 | +2.96 |
| 185324357184 | 35 | 18. Bxe2 | best | brilliant | brilliant_event | best | 0.0000 | 0.663 | yes | Bxe2 | - | +3.07 | +3.12 |
| 185324357184 | 37 | 19. Re1 | great | brilliant | brilliant_event | best | 0.0000 | 0.665 | yes | Re1 | - | +3.07 | +3.03 |
| 185437323918 | 13 | 7. Bd5 | excellent | brilliant | brilliant_event | excellent | 0.0117 | 0.303 | no | d4 | - | -3.51 | -3.81 |
| 185437323918 | 17 | 9. Qd3 | excellent | brilliant | brilliant_event | excellent | 0.0039 | 0.212 | no | Qe3 | - | -5.63 | -5.76 |
| 185437323918 | 19 | 10. exd5 | best | brilliant | brilliant_event | best | 0.0000 | 0.202 | yes | exd5 | - | -5.16 | -5.64 |
| 185437323918 | 32 | 16... dxc3 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.809 | yes | dxc3 | - | -5.87 | -5.97 |
| 185437323918 | 37 | 19. Nf3 | best | brilliant | brilliant_event | best | 0.0000 | 0.211 | yes | Nf3 | - | -5.96 | -5.84 |
| 185438343298 | 14 | 7... Qh4+ | great | brilliant | brilliant_event | best | 0.0000 | 0.792 | yes | Qh4+ | - | -5.11 | -6.25 |
| 185438343298 | 16 | 8... Nxg3 | best | brilliant | brilliant_event | best | 0.0000 | 0.792 | yes | Nxg3 | - | -5.11 | -5.80 |
| 185456088510 | 31 | 16. exd6 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.758 | yes | exd6 | - | +1.55 | +1.18 |
| 185456088510 | 36 | 18... e5 | best | brilliant | brilliant_event | best | 0.0000 | 0.206 | yes | e5 | - | +1.83 | +2.29 |
| 185456088510 | 38 | 19... Nxc5 | best | brilliant | brilliant_event | best | 0.0000 | 0.234 | yes | Nxc5 | - | +1.72 | +1.96 |
| 185456088510 | 41 | 21. Bxa6 | best | brilliant | brilliant_event | best | 0.0000 | 0.826 | yes | Bxa6 | - | +2.36 | +2.65 |
| 185468039834 | 14 | 7... h6 | good | brilliant | brilliant_event | excellent | 0.0145 | 0.489 | no | Ne5 | - | +0.60 | +0.44 |
| 185468039834 | 24 | 12... c6 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.562 | yes | c6 | - | -0.83 | -1.14 |
| 185468039834 | 26 | 13... Ke7 | best | brilliant | brilliant_event | best | 0.0000 | 0.567 | yes | Ke7 | - | -1.28 | -1.17 |
| 185468039834 | 31 | 16. b4 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.306 | no | Qh3 | - | -3.61 | -3.62 |
| 185468614210 | 9 | 5. d4 | book | brilliant | brilliant_event | excellent | 0.0076 | 0.516 | no | b4 | - | +0.15 | +0.04 |
| 185468614210 | 11 | 6. cxd4 | book | brilliant | brilliant_event | best | 0.0000 | 0.501 | yes | cxd4 | - | 0.00 | -0.10 |
| 185468614210 | 15 | 8. d5 | excellent | brilliant | brilliant_event | excellent | 0.0070 | 0.538 | no | Bg5 | - | +0.51 | +0.49 |
| 185468614210 | 24 | 12... Nxd6 | best | brilliant | brilliant_event | best | 0.0000 | 0.513 | yes | Nxd6 | - | -0.24 | -0.32 |
| 185468614210 | 25 | 13. Bd3 | good | brilliant | brilliant_event | excellent | 0.0151 | 0.481 | no | Bxd6 | - | -0.61 | -0.53 |
| 185468614210 | 27 | 14. O-O | best | brilliant | brilliant_event | best | 0.0000 | 0.509 | yes | O-O | - | +0.15 | +0.14 |
| 185468614210 | 29 | 15. Bxh7+ | best | brilliant | brilliant_event | best | 0.0000 | 0.514 | yes | Bxh7+ | - | +0.25 | +0.21 |
| 185468614210 | 30 | 15... Kxh7 | best | brilliant | brilliant_event | best | 0.0000 | 0.488 | yes | Kxh7 | - | +0.25 | +0.15 |
| 185468614210 | 34 | 17... Kg8 | great | brilliant | brilliant_event | best | 0.0000 | 0.491 | yes | Kg8 | - | +0.18 | +0.16 |
| 185468614210 | 35 | 18. Nxe6 | best | brilliant | brilliant_event | best | 0.0000 | 0.509 | yes | Nxe6 | - | +0.18 | +0.16 |
| 185468614210 | 38 | 19... Qf6 | good | brilliant | brilliant_event | excellent | 0.0128 | 0.522 | no | b6 | - | -0.09 | -0.15 |
| 185475865432 | 15 | 8. Ne2 | best | brilliant | brilliant_event | best | 0.0000 | 0.476 | yes | Ne2 | - | -0.53 | -0.41 |
| 185475865432 | 22 | 11... dxe6 | best | brilliant | brilliant_event | best | 0.0000 | 0.537 | yes | dxe6 | - | -0.76 | -0.59 |
| 185475865432 | 25 | 13. Ne5 | best | brilliant | brilliant_event | excellent | 0.0118 | 0.416 | no | Re1 | - | -1.49 | -1.66 |
| 185475865432 | 37 | 19. Rad1 | excellent | brilliant | brilliant_event | excellent | 0.0028 | 0.600 | no | Bxa5 | - | +1.50 | +1.76 |
| 185475865432 | 38 | 19... Rxd1 | best | brilliant | brilliant_event | best | 0.0000 | 0.399 | yes | Rxd1 | - | +1.50 | +1.71 |
| 185962590893 | 34 | 17... Red7 | best | brilliant | brilliant_event | excellent | 0.0056 | 0.329 | no | Rxd1+ | - | +0.96 | +1.14 |

### `miss_detector` (9)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1297 | 0.650 | no | g4 | - | -0.01 | +0.06 |
| 1034847688 | 37 | 19. Rh4 | mistake | miss (brilliant) | miss_detector | mistake | 0.1203 | 0.589 | no | Rh6 | Rh6 | -0.10 | -0.33 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1758 | 0.812 | no | Rxf6+ | Rxf6+ | +2.74 | +2.92 |
| 185209623352 | 88 | 44... Kxf5 | blunder | miss (tactic) | miss_detector | blunder | 0.2000 | 0.503 | no | Kf7 | - | +3.73 | +3.39 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.4385 | 0.770 | no | Rxf6+ | - | -2.81 | -3.10 |
| 185209623352 | 92 | 46... Bg5 | blunder | miss (brilliant) | miss_detector | blunder | 0.4295 | 0.668 | no | a3 | a3 | +5.17 | +5.13 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2244 | 0.734 | no | Kg7 | - | -0.17 | -0.17 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2046 | 0.205 | no | Kd2 | - | -M1 | -M1 |
| 185468614210 | 7 | 4. c3 | mistake | miss (tactic) | miss_detector | mistake | 0.1468 | 0.595 | no | Nxe5 | Nxe5 | -0.88 | -0.89 |

### `mate_override` (7)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M5 |
| 185209623352 | 142 | 71... Kb5 | good | inaccuracy | mate_override | inaccuracy | 0.0815 | 0.081 | no | Kb7 | - | M8 | M9 |
| 185437323918 | 93 | 47. d7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0769 | 0.077 | no | c6 | - | -11.0 | -M19 |
| 185437323918 | 94 | 47... Qb2+ | excellent | good | mate_override | good | 0.0958 | 1.000 | no | Qb1+ | - | -9.07 | -12.24 |
| 185437323918 | 105 | 53. Ke7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0488 | 0.049 | no | Kg7 | - | -M3 | -M15 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |
| 185438707002 | 91 | 46. Kh4 | best | inaccuracy | mate_override | inaccuracy | 0.0806 | 0.081 | no | g5 | - | -M6 | -M6 |

### `blunder_softened` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2084 | 0.878 | no | Qxg2 | Qxg2 | -0.96 | -0.79 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2257 | 0.577 | no | Qxg3+ | Qxg3+ | +2.48 | +2.69 |
| 185438707002 | 67 | 34. Kc2 | blunder | mistake | blunder_softened | blunder | 0.3867 | 0.675 | no | Kd1 | - | -3.65 | -3.80 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0039 | 0.460 | no | Nf6 | - | +0.82 | +0.83 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0606 | 0.527 | no | Nxe5 | Nxe5 | -0.62 | -0.57 |

### `losing_material_hardened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 59 | 30. g5+ | good | mistake | losing_material_hardened | good | 0.0247 | 0.206 | no | Rg3 | - | -6.55 | -6.48 |
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | excellent | 0.0000 | 0.109 | no | Kd7 | - | -8.94 | -8.63 |

### `great_find_event` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.507 | yes | Bxe5 | - | +0.18 | +0.00 |

