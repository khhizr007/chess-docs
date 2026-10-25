# Calibration report: sf18-b2

- Generated: 2026-10-18T14:10:18+00:00
- Commit: `740f5a2b4756` + uncommitted backend changes (diff sha256 `78d53b3a9776`)
- Engine: Stockfish 18; depth 18, multipv 3; config override: none
- Games: 41 requested, 41 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 2842 aligned, 2833 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 66.8% (1893/2833) |
| Within one step | 89.7% (2540/2833) |
| Brilliant precision / recall | 1.00 / 0.25 |
| Great precision / recall | 0.54 / 0.09 |
| Brilliant per 100 moves (app / ours) | 0.14 / 0.04 |
| Great per 100 moves (app / ours) | 2.72 / 0.46 |
| Accuracy mean abs. difference | 3.73 (n=82, max 9.52) |
| Accuracy bias (ours - app) | +3.19 |
| Best move = app's suggestion | 79.8% (344/431 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 2 | . | . | . | 1 | . | . | . | 4 |
| **great** | . | **7** | 68 | . | 1 | 1 | . | . | . | . | 77 |
| **best** | . | 6 | **802** | 132 | 19 | 1 | 2 | 1 | . | . | 963 |
| **excellent** | . | . | 157 | **287** | 76 | 3 | 5 | 9 | . | . | 537 |
| **good** | . | . | 25 | 107 | **187** | 2 | 50 | 3 | 1 | . | 375 |
| **book** | . | . | 20 | 16 | 13 | **246** | 1 | . | . | . | 296 |
| **inaccuracy** | . | . | 7 | 18 | 60 | 4 | **158** | 21 | 7 | . | 275 |
| **mistake** | . | . | 2 | 5 | 12 | 1 | 28 | **118** | 10 | 6 | 182 |
| **miss** | . | . | . | . | 2 | . | 10 | 6 | **52** | 5 | 75 |
| **blunder** | . | . | . | . | . | . | . | 10 | 4 | **35** | 49 |
| **total** | 1 | 13 | 1083 | 565 | 370 | 258 | 255 | 168 | 74 | 46 | 2833 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 4 | 1 | 1 | 1.000 | 0.250 | 0.400 |
| great | 77 | 13 | 7 | 0.538 | 0.091 | 0.156 |
| best | 963 | 1083 | 802 | 0.741 | 0.833 | 0.784 |
| excellent | 537 | 565 | 287 | 0.508 | 0.534 | 0.521 |
| good | 375 | 370 | 187 | 0.505 | 0.499 | 0.502 |
| book | 296 | 258 | 246 | 0.953 | 0.831 | 0.888 |
| inaccuracy | 275 | 255 | 158 | 0.620 | 0.575 | 0.596 |
| mistake | 182 | 168 | 118 | 0.702 | 0.648 | 0.674 |
| miss | 75 | 74 | 52 | 0.703 | 0.693 | 0.698 |
| blunder | 49 | 46 | 35 | 0.761 | 0.714 | 0.737 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.5 | +5.8 |
| 1034847688 | black | 65.0 | 68.0 | +3.0 |
| 1041474766 | white | 98.0 | 96.9 | -1.1 |
| 1041474766 | black | 83.8 | 85.5 | +1.7 |
| 184759554082 | white | 81.2 | 85.0 | +3.8 |
| 184759554082 | black | 87.7 | 89.9 | +2.2 |
| 185209623352 | white | 72.7 | 76.7 | +4.0 |
| 185209623352 | black | 72.6 | 73.3 | +0.7 |
| 185324357184 | white | 73.0 | 76.0 | +3.0 |
| 185324357184 | black | 62.4 | 66.4 | +4.0 |
| 185436488062 | white | 98.6 | 98.1 | -0.5 |
| 185436488062 | black | 38.5 | 44.7 | +6.2 |
| 185437323918 | white | 69.5 | 73.4 | +3.9 |
| 185437323918 | black | 75.7 | 75.2 | -0.5 |
| 185438343298 | white | 46.9 | 47.1 | +0.2 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 77.6 | -0.2 |
| 185438707002 | black | 83.0 | 84.7 | +1.7 |
| 185456088510 | white | 78.4 | 84.4 | +6.0 |
| 185456088510 | black | 82.2 | 86.1 | +3.9 |
| 185468039834 | white | 80.0 | 84.1 | +4.1 |
| 185468039834 | black | 87.5 | 90.5 | +3.0 |
| 185468614210 | white | 70.8 | 76.9 | +6.1 |
| 185468614210 | black | 77.1 | 83.6 | +6.5 |
| 185475865432 | white | 78.1 | 82.9 | +4.8 |
| 185475865432 | black | 66.1 | 71.0 | +4.9 |
| 185962590893 | white | 90.8 | 93.1 | +2.3 |
| 185962590893 | black | 90.9 | 93.9 | +3.0 |
| 1011026868 | white | 78.9 | 84.1 | +5.2 |
| 1011026868 | black | 75.2 | 81.6 | +6.4 |
| 184678264914 | white | 68.3 | 69.8 | +1.5 |
| 184678264914 | black | 80.3 | 70.8 | -9.5 |
| 184732665836 | white | 67.5 | 70.9 | +3.4 |
| 184732665836 | black | 68.7 | 71.1 | +2.4 |
| 184759290504 | white | 79.4 | 81.3 | +1.9 |
| 184759290504 | black | 97.9 | 97.6 | -0.3 |
| 184773009646 | white | 85.0 | 85.4 | +0.4 |
| 184773009646 | black | 77.2 | 80.9 | +3.7 |
| 184784174152 | white | 76.0 | 78.0 | +2.0 |
| 184784174152 | black | 86.8 | 87.4 | +0.6 |
| 184794204922 | white | 77.9 | 83.0 | +5.1 |
| 184794204922 | black | 57.0 | 61.5 | +4.5 |
| 184828162542 | white | 80.5 | 83.4 | +2.9 |
| 184828162542 | black | 85.9 | 87.9 | +2.0 |
| 184829980734 | white | 81.9 | 84.3 | +2.4 |
| 184829980734 | black | 85.5 | 90.4 | +4.9 |
| 184873703892 | white | 87.4 | 90.6 | +3.2 |
| 184873703892 | black | 87.4 | 90.2 | +2.8 |
| 185110487484 | white | 88.0 | 91.6 | +3.6 |
| 185110487484 | black | 91.5 | 94.0 | +2.5 |
| 185117573448 | white | 73.0 | 79.6 | +6.6 |
| 185117573448 | black | 78.9 | 86.1 | +7.2 |
| 185173941140 | white | 50.0 | 56.6 | +6.6 |
| 185173941140 | black | 61.2 | 67.3 | +6.1 |
| 185193771738 | white | 63.3 | 68.2 | +4.9 |
| 185193771738 | black | 70.7 | 76.3 | +5.6 |
| 185217478440 | white | 80.4 | 82.9 | +2.5 |
| 185217478440 | black | 77.3 | 84.7 | +7.4 |
| 185218140778 | white | 84.3 | 86.8 | +2.5 |
| 185218140778 | black | 79.3 | 83.0 | +3.7 |
| 185277691132 | white | 80.2 | 80.0 | -0.2 |
| 185277691132 | black | 78.8 | 79.5 | +0.7 |
| 185328167888 | white | 64.1 | 70.9 | +6.8 |
| 185328167888 | black | 54.8 | 59.6 | +4.8 |
| 185330935602 | white | 77.9 | 85.4 | +7.5 |
| 185330935602 | black | 68.5 | 76.7 | +8.2 |
| 185334658860 | white | 80.5 | 86.4 | +5.9 |
| 185334658860 | black | 73.4 | 79.3 | +5.9 |
| 185363017994 | white | 64.9 | 69.6 | +4.7 |
| 185363017994 | black | 67.8 | 71.2 | +3.4 |
| 185461631884 | white | 72.5 | 82.0 | +9.5 |
| 185461631884 | black | 80.3 | 83.3 | +3.0 |
| 185617589205 | white | 81.7 | 83.5 | +1.8 |
| 185617589205 | black | 76.4 | 81.7 | +5.3 |
| 185966191317 | white | 90.5 | 87.9 | -2.6 |
| 185966191317 | black | 72.5 | 78.2 | +5.7 |
| 186222389165 | white | 87.8 | 89.2 | +1.4 |
| 186222389165 | black | 92.7 | 94.0 | +1.3 |
| 186411389477 | white | 86.9 | 79.7 | -7.2 |
| 186411389477 | black | 81.3 | 84.8 | +3.5 |
| 186429989523 | white | 78.3 | 81.4 | +3.1 |
| 186429989523 | black | 85.9 | 88.2 | +2.3 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 55.1% | 81.6% | reviewed | 35.2 |
| 1041474766 | 25 | 25 | 76.0% | 80.0% | reviewed | 16.1 |
| 184759554082 | 62 | 62 | 66.1% | 88.7% | reviewed | 49.3 |
| 185209623352 | 155 | 155 | 58.1% | 89.7% | reviewed | 74.4 |
| 185324357184 | 55 | 55 | 87.3% | 96.4% | reviewed | 58.8 |
| 185436488062 | 13 | 13 | 84.6% | 92.3% | reviewed | 43.7 |
| 185437323918 | 108 | 103 | 62.1% | 84.5% | reviewed | 63.8 |
| 185438343298 | 20 | 20 | 95.0% | 95.0% | reviewed | 16.6 |
| 185438707002 | 95 | 91 | 72.5% | 90.1% | reviewed | 64.3 |
| 185456088510 | 60 | 60 | 60.0% | 86.7% | reviewed | 63.3 |
| 185468039834 | 38 | 38 | 73.7% | 94.7% | reviewed | 71.8 |
| 185468614210 | 54 | 54 | 83.3% | 94.4% | reviewed | 55.2 |
| 185475865432 | 53 | 53 | 75.5% | 90.6% | reviewed | 54.2 |
| 185962590893 | 78 | 78 | 74.4% | 92.3% | reviewed | 61.8 |
| 1011026868 | 32 | 32 | 78.1% | 96.9% | reviewed | 54.8 |
| 184678264914 | 72 | 72 | 72.2% | 93.1% | reviewed | 69.3 |
| 184732665836 | 93 | 93 | 58.1% | 87.1% | reviewed | 88.8 |
| 184759290504 | 46 | 46 | 73.9% | 91.3% | reviewed | 59.8 |
| 184773009646 | 73 | 73 | 71.2% | 93.2% | reviewed | 71.8 |
| 184784174152 | 36 | 36 | 69.4% | 80.6% | reviewed | 66.8 |
| 184794204922 | 41 | 41 | 63.4% | 87.8% | reviewed | 42.2 |
| 184828162542 | 88 | 88 | 48.9% | 75.0% | reviewed | 78.4 |
| 184829980734 | 50 | 50 | 74.0% | 90.0% | reviewed | 52.7 |
| 184873703892 | 96 | 96 | 54.2% | 84.4% | reviewed | 92.9 |
| 185110487484 | 124 | 124 | 57.3% | 85.5% | reviewed | 119.1 |
| 185117573448 | 88 | 88 | 73.9% | 90.9% | reviewed | 76.8 |
| 185173941140 | 40 | 40 | 72.5% | 90.0% | reviewed | 76.4 |
| 185193771738 | 84 | 84 | 66.7% | 91.7% | reviewed | 72.9 |
| 185217478440 | 75 | 75 | 66.7% | 89.3% | reviewed | 49.8 |
| 185218140778 | 81 | 81 | 65.4% | 91.4% | reviewed | 88.5 |
| 185277691132 | 112 | 112 | 64.3% | 93.8% | reviewed | 113.7 |
| 185328167888 | 49 | 49 | 75.5% | 91.8% | reviewed | 79.0 |
| 185330935602 | 21 | 21 | 61.9% | 95.2% | reviewed | 101.0 |
| 185334658860 | 59 | 59 | 72.9% | 94.9% | reviewed | 71.9 |
| 185363017994 | 107 | 107 | 75.7% | 96.3% | reviewed | 112.1 |
| 185461631884 | 72 | 72 | 68.1% | 97.2% | reviewed | 77.9 |
| 185617589205 | 111 | 111 | 60.4% | 84.7% | reviewed | 135.7 |
| 185966191317 | 41 | 41 | 65.9% | 85.4% | reviewed | 104.6 |
| 186222389165 | 97 | 97 | 62.9% | 89.7% | reviewed | 119.7 |
| 186411389477 | 107 | 107 | 66.4% | 90.7% | reviewed | 94.0 |
| 186429989523 | 82 | 82 | 68.3% | 92.7% | reviewed | 84.0 |

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
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (940)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 871 | excellent -> best x157, best -> excellent x132, good -> excellent x107, excellent -> good x73, great -> best x68, inaccuracy -> good x60 |
| `miss_detector` | 19 | mistake -> miss x10, inaccuracy -> miss x5, blunder -> miss x4 |
| `mate_override` | 15 | excellent -> good x3, good -> inaccuracy x3, excellent -> inaccuracy x2, inaccuracy -> miss x2, miss -> good x2, good -> miss x1 |
| `losing_material_hardened` | 14 | excellent -> mistake x9, inaccuracy -> mistake x2, good -> mistake x2, best -> mistake x1 |
| `book` | 12 | inaccuracy -> book x4, excellent -> book x3, good -> book x2, mistake -> book x1, great -> book x1, best -> book x1 |
| `great_find_event` | 6 | best -> great x6 |
| `blunder_softened` | 3 | miss -> mistake x2, blunder -> mistake x1 |

