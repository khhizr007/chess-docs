# Calibration report: b2-h4

- Generated: 2026-10-18T11:10:31+00:00
- Commit: `27fafb5b0f3b` + uncommitted backend changes (diff sha256 `78d53b3a9776`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: `{"material_horizon_plies":4}`
- Games: 41 requested, 41 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 2842 aligned, 2833 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 67.4% (1909/2833) |
| Within one step | 89.6% (2537/2833) |
| Brilliant precision / recall | 0.50 / 0.25 |
| Great precision / recall | 0.58 / 0.09 |
| Brilliant per 100 moves (app / ours) | 0.14 / 0.07 |
| Great per 100 moves (app / ours) | 2.72 / 0.42 |
| Accuracy mean abs. difference | 3.66 (n=82, max 9.24) |
| Accuracy bias (ours - app) | +3.44 |
| Best move = app's suggestion | 78.0% (336/431 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | 1 | 1 | . | . | . | . | . | 4 |
| **great** | . | **7** | 66 | 2 | 1 | 1 | . | . | . | . | 77 |
| **best** | 1 | 5 | **803** | 128 | 20 | 1 | 5 | . | . | . | 963 |
| **excellent** | . | . | 141 | **296** | 86 | 3 | 7 | 4 | . | . | 537 |
| **good** | . | . | 26 | 108 | **197** | 2 | 38 | 3 | 1 | . | 375 |
| **book** | . | . | 24 | 15 | 10 | **246** | 1 | . | . | . | 296 |
| **inaccuracy** | . | . | 13 | 15 | 64 | 4 | **161** | 17 | 1 | . | 275 |
| **mistake** | . | . | 3 | 3 | 13 | 1 | 29 | **119** | 7 | 7 | 182 |
| **miss** | . | . | . | . | 5 | . | 11 | 10 | **46** | 3 | 75 |
| **blunder** | . | . | . | . | . | . | . | 10 | 6 | **33** | 49 |
| **total** | 2 | 12 | 1077 | 568 | 397 | 258 | 252 | 163 | 61 | 43 | 2833 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 4 | 2 | 1 | 0.500 | 0.250 | 0.333 |
| great | 77 | 12 | 7 | 0.583 | 0.091 | 0.157 |
| best | 963 | 1077 | 803 | 0.746 | 0.834 | 0.787 |
| excellent | 537 | 568 | 296 | 0.521 | 0.551 | 0.536 |
| good | 375 | 397 | 197 | 0.496 | 0.525 | 0.510 |
| book | 296 | 258 | 246 | 0.953 | 0.831 | 0.888 |
| inaccuracy | 275 | 252 | 161 | 0.639 | 0.585 | 0.611 |
| mistake | 182 | 163 | 119 | 0.730 | 0.654 | 0.690 |
| miss | 75 | 61 | 46 | 0.754 | 0.613 | 0.676 |
| blunder | 49 | 43 | 33 | 0.767 | 0.673 | 0.717 |

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
| 185468614210 | white | 70.8 | 77.3 | +6.5 |
| 185468614210 | black | 77.1 | 84.0 | +6.9 |
| 185475865432 | white | 78.1 | 82.4 | +4.3 |
| 185475865432 | black | 66.1 | 72.4 | +6.3 |
| 185962590893 | white | 90.8 | 92.5 | +1.7 |
| 185962590893 | black | 90.9 | 93.3 | +2.4 |
| 1011026868 | white | 78.9 | 82.4 | +3.5 |
| 1011026868 | black | 75.2 | 79.9 | +4.7 |
| 184678264914 | white | 68.3 | 75.0 | +6.7 |
| 184678264914 | black | 80.3 | 82.3 | +2.0 |
| 184732665836 | white | 67.5 | 72.7 | +5.2 |
| 184732665836 | black | 68.7 | 72.4 | +3.7 |
| 184759290504 | white | 79.4 | 81.4 | +2.0 |
| 184759290504 | black | 97.9 | 97.2 | -0.7 |
| 184773009646 | white | 85.0 | 85.5 | +0.5 |
| 184773009646 | black | 77.2 | 81.2 | +4.0 |
| 184784174152 | white | 76.0 | 79.5 | +3.5 |
| 184784174152 | black | 86.8 | 87.7 | +0.9 |
| 184794204922 | white | 77.9 | 81.7 | +3.8 |
| 184794204922 | black | 57.0 | 61.7 | +4.7 |
| 184828162542 | white | 80.5 | 83.8 | +3.3 |
| 184828162542 | black | 85.9 | 88.8 | +2.9 |
| 184829980734 | white | 81.9 | 84.1 | +2.2 |
| 184829980734 | black | 85.5 | 90.7 | +5.2 |
| 184873703892 | white | 87.4 | 90.2 | +2.8 |
| 184873703892 | black | 87.4 | 90.1 | +2.7 |
| 185110487484 | white | 88.0 | 90.7 | +2.7 |
| 185110487484 | black | 91.5 | 92.9 | +1.4 |
| 185117573448 | white | 73.0 | 82.2 | +9.2 |
| 185117573448 | black | 78.9 | 84.8 | +5.9 |
| 185173941140 | white | 50.0 | 55.6 | +5.6 |
| 185173941140 | black | 61.2 | 67.9 | +6.7 |
| 185193771738 | white | 63.3 | 70.3 | +7.0 |
| 185193771738 | black | 70.7 | 74.5 | +3.8 |
| 185217478440 | white | 80.4 | 83.1 | +2.7 |
| 185217478440 | black | 77.3 | 80.0 | +2.7 |
| 185218140778 | white | 84.3 | 86.3 | +2.0 |
| 185218140778 | black | 79.3 | 84.3 | +5.0 |
| 185277691132 | white | 80.2 | 79.7 | -0.5 |
| 185277691132 | black | 78.8 | 79.3 | +0.5 |
| 185328167888 | white | 64.1 | 71.7 | +7.6 |
| 185328167888 | black | 54.8 | 63.0 | +8.2 |
| 185330935602 | white | 77.9 | 84.8 | +6.9 |
| 185330935602 | black | 68.5 | 77.5 | +9.0 |
| 185334658860 | white | 80.5 | 86.6 | +6.1 |
| 185334658860 | black | 73.4 | 78.6 | +5.2 |
| 185363017994 | white | 64.9 | 69.0 | +4.1 |
| 185363017994 | black | 67.8 | 70.8 | +3.0 |
| 185461631884 | white | 72.5 | 79.8 | +7.3 |
| 185461631884 | black | 80.3 | 82.0 | +1.7 |
| 185617589205 | white | 81.7 | 83.6 | +1.9 |
| 185617589205 | black | 76.4 | 82.7 | +6.3 |
| 185966191317 | white | 90.5 | 88.1 | -2.4 |
| 185966191317 | black | 72.5 | 78.1 | +5.6 |
| 186222389165 | white | 87.8 | 89.6 | +1.8 |
| 186222389165 | black | 92.7 | 94.6 | +1.9 |
| 186411389477 | white | 86.9 | 83.1 | -3.8 |
| 186411389477 | black | 81.3 | 85.8 | +4.5 |
| 186429989523 | white | 78.3 | 81.5 | +3.2 |
| 186429989523 | black | 85.9 | 86.7 | +0.8 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 61.2% | 77.6% | reviewed | 0.5 |
| 1041474766 | 25 | 25 | 72.0% | 80.0% | reviewed | 0.5 |
| 184759554082 | 62 | 62 | 71.0% | 88.7% | reviewed | 0.5 |
| 185209623352 | 155 | 155 | 65.8% | 89.7% | reviewed | 0.5 |
| 185324357184 | 55 | 55 | 85.5% | 96.4% | reviewed | 0.5 |
| 185436488062 | 13 | 13 | 76.9% | 92.3% | reviewed | 0.5 |
| 185437323918 | 108 | 103 | 64.1% | 85.4% | reviewed | 0.5 |
| 185438343298 | 20 | 20 | 95.0% | 95.0% | reviewed | 0.5 |
| 185438707002 | 95 | 91 | 74.7% | 92.3% | reviewed | 0.5 |
| 185456088510 | 60 | 60 | 73.3% | 93.3% | reviewed | 0.5 |
| 185468039834 | 38 | 38 | 65.8% | 92.1% | reviewed | 0.5 |
| 185468614210 | 54 | 54 | 83.3% | 94.4% | reviewed | 0.5 |
| 185475865432 | 53 | 53 | 73.6% | 92.5% | reviewed | 0.5 |
| 185962590893 | 78 | 78 | 78.2% | 91.0% | reviewed | 0.5 |
| 1011026868 | 32 | 32 | 68.8% | 93.8% | reviewed | 0.5 |
| 184678264914 | 72 | 72 | 69.4% | 90.3% | reviewed | 0.5 |
| 184732665836 | 93 | 93 | 63.4% | 88.2% | reviewed | 0.5 |
| 184759290504 | 46 | 46 | 71.7% | 78.3% | reviewed | 0.5 |
| 184773009646 | 73 | 73 | 61.6% | 94.5% | reviewed | 0.5 |
| 184784174152 | 36 | 36 | 58.3% | 72.2% | reviewed | 0.5 |
| 184794204922 | 41 | 41 | 73.2% | 90.2% | reviewed | 0.5 |
| 184828162542 | 88 | 88 | 47.7% | 78.4% | reviewed | 0.5 |
| 184829980734 | 50 | 50 | 78.0% | 92.0% | reviewed | 0.5 |
| 184873703892 | 96 | 96 | 60.4% | 81.2% | reviewed | 0.5 |
| 185110487484 | 124 | 124 | 53.2% | 88.7% | reviewed | 0.5 |
| 185117573448 | 88 | 88 | 70.5% | 90.9% | reviewed | 0.5 |
| 185173941140 | 40 | 40 | 67.5% | 82.5% | reviewed | 0.5 |
| 185193771738 | 84 | 84 | 65.5% | 94.0% | reviewed | 0.5 |
| 185217478440 | 75 | 75 | 62.7% | 93.3% | reviewed | 0.5 |
| 185218140778 | 81 | 81 | 66.7% | 95.1% | reviewed | 0.5 |
| 185277691132 | 112 | 112 | 67.9% | 93.8% | reviewed | 0.5 |
| 185328167888 | 49 | 49 | 65.3% | 85.7% | reviewed | 0.5 |
| 185330935602 | 21 | 21 | 61.9% | 95.2% | reviewed | 0.5 |
| 185334658860 | 59 | 59 | 72.9% | 93.2% | reviewed | 0.5 |
| 185363017994 | 107 | 107 | 75.7% | 95.3% | reviewed | 0.5 |
| 185461631884 | 72 | 72 | 72.2% | 95.8% | reviewed | 0.5 |
| 185617589205 | 111 | 111 | 62.2% | 86.5% | reviewed | 0.5 |
| 185966191317 | 41 | 41 | 65.9% | 80.5% | reviewed | 0.5 |
| 186222389165 | 97 | 97 | 63.9% | 85.6% | reviewed | 0.5 |
| 186411389477 | 107 | 107 | 67.3% | 90.7% | reviewed | 0.5 |
| 186429989523 | 82 | 82 | 65.9% | 95.1% | reviewed | 0.5 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label is one of the collector's candidates for 9 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | excellent | precision |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | best | precision |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (924)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 864 | excellent -> best x141, best -> excellent x128, good -> excellent x108, excellent -> good x83, great -> best x66, inaccuracy -> good x64 |
| `miss_detector` | 14 | mistake -> miss x7, blunder -> miss x6, inaccuracy -> miss x1 |
| `mate_override` | 13 | excellent -> inaccuracy x3, excellent -> good x3, best -> inaccuracy x2, miss -> good x2, good -> miss x1, good -> inaccuracy x1 |
| `book` | 12 | inaccuracy -> book x4, excellent -> book x3, good -> book x2, mistake -> book x1, great -> book x1, best -> book x1 |
| `blunder_softened` | 8 | miss -> mistake x5, blunder -> mistake x3 |
| `losing_material_hardened` | 7 | excellent -> mistake x4, inaccuracy -> mistake x2, good -> mistake x1 |
| `great_find_event` | 5 | best -> great x5 |
| `brilliant_event` | 1 | best -> brilliant x1 |

### `precision` (864)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 4 | 2... Nf6 | excellent | best | precision | best | 0.0000 | 0.478 | yes | Nf6 | - | +0.33 | +0.31 |
| 1034847688 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0011 | 0.504 | no | c5 | - | +0.13 | +0.12 |
| 1034847688 | 13 | 7. Bb2 | best | good | precision | good | 0.0204 | 0.488 | no | Be2 | - | -0.10 | -0.21 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0377 | 0.524 | no | Be2 | - | +0.12 | -0.13 |
| 1034847688 | 18 | 9... b5 | good | inaccuracy | precision | inaccuracy | 0.0559 | 0.514 | no | Bf5 | - | +0.38 | +0.39 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0533 | 0.574 | no | cxb5 | - | +0.24 | +0.19 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0915 | 0.648 | no | cxb5 | cxb5 | +0.44 | +0.35 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.462 | yes | h6 | - | +0.90 | +0.53 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0880 | 0.559 | no | bxc4 | Qd7 | +0.53 | +0.27 |
| 1034847688 | 30 | 15... Nh5 | miss | blunder | precision | blunder | 0.3080 | 0.636 | no | a4 | a4 | +1.64 | +1.67 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.544 | yes | Nxf3 | - | -0.10 | -0.44 |
| 1034847688 | 40 | 20... Nf5 | inaccuracy | excellent | precision | excellent | 0.0108 | 0.511 | no | Nh5 | f5 | +0.50 | +0.38 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.541 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.29 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0363 | 0.469 | no | fxe6 | - | +0.46 | +0.77 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.582 | yes | exf7+ | - | +0.09 | +0.89 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.405 | yes | Kxf7 | Rxf7 | +0.92 | +1.24 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0314 | 0.579 | no | d4 | - | +0.37 | +0.46 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0051 | 0.453 | no | e5 | - | +0.38 | +0.50 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.551 | yes | Bg2 | - | +0.34 | +0.43 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0031 | 0.456 | no | Nc6 | - | +0.59 | +0.46 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0297 | 0.547 | no | Nf3 | - | +0.17 | +0.17 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.522 | no | d4 | - | +0.28 | +0.29 |
| 1041474766 | 20 | 10... O-O | excellent | best | precision | best | 0.0000 | 0.464 | yes | O-O | - | +0.40 | +0.27 |
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
| 185209623352 | 8 | 4... Nc6 | best | excellent | precision | excellent | 0.0007 | 0.497 | no | Nf6 | - | -0.08 | +0.02 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.501 | yes | Nf3 | - | -0.16 | +0.00 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.827 | yes | Nxe4 | - | +5.09 | +5.67 |
| 185209623352 | 20 | 10... dxe4 | mistake | good | precision | good | 0.0210 | 0.170 | no | Qxe5 | - | +6.16 | +6.23 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0766 | 0.851 | no | Nxc6 | Nxc6 | +4.00 | +4.36 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0088 | 0.777 | no | Bxc6 | - | +4.04 | +4.19 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0474 | 0.775 | no | O-O-O | O-O-O | +3.00 | +3.64 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0398 | 0.266 | no | b5 | - | +4.18 | +4.41 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.238 | yes | Kc7 | - | +4.76 | +4.53 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0434 | 0.780 | no | Nd8 | Nd8 | +3.29 | +3.68 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.702 | yes | Rc5+ | - | +3.32 | +3.13 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.416 | no | Bxe5 | - | +0.92 | +1.22 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.584 | yes | Nxd3 | Rxd3 | -0.61 | -0.51 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0138 | 0.237 | no | Ka6 | - | +3.97 | +4.15 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0050 | 0.770 | no | Rd5 | - | +3.97 | +4.09 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.785 | yes | Kb2 | - | +4.39 | +4.46 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0066 | 0.788 | no | Rh5 | - | +4.14 | +4.56 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0143 | 0.815 | no | Rh5 | - | +4.64 | +4.97 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0337 | 0.815 | no | Rh5 | - | +4.51 | +4.86 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0344 | 0.250 | no | Kf5 | - | +4.38 | +4.39 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.773 | yes | Kc2 | - | +4.38 | +4.63 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0428 | 0.713 | no | Kd3 | - | +2.98 | +2.43 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.646 | yes | Kc1 | - | +2.15 | +2.41 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0799 | 0.226 | no | Kd5 | - | +6.01 | +6.31 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.713 | yes | Rf1+ | - | +3.73 | +3.49 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.814 | yes | Kxb2 | - | +5.17 | +5.33 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0170 | 0.184 | no | Bxf4 | - | +5.65 | +5.75 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0100 | 0.156 | no | b5 | - | +6.38 | +6.33 |
| 185209623352 | 101 | 51. Rb4 | excellent | best | precision | best | 0.0000 | 0.855 | yes | Rb4 | - | +6.27 | +6.30 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0007 | 0.855 | no | Rc7 | - | +6.33 | +6.54 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0026 | 0.139 | no | Bd8 | - | +6.33 | +6.47 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.859 | yes | R7xb5 | - | +6.30 | +6.66 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0000 | 0.866 | no | Rc4 | - | +6.59 | +6.71 |
| 185209623352 | 110 | 55... Kg6 | excellent | best | precision | best | 0.0000 | 0.135 | no | Bg7 | - | +6.54 | +6.65 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0000 | 0.865 | no | Rb6 | - | +6.54 | +6.77 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.086 | yes | Kf6 | - | +7.19 | +8.34 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0095 | 0.049 | no | Ke7 | Ke7 | +10.6 | +11.15 |
| 185209623352 | 117 | 59. h5 | good | excellent | precision | excellent | 0.0170 | 0.958 | no | Kc3 | - | +8.42 | +13.12 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | +12.25 |
| 185209623352 | 124 | 62... Kf6 | excellent | best | precision | best | 0.0000 | 0.000 | no | Ke6 | - | M6 | M9 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | - | M5 | M11 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg5 | - | M3 | M6 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M9 |
| 185324357184 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0035 | 0.567 | no | O-O | - | -1.29 | -1.17 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0100 | 0.252 | no | d4 | - | -4.03 | -4.09 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.520 | yes | Qg1 | - | +0.29 | +0.15 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0367 | 0.308 | no | Qh5 | - | +3.38 | +3.51 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0042 | 0.516 | no | Rh2 | - | +0.11 | +0.03 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.516 | no | b3 | - | +0.26 | +0.40 |
| 185324357184 | 51 | 26. Bxc3 | excellent | good | precision | good | 0.0247 | 0.473 | no | bxc3 | - | -0.68 | -0.77 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0302 | 0.562 | no | d4 | - | +0.65 | +0.50 |
| 185436488062 | 8 | 4... a6 | inaccuracy | mistake | precision | mistake | 0.1021 | 0.465 | no | Nf6 | - | +1.74 | +1.99 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.637 | yes | Nxe5 | - | +1.74 | +1.97 |
| 185437323918 | 10 | 5... Kf8 | good | inaccuracy | precision | inaccuracy | 0.0503 | 0.442 | no | Ke7 | - | +1.39 | +1.52 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0369 | 0.277 | no | Nh7+ | - | -3.51 | -4.01 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0081 | 0.844 | no | g4 | - | -5.16 | -5.46 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0468 | 0.846 | no | g4 | - | -4.94 | -4.80 |
| 185437323918 | 33 | 17. bxc3 | good | best | precision | best | 0.0000 | 0.149 | yes | bxc3 | - | -6.58 | -6.37 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0000 | 0.862 | no | Rxh2+ | - | -6.58 | -6.48 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.845 | no | Qe2 | - | -5.96 | -5.97 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0440 | 0.794 | no | Qf4 | - | -3.59 | -3.86 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0989 | 0.248 | no | hxg3 | hxg3 | -5.85 | -6.02 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0153 | 0.821 | no | b6 | - | -4.41 | -4.93 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0363 | 0.708 | no | Bc2 | - | -2.41 | -2.79 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.845 | yes | Be4 | - | -5.61 | -6.12 |
| 185437323918 | 59 | 30. g5+ | good | excellent | precision | excellent | 0.0184 | 0.147 | no | Rg3 | - | -6.55 | -6.66 |
| 185437323918 | 65 | 33. Rg3+ | excellent | best | precision | best | 0.0000 | 0.164 | yes | Rg3+ | - | -5.91 | -6.04 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0075 | 0.851 | no | Kf5 | - | -5.11 | -5.84 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | best | precision | best | 0.0000 | 0.157 | yes | Kh2 | Kg2 | -6.13 | -6.15 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0457 | 0.855 | no | e4 | e4 | -5.01 | -5.01 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0000 | 0.852 | no | Bb4 | - | -6.12 | -6.39 |
| 185437323918 | 75 | 38. Ke4 | best | good | precision | good | 0.0293 | 0.137 | no | Ke2 | - | -6.12 | -6.33 |
| 185437323918 | 76 | 38... Rf4+ | best | good | precision | good | 0.0208 | 0.861 | no | Bc3 | - | -6.12 | -6.94 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0089 | 0.113 | no | d6 | - | -7.11 | -7.49 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0044 | 0.914 | no | Bb4 | - | -7.28 | -8.41 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.082 | yes | Kxc7 | - | -8.05 | -8.68 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0010 | 0.924 | no | Bg3+ | - | -8.05 | -9.10 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.068 | yes | d6 | - | -8.99 | -9.08 |
| 185437323918 | 94 | 47... Qb2+ | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qb2+ | - | -9.07 | -M19 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kc6 | Ka6 | -M17 | -M20 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -12.43 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.018 | no | Kd4 | - | -10.7 | -12.77 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0053 | 0.975 | no | Qb3+ | - | -10.7 | -12.88 |
| 185437323918 | 101 | 51. Ke6 | good | excellent | precision | excellent | 0.0051 | 0.024 | no | Kd4 | - | -M6 | -M13 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0102 | 0.513 | no | Nf3 | - | -0.01 | +0.04 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.497 | yes | h6 | - | -0.01 | -0.07 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.495 | yes | Bh4 | - | -0.01 | -0.02 |
| 185438707002 | 30 | 15... Nxf3+ | good | inaccuracy | precision | inaccuracy | 0.0560 | 0.445 | no | Rhg8 | - | +1.28 | +1.55 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.608 | yes | c3 | - | +1.35 | +1.31 |
| 185438707002 | 43 | 22. d4 | excellent | good | precision | good | 0.0224 | 0.762 | no | Rd2 | - | +3.74 | +3.57 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.766 | yes | Rxd4 | - | +3.82 | +3.88 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0649 | 0.256 | no | Rg8 | - | +4.87 | +4.95 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0434 | 0.809 | no | Qf6 | Qf6 | +3.70 | +4.06 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.253 | yes | a6 | - | +3.78 | +3.80 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0005 | 0.752 | no | Qf3 | - | +3.78 | +3.79 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.771 | yes | Qxd8+ | - | +3.69 | +3.97 |
| 185438707002 | 63 | 32. b4 | good | excellent | precision | excellent | 0.0146 | 0.689 | no | Rd2 | - | +1.87 | +1.72 |
| 185438707002 | 65 | 33. Rd5 | excellent | good | precision | good | 0.0259 | 0.681 | no | Rd8 | - | +1.84 | +2.23 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | good | precision | good | 0.0487 | 0.343 | no | Qb3 | Qb3 | +2.60 | +3.00 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.752 | yes | Qb2+ | - | -3.65 | -3.92 |
| 185438707002 | 75 | 38. Kg1 | best | excellent | precision | excellent | 0.0022 | 0.246 | no | f3 | - | -3.38 | -3.91 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0335 | 0.711 | no | Qc2 | - | -2.36 | -2.54 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0000 | 0.920 | no | Qd1 | - | -8.73 | -8.64 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.074 | yes | g4 | - | -8.80 | -8.28 |
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
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0450 | 0.821 | no | Nh4 | - | +1.72 | +1.79 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0000 | 0.875 | no | a5 | - | +2.89 | +3.36 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.927 | yes | Nxe3 | - | -4.25 | -5.02 |
| 185468039834 | 11 | 6. Nd5 | best | good | precision | good | 0.0227 | 0.453 | no | Na4 | - | -0.94 | -1.10 |
| 185468039834 | 12 | 6... d6 | inaccuracy | mistake | precision | mistake | 0.1007 | 0.578 | no | h6 | h6 | 0.00 | +0.31 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0144 | 0.486 | no | Ne5 | - | +0.60 | +0.50 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0335 | 0.468 | no | Kf8 | - | +0.61 | +0.91 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0309 | 0.411 | no | dxe5 | dxe5 | +1.53 | +1.54 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.609 | yes | Qh5 | - | +1.48 | +1.58 |
| 185468039834 | 23 | 12. Qf3 | miss | blunder | precision | blunder | 0.2499 | 0.649 | no | Nxc7+ | Nxc7+ | -0.91 | -1.42 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.601 | yes | c6 | - | -0.83 | -1.10 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0160 | 0.422 | no | b4 | - | -1.28 | -1.39 |
| 185468039834 | 27 | 14. Bxe6 | best | excellent | precision | excellent | 0.0103 | 0.401 | no | b3 | - | -1.28 | -1.44 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.732 | yes | Rf8 | - | -3.36 | -3.55 |
| 185468039834 | 32 | 16... Rxf6 | excellent | best | precision | best | 0.0000 | 0.734 | yes | Rxf6 | - | -3.39 | -3.58 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0006 | 0.263 | no | Qg3 | - | -3.39 | -3.70 |
| 185468614210 | 28 | 14... Nxd5 | excellent | best | precision | best | 0.0000 | 0.485 | yes | Nxd5 | - | +0.25 | +0.18 |
| 185468614210 | 31 | 16. Qxd5 | best | excellent | precision | excellent | 0.0014 | 0.509 | no | Ng5+ | - | +0.25 | +0.24 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0387 | 0.483 | no | Kg8 | Kg8 | +1.21 | +0.78 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0401 | 0.556 | no | Qh5+ | Qh5+ | +0.18 | +0.20 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.486 | yes | Kg8 | - | +0.18 | +0.13 |
| 185468614210 | 38 | 19... Qf6 | good | excellent | precision | excellent | 0.0173 | 0.523 | no | b6 | - | -0.09 | -0.08 |
| 185468614210 | 40 | 20... Rxd6 | excellent | good | precision | good | 0.0245 | 0.515 | no | cxd6 | - | +0.14 | +0.09 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0199 | 0.566 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.451 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.546 | yes | Nc3 | - | +0.74 | +0.67 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.452 | yes | e6 | - | +0.74 | +0.68 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0100 | 0.460 | no | Bb4 | - | +0.55 | +0.70 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0068 | 0.394 | no | c3 | - | -1.49 | -1.60 |
| 185475865432 | 27 | 14. Ng3 | inaccuracy | good | precision | good | 0.0456 | 0.408 | no | Qxd8+ | Qxd8+ | -1.91 | -1.97 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0414 | 0.638 | no | Qxd1 | Qxd1 | -1.24 | -1.16 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0171 | 0.620 | no | Bd6 | - | -1.25 | -1.48 |
| 185475865432 | 37 | 19. Rad1 | excellent | best | precision | best | 0.0000 | 0.612 | yes | Rad1 | - | +1.50 | +1.68 |
| 185475865432 | 44 | 22... Rc8 | excellent | best | precision | best | 0.0000 | 0.391 | yes | Rc8 | - | +1.57 | +1.73 |
| 185475865432 | 48 | 24... Be2 | inaccuracy | mistake | precision | mistake | 0.1011 | 0.384 | no | Rb8 | Rb8 | +3.18 | +3.23 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0943 | 0.717 | no | Rxe6 | Rxe6 | +1.47 | +1.74 |
| 185475865432 | 51 | 26. a7 | excellent | best | precision | best | 0.0000 | 0.774 | yes | a7 | - | +3.79 | +3.91 |
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
| 1011026868 | 6 | 3... d6 | book | good | precision | good | 0.0241 | 0.472 | no | g6 | - | +0.45 | +0.47 |
| 1011026868 | 9 | 5. Bc4 | good | inaccuracy | precision | inaccuracy | 0.0715 | 0.559 | no | d4 | - | +0.09 | -0.11 |
| 1011026868 | 11 | 6. d3 | good | excellent | precision | excellent | 0.0044 | 0.509 | no | O-O | - | -0.10 | -0.01 |
| 1011026868 | 13 | 7. Be3 | excellent | good | precision | good | 0.0253 | 0.487 | no | O-O | - | -0.28 | -0.35 |
| 1011026868 | 17 | 9. a3 | miss | blunder | precision | blunder | 0.2460 | 0.447 | no | Ne2 | Ne2 | -2.74 | -3.12 |
| 1011026868 | 22 | 11... O-O | good | excellent | precision | excellent | 0.0033 | 0.507 | no | Ne5 | - | +0.19 | +0.16 |
| 1011026868 | 23 | 12. O-O | good | excellent | precision | excellent | 0.0166 | 0.518 | no | Qd2 | - | -0.02 | -0.05 |
| 1011026868 | 27 | 14. Bh6 | excellent | good | precision | good | 0.0231 | 0.547 | no | Rbd1 | - | +0.30 | +0.22 |
| 1011026868 | 28 | 14... e5 | good | inaccuracy | precision | inaccuracy | 0.0557 | 0.476 | no | Ne5 | - | +0.76 | +0.73 |
| 1011026868 | 31 | 16. Ng3 | good | excellent | precision | excellent | 0.0143 | 0.544 | no | b4 | - | -0.08 | +0.27 |
| 184678264914 | 10 | 5... a6 | inaccuracy | good | precision | good | 0.0397 | 0.399 | no | d6 | Bb6 | +1.79 | +1.85 |
| 184678264914 | 13 | 7. b4 | inaccuracy | good | precision | good | 0.0433 | 0.569 | no | d4 | d4 | +0.39 | +0.33 |
| 184678264914 | 16 | 8... Bg4 | excellent | good | precision | good | 0.0202 | 0.481 | no | Nf6 | - | +0.57 | +0.50 |
| 184678264914 | 23 | 12. d3 | excellent | best | precision | best | 0.0000 | 0.488 | yes | d3 | - | -0.26 | -0.16 |
| 184678264914 | 25 | 13. Bxc6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Bxc6 | - | -0.19 | -0.19 |
| 184678264914 | 27 | 14. a6 | good | inaccuracy | precision | inaccuracy | 0.0527 | 0.486 | no | Nbd2 | - | -0.87 | -0.86 |
| 184678264914 | 40 | 20... Rxb1 | great | best | precision | best | 0.0000 | 0.742 | yes | Rxb1 | - | -3.34 | -3.55 |
| 184678264914 | 45 | 23. Qd1 | excellent | best | precision | best | 0.0000 | 0.195 | yes | Qd1 | - | -4.69 | -4.90 |
| 184678264914 | 46 | 23... Nh5 | excellent | good | precision | good | 0.0337 | 0.822 | no | Re8 | - | -4.43 | -4.21 |
| 184678264914 | 48 | 24... Nf4 | good | inaccuracy | precision | inaccuracy | 0.0570 | 0.815 | no | Ra8 | - | -3.64 | -3.65 |
| 184678264914 | 52 | 26... Re8 | excellent | good | precision | good | 0.0227 | 0.839 | no | h6 | - | -4.69 | -4.87 |
| 184678264914 | 54 | 27... Qxf3 | inaccuracy | good | precision | good | 0.0259 | 0.893 | no | Re6 | Re6 | -4.60 | -6.68 |
| 184678264914 | 55 | 28. Ra1 | inaccuracy | best | precision | best | 0.0000 | 0.110 | yes | Ra1 | Qd1 | -6.20 | -6.67 |
| 184678264914 | 58 | 29... Qg4+ | best | good | precision | good | 0.0237 | 0.934 | no | Re5 | - | -7.29 | -8.10 |
| 184678264914 | 60 | 30... f3 | excellent | best | precision | best | 0.0000 | 0.901 | yes | f3 | - | -7.13 | -7.62 |
| 184678264914 | 64 | 32... Qg2+ | good | inaccuracy | precision | inaccuracy | 0.0677 | 0.979 | no | Ra8 | - | -7.02 | -7.47 |
| 184678264914 | 66 | 33... d4 | mistake | good | precision | good | 0.0470 | 0.906 | no | Ra8 | - | -4.32 | -5.79 |
| 184678264914 | 68 | 34... cxd4 | excellent | good | precision | good | 0.0209 | 0.847 | no | Ra8 | - | -4.05 | -4.01 |
| 184678264914 | 70 | 35... Qg1+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qg1+ | - | -M2 | -M2 |
| 184732665836 | 8 | 4... c4 | inaccuracy | good | precision | good | 0.0486 | 0.472 | no | Bd7 | Nc6 | +0.99 | +1.02 |
| 184732665836 | 9 | 5. Nf3 | good | excellent | precision | excellent | 0.0074 | 0.577 | no | b3 | - | +0.79 | +0.91 |
| 184732665836 | 14 | 7... bxc3 | best | excellent | precision | excellent | 0.0027 | 0.329 | no | Qa5 | - | +1.98 | +1.99 |
| 184732665836 | 15 | 8. Nxc3 | inaccuracy | good | precision | good | 0.0490 | 0.646 | no | bxc4 | bxc4 | +1.37 | +1.32 |
| 184732665836 | 18 | 9... Qd8 | good | inaccuracy | precision | inaccuracy | 0.0750 | 0.331 | no | cxb3 | - | +3.07 | +3.52 |
| 184732665836 | 24 | 12... fxe5 | good | excellent | precision | excellent | 0.0115 | 0.154 | no | Be7 | - | +5.78 | +6.21 |
| 184732665836 | 26 | 13... Nf6 | mistake | best | precision | best | 0.0000 | 0.144 | yes | Nf6 | - | +5.51 | +5.99 |
| 184732665836 | 28 | 14... Be7 | mistake | best | precision | best | 0.0000 | 0.164 | yes | Be7 | - | +5.54 | +5.95 |
| 184732665836 | 29 | 15. Bxf6 | good | inaccuracy | precision | inaccuracy | 0.0691 | 0.858 | no | Qf3 | - | +4.65 | +4.36 |
| 184732665836 | 33 | 17. Nxg6 | mistake | inaccuracy | precision | inaccuracy | 0.0997 | 0.819 | no | Qf3 | - | +2.71 | +3.11 |
| 184732665836 | 34 | 17... Rg8 | blunder | mistake | precision | mistake | 0.1698 | 0.281 | no | hxg6 | hxg6 | +6.81 | +7.47 |
| 184732665836 | 40 | 20... Bxe5 | best | excellent | precision | excellent | 0.0101 | 0.203 | no | Kf8 | - | +3.98 | +4.12 |
| 184732665836 | 42 | 21... Nc6 | mistake | inaccuracy | precision | inaccuracy | 0.0723 | 0.202 | no | Qxd4+ | - | +6.33 | +6.24 |
| 184732665836 | 43 | 22. Qh4+ | inaccuracy | good | precision | good | 0.0233 | 0.868 | no | d5 | d5 | +5.32 | +5.72 |
| 184732665836 | 46 | 23... Kd7 | mistake | good | precision | good | 0.0491 | 0.153 | no | Rg6 | - | +7.09 | +7.25 |
| 184732665836 | 51 | 26. Rf7+ | excellent | best | precision | best | 0.0000 | 0.844 | yes | Rf7+ | - | +4.77 | +5.64 |
| 184732665836 | 56 | 28... Nc2 | mistake | inaccuracy | precision | inaccuracy | 0.0879 | 0.211 | no | Kc7 | - | +6.50 | +6.49 |
| 184732665836 | 59 | 30. Rf7 | best | good | precision | good | 0.0291 | 0.905 | no | Qf3+ | - | +6.93 | +6.37 |
| 184732665836 | 60 | 30... Qd8 | mistake | good | precision | good | 0.0410 | 0.127 | no | Qxf7 | - | +7.94 | +7.81 |
| 184732665836 | 63 | 32. Qxa8 | good | excellent | precision | excellent | 0.0043 | 0.916 | no | Bf1 | - | +7.22 | +8.07 |
| 184732665836 | 68 | 34... Ka5 | excellent | best | precision | best | 0.0000 | 0.033 | yes | Ka5 | - | M9 | +10.49 |
| 184732665836 | 69 | 35. Ra7 | miss | mistake | precision | mistake | 0.1472 | 0.960 | no | Qe1+ | Qe1+ | +4.45 | +4.85 |
| 184732665836 | 71 | 36. Kf1 | excellent | best | precision | best | 0.0000 | 0.806 | yes | Kf1 | - | +4.44 | +4.54 |
| 184732665836 | 73 | 37. Nxc8 | excellent | best | precision | best | 0.0000 | 0.803 | yes | Nxc8 | - | +4.42 | +4.52 |
| 184732665836 | 74 | 37... Qc7 | excellent | good | precision | good | 0.0207 | 0.203 | no | Qc5 | - | +4.84 | +4.96 |
| 184732665836 | 79 | 40. Qe2 | great | best | precision | best | 0.0000 | 0.759 | yes | Qe2 | - | +3.80 | +3.93 |
| 184732665836 | 81 | 41. Qe3 | good | excellent | precision | excellent | 0.0140 | 0.808 | no | Kf3 | - | +4.02 | +4.57 |
| 184732665836 | 82 | 41... Qh4+ | inaccuracy | good | precision | good | 0.0293 | 0.201 | no | Qb2+ | Nc2 | +5.87 | +7.00 |
| 184732665836 | 86 | 43... Qb2+ | excellent | best | precision | best | 0.0000 | 0.188 | yes | Qb2+ | - | +4.43 | +4.47 |
| 184732665836 | 87 | 44. Qe2 | great | best | precision | best | 0.0000 | 0.794 | yes | Qe2 | - | +4.43 | +4.78 |
| 184732665836 | 91 | 46. Qe2 | great | best | precision | best | 0.0000 | 0.796 | yes | Qe2 | - | +4.48 | +4.64 |
| 184759290504 | 12 | 6... a6 | book | best | precision | best | 0.0000 | 0.390 | yes | a6 | - | +0.80 | +0.82 |
| 184759290504 | 13 | 7. f3 | book | best | precision | best | 0.0000 | 0.628 | yes | f3 | - | +0.64 | +0.58 |
| 184759290504 | 15 | 8. Qd2 | excellent | best | precision | best | 0.0000 | 0.626 | yes | Qd2 | - | +0.56 | +0.74 |
| 184759290504 | 16 | 8... Bg7 | good | best | precision | best | 0.0000 | 0.384 | yes | Bg7 | - | +0.79 | +0.86 |
| 184759290504 | 18 | 9... b5 | best | inaccuracy | precision | inaccuracy | 0.0703 | 0.395 | no | Bd7 | - | +0.64 | +1.15 |
| 184759290504 | 19 | 10. Bb3 | best | inaccuracy | precision | inaccuracy | 0.0703 | 0.675 | no | Bd5 | - | +0.64 | +0.76 |
| 184759290504 | 22 | 11... Nbd7 | best | good | precision | good | 0.0261 | 0.418 | no | Nc6 | - | +0.72 | +0.87 |
| 184759290504 | 23 | 12. h3 | best | inaccuracy | precision | inaccuracy | 0.0530 | 0.635 | no | Rhe1 | - | +0.72 | +0.52 |
| 184759290504 | 25 | 13. Rhe1 | good | best | precision | best | 0.0000 | 0.622 | yes | Rhe1 | - | +0.81 | +0.67 |
| 184759290504 | 26 | 13... Rc8 | best | excellent | precision | excellent | 0.0151 | 0.395 | no | Nc5 | - | +0.81 | +0.70 |
| 184759290504 | 29 | 15. Qf2 | best | good | precision | good | 0.0208 | 0.641 | no | Bg5 | - | +0.91 | +0.78 |
| 184759290504 | 34 | 17... Nfd7 | inaccuracy | good | precision | good | 0.0334 | 0.508 | no | O-O | O-O | +0.37 | +0.38 |
| 184773009646 | 12 | 6... Bb6 | mistake | inaccuracy | precision | inaccuracy | 0.0820 | 0.504 | no | Bb4+ | Bb4+ | +1.89 | +1.80 |
| 184773009646 | 13 | 7. Nc3 | miss | inaccuracy | precision | inaccuracy | 0.0838 | 0.619 | no | e5 | e5 | +0.52 | +0.52 |
| 184773009646 | 14 | 7... O-O | inaccuracy | good | precision | good | 0.0266 | 0.465 | no | d6 | - | +1.27 | +1.40 |
| 184773009646 | 16 | 8... Re8 | mistake | inaccuracy | precision | inaccuracy | 0.0926 | 0.407 | no | d5 | - | +3.29 | +3.10 |
| 184773009646 | 17 | 9. O-O | great | best | precision | best | 0.0000 | 0.697 | yes | O-O | - | +3.29 | +3.01 |
| 184773009646 | 24 | 12... Be6 | excellent | good | precision | good | 0.0240 | 0.259 | no | Bg4 | - | +3.85 | +4.39 |
| 184773009646 | 25 | 13. Bxe6 | best | excellent | precision | excellent | 0.0034 | 0.765 | no | d5 | - | +3.85 | +4.20 |
| 184773009646 | 27 | 14. Qxe6 | excellent | best | precision | best | 0.0000 | 0.774 | yes | Qxe6 | - | +4.08 | +4.47 |
| 184773009646 | 30 | 15... Nxd4 | good | excellent | precision | excellent | 0.0128 | 0.300 | no | Bxd4 | - | +3.26 | +3.49 |
| 184773009646 | 35 | 18. Be3 | excellent | best | precision | best | 0.0000 | 0.708 | yes | Be3 | - | +2.72 | +3.00 |
| 184773009646 | 40 | 20... b6 | good | excellent | precision | excellent | 0.0121 | 0.242 | no | Bxb2 | - | +4.48 | +4.43 |
| 184773009646 | 42 | 21... a6 | good | inaccuracy | precision | inaccuracy | 0.0574 | 0.287 | no | Bxb2 | - | +4.23 | +4.51 |
| 184773009646 | 43 | 22. Nc7 | good | inaccuracy | precision | inaccuracy | 0.0547 | 0.771 | no | Nc3 | - | +3.60 | +3.93 |
| 184773009646 | 44 | 22... Ra7 | good | excellent | precision | excellent | 0.0071 | 0.258 | no | Rc8 | - | +4.03 | +4.05 |
| 184773009646 | 47 | 24. Bf4 | good | inaccuracy | precision | inaccuracy | 0.0612 | 0.771 | no | Nf4 | - | +3.28 | +3.33 |
| 184773009646 | 48 | 24... Bxb2 | good | inaccuracy | precision | inaccuracy | 0.0511 | 0.290 | no | a4 | - | +4.06 | +4.31 |
| 184773009646 | 50 | 25... c4 | excellent | best | precision | best | 0.0000 | 0.277 | yes | c4 | - | +3.51 | +3.73 |
| 184773009646 | 51 | 26. Re8+ | excellent | best | precision | best | 0.0000 | 0.732 | yes | Re8+ | - | +3.38 | +3.73 |
| 184773009646 | 52 | 26... Kh7 | excellent | best | precision | best | 0.0000 | 0.268 | yes | Kh7 | - | +3.56 | +4.06 |
| 184773009646 | 53 | 27. Nb5 | excellent | inaccuracy | precision | inaccuracy | 0.0579 | 0.749 | no | Re2 | - | +3.23 | +2.99 |
| 184773009646 | 55 | 28. Be5 | excellent | good | precision | good | 0.0245 | 0.758 | no | Re2 | - | +3.54 | +3.39 |
| 184773009646 | 57 | 29. Nxa3 | great | best | precision | best | 0.0000 | 0.843 | yes | Nxa3 | - | +6.25 | +6.35 |
| 184773009646 | 58 | 29... Rb7 | best | excellent | precision | excellent | 0.0010 | 0.154 | no | a4 | - | +6.25 | +6.47 |
| 184773009646 | 60 | 30... b5 | excellent | best | precision | best | 0.0000 | 0.163 | yes | b5 | - | +6.39 | +6.67 |
| 184773009646 | 61 | 31. Nxa5 | excellent | best | precision | best | 0.0000 | 0.857 | yes | Nxa5 | - | +6.21 | +6.62 |
| 184773009646 | 67 | 34. g3 | best | excellent | precision | excellent | 0.0178 | 0.856 | no | Kf1 | - | +6.17 | +6.28 |
| 184773009646 | 69 | 35. Nd3 | excellent | best | precision | best | 0.0000 | 0.846 | yes | Nd3 | - | +6.22 | +6.32 |
| 184773009646 | 73 | 37. Rb6 | best | excellent | precision | excellent | 0.0007 | 0.854 | no | Ra6 | - | +6.26 | +6.58 |
| 184784174152 | 8 | 4... c6 | book | inaccuracy | precision | inaccuracy | 0.0668 | 0.532 | no | e6 | - | +0.07 | +0.22 |
| 184784174152 | 9 | 5. e3 | book | best | precision | best | 0.0000 | 0.535 | yes | e3 | - | +0.07 | +0.17 |
| 184784174152 | 10 | 5... h6 | best | excellent | precision | excellent | 0.0079 | 0.473 | no | e6 | - | +0.07 | +0.22 |
| 184784174152 | 12 | 6... Qb6 | good | best | precision | best | 0.0000 | 0.482 | yes | Qb6 | - | +0.18 | +0.21 |
| 184784174152 | 13 | 7. Rb1 | good | best | precision | best | 0.0000 | 0.533 | yes | Rb1 | - | -0.02 | +0.08 |
| 184784174152 | 14 | 7... e6 | inaccuracy | good | precision | good | 0.0222 | 0.487 | no | g5 | g5 | +0.30 | +0.34 |
| 184784174152 | 16 | 8... Bd6 | good | excellent | precision | excellent | 0.0173 | 0.448 | no | c5 | - | +0.54 | +0.44 |
| 184784174152 | 19 | 10. e4 | excellent | inaccuracy | precision | inaccuracy | 0.0703 | 0.602 | no | Re1 | - | +0.47 | +0.20 |
| 184784174152 | 21 | 11. Nxe4 | mistake | good | precision | good | 0.0413 | 0.541 | no | Bxe4 | Bxe4 | -0.84 | -1.26 |
| 184784174152 | 24 | 12... e5 | mistake | blunder | precision | blunder | 0.4270 | 0.674 | no | f5 | f5 | +1.55 | +1.75 |
| 184784174152 | 25 | 13. dxe5 | great | best | precision | best | 0.0000 | 0.753 | yes | dxe5 | - | +1.55 | +1.81 |
| 184784174152 | 32 | 16... f5 | great | best | precision | best | 0.0000 | 0.920 | yes | f5 | - | -3.61 | -3.73 |
| 184784174152 | 33 | 17. Bf3 | mistake | good | precision | good | 0.0370 | 0.085 | no | Be7 | - | -4.19 | -4.69 |
| 184794204922 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.495 | yes | Nf6 | - | +0.20 | +0.25 |
| 184794204922 | 7 | 4. Nc3 | book | best | precision | best | 0.0000 | 0.517 | yes | Nc3 | - | +0.20 | +0.18 |
| 184794204922 | 13 | 7. Nd5 | excellent | good | precision | good | 0.0213 | 0.543 | no | Ne2 | - | +0.49 | +0.40 |
| 184794204922 | 22 | 11... Bg4 | mistake | blunder | precision | blunder | 0.2019 | 0.348 | no | h5 | Be7 | +5.65 | +6.63 |
| 184794204922 | 23 | 12. Qxg4 | great | best | precision | best | 0.0000 | 0.854 | yes | Qxg4 | - | +5.65 | +6.30 |
| 184794204922 | 26 | 13... b5 | good | excellent | precision | excellent | 0.0021 | 0.155 | no | Kc7 | - | +6.18 | +6.37 |
| 184794204922 | 29 | 15. a4 | good | excellent | precision | excellent | 0.0014 | 0.852 | no | Bd2 | - | +5.65 | +6.06 |
| 184794204922 | 31 | 16. Bd2 | inaccuracy | good | precision | good | 0.0205 | 0.862 | no | fxe5 | fxe5 | +5.52 | +5.83 |
| 184794204922 | 32 | 16... g6 | mistake | good | precision | good | 0.0445 | 0.174 | no | h5 | - | +7.41 | +7.13 |
| 184794204922 | 36 | 18... h5 | best | excellent | precision | excellent | 0.0139 | 0.056 | no | Ra7 | - | +9.48 | +10.62 |
| 184794204922 | 38 | 19... Rc8 | good | excellent | precision | excellent | 0.0131 | 0.069 | no | Ra7 | - | M6 | M10 |
| 184828162542 | 5 | 3. Nd2 | book | excellent | precision | excellent | 0.0174 | 0.540 | no | e4 | - | +0.16 | +0.14 |
| 184828162542 | 6 | 3... d5 | book | good | precision | good | 0.0301 | 0.478 | no | c5 | - | +0.42 | +0.30 |
| 184828162542 | 7 | 4. e3 | book | excellent | precision | excellent | 0.0095 | 0.548 | no | e4 | - | +0.14 | +0.21 |
| 184828162542 | 10 | 5... c5 | book | excellent | precision | excellent | 0.0048 | 0.468 | no | Nbd7 | - | +0.16 | +0.29 |
| 184828162542 | 11 | 6. c3 | book | best | precision | best | 0.0000 | 0.546 | yes | c3 | - | +0.16 | +0.22 |
| 184828162542 | 12 | 6... Nc6 | book | excellent | precision | excellent | 0.0063 | 0.465 | no | cxd4 | - | +0.16 | +0.26 |
| 184828162542 | 15 | 8. Bxf6 | inaccuracy | mistake | precision | mistake | 0.1015 | 0.563 | no | Ngf3 | Ngf3 | -0.19 | -0.24 |
| 184828162542 | 17 | 9. f4 | good | excellent | precision | excellent | 0.0016 | 0.454 | no | Ngf3 | - | -0.32 | -0.26 |
| 184828162542 | 18 | 9... Qd6 | inaccuracy | good | precision | good | 0.0222 | 0.541 | no | Qb6 | Qb6 | 0.00 | -0.12 |
| 184828162542 | 19 | 10. Ngf3 | excellent | best | precision | best | 0.0000 | 0.481 | no | Ndf3 | - | -0.10 | -0.12 |
| 184828162542 | 22 | 11... Bd7 | excellent | best | precision | best | 0.0000 | 0.444 | yes | Bd7 | - | +0.30 | +0.18 |
| 184828162542 | 24 | 12... Rc8 | good | excellent | precision | excellent | 0.0189 | 0.462 | no | g5 | - | +0.46 | +0.42 |
| 184828162542 | 29 | 15. Ng4 | best | good | precision | good | 0.0293 | 0.604 | no | Qe2 | - | +0.70 | +0.47 |
| 184828162542 | 30 | 15... Kh8 | best | good | precision | good | 0.0278 | 0.426 | no | Qb6 | - | +0.70 | +0.70 |
| 184828162542 | 33 | 17. Qh5 | best | good | precision | good | 0.0236 | 0.647 | no | Nb3 | - | +0.70 | +0.73 |
| 184828162542 | 34 | 17... Ng8 | best | excellent | precision | excellent | 0.0150 | 0.386 | no | Kg7 | - | +0.70 | +0.85 |
| 184828162542 | 35 | 18. Rf3 | inaccuracy | mistake | precision | mistake | 0.1321 | 0.632 | no | Nb3 | - | +0.11 | +0.00 |
| 184828162542 | 37 | 19. Rg3 | good | inaccuracy | precision | inaccuracy | 0.0602 | 0.560 | no | Rf2 | - | +0.09 | +0.00 |
| 184828162542 | 39 | 20. Rf1 | best | good | precision | good | 0.0281 | 0.584 | no | Nb3 | - | +0.48 | +0.35 |
| 184828162542 | 40 | 20... Qe7 | best | good | precision | good | 0.0235 | 0.444 | no | Be8 | - | +0.48 | +0.43 |
| 184828162542 | 44 | 22... Qh7 | good | inaccuracy | precision | inaccuracy | 0.0539 | 0.500 | no | Qc7 | - | +0.35 | +0.34 |
| 184828162542 | 45 | 23. Nh4 | inaccuracy | good | precision | good | 0.0444 | 0.554 | no | Nd2 | Qh4 | 0.00 | +0.06 |
| 184828162542 | 46 | 23... Ne7 | best | excellent | precision | excellent | 0.0064 | 0.490 | no | Rc7 | - | 0.00 | +0.10 |
| 184828162542 | 47 | 24. Nf3 | good | excellent | precision | excellent | 0.0175 | 0.516 | no | Rgf3 | - | -0.25 | -0.17 |
| 184828162542 | 48 | 24... a6 | inaccuracy | excellent | precision | excellent | 0.0143 | 0.527 | no | h5 | h5 | +0.17 | +0.00 |
| 184828162542 | 49 | 25. Qh4 | inaccuracy | excellent | precision | excellent | 0.0016 | 0.500 | no | Nd2 | - | -0.26 | -0.09 |
| 184828162542 | 50 | 25... Rc7 | mistake | inaccuracy | precision | inaccuracy | 0.0793 | 0.514 | no | Ng6 | Ng6 | +0.45 | +0.55 |
| 184828162542 | 53 | 27. Qh3 | great | best | precision | best | 0.0000 | 0.494 | yes | Qh3 | - | +0.06 | -0.02 |
| 184828162542 | 56 | 28... b6 | mistake | inaccuracy | precision | inaccuracy | 0.0593 | 0.460 | no | h5 | - | +0.85 | +0.55 |
| 184828162542 | 57 | 29. Rgf3 | miss | good | precision | good | 0.0486 | 0.587 | no | Bxa6 | Bxa6 | +0.24 | +0.24 |
| 184828162542 | 59 | 30. R3f2 | inaccuracy | good | precision | good | 0.0472 | 0.579 | no | Rc1 | Rc1 | +0.12 | -0.13 |
| 184828162542 | 61 | 31. Qf3 | mistake | good | precision | good | 0.0461 | 0.541 | no | Rc1 | Rc1 | -0.17 | -0.11 |
| 184828162542 | 62 | 31... Rcg7 | good | excellent | precision | excellent | 0.0175 | 0.518 | no | Ba4 | - | +0.01 | +0.11 |
| 184828162542 | 64 | 32... Nh4 | great | best | precision | best | 0.0000 | 0.720 | yes | Nh4 | - | -1.44 | -1.39 |
| 184828162542 | 67 | 34. Nd2 | mistake | inaccuracy | precision | inaccuracy | 0.0739 | 0.253 | no | Nc1 | Nc1 | -2.18 | -1.60 |
| 184828162542 | 68 | 34... Rg4 | inaccuracy | good | precision | good | 0.0242 | 0.735 | no | h4 | Qg6 | -1.50 | -1.36 |
| 184828162542 | 70 | 35... R4g7 | best | excellent | precision | excellent | 0.0052 | 0.720 | no | Rh4 | - | -1.50 | -1.72 |
| 184828162542 | 71 | 36. Rc1 | mistake | excellent | precision | excellent | 0.0141 | 0.251 | no | Rf3 | Nb1 | -2.63 | -1.84 |
| 184828162542 | 72 | 36... h4 | miss | good | precision | good | 0.0201 | 0.764 | no | Qh6 | Qg6 | -1.07 | -1.52 |
| 184828162542 | 73 | 37. b4 | mistake | inaccuracy | precision | inaccuracy | 0.0512 | 0.275 | no | Ba6 | Nb1 | -1.61 | -1.95 |
| 184828162542 | 74 | 37... axb4 | best | excellent | precision | excellent | 0.0136 | 0.776 | no | a4 | - | -1.61 | -1.65 |
| 184828162542 | 76 | 38... Bh5 | inaccuracy | mistake | precision | mistake | 0.1782 | 0.773 | no | Qh6 | Qh6 | -1.19 | -0.60 |
| 184828162542 | 77 | 39. Bb5 | mistake | blunder | precision | blunder | 0.3498 | 0.406 | no | Bxh5 | Bxh5 | -3.94 | -4.44 |
| 184828162542 | 82 | 41... Rxg2 | excellent | good | precision | good | 0.0227 | 0.947 | no | Qe7 | - | -3.65 | -3.93 |
| 184828162542 | 84 | 42... Qe7 | best | excellent | precision | excellent | 0.0072 | 0.932 | no | Qa7 | - | -3.65 | -3.98 |
| 184828162542 | 87 | 44. Rc8+ | excellent | best | precision | best | 0.0000 | 0.013 | yes | Rc8+ | - | -5.72 | -6.16 |
| 184829980734 | 5 | 3. g3 | book | good | precision | good | 0.0426 | 0.568 | no | d4 | - | +0.14 | +0.16 |
| 184829980734 | 19 | 10. Nc3 | excellent | best | precision | best | 0.0000 | 0.503 | yes | Nc3 | - | -0.01 | +0.00 |
| 184829980734 | 21 | 11. Re1 | best | excellent | precision | excellent | 0.0175 | 0.506 | no | Bg5 | - | -0.01 | -0.05 |
| 184829980734 | 22 | 11... Bg4 | good | excellent | precision | excellent | 0.0159 | 0.508 | no | h6 | - | +0.14 | +0.13 |
| 184829980734 | 24 | 12... Qd7 | excellent | best | precision | best | 0.0000 | 0.533 | yes | Qd7 | - | -0.29 | -0.29 |
| 184829980734 | 25 | 13. Qb3 | inaccuracy | good | precision | good | 0.0437 | 0.454 | no | Bg5 | Qd2 | -0.82 | -0.57 |
| 184829980734 | 31 | 16. Nc3 | inaccuracy | good | precision | good | 0.0399 | 0.387 | no | Qd3 | Qd3 | -1.05 | -0.97 |
| 184829980734 | 36 | 18... Ncxd4 | best | excellent | precision | excellent | 0.0094 | 0.559 | no | Nfxd4 | - | -0.26 | -0.26 |
| 184829980734 | 39 | 20. Qxd5 | great | best | precision | best | 0.0000 | 0.462 | yes | Qxd5 | - | -0.25 | -0.25 |
| 184829980734 | 50 | 25... Qd6 | inaccuracy | best | precision | best | 0.0000 | 0.932 | yes | Qd6 | Qg5 | -2.17 | -3.95 |
| 184873703892 | 9 | 5. Bd2 | book | best | precision | best | 0.0000 | 0.620 | yes | Bd2 | - | +0.48 | +0.56 |
| 184873703892 | 10 | 5... Bg4 | book | best | precision | best | 0.0000 | 0.412 | yes | Bg4 | - | +0.48 | +0.53 |
| 184873703892 | 13 | 7. Bc4 | good | best | precision | best | 0.0000 | 0.570 | yes | Bc4 | - | +0.33 | +0.40 |
| 184873703892 | 14 | 7... Qb6 | great | best | precision | best | 0.0000 | 0.437 | yes | Qb6 | - | +0.33 | +0.45 |
| 184873703892 | 15 | 8. Qe2 | mistake | blunder | precision | blunder | 0.2253 | 0.571 | no | Nge2 | Nge2 | -0.90 | -1.00 |
| 184873703892 | 17 | 9. O-O-O | inaccuracy | best | precision | best | 0.0000 | 0.629 | yes | O-O-O | d5 | +0.62 | +0.84 |
| 184873703892 | 19 | 10. d5 | good | mistake | precision | mistake | 0.1139 | 0.673 | no | Be3 | - | +0.35 | +0.23 |
| 184873703892 | 29 | 15. Kb1 | inaccuracy | good | precision | good | 0.0349 | 0.490 | no | Nf4 | Nf4 | -0.30 | -0.28 |
| 184873703892 | 33 | 17. Nxe6 | miss | inaccuracy | precision | inaccuracy | 0.0582 | 0.626 | no | Qg3 | Qg3 | +0.33 | +0.55 |
| 184873703892 | 36 | 18... Bd4 | blunder | mistake | precision | mistake | 0.1830 | 0.444 | no | g6 | - | +1.62 | +1.63 |
| 184873703892 | 40 | 20... fxe6 | inaccuracy | good | precision | good | 0.0334 | 0.505 | no | Qxe6 | Qxe6 | +0.26 | +0.16 |
| 184873703892 | 41 | 21. Qe1 | excellent | best | precision | best | 0.0000 | 0.525 | yes | Qe1 | - | +0.17 | +0.23 |
| 184873703892 | 44 | 22... e5 | good | inaccuracy | precision | inaccuracy | 0.0521 | 0.482 | no | Be5 | - | +0.37 | +0.45 |
| 184873703892 | 45 | 23. Nxd4 | excellent | good | precision | good | 0.0362 | 0.571 | no | Bg5 | - | +0.27 | +0.22 |
| 184873703892 | 47 | 24. Bg5 | excellent | best | precision | best | 0.0000 | 0.543 | yes | Bg5 | - | +0.25 | +0.19 |
| 184873703892 | 48 | 24... Qd5 | inaccuracy | mistake | precision | mistake | 0.1034 | 0.470 | no | Qd6 | Qd6 | +0.80 | +0.86 |
| 184873703892 | 52 | 26... Qe5 | good | best | precision | best | 0.0000 | 0.356 | no | Qg5 | - | +0.98 | +0.88 |
| 184873703892 | 54 | 27... Qe2 | excellent | best | precision | best | 0.0000 | 0.365 | yes | Qe2 | - | +1.04 | +0.82 |
| 184873703892 | 55 | 28. Qd3 | best | excellent | precision | excellent | 0.0060 | 0.628 | no | Rg1 | - | +1.04 | +0.66 |
| 184873703892 | 57 | 29. Qf5+ | great | best | precision | best | 0.0000 | 0.644 | yes | Qf5+ | - | +1.04 | +0.83 |
| 184873703892 | 59 | 30. h4 | miss | inaccuracy | precision | inaccuracy | 0.0888 | 0.658 | no | Qxf6 | Qxf6 | +0.29 | +0.38 |
| 184873703892 | 60 | 30... a6 | good | excellent | precision | excellent | 0.0031 | 0.440 | no | Qe2 | - | +0.51 | +0.37 |
| 184873703892 | 63 | 32. Qf4 | good | best | precision | best | 0.0000 | 0.556 | yes | Qf4 | - | +0.39 | +0.34 |
| 184873703892 | 64 | 32... Rc6 | mistake | inaccuracy | precision | inaccuracy | 0.0958 | 0.446 | no | Qe2 | Qe2 | +1.04 | +1.04 |
| 184873703892 | 68 | 34... Qh3 | inaccuracy | good | precision | good | 0.0336 | 0.416 | no | Ka7 | Qd2 | +0.89 | +0.75 |
| 184873703892 | 70 | 35... Ka7 | best | good | precision | good | 0.0323 | 0.423 | no | Rh6 | - | +0.89 | +0.87 |
| 184873703892 | 71 | 36. Rd1 | excellent | best | precision | best | 0.0000 | 0.635 | yes | Rd1 | - | +0.88 | +0.87 |
| 184873703892 | 75 | 38. h5 | inaccuracy | excellent | precision | excellent | 0.0157 | 0.565 | no | Kb1 | Kb1 | +0.36 | +0.31 |
| 184873703892 | 77 | 39. Qf5 | great | best | precision | best | 0.0000 | 0.718 | yes | Qf5 | - | +1.42 | +1.63 |
| 184873703892 | 79 | 40. Kb1 | mistake | inaccuracy | precision | inaccuracy | 0.0649 | 0.713 | no | Re1 | Re1 | +0.91 | +0.84 |
| 184873703892 | 80 | 40... c4 | good | inaccuracy | precision | inaccuracy | 0.0760 | 0.369 | no | Qe2 | - | +1.09 | +1.38 |
| 184873703892 | 82 | 41... d3 | great | best | precision | best | 0.0000 | 0.416 | yes | d3 | - | +0.52 | +0.43 |
| 184873703892 | 85 | 43. Qd4+ | great | best | precision | best | 0.0000 | 0.607 | yes | Qd4+ | - | +0.83 | +0.77 |
| 184873703892 | 86 | 43... Ka8 | excellent | best | precision | best | 0.0000 | 0.380 | yes | Ka8 | - | +0.87 | +0.40 |
| 184873703892 | 92 | 46... Rb6+ | great | best | precision | best | 0.0000 | 0.500 | yes | Rb6+ | - | 0.00 | +0.00 |
| 184873703892 | 94 | 47... Qb5 | mistake | inaccuracy | precision | inaccuracy | 0.0959 | 0.500 | no | Qxf3 | Qh2+ | +0.70 | +0.61 |
| 184873703892 | 95 | 48. Rc1 | miss | inaccuracy | precision | inaccuracy | 0.0959 | 0.596 | no | Re1 | Re1 | 0.00 | +0.00 |
| 184873703892 | 96 | 48... Qb3+ | excellent | best | precision | best | 0.0000 | 0.500 | no | Ka8 | - | +0.09 | +0.00 |
| 185110487484 | 7 | 4. Bd3 | book | excellent | precision | excellent | 0.0032 | 0.535 | no | Nf3 | - | +0.13 | +0.20 |
| 185110487484 | 8 | 4... Nc6 | book | excellent | precision | excellent | 0.0032 | 0.468 | no | Bd6 | - | +0.16 | +0.23 |
| 185110487484 | 10 | 5... Bd6 | inaccuracy | good | precision | good | 0.0334 | 0.505 | no | Nb4 | Nb4 | +0.27 | +0.17 |
| 185110487484 | 11 | 6. O-O | good | excellent | precision | excellent | 0.0079 | 0.527 | no | c3 | - | +0.12 | +0.12 |
| 185110487484 | 18 | 9... Bf5 | good | excellent | precision | excellent | 0.0159 | 0.527 | no | c6 | - | +0.02 | -0.08 |
| 185110487484 | 19 | 10. Qg3 | good | excellent | precision | excellent | 0.0175 | 0.487 | no | Qd2 | - | -0.18 | -0.19 |
| 185110487484 | 20 | 10... Bxf4 | great | best | precision | best | 0.0000 | 0.530 | yes | Bxf4 | - | -0.18 | -0.07 |
| 185110487484 | 21 | 11. Nxf4 | best | excellent | precision | excellent | 0.0080 | 0.489 | no | Qxf4 | - | -0.18 | -0.13 |
| 185110487484 | 25 | 13. Rac1 | good | excellent | precision | excellent | 0.0191 | 0.484 | no | Qe3 | - | -0.31 | -0.28 |
| 185110487484 | 27 | 14. h4 | inaccuracy | excellent | precision | excellent | 0.0063 | 0.465 | no | Qh4 | Qh4 | -0.68 | -0.39 |
| 185110487484 | 28 | 14... Nf5 | mistake | inaccuracy | precision | inaccuracy | 0.0729 | 0.562 | no | c6 | h6 | +0.08 | +0.07 |
| 185110487484 | 30 | 15... Qxh4 | good | excellent | precision | excellent | 0.0095 | 0.494 | no | Nxh4 | - | +0.24 | +0.10 |
| 185110487484 | 35 | 18. Ne7+ | great | best | precision | best | 0.0000 | 0.529 | yes | Ne7+ | - | +0.24 | +0.14 |
| 185110487484 | 37 | 19. d5 | good | best | precision | best | 0.0000 | 0.518 | yes | d5 | - | +0.10 | +0.06 |
| 185110487484 | 39 | 20. Nfxd5 | best | excellent | precision | excellent | 0.0048 | 0.524 | no | Nexd5 | - | +0.10 | +0.07 |
| 185110487484 | 40 | 20... Nf5 | best | excellent | precision | excellent | 0.0191 | 0.489 | no | h6 | - | +0.10 | +0.21 |
| 185110487484 | 43 | 22. Re7 | best | excellent | precision | excellent | 0.0159 | 0.478 | no | Rc7 | - | -0.22 | -0.25 |
| 185110487484 | 46 | 23... Rac8 | great | best | precision | best | 0.0000 | 0.498 | yes | Rac8 | - | +0.04 | +0.02 |
| 185110487484 | 49 | 25. Ra1 | excellent | best | precision | best | 0.0000 | 0.475 | yes | Ra1 | - | -0.20 | -0.21 |
| 185110487484 | 51 | 26. Rxa7 | excellent | best | precision | best | 0.0000 | 0.479 | yes | Rxa7 | - | -0.23 | -0.07 |
| 185110487484 | 52 | 26... b5 | good | excellent | precision | excellent | 0.0032 | 0.511 | no | Rb8 | - | -0.11 | -0.07 |
| 185110487484 | 53 | 27. Rb7 | best | excellent | precision | excellent | 0.0080 | 0.489 | no | b3 | - | -0.11 | -0.08 |
| 185110487484 | 54 | 27... Kg8 | excellent | good | precision | good | 0.0207 | 0.513 | no | Rb8 | - | -0.02 | +0.05 |
| 185110487484 | 58 | 29... Rc1+ | best | excellent | precision | excellent | 0.0080 | 0.518 | no | h6 | - | -0.02 | +0.08 |
| 185110487484 | 60 | 30... Rc2 | good | best | precision | best | 0.0000 | 0.510 | yes | Rc2 | - | +0.19 | +0.00 |
| 185110487484 | 61 | 31. f3 | good | excellent | precision | excellent | 0.0064 | 0.500 | no | Kg1 | - | -0.04 | -0.11 |
| 185110487484 | 62 | 31... h6 | excellent | best | precision | best | 0.0000 | 0.518 | yes | h6 | - | +0.07 | -0.01 |
| 185110487484 | 63 | 32. Kg3 | good | excellent | precision | excellent | 0.0064 | 0.498 | no | Rbb7 | - | -0.15 | -0.05 |
| 185110487484 | 64 | 32... g6 | good | excellent | precision | excellent | 0.0016 | 0.508 | no | Rd8 | - | -0.02 | -0.04 |
| 185110487484 | 67 | 34. b4 | excellent | best | precision | best | 0.0000 | 0.500 | no | Kh3 | - | -0.13 | +0.00 |
| 185110487484 | 68 | 34... Rc6 | good | excellent | precision | excellent | 0.0032 | 0.500 | no | g5 | - | 0.00 | +0.02 |
| 185110487484 | 69 | 35. Rec7 | best | excellent | precision | excellent | 0.0032 | 0.503 | no | b5 | - | 0.00 | +0.00 |
| 185110487484 | 73 | 37. Rc4 | excellent | best | precision | best | 0.0000 | 0.530 | yes | Rc4 | - | -0.03 | +0.00 |
| 185110487484 | 74 | 37... Rb5 | good | best | precision | best | 0.0000 | 0.500 | no | g5 | - | +0.16 | +0.00 |
| 185110487484 | 75 | 38. Kf2 | good | best | precision | best | 0.0000 | 0.500 | no | Kf4 | - | 0.00 | +0.00 |
| 185110487484 | 76 | 38... Kf6 | best | excellent | precision | excellent | 0.0111 | 0.500 | no | Rd5 | - | 0.00 | +0.07 |
| 185110487484 | 77 | 39. g4 | excellent | good | precision | good | 0.0239 | 0.511 | no | Rf4+ | - | -0.03 | -0.08 |
| 185110487484 | 79 | 40. Kg3 | best | excellent | precision | excellent | 0.0111 | 0.498 | no | Ke3 | - | 0.00 | -0.08 |
| 185110487484 | 80 | 40... Kd5 | best | excellent | precision | excellent | 0.0127 | 0.513 | no | Ke6 | - | 0.00 | +0.00 |
| 185110487484 | 82 | 41... Ke6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Ke6 | - | +0.02 | +0.00 |
| 185110487484 | 83 | 42. Re4+ | excellent | best | precision | best | 0.0000 | 0.500 | yes | Re4+ | - | 0.00 | -0.07 |
| 185110487484 | 84 | 42... Kf6 | best | excellent | precision | excellent | 0.0080 | 0.511 | no | Re5 | - | 0.00 | -0.12 |
| 185110487484 | 86 | 43... g5 | excellent | good | precision | good | 0.0239 | 0.524 | no | Kg7 | - | 0.00 | +0.00 |
| 185110487484 | 88 | 44... Rd5 | best | excellent | precision | excellent | 0.0048 | 0.505 | no | Kg7 | - | -0.03 | +0.00 |
| 185110487484 | 89 | 45. Rc4 | best | excellent | precision | excellent | 0.0127 | 0.500 | no | Re3 | - | -0.03 | -0.20 |
| 185110487484 | 92 | 46... Rb3 | excellent | best | precision | best | 0.0000 | 0.521 | yes | Rb3 | - | 0.00 | +0.00 |
| 185110487484 | 95 | 48. Rxh6 | inaccuracy | excellent | precision | excellent | 0.0064 | 0.500 | no | Rc5+ | Rc4 | -0.35 | -0.12 |
| 185110487484 | 96 | 48... Rxb4 | good | excellent | precision | excellent | 0.0080 | 0.519 | no | Rb2+ | - | -0.14 | -0.15 |
| 185110487484 | 100 | 50... Rb3+ | great | best | precision | best | 0.0000 | 0.790 | yes | Rb3+ | - | -1.89 | -1.58 |
| 185110487484 | 101 | 51. Kg2 | excellent | best | precision | best | 0.0000 | 0.268 | yes | Kg2 | - | -1.93 | -4.24 |
| 185110487484 | 106 | 53... Kf3 | good | excellent | precision | excellent | 0.0000 | 0.963 | no | Ra6 | - | -3.19 | -5.15 |
| 185110487484 | 107 | 54. Rd8 | good | excellent | precision | excellent | 0.0091 | 0.036 | no | Rc8 | - | -3.92 | -4.39 |
| 185110487484 | 109 | 55. Rd3 | great | good | precision | good | 0.0221 | 0.462 | no | Rd4+ | - | -0.04 | +0.00 |
| 185110487484 | 110 | 55... Rb4 | excellent | best | precision | best | 0.0000 | 0.500 | no | Rb1 | - | 0.00 | +0.00 |
| 185110487484 | 114 | 57... Re3 | great | excellent | precision | excellent | 0.0037 | 0.995 | no | Re1 | - | -7.18 | -7.50 |
| 185110487484 | 115 | 58. Rxe3 | excellent | best | precision | best | 0.0000 | 0.008 | yes | Rxe3 | - | -9.62 | -8.41 |
| 185110487484 | 120 | 60... Kf3 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Ke5 | - | -9.95 | -8.45 |
| 185110487484 | 123 | 62. Kg2 | excellent | best | precision | best | 0.0000 | 0.001 | yes | Kg2 | - | -10.5 | -11.65 |
| 185117573448 | 5 | 3. h3 | good | excellent | precision | excellent | 0.0180 | 0.492 | no | Nf3 | - | -0.29 | -0.38 |
| 185117573448 | 7 | 4. a3 | excellent | good | precision | good | 0.0215 | 0.493 | no | Be2 | - | -0.48 | -0.41 |
| 185117573448 | 9 | 5. Nc3 | excellent | good | precision | good | 0.0263 | 0.486 | no | Be2 | - | -0.49 | -0.58 |
| 185117573448 | 10 | 5... d6 | excellent | good | precision | good | 0.0311 | 0.540 | no | d5 | - | -0.19 | -0.13 |
| 185117573448 | 11 | 6. Nf3 | excellent | best | precision | best | 0.0000 | 0.491 | yes | Nf3 | - | -0.27 | -0.28 |
| 185117573448 | 19 | 10. fxe3 | good | excellent | precision | excellent | 0.0111 | 0.506 | no | Qxe3 | - | -0.23 | -0.27 |
| 185117573448 | 22 | 11... Qd7 | good | excellent | precision | excellent | 0.0104 | 0.503 | no | c6 | - | +0.11 | +0.10 |
| 185117573448 | 26 | 13... exd4 | inaccuracy | good | precision | good | 0.0480 | 0.472 | no | Qe7 | Qe7 | +1.17 | +1.19 |
| 185117573448 | 37 | 19. Qg3 | excellent | best | precision | best | 0.0000 | 0.759 | yes | Qg3 | - | +3.95 | +4.10 |
| 185117573448 | 38 | 19... Re8 | best | excellent | precision | excellent | 0.0081 | 0.243 | no | Bf5 | - | +3.95 | +4.13 |
| 185117573448 | 43 | 22. Re1 | good | excellent | precision | excellent | 0.0031 | 0.760 | no | Rf4 | - | +3.55 | +3.91 |
| 185117573448 | 44 | 22... Rf5 | inaccuracy | good | precision | good | 0.0474 | 0.253 | no | f6 | Rxe1+ | +4.94 | +4.88 |
| 185117573448 | 47 | 24. Qe4 | good | excellent | precision | excellent | 0.0159 | 0.764 | no | Qh4 | - | +3.66 | +3.92 |
| 185117573448 | 52 | 26... Qd4+ | great | best | precision | best | 0.0000 | 0.865 | yes | Qd4+ | - | -6.57 | -7.01 |
| 185117573448 | 53 | 27. Re3 | mistake | good | precision | good | 0.0360 | 0.125 | no | Kh1 | Kh1 | -8.13 | -8.74 |
| 185117573448 | 62 | 31... Qxf1+ | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qxf1+ | - | -M3 | -M3 |
| 185117573448 | 65 | 33. c3 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | c3 | - | -M5 | -M5 |
| 185117573448 | 69 | 35. h4 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | g4 | a5 | -M6 | -M8 |
| 185117573448 | 70 | 35... a5 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd2 | - | -M5 | -M9 |
| 185117573448 | 73 | 37. axb5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | axb5 | - | -M6 | -M8 |
| 185117573448 | 74 | 37... a4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Bxb5 | - | -10.3 | -M16 |
| 185117573448 | 75 | 38. h6 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | g4 | - | -M7 | -13.87 |
| 185117573448 | 76 | 38... gxh6 | good | best | precision | best | 0.0000 | 0.979 | yes | gxh6 | - | -10.2 | -M7 |
| 185117573448 | 77 | 39. g3 | mistake | excellent | precision | excellent | 0.0000 | 0.000 | no | b6 | b6 | -M3 | -M4 |
| 185173941140 | 8 | 4... e5 | inaccuracy | good | precision | good | 0.0379 | 0.406 | no | g6 | Nf6 | +2.05 | +1.92 |
| 185173941140 | 9 | 5. Nf3 | best | excellent | precision | excellent | 0.0007 | 0.631 | no | Bd3 | - | +2.05 | +1.98 |
| 185173941140 | 11 | 6. Be3 | miss | inaccuracy | precision | inaccuracy | 0.0881 | 0.746 | no | Nxe5 | Nxe5 | +2.17 | +2.50 |
| 185173941140 | 12 | 6... e4 | good | inaccuracy | precision | inaccuracy | 0.0511 | 0.332 | no | Bb4 | - | +2.76 | +3.36 |
| 185173941140 | 13 | 7. Ng5 | excellent | good | precision | good | 0.0443 | 0.720 | no | Ne5 | - | +2.48 | +2.90 |
| 185173941140 | 16 | 8... Qxd1+ | best | excellent | precision | excellent | 0.0177 | 0.293 | no | Nh6 | - | +3.07 | +3.37 |
| 185173941140 | 22 | 11... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0896 | 0.284 | no | Nf6 | - | +4.99 | +5.06 |
| 185173941140 | 23 | 12. Rxe4+ | great | best | precision | best | 0.0000 | 0.805 | yes | Rxe4+ | - | +4.99 | +5.11 |
| 185173941140 | 35 | 18. Nxa8 | great | best | precision | best | 0.0000 | 0.514 | yes | Nxa8 | - | +0.35 | +0.03 |
| 185173941140 | 40 | 20... Bxh1 | great | best | precision | best | 0.0000 | 0.821 | yes | Bxh1 | - | -5.54 | -5.34 |
| 185193771738 | 8 | 4... Nxd4 | good | inaccuracy | precision | inaccuracy | 0.0529 | 0.481 | no | g6 | - | +0.96 | +0.97 |
| 185193771738 | 12 | 6... Nf6 | excellent | good | precision | good | 0.0229 | 0.485 | no | b6 | - | +0.41 | +0.51 |
| 185193771738 | 14 | 7... Qb6 | inaccuracy | good | precision | good | 0.0474 | 0.463 | no | h6 | h6 | +1.10 | +1.15 |
| 185193771738 | 15 | 8. Qxb6 | great | best | precision | best | 0.0000 | 0.584 | yes | Qxb6 | - | +1.10 | +1.11 |
| 185193771738 | 17 | 9. Bxf6 | good | excellent | precision | excellent | 0.0182 | 0.573 | no | Nd2 | - | +0.69 | +0.76 |
| 185193771738 | 22 | 11... Bd6 | excellent | good | precision | good | 0.0213 | 0.466 | no | d6 | - | +0.87 | +0.75 |
| 185193771738 | 26 | 13... b5 | good | excellent | precision | excellent | 0.0162 | 0.467 | no | Rc5 | - | +1.03 | +0.66 |
| 185193771738 | 28 | 14... b6 | inaccuracy | good | precision | good | 0.0274 | 0.504 | no | Ke7 | Ke7 | +0.69 | +0.32 |
| 185193771738 | 29 | 15. b4 | inaccuracy | good | precision | good | 0.0393 | 0.524 | no | Nd4 | Nd4 | -0.26 | -0.21 |
| 185193771738 | 31 | 16. Bxb5 | good | inaccuracy | precision | inaccuracy | 0.0503 | 0.546 | no | Nd4 | - | 0.00 | -0.06 |
| 185193771738 | 36 | 18... Bb7 | inaccuracy | best | precision | best | 0.0000 | 0.351 | yes | Bb7 | f5 | +2.76 | +2.61 |
| 185193771738 | 39 | 20. Re3 | best | excellent | precision | excellent | 0.0022 | 0.500 | no | Nh4 | - | -0.01 | -0.11 |
| 185193771738 | 40 | 20... f5 | excellent | best | precision | best | 0.0000 | 0.508 | yes | f5 | - | +0.04 | +0.10 |
| 185193771738 | 41 | 21. Nh4 | excellent | good | precision | good | 0.0215 | 0.507 | no | g3 | - | -0.13 | -0.19 |
| 185193771738 | 44 | 22... Rxh4 | great | best | precision | best | 0.0000 | 0.521 | yes | Rxh4 | - | -0.35 | -0.30 |
| 185193771738 | 46 | 23... fxe4 | good | excellent | precision | excellent | 0.0059 | 0.518 | no | Rxe4 | - | -0.03 | -0.10 |
| 185193771738 | 47 | 24. Rae1 | inaccuracy | good | precision | good | 0.0406 | 0.493 | no | g3 | Rf1 | -0.90 | -0.65 |
| 185193771738 | 51 | 26. Rg3 | good | best | precision | best | 0.0000 | 0.337 | yes | Rg3 | - | -2.33 | -2.36 |
| 185193771738 | 52 | 26... Kf6 | good | excellent | precision | excellent | 0.0013 | 0.668 | no | Ra7 | - | -1.88 | -2.46 |
| 185193771738 | 55 | 28. Rd8 | mistake | inaccuracy | precision | inaccuracy | 0.0863 | 0.379 | no | Rd1 | Rd1 | -2.68 | -2.97 |
| 185193771738 | 60 | 30... Rg6 | inaccuracy | good | precision | good | 0.0473 | 0.763 | no | e3 | e3 | -2.48 | -3.12 |
| 185193771738 | 62 | 31... Rg7 | good | inaccuracy | precision | inaccuracy | 0.0544 | 0.817 | no | Bc5+ | - | -3.65 | -3.93 |
| 185193771738 | 63 | 32. Bh5 | good | inaccuracy | precision | inaccuracy | 0.0623 | 0.238 | no | Bc4 | - | -4.58 | -5.22 |
| 185193771738 | 65 | 33. Re8+ | good | excellent | precision | excellent | 0.0120 | 0.209 | no | g3 | - | -4.19 | -4.87 |
| 185193771738 | 67 | 34. c4 | inaccuracy | good | precision | good | 0.0499 | 0.198 | no | Kh1 | - | -5.45 | -5.89 |
| 185193771738 | 68 | 34... f3 | good | excellent | precision | excellent | 0.0148 | 0.851 | no | Ra2 | - | -4.98 | -5.61 |
| 185193771738 | 73 | 37. Bxf3 | excellent | best | precision | best | 0.0000 | 0.077 | yes | Bxf3 | - | -9.39 | -8.60 |
| 185193771738 | 80 | 40... Rf7 | excellent | good | precision | good | 0.0271 | 0.967 | no | e4 | - | -9.15 | -9.46 |
| 185193771738 | 83 | 42. h3 | inaccuracy | best | precision | best | 0.0000 | 0.067 | yes | h3 | Ke1 | -M8 | -10.43 |
| 185217478440 | 10 | 5... Nf6 | best | excellent | precision | excellent | 0.0014 | 0.492 | no | d6 | - | +0.16 | +0.17 |
| 185217478440 | 11 | 6. O-O | excellent | best | precision | best | 0.0000 | 0.512 | yes | O-O | - | +0.14 | +0.11 |
| 185217478440 | 12 | 6... d6 | excellent | best | precision | best | 0.0000 | 0.492 | yes | d6 | - | +0.20 | +0.13 |
| 185217478440 | 13 | 7. Be3 | good | excellent | precision | excellent | 0.0049 | 0.509 | no | Na4 | - | -0.25 | +0.06 |
| 185217478440 | 16 | 8... exd4 | best | good | precision | good | 0.0331 | 0.464 | no | Bxd4 | - | +0.90 | +0.86 |
| 185217478440 | 22 | 11... a6 | good | excellent | precision | excellent | 0.0174 | 0.483 | no | c6 | - | +0.44 | +0.50 |
| 185217478440 | 25 | 13. Re1 | excellent | best | precision | best | 0.0000 | 0.527 | yes | Re1 | - | +0.45 | +0.34 |
| 185217478440 | 26 | 13... Bg4 | excellent | good | precision | good | 0.0305 | 0.476 | no | Nxd5 | - | +0.75 | +0.78 |
| 185217478440 | 27 | 14. h3 | best | excellent | precision | excellent | 0.0021 | 0.554 | no | Nf4 | - | +0.75 | +0.73 |
| 185217478440 | 28 | 14... Bxf3 | excellent | good | precision | good | 0.0322 | 0.449 | no | Be6 | - | +0.94 | +1.11 |
| 185217478440 | 34 | 17... b5 | good | excellent | precision | excellent | 0.0157 | 0.428 | no | g6 | - | +1.17 | +1.27 |
| 185217478440 | 36 | 18... a5 | excellent | good | precision | good | 0.0317 | 0.459 | no | c5 | - | +0.88 | +1.05 |
| 185217478440 | 37 | 19. e5 | excellent | good | precision | good | 0.0248 | 0.573 | no | Rad1 | - | +0.73 | +0.69 |
| 185217478440 | 41 | 21. Re3 | miss | mistake | precision | mistake | 0.1897 | 0.536 | no | dxe5 | dxe5 | -1.90 | -2.28 |
| 185217478440 | 43 | 22. Rg3 | good | excellent | precision | excellent | 0.0063 | 0.342 | no | Rf3 | - | -2.26 | -2.63 |
| 185217478440 | 44 | 22... Qf6 | excellent | good | precision | good | 0.0237 | 0.676 | no | Qe8 | - | -2.08 | -2.24 |
| 185217478440 | 47 | 24. Rxg6+ | great | best | precision | best | 0.0000 | 0.817 | yes | Rxg6+ | - | +5.51 | +6.09 |
| 185217478440 | 53 | 27. Bc2 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qg6+ | - | M5 | M5 |
| 185217478440 | 63 | 32. Re1 | inaccuracy | good | precision | good | 0.0383 | 0.889 | no | Kg3 | - | +5.80 | +6.23 |
| 185217478440 | 65 | 33. Qxf8+ | best | excellent | precision | excellent | 0.0078 | 0.836 | no | g4 | - | +5.80 | +5.55 |
| 185217478440 | 67 | 34. Ke2 | best | excellent | precision | excellent | 0.0004 | 0.826 | no | Ke3 | - | +5.80 | +6.21 |
| 185217478440 | 68 | 34... b4 | excellent | best | precision | best | 0.0000 | 0.150 | yes | b4 | - | +6.01 | +5.99 |
| 185217478440 | 69 | 35. Kd3 | good | excellent | precision | excellent | 0.0087 | 0.842 | no | h4 | - | +5.50 | +6.13 |
| 185217478440 | 70 | 35... c5 | good | excellent | precision | excellent | 0.0004 | 0.153 | no | Kf7 | - | +6.11 | +6.36 |
| 185217478440 | 71 | 36. Kc4 | good | excellent | precision | excellent | 0.0129 | 0.855 | no | Re5 | - | +5.36 | +6.00 |
| 185217478440 | 72 | 36... c2 | inaccuracy | excellent | precision | excellent | 0.0076 | 0.158 | no | Kg7 | - | +6.63 | +6.21 |
| 185217478440 | 75 | 38. axb3 | excellent | best | precision | best | 0.0000 | 0.887 | yes | axb3 | - | +7.53 | +8.02 |
| 185218140778 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.513 | yes | Nf6 | - | +0.07 | -0.10 |
| 185218140778 | 12 | 6... Bb7 | good | excellent | precision | excellent | 0.0084 | 0.482 | no | O-O | - | +0.59 | +0.40 |
| 185218140778 | 19 | 10. Nc4 | good | inaccuracy | precision | inaccuracy | 0.0589 | 0.609 | no | d4 | - | +0.93 | +0.77 |
| 185218140778 | 21 | 11. Ncxe5 | inaccuracy | good | precision | good | 0.0236 | 0.571 | no | d4 | d4 | +0.34 | +0.77 |
| 185218140778 | 26 | 13... O-O | excellent | best | precision | best | 0.0000 | 0.454 | yes | O-O | - | +0.78 | +0.78 |
| 185218140778 | 27 | 14. Bg4 | good | excellent | precision | excellent | 0.0188 | 0.555 | no | Qb3 | - | +0.22 | +0.34 |
| 185218140778 | 31 | 16. Qe2 | excellent | good | precision | good | 0.0274 | 0.730 | no | Qf3 | - | +2.84 | +3.14 |
| 185218140778 | 33 | 17. g3 | good | mistake | precision | mistake | 0.1136 | 0.727 | no | Bxd7 | - | +2.25 | +1.64 |
| 185218140778 | 36 | 18... Bxe4+ | good | inaccuracy | precision | inaccuracy | 0.0510 | 0.564 | no | Qxe4+ | - | -0.08 | -0.07 |
| 185218140778 | 38 | 19... Bxf3+ | excellent | best | precision | best | 0.0000 | 0.508 | yes | Bxf3+ | - | -0.07 | -0.16 |
| 185218140778 | 52 | 26... c6 | excellent | best | precision | best | 0.0000 | 0.239 | yes | c6 | - | +3.94 | +4.16 |
| 185218140778 | 53 | 27. Kf3 | excellent | best | precision | best | 0.0000 | 0.763 | yes | Kf3 | - | +3.93 | +3.99 |
| 185218140778 | 56 | 28... Ke6 | best | excellent | precision | excellent | 0.0092 | 0.227 | no | Kf7 | - | +4.16 | +4.55 |
| 185218140778 | 59 | 30. Re7 | best | excellent | precision | excellent | 0.0033 | 0.785 | no | Re5+ | - | +4.57 | +5.08 |
| 185218140778 | 60 | 30... Kd6 | good | excellent | precision | excellent | 0.0182 | 0.193 | no | d6 | - | +5.40 | +5.51 |
| 185218140778 | 63 | 32. Rxh7 | best | excellent | precision | excellent | 0.0027 | 0.835 | no | Ke4 | - | +5.73 | +5.68 |
| 185218140778 | 64 | 32... a4 | best | excellent | precision | excellent | 0.0016 | 0.168 | no | Ke6 | - | +5.73 | +5.75 |
| 185218140778 | 65 | 33. Rh6+ | good | excellent | precision | excellent | 0.0112 | 0.834 | no | Ke4 | - | +5.28 | +5.47 |
| 185218140778 | 66 | 33... Kc7 | good | excellent | precision | excellent | 0.0150 | 0.177 | no | Kd5 | - | +5.96 | +5.78 |
| 185218140778 | 67 | 34. Ke4 | best | excellent | precision | excellent | 0.0047 | 0.836 | no | Rf6 | - | +5.96 | +5.78 |
| 185218140778 | 68 | 34... Ba5 | best | excellent | precision | excellent | 0.0031 | 0.164 | no | Kc8 | - | +5.96 | +6.15 |
| 185218140778 | 69 | 35. Kd3 | best | excellent | precision | excellent | 0.0107 | 0.849 | no | a3 | - | +5.96 | +5.76 |
| 185218140778 | 73 | 37. Kc4 | good | excellent | precision | excellent | 0.0110 | 0.845 | no | h4 | - | +5.66 | +5.74 |
| 185218140778 | 75 | 38. b3 | good | excellent | precision | excellent | 0.0089 | 0.839 | no | Rf6 | - | +5.62 | +5.63 |
| 185218140778 | 79 | 40. d5 | good | excellent | precision | excellent | 0.0199 | 0.867 | no | b4 | - | +5.58 | +6.09 |
| 185218140778 | 80 | 40... d6 | mistake | best | precision | best | 0.0000 | 0.153 | yes | d6 | Be1 | +6.31 | +6.32 |
| 185277691132 | 8 | 4... Nf6 | book | good | precision | good | 0.0245 | 0.415 | no | Nd7 | - | +0.80 | +0.70 |
| 185277691132 | 9 | 5. Nxf6+ | book | best | precision | best | 0.0000 | 0.610 | yes | Nxf6+ | - | +0.80 | +0.79 |
| 185277691132 | 10 | 5... gxf6 | book | best | precision | best | 0.0000 | 0.377 | yes | gxf6 | - | +0.80 | +0.86 |
| 185277691132 | 11 | 6. Nf3 | book | best | precision | best | 0.0000 | 0.634 | yes | Nf3 | - | +0.80 | +0.91 |
| 185277691132 | 13 | 7. Bd3 | good | inaccuracy | precision | inaccuracy | 0.0759 | 0.644 | no | Bc4 | - | +0.53 | +0.43 |
| 185277691132 | 17 | 9. c4 | best | excellent | precision | excellent | 0.0170 | 0.720 | no | Qe2 | - | +1.32 | +1.28 |
| 185277691132 | 19 | 10. b3 | miss | inaccuracy | precision | inaccuracy | 0.0857 | 0.796 | no | O-O | O-O | +1.35 | +1.41 |
| 185277691132 | 20 | 10... Bb4+ | inaccuracy | good | precision | good | 0.0377 | 0.289 | no | f5 | f5 | +1.74 | +1.67 |
| 185277691132 | 22 | 11... Bxd2+ | excellent | best | precision | best | 0.0000 | 0.238 | yes | Bxd2+ | - | +1.75 | +1.92 |
| 185277691132 | 25 | 13. Qh6 | good | inaccuracy | precision | inaccuracy | 0.0619 | 0.889 | no | Bxb7 | - | +2.29 | +2.46 |
| 185277691132 | 30 | 15... Qe7 | inaccuracy | best | precision | best | 0.0000 | 0.322 | yes | Qe7 | a5 | +1.32 | +0.99 |
| 185277691132 | 31 | 16. Kc2 | mistake | inaccuracy | precision | inaccuracy | 0.0861 | 0.653 | no | Rd2 | Rd2 | +0.64 | +0.42 |
| 185277691132 | 32 | 16... O-O-O | inaccuracy | mistake | precision | mistake | 0.1019 | 0.434 | no | Rg8 | Rg8 | +0.95 | +0.75 |
| 185277691132 | 34 | 17... Kb7 | inaccuracy | good | precision | good | 0.0358 | 0.444 | no | Qa3 | Qa3 | +0.84 | +0.58 |
| 185277691132 | 35 | 18. a4 | inaccuracy | good | precision | good | 0.0202 | 0.591 | no | Re3 | Rhd1 | +0.50 | +0.45 |
| 185277691132 | 38 | 19... Rhg8 | mistake | inaccuracy | precision | inaccuracy | 0.0975 | 0.500 | no | e5 | Rhe8 | +0.92 | +0.62 |
| 185277691132 | 39 | 20. Re1 | inaccuracy | good | precision | good | 0.0263 | 0.597 | no | Qxh7 | Rhd1 | +0.53 | +0.45 |
| 185277691132 | 42 | 21... Rgg8 | mistake | blunder | precision | blunder | 0.2257 | 0.377 | no | Qa3 | - | +2.35 | +2.71 |
| 185277691132 | 44 | 22... Ra8 | good | excellent | precision | excellent | 0.0049 | 0.155 | no | Qa3 | - | +2.66 | +2.72 |
| 185277691132 | 45 | 23. Qc3 | excellent | best | precision | best | 0.0000 | 0.850 | yes | Qc3 | - | +2.49 | +2.68 |
| 185277691132 | 46 | 23... Rgb8 | excellent | good | precision | good | 0.0282 | 0.154 | no | Nd7 | - | +2.59 | +3.05 |
| 185277691132 | 47 | 24. Rb1 | excellent | good | precision | good | 0.0299 | 0.875 | no | Kd1 | - | +2.35 | +2.66 |
| 185277691132 | 49 | 25. Rdd1 | excellent | good | precision | good | 0.0219 | 0.861 | no | Qe1 | - | +2.28 | +2.59 |
| 185277691132 | 61 | 31. Rf1 | excellent | best | precision | best | 0.0000 | 0.949 | yes | Rf1 | - | +4.37 | +4.45 |
| 185277691132 | 65 | 33. Rxh7 | excellent | good | precision | good | 0.0220 | 0.955 | no | Qe4 | - | +3.71 | +4.13 |
| 185277691132 | 68 | 34... c5 | excellent | good | precision | good | 0.0335 | 0.068 | no | Rb4 | - | +4.86 | +5.25 |
| 185277691132 | 71 | 36. Rf8+ | excellent | good | precision | good | 0.0223 | 0.965 | no | Qe4 | - | +4.26 | +4.32 |
| 185277691132 | 77 | 39. Qe8+ | best | excellent | precision | excellent | 0.0060 | 0.944 | no | Qf1 | - | +4.26 | +4.43 |
| 185277691132 | 78 | 39... Kb7 | excellent | best | precision | best | 0.0000 | 0.056 | yes | Kb7 | - | +4.38 | +4.45 |
| 185277691132 | 92 | 46... Qf3+ | excellent | best | precision | best | 0.0000 | 0.966 | yes | Qf3+ | - | -4.84 | -4.98 |
| 185277691132 | 94 | 47... Qf2+ | best | excellent | precision | excellent | 0.0122 | 0.968 | no | Qe2+ | - | -4.84 | -4.80 |
| 185277691132 | 102 | 51... Qg2+ | excellent | best | precision | best | 0.0000 | 0.960 | yes | Qg2+ | - | -4.89 | -4.77 |
| 185277691132 | 103 | 52. Kb3 | best | excellent | precision | excellent | 0.0027 | 0.046 | no | Kc3 | - | -4.89 | -4.97 |
| 185277691132 | 106 | 53... Qf3+ | good | inaccuracy | precision | inaccuracy | 0.0719 | 0.973 | no | Rxa4 | - | -3.57 | -3.46 |
| 185277691132 | 112 | 56... Qc2+ | best | excellent | precision | excellent | 0.0169 | 0.851 | no | Kb8 | - | -2.39 | -3.43 |
| 185328167888 | 4 | 2... Nf6 | best | excellent | precision | excellent | 0.0021 | 0.523 | no | d5 | - | -0.43 | -0.34 |
| 185328167888 | 9 | 5. g4 | miss | mistake | precision | mistake | 0.1009 | 0.506 | no | b5 | b5 | -1.40 | -1.35 |
| 185328167888 | 11 | 6. Bg2 | good | excellent | precision | excellent | 0.0182 | 0.401 | no | e3 | - | -1.71 | -1.68 |
| 185328167888 | 12 | 6... e4 | inaccuracy | good | precision | good | 0.0499 | 0.617 | no | a5 | a5 | -0.84 | -0.95 |
| 185328167888 | 13 | 7. e3 | inaccuracy | good | precision | good | 0.0432 | 0.433 | no | c4 | c4 | -1.40 | -1.58 |
| 185328167888 | 17 | 9. f4 | excellent | best | precision | best | 0.0000 | 0.355 | yes | f4 | - | -2.02 | -2.34 |
| 185328167888 | 21 | 11. Bc3 | inaccuracy | good | precision | good | 0.0227 | 0.596 | no | Bd4 | Bd4 | +0.79 | +1.08 |
| 185328167888 | 24 | 12... Rg6 | good | inaccuracy | precision | inaccuracy | 0.0504 | 0.313 | no | Kf8 | - | +3.02 | +3.51 |
| 185328167888 | 26 | 13... Nf8 | great | best | precision | best | 0.0000 | 0.525 | yes | Nf8 | - | -0.06 | -0.20 |
| 185328167888 | 34 | 17... Nd5 | miss | inaccuracy | precision | inaccuracy | 0.0629 | 0.869 | no | Bxf4 | Bxf4 | -4.30 | -5.03 |
| 185328167888 | 35 | 18. Bh8 | mistake | good | precision | good | 0.0276 | 0.194 | no | Nf3 | dxe4 | -5.56 | -5.69 |
| 185328167888 | 37 | 19. Qxe4+ | best | good | precision | good | 0.0209 | 0.186 | no | Qf1 | - | -5.56 | -5.59 |
| 185328167888 | 43 | 22. O-O-O | best | excellent | precision | excellent | 0.0073 | 0.695 | no | Ne2 | - | +2.79 | +2.93 |
| 185328167888 | 46 | 23... Re8 | good | inaccuracy | precision | inaccuracy | 0.0548 | 0.313 | no | N8g6 | - | +3.61 | +3.73 |
| 185328167888 | 47 | 24. Nxg5 | inaccuracy | good | precision | good | 0.0493 | 0.742 | no | Rde1 | Rde1 | +2.27 | +2.87 |
| 185330935602 | 6 | 3... Nf6 | excellent | best | precision | best | 0.0000 | 0.572 | yes | Nf6 | - | -0.88 | -0.96 |
| 185330935602 | 12 | 6... d6 | excellent | best | precision | best | 0.0000 | 0.523 | yes | d6 | - | -0.29 | -0.41 |
| 185330935602 | 13 | 7. Qc3 | excellent | best | precision | best | 0.0000 | 0.470 | yes | Qc3 | - | -0.53 | -0.33 |
| 185330935602 | 14 | 7... Nc6 | good | excellent | precision | excellent | 0.0195 | 0.524 | no | c5 | - | 0.00 | +0.26 |
| 185330935602 | 15 | 8. Qb3 | excellent | best | precision | best | 0.0000 | 0.519 | yes | Qb3 | - | -0.07 | -0.10 |
| 185330935602 | 16 | 8... Qe7 | inaccuracy | good | precision | good | 0.0497 | 0.507 | no | Ne5 | Ne5 | +0.90 | +0.59 |
| 185330935602 | 17 | 9. Qa4 | mistake | inaccuracy | precision | inaccuracy | 0.0800 | 0.542 | no | Be2 | Nf3 | -0.64 | -0.52 |
| 185330935602 | 19 | 10. Bxb5 | great | best | precision | best | 0.0000 | 0.638 | yes | Bxb5 | - | +1.77 | +2.04 |
| 185334658860 | 12 | 6... O-O | excellent | best | precision | best | 0.0000 | 0.516 | yes | O-O | - | -0.20 | -0.23 |
| 185334658860 | 15 | 8. Nf3 | great | best | precision | best | 0.0000 | 0.467 | yes | Nf3 | - | -0.51 | -0.58 |
| 185334658860 | 17 | 9. Nxd4 | excellent | best | precision | best | 0.0000 | 0.473 | yes | Nxd4 | - | -0.47 | -0.32 |
| 185334658860 | 20 | 10... Bc5 | good | excellent | precision | excellent | 0.0118 | 0.541 | no | Bb6 | - | -0.28 | -0.31 |
| 185334658860 | 25 | 13. Nc3 | excellent | good | precision | good | 0.0241 | 0.460 | no | Qd3 | - | -0.60 | -0.87 |
| 185334658860 | 26 | 13... Bg4 | inaccuracy | mistake | precision | mistake | 0.1178 | 0.564 | no | Nxe4 | Nxe4 | +0.85 | +0.73 |
| 185334658860 | 27 | 14. f3 | best | excellent | precision | excellent | 0.0037 | 0.554 | no | Qd3 | - | +0.85 | +0.66 |
| 185334658860 | 30 | 15... c5 | mistake | inaccuracy | precision | inaccuracy | 0.0914 | 0.468 | no | Bg6 | Bg6 | +1.64 | +1.71 |
| 185334658860 | 34 | 17... Bd8 | good | excellent | precision | excellent | 0.0195 | 0.436 | no | Bg6 | - | +1.15 | +1.14 |
| 185334658860 | 42 | 21... bxa6 | best | excellent | precision | excellent | 0.0167 | 0.440 | no | Nd7 | - | +0.87 | +1.00 |
| 185334658860 | 44 | 22... Rxa6 | excellent | best | precision | best | 0.0000 | 0.443 | yes | Rxa6 | - | +0.86 | +0.78 |
| 185334658860 | 49 | 25. Qc6 | good | best | precision | best | 0.0000 | 0.581 | yes | Qc6 | - | +0.91 | +1.19 |
| 185334658860 | 50 | 25... Bxc3 | blunder | mistake | precision | mistake | 0.1731 | 0.413 | no | Rb8 | - | +3.72 | +3.90 |
| 185334658860 | 53 | 27. Qc6 | excellent | good | precision | good | 0.0262 | 0.768 | no | Bf4 | - | +3.35 | +3.57 |
| 185363017994 | 6 | 3... d6 | book | good | precision | good | 0.0316 | 0.484 | no | Nf6 | - | +0.65 | +0.59 |
| 185363017994 | 11 | 6. Nxe7 | excellent | good | precision | good | 0.0209 | 0.497 | no | Bc4 | - | -0.27 | -0.33 |
| 185363017994 | 17 | 9. h3 | excellent | best | precision | best | 0.0000 | 0.483 | yes | h3 | - | -0.57 | -0.29 |
| 185363017994 | 21 | 11. Qg4 | excellent | good | precision | good | 0.0266 | 0.533 | no | b3 | - | +0.33 | +0.09 |
| 185363017994 | 22 | 11... O-O | excellent | good | precision | good | 0.0273 | 0.494 | no | h5 | - | +0.61 | +0.47 |
| 185363017994 | 28 | 14... exf4 | great | best | precision | best | 0.0000 | 0.705 | yes | exf4 | - | -2.95 | -3.06 |
| 185363017994 | 33 | 17. Ke2 | excellent | best | precision | best | 0.0000 | 0.252 | yes | Ke2 | - | -3.67 | -3.89 |
| 185363017994 | 50 | 25... Be5 | inaccuracy | good | precision | good | 0.0457 | 0.719 | no | Rde8 | Rde8 | -2.11 | -2.51 |
| 185363017994 | 54 | 27... c5 | good | inaccuracy | precision | inaccuracy | 0.0614 | 0.732 | no | Rfe8 | - | -2.52 | -2.47 |
| 185363017994 | 60 | 30... Qc3 | excellent | good | precision | good | 0.0213 | 0.690 | no | g6 | - | -2.44 | -2.56 |
| 185363017994 | 61 | 31. Rgd5 | best | excellent | precision | excellent | 0.0075 | 0.323 | no | Qf4 | - | -2.44 | -2.42 |
| 185363017994 | 70 | 35... Qxa2 | best | good | precision | good | 0.0336 | 0.752 | no | h6 | - | -3.64 | -3.25 |
| 185363017994 | 71 | 36. Qd7 | good | inaccuracy | precision | inaccuracy | 0.0820 | 0.282 | no | h4 | - | -4.66 | -4.82 |
| 185363017994 | 73 | 37. Rd1 | excellent | best | precision | best | 0.0000 | 0.201 | yes | Rd1 | - | -4.76 | -4.86 |
| 185363017994 | 77 | 39. e6 | mistake | inaccuracy | precision | inaccuracy | 0.0534 | 0.230 | no | Rf1 | - | -5.18 | -5.35 |
| 185363017994 | 79 | 40. Re1 | blunder | mistake | precision | mistake | 0.1469 | 0.201 | no | Kh2 | - | -M13 | -9.90 |
| 185363017994 | 81 | 41. Kg2 | best | excellent | precision | excellent | 0.0009 | 0.194 | no | Kh1 | - | -4.31 | -4.64 |
| 185363017994 | 82 | 41... Qb2+ | excellent | best | precision | best | 0.0000 | 0.792 | yes | Qb2+ | - | -4.20 | -4.35 |
| 185363017994 | 92 | 46... a5 | best | excellent | precision | excellent | 0.0058 | 0.519 | no | Qb7 | - | -0.21 | -0.18 |
| 185363017994 | 95 | 48. Qa2 | blunder | mistake | precision | mistake | 0.1375 | 0.235 | no | Kf2 | - | -8.21 | -7.71 |
| 185363017994 | 97 | 49. Ke1 | excellent | best | precision | best | 0.0000 | 0.279 | yes | Ke1 | - | -3.34 | -3.31 |
| 185363017994 | 101 | 51. Kc2 | good | excellent | precision | excellent | 0.0000 | 0.267 | no | Ke2 | - | -3.35 | -3.37 |
| 185363017994 | 102 | 51... Qc5+ | good | excellent | precision | excellent | 0.0046 | 0.725 | no | Qe4+ | - | -2.98 | -3.02 |
| 185363017994 | 103 | 52. Kb2 | inaccuracy | mistake | precision | mistake | 0.1656 | 0.295 | no | Kd3 | Kd3 | -3.99 | -5.26 |
| 185363017994 | 105 | 53. Ka1 | good | best | precision | best | 0.0000 | 0.174 | yes | Ka1 | - | -4.84 | -6.65 |
| 185461631884 | 10 | 5... dxc3 | excellent | good | precision | good | 0.0285 | 0.449 | no | Nf6 | - | +0.97 | +1.00 |
| 185461631884 | 11 | 6. O-O | good | excellent | precision | excellent | 0.0135 | 0.572 | no | Qb3 | - | +0.71 | +0.94 |
| 185461631884 | 12 | 6... Be7 | inaccuracy | excellent | precision | excellent | 0.0134 | 0.432 | no | Nc6 | Nc6 | +1.48 | +1.13 |
| 185461631884 | 13 | 7. Nxc3 | inaccuracy | good | precision | good | 0.0313 | 0.581 | no | Qb3 | Qb3 | +0.75 | +1.01 |
| 185461631884 | 16 | 8... O-O | best | excellent | precision | excellent | 0.0007 | 0.486 | no | Nc6 | - | +0.05 | +0.14 |
| 185461631884 | 22 | 11... Bf5 | good | excellent | precision | excellent | 0.0142 | 0.579 | no | Na6 | - | -0.81 | -0.87 |
| 185461631884 | 24 | 12... Nd7 | best | excellent | precision | excellent | 0.0061 | 0.635 | no | Na6 | - | -1.81 | -1.78 |
| 185461631884 | 27 | 14. Bd3 | best | excellent | precision | excellent | 0.0132 | 0.358 | no | Bf1 | - | -2.02 | -2.22 |
| 185461631884 | 28 | 14... Bxd3 | excellent | best | precision | best | 0.0000 | 0.655 | yes | Bxd3 | - | -1.89 | -2.17 |
| 185461631884 | 30 | 15... c4 | excellent | best | precision | best | 0.0000 | 0.659 | yes | c4 | - | -1.77 | -1.99 |
| 185461631884 | 31 | 16. Qd1 | inaccuracy | good | precision | good | 0.0390 | 0.360 | no | Qc2 | Qc2 | -2.53 | -2.59 |
| 185461631884 | 32 | 16... Nd7 | inaccuracy | good | precision | good | 0.0410 | 0.679 | no | Re8 | Re8 | -1.71 | -1.96 |
| 185461631884 | 33 | 17. Rb1 | best | excellent | precision | excellent | 0.0000 | 0.362 | no | Qc2 | - | -1.71 | -1.95 |
| 185461631884 | 36 | 18... a6 | excellent | good | precision | good | 0.0248 | 0.623 | no | Ne5 | - | -1.32 | -1.38 |
| 185461631884 | 42 | 21... dxe5 | excellent | good | precision | good | 0.0315 | 0.566 | no | Bxe5 | - | -0.59 | -0.46 |
| 185461631884 | 45 | 23. Rxb3 | excellent | best | precision | best | 0.0000 | 0.486 | yes | Rxb3 | - | -0.29 | -0.28 |
| 185461631884 | 66 | 33... Qxe3 | excellent | best | precision | best | 0.0000 | 0.552 | yes | Qxe3 | - | -0.62 | -0.58 |
| 185461631884 | 68 | 34... Be5+ | great | best | precision | best | 0.0000 | 0.908 | yes | Be5+ | - | -8.01 | -9.00 |
| 185461631884 | 69 | 35. g3 | excellent | best | precision | best | 0.0000 | 0.069 | yes | g3 | - | -8.18 | -7.98 |
| 185617589205 | 7 | 4. b3 | book | good | precision | good | 0.0366 | 0.519 | no | d4 | - | +0.12 | -0.11 |
| 185617589205 | 8 | 4... Bd6 | book | good | precision | good | 0.0430 | 0.518 | no | c5 | - | +0.19 | +0.16 |
| 185617589205 | 9 | 5. Bb2 | book | best | precision | best | 0.0000 | 0.525 | yes | Bb2 | - | +0.10 | +0.06 |
| 185617589205 | 10 | 5... O-O | book | best | precision | best | 0.0000 | 0.490 | yes | O-O | - | +0.13 | +0.08 |
| 185617589205 | 12 | 6... Nc6 | good | inaccuracy | precision | inaccuracy | 0.0508 | 0.505 | no | c5 | - | +0.26 | +0.29 |
| 185617589205 | 17 | 9. Qc2 | inaccuracy | good | precision | good | 0.0334 | 0.540 | no | Nb5 | - | -0.15 | +0.04 |
| 185617589205 | 20 | 10... Ng6 | mistake | inaccuracy | precision | inaccuracy | 0.0672 | 0.375 | no | Nc6 | Nc6 | +1.32 | +1.27 |
| 185617589205 | 23 | 12. Bd3 | great | best | precision | best | 0.0000 | 0.699 | yes | Bd3 | - | +1.32 | +1.30 |
| 185617589205 | 24 | 12... Nxe4 | best | excellent | precision | excellent | 0.0080 | 0.304 | no | Bxe4 | - | +1.32 | +1.31 |
| 185617589205 | 29 | 15. h5 | good | best | precision | best | 0.0000 | 0.726 | yes | h5 | - | +1.20 | +1.36 |
| 185617589205 | 34 | 17... Nd7 | inaccuracy | good | precision | good | 0.0283 | 0.296 | no | e4 | e4 | +1.54 | +1.65 |
| 185617589205 | 35 | 18. Qc6 | excellent | best | precision | best | 0.0000 | 0.741 | yes | Qc6 | - | +1.53 | +1.55 |
| 185617589205 | 37 | 19. d3 | excellent | best | precision | best | 0.0000 | 0.745 | yes | d3 | - | +1.57 | +1.60 |
| 185617589205 | 38 | 19... Rb6 | excellent | good | precision | good | 0.0229 | 0.265 | no | a5 | - | +1.62 | +1.67 |
| 185617589205 | 41 | 21. Rh4 | inaccuracy | excellent | precision | excellent | 0.0124 | 0.741 | no | Qc4 | Qc4 | +1.30 | +1.35 |
| 185617589205 | 49 | 25. Ng5 | excellent | good | precision | good | 0.0208 | 0.847 | no | Qc6 | - | +2.32 | +2.45 |
| 185617589205 | 53 | 27. Nf3 | great | best | precision | best | 0.0000 | 0.893 | yes | Nf3 | - | +2.97 | +2.83 |
| 185617589205 | 55 | 28. Qc6 | excellent | good | precision | good | 0.0267 | 0.890 | no | Qd6 | - | +2.66 | +2.87 |
| 185617589205 | 57 | 29. Qa8+ | best | good | precision | good | 0.0231 | 0.898 | no | Qa4 | - | +2.66 | +3.00 |
| 185617589205 | 58 | 29... Kg7 | excellent | best | precision | best | 0.0000 | 0.129 | yes | Kg7 | - | +2.86 | +3.09 |
| 185617589205 | 59 | 30. Rc6 | good | excellent | precision | excellent | 0.0028 | 0.877 | no | Rc8 | - | +2.52 | +3.05 |
| 185617589205 | 62 | 31... Nh5 | excellent | best | precision | best | 0.0000 | 0.085 | yes | Nh5 | - | +3.56 | +3.98 |
| 185617589205 | 63 | 32. Rc7 | good | excellent | precision | excellent | 0.0106 | 0.927 | no | Kf1 | - | +3.02 | +3.75 |
| 185617589205 | 64 | 32... Qxg2 | best | excellent | precision | excellent | 0.0152 | 0.084 | no | Kg8 | - | +3.02 | +4.69 |
| 185617589205 | 65 | 33. Bxe5+ | excellent | inaccuracy | precision | inaccuracy | 0.0514 | 0.952 | no | Rxf7+ | - | +3.00 | +3.54 |
| 185617589205 | 69 | 35. Kd1 | inaccuracy | excellent | precision | excellent | 0.0087 | 0.894 | no | Ke1 | Kd2 | +1.93 | +3.61 |
| 185617589205 | 70 | 35... Qf1+ | best | excellent | precision | excellent | 0.0095 | 0.091 | no | Nf5 | - | +1.93 | +2.97 |
| 185617589205 | 71 | 36. Kc2 | inaccuracy | mistake | precision | mistake | 0.1584 | 0.869 | no | Kd2 | - | +1.53 | +2.30 |
| 185617589205 | 73 | 37. Nd2 | excellent | best | precision | best | 0.0000 | 0.945 | yes | Nd2 | - | +3.99 | +4.74 |
| 185617589205 | 74 | 37... Nf5 | excellent | good | precision | good | 0.0223 | 0.047 | no | Rc8+ | - | +4.61 | +5.95 |
| 185617589205 | 75 | 38. Rxf5 | miss | mistake | precision | mistake | 0.1816 | 0.978 | no | Rxh7 | Rxh7 | +1.61 | +2.06 |
| 185617589205 | 79 | 40. Qa6 | great | best | precision | best | 0.0000 | 0.965 | yes | Qa6 | - | +4.51 | +5.33 |
| 185617589205 | 86 | 43... Kf7 | best | excellent | precision | excellent | 0.0020 | 0.021 | no | Kf8 | - | +5.62 | +6.18 |
| 185617589205 | 89 | 45. Qh8+ | best | excellent | precision | excellent | 0.0039 | 0.979 | no | Kb2 | - | +5.61 | +5.73 |
| 185617589205 | 92 | 46... Kc8 | excellent | best | precision | best | 0.0000 | 0.025 | yes | Kc8 | - | +6.26 | +5.95 |
| 185617589205 | 94 | 47... Rd7 | excellent | best | precision | best | 0.0000 | 0.028 | yes | Rd7 | - | +5.54 | +6.04 |
| 185617589205 | 102 | 51... Kxc6 | best | excellent | precision | excellent | 0.0004 | 0.017 | no | Rxc6 | - | +6.15 | +6.50 |
| 185617589205 | 106 | 53... Re7 | best | excellent | precision | excellent | 0.0042 | 0.019 | no | Rb7 | - | +5.84 | +6.60 |
| 185617589205 | 111 | 56. Nxf5 | good | excellent | precision | excellent | 0.0000 | 0.999 | no | f4 | - | +11.0 | +13.01 |
| 185966191317 | 10 | 5... Ne7 | book | best | precision | best | 0.0000 | 0.484 | yes | Ne7 | - | -0.05 | +0.11 |
| 185966191317 | 11 | 6. exd5 | book | best | precision | best | 0.0000 | 0.518 | yes | exd5 | - | -0.05 | +0.00 |
| 185966191317 | 12 | 6... exd5 | book | excellent | precision | excellent | 0.0064 | 0.500 | no | Nxd5 | - | +0.07 | +0.27 |
| 185966191317 | 13 | 7. Qe2 | book | best | precision | best | 0.0000 | 0.543 | yes | Qe2 | - | +0.07 | +0.19 |
| 185966191317 | 17 | 9. Ne4 | best | excellent | precision | excellent | 0.0030 | 0.620 | no | Na4 | - | +0.81 | +0.74 |
| 185966191317 | 18 | 9... Qb6 | mistake | blunder | precision | blunder | 0.2926 | 0.384 | no | d3 | d3 | +3.49 | +3.60 |
| 185966191317 | 19 | 10. Nd6+ | great | best | precision | best | 0.0000 | 0.908 | yes | Nd6+ | - | +3.49 | +3.57 |
| 185966191317 | 29 | 15. Nd6+ | excellent | good | precision | good | 0.0449 | 0.870 | no | d3 | - | +2.57 | +2.44 |
| 185966191317 | 31 | 16. b4 | good | inaccuracy | precision | inaccuracy | 0.0542 | 0.886 | no | a4 | - | +2.06 | +2.13 |
| 185966191317 | 34 | 17... Kxc5 | mistake | good | precision | good | 0.0384 | 0.042 | no | Kc7 | - | +9.48 | +9.26 |
| 185966191317 | 35 | 18. Ne4+ | excellent | good | precision | good | 0.0311 | 0.997 | no | Rb1 | - | +4.97 | +5.36 |
| 185966191317 | 39 | 20. Nxd4 | excellent | best | precision | best | 0.0000 | 0.987 | no | d3 | - | +6.36 | +6.79 |
| 185966191317 | 40 | 20... Bg4 | mistake | excellent | precision | excellent | 0.0086 | 0.013 | no | Qb6 | - | +8.19 | +8.48 |
| 186222389165 | 5 | 3. e3 | book | good | precision | good | 0.0269 | 0.554 | no | d4 | - | +0.10 | +0.17 |
| 186222389165 | 8 | 4... c5 | book | excellent | precision | excellent | 0.0175 | 0.495 | no | Be7 | - | +0.20 | +0.13 |
| 186222389165 | 10 | 5... a6 | book | excellent | precision | excellent | 0.0048 | 0.476 | no | Nc6 | - | +0.22 | +0.17 |
| 186222389165 | 11 | 6. dxc5 | book | excellent | precision | excellent | 0.0143 | 0.527 | no | cxd5 | - | +0.07 | +0.10 |
| 186222389165 | 12 | 6... Bxc5 | book | best | precision | best | 0.0000 | 0.484 | yes | Bxc5 | - | +0.07 | +0.07 |
| 186222389165 | 14 | 7... O-O | excellent | best | precision | best | 0.0000 | 0.530 | yes | O-O | - | -0.10 | -0.14 |
| 186222389165 | 19 | 10. a3 | mistake | inaccuracy | precision | inaccuracy | 0.0587 | 0.500 | no | b3 | b3 | -0.64 | -0.49 |
| 186222389165 | 20 | 10... d4 | miss | mistake | precision | mistake | 0.1235 | 0.577 | no | dxc4 | dxc4 | +0.35 | +0.29 |
| 186222389165 | 27 | 14. Be3 | inaccuracy | excellent | precision | excellent | 0.0191 | 0.500 | no | Bd2 | Bd2 | -0.14 | -0.07 |
| 186222389165 | 30 | 15... Bd7 | good | best | precision | best | 0.0000 | 0.524 | no | Qc7 | - | -0.02 | -0.13 |
| 186222389165 | 33 | 17. b4 | inaccuracy | good | precision | good | 0.0411 | 0.481 | no | Nxd7 | Nxd7 | -0.51 | -0.45 |
| 186222389165 | 35 | 18. Bf3 | excellent | best | precision | best | 0.0000 | 0.440 | yes | Bf3 | - | -0.58 | -0.34 |
| 186222389165 | 36 | 18... Qc7 | good | best | precision | best | 0.0000 | 0.554 | no | Bxf3 | - | -0.38 | -0.32 |
| 186222389165 | 37 | 19. c5 | great | best | precision | best | 0.0000 | 0.449 | yes | c5 | - | -0.38 | -0.47 |
| 186222389165 | 39 | 20. gxf3 | excellent | good | precision | good | 0.0344 | 0.449 | no | Rxf3 | - | -0.43 | -0.36 |
| 186222389165 | 40 | 20... Nd5 | excellent | best | precision | best | 0.0000 | 0.557 | yes | Nd5 | - | -0.36 | -0.25 |
| 186222389165 | 41 | 21. Nc4 | blunder | mistake | precision | mistake | 0.1976 | 0.460 | no | Nxd5 | - | -1.70 | -1.82 |
| 186222389165 | 42 | 21... b5 | great | best | precision | best | 0.0000 | 0.761 | yes | b5 | - | -1.70 | -1.84 |
| 186222389165 | 44 | 22... Nf4 | mistake | inaccuracy | precision | inaccuracy | 0.0861 | 0.760 | no | bxc4 | bxc4 | -1.10 | -1.24 |
| 186222389165 | 45 | 23. Ne3 | mistake | inaccuracy | precision | inaccuracy | 0.0990 | 0.312 | no | Nb2 | Nb2 | -1.96 | -2.05 |
| 186222389165 | 46 | 23... Rd3 | great | best | precision | best | 0.0000 | 0.787 | yes | Rd3 | - | -1.96 | -2.00 |
| 186222389165 | 48 | 24... Nh3+ | good | excellent | precision | excellent | 0.0033 | 0.780 | no | Rfd8 | - | -1.68 | -1.73 |
| 186222389165 | 53 | 27. Qc1 | good | best | precision | best | 0.0000 | 0.101 | yes | Qc1 | - | -3.60 | -3.69 |
| 186222389165 | 54 | 27... Qe5 | best | excellent | precision | excellent | 0.0194 | 0.913 | no | h6 | - | -3.60 | -3.34 |
| 186222389165 | 65 | 33. Re1 | excellent | best | precision | best | 0.0000 | 0.036 | yes | Re1 | - | -5.15 | -5.31 |
| 186222389165 | 70 | 35... Qd4+ | excellent | best | precision | best | 0.0000 | 0.972 | yes | Qd4+ | - | -5.03 | -5.34 |
| 186222389165 | 72 | 36... Qd5+ | best | excellent | precision | excellent | 0.0021 | 0.973 | no | Rc8 | - | -5.03 | -5.44 |
| 186222389165 | 75 | 38. Kg3 | best | excellent | precision | excellent | 0.0007 | 0.029 | no | a4 | - | -5.03 | -5.54 |
| 186222389165 | 76 | 38... Qd6 | excellent | best | precision | best | 0.0000 | 0.972 | yes | Qd6 | - | -4.99 | -5.32 |
| 186222389165 | 77 | 39. Qe3 | excellent | best | precision | best | 0.0000 | 0.033 | yes | Qe3 | - | -5.18 | -5.56 |
| 186222389165 | 87 | 44. Qg6 | excellent | best | precision | best | 0.0000 | 0.034 | yes | Qg6 | - | -5.42 | -5.64 |
| 186222389165 | 88 | 44... Rc3 | excellent | good | precision | good | 0.0227 | 0.973 | no | Kd8 | - | -4.72 | -4.64 |
| 186222389165 | 91 | 46. Qg8+ | excellent | best | precision | best | 0.0000 | 0.042 | yes | Qg8+ | - | -4.73 | -5.15 |
| 186222389165 | 94 | 47... Ke8 | excellent | best | precision | best | 0.0000 | 0.956 | yes | Ke8 | - | -4.67 | -4.83 |
| 186222389165 | 97 | 49. Qg7+ | great | best | precision | best | 0.0000 | 0.042 | yes | Qg7+ | - | -4.67 | +0.00 |
| 186411389477 | 12 | 6... h5 | good | excellent | precision | excellent | 0.0087 | 0.222 | no | Ng4 | - | +2.30 | +2.05 |
| 186411389477 | 15 | 8. Rf1 | good | excellent | precision | excellent | 0.0110 | 0.783 | no | O-O | - | +1.76 | +1.85 |
| 186411389477 | 16 | 8... Qd6 | excellent | best | precision | best | 0.0000 | 0.235 | yes | Qd6 | - | +1.83 | +2.01 |
| 186411389477 | 22 | 11... Qxc5 | inaccuracy | mistake | precision | mistake | 0.1280 | 0.203 | no | Qg6 | Qg6 | +3.21 | +3.95 |
| 186411389477 | 23 | 12. Qd4 | best | excellent | precision | excellent | 0.0138 | 0.925 | no | Be3 | - | +3.21 | +3.66 |
| 186411389477 | 27 | 14. Qc4 | great | best | precision | best | 0.0000 | 0.835 | yes | Qc4 | - | +2.26 | +2.34 |
| 186411389477 | 28 | 14... b5 | best | excellent | precision | excellent | 0.0066 | 0.184 | no | Bc6 | - | +2.26 | +2.49 |
| 186411389477 | 30 | 15... c4 | good | inaccuracy | precision | inaccuracy | 0.0533 | 0.183 | no | O-O | - | +2.78 | +2.99 |
| 186411389477 | 37 | 19. O-O-O | brilliant | excellent | precision | excellent | 0.0042 | 0.878 | no | Rf3 | - | +2.74 | +2.75 |
| 186411389477 | 39 | 20. Bf3 | best | excellent | precision | excellent | 0.0060 | 0.866 | no | Rde1 | - | +2.74 | +2.81 |
| 186411389477 | 48 | 24... Kh7 | excellent | best | precision | best | 0.0000 | 0.050 | yes | Kh7 | - | +4.91 | +5.19 |
| 186411389477 | 49 | 25. g4 | best | excellent | precision | excellent | 0.0104 | 0.965 | no | Qd5 | - | +4.91 | +4.99 |
| 186411389477 | 51 | 26. Qe5 | excellent | good | precision | good | 0.0243 | 0.976 | no | Qxh5+ | - | +4.53 | +4.69 |
| 186411389477 | 52 | 26... Qb6 | excellent | good | precision | good | 0.0299 | 0.048 | no | Qa6 | - | +6.36 | +6.27 |
| 186411389477 | 54 | 27... Bxc4 | excellent | best | precision | best | 0.0000 | 0.017 | yes | Bxc4 | - | +6.54 | +6.51 |
| 186411389477 | 74 | 37... Kf4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kh4 | - | +9.76 | +9.81 |
| 186411389477 | 76 | 38... g5 | inaccuracy | excellent | precision | excellent | 0.0005 | 0.001 | no | Kg3 | Kg3 | M8 | +13.74 |
| 186411389477 | 77 | 39. Rxg5 | good | excellent | precision | excellent | 0.0064 | 1.000 | no | Rb5 | - | +8.41 | +7.88 |
| 186411389477 | 81 | 41. g5 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Re4 | - | +14.8 | M12 |
| 186411389477 | 82 | 41... Kg4 | good | best | precision | best | 0.0000 | 0.000 | no | Kh5 | - | M6 | M16 |
| 186411389477 | 83 | 42. g6 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rfe5 | - | M5 | M6 |
| 186411389477 | 86 | 43... Kh4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kh2 | - | M3 | M3 |
| 186411389477 | 90 | 45... Kh4 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kg4 | - | M3 | M4 |
| 186411389477 | 92 | 46... Kg4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kh3 | - | M4 | M4 |
| 186411389477 | 96 | 48... Kg5 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kf4 | - | M3 | M3 |
| 186411389477 | 103 | 52. Rg1+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qf6 | - | M2 | M4 |
| 186411389477 | 104 | 52... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kf8 | - | M2 | M2 |
| 186429989523 | 8 | 4... h6 | good | excellent | precision | excellent | 0.0156 | 0.440 | no | dxe4 | - | +0.48 | +0.33 |
| 186429989523 | 9 | 5. Bxf6 | great | best | precision | best | 0.0000 | 0.552 | yes | Bxf6 | - | +0.48 | +0.44 |
| 186429989523 | 12 | 6... c6 | best | excellent | precision | excellent | 0.0187 | 0.438 | no | Qe7 | - | +0.48 | +0.51 |
| 186429989523 | 13 | 7. Nf3 | best | excellent | precision | excellent | 0.0031 | 0.581 | no | h4 | - | +0.48 | +0.52 |
| 186429989523 | 16 | 8... Qd8 | excellent | good | precision | good | 0.0270 | 0.482 | no | dxe4 | - | +0.24 | +0.28 |
| 186429989523 | 17 | 9. O-O | best | excellent | precision | excellent | 0.0016 | 0.544 | no | Qd2 | - | +0.24 | +0.21 |
| 186429989523 | 20 | 10... O-O | best | excellent | precision | excellent | 0.0016 | 0.468 | no | a5 | - | +0.23 | +0.17 |
| 186429989523 | 21 | 11. Qd3 | good | excellent | precision | excellent | 0.0175 | 0.527 | no | Bd3 | - | +0.08 | +0.06 |
| 186429989523 | 23 | 12. Rad1 | inaccuracy | good | precision | good | 0.0430 | 0.518 | no | Qd2 | Qe3 | -0.31 | -0.16 |
| 186429989523 | 24 | 12... b6 | inaccuracy | good | precision | good | 0.0302 | 0.525 | no | b5 | b5 | +0.06 | -0.13 |
| 186429989523 | 25 | 13. h3 | good | excellent | precision | excellent | 0.0016 | 0.479 | no | Qe3 | - | -0.19 | -0.14 |
| 186429989523 | 27 | 14. Nxe4 | inaccuracy | mistake | precision | mistake | 0.1037 | 0.602 | no | Qxe4 | Qxe4 | -0.06 | +0.07 |
| 186429989523 | 28 | 14... Bb7 | excellent | best | precision | best | 0.0000 | 0.489 | yes | Bb7 | - | +0.01 | +0.07 |
| 186429989523 | 30 | 15... Qc7 | good | excellent | precision | excellent | 0.0048 | 0.500 | no | c5 | - | +0.13 | +0.18 |
| 186429989523 | 36 | 18... c5 | good | best | precision | best | 0.0000 | 0.594 | yes | c5 | - | -0.31 | -0.42 |
| 186429989523 | 38 | 19... f5 | great | excellent | precision | excellent | 0.0048 | 0.855 | no | f6 | - | -3.04 | -3.23 |
| 186429989523 | 40 | 20... Bxe4 | best | excellent | precision | excellent | 0.0194 | 0.895 | no | fxe4 | - | -3.04 | -3.33 |
| 186429989523 | 43 | 22. dxc5 | excellent | good | precision | good | 0.0415 | 0.137 | no | Bh5 | - | -3.23 | -3.53 |
| 186429989523 | 44 | 22... bxc5 | excellent | good | precision | good | 0.0370 | 0.905 | no | Rc8 | - | -2.90 | -3.06 |
| 186429989523 | 50 | 25... Qf6 | excellent | good | precision | good | 0.0229 | 0.933 | no | Qd6 | - | -3.63 | -3.39 |
| 186429989523 | 51 | 26. Qxc5 | excellent | good | precision | good | 0.0442 | 0.103 | no | Qxf6 | - | -4.12 | -4.08 |
| 186429989523 | 66 | 33... Kf7 | excellent | best | precision | best | 0.0000 | 0.953 | yes | Kf7 | - | -4.63 | -4.61 |
| 186429989523 | 68 | 34... Rd7 | excellent | good | precision | good | 0.0291 | 0.960 | no | Bb5 | - | -4.10 | -4.02 |
| 186429989523 | 70 | 35... Bc4 | excellent | good | precision | good | 0.0286 | 0.970 | no | Bb5 | - | -4.51 | -4.37 |
| 186429989523 | 77 | 39. Kg2 | excellent | good | precision | good | 0.0240 | 0.051 | no | Ke1 | - | -5.96 | -5.32 |
| 186429989523 | 79 | 40. Rxh6 | excellent | best | precision | best | 0.0000 | 0.027 | yes | Rxh6 | - | -7.35 | -7.37 |

### `miss_detector` (14)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (tactic) | miss_detector | mistake | 0.1682 | 0.673 | no | g4 | - | -0.01 | +0.12 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1820 | 0.854 | no | Rxf6+ | Rxf6+ | +2.74 | +2.69 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.5023 | 0.823 | no | Rxf6+ | - | -2.81 | -2.68 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2523 | 0.759 | no | Kg7 | - | -0.17 | -0.09 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | mistake | 0.1560 | 0.156 | no | Kd2 | - | -M1 | -M1 |
| 184732665836 | 48 | 24... a6 | mistake | miss (tactic) | miss_detector | mistake | 0.1585 | 0.158 | no | Qe8 | - | M8 | M8 |
| 184784174152 | 27 | 14. Nxe5 | mistake | miss (tactic) | miss_detector | blunder | 0.3408 | 0.895 | no | Bf5 | Bf5 | +0.36 | +0.25 |
| 184829980734 | 34 | 17... Bxf3 | mistake | miss (opportunity) | miss_detector | blunder | 0.2216 | 0.757 | no | Nxe3 | Nxe3 | -0.26 | -0.22 |
| 185173941140 | 27 | 14. Bb5+ | mistake | miss (tactic) | miss_detector | blunder | 0.2463 | 0.814 | no | Nxf7 | Nxf7 | +0.69 | +0.97 |
| 185173941140 | 33 | 17. Bxc6+ | blunder | miss (tactic) | miss_detector | blunder | 0.2713 | 0.623 | no | Nxa8 | Nxa8 | -2.13 | -2.39 |
| 185173941140 | 37 | 19. Nxf7 | mistake | miss (free_piece) | miss_detector | blunder | 0.2009 | 0.514 | no | Nxe4 | Nxe4 | -2.17 | -2.70 |
| 185277691132 | 111 | 56. Rb4 | mistake | miss (opportunity) | miss_detector | mistake | 0.1849 | 0.358 | no | Rc1 | Rc1 | -2.39 | -2.74 |
| 185363017994 | 99 | 50. Kd2 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1444 | 0.409 | no | Qa3 | Qa3 | -2.92 | -3.55 |
| 185617589205 | 78 | 39... Rd8 | blunder | miss (tactic) | miss_detector | blunder | 0.3302 | 0.365 | no | Qxf2 | Qxf2 | +4.51 | +5.22 |

### `mate_override` (13)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M7 |
| 185209623352 | 142 | 71... Kb5 | good | inaccuracy | mate_override | inaccuracy | 0.0221 | 0.022 | no | Ka7 | - | M8 | M11 |
| 185437323918 | 93 | 47. d7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0322 | 0.032 | no | Kb6 | - | -11.0 | -M21 |
| 185437323918 | 97 | 49. Kd5 | best | inaccuracy | mate_override | inaccuracy | 0.0271 | 0.027 | no | d8=Q | - | -M16 | -M18 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |
| 185438707002 | 91 | 46. Kh4 | best | inaccuracy | mate_override | inaccuracy | 0.0711 | 0.071 | no | g5 | - | -M6 | -M6 |
| 184732665836 | 67 | 34. Qe4+ | excellent | good | mate_override | good | 0.0376 | 1.000 | no | Rf4+ | - | M15 | +11.18 |
| 185117573448 | 64 | 32... Qc1 | miss | good | mate_override | good | 0.0000 | 1.000 | no | g5 | Qf2 | -9.30 | -M7 |
| 185117573448 | 68 | 34... Qxc3 | miss | good | mate_override | good | 0.0000 | 1.000 | no | Qf2 | Qf2 | -8.94 | -M9 |
| 186411389477 | 79 | 40. Rf5 | excellent | good | mate_override | good | 0.0002 | 1.000 | no | Re2 | - | M9 | +13.44 |
| 186411389477 | 80 | 40... Kh4 | excellent | inaccuracy | mate_override | inaccuracy | 0.0002 | 0.000 | no | Kxg4 | - | M7 | M10 |
| 186411389477 | 101 | 51. g8=Q+ | excellent | good | mate_override | good | 0.0000 | 1.000 | no | Rg1 | - | M3 | M8 |
| 186429989523 | 81 | 41. Kh2 | mistake | inaccuracy | mate_override | inaccuracy | 0.0227 | 0.023 | no | Kg1 | - | -7.28 | -M8 |

### `book` (12)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0062 | 0.450 | no | Nf6 | - | +0.82 | +1.00 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0583 | 0.531 | no | d4 | Nxe5 | -0.62 | -0.38 |
| 185468614210 | 8 | 4... Nc6 | inaccuracy | book | book | inaccuracy | 0.0718 | 0.555 | no | Nxe4 | Nxe4 | +0.30 | +0.24 |
| 185217478440 | 6 | 3... h6 | good | book | book | good | 0.0438 | 0.492 | no | Nf6 | - | +0.74 | +0.74 |
| 185334658860 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0598 | 0.532 | no | d4 | Nxe5 | -0.62 | -0.38 |
| 185334658860 | 6 | 3... Nc6 | inaccuracy | book | book | good | 0.0384 | 0.528 | no | Nxe4 | Nxe4 | +0.28 | +0.23 |
| 185461631884 | 7 | 4. Bc4 | excellent | book | book | good | 0.0202 | 0.543 | no | Nxd4 | - | +0.31 | +0.30 |
| 186411389477 | 6 | 3... Nc6 | mistake | book | book | mistake | 0.1830 | 0.424 | no | d6 | d6 | +1.57 | +1.80 |
| 186411389477 | 7 | 4. Nxc6 | great | book | book | best | 0.0000 | 0.759 | yes | Nxc6 | - | +1.57 | +1.75 |
| 186411389477 | 8 | 4... dxc6 | best | book | book | good | 0.0240 | 0.247 | no | bxc6 | - | +1.57 | +1.76 |
| 186411389477 | 9 | 5. d3 | excellent | book | book | best | 0.0000 | 0.754 | yes | d3 | - | +1.53 | +1.78 |
| 186411389477 | 10 | 5... Bc5 | good | book | book | excellent | 0.0160 | 0.243 | no | Be6 | - | +1.84 | +2.05 |

### `blunder_softened` (8)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 41 | 21. c4 | blunder | mistake | blunder_softened | blunder | 0.2273 | 0.764 | no | Bxe6 | - | +0.61 | +0.53 |
| 185209623352 | 48 | 24... exd3 | miss | mistake | blunder_softened | blunder | 0.2802 | 0.536 | no | Bh6+ | Bh6+ | +4.08 | +4.46 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | blunder_softened | blunder | 0.2063 | 0.703 | no | Rhxe7 | Rhxe7 | -0.08 | -0.10 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2607 | 0.585 | no | Qxg3+ | Qxg3+ | +2.48 | +2.59 |
| 185438707002 | 67 | 34. Kc2 | blunder | mistake | blunder_softened | blunder | 0.4437 | 0.706 | no | Kd1 | - | -3.65 | -3.79 |
| 184784174152 | 31 | 16. Qe2 | blunder | mistake | blunder_softened | blunder | 0.4150 | 0.495 | no | Rbe1 | - | -3.61 | -3.83 |
| 185328167888 | 25 | 13. Qxh7 | miss | mistake | blunder_softened | blunder | 0.2549 | 0.730 | no | f5 | f5 | -0.06 | -0.35 |
| 186429989523 | 34 | 17... Nf8 | miss | mistake | blunder_softened | blunder | 0.3423 | 0.611 | no | c5 | c5 | +1.28 | +1.57 |

### `losing_material_hardened` (7)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | excellent | 0.0196 | 0.066 | no | Kd7 | - | -8.94 | -8.54 |
| 184678264914 | 61 | 31. Qe3 | good | mistake | losing_material_hardened | inaccuracy | 0.0521 | 0.085 | no | Qa2 | - | -8.92 | -10.85 |
| 184678264914 | 63 | 32. Rxc7 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0612 | 0.082 | no | Ra1 | Ke1 | -10.1 | -12.35 |
| 184732665836 | 62 | 31... Kc5 | excellent | mistake | losing_material_hardened | excellent | 0.0025 | 0.083 | no | Kb6 | - | +8.78 | +7.92 |
| 185617589205 | 80 | 40... Qh5 | excellent | mistake | losing_material_hardened | excellent | 0.0128 | 0.032 | no | Bg7 | - | +5.58 | +6.14 |
| 185617589205 | 108 | 54... Rxe3+ | inaccuracy | mistake | losing_material_hardened | excellent | 0.0122 | 0.014 | no | Rh7 | - | M17 | +9.76 |
| 185966191317 | 38 | 19... Ka5 | excellent | mistake | losing_material_hardened | excellent | 0.0175 | 0.035 | no | Nb4 | - | +6.44 | +6.79 |

### `great_find_event` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.502 | yes | Bxe5 | - | +0.18 | -0.08 |
| 185438707002 | 84 | 42... Nxg3 | best | great | great_find_event | best | 0.0000 | 0.893 | yes | Nxg3 | - | -7.11 | -7.07 |
| 184678264914 | 49 | 25. Bxf4 | best | great | great_find_event | best | 0.0000 | 0.242 | yes | Bxf4 | - | -3.64 | -3.86 |
| 185218140778 | 25 | 13. Kh1 | best | great | great_find_event | best | 0.0000 | 0.554 | yes | Kh1 | - | +0.51 | +0.65 |
| 185328167888 | 41 | 21. Bxf6 | best | great | great_find_event | best | 0.0000 | 0.690 | yes | Bxf6 | - | +2.79 | +2.83 |

### `brilliant_event` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759290504 | 30 | 15... Rxc3 | best | brilliant | brilliant_event | best | 0.0000 | 0.378 | yes | Rxc3 | - | +0.91 | +0.75 |

