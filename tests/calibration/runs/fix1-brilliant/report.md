# Calibration report: fix1-brilliant

- Generated: 2026-10-17T19:13:09+00:00
- Commit: `9ddf4a553322` + uncommitted backend changes (diff sha256 `391a695c218c`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 68.2% (584/856) |
| Within one step | 89.6% (767/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.71 / 0.19 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 0.82 |
| Accuracy mean abs. difference | 2.96 (n=28, max 6.84) |
| Accuracy bias (ours - app) | +2.79 |
| Best move = app's suggestion | 83.2% (114/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | 1 | . | . | . | . | . | 3 |
| **great** | . | **5** | 21 | . | . | . | . | . | . | . | 26 |
| **best** | . | 2 | **270** | 39 | 5 | . | . | . | . | . | 316 |
| **excellent** | . | . | 43 | **61** | 19 | 1 | 2 | 1 | . | . | 127 |
| **good** | . | . | 7 | 32 | **56** | . | 7 | . | 1 | . | 103 |
| **book** | . | . | 8 | 7 | 3 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 5 | 2 | 24 | 1 | **57** | 3 | . | . | 92 |
| **mistake** | . | . | . | 2 | 1 | . | 11 | **25** | 3 | 2 | 44 |
| **miss** | . | . | . | . | . | . | 6 | 4 | **16** | 1 | 27 |
| **blunder** | . | . | . | . | . | . | . | 3 | 4 | **14** | 21 |
| **total** | 1 | 7 | 355 | 143 | 109 | 81 | 83 | 36 | 24 | 17 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 7 | 5 | 0.714 | 0.192 | 0.303 |
| best | 316 | 355 | 270 | 0.761 | 0.854 | 0.805 |
| excellent | 127 | 143 | 61 | 0.427 | 0.480 | 0.452 |
| good | 103 | 109 | 56 | 0.514 | 0.544 | 0.528 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 83 | 57 | 0.687 | 0.620 | 0.651 |
| mistake | 44 | 36 | 25 | 0.694 | 0.568 | 0.625 |
| miss | 27 | 24 | 16 | 0.667 | 0.593 | 0.627 |
| blunder | 21 | 17 | 14 | 0.824 | 0.667 | 0.737 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.9 | +6.2 |
| 1034847688 | black | 65.0 | 71.8 | +6.8 |
| 1041474766 | white | 98.0 | 97.5 | -0.5 |
| 1041474766 | black | 83.8 | 85.9 | +2.1 |
| 184759554082 | white | 81.2 | 85.2 | +4.0 |
| 184759554082 | black | 87.7 | 90.0 | +2.3 |
| 185209623352 | white | 72.7 | 74.6 | +1.9 |
| 185209623352 | black | 72.6 | 75.3 | +2.7 |
| 185324357184 | white | 73.0 | 76.4 | +3.4 |
| 185324357184 | black | 62.4 | 65.6 | +3.2 |
| 185436488062 | white | 98.6 | 98.1 | -0.5 |
| 185436488062 | black | 38.5 | 41.2 | +2.7 |
| 185437323918 | white | 69.5 | 73.5 | +4.0 |
| 185437323918 | black | 75.7 | 78.8 | +3.1 |
| 185438343298 | white | 46.9 | 47.3 | +0.4 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 76.5 | -1.3 |
| 185438707002 | black | 83.0 | 84.5 | +1.5 |
| 185456088510 | white | 78.4 | 83.3 | +4.9 |
| 185456088510 | black | 82.2 | 86.5 | +4.3 |
| 185468039834 | white | 80.0 | 80.2 | +0.2 |
| 185468039834 | black | 87.5 | 90.3 | +2.8 |
| 185468614210 | white | 70.8 | 75.7 | +4.9 |
| 185468614210 | black | 77.1 | 82.2 | +5.1 |
| 185475865432 | white | 78.1 | 81.0 | +2.9 |
| 185475865432 | black | 66.1 | 71.8 | +5.7 |
| 185962590893 | white | 90.8 | 93.0 | +2.2 |
| 185962590893 | black | 90.9 | 94.1 | +3.2 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 65.3% | 83.7% | reviewed | 87.6 |
| 1041474766 | 25 | 25 | 68.0% | 80.0% | reviewed | 52.9 |
| 184759554082 | 62 | 62 | 69.4% | 88.7% | reviewed | 107.7 |
| 185209623352 | 155 | 155 | 58.1% | 88.4% | reviewed | 91.1 |
| 185324357184 | 55 | 55 | 80.0% | 94.5% | reviewed | 59.4 |
| 185436488062 | 13 | 13 | 92.3% | 92.3% | reviewed | 17.1 |
| 185437323918 | 108 | 103 | 60.2% | 88.3% | reviewed | 78.2 |
| 185438343298 | 20 | 20 | 85.0% | 90.0% | reviewed | 18.7 |
| 185438707002 | 95 | 91 | 74.7% | 93.4% | reviewed | 97.7 |
| 185456088510 | 60 | 60 | 68.3% | 91.7% | reviewed | 73.5 |
| 185468039834 | 38 | 38 | 76.3% | 89.5% | reviewed | 45.7 |
| 185468614210 | 54 | 54 | 72.2% | 85.2% | reviewed | 71.4 |
| 185475865432 | 53 | 53 | 67.9% | 90.6% | reviewed | 78.5 |
| 185962590893 | 78 | 78 | 69.2% | 93.6% | reviewed | 79.9 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label equals the collector's guess for 0 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | excellent | precision |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (272)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 255 | excellent -> best x43, best -> excellent x39, good -> excellent x32, inaccuracy -> good x24, great -> best x21, excellent -> good x19 |
| `miss_detector` | 7 | blunder -> miss x4, mistake -> miss x3 |
| `blunder_softened` | 3 | miss -> mistake x3 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `mate_override` | 2 | good -> miss x1, excellent -> inaccuracy x1 |
| `great_find_event` | 2 | best -> great x2 |
| `losing_material_hardened` | 1 | excellent -> mistake x1 |

### `precision` (255)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 4 | 2... Nf6 | excellent | best | precision | best | 0.0000 | 0.481 | yes | Nf6 | - | +0.33 | +0.31 |
| 1034847688 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0009 | 0.504 | no | c5 | - | +0.13 | +0.12 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0178 | 0.490 | no | Be2 | - | -0.10 | -0.21 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0512 | 0.572 | no | cxb5 | - | +0.24 | +0.22 |
| 1034847688 | 22 | 11... a5 | mistake | inaccuracy | precision | inaccuracy | 0.0939 | 0.479 | no | Bf5 | Nbd7 | +1.29 | +1.24 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0789 | 0.615 | no | cxb5 | cxb5 | +0.44 | +0.27 |
| 1034847688 | 26 | 13... h6 | inaccuracy | excellent | precision | excellent | 0.0066 | 0.470 | no | Qd7 | - | +0.90 | +0.45 |
| 1034847688 | 27 | 14. Ndf3 | mistake | inaccuracy | precision | inaccuracy | 0.0938 | 0.542 | no | g4 | h5 | -0.60 | -0.55 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0703 | 0.552 | no | Qc8 | Qd7 | +0.53 | +0.20 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.548 | yes | Nxf3 | - | -0.10 | -0.42 |
| 1034847688 | 40 | 20... Nf5 | inaccuracy | good | precision | good | 0.0450 | 0.544 | no | f5 | f5 | +0.50 | +0.01 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.01 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0459 | 0.499 | no | fxe6 | - | +0.46 | +0.88 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.582 | yes | exf7+ | - | +0.09 | +0.81 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.424 | yes | Kxf7 | Rxf7 | +0.92 | +1.59 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | +10.05 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0282 | 0.569 | no | d4 | - | +0.37 | +0.46 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0018 | 0.459 | no | Nc6 | - | +0.38 | +0.35 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.531 | yes | Bg2 | - | +0.34 | +0.40 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0071 | 0.464 | no | Nc6 | - | +0.59 | +0.48 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0231 | 0.543 | no | Nf3 | - | +0.17 | +0.22 |
| 1041474766 | 12 | 6... Nbd7 | excellent | best | precision | best | 0.0000 | 0.480 | yes | Nbd7 | - | +0.37 | +0.39 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.535 | yes | O-O | - | +0.28 | +0.25 |
| 1041474766 | 19 | 10. Bd2 | excellent | best | precision | best | 0.0000 | 0.526 | yes | Bd2 | - | +0.25 | +0.29 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0350 | 0.532 | no | d5 | - | +0.08 | +0.05 |
| 184759554082 | 9 | 5. h4 | inaccuracy | good | precision | good | 0.0429 | 0.543 | no | Nf3 | Be2 | -0.11 | +0.00 |
| 184759554082 | 12 | 6... Bg7 | good | inaccuracy | precision | inaccuracy | 0.0507 | 0.557 | no | d5 | - | 0.00 | +0.00 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0398 | 0.510 | no | Nxh5 | - | +0.03 | +0.18 |
| 184759554082 | 15 | 8. hxg6 | good | excellent | precision | excellent | 0.0095 | 0.529 | no | d3 | - | -0.21 | -0.10 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.516 | yes | hxg6 | - | -0.13 | -0.04 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0604 | 0.685 | no | d5 | d5 | -0.52 | -0.39 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.587 | yes | d5 | - | -0.52 | -0.67 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1297 | 0.395 | no | cxd5 | cxd5 | -1.98 | -1.91 |
| 184759554082 | 34 | 17... Qg5 | excellent | good | precision | good | 0.0219 | 0.654 | no | Bg4 | - | -0.88 | -0.90 |
| 184759554082 | 35 | 18. O-O-O | good | excellent | precision | excellent | 0.0059 | 0.360 | no | Qb2+ | - | -1.01 | -1.28 |
| 184759554082 | 37 | 19. Kb1 | good | best | precision | best | 0.0000 | 0.340 | yes | Kb1 | - | -1.19 | -1.17 |
| 184759554082 | 38 | 19... Bf5 | excellent | good | precision | good | 0.0475 | 0.678 | no | Re5 | - | -1.10 | -0.84 |
| 184759554082 | 44 | 22... Rd6 | excellent | best | precision | best | 0.0000 | 0.686 | yes | Rd6 | - | -1.28 | -1.32 |
| 184759554082 | 47 | 24. Ka1 | best | good | precision | good | 0.0323 | 0.299 | no | b4 | - | -1.28 | -1.59 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.734 | yes | a5 | - | -1.16 | -1.52 |
| 184759554082 | 49 | 25. a4 | inaccuracy | good | precision | good | 0.0223 | 0.275 | no | Rh1 | f3 | -1.61 | -1.85 |
| 184759554082 | 52 | 26... Rh8 | good | inaccuracy | precision | inaccuracy | 0.0589 | 0.759 | no | Bg4 | - | -1.41 | -1.33 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0434 | 0.544 | no | dxc6 | - | -0.08 | +0.01 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.503 | yes | Nf3 | - | -0.16 | +0.00 |
| 185209623352 | 14 | 7... Qd6 | inaccuracy | good | precision | good | 0.0448 | 0.475 | no | Bd7 | Bd7 | +1.28 | +1.24 |
| 185209623352 | 15 | 8. Bf4 | best | excellent | precision | excellent | 0.0017 | 0.570 | no | O-O | - | +1.28 | +1.30 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.790 | yes | Nxe4 | - | +5.09 | +5.84 |
| 185209623352 | 20 | 10... dxe4 | mistake | excellent | precision | excellent | 0.0107 | 0.211 | no | Bxe4 | - | +6.16 | +6.11 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0674 | 0.799 | no | Nxc6 | Nxc6 | +4.00 | +4.29 |
| 185209623352 | 23 | 12. Qxd4 | best | good | precision | good | 0.0320 | 0.740 | no | Bxc6 | - | +4.04 | +4.35 |
| 185209623352 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0080 | 0.272 | no | Rxd4 | - | +4.04 | +4.50 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0463 | 0.734 | no | O-O-O | O-O-O | +3.00 | +3.51 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0481 | 0.311 | no | e5 | - | +4.18 | +4.55 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.270 | yes | Kc7 | - | +4.76 | +4.70 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0498 | 0.743 | no | Nd8 | Nd8 | +3.29 | +3.61 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1932 | 0.716 | no | Bxe6 | - | +0.61 | +0.41 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.670 | yes | Rc5+ | - | +3.32 | +3.57 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.457 | yes | Nd3+ | - | +0.92 | +1.25 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.570 | yes | Nxd3 | Rxd3 | -0.61 | +1.12 |
| 185209623352 | 49 | 25. Rb5+ | excellent | best | precision | best | 0.0000 | 0.708 | yes | Rb5+ | - | +3.97 | +4.23 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0009 | 0.725 | no | Rd5 | - | +3.97 | +4.38 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0145 | 0.271 | no | Rd4 | - | +4.48 | +4.71 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.744 | yes | Kb2 | - | +4.39 | +4.62 |
| 185209623352 | 56 | 28... d2 | excellent | best | precision | best | 0.0000 | 0.260 | yes | d2 | - | +4.65 | +4.62 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0000 | 0.740 | no | Rh5 | - | +4.14 | +4.69 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0096 | 0.776 | no | Rh5 | - | +4.64 | +5.27 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0265 | 0.765 | no | Rh5 | - | +4.51 | +4.63 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.744 | yes | Kc2 | - | +4.38 | +4.42 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0453 | 0.688 | no | Kd3 | - | +2.98 | +2.37 |
| 185209623352 | 77 | 39. Kb1 | inaccuracy | good | precision | good | 0.0495 | 0.655 | no | g4 | g4 | +1.67 | +1.89 |
| 185209623352 | 78 | 39... Rb2+ | good | excellent | precision | excellent | 0.0166 | 0.395 | no | Rf2 | - | +2.15 | +2.12 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.618 | yes | Kc1 | - | +2.15 | +2.47 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0628 | 0.263 | no | Kd7 | - | +6.01 | +6.13 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1481 | 0.647 | no | Rhxe7 | Rhxe7 | -0.08 | -0.02 |
| 185209623352 | 87 | 44. f5+ | excellent | best | precision | best | 0.0000 | 0.497 | yes | f5+ | - | 0.00 | -0.07 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1837 | 0.504 | no | Kf7 | - | +3.73 | +3.51 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.689 | yes | Rf1+ | - | +3.73 | +3.39 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.751 | yes | Kxb2 | - | +5.17 | +5.28 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0177 | 0.233 | no | b5 | - | +5.65 | +5.73 |
| 185209623352 | 97 | 49. Kc2 | best | excellent | precision | excellent | 0.0052 | 0.797 | no | g4 | - | +5.89 | +6.02 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0108 | 0.204 | no | b5 | - | +6.38 | +6.32 |
| 185209623352 | 102 | 51... Kg6 | excellent | best | precision | best | 0.0000 | 0.197 | yes | Kg6 | - | +6.33 | +6.52 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0031 | 0.814 | no | Ra7 | - | +6.33 | +6.88 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0000 | 0.174 | no | Kg5 | - | +6.33 | +6.56 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0000 | 0.815 | no | Rb6 | - | +6.59 | +6.81 |
| 185209623352 | 108 | 54... Kh5 | excellent | best | precision | best | 0.0000 | 0.177 | yes | Kh5 | - | +6.70 | +7.34 |
| 185209623352 | 110 | 55... Kg6 | excellent | best | precision | best | 0.0000 | 0.167 | yes | Kg6 | - | +6.54 | +7.56 |
| 185209623352 | 111 | 56. Rbxe5 | best | good | precision | good | 0.0207 | 0.847 | no | Rb6 | - | +6.54 | +6.89 |
| 185209623352 | 112 | 56... Bxe5 | excellent | best | precision | best | 0.0000 | 0.174 | yes | Bxe5 | - | +6.75 | +7.05 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.115 | yes | Kf6 | - | +7.19 | +11.46 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Ke6 | Ke7 | +10.6 | M17 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | M14 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | - | M5 | M6 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Re8+ | - | M3 | M4 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | no | Ke5 | - | M2 | M2 |
| 185209623352 | 133 | 67. Re8+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kc3 | - | M2 | M5 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 141 | 71. g4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Kc1 | - | +10.4 | M14 |
| 185209623352 | 142 | 71... Kb5 | good | best | precision | best | 0.0000 | 0.000 | no | Ka7 | - | M8 | M12 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M8 |
| 185209623352 | 144 | 72... Ka5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Ka5 | - | M6 | M8 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb6 | - | M5 | M7 |
| 185209623352 | 153 | 77. Qc7 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qc7 | - | M3 | M3 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0043 | 0.294 | no | d4 | - | -4.03 | -4.04 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0338 | 0.604 | no | Ng3 | Ng3 | -0.98 | -1.05 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0833 | 0.583 | no | Na6 | - | +0.29 | +0.20 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.511 | yes | Qg1 | - | +0.29 | +0.12 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.670 | yes | Re1 | - | +3.07 | +2.85 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0277 | 0.343 | no | Qh5 | - | +3.38 | +3.59 |
| 185324357184 | 40 | 20... Be4 | inaccuracy | good | precision | good | 0.0496 | 0.308 | no | Qxg3 | Qxg3 | +4.45 | +4.61 |
| 185324357184 | 46 | 23... b5 | excellent | best | precision | best | 0.0000 | 0.484 | yes | b5 | - | +0.26 | +0.09 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.505 | no | b3 | - | +0.26 | +0.37 |
| 185324357184 | 52 | 26... a5 | good | excellent | precision | excellent | 0.0051 | 0.542 | no | a6 | - | -0.29 | -0.41 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.612 | yes | Nxe5 | - | +1.74 | +1.98 |
| 185437323918 | 10 | 5... Kf8 | good | excellent | precision | excellent | 0.0149 | 0.439 | no | Ke7 | - | +1.39 | +1.58 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0226 | 0.313 | no | d4 | - | -3.51 | -3.83 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0890 | 0.291 | no | d3 | d3 | -5.55 | -5.88 |
| 185437323918 | 17 | 9. Qd3 | excellent | best | precision | best | 0.0000 | 0.211 | yes | Qd3 | - | -5.63 | -5.90 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0065 | 0.798 | no | g4 | - | -5.16 | -5.60 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0367 | 0.796 | no | g4 | - | -4.94 | -5.01 |
| 185437323918 | 22 | 11... Bf5 | best | excellent | precision | excellent | 0.0034 | 0.763 | no | Nf5 | - | -4.94 | -5.22 |
| 185437323918 | 23 | 12. Qg3 | mistake | inaccuracy | precision | inaccuracy | 0.0541 | 0.228 | no | Qe3 | - | -6.88 | -6.96 |
| 185437323918 | 26 | 13... Nxg3+ | excellent | best | precision | best | 0.0000 | 0.847 | yes | Nxg3+ | - | -6.67 | -6.92 |
| 185437323918 | 28 | 14... g6 | good | excellent | precision | excellent | 0.0190 | 0.836 | no | Kg8 | - | -6.13 | -5.87 |
| 185437323918 | 34 | 17... Qe7 | best | good | precision | good | 0.0248 | 0.825 | no | Kg7 | - | -6.58 | -5.95 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.808 | no | Qe2 | - | -5.96 | -7.60 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0339 | 0.742 | no | Qf4 | - | -3.59 | -3.98 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0912 | 0.283 | no | hxg3 | hxg3 | -5.85 | -6.12 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0099 | 0.775 | no | e4 | - | -4.41 | -5.07 |
| 185437323918 | 53 | 27. h3 | excellent | best | precision | best | 0.0000 | 0.235 | no | Rb3 | - | -4.46 | -4.94 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0272 | 0.685 | no | Bc2 | - | -2.41 | -2.78 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.799 | yes | Be4 | - | -5.61 | -5.87 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0031 | 0.841 | no | Rf8 | - | -6.21 | -7.04 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0000 | 0.798 | no | Kf4 | - | -5.11 | -5.93 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | good | precision | good | 0.0286 | 0.201 | no | Kg2 | Kg2 | -6.13 | -6.74 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.186 | yes | Kf3 | - | -6.12 | -6.35 |
| 185437323918 | 74 | 37... Rf8+ | best | good | precision | good | 0.0209 | 0.815 | no | Bb4 | - | -6.12 | -5.78 |
| 185437323918 | 80 | 40... Kxg4 | best | excellent | precision | excellent | 0.0022 | 0.844 | no | Kg5 | - | -6.12 | -8.16 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0000 | 0.130 | no | Ke4 | - | -7.11 | -7.45 |
| 185437323918 | 83 | 42. Kd7 | excellent | good | precision | good | 0.0244 | 0.142 | no | d6 | - | -7.28 | -8.65 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0059 | 0.883 | no | Bg3 | - | -7.28 | -8.86 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.112 | yes | Kxc7 | - | -8.05 | -8.90 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.103 | no | Kc8 | - | -8.99 | -8.91 |
| 185437323918 | 91 | 46. Kxb7 | excellent | good | precision | good | 0.0280 | 0.081 | no | c6 | - | -9.64 | -9.58 |
| 185437323918 | 93 | 47. d7 | excellent | best | precision | best | 0.0000 | 0.070 | yes | d7 | - | -11.0 | -14.11 |
| 185437323918 | 94 | 47... Qb2+ | excellent | best | precision | best | 0.0000 | 0.964 | yes | Qb2+ | - | -9.07 | -M17 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kc6 | Ka6 | -M17 | -M18 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -M18 |
| 185437323918 | 98 | 49... Qb7+ | good | best | precision | best | 0.0000 | 1.000 | no | Qc7 | - | -8.99 | -M17 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kc4 | - | -10.7 | -13.60 |
| 185437323918 | 101 | 51. Ke6 | good | excellent | precision | excellent | 0.0145 | 0.051 | no | Kd4 | - | -M6 | -M14 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2035 | 0.203 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0184 | 0.509 | no | Nf3 | - | -0.01 | -0.16 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.509 | yes | h6 | - | -0.01 | -0.06 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.496 | yes | Bh4 | - | -0.01 | -0.17 |
| 185438707002 | 26 | 13... O-O-O | miss | inaccuracy | precision | inaccuracy | 0.0981 | 0.642 | no | Rg8 | Rg8 | -0.69 | -0.70 |
| 185438707002 | 27 | 14. Nf3 | best | excellent | precision | excellent | 0.0012 | 0.459 | no | Qd2 | - | -0.69 | -0.57 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.580 | yes | c3 | - | +1.35 | +1.45 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0654 | 0.415 | no | Bb6 | - | +2.65 | +2.62 |
| 185438707002 | 41 | 21. O-O-O | excellent | good | precision | good | 0.0366 | 0.735 | no | Qe2 | - | +3.58 | +3.54 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0204 | 0.722 | no | Rhf1 | - | +3.74 | +3.61 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0039 | 0.713 | no | Rd2 | - | +3.82 | +3.63 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0691 | 0.297 | no | Rg8 | - | +4.87 | +5.14 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.722 | yes | Qxd8+ | - | +3.69 | +4.10 |
| 185438707002 | 59 | 30. Qxh4 | excellent | good | precision | good | 0.0369 | 0.731 | no | Qd2 | - | +3.68 | +3.46 |
| 185438707002 | 65 | 33. Rd5 | excellent | good | precision | good | 0.0358 | 0.664 | no | Rd8 | - | +1.84 | +2.30 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | good | precision | good | 0.0308 | 0.367 | no | Qb3 | Qb3 | +2.60 | +2.87 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.706 | yes | Qb2+ | - | -3.65 | -4.08 |
| 185438707002 | 74 | 37... Qxd5 | excellent | best | precision | best | 0.0000 | 0.724 | yes | Qxd5 | - | -3.38 | -3.95 |
| 185438707002 | 75 | 38. Kg1 | best | excellent | precision | excellent | 0.0114 | 0.281 | no | f3 | - | -3.38 | -3.71 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0252 | 0.667 | no | Qc2 | - | -2.36 | -2.45 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0015 | 0.883 | no | e4 | - | -8.73 | -8.48 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.118 | yes | g4 | - | -8.80 | -8.25 |
| 185438707002 | 90 | 45... e3 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qf3 | - | -M6 | -M14 |
| 185438707002 | 91 | 46. Kh4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | g5 | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0616 | 0.413 | no | e6 | e6 | +1.09 | +0.96 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0000 | 0.648 | no | Nf3 | - | +0.96 | +0.97 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0113 | 0.339 | no | c5 | - | +1.01 | +1.07 |
| 185456088510 | 9 | 5. Nc3 | excellent | best | precision | best | 0.0000 | 0.664 | yes | Nc3 | - | +0.95 | +1.01 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0381 | 0.350 | no | Ne7 | Bg7 | +1.25 | +1.24 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0178 | 0.641 | no | d5 | - | +0.81 | +0.77 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0030 | 0.380 | no | Bg7 | - | +0.81 | +0.84 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.626 | yes | Ng3 | - | +0.65 | +0.70 |
| 185456088510 | 22 | 11... Bg7 | inaccuracy | good | precision | good | 0.0459 | 0.366 | no | h5 | h5 | +1.10 | +1.19 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.663 | yes | h5 | - | +1.12 | +1.14 |
| 185456088510 | 29 | 15. e5 | inaccuracy | mistake | precision | mistake | 0.1034 | 0.835 | no | Qe2 | Qe2 | +1.58 | +1.57 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.760 | yes | exd6 | - | +1.55 | +1.36 |
| 185456088510 | 34 | 17... Qe7 | miss | blunder | precision | blunder | 0.2428 | 0.426 | no | Bxe4 | Bxe4 | +1.83 | +2.35 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0449 | 0.833 | no | Nh4 | - | +1.72 | +2.06 |
| 185456088510 | 42 | 21... Bxa6 | best | excellent | precision | excellent | 0.0184 | 0.185 | no | Qd5 | - | +2.36 | +2.79 |
| 185456088510 | 48 | 24... Qc7 | excellent | best | precision | best | 0.0000 | 0.100 | yes | Qc7 | - | +3.01 | +3.64 |
| 185456088510 | 52 | 26... Rxd1+ | good | excellent | precision | excellent | 0.0076 | 0.185 | no | Nxe3 | - | +2.14 | +2.30 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.942 | yes | Nxe3 | - | -4.25 | -5.05 |
| 185456088510 | 57 | 29. Nd4 | mistake | excellent | precision | excellent | 0.0000 | 0.039 | no | Re1 | - | -4.77 | -4.85 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0017 | 0.440 | no | Na4 | - | -0.94 | -1.05 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0076 | 0.485 | no | Ne5 | - | +0.60 | +0.49 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0370 | 0.476 | no | Kf8 | - | +0.61 | +1.05 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | excellent | precision | excellent | 0.0114 | 0.429 | no | dxe5 | dxe5 | +1.53 | +1.62 |
| 185468039834 | 21 | 11. Qh5 | excellent | inaccuracy | precision | inaccuracy | 0.0816 | 0.593 | no | b4 | - | +1.48 | +1.61 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.576 | yes | c6 | - | -0.83 | -0.96 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.699 | yes | Rf8 | - | -3.36 | -3.39 |
| 185468039834 | 31 | 16. b4 | excellent | best | precision | best | 0.0000 | 0.312 | yes | b4 | - | -3.61 | -3.52 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0093 | 0.513 | no | b4 | - | +0.15 | +0.09 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.495 | yes | exd4 | - | +0.15 | +0.00 |
| 185468614210 | 11 | 6. cxd4 | book | best | precision | best | 0.0000 | 0.500 | yes | cxd4 | - | 0.00 | +0.01 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.499 | yes | Bb4+ | - | 0.00 | +0.11 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0181 | 0.506 | no | Bd2 | - | -0.35 | -0.31 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0468 | 0.478 | no | Nxe4 | Nxe4 | +1.21 | +1.18 |
| 185468614210 | 25 | 13. Bd3 | good | excellent | precision | excellent | 0.0192 | 0.483 | no | Bxd6 | - | -0.61 | -0.62 |
| 185468614210 | 26 | 13... Re8 | good | inaccuracy | precision | inaccuracy | 0.0513 | 0.536 | no | Nxd5 | - | +0.15 | +0.26 |
| 185468614210 | 31 | 16. Qxd5 | best | excellent | precision | excellent | 0.0029 | 0.517 | no | Ng5+ | - | +0.25 | +0.22 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0331 | 0.487 | no | Kg8 | Kg8 | +1.21 | +0.79 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0355 | 0.546 | no | Qh5+ | Qh5+ | +0.18 | +0.25 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.485 | yes | Kg8 | - | +0.18 | +0.14 |
| 185468614210 | 38 | 19... Qf6 | good | excellent | precision | excellent | 0.0140 | 0.522 | no | b6 | - | -0.09 | -0.13 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0121 | 0.549 | no | d4 | - | +0.74 | +0.66 |
| 185475865432 | 4 | 2... Bb7 | book | excellent | precision | excellent | 0.0023 | 0.462 | no | c5 | - | +0.74 | +0.74 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.543 | yes | Nc3 | - | +0.74 | +0.63 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.463 | yes | e6 | - | +0.74 | +0.60 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0035 | 0.469 | no | d5 | - | +0.55 | +0.66 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0934 | 0.560 | no | Ng3 | Ng3 | -0.76 | -0.57 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0034 | 0.411 | no | Qxd8+ | - | -1.49 | -1.60 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0428 | 0.626 | no | Qxd1 | Qxd1 | -1.24 | -1.40 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0180 | 0.419 | no | hxg3 | - | -1.52 | -1.68 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0017 | 0.589 | no | Qxd1 | - | -1.25 | -1.51 |
| 185475865432 | 33 | 17. Qxd8+ | good | excellent | precision | excellent | 0.0135 | 0.413 | no | Qe2 | - | -1.78 | -1.75 |
| 185475865432 | 34 | 17... Rxd8 | inaccuracy | good | precision | good | 0.0443 | 0.600 | no | Kxd8 | Kxd8 | -0.89 | -0.97 |
| 185475865432 | 37 | 19. Rad1 | excellent | best | precision | best | 0.0000 | 0.593 | yes | Rad1 | - | +1.50 | +1.60 |
| 185475865432 | 42 | 21... Bxb2 | best | excellent | precision | excellent | 0.0011 | 0.408 | no | Rb8 | - | +1.50 | +1.73 |
| 185475865432 | 44 | 22... Rc8 | excellent | best | precision | best | 0.0000 | 0.412 | yes | Rc8 | - | +1.57 | +1.64 |
| 185475865432 | 48 | 24... Be2 | inaccuracy | mistake | precision | mistake | 0.1046 | 0.412 | no | Rb8 | Rb8 | +3.18 | +3.48 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0658 | 0.629 | no | Qd4 | - | +0.50 | +0.40 |
| 185962590893 | 15 | 8. Nc4 | inaccuracy | good | precision | good | 0.0490 | 0.620 | no | Be2 | - | +0.40 | +0.45 |
| 185962590893 | 16 | 8... Ngf6 | inaccuracy | good | precision | good | 0.0339 | 0.429 | no | b5 | b5 | +0.82 | +0.72 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.413 | yes | e5 | - | +0.67 | +0.61 |
| 185962590893 | 19 | 10. Bd2 | good | excellent | precision | excellent | 0.0108 | 0.596 | no | Bh2 | - | +0.50 | +0.34 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.446 | yes | Be7 | - | +0.55 | +0.46 |
| 185962590893 | 23 | 12. Ne3 | inaccuracy | good | precision | good | 0.0419 | 0.642 | no | Ba5 | Ba5 | +0.66 | +0.65 |
| 185962590893 | 27 | 14. Nxe7+ | miss | inaccuracy | precision | inaccuracy | 0.0566 | 0.774 | no | Bh6 | Bh6 | +1.01 | +1.33 |
| 185962590893 | 29 | 15. Be3 | inaccuracy | mistake | precision | mistake | 0.1020 | 0.713 | no | g4 | g4 | +0.77 | +0.71 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0222 | 0.299 | no | Nf8 | Ne8 | +1.62 | +1.51 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0709 | 0.723 | no | Rxd8+ | Rxd8+ | +0.96 | +0.99 |
| 185962590893 | 35 | 18. g5 | best | excellent | precision | excellent | 0.0156 | 0.671 | no | Rxd7 | - | +0.96 | +0.71 |
| 185962590893 | 43 | 22. Bd2 | good | excellent | precision | excellent | 0.0088 | 0.647 | no | Qe2 | - | +0.86 | +0.91 |
| 185962590893 | 45 | 23. Qd3 | good | inaccuracy | precision | inaccuracy | 0.0510 | 0.670 | no | Qc3 | - | +0.71 | +0.65 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0182 | 0.398 | no | Nf4 | - | +0.86 | +0.77 |
| 185962590893 | 48 | 24... Nd7 | best | excellent | precision | excellent | 0.0101 | 0.352 | no | Nd4 | - | +0.86 | +0.80 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.634 | yes | Qe3 | Qf3 | +0.47 | +0.91 |
| 185962590893 | 52 | 26... Nd4 | mistake | good | precision | good | 0.0302 | 0.359 | no | Nf4 | Nf4 | +1.15 | +1.27 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2521 | 0.692 | no | f4 | - | -0.39 | -0.38 |
| 185962590893 | 62 | 31... exf4 | good | excellent | precision | excellent | 0.0111 | 0.529 | no | Kf7 | - | -0.08 | -0.03 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | b4 | - | 0.00 | +0.00 |
| 185962590893 | 67 | 34. h5 | best | excellent | precision | excellent | 0.0080 | 0.508 | no | Kc2 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | -0.01 |
| 185962590893 | 78 | 39... Qd1+ | best | excellent | precision | excellent | 0.0016 | 0.502 | no | g6 | - | 0.00 | +0.00 |

### `miss_detector` (7)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1383 | 0.658 | no | g4 | - | -0.01 | +0.12 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1759 | 0.800 | no | Rxf6+ | Rxf6+ | +2.74 | +2.66 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.4085 | 0.768 | no | Rxf6+ | - | -2.81 | -2.56 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2263 | 0.736 | no | Kg7 | - | -0.17 | -0.16 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | mistake | 0.1959 | 0.196 | no | Kd2 | - | -M1 | -M1 |
| 185468614210 | 7 | 4. c3 | mistake | miss (tactic) | miss_detector | mistake | 0.1258 | 0.582 | no | Nxe5 | Nxe5 | -0.88 | -0.75 |
| 185475865432 | 49 | 25. a6 | mistake | miss (brilliant) | miss_detector | mistake | 0.1018 | 0.692 | no | Rxe6 | Rxe6 | +1.47 | +1.57 |

### `blunder_softened` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2190 | 0.887 | no | Qxg2 | Qxg2 | -0.96 | -1.20 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2134 | 0.564 | no | Qxg3+ | Qxg3+ | +2.48 | +2.69 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | blunder_softened | blunder | 0.2048 | 0.629 | no | Nxc7+ | Nxc7+ | -0.91 | -1.32 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0078 | 0.459 | no | Nf6 | - | +0.82 | +0.78 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0571 | 0.527 | no | Nxe5 | Nxe5 | -0.62 | -0.52 |

### `mate_override` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M5 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.506 | yes | Bxe5 | - | +0.18 | +0.20 |
| 185438343298 | 15 | 8. g3 | best | great | great_find_event | best | 0.0000 | 0.205 | yes | g3 | - | -5.11 | -5.95 |

### `losing_material_hardened` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | good | 0.0344 | 0.076 | no | Kc8 | - | -8.94 | -8.44 |