### `precision` (871)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 5 | 3. d4 | best | excellent | precision | excellent | 0.0043 | 0.535 | no | c4 | - | +0.33 | +0.28 |
| 1034847688 | 7 | 4. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0506 | 0.537 | no | c4 | - | +0.13 | -0.13 |
| 1034847688 | 10 | 5... O-O | excellent | best | precision | best | 0.0000 | 0.558 | yes | O-O | - | -0.50 | -0.44 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0011 | 0.491 | no | Be2 | - | -0.10 | -0.15 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0398 | 0.528 | no | Bd3 | - | +0.12 | -0.11 |
| 1034847688 | 18 | 9... b5 | good | inaccuracy | precision | inaccuracy | 0.0506 | 0.512 | no | Bf5 | - | +0.38 | +0.36 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0629 | 0.580 | no | cxb5 | - | +0.24 | +0.16 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0720 | 0.621 | no | cxb5 | cxb5 | +0.44 | +0.31 |
| 1034847688 | 26 | 13... h6 | inaccuracy | excellent | precision | excellent | 0.0117 | 0.459 | no | a4 | - | +0.90 | +0.38 |
| 1034847688 | 29 | 15. Rad1 | mistake | blunder | precision | blunder | 0.2165 | 0.563 | no | h5 | h5 | -1.48 | -1.47 |
| 1034847688 | 33 | 17. cxb5 | miss | blunder | precision | blunder | 0.2232 | 0.750 | no | h5 | h5 | 0.00 | +0.00 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.500 | yes | Nxf3 | - | -0.10 | +0.00 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.562 | yes | Rh3 | - | +0.39 | +0.23 |
| 1034847688 | 42 | 21... e5 | best | excellent | precision | excellent | 0.0150 | 0.475 | no | Qd7 | - | +0.39 | +0.48 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.552 | yes | dxe6 | - | +0.30 | +0.43 |
| 1034847688 | 44 | 22... Qxg5 | excellent | best | precision | best | 0.0000 | 0.454 | yes | Qxg5 | - | +0.46 | +1.01 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.607 | yes | exf7+ | - | +0.09 | +0.66 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | mistake | precision | mistake | 0.1010 | 0.429 | no | Rxf7 | Rxf7 | +0.92 | +1.56 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M9 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0314 | 0.580 | no | d4 | - | +0.37 | +0.47 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0020 | 0.452 | no | g6 | - | +0.38 | +0.52 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.553 | yes | Bg2 | - | +0.34 | +0.46 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0071 | 0.453 | no | e5 | - | +0.59 | +0.53 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0328 | 0.554 | no | Nf3 | - | +0.17 | +0.21 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.547 | yes | O-O | - | +0.28 | +0.37 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0302 | 0.527 | no | Nf6 | - | +0.08 | -0.04 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0127 | 0.487 | no | Nf3 | - | -0.25 | -0.28 |
| 184759554082 | 15 | 8. hxg6 | good | inaccuracy | precision | inaccuracy | 0.0509 | 0.524 | no | Nc3 | - | -0.21 | -0.17 |
| 184759554082 | 17 | 9. Nf3 | good | excellent | precision | excellent | 0.0174 | 0.476 | no | Nc3 | - | -0.39 | -0.26 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0856 | 0.689 | no | d5 | d5 | -0.52 | -0.47 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.571 | yes | d5 | - | -0.52 | -0.41 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1797 | 0.435 | no | cxd5 | cxd5 | -1.98 | -1.97 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.797 | yes | Qxg5 | - | -1.98 | -1.76 |
| 184759554082 | 27 | 14. cxd5 | inaccuracy | mistake | precision | mistake | 0.1552 | 0.246 | no | Bb2 | Bb2 | -3.24 | -3.55 |
| 184759554082 | 32 | 16... b6 | best | inaccuracy | precision | inaccuracy | 0.0696 | 0.697 | no | b5 | - | -0.96 | -1.19 |
| 184759554082 | 33 | 17. Qc2 | best | excellent | precision | excellent | 0.0014 | 0.319 | no | Qc1 | - | -0.96 | -1.09 |
| 184759554082 | 36 | 18... Qf6 | best | excellent | precision | excellent | 0.0014 | 0.677 | no | Re5 | - | -1.01 | -1.17 |
| 184759554082 | 37 | 19. Kb1 | good | excellent | precision | excellent | 0.0124 | 0.322 | no | Qb2 | - | -1.19 | -1.21 |
| 184759554082 | 39 | 20. d3 | inaccuracy | good | precision | good | 0.0485 | 0.329 | no | d4 | - | -1.35 | -1.40 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.709 | yes | Re6 | - | -1.31 | -1.32 |
| 184759554082 | 44 | 22... Rd6 | excellent | good | precision | good | 0.0405 | 0.714 | no | a5 | - | -1.28 | -1.45 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.705 | yes | a5 | - | -1.16 | -1.40 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0180 | 0.291 | no | Rh1 | f3 | -1.61 | -1.60 |
| 184759554082 | 57 | 29. Ka2 | good | excellent | precision | excellent | 0.0147 | 0.266 | no | Rhe1 | - | -1.73 | -1.71 |
| 184759554082 | 58 | 29... Rc8 | inaccuracy | good | precision | good | 0.0312 | 0.748 | no | Rxh1 | Rxh1 | -1.36 | -1.46 |
| 184759554082 | 59 | 30. Rxh8 | inaccuracy | good | precision | good | 0.0487 | 0.283 | no | Rhd1 | Rhd1 | -1.74 | -1.86 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.503 | yes | Nf3 | - | -0.16 | -0.03 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.838 | yes | Nxe4 | - | +5.09 | +5.58 |
| 185209623352 | 20 | 10... dxe4 | mistake | good | precision | good | 0.0315 | 0.174 | no | Qb4 | - | +6.16 | +5.97 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0735 | 0.841 | no | Nxc6 | Nxc6 | +4.00 | +4.48 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0139 | 0.776 | no | Bxc6 | - | +4.04 | +4.26 |
| 185209623352 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0064 | 0.233 | no | Rxd4 | - | +4.04 | +4.27 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0445 | 0.767 | no | O-O-O | O-O-O | +3.00 | +3.47 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0457 | 0.275 | no | b5 | - | +4.18 | +4.34 |
| 185209623352 | 29 | 15. Nf7 | excellent | best | precision | best | 0.0000 | 0.699 | yes | Nf7 | - | +2.76 | +2.78 |
| 185209623352 | 34 | 17... Kc7 | good | excellent | precision | excellent | 0.0105 | 0.223 | no | Kb8 | - | +4.76 | +4.56 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0411 | 0.781 | no | Nd8 | Nd8 | +3.29 | +3.75 |
| 185209623352 | 40 | 20... Rd8 | inaccuracy | good | precision | good | 0.0429 | 0.291 | no | b6 | - | +3.82 | +3.96 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.715 | yes | Rc5+ | - | +3.32 | +3.33 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.604 | yes | Nxd3 | Rxd3 | -0.61 | -0.58 |
| 185209623352 | 49 | 25. Rb5+ | excellent | best | precision | best | 0.0000 | 0.766 | yes | Rb5+ | - | +3.97 | +4.20 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0005 | 0.236 | no | Ka6 | - | +3.97 | +3.87 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0020 | 0.761 | no | Rc5+ | - | +3.97 | +3.96 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.780 | yes | Kb2 | - | +4.39 | +4.55 |
| 185209623352 | 56 | 28... d2 | excellent | best | precision | best | 0.0000 | 0.219 | yes | d2 | - | +4.65 | +4.81 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0074 | 0.793 | no | Kc2 | - | +4.14 | +4.65 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0112 | 0.815 | no | Rh5 | - | +4.64 | +5.05 |
| 185209623352 | 62 | 31... Ke6 | best | excellent | precision | excellent | 0.0082 | 0.196 | no | a5 | - | +4.64 | +4.99 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0213 | 0.801 | no | Kc2 | - | +4.51 | +4.53 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.770 | yes | Kc2 | - | +4.38 | +4.23 |
| 185209623352 | 68 | 34... Rc3+ | excellent | good | precision | good | 0.0204 | 0.235 | no | Ra3 | - | +4.70 | +4.55 |
| 185209623352 | 70 | 35... Rxc4 | excellent | best | precision | best | 0.0000 | 0.228 | yes | Rxc4 | - | +4.77 | +4.53 |
| 185209623352 | 71 | 36. Rh6 | good | excellent | precision | excellent | 0.0092 | 0.780 | no | Rh5 | - | +4.11 | +4.34 |
| 185209623352 | 78 | 39... Rb2+ | good | excellent | precision | excellent | 0.0104 | 0.370 | no | Rg2 | - | +2.15 | +2.06 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.640 | yes | Kc1 | - | +2.15 | +2.06 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0774 | 0.217 | no | Kd7 | - | +6.01 | +6.52 |
| 185209623352 | 87 | 44. f5+ | excellent | best | precision | best | 0.0000 | 0.499 | yes | f5+ | - | 0.00 | +0.01 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.726 | yes | Rf1+ | - | +3.73 | +3.54 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.821 | yes | Kxb2 | - | +5.17 | +5.60 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0024 | 0.173 | no | Bxf4 | - | +5.65 | +5.70 |
| 185209623352 | 97 | 49. Kc2 | best | excellent | precision | excellent | 0.0018 | 0.844 | no | g4 | - | +5.89 | +6.13 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0132 | 0.153 | no | Be7 | - | +6.38 | +6.51 |
| 185209623352 | 102 | 51... Kg6 | excellent | best | precision | best | 0.0000 | 0.131 | yes | Kg6 | - | +6.33 | +7.03 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.872 | yes | R7xb5 | - | +6.30 | +7.27 |
| 185209623352 | 106 | 53... Kg6 | excellent | best | precision | best | 0.0000 | 0.116 | yes | Kg6 | - | +6.59 | +7.19 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0106 | 0.882 | no | Rb6 | - | +6.59 | +6.84 |
| 185209623352 | 110 | 55... Kg6 | excellent | best | precision | best | 0.0000 | 0.119 | yes | Kg6 | - | +6.54 | +7.06 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0000 | 0.878 | no | Rb6 | - | +6.54 | +7.32 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.056 | yes | Kf6 | - | +7.19 | +12.95 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | Ke7 | +10.6 | M17 |
| 185209623352 | 117 | 59. h5 | good | best | precision | best | 0.0000 | 1.000 | yes | h5 | - | +8.42 | M18 |
| 185209623352 | 118 | 59... Kf7 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | Kf6 | M10 | M12 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | M12 |
| 185209623352 | 123 | 62. Rg8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rh4 | - | M7 | M7 |
| 185209623352 | 124 | 62... Kf6 | excellent | best | precision | best | 0.0000 | 0.000 | no | Ke4 | - | M6 | M7 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qh5 | - | M3 | M7 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 133 | 67. Re8+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kc3 | - | M2 | M4 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 141 | 71. g4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Kb1 | - | +10.4 | M11 |
| 185209623352 | 142 | 71... Kb5 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Ka6 | - | M8 | M9 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M11 |
| 185209623352 | 145 | 73. g6 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rb8 | - | M5 | M6 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ka6 | - | M5 | M5 |
| 185209623352 | 153 | 77. Qc7 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qc7 | - | M3 | M3 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0054 | 0.256 | no | d4 | - | -4.03 | -3.83 |
| 185324357184 | 19 | 10. Ne2 | good | inaccuracy | precision | inaccuracy | 0.0590 | 0.461 | no | Qd4 | - | -1.32 | -1.40 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.511 | yes | Qg1 | - | +0.29 | +0.30 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0028 | 0.505 | no | Rh2 | - | +0.11 | +0.00 |
| 185324357184 | 46 | 23... b5 | excellent | best | precision | best | 0.0000 | 0.491 | yes | b5 | - | +0.26 | +0.22 |
| 185324357184 | 49 | 25. c3 | good | inaccuracy | precision | inaccuracy | 0.0531 | 0.512 | no | Rd7 | - | -0.53 | -0.58 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0231 | 0.566 | no | d4 | - | +0.65 | +0.71 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.622 | yes | Nxe5 | - | +1.74 | +1.89 |
| 185437323918 | 10 | 5... Kf8 | good | excellent | precision | excellent | 0.0111 | 0.416 | no | Ke7 | - | +1.39 | +1.25 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0216 | 0.293 | no | d4 | - | -3.51 | -3.43 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0910 | 0.269 | no | d4 | d3 | -5.55 | -5.31 |
| 185437323918 | 17 | 9. Qd3 | excellent | best | precision | best | 0.0000 | 0.175 | yes | Qd3 | - | -5.63 | -5.45 |
| 185437323918 | 18 | 9... Nxd5 | good | best | precision | best | 0.0000 | 0.828 | yes | Nxd5 | - | -5.16 | -5.43 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0253 | 0.842 | no | g4 | - | -4.94 | -5.18 |
| 185437323918 | 26 | 13... Nxg3+ | excellent | best | precision | best | 0.0000 | 0.897 | yes | Nxg3+ | - | -6.67 | -6.85 |
| 185437323918 | 32 | 16... dxc3 | excellent | best | precision | best | 0.0000 | 0.861 | yes | dxc3 | - | -5.87 | -6.26 |
| 185437323918 | 33 | 17. bxc3 | good | best | precision | best | 0.0000 | 0.142 | yes | bxc3 | - | -6.58 | -7.68 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0177 | 0.901 | no | Rxh2+ | - | -6.58 | -7.04 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.850 | no | Qe2 | - | -5.96 | -7.35 |
| 185437323918 | 42 | 21... gxf3 | brilliant | inaccuracy | precision | inaccuracy | 0.0696 | 0.794 | no | Qf4 | - | -3.59 | -4.03 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0914 | 0.239 | no | hxg3 | hxg3 | -5.85 | -6.11 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0143 | 0.815 | no | e4 | - | -4.41 | -4.83 |
| 185437323918 | 53 | 27. h3 | excellent | best | precision | best | 0.0000 | 0.199 | yes | h3 | - | -4.46 | -4.60 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.835 | yes | Be4 | - | -5.61 | -7.18 |
| 185437323918 | 59 | 30. g5+ | good | excellent | precision | excellent | 0.0064 | 0.112 | no | Rg3 | - | -6.55 | -7.02 |
| 185437323918 | 62 | 31... Bxf3+ | good | best | precision | best | 0.0000 | 0.897 | no | Rf8 | - | -6.21 | -7.22 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | best | precision | best | 0.0000 | 0.174 | yes | Kh2 | Kg2 | -6.13 | -7.08 |
| 185437323918 | 69 | 35. Rg4+ | good | excellent | precision | excellent | 0.0162 | 0.183 | no | Rxg6 | - | -5.79 | -5.59 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.156 | yes | Kf3 | - | -6.12 | -6.15 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0000 | 0.855 | no | Bb4 | - | -6.12 | -6.36 |
| 185437323918 | 77 | 39. Kxe5 | best | excellent | precision | excellent | 0.0030 | 0.119 | no | Rxf4 | - | -6.12 | -7.05 |
| 185437323918 | 80 | 40... Kxg4 | best | excellent | precision | excellent | 0.0016 | 0.877 | no | Kg5 | - | -6.12 | -7.03 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0002 | 0.934 | no | Bg3 | - | -7.28 | -9.79 |
| 185437323918 | 88 | 44... Bg3 | excellent | good | precision | good | 0.0200 | 0.951 | no | a2 | - | -8.13 | -12.49 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.040 | yes | Kc6 | Ka6 | -M17 | -M16 |
| 185437323918 | 98 | 49... Qb7+ | good | excellent | precision | excellent | 0.0053 | 0.981 | no | Qg8+ | - | -8.99 | -12.75 |
| 185437323918 | 105 | 53. Ke7 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kf8 | - | -M3 | -M12 |
| 185438707002 | 9 | 5. Bg5 | book | good | precision | good | 0.0307 | 0.516 | no | Nf3 | - | -0.01 | -0.20 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.515 | yes | h6 | - | -0.01 | -0.03 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.498 | yes | Bh4 | - | -0.01 | -0.15 |
| 185438707002 | 14 | 7... h5 | good | inaccuracy | precision | inaccuracy | 0.0513 | 0.480 | no | d6 | - | +0.95 | +0.99 |
| 185438707002 | 19 | 10. Nf3 | excellent | best | precision | best | 0.0000 | 0.485 | yes | Nf3 | - | -0.52 | -0.35 |
| 185438707002 | 23 | 12. Nxg5 | good | inaccuracy | precision | inaccuracy | 0.0545 | 0.555 | no | Na4 | - | +0.04 | +0.00 |
| 185438707002 | 28 | 14... Nd4 | inaccuracy | mistake | precision | mistake | 0.1061 | 0.541 | no | Rhg8 | Rhg8 | +0.82 | +0.90 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.626 | yes | c3 | - | +1.35 | +1.75 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0574 | 0.375 | no | Bb6 | - | +2.65 | +2.62 |
| 185438707002 | 41 | 21. O-O-O | excellent | good | precision | good | 0.0260 | 0.774 | no | Qe2 | - | +3.58 | +3.72 |
| 185438707002 | 42 | 21... Nb6 | good | excellent | precision | excellent | 0.0156 | 0.252 | no | e5 | - | +3.99 | +4.01 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.753 | no | cxd4 | - | +3.82 | +3.69 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0628 | 0.247 | no | a6 | - | +4.87 | +5.10 |
| 185438707002 | 51 | 26. Rhd1 | excellent | good | precision | good | 0.0366 | 0.769 | no | Qf6 | - | +3.49 | +3.57 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.771 | yes | Qxd8+ | - | +3.69 | +4.05 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | excellent | precision | excellent | 0.0056 | 0.307 | no | Qb3 | Qb3 | +2.60 | +3.02 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.752 | yes | Qb2+ | - | -3.65 | -3.60 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0362 | 0.708 | no | Qe2 | - | -2.36 | -2.46 |
| 185438707002 | 79 | 40. h4 | best | excellent | precision | excellent | 0.0102 | 0.328 | no | Qg7 | - | -2.36 | -2.64 |
| 185438707002 | 85 | 43. fxg3 | good | inaccuracy | precision | inaccuracy | 0.0718 | 0.105 | no | Kxg3 | - | -8.73 | -11.55 |
| 185438707002 | 86 | 43... Qf7 | best | good | precision | good | 0.0256 | 0.967 | no | e4 | - | -8.73 | -9.50 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.059 | yes | g4 | - | -8.80 | -8.47 |
| 185438707002 | 90 | 45... e3 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qf1+ | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0535 | 0.399 | no | e6 | e6 | +1.09 | +1.00 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0043 | 0.654 | no | Nf3 | - | +0.96 | +0.97 |
| 185456088510 | 9 | 5. Nc3 | excellent | good | precision | good | 0.0230 | 0.667 | no | c4 | - | +0.95 | +0.93 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0259 | 0.359 | no | Ne7 | Bg7 | +1.25 | +1.09 |
| 185456088510 | 13 | 7. a4 | inaccuracy | good | precision | good | 0.0363 | 0.667 | no | Bf4 | Qe2 | +0.87 | +0.84 |
| 185456088510 | 14 | 7... Bb7 | good | excellent | precision | excellent | 0.0147 | 0.369 | no | Bg7 | - | +1.00 | +0.83 |
| 185456088510 | 15 | 8. Be3 | good | best | precision | best | 0.0000 | 0.629 | yes | Be3 | - | +0.81 | +0.76 |
| 185456088510 | 16 | 8... Nd7 | best | good | precision | good | 0.0208 | 0.381 | no | Bg7 | - | +0.81 | +0.96 |
| 185456088510 | 17 | 9. Ne2 | good | inaccuracy | precision | inaccuracy | 0.0554 | 0.648 | no | Qe2 | - | +0.65 | +0.59 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.607 | yes | Ng3 | - | +0.65 | +0.59 |
| 185456088510 | 20 | 10... Ng4 | excellent | good | precision | good | 0.0318 | 0.407 | no | h5 | - | +0.74 | +0.80 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.678 | yes | h5 | - | +1.12 | +1.16 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.743 | yes | exd6 | - | +1.55 | +1.12 |
| 185456088510 | 34 | 17... Qe7 | miss | blunder | precision | blunder | 0.2235 | 0.427 | no | Bxe4 | Bxe4 | +1.83 | +2.14 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0282 | 0.807 | no | Nh4 | - | +1.72 | +2.01 |
| 185456088510 | 40 | 20... Qxc5 | inaccuracy | good | precision | good | 0.0481 | 0.221 | no | bxc5 | bxc5 | +2.36 | +2.32 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0560 | 0.170 | no | Rd6 | - | +2.89 | +3.22 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0164 | 0.886 | no | a5 | - | +2.89 | +3.36 |
| 185456088510 | 48 | 24... Qc7 | excellent | best | precision | best | 0.0000 | 0.105 | yes | Qc7 | - | +3.01 | +3.04 |
| 185456088510 | 52 | 26... Rxd1+ | good | excellent | precision | excellent | 0.0193 | 0.197 | no | Nxe3 | - | +2.14 | +2.20 |
| 185456088510 | 54 | 27... e4 | inaccuracy | mistake | precision | mistake | 0.1017 | 0.202 | no | Rc6 | - | +2.96 | +3.45 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.921 | yes | Nxe3 | - | -4.25 | -5.03 |
| 185456088510 | 57 | 29. Nd4 | mistake | excellent | precision | excellent | 0.0103 | 0.039 | no | Qe2 | - | -4.77 | -5.53 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0092 | 0.440 | no | Na4 | - | -0.94 | -1.00 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0122 | 0.486 | no | Ne5 | - | +0.60 | +0.52 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0362 | 0.463 | no | Kf8 | - | +0.61 | +1.02 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0492 | 0.429 | no | dxe5 | dxe5 | +1.53 | +1.68 |
| 185468039834 | 23 | 12. Qf3 | miss | blunder | precision | blunder | 0.2309 | 0.641 | no | Nxc7+ | Nxc7+ | -0.91 | -1.26 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.590 | yes | c6 | - | -0.83 | -1.20 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0104 | 0.415 | no | b4 | - | -1.28 | -1.32 |
| 185468039834 | 27 | 14. Bxe6 | best | excellent | precision | excellent | 0.0069 | 0.395 | no | Bb3 | - | -1.28 | -1.64 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.728 | yes | Rf8 | - | -3.36 | -3.34 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0011 | 0.269 | no | Qg3 | - | -3.39 | -3.44 |
| 185468614210 | 18 | 9... Ne7 | excellent | good | precision | good | 0.0200 | 0.410 | no | Na5 | - | +1.36 | +1.63 |
| 185468614210 | 26 | 13... Re8 | good | inaccuracy | precision | inaccuracy | 0.0547 | 0.541 | no | Nxd5 | - | +0.15 | +0.19 |
| 185468614210 | 28 | 14... Nxd5 | excellent | best | precision | best | 0.0000 | 0.487 | yes | Nxd5 | - | +0.25 | +0.18 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0416 | 0.487 | no | Kg8 | Kg8 | +1.21 | +0.76 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0430 | 0.555 | no | Qh5+ | Qh5+ | +0.18 | +0.14 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.490 | yes | Kg8 | - | +0.18 | +0.20 |
| 185468614210 | 48 | 24... Rxc3 | best | excellent | precision | excellent | 0.0007 | 0.491 | no | Rd2 | - | +0.14 | +0.03 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0128 | 0.565 | no | d4 | - | +0.74 | +0.68 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.451 | yes | Bb7 | - | +0.74 | +0.68 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.549 | yes | Nc3 | - | +0.74 | +0.73 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.448 | yes | e6 | - | +0.74 | +0.66 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0093 | 0.460 | no | Bb4 | - | +0.55 | +0.65 |
| 185475865432 | 16 | 8... a5 | inaccuracy | mistake | precision | mistake | 0.1025 | 0.555 | no | Bxe4 | Bxe4 | +0.75 | +0.61 |
| 185475865432 | 23 | 12. Bf4 | inaccuracy | good | precision | good | 0.0463 | 0.446 | no | e5 | - | -1.49 | -1.42 |
| 185475865432 | 25 | 13. Ne5 | best | good | precision | good | 0.0241 | 0.410 | no | Ned4 | - | -1.49 | -1.62 |
| 185475865432 | 37 | 19. Rad1 | excellent | best | precision | best | 0.0000 | 0.606 | yes | Rad1 | - | +1.50 | +1.56 |
| 185475865432 | 42 | 21... Bxb2 | best | excellent | precision | excellent | 0.0076 | 0.402 | no | Rc8 | - | +1.50 | +1.55 |
| 185475865432 | 44 | 22... Rc8 | excellent | best | precision | best | 0.0000 | 0.399 | yes | Rc8 | - | +1.57 | +1.45 |
| 185475865432 | 48 | 24... Be2 | inaccuracy | mistake | precision | mistake | 0.1214 | 0.383 | no | Rb8 | Rb8 | +3.18 | +3.61 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0802 | 0.739 | no | Rxe6 | Rxe6 | +1.47 | +2.28 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.409 | yes | e5 | - | +0.67 | +0.62 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.426 | yes | Be7 | - | +0.55 | +0.52 |
| 185962590893 | 24 | 12... O-O | best | excellent | precision | excellent | 0.0031 | 0.409 | no | g6 | - | +0.66 | +0.62 |
| 185962590893 | 27 | 14. Nxe7+ | miss | inaccuracy | precision | inaccuracy | 0.0681 | 0.734 | no | Bh6 | Bh6 | +1.01 | +1.19 |
| 185962590893 | 30 | 15... Rd8 | inaccuracy | good | precision | good | 0.0496 | 0.381 | no | Nf8 | Nf8 | +1.12 | +1.26 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0826 | 0.741 | no | Rxd8+ | Rxd8+ | +0.96 | +1.03 |
| 185962590893 | 34 | 17... Red7 | best | excellent | precision | excellent | 0.0029 | 0.342 | no | Rxd1+ | - | +0.96 | +1.04 |
| 185962590893 | 42 | 21... Nf8 | best | good | precision | good | 0.0337 | 0.375 | no | c5 | - | +0.96 | +1.03 |
| 185962590893 | 44 | 22... Ne6 | excellent | best | precision | best | 0.0000 | 0.377 | yes | Ne6 | - | +0.92 | +0.87 |
| 185962590893 | 45 | 23. Qd3 | good | excellent | precision | excellent | 0.0044 | 0.635 | no | Qc3 | - | +0.71 | +0.73 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0090 | 0.386 | no | Nf4 | - | +0.86 | +0.79 |
| 185962590893 | 49 | 25. Bg4 | excellent | good | precision | good | 0.0225 | 0.632 | no | Qc3 | - | +0.82 | +0.70 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.610 | yes | Qe3 | Qf3 | +0.47 | +0.76 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0566 | 0.381 | no | Nf4 | Nf4 | +1.15 | +1.18 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2429 | 0.680 | no | f4 | - | -0.39 | -0.40 |
| 185962590893 | 59 | 30. Bxe6 | great | best | precision | best | 0.0000 | 0.460 | yes | Bxe6 | - | -0.23 | -0.14 |
| 185962590893 | 61 | 31. f4 | best | excellent | precision | excellent | 0.0064 | 0.476 | no | h5 | - | -0.23 | -0.20 |
| 185962590893 | 62 | 31... exf4 | good | excellent | precision | excellent | 0.0111 | 0.532 | no | Kf7 | - | -0.08 | -0.13 |
| 185962590893 | 64 | 32... e5 | excellent | good | precision | good | 0.0334 | 0.533 | no | b4 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |
| 1011026868 | 6 | 3... d6 | book | good | precision | good | 0.0209 | 0.474 | no | g6 | - | +0.45 | +0.43 |
| 1011026868 | 11 | 6. d3 | good | excellent | precision | excellent | 0.0110 | 0.501 | no | O-O | - | -0.10 | -0.15 |
| 1011026868 | 13 | 7. Be3 | excellent | good | precision | good | 0.0242 | 0.482 | no | O-O | - | -0.28 | -0.38 |
| 1011026868 | 22 | 11... O-O | good | excellent | precision | excellent | 0.0066 | 0.506 | no | Qc7 | - | +0.19 | +0.25 |
| 1011026868 | 23 | 12. O-O | good | excellent | precision | excellent | 0.0154 | 0.528 | no | h4 | - | -0.02 | -0.02 |
| 1011026868 | 27 | 14. Bh6 | excellent | good | precision | good | 0.0208 | 0.552 | no | c3 | - | +0.30 | +0.28 |
| 1011026868 | 28 | 14... e5 | good | inaccuracy | precision | inaccuracy | 0.0534 | 0.469 | no | Ne5 | - | +0.76 | +0.77 |
| 184678264914 | 10 | 5... a6 | inaccuracy | good | precision | good | 0.0376 | 0.402 | no | Bb6 | Bb6 | +1.79 | +1.78 |
| 184678264914 | 13 | 7. b4 | inaccuracy | good | precision | good | 0.0432 | 0.576 | no | d4 | d4 | +0.39 | +0.42 |
| 184678264914 | 19 | 10. b5 | good | inaccuracy | precision | inaccuracy | 0.0507 | 0.535 | no | h3 | - | -0.18 | -0.20 |
| 184678264914 | 24 | 12... O-O | excellent | best | precision | best | 0.0000 | 0.529 | yes | O-O | - | -0.17 | -0.26 |
| 184678264914 | 25 | 13. Bxc6 | excellent | best | precision | best | 0.0000 | 0.480 | yes | Bxc6 | - | -0.19 | -0.26 |
| 184678264914 | 27 | 14. a6 | good | inaccuracy | precision | inaccuracy | 0.0511 | 0.482 | no | Nbd2 | - | -0.87 | -0.89 |
| 184678264914 | 28 | 14... Bb6 | excellent | best | precision | best | 0.0000 | 0.569 | yes | Bb6 | - | -0.76 | -0.82 |
| 184678264914 | 36 | 18... Rxa6 | excellent | best | precision | best | 0.0000 | 0.534 | no | h6 | - | -0.48 | -0.43 |
| 184678264914 | 40 | 20... Rxb1 | great | best | precision | best | 0.0000 | 0.754 | yes | Rxb1 | - | -3.34 | -3.46 |
| 184678264914 | 48 | 24... Nf4 | good | inaccuracy | precision | inaccuracy | 0.0654 | 0.820 | no | h6 | - | -3.64 | -3.60 |
| 184678264914 | 52 | 26... Re8 | excellent | good | precision | good | 0.0201 | 0.827 | no | h6 | - | -4.69 | -4.79 |
| 184678264914 | 53 | 27. Qd2 | inaccuracy | mistake | precision | mistake | 0.1830 | 0.183 | no | Qa4 | Qa4 | -6.40 | -M4 |
| 184678264914 | 60 | 30... f3 | excellent | best | precision | best | 0.0000 | 0.941 | yes | f3 | - | -7.13 | -8.44 |
| 184678264914 | 68 | 34... cxd4 | excellent | best | precision | best | 0.0000 | 0.865 | yes | cxd4 | - | -4.05 | -5.15 |
| 184678264914 | 69 | 35. Qc1 | blunder | mistake | precision | mistake | 0.1668 | 0.167 | no | Qxd4 | - | -M3 | -M3 |
| 184678264914 | 70 | 35... Qg1+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qg1+ | - | -M2 | -M2 |
| 184732665836 | 8 | 4... c4 | inaccuracy | good | precision | good | 0.0487 | 0.477 | no | Bd7 | Nc6 | +0.99 | +0.96 |
| 184732665836 | 9 | 5. Nf3 | good | excellent | precision | excellent | 0.0126 | 0.572 | no | b3 | - | +0.79 | +0.70 |
| 184732665836 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0015 | 0.447 | no | Nc6 | - | +0.79 | +0.80 |
| 184732665836 | 15 | 8. Nxc3 | inaccuracy | good | precision | good | 0.0313 | 0.637 | no | bxc4 | bxc4 | +1.37 | +1.30 |
| 184732665836 | 18 | 9... Qd8 | good | inaccuracy | precision | inaccuracy | 0.0632 | 0.336 | no | cxb3 | - | +3.07 | +3.24 |
| 184732665836 | 20 | 10... dxc4 | good | excellent | precision | excellent | 0.0198 | 0.270 | no | Ne7 | - | +3.53 | +3.63 |
| 184732665836 | 23 | 12. O-O | excellent | best | precision | best | 0.0000 | 0.833 | yes | O-O | - | +5.08 | +5.27 |
| 184732665836 | 24 | 12... fxe5 | good | excellent | precision | excellent | 0.0124 | 0.169 | no | Be7 | - | +5.78 | +6.17 |
| 184732665836 | 26 | 13... Nf6 | mistake | excellent | precision | excellent | 0.0164 | 0.156 | no | Qxd4 | - | +5.51 | +5.72 |
| 184732665836 | 27 | 14. Bg5 | good | excellent | precision | excellent | 0.0153 | 0.849 | no | Qa4+ | - | +5.17 | +5.34 |
| 184732665836 | 31 | 16. Qh5+ | best | excellent | precision | excellent | 0.0170 | 0.815 | no | Bb5+ | - | +4.65 | +4.74 |
| 184732665836 | 33 | 17. Nxg6 | mistake | inaccuracy | precision | inaccuracy | 0.0871 | 0.811 | no | Qf3 | - | +2.71 | +3.19 |
| 184732665836 | 34 | 17... Rg8 | blunder | mistake | precision | mistake | 0.1739 | 0.276 | no | hxg6 | hxg6 | +6.81 | +7.29 |
| 184732665836 | 35 | 18. Ne5+ | best | excellent | precision | excellent | 0.0014 | 0.901 | no | Nh8+ | - | +6.81 | +7.33 |
| 184732665836 | 40 | 20... Bxe5 | best | excellent | precision | excellent | 0.0030 | 0.213 | no | Qxd4+ | - | +3.98 | +4.49 |
| 184732665836 | 42 | 21... Nc6 | mistake | good | precision | good | 0.0360 | 0.182 | no | Qxd4+ | - | +6.33 | +6.52 |
| 184732665836 | 43 | 22. Qh4+ | inaccuracy | excellent | precision | excellent | 0.0049 | 0.878 | no | d5 | d5 | +5.32 | +6.37 |
| 184732665836 | 46 | 23... Kd7 | mistake | good | precision | good | 0.0493 | 0.109 | no | Ke7 | - | +7.09 | +8.63 |
| 184732665836 | 53 | 27. Qxf7+ | best | excellent | precision | excellent | 0.0030 | 0.832 | no | Bxe6+ | - | +4.77 | +5.84 |
| 184732665836 | 55 | 28. Qh5 | good | inaccuracy | precision | inaccuracy | 0.0695 | 0.860 | no | Qf2 | - | +4.07 | +4.39 |
| 184732665836 | 58 | 29... Kc6 | excellent | good | precision | good | 0.0324 | 0.109 | no | Kd8 | - | +6.93 | +8.21 |
| 184732665836 | 59 | 30. Rf7 | best | good | precision | good | 0.0295 | 0.923 | no | Qf3+ | - | +6.93 | +7.25 |
| 184732665836 | 60 | 30... Qd8 | mistake | good | precision | good | 0.0444 | 0.100 | no | Qxf7 | - | +7.94 | +9.34 |
| 184732665836 | 62 | 31... Kc5 | excellent | best | precision | best | 0.0000 | 0.076 | yes | Kc5 | - | +8.78 | +10.01 |
| 184732665836 | 66 | 33... Kb4 | inaccuracy | good | precision | good | 0.0412 | 0.071 | no | Nb5 | Qh4 | M9 | +11.47 |
| 184732665836 | 67 | 34. Qe4+ | excellent | best | precision | best | 0.0000 | 0.970 | yes | Qe4+ | - | M15 | M9 |
| 184732665836 | 68 | 34... Ka5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Ka5 | - | M9 | +15.22 |
| 184732665836 | 69 | 35. Ra7 | miss | mistake | precision | mistake | 0.1821 | 0.990 | no | Qe1+ | Qe1+ | +4.45 | +4.75 |
| 184732665836 | 75 | 38. Nd6 | excellent | good | precision | good | 0.0218 | 0.816 | no | Qe1+ | - | +4.45 | +4.46 |
| 184732665836 | 76 | 38... Qc1+ | excellent | best | precision | best | 0.0000 | 0.206 | yes | Qc1+ | - | +4.61 | +4.88 |
| 184732665836 | 79 | 40. Qe2 | great | best | precision | best | 0.0000 | 0.766 | yes | Qe2 | - | +3.80 | +4.00 |
| 184732665836 | 81 | 41. Qe3 | good | excellent | precision | excellent | 0.0125 | 0.807 | no | Kg3 | - | +4.02 | +4.78 |
| 184732665836 | 82 | 41... Qh4+ | inaccuracy | mistake | precision | mistake | 0.1085 | 0.191 | no | Qb2+ | Nc2 | +5.87 | +7.98 |
| 184732665836 | 86 | 43... Qb2+ | excellent | best | precision | best | 0.0000 | 0.189 | yes | Qb2+ | - | +4.43 | +4.60 |
| 184732665836 | 87 | 44. Qe2 | great | best | precision | best | 0.0000 | 0.801 | yes | Qe2 | - | +4.43 | +4.77 |
| 184732665836 | 91 | 46. Qe2 | great | best | precision | best | 0.0000 | 0.804 | yes | Qe2 | - | +4.48 | +4.70 |
| 184732665836 | 92 | 46... Qd4+ | excellent | best | precision | best | 0.0000 | 0.194 | yes | Qd4+ | - | +4.61 | +4.99 |
| 184759290504 | 12 | 6... a6 | book | good | precision | good | 0.0211 | 0.396 | no | Nc6 | - | +0.80 | +0.80 |
| 184759290504 | 13 | 7. f3 | book | excellent | precision | excellent | 0.0105 | 0.625 | no | Qd2 | - | +0.64 | +0.64 |
| 184759290504 | 14 | 7... h5 | best | excellent | precision | excellent | 0.0167 | 0.399 | no | b5 | - | +0.64 | +0.79 |
| 184759290504 | 15 | 8. Qd2 | excellent | best | precision | best | 0.0000 | 0.623 | yes | Qd2 | - | +0.56 | +0.80 |
| 184759290504 | 16 | 8... Bg7 | good | excellent | precision | excellent | 0.0045 | 0.375 | no | e5 | - | +0.79 | +0.77 |
| 184759290504 | 17 | 9. Bc4 | good | excellent | precision | excellent | 0.0000 | 0.620 | no | Be2 | - | +0.64 | +0.80 |
| 184759290504 | 19 | 10. Bb3 | best | excellent | precision | excellent | 0.0091 | 0.616 | no | Be2 | - | +0.64 | +0.64 |
| 184759290504 | 20 | 10... Bb7 | excellent | best | precision | best | 0.0000 | 0.399 | yes | Bb7 | - | +0.72 | +0.77 |
| 184759290504 | 23 | 12. h3 | best | good | precision | good | 0.0349 | 0.625 | no | Rhe1 | - | +0.72 | +0.57 |
| 184759290504 | 25 | 13. Rhe1 | good | excellent | precision | excellent | 0.0075 | 0.628 | no | Kb1 | - | +0.81 | +0.72 |
| 184759290504 | 26 | 13... Rc8 | best | good | precision | good | 0.0209 | 0.387 | no | Nc5 | - | +0.81 | +0.86 |
| 184759290504 | 30 | 15... Rxc3 | best | excellent | precision | excellent | 0.0059 | 0.372 | no | Qc7 | - | +0.91 | +0.88 |
| 184773009646 | 13 | 7. Nc3 | miss | inaccuracy | precision | inaccuracy | 0.0780 | 0.613 | no | d5 | e5 | +0.52 | +0.52 |
| 184773009646 | 14 | 7... O-O | inaccuracy | good | precision | good | 0.0431 | 0.465 | no | d6 | - | +1.27 | +1.16 |
| 184773009646 | 16 | 8... Re8 | mistake | inaccuracy | precision | inaccuracy | 0.0827 | 0.414 | no | d5 | - | +3.29 | +2.91 |
| 184773009646 | 17 | 9. O-O | great | best | precision | best | 0.0000 | 0.686 | yes | O-O | - | +3.29 | +2.88 |
| 184773009646 | 25 | 13. Bxe6 | best | good | precision | good | 0.0383 | 0.778 | no | d5 | - | +3.85 | +4.06 |
| 184773009646 | 29 | 15. Bg5 | inaccuracy | good | precision | good | 0.0440 | 0.751 | no | Be3 | - | +2.86 | +3.27 |
| 184773009646 | 30 | 15... Nxd4 | good | excellent | precision | excellent | 0.0099 | 0.293 | no | Bxd4 | - | +3.26 | +3.23 |
| 184773009646 | 33 | 17. Re1 | good | inaccuracy | precision | inaccuracy | 0.0534 | 0.710 | no | Nb5 | - | +2.39 | +2.41 |
| 184773009646 | 38 | 19... c5 | excellent | good | precision | good | 0.0279 | 0.267 | no | Rc8 | - | +4.03 | +4.31 |
| 184773009646 | 40 | 20... b6 | good | excellent | precision | excellent | 0.0150 | 0.242 | no | Bxb2 | - | +4.48 | +4.51 |
| 184773009646 | 42 | 21... a6 | good | inaccuracy | precision | inaccuracy | 0.0589 | 0.297 | no | Bxb2 | - | +4.23 | +4.32 |
| 184773009646 | 44 | 22... Ra7 | good | excellent | precision | excellent | 0.0118 | 0.264 | no | Rc8 | - | +4.03 | +4.10 |
| 184773009646 | 46 | 23... a5 | excellent | best | precision | best | 0.0000 | 0.248 | yes | a5 | - | +4.16 | +4.17 |
| 184773009646 | 53 | 27. Nb5 | excellent | good | precision | good | 0.0347 | 0.737 | no | Kf1 | - | +3.23 | +3.19 |
| 184773009646 | 55 | 28. Be5 | excellent | good | precision | good | 0.0383 | 0.747 | no | Re2 | - | +3.54 | +3.47 |
| 184773009646 | 57 | 29. Nxa3 | great | best | precision | best | 0.0000 | 0.838 | yes | Nxa3 | - | +6.25 | +6.16 |
| 184773009646 | 59 | 30. Nxc4 | best | excellent | precision | excellent | 0.0024 | 0.848 | no | Nb5 | - | +6.25 | +6.57 |
| 184773009646 | 60 | 30... b5 | excellent | best | precision | best | 0.0000 | 0.146 | yes | b5 | - | +6.39 | +6.76 |
| 184773009646 | 67 | 34. g3 | best | excellent | precision | excellent | 0.0055 | 0.851 | no | Kf1 | - | +6.17 | +6.32 |
| 184773009646 | 72 | 36... Kf7 | excellent | best | precision | best | 0.0000 | 0.150 | yes | Kf7 | - | +6.26 | +6.54 |
| 184784174152 | 8 | 4... c6 | book | inaccuracy | precision | inaccuracy | 0.0652 | 0.541 | no | h6 | - | +0.07 | +0.15 |
| 184784174152 | 9 | 5. e3 | book | best | precision | best | 0.0000 | 0.524 | yes | e3 | - | +0.07 | +0.12 |
| 184784174152 | 10 | 5... h6 | best | excellent | precision | excellent | 0.0016 | 0.481 | no | e6 | - | +0.07 | +0.14 |
| 184784174152 | 12 | 6... Qb6 | good | excellent | precision | excellent | 0.0095 | 0.478 | no | e6 | - | +0.18 | +0.19 |
| 184784174152 | 13 | 7. Rb1 | good | best | precision | best | 0.0000 | 0.530 | yes | Rb1 | - | -0.02 | +0.01 |
| 184784174152 | 14 | 7... e6 | inaccuracy | good | precision | good | 0.0366 | 0.498 | no | g5 | g5 | +0.30 | +0.31 |
| 184784174152 | 16 | 8... Bd6 | good | inaccuracy | precision | inaccuracy | 0.0626 | 0.468 | no | c5 | - | +0.54 | +0.60 |
| 184784174152 | 19 | 10. e4 | excellent | inaccuracy | precision | inaccuracy | 0.0560 | 0.604 | no | Re1 | - | +0.47 | +0.30 |
| 184784174152 | 25 | 13. dxe5 | great | best | precision | best | 0.0000 | 0.740 | yes | dxe5 | - | +1.55 | +1.66 |
| 184784174152 | 32 | 16... f5 | great | best | precision | best | 0.0000 | 0.907 | yes | f5 | - | -3.61 | -3.76 |
| 184784174152 | 33 | 17. Bf3 | mistake | good | precision | good | 0.0277 | 0.084 | no | Rfe1 | - | -4.19 | -4.44 |
| 184794204922 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.487 | yes | Nf6 | - | +0.20 | +0.17 |
| 184794204922 | 7 | 4. Nc3 | book | best | precision | best | 0.0000 | 0.511 | yes | Nc3 | - | +0.20 | +0.16 |
| 184794204922 | 14 | 7... e6 | inaccuracy | good | precision | good | 0.0487 | 0.467 | no | Nxd5 | Nxd5 | +1.42 | +1.23 |
| 184794204922 | 17 | 9. O-O | inaccuracy | good | precision | good | 0.0347 | 0.583 | no | Bb5+ | Bb5+ | +0.80 | +0.68 |
| 184794204922 | 20 | 10... Kd8 | best | excellent | precision | excellent | 0.0030 | 0.352 | no | Ke7 | - | +2.23 | +2.37 |
| 184794204922 | 21 | 11. f4 | best | excellent | precision | excellent | 0.0097 | 0.653 | no | c3 | - | +2.23 | +2.15 |
| 184794204922 | 23 | 12. Qxg4 | great | best | precision | best | 0.0000 | 0.821 | yes | Qxg4 | - | +5.65 | +5.33 |
| 184794204922 | 26 | 13... b5 | good | excellent | precision | excellent | 0.0103 | 0.187 | no | Qe7 | - | +6.18 | +5.76 |
| 184794204922 | 28 | 14... a5 | excellent | good | precision | good | 0.0305 | 0.186 | no | h5 | - | +6.22 | +6.34 |
| 184794204922 | 30 | 15... b4 | mistake | good | precision | good | 0.0239 | 0.184 | no | h5 | - | +6.63 | +6.21 |
| 184794204922 | 31 | 16. Bd2 | inaccuracy | good | precision | good | 0.0219 | 0.840 | no | fxe5 | fxe5 | +5.52 | +5.63 |
| 184794204922 | 32 | 16... g6 | mistake | good | precision | good | 0.0413 | 0.182 | no | Qg6 | - | +7.41 | +6.78 |
| 184794204922 | 36 | 18... h5 | best | excellent | precision | excellent | 0.0107 | 0.046 | no | Ra7 | - | +9.48 | +12.44 |
| 184794204922 | 39 | 20. Rxf7 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Bg5 | - | +10.5 | +12.38 |
| 184828162542 | 5 | 3. Nd2 | book | excellent | precision | excellent | 0.0016 | 0.530 | no | e4 | - | +0.16 | +0.18 |
| 184828162542 | 6 | 3... d5 | book | good | precision | good | 0.0222 | 0.471 | no | h6 | - | +0.42 | +0.30 |
| 184828162542 | 7 | 4. e3 | book | excellent | precision | excellent | 0.0127 | 0.548 | no | e4 | - | +0.14 | +0.15 |
| 184828162542 | 8 | 4... h6 | excellent | best | precision | best | 0.0000 | 0.476 | no | c5 | - | +0.16 | +0.19 |
| 184828162542 | 10 | 5... c5 | book | excellent | precision | excellent | 0.0095 | 0.468 | no | Nbd7 | - | +0.16 | +0.24 |
| 184828162542 | 11 | 6. c3 | book | best | precision | best | 0.0000 | 0.538 | yes | c3 | - | +0.16 | +0.25 |
| 184828162542 | 12 | 6... Nc6 | book | excellent | precision | excellent | 0.0047 | 0.460 | no | Bd7 | - | +0.16 | +0.28 |
| 184828162542 | 17 | 9. f4 | good | best | precision | best | 0.0000 | 0.467 | yes | f4 | - | -0.32 | -0.47 |
| 184828162542 | 19 | 10. Ngf3 | excellent | good | precision | good | 0.0318 | 0.492 | no | Ndf3 | - | -0.10 | -0.25 |
| 184828162542 | 20 | 10... cxd4 | inaccuracy | good | precision | good | 0.0429 | 0.540 | no | g5 | g5 | +0.22 | +0.16 |
| 184828162542 | 22 | 11... Bd7 | excellent | best | precision | best | 0.0000 | 0.470 | yes | Bd7 | - | +0.30 | +0.24 |
| 184828162542 | 25 | 13. O-O | good | best | precision | best | 0.0000 | 0.562 | yes | O-O | - | +0.33 | +0.34 |
| 184828162542 | 27 | 14. Ne5 | excellent | good | precision | good | 0.0474 | 0.565 | no | Kh1 | - | +0.24 | +0.11 |
| 184828162542 | 30 | 15... Kh8 | best | inaccuracy | precision | inaccuracy | 0.0571 | 0.443 | no | Qb6 | - | +0.70 | +0.72 |
| 184828162542 | 31 | 16. Nxf6 | best | excellent | precision | excellent | 0.0168 | 0.613 | no | Rf2 | - | +0.70 | +0.62 |
| 184828162542 | 35 | 18. Rf3 | inaccuracy | mistake | precision | mistake | 0.1157 | 0.616 | no | Nb3 | - | +0.11 | +0.00 |
| 184828162542 | 37 | 19. Rg3 | good | inaccuracy | precision | inaccuracy | 0.0508 | 0.551 | no | Rf2 | - | +0.09 | +0.00 |
| 184828162542 | 39 | 20. Rf1 | best | good | precision | good | 0.0281 | 0.582 | no | Nb3 | - | +0.48 | +0.28 |
| 184828162542 | 40 | 20... Qe7 | best | good | precision | good | 0.0391 | 0.456 | no | Be8 | - | +0.48 | +0.47 |
| 184828162542 | 41 | 21. Nf3 | inaccuracy | good | precision | good | 0.0361 | 0.574 | no | Nb3 | - | +0.13 | +0.24 |
| 184828162542 | 43 | 22. Qh3 | best | excellent | precision | excellent | 0.0048 | 0.530 | no | Qh4 | - | +0.13 | +0.00 |
| 184828162542 | 45 | 23. Nh4 | inaccuracy | excellent | precision | excellent | 0.0191 | 0.537 | no | Nd2 | Qh4 | 0.00 | +0.11 |
| 184828162542 | 46 | 23... Ne7 | best | excellent | precision | excellent | 0.0016 | 0.482 | no | Rc7 | - | 0.00 | +0.08 |
| 184828162542 | 48 | 24... a6 | inaccuracy | excellent | precision | excellent | 0.0080 | 0.500 | no | Rc7 | h5 | +0.17 | +0.05 |
| 184828162542 | 49 | 25. Qh4 | inaccuracy | excellent | precision | excellent | 0.0080 | 0.508 | no | Nd2 | - | -0.26 | +0.00 |
| 184828162542 | 50 | 25... Rc7 | mistake | good | precision | good | 0.0397 | 0.500 | no | Ng6 | Ng6 | +0.45 | +0.52 |
| 184828162542 | 53 | 27. Qh3 | great | best | precision | best | 0.0000 | 0.510 | yes | Qh3 | - | +0.06 | +0.00 |
| 184828162542 | 55 | 28. Nb3 | good | excellent | precision | excellent | 0.0173 | 0.565 | no | Qh5 | - | +0.11 | +0.39 |
| 184828162542 | 56 | 28... b6 | mistake | good | precision | good | 0.0433 | 0.438 | no | h5 | - | +0.85 | +0.66 |
| 184828162542 | 57 | 29. Rgf3 | miss | inaccuracy | precision | inaccuracy | 0.0877 | 0.604 | no | Bxa6 | Bxa6 | +0.24 | +0.10 |
| 184828162542 | 58 | 29... a5 | good | inaccuracy | precision | inaccuracy | 0.0630 | 0.484 | no | Bb5 | - | +0.45 | +0.37 |
| 184828162542 | 59 | 30. R3f2 | inaccuracy | good | precision | good | 0.0396 | 0.559 | no | Rc1 | Rc1 | +0.12 | +0.05 |
| 184828162542 | 60 | 30... h5 | inaccuracy | good | precision | good | 0.0460 | 0.492 | no | Ba4 | Ba4 | +0.51 | +0.34 |
| 184828162542 | 61 | 31. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0571 | 0.554 | no | Rc1 | Rc1 | -0.17 | -0.02 |
| 184828162542 | 62 | 31... Rcg7 | good | excellent | precision | excellent | 0.0191 | 0.503 | no | Ba4 | - | +0.01 | -0.01 |
| 184828162542 | 63 | 32. Kh1 | blunder | mistake | precision | mistake | 0.1984 | 0.498 | no | Qh3 | - | -1.44 | -1.33 |
| 184828162542 | 64 | 32... Nh4 | great | best | precision | best | 0.0000 | 0.700 | yes | Nh4 | - | -1.44 | -1.26 |
| 184828162542 | 71 | 36. Rc1 | mistake | inaccuracy | precision | inaccuracy | 0.0919 | 0.245 | no | Rf3 | Nb1 | -2.63 | -2.69 |
| 184828162542 | 72 | 36... h4 | miss | mistake | precision | mistake | 0.1302 | 0.847 | no | Qg6 | Qg6 | -1.07 | -1.58 |
| 184828162542 | 73 | 37. b4 | mistake | best | precision | best | 0.0000 | 0.268 | yes | b4 | Nb1 | -1.61 | -1.69 |
| 184828162542 | 74 | 37... axb4 | best | excellent | precision | excellent | 0.0024 | 0.746 | no | a4 | - | -1.61 | -1.45 |
| 184828162542 | 76 | 38... Bh5 | inaccuracy | mistake | precision | mistake | 0.1320 | 0.761 | no | Qh6 | Qh6 | -1.19 | -0.83 |
| 184828162542 | 77 | 39. Bb5 | mistake | blunder | precision | blunder | 0.3056 | 0.371 | no | Bxh5 | Bxh5 | -3.94 | -4.18 |
| 184828162542 | 88 | 44... Kg7 | excellent | best | precision | best | 0.0000 | 0.987 | yes | Kg7 | - | -5.69 | -6.95 |
| 184829980734 | 5 | 3. g3 | book | good | precision | good | 0.0424 | 0.577 | no | d4 | - | +0.14 | +0.22 |
| 184829980734 | 7 | 4. Bg2 | best | excellent | precision | excellent | 0.0076 | 0.607 | no | d4 | - | +0.61 | +0.65 |
| 184829980734 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0106 | 0.398 | no | Nc6 | - | +0.61 | +0.67 |
| 184829980734 | 16 | 8... d5 | best | excellent | precision | excellent | 0.0029 | 0.358 | no | O-O | - | +0.85 | +0.83 |
| 184829980734 | 19 | 10. Nc3 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Nc3 | - | -0.01 | +0.03 |
| 184829980734 | 21 | 11. Re1 | best | excellent | precision | excellent | 0.0096 | 0.502 | no | Bg5 | - | -0.01 | +0.00 |
| 184829980734 | 31 | 16. Nc3 | inaccuracy | good | precision | good | 0.0267 | 0.384 | no | Qd3 | Qd3 | -1.05 | -0.88 |
| 184829980734 | 36 | 18... Ncxd4 | best | excellent | precision | excellent | 0.0095 | 0.544 | no | Nfxd4 | - | -0.26 | -0.38 |
| 184829980734 | 39 | 20. Qxd5 | great | best | precision | best | 0.0000 | 0.467 | yes | Qxd5 | - | -0.25 | -0.41 |
| 184829980734 | 42 | 21... Qc8 | excellent | good | precision | good | 0.0253 | 0.556 | no | Qc7 | - | -0.23 | -0.19 |
| 184829980734 | 49 | 25. Qf4 | miss | blunder | precision | blunder | 0.4083 | 0.500 | no | Bg2 | Bg2 | -3.58 | -3.60 |
| 184829980734 | 50 | 25... Qd6 | inaccuracy | best | precision | best | 0.0000 | 0.908 | yes | Qd6 | Qg5 | -2.17 | -3.50 |
| 184873703892 | 9 | 5. Bd2 | book | good | precision | good | 0.0322 | 0.611 | no | Nf3 | - | +0.48 | +0.52 |
| 184873703892 | 10 | 5... Bg4 | book | best | precision | best | 0.0000 | 0.418 | yes | Bg4 | - | +0.48 | +0.43 |
| 184873703892 | 11 | 6. f3 | best | excellent | precision | excellent | 0.0063 | 0.568 | no | Nf3 | - | +0.48 | +0.51 |
| 184873703892 | 13 | 7. Bc4 | good | excellent | precision | excellent | 0.0140 | 0.581 | no | f4 | - | +0.33 | +0.42 |
| 184873703892 | 14 | 7... Qb6 | great | best | precision | best | 0.0000 | 0.434 | yes | Qb6 | - | +0.33 | +0.38 |
| 184873703892 | 15 | 8. Qe2 | mistake | blunder | precision | blunder | 0.2071 | 0.560 | no | Nge2 | Nge2 | -0.90 | -0.95 |
| 184873703892 | 17 | 9. O-O-O | inaccuracy | excellent | precision | excellent | 0.0103 | 0.640 | no | d5 | d5 | +0.62 | +0.71 |
| 184873703892 | 19 | 10. d5 | good | inaccuracy | precision | inaccuracy | 0.0591 | 0.605 | no | Be3 | - | +0.35 | +0.27 |
| 184873703892 | 21 | 11. Qe1 | inaccuracy | mistake | precision | mistake | 0.1016 | 0.554 | no | Qd3 | Qd3 | -0.22 | -0.34 |
| 184873703892 | 27 | 14. Nh3 | inaccuracy | good | precision | good | 0.0344 | 0.451 | no | Kb1 | Nge2 | -0.80 | -0.53 |
| 184873703892 | 28 | 14... Qa6 | mistake | inaccuracy | precision | inaccuracy | 0.0741 | 0.584 | no | Bb4 | Bb4 | -0.01 | -0.06 |
| 184873703892 | 29 | 15. Kb1 | inaccuracy | good | precision | good | 0.0302 | 0.490 | no | Ng5 | Nf4 | -0.30 | -0.25 |
| 184873703892 | 33 | 17. Nxe6 | miss | inaccuracy | precision | inaccuracy | 0.0713 | 0.642 | no | Qg3 | Qg3 | +0.33 | +0.55 |
| 184873703892 | 36 | 18... Bd4 | blunder | mistake | precision | mistake | 0.1378 | 0.412 | no | g6 | - | +1.62 | +1.53 |
| 184873703892 | 40 | 20... fxe6 | inaccuracy | good | precision | good | 0.0302 | 0.500 | no | Qxe6 | Qxe6 | +0.26 | +0.29 |
| 184873703892 | 41 | 21. Qe1 | excellent | best | precision | best | 0.0000 | 0.546 | yes | Qe1 | - | +0.17 | +0.22 |
| 184873703892 | 42 | 21... Qc6 | excellent | best | precision | best | 0.0000 | 0.465 | yes | Qc6 | - | +0.24 | +0.21 |
| 184873703892 | 43 | 22. Ne2 | best | excellent | precision | excellent | 0.0048 | 0.533 | no | a3 | - | +0.24 | +0.19 |
| 184873703892 | 47 | 24. Bg5 | excellent | best | precision | best | 0.0000 | 0.543 | yes | Bg5 | - | +0.25 | +0.19 |
| 184873703892 | 48 | 24... Qd5 | inaccuracy | mistake | precision | mistake | 0.1034 | 0.470 | no | Qe8 | Qd6 | +0.80 | +0.86 |
| 184873703892 | 52 | 26... Qe5 | good | excellent | precision | excellent | 0.0000 | 0.369 | no | Qg5 | - | +0.98 | +0.76 |
| 184873703892 | 55 | 28. Qd3 | best | excellent | precision | excellent | 0.0015 | 0.640 | no | Rg1 | - | +1.04 | +0.94 |
| 184873703892 | 57 | 29. Qf5+ | great | best | precision | best | 0.0000 | 0.634 | yes | Qf5+ | - | +1.04 | +1.00 |
| 184873703892 | 58 | 29... Kb8 | good | excellent | precision | excellent | 0.0086 | 0.346 | no | Rd7 | - | +1.24 | +1.01 |
| 184873703892 | 59 | 30. h4 | miss | mistake | precision | mistake | 0.1110 | 0.656 | no | Qxf6 | Qxf6 | +0.29 | +0.20 |
| 184873703892 | 60 | 30... a6 | good | excellent | precision | excellent | 0.0158 | 0.468 | no | Qe2 | - | +0.51 | +0.52 |
| 184873703892 | 62 | 31... Rd6 | best | excellent | precision | excellent | 0.0047 | 0.444 | no | Rd5 | - | +0.51 | +0.40 |
| 184873703892 | 63 | 32. Qf4 | good | excellent | precision | excellent | 0.0157 | 0.563 | no | Qf7 | - | +0.39 | +0.30 |
| 184873703892 | 66 | 33... Rd6 | best | good | precision | good | 0.0206 | 0.374 | no | Qe2 | - | +0.88 | +0.95 |
| 184873703892 | 70 | 35... Ka7 | best | good | precision | good | 0.0379 | 0.409 | no | Rh6 | - | +0.89 | +0.97 |
| 184873703892 | 71 | 36. Rd1 | excellent | best | precision | best | 0.0000 | 0.650 | yes | Rd1 | - | +0.88 | +0.81 |
| 184873703892 | 76 | 38... Qh2 | mistake | blunder | precision | blunder | 0.2062 | 0.490 | no | Rf6 | Rf6 | +1.42 | +1.45 |
| 184873703892 | 77 | 39. Qf5 | great | best | precision | best | 0.0000 | 0.716 | yes | Qf5 | - | +1.42 | +1.62 |
| 184873703892 | 79 | 40. Kb1 | mistake | inaccuracy | precision | inaccuracy | 0.0871 | 0.740 | no | f4 | Re1 | +0.91 | +0.82 |
| 184873703892 | 81 | 41. Qe4 | mistake | inaccuracy | precision | inaccuracy | 0.0685 | 0.660 | no | Qg5 | Qg4 | +0.52 | +0.58 |
| 184873703892 | 82 | 41... d3 | great | best | precision | best | 0.0000 | 0.409 | yes | d3 | - | +0.52 | +0.63 |
| 184873703892 | 85 | 43. Qd4+ | great | best | precision | best | 0.0000 | 0.610 | yes | Qd4+ | - | +0.83 | +0.55 |
| 184873703892 | 86 | 43... Ka8 | excellent | best | precision | best | 0.0000 | 0.413 | yes | Ka8 | - | +0.87 | +0.59 |
| 184873703892 | 88 | 44... Qxh5 | inaccuracy | mistake | precision | mistake | 0.1236 | 0.412 | no | Rd6 | Rd6 | +1.12 | +1.38 |
| 184873703892 | 92 | 46... Rb6+ | great | best | precision | best | 0.0000 | 0.500 | yes | Rb6+ | - | 0.00 | +0.00 |
| 184873703892 | 94 | 47... Qb5 | mistake | inaccuracy | precision | inaccuracy | 0.0634 | 0.500 | no | Qxf3 | Qh2+ | +0.70 | +0.40 |
| 184873703892 | 95 | 48. Rc1 | miss | inaccuracy | precision | inaccuracy | 0.0634 | 0.563 | no | c4 | Re1 | 0.00 | +0.00 |
| 184873703892 | 96 | 48... Qb3+ | excellent | best | precision | best | 0.0000 | 0.500 | no | Ka8 | - | +0.09 | +0.00 |
| 185110487484 | 7 | 4. Bd3 | book | best | precision | best | 0.0000 | 0.543 | yes | Bd3 | - | +0.13 | +0.19 |
| 185110487484 | 8 | 4... Nc6 | book | excellent | precision | excellent | 0.0063 | 0.470 | no | c5 | - | +0.16 | +0.23 |
| 185110487484 | 11 | 6. O-O | good | excellent | precision | excellent | 0.0175 | 0.533 | no | c3 | - | +0.12 | +0.10 |
| 185110487484 | 16 | 8... Ne7 | best | excellent | precision | excellent | 0.0016 | 0.502 | no | Nf6 | - | -0.04 | -0.08 |
| 185110487484 | 17 | 9. Nbc3 | good | excellent | precision | excellent | 0.0111 | 0.487 | no | Nd2 | - | -0.22 | -0.15 |
| 185110487484 | 18 | 9... Bf5 | good | excellent | precision | excellent | 0.0016 | 0.524 | no | c6 | - | +0.02 | -0.14 |
| 185110487484 | 19 | 10. Qg3 | good | excellent | precision | excellent | 0.0032 | 0.478 | no | Qd2 | - | -0.18 | -0.18 |
| 185110487484 | 20 | 10... Bxf4 | great | best | precision | best | 0.0000 | 0.529 | yes | Bxf4 | - | -0.18 | -0.17 |
| 185110487484 | 24 | 12... Bxc2 | excellent | good | precision | good | 0.0222 | 0.551 | no | c6 | - | -0.15 | -0.15 |
| 185110487484 | 25 | 13. Rac1 | good | excellent | precision | excellent | 0.0127 | 0.476 | no | Qe3 | - | -0.31 | -0.34 |
| 185110487484 | 27 | 14. h4 | inaccuracy | excellent | precision | excellent | 0.0141 | 0.451 | no | Qh4 | Qh4 | -0.68 | -0.54 |
| 185110487484 | 28 | 14... Nf5 | mistake | inaccuracy | precision | inaccuracy | 0.0995 | 0.585 | no | c6 | h6 | +0.08 | +0.09 |
| 185110487484 | 30 | 15... Qxh4 | good | best | precision | best | 0.0000 | 0.482 | yes | Qxh4 | - | +0.24 | +0.19 |
| 185110487484 | 35 | 18. Ne7+ | great | best | precision | best | 0.0000 | 0.524 | yes | Ne7+ | - | +0.24 | +0.14 |
| 185110487484 | 40 | 20... Nf5 | best | good | precision | good | 0.0270 | 0.498 | no | h6 | - | +0.10 | +0.18 |
| 185110487484 | 41 | 21. Nxf5 | inaccuracy | good | precision | good | 0.0430 | 0.529 | no | Rc7 | Rc7 | -0.22 | -0.09 |
| 185110487484 | 43 | 22. Re7 | best | good | precision | good | 0.0207 | 0.503 | no | Rc7 | - | -0.22 | -0.05 |
| 185110487484 | 46 | 23... Rac8 | great | best | precision | best | 0.0000 | 0.486 | yes | Rac8 | - | +0.04 | +0.14 |
| 185110487484 | 49 | 25. Ra1 | excellent | best | precision | best | 0.0000 | 0.486 | yes | Ra1 | - | -0.20 | -0.11 |
| 185110487484 | 51 | 26. Rxa7 | excellent | best | precision | best | 0.0000 | 0.490 | yes | Rxa7 | - | -0.23 | -0.04 |
| 185110487484 | 52 | 26... b5 | good | excellent | precision | excellent | 0.0048 | 0.506 | no | Rb8 | - | -0.11 | -0.04 |
| 185110487484 | 58 | 29... Rc1+ | best | excellent | precision | excellent | 0.0143 | 0.505 | no | Rc2 | - | -0.02 | +0.06 |
| 185110487484 | 60 | 30... Rc2 | good | excellent | precision | excellent | 0.0096 | 0.510 | no | h6 | - | +0.19 | +0.01 |
| 185110487484 | 61 | 31. f3 | good | best | precision | best | 0.0000 | 0.502 | yes | f3 | - | -0.04 | +0.00 |
| 185110487484 | 62 | 31... h6 | excellent | best | precision | best | 0.0000 | 0.500 | no | h5 | - | +0.07 | +0.03 |
| 185110487484 | 63 | 32. Kg3 | good | excellent | precision | excellent | 0.0127 | 0.505 | no | Rbb7 | - | -0.15 | -0.26 |
| 185110487484 | 64 | 32... g6 | good | best | precision | best | 0.0000 | 0.541 | yes | g6 | - | -0.02 | -0.02 |
| 185110487484 | 66 | 33... Kg7 | excellent | best | precision | best | 0.0000 | 0.516 | yes | Kg7 | - | -0.02 | +0.00 |
| 185110487484 | 67 | 34. b4 | excellent | best | precision | best | 0.0000 | 0.500 | yes | b4 | - | -0.13 | +0.00 |
| 185110487484 | 68 | 34... Rc6 | good | best | precision | best | 0.0000 | 0.500 | no | Rb2 | - | 0.00 | +0.00 |
| 185110487484 | 73 | 37. Rc4 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Rc4 | - | -0.03 | +0.00 |
| 185110487484 | 74 | 37... Rb5 | good | best | precision | best | 0.0000 | 0.500 | no | g5 | - | +0.16 | +0.00 |
| 185110487484 | 75 | 38. Kf2 | good | best | precision | best | 0.0000 | 0.500 | no | Kf4 | - | 0.00 | +0.00 |
| 185110487484 | 82 | 41... Ke6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Ke6 | - | +0.02 | +0.00 |
| 185110487484 | 85 | 43. f4 | excellent | best | precision | best | 0.0000 | 0.500 | no | Rc4 | - | -0.07 | +0.00 |
| 185110487484 | 86 | 43... g5 | excellent | best | precision | best | 0.0000 | 0.500 | no | Rb8 | - | 0.00 | +0.00 |
| 185110487484 | 88 | 44... Rd5 | best | excellent | precision | excellent | 0.0032 | 0.503 | no | Rb6 | - | -0.03 | +0.00 |
| 185110487484 | 89 | 45. Rc4 | best | excellent | precision | excellent | 0.0048 | 0.500 | no | Re3 | - | -0.03 | -0.02 |
| 185110487484 | 95 | 48. Rxh6 | inaccuracy | good | precision | good | 0.0223 | 0.500 | no | Rc4 | Rc4 | -0.35 | -0.06 |
| 185110487484 | 96 | 48... Rxb4 | good | excellent | precision | excellent | 0.0096 | 0.510 | no | f6 | - | -0.14 | +0.00 |
| 185110487484 | 100 | 50... Rb3+ | great | best | precision | best | 0.0000 | 0.802 | yes | Rb3+ | - | -1.89 | -1.92 |
| 185110487484 | 101 | 51. Kg2 | excellent | best | precision | best | 0.0000 | 0.227 | yes | Kg2 | - | -1.93 | -2.11 |
| 185110487484 | 102 | 51... Kf4 | best | excellent | precision | excellent | 0.0053 | 0.793 | no | Rb2+ | - | -1.93 | -2.14 |
| 185110487484 | 107 | 54. Rd8 | good | best | precision | best | 0.0000 | 0.045 | no | Ra8 | - | -3.92 | -4.36 |
| 185110487484 | 109 | 55. Rd3 | great | good | precision | good | 0.0302 | 0.495 | no | Rd4+ | - | -0.04 | +0.00 |
| 185110487484 | 110 | 55... Rb4 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Rb4 | - | 0.00 | +0.00 |
| 185110487484 | 114 | 57... Re3 | great | best | precision | best | 0.0000 | 1.000 | yes | Re3 | - | -7.18 | -12.16 |
| 185110487484 | 115 | 58. Rxe3 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Rxe3 | - | -9.62 | -14.09 |
| 185110487484 | 117 | 59. Kh2 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kg3 | - | -10.1 | -81.15 |
| 185110487484 | 118 | 59... Kf4 | excellent | best | precision | best | 0.0000 | 1.000 | no | Kf2 | - | -9.93 | -12.20 |
| 185110487484 | 122 | 61... Kxg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kf2 | - | -9.95 | -13.15 |
| 185110487484 | 123 | 62. Kg2 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kg1 | - | -10.5 | -81.15 |
| 185110487484 | 124 | 62... Kxf5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Kxf5 | - | -7.27 | -12.97 |
| 185117573448 | 10 | 5... d6 | excellent | good | precision | good | 0.0298 | 0.539 | no | d5 | - | -0.19 | -0.14 |
| 185117573448 | 19 | 10. fxe3 | good | excellent | precision | excellent | 0.0132 | 0.503 | no | Qxe3 | - | -0.23 | -0.25 |
| 185117573448 | 21 | 11. O-O | excellent | best | precision | best | 0.0000 | 0.491 | yes | O-O | - | -0.24 | -0.17 |
| 185117573448 | 22 | 11... Qd7 | good | excellent | precision | excellent | 0.0118 | 0.512 | no | c6 | - | +0.11 | +0.00 |
| 185117573448 | 25 | 13. d4 | inaccuracy | good | precision | good | 0.0492 | 0.585 | no | Rxf6 | Rxf6 | +0.51 | +0.52 |
| 185117573448 | 26 | 13... exd4 | inaccuracy | good | precision | good | 0.0417 | 0.464 | no | Qe7 | Qe7 | +1.17 | +1.13 |
| 185117573448 | 34 | 17... Re5 | excellent | best | precision | best | 0.0000 | 0.247 | no | Bc6 | - | +3.97 | +3.94 |
| 185117573448 | 35 | 18. Qg4 | excellent | best | precision | best | 0.0000 | 0.749 | yes | Qg4 | - | +3.90 | +3.90 |
| 185117573448 | 40 | 20... Bc4 | excellent | good | precision | good | 0.0236 | 0.265 | no | Rxe1 | - | +4.04 | +4.13 |
| 185117573448 | 41 | 21. Rxe5 | excellent | best | precision | best | 0.0000 | 0.759 | yes | Rxe5 | - | +3.97 | +3.90 |
| 185117573448 | 45 | 23. Qg4 | good | inaccuracy | precision | inaccuracy | 0.0502 | 0.806 | no | Ng4 | - | +4.08 | +4.07 |
| 185117573448 | 52 | 26... Qd4+ | great | best | precision | best | 0.0000 | 0.874 | yes | Qd4+ | - | -6.57 | -7.01 |
| 185117573448 | 62 | 31... Qxf1+ | excellent | best | precision | best | 0.0000 | 1.000 | no | g5 | - | -M3 | -M3 |
| 185117573448 | 65 | 33. c3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | b3 | - | -M5 | -M5 |
| 185117573448 | 69 | 35. h4 | inaccuracy | best | precision | best | 0.0000 | 0.000 | no | a5 | a5 | -M6 | -M7 |
| 185117573448 | 73 | 37. axb5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | axb5 | - | -M6 | -M7 |
| 185117573448 | 74 | 37... a4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Bxb5 | - | -10.3 | -M8 |
| 185117573448 | 75 | 38. h6 | good | best | precision | best | 0.0000 | 0.000 | yes | h6 | - | -M7 | -M9 |
| 185117573448 | 76 | 38... gxh6 | good | best | precision | best | 0.0000 | 1.000 | yes | gxh6 | - | -10.2 | -M8 |
| 185117573448 | 77 | 39. g3 | mistake | best | precision | best | 0.0000 | 0.000 | yes | g3 | b6 | -M3 | -M5 |
| 185117573448 | 79 | 40. Kh3 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | b6 | - | -M4 | -M4 |
| 185173941140 | 7 | 4. d4 | best | excellent | precision | excellent | 0.0068 | 0.595 | no | Nf3 | - | +1.24 | +1.14 |
| 185173941140 | 8 | 4... e5 | inaccuracy | good | precision | good | 0.0463 | 0.421 | no | c6 | Nf6 | +2.05 | +1.83 |
| 185173941140 | 9 | 5. Nf3 | best | excellent | precision | excellent | 0.0007 | 0.626 | no | Bd3 | - | +2.05 | +1.66 |
| 185173941140 | 12 | 6... e4 | good | inaccuracy | precision | inaccuracy | 0.0657 | 0.358 | no | Bb4 | - | +2.76 | +3.15 |
| 185173941140 | 13 | 7. Ng5 | excellent | good | precision | good | 0.0379 | 0.708 | no | Ne5 | - | +2.48 | +2.56 |
| 185173941140 | 15 | 8. Bc4 | excellent | best | precision | best | 0.0000 | 0.710 | yes | Bc4 | - | +3.07 | +2.99 |
| 185173941140 | 16 | 8... Qxd1+ | best | excellent | precision | excellent | 0.0041 | 0.302 | no | Nh6 | - | +3.07 | +3.07 |
| 185173941140 | 23 | 12. Rxe4+ | great | best | precision | best | 0.0000 | 0.802 | yes | Rxe4+ | - | +4.99 | +4.96 |
| 185173941140 | 35 | 18. Nxa8 | great | best | precision | best | 0.0000 | 0.513 | yes | Nxa8 | - | +0.35 | +0.18 |
| 185173941140 | 40 | 20... Bxh1 | great | best | precision | best | 0.0000 | 0.826 | yes | Bxh1 | - | -5.54 | -5.80 |
| 185193771738 | 14 | 7... Qb6 | inaccuracy | good | precision | good | 0.0482 | 0.464 | no | h6 | h6 | +1.10 | +1.14 |
| 185193771738 | 15 | 8. Qxb6 | great | best | precision | best | 0.0000 | 0.584 | yes | Qxb6 | - | +1.10 | +0.97 |
| 185193771738 | 17 | 9. Bxf6 | good | excellent | precision | excellent | 0.0174 | 0.580 | no | Nd2 | - | +0.69 | +0.82 |
| 185193771738 | 22 | 11... Bd6 | excellent | good | precision | good | 0.0439 | 0.469 | no | Kd8 | - | +0.87 | +1.02 |
| 185193771738 | 31 | 16. Bxb5 | good | inaccuracy | precision | inaccuracy | 0.0539 | 0.555 | no | Nd4 | - | 0.00 | +0.01 |
| 185193771738 | 36 | 18... Bb7 | inaccuracy | excellent | precision | excellent | 0.0189 | 0.360 | no | f5 | f5 | +2.76 | +2.68 |
| 185193771738 | 40 | 20... f5 | excellent | best | precision | best | 0.0000 | 0.503 | yes | f5 | - | +0.04 | +0.02 |
| 185193771738 | 44 | 22... Rxh4 | great | best | precision | best | 0.0000 | 0.526 | yes | Rxh4 | - | -0.35 | -0.14 |
| 185193771738 | 46 | 23... fxe4 | good | excellent | precision | excellent | 0.0037 | 0.512 | no | Rxe4 | - | -0.03 | -0.07 |
| 185193771738 | 47 | 24. Rae1 | inaccuracy | good | precision | good | 0.0325 | 0.495 | no | g3 | Rf1 | -0.90 | -0.51 |
| 185193771738 | 48 | 24... f5 | good | excellent | precision | excellent | 0.0192 | 0.538 | no | Rc7 | - | -0.53 | -0.31 |
| 185193771738 | 52 | 26... Kf6 | good | best | precision | best | 0.0000 | 0.679 | yes | Kf6 | - | -1.88 | -2.24 |
| 185193771738 | 55 | 28. Rd8 | mistake | inaccuracy | precision | inaccuracy | 0.0957 | 0.401 | no | Rd1 | Rd1 | -2.68 | -2.78 |
| 185193771738 | 56 | 28... Ke7 | mistake | inaccuracy | precision | inaccuracy | 0.0942 | 0.695 | no | Ra7 | - | -1.17 | -1.10 |
| 185193771738 | 58 | 29... Ra3 | excellent | good | precision | good | 0.0361 | 0.742 | no | e3 | - | -3.16 | -3.29 |
| 185193771738 | 62 | 31... Rg7 | good | inaccuracy | precision | inaccuracy | 0.0676 | 0.808 | no | Bc5+ | - | -3.65 | -3.53 |
| 185193771738 | 63 | 32. Bh5 | good | inaccuracy | precision | inaccuracy | 0.0634 | 0.260 | no | Bc4 | - | -4.58 | -4.75 |
| 185193771738 | 64 | 32... f4 | good | excellent | precision | excellent | 0.0199 | 0.803 | no | Ra2 | - | -3.74 | -4.34 |
| 185193771738 | 65 | 33. Re8+ | good | excellent | precision | excellent | 0.0010 | 0.216 | no | g4 | - | -4.19 | -4.36 |
| 185193771738 | 67 | 34. c4 | inaccuracy | good | precision | good | 0.0434 | 0.192 | no | g3 | - | -5.45 | -5.88 |
| 185193771738 | 68 | 34... f3 | good | excellent | precision | excellent | 0.0100 | 0.851 | no | Ra2 | - | -4.98 | -5.51 |
| 185193771738 | 74 | 37... exf3 | best | excellent | precision | excellent | 0.0120 | 0.977 | no | Bc5+ | - | -9.39 | -8.46 |
| 185193771738 | 77 | 39. g3 | excellent | best | precision | best | 0.0000 | 0.070 | yes | g3 | - | -9.51 | -10.16 |
| 185193771738 | 78 | 39... Bc5+ | best | excellent | precision | excellent | 0.0066 | 0.953 | no | Rf7 | - | -9.51 | -M14 |
| 185193771738 | 80 | 40... Rf7 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Rf7 | - | -9.15 | -13.33 |
| 185217478440 | 22 | 11... a6 | good | excellent | precision | excellent | 0.0139 | 0.484 | no | Bb6 | - | +0.44 | +0.43 |
| 185217478440 | 23 | 12. d4 | excellent | best | precision | best | 0.0000 | 0.530 | yes | d4 | - | +0.37 | +0.38 |
| 185217478440 | 24 | 12... Ba7 | excellent | best | precision | best | 0.0000 | 0.473 | yes | Ba7 | - | +0.50 | +0.33 |
| 185217478440 | 25 | 13. Re1 | excellent | best | precision | best | 0.0000 | 0.523 | yes | Re1 | - | +0.45 | +0.42 |
| 185217478440 | 26 | 13... Bg4 | excellent | good | precision | good | 0.0250 | 0.471 | no | Nxd5 | - | +0.75 | +0.78 |
| 185217478440 | 34 | 17... b5 | good | excellent | precision | excellent | 0.0062 | 0.433 | no | g6 | - | +1.17 | +1.05 |
| 185217478440 | 36 | 18... a5 | excellent | good | precision | good | 0.0304 | 0.460 | no | c5 | - | +0.88 | +1.01 |
| 185217478440 | 37 | 19. e5 | excellent | good | precision | good | 0.0213 | 0.570 | no | Rad1 | - | +0.73 | +0.70 |
| 185217478440 | 41 | 21. Re3 | miss | mistake | precision | mistake | 0.1659 | 0.527 | no | dxe5 | dxe5 | -1.90 | -2.05 |
| 185217478440 | 43 | 22. Rg3 | good | excellent | precision | excellent | 0.0154 | 0.364 | no | Rf3 | - | -2.26 | -2.37 |
| 185217478440 | 44 | 22... Qf6 | excellent | good | precision | good | 0.0262 | 0.660 | no | Qd6 | - | -2.08 | -2.13 |
| 185217478440 | 45 | 23. Bb3 | inaccuracy | good | precision | good | 0.0494 | 0.355 | no | Rf3 | Rf3 | -3.22 | -2.93 |
| 185217478440 | 47 | 24. Rxg6+ | great | best | precision | best | 0.0000 | 0.846 | yes | Rxg6+ | - | +5.51 | +6.13 |
| 185217478440 | 48 | 24... Qxg6 | mistake | excellent | precision | excellent | 0.0189 | 0.153 | no | Qg7 | - | M8 | +13.24 |
| 185217478440 | 53 | 27. Bc2 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qg5+ | - | M5 | M5 |
| 185217478440 | 58 | 29... Bxf2+ | mistake | excellent | precision | excellent | 0.0167 | 0.133 | no | Rxf5 | - | +6.66 | +6.79 |
| 185217478440 | 62 | 31... Kg8 | good | inaccuracy | precision | inaccuracy | 0.0539 | 0.127 | no | b4 | - | +7.84 | +9.09 |
| 185217478440 | 67 | 34. Ke2 | best | excellent | precision | excellent | 0.0022 | 0.845 | no | Ke3 | - | +5.80 | +6.16 |
| 185217478440 | 69 | 35. Kd3 | good | best | precision | best | 0.0000 | 0.845 | yes | Kd3 | - | +5.50 | +6.35 |
| 185217478440 | 70 | 35... c5 | good | best | precision | best | 0.0000 | 0.145 | no | Kf7 | - | +6.11 | +6.26 |
| 185217478440 | 71 | 36. Kc4 | good | excellent | precision | excellent | 0.0087 | 0.852 | no | a4 | - | +5.36 | +6.02 |
| 185217478440 | 73 | 37. Rc1 | best | good | precision | good | 0.0240 | 0.889 | no | Kxc5 | - | +6.63 | +6.51 |
| 185217478440 | 75 | 38. axb3 | excellent | best | precision | best | 0.0000 | 0.892 | yes | axb3 | - | +7.53 | +7.62 |
| 185218140778 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.512 | yes | Nf6 | - | +0.07 | -0.09 |
| 185218140778 | 12 | 6... Bb7 | good | excellent | precision | excellent | 0.0126 | 0.479 | no | O-O | - | +0.59 | +0.48 |
| 185218140778 | 21 | 11. Ncxe5 | inaccuracy | excellent | precision | excellent | 0.0194 | 0.573 | no | d4 | d4 | +0.34 | +0.71 |
| 185218140778 | 22 | 11... Nxe5 | excellent | best | precision | best | 0.0000 | 0.450 | yes | Nxe5 | - | +0.51 | +0.67 |
| 185218140778 | 26 | 13... O-O | excellent | best | precision | best | 0.0000 | 0.459 | yes | O-O | - | +0.78 | +0.68 |
| 185218140778 | 27 | 14. Bg4 | good | excellent | precision | excellent | 0.0042 | 0.548 | no | Qb3 | - | +0.22 | +0.78 |
| 185218140778 | 31 | 16. Qe2 | excellent | good | precision | good | 0.0319 | 0.733 | no | Qf3 | - | +2.84 | +3.13 |
| 185218140778 | 32 | 16... Bb6 | best | good | precision | good | 0.0294 | 0.293 | no | Rf8 | - | +2.84 | +3.65 |
| 185218140778 | 33 | 17. g3 | good | mistake | precision | mistake | 0.1124 | 0.736 | no | Bxd7 | - | +2.25 | +1.80 |
| 185218140778 | 38 | 19... Bxf3+ | excellent | best | precision | best | 0.0000 | 0.500 | yes | Bxf3+ | - | -0.07 | -0.03 |
| 185218140778 | 43 | 22. Rxf7 | inaccuracy | good | precision | good | 0.0498 | 0.815 | no | Rae1 | Rae1 | +4.24 | +4.07 |
| 185218140778 | 47 | 24. Qxf8+ | best | excellent | precision | excellent | 0.0005 | 0.766 | no | Qe4 | - | +4.24 | +4.04 |
| 185218140778 | 50 | 25... Kf7 | excellent | best | precision | best | 0.0000 | 0.246 | yes | Kf7 | - | +4.02 | +4.00 |
| 185218140778 | 56 | 28... Ke6 | best | excellent | precision | excellent | 0.0040 | 0.235 | no | d5+ | - | +4.16 | +4.27 |
| 185218140778 | 57 | 29. Kf4+ | good | excellent | precision | excellent | 0.0066 | 0.769 | no | Kd3+ | - | +3.67 | +4.14 |
| 185218140778 | 64 | 32... a4 | best | excellent | precision | excellent | 0.0015 | 0.154 | no | Ke6 | - | +5.73 | +5.94 |
| 185218140778 | 65 | 33. Rh6+ | good | excellent | precision | excellent | 0.0100 | 0.842 | no | Ke3 | - | +5.28 | +5.68 |
| 185218140778 | 66 | 33... Kc7 | good | excellent | precision | excellent | 0.0195 | 0.168 | no | Kd5 | - | +5.96 | +6.09 |
| 185218140778 | 68 | 34... Ba5 | best | excellent | precision | excellent | 0.0046 | 0.149 | no | Kd8 | - | +5.96 | +6.19 |
| 185218140778 | 69 | 35. Kd3 | best | excellent | precision | excellent | 0.0004 | 0.851 | no | g4 | - | +5.96 | +6.12 |
| 185218140778 | 73 | 37. Kc4 | good | excellent | precision | excellent | 0.0062 | 0.851 | no | h4 | - | +5.66 | +6.02 |
| 185218140778 | 75 | 38. b3 | good | excellent | precision | excellent | 0.0078 | 0.848 | no | Kd3 | - | +5.62 | +5.90 |
| 185218140778 | 77 | 39. axb3 | best | excellent | precision | excellent | 0.0035 | 0.839 | no | Kxb3 | - | +5.62 | +5.83 |
| 185218140778 | 79 | 40. d5 | good | inaccuracy | precision | inaccuracy | 0.0507 | 0.887 | no | b4 | - | +5.58 | +5.81 |
| 185218140778 | 80 | 40... d6 | mistake | excellent | precision | excellent | 0.0137 | 0.163 | no | Be1 | Be1 | +6.31 | +6.18 |
| 185218140778 | 81 | 41. Rxd6 | best | excellent | precision | excellent | 0.0000 | 0.851 | no | Rh7 | - | +6.31 | +6.91 |
| 185277691132 | 8 | 4... Nf6 | book | good | precision | good | 0.0441 | 0.418 | no | Nd7 | - | +0.80 | +0.81 |
| 185277691132 | 9 | 5. Nxf6+ | book | best | precision | best | 0.0000 | 0.626 | yes | Nxf6+ | - | +0.80 | +0.80 |
| 185277691132 | 10 | 5... gxf6 | book | excellent | precision | excellent | 0.0030 | 0.375 | no | Qxf6 | - | +0.80 | +0.92 |
| 185277691132 | 11 | 6. Nf3 | book | best | precision | best | 0.0000 | 0.642 | yes | Nf3 | - | +0.80 | +0.73 |
| 185277691132 | 13 | 7. Bd3 | good | inaccuracy | precision | inaccuracy | 0.0624 | 0.635 | no | Bc4 | - | +0.53 | +0.46 |
| 185277691132 | 17 | 9. c4 | best | excellent | precision | excellent | 0.0167 | 0.685 | no | Qe2 | - | +1.32 | +1.19 |
| 185277691132 | 18 | 9... Nb6 | mistake | inaccuracy | precision | inaccuracy | 0.0994 | 0.319 | no | Ne7 | Ne7 | +2.10 | +1.97 |
| 185277691132 | 19 | 10. b3 | miss | inaccuracy | precision | inaccuracy | 0.0702 | 0.778 | no | O-O | O-O | +1.35 | +1.39 |
| 185277691132 | 20 | 10... Bb4+ | inaccuracy | good | precision | good | 0.0367 | 0.292 | no | f5 | f5 | +1.74 | +1.77 |
| 185277691132 | 22 | 11... Bxd2+ | excellent | best | precision | best | 0.0000 | 0.260 | yes | Bxd2+ | - | +1.75 | +1.64 |
| 185277691132 | 25 | 13. Qh6 | good | inaccuracy | precision | inaccuracy | 0.0663 | 0.875 | no | Bxb7 | - | +2.29 | +2.22 |
| 185277691132 | 27 | 14. Bxc6+ | best | excellent | precision | excellent | 0.0097 | 0.818 | no | Qg7 | - | +2.29 | +2.29 |
| 185277691132 | 30 | 15... Qe7 | inaccuracy | good | precision | good | 0.0224 | 0.337 | no | a5 | a5 | +1.32 | +1.35 |
| 185277691132 | 34 | 17... Kb7 | inaccuracy | good | precision | good | 0.0326 | 0.440 | no | Qa3 | Qa3 | +0.84 | +0.66 |
| 185277691132 | 35 | 18. a4 | inaccuracy | good | precision | good | 0.0387 | 0.604 | no | Rhd1 | Rhd1 | +0.50 | +0.41 |
| 185277691132 | 36 | 18... a5 | excellent | inaccuracy | precision | inaccuracy | 0.0628 | 0.435 | no | e5 | - | +0.57 | +0.82 |
| 185277691132 | 37 | 19. g3 | inaccuracy | mistake | precision | mistake | 0.1277 | 0.628 | no | Qd2 | Qd2 | +0.24 | +0.00 |
| 185277691132 | 39 | 20. Re1 | inaccuracy | good | precision | good | 0.0293 | 0.602 | no | Rhd1 | Rhd1 | +0.53 | +0.46 |
| 185277691132 | 46 | 23... Rgb8 | excellent | good | precision | good | 0.0300 | 0.175 | no | Rgd8 | - | +2.59 | +2.78 |
| 185277691132 | 47 | 24. Rb1 | excellent | good | precision | good | 0.0365 | 0.855 | no | d5 | - | +2.35 | +2.36 |
| 185277691132 | 49 | 25. Rdd1 | excellent | good | precision | good | 0.0239 | 0.837 | no | a5 | - | +2.28 | +2.31 |
| 185277691132 | 50 | 25... Qa3 | excellent | good | precision | good | 0.0324 | 0.187 | no | Nd7 | - | +2.54 | +2.67 |
| 185277691132 | 51 | 26. Ra1 | excellent | good | precision | good | 0.0304 | 0.846 | no | Ne1 | - | +2.40 | +2.33 |
| 185277691132 | 57 | 29. Nd2 | excellent | best | precision | best | 0.0000 | 0.952 | yes | Nd2 | - | +4.29 | +4.52 |
| 185277691132 | 58 | 29... Qf5+ | excellent | best | precision | best | 0.0000 | 0.053 | yes | Qf5+ | - | +4.46 | +4.64 |
| 185277691132 | 61 | 31. Rf1 | excellent | best | precision | best | 0.0000 | 0.942 | yes | Rf1 | - | +4.37 | +4.46 |
| 185277691132 | 68 | 34... c5 | excellent | good | precision | good | 0.0225 | 0.070 | no | Qd5 | - | +4.86 | +4.69 |
| 185277691132 | 71 | 36. Rf8+ | excellent | good | precision | good | 0.0224 | 0.960 | no | Qe4 | - | +4.26 | +4.31 |
| 185277691132 | 75 | 38. Rxb8+ | best | excellent | precision | excellent | 0.0019 | 0.936 | no | Qf1 | - | +4.26 | +4.25 |
| 185277691132 | 77 | 39. Qe8+ | best | excellent | precision | excellent | 0.0066 | 0.942 | no | Qf1 | - | +4.26 | +4.37 |
| 185277691132 | 80 | 40... Rc6 | excellent | best | precision | best | 0.0000 | 0.054 | yes | Rc6 | - | +4.58 | +4.79 |
| 185277691132 | 81 | 41. b4 | excellent | best | precision | best | 0.0000 | 0.955 | yes | b4 | - | +4.43 | +4.75 |
| 185277691132 | 82 | 41... Qd5 | best | excellent | precision | excellent | 0.0019 | 0.046 | no | Qxg3 | - | +4.43 | +4.80 |
| 185277691132 | 88 | 44... Qf3+ | best | excellent | precision | excellent | 0.0002 | 0.965 | no | e5 | - | -5.24 | -5.08 |
| 185277691132 | 92 | 46... Qf3+ | excellent | best | precision | best | 0.0000 | 0.970 | yes | Qf3+ | - | -4.84 | -5.24 |
| 185277691132 | 94 | 47... Qf2+ | best | excellent | precision | excellent | 0.0057 | 0.966 | no | Qe2+ | - | -4.84 | -4.85 |
| 185277691132 | 100 | 50... Qg3+ | excellent | best | precision | best | 0.0000 | 0.966 | yes | Qg3+ | - | -4.91 | -4.89 |
| 185277691132 | 102 | 51... Qg2+ | excellent | best | precision | best | 0.0000 | 0.968 | yes | Qg2+ | - | -4.89 | -5.17 |
| 185277691132 | 103 | 52. Kb3 | best | excellent | precision | excellent | 0.0021 | 0.036 | no | Kc3 | - | -4.89 | -5.20 |
| 185328167888 | 4 | 2... Nf6 | best | excellent | precision | excellent | 0.0113 | 0.536 | no | d5 | - | -0.43 | -0.37 |
| 185328167888 | 8 | 4... Nc6 | inaccuracy | mistake | precision | mistake | 0.1002 | 0.566 | no | Nbd7 | - | +0.37 | +0.49 |
| 185328167888 | 10 | 5... Bd6 | excellent | best | precision | best | 0.0000 | 0.598 | yes | Bd6 | - | -1.37 | -1.35 |
| 185328167888 | 11 | 6. Bg2 | good | excellent | precision | excellent | 0.0197 | 0.405 | no | e3 | - | -1.71 | -1.57 |
| 185328167888 | 21 | 11. Bc3 | inaccuracy | excellent | precision | excellent | 0.0152 | 0.589 | no | Bd4 | Bd4 | +0.79 | +1.10 |
| 185328167888 | 24 | 12... Rg6 | good | inaccuracy | precision | inaccuracy | 0.0609 | 0.314 | no | Kf8 | - | +3.02 | +3.92 |
| 185328167888 | 34 | 17... Nd5 | miss | inaccuracy | precision | inaccuracy | 0.0980 | 0.876 | no | Bxf4 | Bxf4 | -4.30 | -4.42 |
| 185328167888 | 35 | 18. Bh8 | mistake | good | precision | good | 0.0422 | 0.222 | no | dxe4 | dxe4 | -5.56 | -5.35 |
| 185328167888 | 39 | 20. Nd2 | excellent | good | precision | good | 0.0255 | 0.248 | no | Nc3 | - | -4.30 | -4.42 |
| 185328167888 | 44 | 22... O-O-O | excellent | best | precision | best | 0.0000 | 0.314 | yes | O-O-O | - | +2.88 | +2.80 |
| 185328167888 | 46 | 23... Re8 | good | inaccuracy | precision | inaccuracy | 0.0648 | 0.319 | no | Bd5 | - | +3.61 | +3.79 |
| 185330935602 | 5 | 3. Bb5 | excellent | best | precision | best | 0.0000 | 0.441 | yes | Bb5 | - | -0.90 | -0.90 |
| 185330935602 | 6 | 3... Nf6 | excellent | best | precision | best | 0.0000 | 0.565 | yes | Nf6 | - | -0.88 | -0.90 |
| 185330935602 | 10 | 5... a6 | excellent | best | precision | best | 0.0000 | 0.461 | yes | a6 | - | +0.62 | +0.63 |
| 185330935602 | 12 | 6... d6 | excellent | best | precision | best | 0.0000 | 0.522 | yes | d6 | - | -0.29 | +0.00 |
| 185330935602 | 13 | 7. Qc3 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Qc3 | - | -0.53 | -0.25 |
| 185330935602 | 15 | 8. Qb3 | excellent | best | precision | best | 0.0000 | 0.514 | yes | Qb3 | - | -0.07 | -0.13 |
| 185330935602 | 17 | 9. Qa4 | mistake | inaccuracy | precision | inaccuracy | 0.0719 | 0.558 | no | Be2 | Nf3 | -0.64 | -0.19 |
| 185330935602 | 19 | 10. Bxb5 | great | best | precision | best | 0.0000 | 0.636 | yes | Bxb5 | - | +1.77 | +1.96 |
| 185334658860 | 15 | 8. Nf3 | great | best | precision | best | 0.0000 | 0.456 | yes | Nf3 | - | -0.51 | -0.60 |
| 185334658860 | 17 | 9. Nxd4 | excellent | best | precision | best | 0.0000 | 0.472 | yes | Nxd4 | - | -0.47 | -0.53 |
| 185334658860 | 20 | 10... Bc5 | good | excellent | precision | excellent | 0.0081 | 0.545 | no | Bb6 | - | -0.28 | -0.31 |
| 185334658860 | 26 | 13... Bg4 | inaccuracy | mistake | precision | mistake | 0.1068 | 0.548 | no | Nxe4 | Nxe4 | +0.85 | +0.80 |
| 185334658860 | 28 | 14... Bh5 | inaccuracy | good | precision | good | 0.0484 | 0.448 | no | Be6 | Be6 | +1.41 | +1.38 |
| 185334658860 | 30 | 15... c5 | mistake | inaccuracy | precision | inaccuracy | 0.0800 | 0.464 | no | Bg6 | Bg6 | +1.64 | +1.60 |
| 185334658860 | 31 | 16. d5 | inaccuracy | good | precision | good | 0.0391 | 0.616 | no | dxc5 | Be3 | +0.96 | +1.05 |
| 185334658860 | 33 | 17. a3 | good | excellent | precision | excellent | 0.0174 | 0.576 | no | Qc2 | - | +0.76 | +0.80 |
| 185334658860 | 39 | 20. b5 | excellent | good | precision | good | 0.0219 | 0.566 | no | Bb2 | - | +0.53 | +0.60 |
| 185334658860 | 41 | 21. bxa6 | best | excellent | precision | excellent | 0.0087 | 0.566 | no | Na4 | - | +0.87 | +0.86 |
| 185334658860 | 42 | 21... bxa6 | best | excellent | precision | excellent | 0.0167 | 0.437 | no | Nd7 | - | +0.87 | +1.13 |
| 185334658860 | 49 | 25. Qc6 | good | excellent | precision | excellent | 0.0022 | 0.578 | no | Qc4 | - | +0.91 | +1.13 |
| 185334658860 | 50 | 25... Bxc3 | blunder | mistake | precision | mistake | 0.1620 | 0.417 | no | Rb8 | - | +3.72 | +3.62 |
| 185334658860 | 53 | 27. Qc6 | excellent | good | precision | good | 0.0301 | 0.763 | no | Bf4 | - | +3.35 | +3.42 |
| 185363017994 | 6 | 3... d6 | book | good | precision | good | 0.0416 | 0.489 | no | Nf6 | - | +0.65 | +0.73 |
| 185363017994 | 11 | 6. Nxe7 | excellent | good | precision | good | 0.0295 | 0.496 | no | Bc4 | - | -0.27 | -0.46 |
| 185363017994 | 17 | 9. h3 | excellent | best | precision | best | 0.0000 | 0.481 | yes | h3 | - | -0.57 | -0.24 |
| 185363017994 | 28 | 14... exf4 | great | best | precision | best | 0.0000 | 0.698 | yes | exf4 | - | -2.95 | -2.90 |
| 185363017994 | 37 | 19. Qf3 | good | excellent | precision | excellent | 0.0150 | 0.269 | no | Qh5 | - | -3.87 | -3.74 |
| 185363017994 | 40 | 20... Qxc4+ | excellent | best | precision | best | 0.0000 | 0.682 | yes | Qxc4+ | - | -2.59 | -2.63 |
| 185363017994 | 42 | 21... Bd4+ | excellent | good | precision | good | 0.0281 | 0.756 | no | Rae8 | - | -3.40 | -3.41 |
| 185363017994 | 47 | 24. Kh2 | good | excellent | precision | excellent | 0.0128 | 0.310 | no | Re2 | - | -3.10 | -2.98 |
| 185363017994 | 54 | 27... c5 | good | inaccuracy | precision | inaccuracy | 0.0519 | 0.732 | no | Rfe8 | - | -2.52 | -2.62 |
| 185363017994 | 56 | 28... Qb2+ | good | inaccuracy | precision | inaccuracy | 0.0508 | 0.679 | no | Qe7 | - | -2.14 | -1.82 |
| 185363017994 | 60 | 30... Qc3 | excellent | good | precision | good | 0.0201 | 0.690 | no | g6 | - | -2.44 | -2.64 |
| 185363017994 | 61 | 31. Rgd5 | best | excellent | precision | excellent | 0.0056 | 0.318 | no | Qf4 | - | -2.44 | -2.45 |
| 185363017994 | 64 | 32... Qb4 | good | excellent | precision | excellent | 0.0000 | 0.710 | no | Qa5 | - | -2.58 | -3.40 |
| 185363017994 | 70 | 35... Qxa2 | best | excellent | precision | excellent | 0.0076 | 0.753 | no | h6 | - | -3.64 | -3.70 |
| 185363017994 | 71 | 36. Qd7 | good | inaccuracy | precision | inaccuracy | 0.0519 | 0.256 | no | h4 | - | -4.66 | -4.72 |
| 185363017994 | 73 | 37. Rd1 | excellent | best | precision | best | 0.0000 | 0.205 | yes | Rd1 | - | -4.76 | -4.60 |
| 185363017994 | 77 | 39. e6 | mistake | inaccuracy | precision | inaccuracy | 0.0727 | 0.240 | no | Rf1 | - | -5.18 | -5.57 |
| 185363017994 | 79 | 40. Re1 | blunder | mistake | precision | mistake | 0.1629 | 0.204 | no | Kg2 | - | -M13 | -10.91 |
| 185363017994 | 83 | 42. Kh1 | good | best | precision | best | 0.0000 | 0.199 | no | Kg1 | - | -4.77 | -4.53 |
| 185363017994 | 90 | 45... Qa8+ | best | excellent | precision | excellent | 0.0007 | 0.511 | no | a5 | - | -0.17 | -0.13 |
| 185363017994 | 95 | 48. Qa2 | blunder | mistake | precision | mistake | 0.1423 | 0.219 | no | Kf2 | - | -8.21 | -8.63 |
| 185363017994 | 100 | 50... Qb4+ | best | excellent | precision | excellent | 0.0184 | 0.720 | no | Qa5+ | - | -2.92 | -3.49 |
| 185363017994 | 101 | 51. Kc2 | good | excellent | precision | excellent | 0.0172 | 0.268 | no | Ke2 | - | -3.35 | -3.51 |
| 185363017994 | 103 | 52. Kb2 | inaccuracy | mistake | precision | mistake | 0.1462 | 0.257 | no | Kd3 | Kd3 | -3.99 | -6.18 |
| 185363017994 | 106 | 53... Qe1+ | excellent | best | precision | best | 0.0000 | 0.905 | yes | Qe1+ | - | -4.69 | -7.42 |
| 185461631884 | 11 | 6. O-O | good | excellent | precision | excellent | 0.0071 | 0.570 | no | Qb3 | - | +0.71 | +0.74 |
| 185461631884 | 12 | 6... Be7 | inaccuracy | good | precision | good | 0.0368 | 0.447 | no | Nc6 | Nc6 | +1.48 | +1.26 |
| 185461631884 | 13 | 7. Nxc3 | inaccuracy | good | precision | good | 0.0254 | 0.590 | no | Qb3 | Qb3 | +0.75 | +0.71 |
| 185461631884 | 22 | 11... Bf5 | good | excellent | precision | excellent | 0.0135 | 0.577 | no | Na6 | - | -0.81 | -0.88 |
| 185461631884 | 28 | 14... Bxd3 | excellent | best | precision | best | 0.0000 | 0.640 | yes | Bxd3 | - | -1.89 | -1.97 |
| 185461631884 | 31 | 16. Qd1 | inaccuracy | good | precision | good | 0.0237 | 0.360 | no | Qc2 | Qc2 | -2.53 | -2.36 |
| 185461631884 | 32 | 16... Nd7 | inaccuracy | good | precision | good | 0.0466 | 0.664 | no | Re8 | Re8 | -1.71 | -1.66 |
| 185461631884 | 33 | 17. Rb1 | best | excellent | precision | excellent | 0.0088 | 0.382 | no | Qc2 | - | -1.71 | -1.81 |
| 185461631884 | 34 | 17... b5 | good | excellent | precision | excellent | 0.0136 | 0.628 | no | a6 | - | -1.48 | -1.61 |
| 185461631884 | 35 | 18. Nd4 | best | excellent | precision | excellent | 0.0109 | 0.386 | no | Be3 | - | -1.48 | -1.68 |
| 185461631884 | 36 | 18... a6 | excellent | good | precision | good | 0.0242 | 0.619 | no | Bxd4 | - | -1.32 | -1.33 |
| 185461631884 | 39 | 20. Bf4 | good | excellent | precision | excellent | 0.0179 | 0.397 | no | b3 | - | -1.70 | -1.71 |
| 185461631884 | 42 | 21... dxe5 | excellent | best | precision | best | 0.0000 | 0.548 | yes | dxe5 | - | -0.59 | -0.54 |
| 185461631884 | 45 | 23. Rxb3 | excellent | best | precision | best | 0.0000 | 0.488 | yes | Rxb3 | - | -0.29 | -0.26 |
| 185461631884 | 46 | 23... h6 | excellent | good | precision | good | 0.0217 | 0.519 | no | g6 | - | 0.00 | +0.04 |
| 185461631884 | 49 | 25. Rxe4 | excellent | best | precision | best | 0.0000 | 0.507 | yes | Rxe4 | - | +0.04 | +0.02 |
| 185461631884 | 54 | 27... Qd6 | good | excellent | precision | excellent | 0.0166 | 0.509 | no | Be5 | - | +0.31 | +0.11 |
| 185461631884 | 55 | 28. Re3 | mistake | inaccuracy | precision | inaccuracy | 0.0883 | 0.508 | no | h4 | Rd3 | -1.31 | -1.12 |
| 185461631884 | 59 | 30. Qxh5 | mistake | inaccuracy | precision | inaccuracy | 0.0840 | 0.418 | no | Qc2 | Qc2 | -2.40 | -2.38 |
| 185461631884 | 66 | 33... Qxe3 | excellent | best | precision | best | 0.0000 | 0.551 | yes | Qxe3 | - | -0.62 | -0.74 |
| 185461631884 | 68 | 34... Be5+ | great | best | precision | best | 0.0000 | 0.911 | yes | Be5+ | - | -8.01 | -10.56 |
| 185461631884 | 69 | 35. g3 | excellent | best | precision | best | 0.0000 | 0.045 | yes | g3 | - | -8.18 | -8.12 |
| 185617589205 | 7 | 4. b3 | book | excellent | precision | excellent | 0.0127 | 0.530 | no | d4 | - | +0.12 | +0.11 |
| 185617589205 | 8 | 4... Bd6 | book | excellent | precision | excellent | 0.0064 | 0.482 | no | c5 | - | +0.19 | +0.19 |
| 185617589205 | 9 | 5. Bb2 | book | best | precision | best | 0.0000 | 0.530 | yes | Bb2 | - | +0.10 | +0.15 |
| 185617589205 | 10 | 5... O-O | book | excellent | precision | excellent | 0.0016 | 0.476 | no | Nbd7 | - | +0.13 | +0.08 |
| 185617589205 | 11 | 6. Nc3 | excellent | best | precision | best | 0.0000 | 0.513 | yes | Nc3 | - | +0.12 | -0.02 |
| 185617589205 | 12 | 6... Nc6 | good | inaccuracy | precision | inaccuracy | 0.0508 | 0.503 | no | c5 | - | +0.26 | +0.30 |
| 185617589205 | 17 | 9. Qc2 | inaccuracy | best | precision | best | 0.0000 | 0.519 | no | Nb5 | - | -0.15 | -0.01 |
| 185617589205 | 23 | 12. Bd3 | great | best | precision | best | 0.0000 | 0.701 | yes | Bd3 | - | +1.32 | +1.36 |
| 185617589205 | 24 | 12... Nxe4 | best | excellent | precision | excellent | 0.0013 | 0.296 | no | Bxe4 | - | +1.32 | +1.27 |
| 185617589205 | 29 | 15. h5 | good | excellent | precision | excellent | 0.0150 | 0.699 | no | Qxb7 | - | +1.20 | +1.23 |
| 185617589205 | 34 | 17... Nd7 | inaccuracy | good | precision | good | 0.0440 | 0.320 | no | e4 | e4 | +1.54 | +1.60 |
| 185617589205 | 35 | 18. Qc6 | excellent | best | precision | best | 0.0000 | 0.735 | yes | Qc6 | - | +1.53 | +1.66 |
| 185617589205 | 36 | 18... Rb8 | excellent | best | precision | best | 0.0000 | 0.258 | yes | Rb8 | - | +1.62 | +1.65 |
| 185617589205 | 37 | 19. d3 | excellent | best | precision | best | 0.0000 | 0.741 | yes | d3 | - | +1.57 | +1.55 |
| 185617589205 | 39 | 20. Qc2 | excellent | good | precision | good | 0.0256 | 0.755 | no | Qc4 | - | +1.52 | +1.49 |
| 185617589205 | 41 | 21. Rh4 | inaccuracy | excellent | precision | excellent | 0.0077 | 0.725 | no | Qc4 | Qc4 | +1.30 | +1.65 |
| 185617589205 | 42 | 21... Rb4 | mistake | inaccuracy | precision | inaccuracy | 0.0944 | 0.259 | no | Nd5 | Nd5 | +2.44 | +2.55 |
| 185617589205 | 48 | 24... Qd7 | excellent | good | precision | good | 0.0271 | 0.172 | no | Qe7 | - | +2.41 | +2.79 |
| 185617589205 | 49 | 25. Ng5 | excellent | inaccuracy | precision | inaccuracy | 0.0509 | 0.855 | no | Qc6 | - | +2.32 | +2.19 |
| 185617589205 | 50 | 25... Bf8 | good | inaccuracy | precision | inaccuracy | 0.0878 | 0.199 | no | c5 | - | +2.97 | +3.27 |
| 185617589205 | 53 | 27. Nf3 | great | best | precision | best | 0.0000 | 0.873 | yes | Nf3 | - | +2.97 | +3.37 |
| 185617589205 | 54 | 27... Bxh6 | best | excellent | precision | excellent | 0.0024 | 0.105 | no | Qh5 | - | +2.97 | +3.24 |
| 185617589205 | 55 | 28. Qc6 | excellent | good | precision | good | 0.0392 | 0.887 | no | Qd6 | - | +2.66 | +2.85 |
| 185617589205 | 57 | 29. Qa8+ | best | good | precision | good | 0.0281 | 0.879 | no | Qa4 | - | +2.66 | +2.72 |
| 185617589205 | 60 | 30... Re8 | good | inaccuracy | precision | inaccuracy | 0.0616 | 0.142 | no | Bxe3 | - | +3.31 | +3.82 |
| 185617589205 | 63 | 32. Rc7 | good | excellent | precision | excellent | 0.0072 | 0.921 | no | Kf1 | - | +3.02 | +3.71 |
| 185617589205 | 64 | 32... Qxg2 | best | excellent | precision | excellent | 0.0086 | 0.086 | no | Kg8 | - | +3.02 | +3.84 |
| 185617589205 | 65 | 33. Bxe5+ | excellent | good | precision | good | 0.0415 | 0.920 | no | Rxf7+ | - | +3.00 | +3.03 |
| 185617589205 | 69 | 35. Kd1 | inaccuracy | excellent | precision | excellent | 0.0022 | 0.925 | no | Kd2 | Kd2 | +1.93 | +3.18 |
| 185617589205 | 70 | 35... Qf1+ | best | good | precision | good | 0.0243 | 0.117 | no | Nf5 | - | +1.93 | +2.71 |
| 185617589205 | 74 | 37... Nf5 | excellent | good | precision | good | 0.0273 | 0.055 | no | Rc8+ | - | +4.61 | +5.57 |
| 185617589205 | 75 | 38. Rxf5 | miss | blunder | precision | blunder | 0.2262 | 0.972 | no | Rxh7 | Rxh7 | +1.61 | +1.84 |
| 185617589205 | 77 | 39. Bc3 | mistake | good | precision | good | 0.0467 | 0.723 | no | f4 | - | +0.93 | +1.04 |
| 185617589205 | 79 | 40. Qa6 | great | best | precision | best | 0.0000 | 0.961 | yes | Qa6 | - | +4.51 | +5.44 |
| 185617589205 | 86 | 43... Kf7 | best | excellent | precision | excellent | 0.0038 | 0.021 | no | Kf8 | - | +5.62 | +6.17 |
| 185617589205 | 90 | 45... Kd7 | best | excellent | precision | excellent | 0.0015 | 0.023 | no | Kf7 | - | +5.61 | +5.84 |
| 185617589205 | 91 | 46. Qxh7+ | excellent | best | precision | best | 0.0000 | 0.976 | yes | Qxh7+ | - | +5.52 | +6.01 |
| 185617589205 | 101 | 51. Qxc6+ | best | excellent | precision | excellent | 0.0021 | 0.984 | no | Qf3 | - | +6.15 | +6.30 |
| 185617589205 | 106 | 53... Re7 | best | excellent | precision | excellent | 0.0085 | 0.023 | no | Rh7 | - | +5.84 | +6.62 |
| 185617589205 | 109 | 55. Nxe3+ | best | excellent | precision | excellent | 0.0002 | 1.000 | no | Kxe3 | - | M16 | +13.32 |
| 185617589205 | 110 | 55... Kc6 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kc6 | - | M13 | M14 |
| 185966191317 | 10 | 5... Ne7 | book | best | precision | best | 0.0000 | 0.463 | yes | Ne7 | - | -0.05 | +0.20 |
| 185966191317 | 11 | 6. exd5 | book | best | precision | best | 0.0000 | 0.532 | yes | exd5 | - | -0.05 | +0.08 |
| 185966191317 | 12 | 6... exd5 | book | excellent | precision | excellent | 0.0095 | 0.487 | no | Nxd5 | - | +0.07 | +0.18 |
| 185966191317 | 13 | 7. Qe2 | book | best | precision | best | 0.0000 | 0.529 | yes | Qe2 | - | +0.07 | +0.14 |
| 185966191317 | 15 | 8. Bxc6+ | good | excellent | precision | excellent | 0.0160 | 0.657 | no | Ne4 | - | +0.81 | +0.65 |
| 185966191317 | 18 | 9... Qb6 | mistake | blunder | precision | blunder | 0.2624 | 0.378 | no | d3 | d3 | +3.49 | +3.19 |
| 185966191317 | 19 | 10. Nd6+ | great | best | precision | best | 0.0000 | 0.884 | yes | Nd6+ | - | +3.49 | +3.48 |
| 185966191317 | 23 | 12. N7e5+ | good | inaccuracy | precision | inaccuracy | 0.0621 | 0.937 | no | N3e5+ | - | +2.83 | +3.06 |
| 185966191317 | 27 | 14. Qe5+ | excellent | good | precision | good | 0.0349 | 0.882 | no | d3 | - | +2.71 | +2.72 |
| 185966191317 | 29 | 15. Nd6+ | excellent | best | precision | best | 0.0000 | 0.856 | yes | Nd6+ | - | +2.57 | +2.69 |
| 185966191317 | 31 | 16. b4 | good | inaccuracy | precision | inaccuracy | 0.0708 | 0.861 | no | a4 | - | +2.06 | +2.11 |
| 185966191317 | 35 | 18. Ne4+ | excellent | good | precision | good | 0.0294 | 0.997 | no | Rb1 | - | +4.97 | +5.37 |
| 185966191317 | 39 | 20. Nxd4 | excellent | best | precision | best | 0.0000 | 0.990 | yes | Nxd4 | - | +6.36 | +6.89 |
| 186222389165 | 5 | 3. e3 | book | good | precision | good | 0.0379 | 0.562 | no | d4 | - | +0.10 | +0.15 |
| 186222389165 | 8 | 4... c5 | book | excellent | precision | excellent | 0.0175 | 0.486 | no | Bd6 | - | +0.20 | +0.20 |
| 186222389165 | 10 | 5... a6 | book | excellent | precision | excellent | 0.0032 | 0.459 | no | Nc6 | - | +0.22 | +0.28 |
| 186222389165 | 11 | 6. dxc5 | book | good | precision | good | 0.0301 | 0.544 | no | cxd5 | - | +0.07 | +0.04 |
| 186222389165 | 12 | 6... Bxc5 | book | best | precision | best | 0.0000 | 0.494 | yes | Bxc5 | - | +0.07 | +0.02 |
| 186222389165 | 14 | 7... O-O | excellent | best | precision | best | 0.0000 | 0.513 | yes | O-O | - | -0.10 | -0.09 |
| 186222389165 | 15 | 8. O-O | excellent | good | precision | good | 0.0222 | 0.486 | no | cxd5 | - | -0.20 | -0.19 |
| 186222389165 | 16 | 8... Nc6 | inaccuracy | good | precision | good | 0.0270 | 0.530 | no | dxc4 | dxc4 | +0.12 | +0.00 |
| 186222389165 | 17 | 9. Qc2 | inaccuracy | good | precision | good | 0.0381 | 0.500 | no | b3 | - | -0.24 | -0.24 |
| 186222389165 | 21 | 11. Na4 | good | excellent | precision | excellent | 0.0174 | 0.549 | no | exd4 | - | +0.19 | +0.24 |
| 186222389165 | 23 | 12. exd4 | best | excellent | precision | excellent | 0.0032 | 0.530 | no | e4 | - | +0.19 | +0.18 |
| 186222389165 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0048 | 0.471 | no | Bxd4 | - | +0.19 | +0.17 |
| 186222389165 | 27 | 14. Be3 | inaccuracy | good | precision | good | 0.0477 | 0.533 | no | Bd2 | Bd2 | -0.14 | -0.09 |
| 186222389165 | 30 | 15... Bd7 | good | excellent | precision | excellent | 0.0080 | 0.510 | no | Qc7 | - | -0.02 | -0.01 |
| 186222389165 | 35 | 18. Bf3 | excellent | best | precision | best | 0.0000 | 0.423 | yes | Bf3 | - | -0.58 | -0.43 |
| 186222389165 | 36 | 18... Qc7 | good | excellent | precision | excellent | 0.0110 | 0.568 | no | Bxf3 | - | -0.38 | -0.43 |
| 186222389165 | 37 | 19. c5 | great | best | precision | best | 0.0000 | 0.432 | yes | c5 | - | -0.38 | -0.51 |
| 186222389165 | 40 | 20... Nd5 | excellent | best | precision | best | 0.0000 | 0.577 | yes | Nd5 | - | -0.36 | -0.54 |
| 186222389165 | 41 | 21. Nc4 | blunder | mistake | precision | mistake | 0.1667 | 0.415 | no | Nxd5 | - | -1.70 | -1.58 |
| 186222389165 | 42 | 21... b5 | great | best | precision | best | 0.0000 | 0.732 | yes | b5 | - | -1.70 | -1.80 |
| 186222389165 | 44 | 22... Nf4 | mistake | inaccuracy | precision | inaccuracy | 0.0577 | 0.758 | no | bxc4 | bxc4 | -1.10 | -1.20 |
| 186222389165 | 46 | 23... Rd3 | great | best | precision | best | 0.0000 | 0.787 | yes | Rd3 | - | -1.96 | -1.86 |
| 186222389165 | 48 | 24... Nh3+ | good | excellent | precision | excellent | 0.0044 | 0.777 | no | Rfd8 | - | -1.68 | -1.62 |
| 186222389165 | 54 | 27... Qe5 | best | excellent | precision | excellent | 0.0092 | 0.930 | no | Nf2+ | - | -3.60 | -3.85 |
| 186222389165 | 61 | 31. c6 | excellent | good | precision | good | 0.0250 | 0.061 | no | Ne1 | - | -4.87 | -5.14 |
| 186222389165 | 65 | 33. Re1 | excellent | best | precision | best | 0.0000 | 0.041 | yes | Re1 | - | -5.15 | -5.03 |
| 186222389165 | 72 | 36... Qd5+ | best | excellent | precision | excellent | 0.0085 | 0.968 | no | Rc8 | - | -5.03 | -5.27 |
| 186222389165 | 73 | 37. Nf3 | best | excellent | precision | excellent | 0.0046 | 0.034 | no | Kf2 | - | -5.03 | -5.16 |
| 186222389165 | 75 | 38. Kg3 | best | excellent | precision | excellent | 0.0059 | 0.035 | no | a4 | - | -5.03 | -5.51 |
| 186222389165 | 78 | 39... Rxc7 | excellent | best | precision | best | 0.0000 | 0.968 | no | h6 | - | -4.87 | -5.34 |
| 186222389165 | 86 | 43... Ke7 | best | excellent | precision | excellent | 0.0087 | 0.979 | no | Kf8 | - | -5.28 | -5.59 |
| 186222389165 | 87 | 44. Qg6 | excellent | best | precision | best | 0.0000 | 0.028 | yes | Qg6 | - | -5.42 | -5.85 |
| 186222389165 | 88 | 44... Rc3 | excellent | good | precision | good | 0.0281 | 0.976 | no | Kf8 | - | -4.72 | -4.57 |
| 186222389165 | 90 | 45... Ke8 | excellent | best | precision | best | 0.0000 | 0.955 | yes | Ke8 | - | -4.49 | -4.52 |
| 186222389165 | 97 | 49. Qg7+ | great | best | precision | best | 0.0000 | 0.045 | yes | Qg7+ | - | -4.67 | +0.00 |
| 186411389477 | 12 | 6... h5 | good | inaccuracy | precision | inaccuracy | 0.0520 | 0.245 | no | Ng4 | - | +2.30 | +2.25 |
| 186411389477 | 13 | 7. h3 | good | inaccuracy | precision | inaccuracy | 0.0544 | 0.807 | no | c3 | - | +1.99 | +1.82 |
| 186411389477 | 15 | 8. Rf1 | good | excellent | precision | excellent | 0.0112 | 0.778 | no | O-O | - | +1.76 | +1.84 |
| 186411389477 | 18 | 9... Bd7 | mistake | good | precision | good | 0.0344 | 0.253 | no | Qh2 | - | +2.00 | +2.00 |
| 186411389477 | 21 | 11. dxc5 | best | excellent | precision | excellent | 0.0117 | 0.793 | no | Nd2 | - | +2.00 | +2.16 |
| 186411389477 | 22 | 11... Qxc5 | inaccuracy | mistake | precision | mistake | 0.1126 | 0.202 | no | Qg6 | Qg6 | +3.21 | +3.65 |
| 186411389477 | 23 | 12. Qd4 | best | excellent | precision | excellent | 0.0048 | 0.911 | no | Be3 | - | +3.21 | +3.45 |
| 186411389477 | 25 | 13. Be3 | inaccuracy | mistake | precision | mistake | 0.1106 | 0.911 | no | Nd2 | Nd2 | +2.26 | +2.18 |
| 186411389477 | 27 | 14. Qc4 | great | best | precision | best | 0.0000 | 0.808 | yes | Qc4 | - | +2.26 | +2.28 |
| 186411389477 | 30 | 15... c4 | good | inaccuracy | precision | inaccuracy | 0.0675 | 0.204 | no | Rd8 | - | +2.78 | +2.90 |
| 186411389477 | 37 | 19. O-O-O | brilliant | best | precision | best | 0.0000 | 0.861 | yes | O-O-O | - | +2.74 | +3.00 |
| 186411389477 | 44 | 22... Bd3 | best | excellent | precision | excellent | 0.0046 | 0.044 | no | Bd7 | - | +4.85 | +4.92 |
| 186411389477 | 48 | 24... Kh7 | excellent | best | precision | best | 0.0000 | 0.039 | yes | Kh7 | - | +4.91 | +5.44 |
| 186411389477 | 49 | 25. g4 | best | excellent | precision | excellent | 0.0068 | 0.970 | no | Re5 | - | +4.91 | +5.11 |
| 186411389477 | 51 | 26. Qe5 | excellent | good | precision | good | 0.0253 | 0.984 | no | Qxh5+ | - | +4.53 | +4.93 |
| 186411389477 | 52 | 26... Qb6 | excellent | good | precision | good | 0.0282 | 0.041 | no | Qa6 | - | +6.36 | +6.77 |
| 186411389477 | 54 | 27... Bxc4 | excellent | best | precision | best | 0.0000 | 0.014 | yes | Bxc4 | - | +6.54 | +6.82 |
| 186411389477 | 73 | 37. Rd5+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Re4 | - | +9.76 | M12 |
| 186411389477 | 77 | 39. Rxg5 | good | excellent | precision | excellent | 0.0011 | 1.000 | no | Kd1 | - | +8.41 | +10.48 |
| 186411389477 | 78 | 39... Kg3 | inaccuracy | excellent | precision | excellent | 0.0011 | 0.001 | no | Kxg5 | Kxg5 | M7 | M10 |
| 186411389477 | 80 | 40... Kh4 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kxg2 | - | M7 | M9 |
| 186411389477 | 82 | 41... Kg4 | good | best | precision | best | 0.0000 | 0.000 | no | Kh5 | - | M6 | M7 |
| 186411389477 | 83 | 42. g6 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rc5 | - | M5 | M7 |
| 186411389477 | 86 | 43... Kh4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kg4 | - | M3 | M3 |
| 186411389477 | 90 | 45... Kh4 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kg4 | - | M3 | M4 |
| 186411389477 | 92 | 46... Kg4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kg3 | - | M4 | M4 |
| 186411389477 | 96 | 48... Kg5 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kf4 | - | M3 | M3 |
| 186411389477 | 103 | 52. Rg1+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rf1 | - | M2 | M3 |
| 186411389477 | 104 | 52... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kf8 | - | M2 | M2 |
| 186429989523 | 8 | 4... h6 | good | excellent | precision | excellent | 0.0125 | 0.438 | no | dxe4 | - | +0.48 | +0.56 |
| 186429989523 | 9 | 5. Bxf6 | great | best | precision | best | 0.0000 | 0.588 | yes | Bxf6 | - | +0.48 | +0.41 |
| 186429989523 | 14 | 7... Nd7 | excellent | best | precision | best | 0.0000 | 0.440 | yes | Nd7 | - | +0.50 | +0.44 |
| 186429989523 | 16 | 8... Qd8 | excellent | good | precision | good | 0.0334 | 0.498 | no | dxe4 | - | +0.24 | +0.25 |
| 186429989523 | 18 | 9... Be7 | best | excellent | precision | excellent | 0.0063 | 0.462 | no | a6 | - | +0.24 | +0.26 |
| 186429989523 | 19 | 10. Re1 | excellent | best | precision | best | 0.0000 | 0.541 | yes | Re1 | - | +0.23 | +0.16 |
| 186429989523 | 22 | 11... Re8 | excellent | good | precision | good | 0.0286 | 0.502 | no | Qc7 | - | +0.16 | +0.17 |
| 186429989523 | 24 | 12... b6 | inaccuracy | good | precision | good | 0.0239 | 0.525 | no | a5 | b5 | +0.06 | -0.02 |
| 186429989523 | 25 | 13. h3 | good | excellent | precision | excellent | 0.0143 | 0.497 | no | Qe3 | - | -0.19 | -0.11 |
| 186429989523 | 28 | 14... Bb7 | excellent | best | precision | best | 0.0000 | 0.481 | yes | Bb7 | - | +0.01 | +0.10 |
| 186429989523 | 30 | 15... Qc7 | good | excellent | precision | excellent | 0.0016 | 0.514 | no | c5 | - | +0.13 | +0.33 |
| 186429989523 | 36 | 18... c5 | good | best | precision | best | 0.0000 | 0.616 | yes | c5 | - | -0.31 | -0.27 |
| 186429989523 | 38 | 19... f5 | great | best | precision | best | 0.0000 | 0.883 | yes | f5 | - | -3.04 | -3.00 |
| 186429989523 | 50 | 25... Qf6 | excellent | best | precision | best | 0.0000 | 0.916 | yes | Qf6 | - | -3.63 | -3.35 |
| 186429989523 | 51 | 26. Qxc5 | excellent | good | precision | good | 0.0410 | 0.106 | no | Qxf6 | - | -4.12 | -4.24 |
| 186429989523 | 53 | 27. f3 | excellent | best | precision | best | 0.0000 | 0.063 | yes | f3 | - | -4.46 | -4.65 |
| 186429989523 | 58 | 29... Bd3 | good | excellent | precision | excellent | 0.0191 | 0.846 | no | Bc2 | - | -2.17 | -2.46 |
| 186429989523 | 61 | 31. Bxg6 | excellent | best | precision | best | 0.0000 | 0.080 | yes | Bxg6 | - | -3.79 | -3.62 |
| 186429989523 | 66 | 33... Kf7 | excellent | best | precision | best | 0.0000 | 0.947 | yes | Kf7 | - | -4.63 | -4.72 |
| 186429989523 | 68 | 34... Rd7 | excellent | good | precision | good | 0.0288 | 0.967 | no | Bb5 | - | -4.10 | -4.27 |
| 186429989523 | 70 | 35... Bc4 | excellent | good | precision | good | 0.0317 | 0.974 | no | Bb5 | - | -4.51 | -4.38 |
| 186429989523 | 76 | 38... Rxf3+ | best | excellent | precision | excellent | 0.0008 | 0.955 | no | Ne5 | - | -4.57 | -4.94 |

