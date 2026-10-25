# Calibration report: depth-20

- Generated: 2026-10-18T07:47:08+00:00
- Commit: `2703019df381` + uncommitted backend changes (diff sha256 `fa559f3352d9`)
- Engine: Stockfish 17.1; depth 20, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 68.2% (584/856) |
| Within one step | 89.8% (769/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.60 / 0.12 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 0.58 |
| Accuracy mean abs. difference | 2.71 (n=28, max 8.58) |
| Accuracy bias (ours - app) | +2.57 |
| Best move = app's suggestion | 81.0% (111/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | 1 | . | . | . | . | . | 3 |
| **great** | . | **3** | 22 | 1 | . | . | . | . | . | . | 26 |
| **best** | . | 2 | **263** | 45 | 6 | . | . | . | . | . | 316 |
| **excellent** | . | . | 37 | **62** | 23 | 1 | 4 | . | . | . | 127 |
| **good** | . | . | 4 | 34 | **56** | . | 7 | 1 | 1 | . | 103 |
| **book** | . | . | 7 | 8 | 3 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 6 | 2 | 22 | 1 | **60** | 1 | . | . | 92 |
| **mistake** | . | . | . | 1 | 1 | . | 11 | **29** | 1 | 1 | 44 |
| **miss** | . | . | . | . | 1 | . | 3 | 5 | **17** | 1 | 27 |
| **blunder** | . | . | . | . | . | . | . | 4 | 3 | **14** | 21 |
| **total** | 1 | 5 | 340 | 153 | 113 | 81 | 85 | 40 | 22 | 16 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 5 | 3 | 0.600 | 0.115 | 0.194 |
| best | 316 | 340 | 263 | 0.774 | 0.832 | 0.802 |
| excellent | 127 | 153 | 62 | 0.405 | 0.488 | 0.443 |
| good | 103 | 113 | 56 | 0.496 | 0.544 | 0.519 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 85 | 60 | 0.706 | 0.652 | 0.678 |
| mistake | 44 | 40 | 29 | 0.725 | 0.659 | 0.690 |
| miss | 27 | 22 | 17 | 0.773 | 0.630 | 0.694 |
| blunder | 21 | 16 | 14 | 0.875 | 0.667 | 0.757 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 80.5 | +6.8 |
| 1034847688 | black | 65.0 | 73.6 | +8.6 |
| 1041474766 | white | 98.0 | 96.3 | -1.7 |
| 1041474766 | black | 83.8 | 85.2 | +1.4 |
| 184759554082 | white | 81.2 | 84.4 | +3.2 |
| 184759554082 | black | 87.7 | 88.7 | +1.0 |
| 185209623352 | white | 72.7 | 75.0 | +2.3 |
| 185209623352 | black | 72.6 | 73.2 | +0.6 |
| 185324357184 | white | 73.0 | 74.8 | +1.8 |
| 185324357184 | black | 62.4 | 63.7 | +1.3 |
| 185436488062 | white | 98.6 | 98.4 | -0.2 |
| 185436488062 | black | 38.5 | 42.4 | +3.9 |
| 185437323918 | white | 69.5 | 72.0 | +2.5 |
| 185437323918 | black | 75.7 | 77.8 | +2.1 |
| 185438343298 | white | 46.9 | 46.9 | +0.0 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 78.0 | +0.2 |
| 185438707002 | black | 83.0 | 83.8 | +0.8 |
| 185456088510 | white | 78.4 | 81.5 | +3.1 |
| 185456088510 | black | 82.2 | 85.4 | +3.2 |
| 185468039834 | white | 80.0 | 83.2 | +3.2 |
| 185468039834 | black | 87.5 | 90.2 | +2.7 |
| 185468614210 | white | 70.8 | 76.3 | +5.5 |
| 185468614210 | black | 77.1 | 81.6 | +4.5 |
| 185475865432 | white | 78.1 | 82.4 | +4.3 |
| 185475865432 | black | 66.1 | 72.4 | +6.3 |
| 185962590893 | white | 90.8 | 93.2 | +2.4 |
| 185962590893 | black | 90.9 | 93.3 | +2.4 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 61.2% | 79.6% | reviewed | 138.1 |
| 1041474766 | 25 | 25 | 80.0% | 80.0% | reviewed | 55.8 |
| 184759554082 | 62 | 62 | 72.6% | 87.1% | reviewed | 160.8 |
| 185209623352 | 155 | 155 | 57.4% | 89.7% | reviewed | 200.0 |
| 185324357184 | 55 | 55 | 81.8% | 94.5% | reviewed | 120.7 |
| 185436488062 | 13 | 13 | 92.3% | 92.3% | reviewed | 23.6 |
| 185437323918 | 108 | 103 | 57.3% | 90.3% | reviewed | 146.8 |
| 185438343298 | 20 | 20 | 95.0% | 95.0% | reviewed | 17.6 |
| 185438707002 | 95 | 91 | 67.0% | 91.2% | reviewed | 206.0 |
| 185456088510 | 60 | 60 | 66.7% | 90.0% | reviewed | 151.3 |
| 185468039834 | 38 | 38 | 65.8% | 94.7% | reviewed | 100.5 |
| 185468614210 | 54 | 54 | 75.9% | 87.0% | reviewed | 112.6 |
| 185475865432 | 53 | 53 | 71.7% | 90.6% | reviewed | 123.1 |
| 185962590893 | 78 | 78 | 76.9% | 93.6% | reviewed | 114.6 |

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
| `precision` | 255 | best -> excellent x45, excellent -> best x37, good -> excellent x34, excellent -> good x23, inaccuracy -> good x22, great -> best x22 |
| `mate_override` | 5 | excellent -> inaccuracy x2, good -> miss x1, best -> good x1, good -> inaccuracy x1 |
| `miss_detector` | 4 | blunder -> miss x3, mistake -> miss x1 |
| `blunder_softened` | 3 | miss -> mistake x3 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `great_find_event` | 2 | best -> great x2 |
| `losing_material_hardened` | 1 | good -> mistake x1 |

### `precision` (255)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 10 | 5... O-O | excellent | best | precision | best | 0.0000 | 0.545 | yes | O-O | - | -0.50 | -0.39 |
| 1034847688 | 12 | 6... c5 | inaccuracy | good | precision | good | 0.0495 | 0.562 | no | e5 | e5 | -0.10 | -0.13 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0047 | 0.488 | no | Be2 | - | -0.10 | -0.33 |
| 1034847688 | 14 | 7... Nc6 | good | inaccuracy | precision | inaccuracy | 0.0554 | 0.531 | no | cxd4 | - | +0.28 | +0.26 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0301 | 0.521 | no | Be2 | - | +0.12 | -0.10 |
| 1034847688 | 19 | 10. h4 | good | excellent | precision | excellent | 0.0178 | 0.528 | no | Bd3 | - | +0.11 | +0.11 |
| 1034847688 | 22 | 11... a5 | mistake | inaccuracy | precision | inaccuracy | 0.0880 | 0.470 | no | Nbd7 | Nbd7 | +1.29 | +1.28 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0824 | 0.618 | no | cxb5 | cxb5 | +0.44 | +0.20 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.476 | yes | h6 | - | +0.90 | +0.49 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0769 | 0.556 | no | a4 | Qd7 | +0.53 | +0.22 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.528 | yes | Nxf3 | - | -0.10 | -0.46 |
| 1034847688 | 40 | 20... Nf5 | inaccuracy | excellent | precision | excellent | 0.0038 | 0.504 | no | Nh5 | f5 | +0.50 | +0.30 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.528 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.52 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.578 | yes | exf7+ | - | +0.09 | +0.82 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.423 | yes | Kxf7 | Rxf7 | +0.92 | +1.70 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0310 | 0.563 | no | d4 | - | +0.37 | +0.36 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0018 | 0.468 | no | Nc6 | - | +0.38 | +0.33 |
| 1041474766 | 9 | 5. Bg2 | book | excellent | precision | excellent | 0.0018 | 0.529 | no | Nf3 | - | +0.34 | +0.35 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0107 | 0.469 | no | e5 | - | +0.59 | +0.47 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0321 | 0.542 | no | Nf3 | - | +0.17 | +0.11 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0398 | 0.529 | no | d5 | - | +0.08 | +0.07 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0016 | 0.468 | no | Nc3 | - | -0.25 | -0.21 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0286 | 0.500 | no | Nxh5 | - | +0.03 | +0.18 |
| 184759554082 | 15 | 8. hxg6 | good | inaccuracy | precision | inaccuracy | 0.0525 | 0.529 | no | Nc3 | - | -0.21 | -0.15 |
| 184759554082 | 17 | 9. Nf3 | good | inaccuracy | precision | inaccuracy | 0.0651 | 0.513 | no | Nc3 | - | -0.39 | -0.33 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.582 | yes | d5 | - | -0.52 | -0.54 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1667 | 0.415 | no | cxd5 | cxd5 | -1.98 | -2.40 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.828 | yes | Qxg5 | - | -1.98 | -2.64 |
| 184759554082 | 32 | 16... b6 | best | good | precision | good | 0.0285 | 0.677 | no | b5 | - | -0.96 | -1.06 |
| 184759554082 | 34 | 17... Qg5 | excellent | good | precision | good | 0.0331 | 0.671 | no | Bf5 | - | -0.88 | -1.02 |
| 184759554082 | 37 | 19. Kb1 | good | excellent | precision | excellent | 0.0027 | 0.311 | no | Qb2 | - | -1.19 | -1.25 |
| 184759554082 | 38 | 19... Bf5 | excellent | inaccuracy | precision | inaccuracy | 0.0720 | 0.689 | no | Rh8 | - | -1.10 | -0.75 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.708 | yes | Re6 | - | -1.31 | -1.51 |
| 184759554082 | 47 | 24. Ka1 | best | good | precision | good | 0.0254 | 0.288 | no | b4 | - | -1.28 | -1.48 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.720 | yes | a5 | - | -1.16 | -1.39 |
| 184759554082 | 49 | 25. a4 | inaccuracy | good | precision | good | 0.0355 | 0.292 | no | f4 | f3 | -1.61 | -1.74 |
| 185209623352 | 7 | 4. d4 | best | excellent | precision | excellent | 0.0051 | 0.507 | no | Nf3 | - | -0.08 | +0.00 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.502 | yes | Nf3 | - | -0.16 | -0.15 |
| 185209623352 | 15 | 8. Bf4 | best | excellent | precision | excellent | 0.0022 | 0.575 | no | Qf3 | - | +1.28 | +1.26 |
| 185209623352 | 17 | 9. Qd2 | inaccuracy | good | precision | good | 0.0381 | 0.687 | no | Bxc6 | Bxc6 | +2.14 | +2.58 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.792 | yes | Nxe4 | - | +5.09 | +5.70 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0634 | 0.793 | no | Nxc6 | Nxc6 | +4.00 | +4.30 |
| 185209623352 | 22 | 11... Qxd4 | excellent | good | precision | good | 0.0223 | 0.275 | no | Qd5 | - | +4.04 | +4.68 |
| 185209623352 | 23 | 12. Qxd4 | best | good | precision | good | 0.0227 | 0.742 | no | Bxc6 | - | +4.04 | +4.52 |
| 185209623352 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0176 | 0.265 | no | Rxd4 | - | +4.04 | +4.87 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0447 | 0.750 | no | O-O-O | O-O-O | +3.00 | +3.77 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0334 | 0.299 | no | b5 | - | +4.18 | +4.50 |
| 185209623352 | 34 | 17... Kc7 | good | excellent | precision | excellent | 0.0119 | 0.258 | no | Kb8 | - | +4.76 | +4.81 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0478 | 0.748 | no | Nd8 | Nd8 | +3.29 | +3.75 |
| 185209623352 | 40 | 20... Rd8 | inaccuracy | good | precision | good | 0.0428 | 0.323 | no | b6 | - | +3.82 | +4.17 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1981 | 0.720 | no | Bxe6 | - | +0.61 | +0.38 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.681 | yes | Rc5+ | - | +3.32 | +3.44 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.440 | yes | Nd3+ | - | +0.92 | +1.23 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.569 | yes | Nxd3 | Rxd3 | -0.61 | +0.78 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0031 | 0.270 | no | Ka6 | - | +3.97 | +4.31 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0121 | 0.734 | no | Rd5 | - | +3.97 | +4.35 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0084 | 0.272 | no | Bc3 | - | +4.48 | +4.78 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.747 | yes | Kb2 | - | +4.39 | +4.74 |
| 185209623352 | 56 | 28... d2 | excellent | best | precision | best | 0.0000 | 0.255 | yes | d2 | - | +4.65 | +4.76 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0000 | 0.746 | no | Rc5+ | - | +4.14 | +4.79 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0106 | 0.782 | no | Rh5 | - | +4.64 | +5.37 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0266 | 0.764 | no | Rh5 | - | +4.51 | +4.50 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0210 | 0.283 | no | Kf5 | - | +4.38 | +4.43 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.731 | yes | Kc2 | - | +4.38 | +4.55 |
| 185209623352 | 70 | 35... Rxc4 | excellent | best | precision | best | 0.0000 | 0.262 | yes | Rxc4 | - | +4.77 | +4.73 |
| 185209623352 | 73 | 37. Kc2 | inaccuracy | good | precision | good | 0.0486 | 0.721 | no | Ke3 | - | +3.00 | +3.19 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0213 | 0.670 | no | Kd3 | - | +2.98 | +2.47 |
| 185209623352 | 78 | 39... Rb2+ | good | excellent | precision | excellent | 0.0065 | 0.396 | no | Rf2 | - | +2.15 | +2.25 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.624 | yes | Kc1 | - | +2.15 | +2.20 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0904 | 0.270 | no | Kd5 | - | +6.01 | +6.72 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1515 | 0.652 | no | Rhxe7 | Rhxe7 | -0.08 | -0.10 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1963 | 0.501 | no | Kf7 | - | +3.73 | +3.64 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.695 | yes | Rf1+ | - | +3.73 | +3.95 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.767 | yes | Kxb2 | - | +5.17 | +5.53 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0039 | 0.223 | no | Bxf4 | - | +5.65 | +5.58 |
| 185209623352 | 97 | 49. Kc2 | best | excellent | precision | excellent | 0.0018 | 0.800 | no | Kb3 | - | +5.89 | +6.32 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0070 | 0.193 | no | Bg7 | - | +6.38 | +6.52 |
| 185209623352 | 100 | 50... b5 | best | excellent | precision | excellent | 0.0017 | 0.183 | no | Bd8 | - | +6.38 | +6.67 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0010 | 0.814 | no | Rc7 | - | +6.33 | +7.06 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0031 | 0.169 | no | Bd8 | - | +6.33 | +6.67 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.819 | yes | R7xb5 | - | +6.30 | +6.94 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0000 | 0.839 | no | Rb6 | - | +6.59 | +7.38 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0065 | 0.848 | no | Rb6 | - | +6.54 | +8.26 |
| 185209623352 | 112 | 56... Bxe5 | excellent | best | precision | best | 0.0000 | 0.134 | yes | Bxe5 | - | +6.75 | +6.61 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.122 | yes | Kf6 | - | +7.19 | +12.72 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | no | Kf7 | Ke7 | +10.6 | M16 |
| 185209623352 | 117 | 59. h5 | good | best | precision | best | 0.0000 | 1.000 | yes | h5 | - | +8.42 | +13.63 |
| 185209623352 | 119 | 60. h6 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg4 | - | M9 | M11 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | M13 |
| 185209623352 | 123 | 62. Rg8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rh4 | - | M7 | M8 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | - | M5 | M6 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg5 | - | M3 | M6 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 141 | 71. g4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Kb1 | - | +10.4 | M14 |
| 185209623352 | 142 | 71... Kb5 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Ka7 | - | M8 | M10 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M9 |
| 185324357184 | 6 | 3... Bc5 | blunder | mistake | precision | mistake | 0.1895 | 0.514 | no | d5 | - | +3.27 | +3.21 |
| 185324357184 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0011 | 0.546 | no | O-O | - | -1.29 | -0.89 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0103 | 0.294 | no | d4 | - | -4.03 | -4.16 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0788 | 0.579 | no | Na6 | - | +0.29 | +0.23 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.513 | yes | Qg1 | - | +0.29 | +0.21 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.674 | yes | Re1 | - | +3.07 | +2.91 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0286 | 0.339 | no | Qh5 | - | +3.38 | +3.55 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0006 | 0.501 | no | Rh2 | - | +0.11 | +0.00 |
| 185324357184 | 45 | 23. Re7 | best | excellent | precision | excellent | 0.0006 | 0.509 | no | Re3 | - | +0.19 | +0.10 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.616 | yes | Nxe5 | - | +1.74 | +2.03 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0257 | 0.308 | no | d4 | - | -3.51 | -4.01 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0940 | 0.295 | no | c3 | d3 | -5.55 | -5.91 |
| 185437323918 | 18 | 9... Nxd5 | good | best | precision | best | 0.0000 | 0.795 | yes | Nxd5 | - | -5.16 | -5.63 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0391 | 0.793 | no | Qe8 | - | -4.94 | -4.80 |
| 185437323918 | 22 | 11... Bf5 | best | excellent | precision | excellent | 0.0051 | 0.765 | no | Nf5 | - | -4.94 | -5.49 |
| 185437323918 | 23 | 12. Qg3 | mistake | inaccuracy | precision | inaccuracy | 0.0603 | 0.218 | no | Qe3 | - | -6.88 | -7.18 |
| 185437323918 | 26 | 13... Nxg3+ | excellent | best | precision | best | 0.0000 | 0.846 | yes | Nxg3+ | - | -6.67 | -6.91 |
| 185437323918 | 31 | 16. Nd2 | excellent | best | precision | best | 0.0000 | 0.192 | yes | Nd2 | - | -6.16 | -6.27 |
| 185437323918 | 32 | 16... dxc3 | excellent | best | precision | best | 0.0000 | 0.812 | yes | dxc3 | - | -5.87 | -6.46 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0053 | 0.843 | no | Rxh2+ | - | -6.58 | -7.05 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.804 | no | Qe2 | - | -5.96 | -7.91 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0475 | 0.760 | no | Qf4 | - | -3.59 | -4.07 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0877 | 0.279 | no | hxg3 | hxg3 | -5.85 | -6.18 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0033 | 0.775 | no | b6 | - | -4.41 | -5.22 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0211 | 0.680 | no | Bc2 | - | -2.41 | -2.88 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.816 | yes | Be4 | - | -5.61 | -6.70 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0089 | 0.849 | no | Rf8 | - | -6.21 | -7.05 |
| 185437323918 | 65 | 33. Rg3+ | excellent | best | precision | best | 0.0000 | 0.210 | yes | Rg3+ | - | -5.91 | -6.21 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0000 | 0.810 | no | Kf4 | - | -5.11 | -6.34 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | good | precision | good | 0.0225 | 0.186 | no | Kg2 | Kg2 | -6.13 | -6.78 |
| 185437323918 | 69 | 35. Rg4+ | good | excellent | precision | excellent | 0.0188 | 0.224 | no | d6 | - | -5.79 | -5.81 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.185 | yes | Kf3 | - | -6.12 | -6.27 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0000 | 0.812 | no | Bb4 | - | -6.12 | -6.56 |
| 185437323918 | 75 | 38. Ke4 | best | good | precision | good | 0.0307 | 0.178 | no | Ke2 | - | -6.12 | -6.51 |
| 185437323918 | 76 | 38... Rf4+ | best | excellent | precision | excellent | 0.0084 | 0.820 | no | Bc3 | - | -6.12 | -6.95 |
| 185437323918 | 80 | 40... Kxg4 | best | excellent | precision | excellent | 0.0107 | 0.860 | no | Kh4 | - | -6.12 | -7.59 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0115 | 0.146 | no | c5 | - | -7.11 | -8.15 |
| 185437323918 | 83 | 42. Kd7 | excellent | best | precision | best | 0.0000 | 0.106 | yes | Kd7 | - | -7.28 | -9.58 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0139 | 0.903 | no | Bg3 | - | -7.28 | -9.89 |
| 185437323918 | 85 | 43. Kxc7 | good | excellent | precision | excellent | 0.0079 | 0.091 | no | Kc8 | - | -8.05 | -10.32 |
| 185437323918 | 88 | 44... Bg3 | excellent | good | precision | good | 0.0226 | 0.919 | no | Ba5+ | - | -8.13 | -10.61 |
| 185437323918 | 89 | 45. c5 | excellent | good | precision | good | 0.0482 | 0.078 | no | Kd7 | - | -8.94 | -9.87 |
| 185437323918 | 91 | 46. Kxb7 | excellent | best | precision | best | 0.0000 | 0.065 | yes | Kxb7 | - | -9.64 | -10.93 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kc6 | Ka6 | -M17 | -M20 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -M18 |
| 185437323918 | 98 | 49... Qb7+ | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qe5+ | - | -8.99 | -M15 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.000 | yes | c6 | - | -10.7 | -M16 |
| 185437323918 | 102 | 51... Qe5+ | excellent | best | precision | best | 0.0000 | 1.000 | no | Qxc6+ | - | -M7 | -M12 |
| 185437323918 | 105 | 53. Ke7 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kg7 | - | -M3 | -M5 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0030 | 0.509 | no | Nf3 | - | -0.01 | +0.10 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.494 | yes | h6 | - | -0.01 | +0.07 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.504 | yes | Bh4 | - | -0.01 | +0.02 |
| 185438707002 | 12 | 6... g5 | good | excellent | precision | excellent | 0.0113 | 0.499 | no | a5 | - | +0.33 | +0.21 |
| 185438707002 | 19 | 10. Nf3 | excellent | best | precision | best | 0.0000 | 0.482 | yes | Nf3 | - | -0.52 | -0.54 |
| 185438707002 | 27 | 14. Nf3 | best | excellent | precision | excellent | 0.0029 | 0.464 | no | Na4 | - | -0.69 | -0.60 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.597 | yes | c3 | - | +1.35 | +1.60 |
| 185438707002 | 34 | 17... Bc5 | mistake | good | precision | good | 0.0498 | 0.406 | no | Bb6 | - | +2.65 | +2.49 |
| 185438707002 | 41 | 21. O-O-O | excellent | good | precision | good | 0.0301 | 0.735 | no | O-O | - | +3.58 | +3.66 |
| 185438707002 | 42 | 21... Nb6 | good | excellent | precision | excellent | 0.0179 | 0.296 | no | c4 | - | +3.99 | +4.03 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0224 | 0.722 | no | Qe2 | - | +3.74 | +3.57 |
| 185438707002 | 44 | 22... cxd4 | excellent | good | precision | good | 0.0224 | 0.300 | no | Nc4 | - | +4.01 | +4.17 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.729 | yes | Rxd4 | - | +3.82 | +3.71 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0034 | 0.713 | no | Rd2 | - | +3.82 | +3.56 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0675 | 0.301 | no | Rg8 | - | +4.87 | +5.02 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0394 | 0.767 | no | Qf6 | Qf6 | +3.70 | +4.14 |
| 185438707002 | 51 | 26. Rhd1 | excellent | good | precision | good | 0.0308 | 0.732 | no | Qf6 | - | +3.49 | +3.92 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.283 | yes | a6 | - | +3.78 | +3.79 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.724 | yes | Qxd8+ | - | +3.69 | +4.02 |
| 185438707002 | 63 | 32. b4 | good | excellent | precision | excellent | 0.0070 | 0.660 | no | Rd2 | - | +1.87 | +2.19 |
| 185438707002 | 65 | 33. Rd5 | excellent | good | precision | good | 0.0244 | 0.659 | no | Rd8 | - | +1.84 | +2.47 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | good | precision | good | 0.0367 | 0.358 | no | c6 | Qb3 | +2.60 | +3.16 |
| 185438707002 | 68 | 34... Qb2+ | great | excellent | precision | excellent | 0.0134 | 0.727 | no | Qa2+ | - | -3.65 | -3.99 |
| 185438707002 | 75 | 38. Kg1 | best | excellent | precision | excellent | 0.0105 | 0.282 | no | f3 | - | -3.38 | -3.86 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0378 | 0.687 | no | Qe2 | - | -2.36 | -2.60 |
| 185438707002 | 79 | 40. h4 | best | excellent | precision | excellent | 0.0065 | 0.351 | no | Qg7 | - | -2.36 | -2.89 |
| 185438707002 | 85 | 43. fxg3 | good | inaccuracy | precision | inaccuracy | 0.0933 | 0.145 | no | Kxg3 | - | -8.73 | -12.24 |
| 185438707002 | 86 | 43... Qf7 | best | good | precision | good | 0.0276 | 0.948 | no | Qe6+ | - | -8.73 | -10.32 |
| 185438707002 | 91 | 46. Kh4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | g5 | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0623 | 0.403 | no | e6 | e6 | +1.09 | +1.04 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0130 | 0.660 | no | Nf3 | - | +0.96 | +0.95 |
| 185456088510 | 6 | 3... e6 | excellent | good | precision | good | 0.0243 | 0.353 | no | d6 | - | +1.01 | +1.12 |
| 185456088510 | 9 | 5. Nc3 | excellent | good | precision | good | 0.0255 | 0.678 | no | c4 | - | +0.95 | +0.99 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0415 | 0.362 | no | Nc6 | Bg7 | +1.25 | +1.18 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0148 | 0.641 | no | d5 | - | +0.81 | +0.73 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.608 | yes | Ng3 | - | +0.65 | +0.72 |
| 185456088510 | 20 | 10... Ng4 | excellent | good | precision | good | 0.0224 | 0.387 | no | h5 | - | +0.74 | +0.93 |
| 185456088510 | 22 | 11... Bg7 | inaccuracy | good | precision | good | 0.0344 | 0.359 | no | c5 | h5 | +1.10 | +1.23 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.680 | yes | h5 | - | +1.12 | +1.19 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.768 | yes | exd6 | - | +1.55 | +1.25 |
| 185456088510 | 34 | 17... Qe7 | miss | blunder | precision | blunder | 0.2407 | 0.413 | no | Bxe4 | Bxe4 | +1.83 | +2.46 |
| 185456088510 | 35 | 18. Qe2 | best | excellent | precision | excellent | 0.0102 | 0.827 | no | Nh4 | - | +1.83 | +2.06 |
| 185456088510 | 37 | 19. dxc5 | excellent | inaccuracy | precision | inaccuracy | 0.0532 | 0.813 | no | d5 | - | +1.72 | +2.26 |
| 185456088510 | 40 | 20... Qxc5 | inaccuracy | good | precision | good | 0.0493 | 0.208 | no | bxc5 | bxc5 | +2.36 | +2.55 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0764 | 0.159 | no | Rd6 | - | +2.89 | +3.77 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0119 | 0.917 | no | a5 | - | +2.89 | +3.54 |
| 185456088510 | 50 | 25... Rf6 | inaccuracy | good | precision | good | 0.0473 | 0.173 | no | Nxe3 | Nxe3 | +2.84 | +3.25 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.960 | yes | Nxe3 | - | -4.25 | -5.01 |
| 185456088510 | 57 | 29. Nd4 | mistake | excellent | precision | excellent | 0.0140 | 0.039 | no | a5 | - | -4.77 | -5.72 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0110 | 0.457 | no | Na4 | - | -0.94 | -1.12 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0151 | 0.488 | no | Bg4 | - | +0.60 | +0.46 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0266 | 0.469 | no | Kf8 | - | +0.61 | +0.99 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0466 | 0.448 | no | dxe5 | dxe5 | +1.53 | +1.72 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.599 | yes | Qh5 | - | +1.48 | +1.53 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1966 | 0.622 | no | Nxc7+ | Nxc7+ | -0.91 | -1.30 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.575 | yes | c6 | - | -0.83 | -1.19 |
| 185468039834 | 27 | 14. Bxe6 | best | excellent | precision | excellent | 0.0192 | 0.423 | no | Bb3 | - | -1.28 | -1.59 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.702 | yes | Rf8 | - | -3.36 | -3.59 |
| 185468039834 | 31 | 16. b4 | excellent | best | precision | best | 0.0000 | 0.302 | yes | b4 | - | -3.61 | -3.57 |
| 185468039834 | 32 | 16... Rxf6 | excellent | best | precision | best | 0.0000 | 0.697 | yes | Rxf6 | - | -3.39 | -3.36 |
| 185468039834 | 36 | 18... a5 | good | excellent | precision | excellent | 0.0184 | 0.699 | no | d3 | - | -2.75 | -3.24 |
| 185468039834 | 37 | 19. bxa5 | best | excellent | precision | excellent | 0.0030 | 0.320 | no | g4 | - | -2.75 | -2.83 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0093 | 0.515 | no | d3 | - | +0.15 | +0.04 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.498 | yes | exd4 | - | +0.15 | +0.06 |
| 185468614210 | 11 | 6. cxd4 | book | excellent | precision | excellent | 0.0018 | 0.504 | no | e5 | - | 0.00 | -0.11 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.506 | yes | Bb4+ | - | 0.00 | +0.04 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0175 | 0.502 | no | Bd2 | - | -0.35 | -0.39 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0496 | 0.471 | no | Nxe4 | Nxe4 | +1.21 | +1.36 |
| 185468614210 | 28 | 14... Nxd5 | excellent | best | precision | best | 0.0000 | 0.487 | yes | Nxd5 | - | +0.25 | +0.18 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0401 | 0.496 | no | Kg8 | Kg8 | +1.21 | +0.75 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0326 | 0.544 | no | Qh5+ | Qh5+ | +0.18 | +0.15 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.491 | yes | Kg8 | - | +0.18 | +0.10 |
| 185468614210 | 38 | 19... Qf6 | good | excellent | precision | excellent | 0.0111 | 0.516 | no | b6 | - | -0.09 | -0.09 |
| 185468614210 | 48 | 24... Rxc3 | best | excellent | precision | excellent | 0.0076 | 0.504 | no | g6 | - | +0.14 | +0.00 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0138 | 0.553 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.460 | yes | Bb7 | - | +0.74 | +0.58 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.534 | yes | Nc3 | - | +0.74 | +0.68 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.460 | yes | e6 | - | +0.74 | +0.68 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0133 | 0.469 | no | d5 | - | +0.55 | +0.77 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0195 | 0.572 | no | e5 | - | +0.82 | +0.91 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0946 | 0.555 | no | Ng3 | Ng3 | -0.76 | -0.69 |
| 185475865432 | 23 | 12. Bf4 | inaccuracy | good | precision | good | 0.0408 | 0.463 | no | Qxd8+ | - | -1.49 | -1.34 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0197 | 0.421 | no | Ned4 | - | -1.49 | -1.71 |
| 185475865432 | 27 | 14. Ng3 | inaccuracy | good | precision | good | 0.0480 | 0.439 | no | Qxd8+ | Qxd8+ | -1.91 | -1.91 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | excellent | precision | excellent | 0.0190 | 0.609 | no | Qxd1 | Qxd1 | -1.24 | -1.37 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0124 | 0.421 | no | hxg3 | - | -1.52 | -1.62 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0022 | 0.595 | no | Bd6 | - | -1.25 | -1.58 |
| 185475865432 | 33 | 17. Qxd8+ | good | excellent | precision | excellent | 0.0179 | 0.409 | no | Qe2 | - | -1.78 | -1.90 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0635 | 0.693 | no | Rxe6 | Rxe6 | +1.47 | +2.28 |
| 185962590893 | 14 | 7... Nd7 | best | excellent | precision | excellent | 0.0045 | 0.390 | no | Nf6 | - | +0.82 | +0.82 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.421 | yes | e5 | - | +0.67 | +0.55 |
| 185962590893 | 19 | 10. Bd2 | good | excellent | precision | excellent | 0.0077 | 0.587 | no | Bg5 | - | +0.50 | +0.48 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.424 | yes | Be7 | - | +0.55 | +0.46 |
| 185962590893 | 22 | 11... b5 | inaccuracy | mistake | precision | mistake | 0.1019 | 0.434 | no | O-O | O-O | +0.92 | +1.10 |
| 185962590893 | 27 | 14. Nxe7+ | miss | good | precision | good | 0.0470 | 0.759 | no | Bh6 | Bh6 | +1.01 | +1.36 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0456 | 0.311 | no | Nf8 | Ne8 | +1.62 | +1.60 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0779 | 0.735 | no | Rxd8+ | Rxd8+ | +0.96 | +1.02 |
| 185962590893 | 40 | 20... Nfd7 | best | excellent | precision | excellent | 0.0116 | 0.359 | no | Ne8 | - | +0.96 | +1.11 |
| 185962590893 | 44 | 22... Ne6 | excellent | best | precision | best | 0.0000 | 0.366 | yes | Ne6 | - | +0.92 | +0.92 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.629 | yes | Qe3 | Qf3 | +0.47 | +0.70 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0657 | 0.390 | no | Nf4 | Nf4 | +1.15 | +1.27 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2443 | 0.692 | no | f4 | - | -0.39 | -0.33 |
| 185962590893 | 59 | 30. Bxe6 | great | best | precision | best | 0.0000 | 0.471 | yes | Bxe6 | - | -0.23 | -0.17 |
| 185962590893 | 62 | 31... exf4 | good | excellent | precision | excellent | 0.0064 | 0.506 | no | Kf7 | - | -0.08 | +0.00 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | a5 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | -0.01 |
| 185962590893 | 78 | 39... Qd1+ | best | excellent | precision | excellent | 0.0016 | 0.502 | no | g6 | - | 0.00 | +0.00 |

### `mate_override` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M6 |
| 185209623352 | 133 | 67. Re8+ | best | good | mate_override | good | 0.0000 | 1.000 | no | Kc3 | - | M2 | M5 |
| 185437323918 | 93 | 47. d7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0658 | 0.066 | no | Kc6 | - | -11.0 | -M18 |
| 185437323918 | 101 | 51. Ke6 | good | inaccuracy | mate_override | inaccuracy | 0.0430 | 0.043 | no | Kd4 | - | -M6 | -M13 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |

### `miss_detector` (4)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1250 | 0.660 | no | g4 | - | -0.01 | +0.16 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1749 | 0.820 | no | Rxf6+ | Rxf6+ | +2.74 | +2.76 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.4694 | 0.789 | no | Rxf6+ | - | -2.81 | -3.34 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2000 | 0.200 | no | Kd2 | - | -M1 | -M1 |

### `blunder_softened` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 30 | 15... Nh5 | miss | mistake | blunder_softened | blunder | 0.2778 | 0.618 | no | a4 | a4 | +1.64 | +1.76 |
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2617 | 0.911 | no | Qxg2 | Qxg2 | -0.96 | -0.88 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2064 | 0.561 | no | Qxg3+ | Qxg3+ | +2.48 | +2.61 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0163 | 0.464 | no | Nf6 | - | +0.82 | +0.85 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0583 | 0.526 | no | Nxe5 | Nxe5 | -0.62 | -0.56 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.511 | yes | Bxe5 | - | +0.18 | +0.24 |
| 185438707002 | 84 | 42... Nxg3 | best | great | great_find_event | best | 0.0000 | 0.850 | yes | Nxg3 | - | -7.11 | -7.47 |

### `losing_material_hardened` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 59 | 30. g5+ | good | mistake | losing_material_hardened | good | 0.0362 | 0.173 | no | Kg2 | - | -6.55 | -7.89 |