### `miss_detector` (19)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1427 | 0.651 | no | g4 | - | -0.01 | -0.05 |
| 1034847688 | 36 | 18... Ne5 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1365 | 0.500 | no | a4 | a4 | +0.86 | +1.30 |
| 1034847688 | 37 | 19. Rh4 | mistake | miss (opportunity) | miss_detector | mistake | 0.1365 | 0.637 | no | Rh6 | Rh6 | -0.10 | +0.00 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1782 | 0.861 | no | Rxf6+ | Rxf6+ | +2.74 | +2.79 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.5057 | 0.829 | no | Rxf6+ | - | -2.81 | -2.65 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2524 | 0.752 | no | Kg7 | - | -0.17 | +0.00 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (opportunity) | miss_detector | mistake | 0.1899 | 0.190 | no | Kd2 | - | -M1 | -M1 |
| 185456088510 | 33 | 17. Ne4 | mistake | miss (tactic) | miss_detector | mistake | 0.1096 | 0.682 | no | O-O | Qe2 | +0.65 | +0.46 |
| 184678264914 | 66 | 33... d4 | mistake | miss (tactic) | miss_detector | mistake | 0.1128 | 0.978 | no | Ra8 | - | -4.32 | -5.94 |
| 184732665836 | 83 | 42. Qg3 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1099 | 0.918 | no | Kg1 | Kf1 | +4.23 | +4.75 |
| 184828162542 | 68 | 34... Rg4 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1193 | 0.855 | no | Qg6 | Qg6 | -1.50 | -1.37 |
| 184829980734 | 34 | 17... Bxf3 | mistake | miss (opportunity) | miss_detector | blunder | 0.2254 | 0.764 | no | Nxe3 | Nxe3 | -0.26 | -0.24 |
| 184873703892 | 89 | 45. Qd8+ | mistake | miss (opportunity) | miss_detector | blunder | 0.2066 | 0.707 | no | Re1 | Rg1 | +0.02 | +0.00 |
| 185173941140 | 27 | 14. Bb5+ | mistake | miss (tactic) | miss_detector | blunder | 0.2487 | 0.799 | no | Nxf7 | Nxf7 | +0.69 | +0.72 |
| 185193771738 | 35 | 18. Rd3 | mistake | miss (tactic) | miss_detector | mistake | 0.1108 | 0.751 | no | Nh4 | Nh4 | +1.83 | +1.94 |
| 185193771738 | 61 | 31. b5 | mistake | miss (tactic) | miss_detector | mistake | 0.1107 | 0.303 | no | Bh5 | Bh5 | -4.61 | -4.84 |
| 185277691132 | 111 | 56. Rb4 | mistake | miss (opportunity) | miss_detector | blunder | 0.2614 | 0.389 | no | Rc1 | Rc1 | -2.39 | -2.78 |
| 185363017994 | 99 | 50. Kd2 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1076 | 0.387 | no | Qa3 | Qa3 | -2.92 | -3.28 |
| 186429989523 | 27 | 14. Nxe4 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1039 | 0.626 | no | Qxe4 | Qxe4 | -0.06 | +0.12 |

### `mate_override` (15)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M5 |
| 185437323918 | 93 | 47. d7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0204 | 0.020 | no | Kc7 | - | -11.0 | -M11 |
| 185437323918 | 94 | 47... Qb2+ | excellent | good | mate_override | good | 0.0399 | 1.000 | no | Qa5 | - | -9.07 | -11.05 |
| 185437323918 | 100 | 50... Qb5+ | best | good | mate_override | good | 0.0237 | 1.000 | no | Qb6 | - | -10.7 | -13.62 |
| 185437323918 | 101 | 51. Ke6 | good | inaccuracy | mate_override | inaccuracy | 0.0194 | 0.019 | no | Kd4 | - | -M6 | -M8 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |
| 184678264914 | 54 | 27... Qxf3 | inaccuracy | miss (mate) | mate_override | mistake | 0.1844 | 1.000 | no | Re5 | Re6 | -4.60 | -4.76 |
| 184678264914 | 61 | 31. Qe3 | good | inaccuracy | mate_override | inaccuracy | 0.0669 | 0.067 | no | Qb2 | - | -8.92 | -M9 |
| 184794204922 | 38 | 19... Rc8 | good | inaccuracy | mate_override | inaccuracy | 0.0426 | 0.043 | no | Ra7 | - | M6 | M6 |
| 185117573448 | 64 | 32... Qc1 | miss | good | mate_override | good | 0.0000 | 1.000 | no | g5 | Qf2 | -9.30 | -M6 |
| 185117573448 | 68 | 34... Qxc3 | miss | good | mate_override | good | 0.0000 | 1.000 | no | Qf2 | Qf2 | -8.94 | -M6 |
| 185193771738 | 83 | 42. h3 | inaccuracy | miss (mate) | mate_override | excellent | 0.0000 | 0.000 | no | Ke1 | Ke1 | -M8 | -13.71 |
| 186411389477 | 71 | 36. Rd7 | excellent | good | mate_override | good | 0.0027 | 1.000 | no | Re4 | - | +8.61 | +9.29 |
| 186411389477 | 75 | 38. Rxa5 | excellent | good | mate_override | good | 0.0002 | 1.000 | no | g5 | - | +8.90 | +13.81 |
| 186429989523 | 81 | 41. Kh2 | mistake | inaccuracy | mate_override | inaccuracy | 0.0204 | 0.020 | no | Kg1 | - | -7.28 | -M5 |

### `losing_material_hardened` (14)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 31 | 16. Nd2 | excellent | mistake | losing_material_hardened | excellent | 0.0047 | 0.151 | no | b4 | - | -6.16 | -6.32 |
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | excellent | 0.0000 | 0.027 | no | Kb6 | - | -8.94 | -9.39 |
| 185437323918 | 91 | 46. Kxb7 | excellent | mistake | losing_material_hardened | excellent | 0.0057 | 0.028 | no | c6 | - | -9.64 | -13.13 |
| 184732665836 | 50 | 25... Nxd4 | excellent | mistake | losing_material_hardened | good | 0.0248 | 0.170 | no | Qg8 | - | +5.08 | +5.87 |
| 184773009646 | 58 | 29... Rb7 | best | mistake | losing_material_hardened | excellent | 0.0050 | 0.160 | no | Rd7 | - | +6.25 | +6.40 |
| 185217478440 | 72 | 36... c2 | inaccuracy | mistake | losing_material_hardened | good | 0.0462 | 0.157 | no | Kg7 | - | +6.63 | +7.46 |
| 185218140778 | 60 | 30... Kd6 | good | mistake | losing_material_hardened | excellent | 0.0127 | 0.190 | no | d6 | - | +5.40 | +5.45 |
| 185617589205 | 58 | 29... Kg7 | excellent | mistake | losing_material_hardened | good | 0.0263 | 0.150 | no | Re8 | - | +2.86 | +3.13 |
| 185617589205 | 80 | 40... Qh5 | excellent | mistake | losing_material_hardened | excellent | 0.0072 | 0.030 | no | Bxe3 | - | +5.58 | +5.88 |
| 185617589205 | 108 | 54... Rxe3+ | inaccuracy | mistake | losing_material_hardened | excellent | 0.0147 | 0.015 | no | Ke6 | - | M17 | +16.49 |
| 185966191317 | 38 | 19... Ka5 | excellent | mistake | losing_material_hardened | good | 0.0206 | 0.037 | no | Nb4 | - | +6.44 | +7.23 |
| 186222389165 | 53 | 27. Qc1 | good | mistake | losing_material_hardened | excellent | 0.0074 | 0.094 | no | Qc3 | - | -3.60 | -4.06 |
| 186429989523 | 43 | 22. dxc5 | excellent | mistake | losing_material_hardened | good | 0.0248 | 0.122 | no | f4 | - | -3.23 | -3.50 |
| 186429989523 | 79 | 40. Rxh6 | excellent | mistake | losing_material_hardened | excellent | 0.0015 | 0.016 | no | Rc8 | - | -7.35 | -7.40 |

### `book` (12)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0179 | 0.451 | no | Qxd5 | - | +0.82 | +0.84 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0683 | 0.531 | no | d4 | Nxe5 | -0.62 | -0.52 |
| 185468614210 | 8 | 4... Nc6 | inaccuracy | book | book | inaccuracy | 0.0818 | 0.562 | no | Nxe4 | Nxe4 | +0.30 | +0.28 |
| 185217478440 | 6 | 3... h6 | good | book | book | good | 0.0347 | 0.483 | no | Bc5 | - | +0.74 | +0.75 |
| 185334658860 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0702 | 0.532 | no | d4 | Nxe5 | -0.62 | -0.52 |
| 185334658860 | 6 | 3... Nc6 | inaccuracy | book | book | inaccuracy | 0.0532 | 0.538 | no | Nxe4 | Nxe4 | +0.28 | +0.26 |
| 185461631884 | 7 | 4. Bc4 | excellent | book | book | good | 0.0244 | 0.554 | no | Nxd4 | - | +0.31 | +0.30 |
| 186411389477 | 6 | 3... Nc6 | mistake | book | book | mistake | 0.1549 | 0.416 | no | d6 | d6 | +1.57 | +1.63 |
| 186411389477 | 7 | 4. Nxc6 | great | book | book | best | 0.0000 | 0.739 | yes | Nxc6 | - | +1.57 | +1.66 |
| 186411389477 | 8 | 4... dxc6 | best | book | book | excellent | 0.0108 | 0.258 | no | bxc6 | - | +1.57 | +1.79 |
| 186411389477 | 9 | 5. d3 | excellent | book | book | best | 0.0000 | 0.758 | yes | d3 | - | +1.53 | +1.63 |
| 186411389477 | 10 | 5... Bc5 | good | book | book | excellent | 0.0157 | 0.261 | no | Qe7 | - | +1.84 | +1.74 |

### `great_find_event` (6)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.507 | yes | Bxe5 | - | +0.18 | -0.03 |
| 185438707002 | 50 | 25... Kb8 | best | great | great_find_event | best | 0.0000 | 0.239 | yes | Kb8 | - | +3.70 | +4.12 |
| 185438707002 | 84 | 42... Nxg3 | best | great | great_find_event | best | 0.0000 | 0.895 | yes | Nxg3 | - | -7.11 | -7.34 |
| 184678264914 | 49 | 25. Bxf4 | best | great | great_find_event | best | 0.0000 | 0.245 | yes | Bxf4 | - | -3.64 | -3.63 |
| 185218140778 | 25 | 13. Kh1 | best | great | great_find_event | best | 0.0000 | 0.553 | yes | Kh1 | - | +0.51 | +0.59 |
| 185328167888 | 41 | 21. Bxf6 | best | great | great_find_event | best | 0.0000 | 0.681 | yes | Bxf6 | - | +2.79 | +2.78 |

### `blunder_softened` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 41 | 21. c4 | blunder | mistake | blunder_softened | blunder | 0.2194 | 0.751 | no | Bxe6 | - | +0.61 | +0.46 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | blunder_softened | blunder | 0.2031 | 0.698 | no | Rhxe7 | Rhxe7 | -0.08 | -0.08 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2519 | 0.577 | no | Qxg3+ | Qxg3+ | +2.48 | +2.57 |

