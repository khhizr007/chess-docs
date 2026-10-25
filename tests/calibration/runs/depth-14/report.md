# Calibration report: depth-14

- Generated: 2026-10-18T07:35:04+00:00
- Commit: `2703019df381` + uncommitted backend changes (diff sha256 `fa559f3352d9`)
- Engine: Stockfish 17.1; depth 14, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 66.5% (569/856) |
| Within one step | 87.7% (751/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.60 / 0.12 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 0.58 |
| Accuracy mean abs. difference | 3.04 (n=28, max 8.42) |
| Accuracy bias (ours - app) | +2.65 |
| Best move = app's suggestion | 73.7% (101/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | 1 | . | . | . | . | . | . | 3 |
| **great** | . | **3** | 22 | 1 | . | . | . | . | . | . | 26 |
| **best** | . | 2 | **253** | 51 | 8 | . | 1 | 1 | . | . | 316 |
| **excellent** | . | . | 27 | **77** | 18 | 1 | 2 | 1 | 1 | . | 127 |
| **good** | . | . | 8 | 33 | **50** | . | 10 | 1 | 1 | . | 103 |
| **book** | . | . | 8 | 6 | 4 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 5 | 6 | 19 | 1 | **56** | 4 | 1 | . | 92 |
| **mistake** | . | . | . | 1 | 1 | . | 13 | **25** | 1 | 3 | 44 |
| **miss** | . | . | . | . | 1 | . | 6 | 5 | **12** | 3 | 27 |
| **blunder** | . | . | . | . | . | . | . | 4 | 4 | **13** | 21 |
| **total** | 1 | 5 | 324 | 176 | 101 | 81 | 88 | 41 | 20 | 19 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 5 | 3 | 0.600 | 0.115 | 0.194 |
| best | 316 | 324 | 253 | 0.781 | 0.801 | 0.791 |
| excellent | 127 | 176 | 77 | 0.438 | 0.606 | 0.508 |
| good | 103 | 101 | 50 | 0.495 | 0.485 | 0.490 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 88 | 56 | 0.636 | 0.609 | 0.622 |
| mistake | 44 | 41 | 25 | 0.610 | 0.568 | 0.588 |
| miss | 27 | 20 | 12 | 0.600 | 0.444 | 0.511 |
| blunder | 21 | 19 | 13 | 0.684 | 0.619 | 0.650 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.8 | +6.1 |
| 1034847688 | black | 65.0 | 73.4 | +8.4 |
| 1041474766 | white | 98.0 | 97.2 | -0.8 |
| 1041474766 | black | 83.8 | 83.7 | -0.1 |
| 184759554082 | white | 81.2 | 85.9 | +4.7 |
| 184759554082 | black | 87.7 | 90.1 | +2.4 |
| 185209623352 | white | 72.7 | 72.1 | -0.6 |
| 185209623352 | black | 72.6 | 73.7 | +1.1 |
| 185324357184 | white | 73.0 | 76.4 | +3.4 |
| 185324357184 | black | 62.4 | 67.2 | +4.8 |
| 185436488062 | white | 98.6 | 98.1 | -0.5 |
| 185436488062 | black | 38.5 | 42.3 | +3.8 |
| 185437323918 | white | 69.5 | 71.7 | +2.2 |
| 185437323918 | black | 75.7 | 74.1 | -1.6 |
| 185438343298 | white | 46.9 | 47.4 | +0.5 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 75.8 | -2.0 |
| 185438707002 | black | 83.0 | 84.5 | +1.5 |
| 185456088510 | white | 78.4 | 85.1 | +6.7 |
| 185456088510 | black | 82.2 | 85.7 | +3.5 |
| 185468039834 | white | 80.0 | 82.7 | +2.7 |
| 185468039834 | black | 87.5 | 88.4 | +0.9 |
| 185468614210 | white | 70.8 | 76.4 | +5.6 |
| 185468614210 | black | 77.1 | 82.3 | +5.2 |
| 185475865432 | white | 78.1 | 83.0 | +4.9 |
| 185475865432 | black | 66.1 | 73.7 | +7.6 |
| 185962590893 | white | 90.8 | 92.7 | +1.9 |
| 185962590893 | black | 90.9 | 92.4 | +1.5 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 65.3% | 79.6% | reviewed | 23.8 |
| 1041474766 | 25 | 25 | 76.0% | 80.0% | reviewed | 13.8 |
| 184759554082 | 62 | 62 | 59.7% | 79.0% | reviewed | 24.0 |
| 185209623352 | 155 | 155 | 57.4% | 88.4% | reviewed | 20.8 |
| 185324357184 | 55 | 55 | 76.4% | 92.7% | reviewed | 11.6 |
| 185436488062 | 13 | 13 | 92.3% | 92.3% | reviewed | 3.0 |
| 185437323918 | 108 | 103 | 59.2% | 87.4% | reviewed | 8.6 |
| 185438343298 | 20 | 20 | 85.0% | 90.0% | reviewed | 3.0 |
| 185438707002 | 95 | 91 | 72.5% | 89.0% | reviewed | 19.1 |
| 185456088510 | 60 | 60 | 65.0% | 91.7% | reviewed | 17.1 |
| 185468039834 | 38 | 38 | 73.7% | 89.5% | reviewed | 11.1 |
| 185468614210 | 54 | 54 | 68.5% | 87.0% | reviewed | 12.1 |
| 185475865432 | 53 | 53 | 73.6% | 92.5% | reviewed | 11.6 |
| 185962590893 | 78 | 78 | 65.4% | 88.5% | reviewed | 11.6 |

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

## Mismatches by rule (287)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 268 | best -> excellent x51, good -> excellent x33, excellent -> best x27, great -> best x22, inaccuracy -> good x19, excellent -> good x17 |
| `miss_detector` | 7 | blunder -> miss x4, inaccuracy -> miss x1, mistake -> miss x1, excellent -> miss x1 |
| `mate_override` | 3 | best -> good x1, good -> miss x1, excellent -> good x1 |
| `losing_material_hardened` | 3 | good -> mistake x1, excellent -> mistake x1, inaccuracy -> mistake x1 |
| `blunder_softened` | 2 | miss -> mistake x2 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `great_find_event` | 2 | best -> great x2 |

### `precision` (268)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 9 | 5. c4 | inaccuracy | good | precision | good | 0.0375 | 0.492 | no | Be2 | Bd3 | -0.52 | -0.48 |
| 1034847688 | 10 | 5... O-O | excellent | best | precision | best | 0.0000 | 0.545 | no | e5 | - | -0.50 | -0.52 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0291 | 0.519 | no | a3 | - | +0.12 | -0.11 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0961 | 0.625 | no | cxb5 | cxb5 | +0.44 | +0.31 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.457 | yes | h6 | - | +0.90 | +0.40 |
| 1034847688 | 27 | 14. Ndf3 | mistake | inaccuracy | precision | inaccuracy | 0.0863 | 0.538 | no | Nge4 | h5 | -0.60 | -0.52 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0825 | 0.549 | no | bxc4 | Qd7 | +0.53 | +0.36 |
| 1034847688 | 30 | 15... Nh5 | miss | blunder | precision | blunder | 0.2696 | 0.630 | no | bxc4 | a4 | +1.64 | +1.52 |
| 1034847688 | 33 | 17. cxb5 | miss | blunder | precision | blunder | 0.2138 | 0.714 | no | h5 | h5 | 0.00 | +0.00 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.533 | yes | Nxf3 | - | -0.10 | -0.58 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.544 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.47 |
| 1034847688 | 44 | 22... Qxg5 | excellent | best | precision | best | 0.0000 | 0.456 | yes | Qxg5 | - | +0.46 | +0.52 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.549 | yes | exf7+ | - | +0.09 | +0.90 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.416 | yes | Kxf7 | Rxf7 | +0.92 | +0.91 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 0.971 | yes | Qe4+ | - | M8 | +9.16 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0308 | 0.574 | no | d4 | - | +0.37 | +0.48 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0018 | 0.457 | no | Nc6 | - | +0.38 | +0.55 |
| 1041474766 | 9 | 5. Bg2 | book | excellent | precision | excellent | 0.0044 | 0.549 | no | Nf3 | - | +0.34 | +0.40 |
| 1041474766 | 10 | 5... c6 | book | best | precision | best | 0.0000 | 0.464 | no | Nc6 | - | +0.59 | +0.40 |
| 1041474766 | 11 | 6. Nge2 | book | excellent | precision | excellent | 0.0080 | 0.536 | no | Nf3 | - | +0.17 | +0.31 |
| 1041474766 | 16 | 8... Bb4 | good | inaccuracy | precision | inaccuracy | 0.0695 | 0.476 | no | Be7 | - | +0.76 | +0.70 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0222 | 0.546 | no | d5 | - | +0.08 | -0.01 |
| 184759554082 | 9 | 5. h4 | inaccuracy | excellent | precision | excellent | 0.0175 | 0.533 | no | Nc3 | Be2 | -0.11 | +0.10 |
| 184759554082 | 10 | 5... Nf6 | best | excellent | precision | excellent | 0.0000 | 0.484 | no | Bg7 | - | -0.11 | +0.01 |
| 184759554082 | 12 | 6... Bg7 | good | inaccuracy | precision | inaccuracy | 0.0667 | 0.546 | no | d5 | - | 0.00 | +0.22 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0239 | 0.498 | no | Nxh5 | - | +0.03 | +0.17 |
| 184759554082 | 15 | 8. hxg6 | good | inaccuracy | precision | inaccuracy | 0.0509 | 0.527 | no | h6 | - | -0.21 | -0.15 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.524 | yes | hxg6 | - | -0.13 | +0.07 |
| 184759554082 | 17 | 9. Nf3 | good | inaccuracy | precision | inaccuracy | 0.0525 | 0.511 | no | Nc3 | - | -0.39 | -0.26 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0677 | 0.686 | no | d5 | d5 | -0.52 | -0.48 |
| 184759554082 | 21 | 11. Nc3 | best | good | precision | good | 0.0262 | 0.424 | no | d4 | - | -0.52 | -0.61 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.596 | yes | d5 | - | -0.52 | -0.70 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1239 | 0.390 | no | cxd5 | cxd5 | -1.98 | -1.59 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.729 | yes | Qxg5 | - | -1.98 | -1.82 |
| 184759554082 | 34 | 17... Qg5 | excellent | inaccuracy | precision | inaccuracy | 0.0671 | 0.707 | no | Bg4 | - | -0.88 | -0.90 |
| 184759554082 | 37 | 19. Kb1 | good | best | precision | best | 0.0000 | 0.337 | yes | Kb1 | - | -1.19 | -1.35 |
| 184759554082 | 38 | 19... Bf5 | excellent | inaccuracy | precision | inaccuracy | 0.0720 | 0.703 | no | Rh8 | - | -1.10 | -0.84 |
| 184759554082 | 40 | 20... Re6 | excellent | good | precision | good | 0.0278 | 0.720 | no | Bh3 | - | -1.31 | -1.30 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0109 | 0.314 | no | Rh1 | - | -1.28 | -1.26 |
| 184759554082 | 47 | 24. Ka1 | best | excellent | precision | excellent | 0.0066 | 0.300 | no | Rh1 | - | -1.28 | -1.30 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.696 | yes | a5 | - | -1.16 | -1.47 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0026 | 0.282 | no | Rh1 | f3 | -1.61 | -1.66 |
| 184759554082 | 55 | 28. Rh1 | inaccuracy | good | precision | good | 0.0380 | 0.293 | no | Rc2 | Rg1 | -1.76 | -1.68 |
| 184759554082 | 56 | 28... Ree8 | good | excellent | precision | excellent | 0.0061 | 0.745 | no | Rxh1 | - | -1.61 | -1.60 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0422 | 0.548 | no | dxc6 | - | -0.08 | +0.11 |
| 185209623352 | 7 | 4. d4 | best | excellent | precision | excellent | 0.0023 | 0.508 | no | Nf3 | - | -0.08 | +0.11 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.502 | yes | Nf3 | - | -0.16 | -0.03 |
| 185209623352 | 11 | 6. Bb5 | excellent | good | precision | good | 0.0226 | 0.512 | no | h3 | - | 0.00 | -0.19 |
| 185209623352 | 15 | 8. Bf4 | best | excellent | precision | excellent | 0.0077 | 0.581 | no | Ba4 | - | +1.28 | +1.37 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.766 | yes | Nxe4 | - | +5.09 | +5.30 |
| 185209623352 | 20 | 10... dxe4 | mistake | excellent | precision | excellent | 0.0080 | 0.232 | no | Bxe4 | - | +6.16 | +5.69 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0717 | 0.783 | no | Nxc6 | Nxc6 | +4.00 | +4.20 |
| 185209623352 | 22 | 11... Qxd4 | excellent | best | precision | best | 0.0000 | 0.279 | yes | Qxd4 | - | +4.04 | +4.08 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0093 | 0.715 | no | Bxc6 | - | +4.04 | +3.88 |
| 185209623352 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0084 | 0.294 | no | Rxd4 | - | +4.04 | +4.20 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0475 | 0.331 | no | e5 | - | +4.18 | +4.11 |
| 185209623352 | 29 | 15. Nf7 | excellent | best | precision | best | 0.0000 | 0.665 | no | O-O-O | - | +2.76 | +2.84 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.282 | yes | Kc7 | - | +4.76 | +4.82 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1657 | 0.716 | no | Bxe6 | - | +0.61 | +0.90 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.667 | yes | Rc5+ | - | +3.32 | +2.91 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.561 | yes | Nxd3 | Rxd3 | -0.61 | -0.44 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0078 | 0.290 | no | Ka6 | - | +3.97 | +4.02 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0134 | 0.721 | no | Rd5 | - | +3.97 | +4.07 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0009 | 0.285 | no | Bc3 | - | +4.48 | +4.26 |
| 185209623352 | 56 | 28... d2 | excellent | good | precision | good | 0.0373 | 0.304 | no | e5 | - | +4.65 | +4.48 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0135 | 0.734 | no | Rh5 | - | +4.14 | +4.18 |
| 185209623352 | 60 | 30... Bg5 | best | excellent | precision | excellent | 0.0028 | 0.231 | no | Bf4 | - | +5.17 | +5.45 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0442 | 0.303 | no | Kf5 | - | +4.38 | +3.93 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.709 | yes | Kc2 | - | +4.38 | +4.08 |
| 185209623352 | 71 | 36. Rh6 | good | excellent | precision | excellent | 0.0156 | 0.737 | no | Ke3 | - | +4.11 | +4.20 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0341 | 0.674 | no | Kd3 | - | +2.98 | +2.83 |
| 185209623352 | 77 | 39. Kb1 | inaccuracy | good | precision | good | 0.0348 | 0.646 | no | Rd2 | g4 | +1.67 | +2.00 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.640 | yes | Kc1 | - | +2.15 | +2.28 |
| 185209623352 | 81 | 41. Re1+ | inaccuracy | good | precision | good | 0.0351 | 0.776 | no | Rxf6+ | Rxf6+ | +4.65 | +4.43 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0750 | 0.269 | no | Kd5 | - | +6.01 | +6.31 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1490 | 0.643 | no | Rhxe7 | Rhxe7 | -0.08 | -0.11 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1842 | 0.500 | no | Kg5 | - | +3.73 | +3.42 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.684 | yes | Rf1+ | - | +3.73 | +3.29 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.758 | yes | Kxb2 | - | +5.17 | +4.87 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0088 | 0.209 | no | Bg5 | - | +6.38 | +6.13 |
| 185209623352 | 99 | 50. Rh7 | best | excellent | precision | excellent | 0.0015 | 0.800 | no | Rhh4 | - | +6.38 | +5.79 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0068 | 0.806 | no | Rc7 | - | +6.33 | +6.25 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0042 | 0.196 | no | Bg5 | - | +6.33 | +6.28 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.805 | yes | R7xb5 | - | +6.30 | +6.23 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0110 | 0.818 | no | Kd3 | - | +6.59 | +6.32 |
| 185209623352 | 108 | 54... Kh5 | excellent | best | precision | best | 0.0000 | 0.193 | yes | Kh5 | - | +6.70 | +6.29 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0080 | 0.813 | no | Kd3 | - | +6.54 | +6.28 |
| 185209623352 | 112 | 56... Bxe5 | excellent | best | precision | best | 0.0000 | 0.195 | no | Bg7 | - | +6.75 | +6.06 |
| 185209623352 | 114 | 57... Kf6 | excellent | good | precision | good | 0.0330 | 0.199 | no | Kh6 | - | +7.19 | +7.13 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0071 | 0.176 | no | Ke7 | Ke7 | +10.6 | +8.75 |
| 185209623352 | 117 | 59. h5 | good | best | precision | best | 0.0000 | 0.878 | no | Rg8 | - | +8.42 | +6.77 |
| 185209623352 | 119 | 60. h6 | best | excellent | precision | excellent | 0.0085 | 0.878 | no | Kc3 | - | M9 | +8.51 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0074 | 0.888 | no | Rg8 | - | M8 | +8.73 |
| 185209623352 | 123 | 62. Rg8 | best | excellent | precision | excellent | 0.0043 | 0.873 | no | Rh4 | - | M7 | +9.13 |
| 185209623352 | 125 | 63. h7 | best | excellent | precision | excellent | 0.0007 | 0.886 | no | Kd2 | - | M5 | M9 |
| 185209623352 | 127 | 64. h8=Q | best | good | precision | good | 0.0427 | 0.927 | no | Kd2 | - | M4 | +8.99 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 141 | 71. g4 | good | excellent | precision | excellent | 0.0062 | 0.849 | no | Kb2 | - | +10.4 | +10.29 |
| 185209623352 | 142 | 71... Kb5 | good | excellent | precision | excellent | 0.0000 | 0.089 | no | Kb7 | - | M8 | +9.33 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 0.892 | yes | g5 | - | M9 | M9 |
| 185209623352 | 145 | 73. g6 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kb2 | - | M5 | M7 |
| 185209623352 | 147 | 74. g7 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kd1 | - | M4 | M5 |
| 185209623352 | 153 | 77. Qc7 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qc7 | - | M3 | M6 |
| 185324357184 | 6 | 3... Bc5 | blunder | mistake | precision | mistake | 0.1949 | 0.513 | no | d5 | - | +3.27 | +3.33 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | excellent | precision | excellent | 0.0133 | 0.591 | no | Ng3 | Ng3 | -0.98 | -1.22 |
| 185324357184 | 19 | 10. Ne2 | good | excellent | precision | excellent | 0.0017 | 0.431 | no | Qd4 | - | -1.32 | -1.25 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0630 | 0.571 | no | Na6 | - | +0.29 | +0.21 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.512 | yes | Qg1 | - | +0.29 | +0.02 |
| 185324357184 | 31 | 16. g3 | inaccuracy | good | precision | good | 0.0365 | 0.500 | no | Kd1 | Kd1 | -0.97 | -0.80 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | precision | mistake | 0.1843 | 0.546 | no | Qxg3+ | Qxg3+ | +2.48 | +2.49 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.673 | yes | Re1 | - | +3.07 | +3.29 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0263 | 0.320 | no | Qh5 | - | +3.38 | +3.86 |
| 185324357184 | 40 | 20... Be4 | inaccuracy | good | precision | good | 0.0365 | 0.300 | no | Qxg3 | Qxg3 | +4.45 | +4.63 |
| 185324357184 | 45 | 23. Re7 | best | excellent | precision | excellent | 0.0040 | 0.525 | no | Re3 | - | +0.19 | +0.37 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0103 | 0.522 | no | b3 | - | +0.26 | +0.20 |
| 185324357184 | 52 | 26... a5 | good | excellent | precision | excellent | 0.0040 | 0.522 | no | h5 | - | -0.29 | -0.29 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.606 | yes | Nxe5 | - | +1.74 | +1.84 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0853 | 0.287 | no | d3 | d3 | -5.55 | -5.91 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0177 | 0.801 | no | c6 | - | -5.16 | -5.35 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0342 | 0.794 | no | g4 | - | -4.94 | -4.95 |
| 185437323918 | 23 | 12. Qg3 | mistake | inaccuracy | precision | inaccuracy | 0.0500 | 0.231 | no | Qe3 | - | -6.88 | -6.98 |
| 185437323918 | 28 | 14... g6 | good | excellent | precision | excellent | 0.0064 | 0.817 | no | Kg8 | - | -6.13 | -6.23 |
| 185437323918 | 31 | 16. Nd2 | excellent | best | precision | best | 0.0000 | 0.192 | yes | Nd2 | - | -6.16 | -6.03 |
| 185437323918 | 33 | 17. bxc3 | good | excellent | precision | excellent | 0.0130 | 0.214 | no | g4 | - | -6.58 | -5.91 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0000 | 0.799 | no | Kg8 | - | -6.58 | -5.92 |
| 185437323918 | 35 | 18. Bb2 | mistake | blunder | precision | blunder | 0.2010 | 0.201 | no | Nf3 | - | -M2 | -M2 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.779 | no | Qe2 | - | -5.96 | -5.51 |
| 185437323918 | 42 | 21... gxf3 | brilliant | excellent | precision | excellent | 0.0195 | 0.724 | no | Qf4 | - | -3.59 | -3.85 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0878 | 0.290 | no | hxg3 | hxg3 | -5.85 | -5.91 |
| 185437323918 | 50 | 25... Kg7 | excellent | best | precision | best | 0.0000 | 0.776 | yes | Kg7 | - | -4.71 | -4.95 |
| 185437323918 | 54 | 27... a6 | inaccuracy | mistake | precision | mistake | 0.1069 | 0.762 | no | e4 | e4 | -2.64 | -2.75 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0255 | 0.661 | no | Bc2 | - | -2.41 | -2.20 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.791 | yes | Be4 | - | -5.61 | -5.65 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0115 | 0.808 | no | Rf8 | - | -6.21 | -5.85 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | good | precision | good | 0.0442 | 0.250 | no | Kg2 | Kg2 | -6.13 | -5.50 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0476 | 0.783 | no | e4 | e4 | -5.01 | -4.38 |
| 185437323918 | 71 | 36. Kg3 | excellent | best | precision | best | 0.0000 | 0.231 | yes | Kg3 | - | -5.97 | -5.75 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.231 | yes | Kf3 | - | -6.12 | -5.70 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0126 | 0.791 | no | e4+ | - | -6.12 | -5.38 |
| 185437323918 | 76 | 38... Rf4+ | best | good | precision | good | 0.0220 | 0.784 | no | Bc3 | - | -6.12 | -5.26 |
| 185437323918 | 80 | 40... Kxg4 | best | excellent | precision | excellent | 0.0004 | 0.785 | no | Kg5 | - | -6.12 | -5.70 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0128 | 0.209 | no | Ke4 | - | -7.11 | -6.55 |
| 185437323918 | 82 | 41... a5 | best | excellent | precision | excellent | 0.0105 | 0.822 | no | Bb4 | - | -7.11 | -6.66 |
| 185437323918 | 84 | 42... a4 | best | good | precision | good | 0.0405 | 0.838 | no | Bg3 | - | -7.28 | -7.52 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.148 | yes | Kxc7 | - | -8.05 | -6.74 |
| 185437323918 | 87 | 44. d6 | excellent | good | precision | good | 0.0205 | 0.146 | no | Kxb7 | - | -8.99 | -7.54 |
| 185437323918 | 88 | 44... Bg3 | excellent | good | precision | good | 0.0270 | 0.853 | no | a2 | - | -8.13 | -6.97 |
| 185437323918 | 91 | 46. Kxb7 | excellent | best | precision | best | 0.0000 | 0.127 | yes | Kxb7 | - | -9.64 | -7.85 |
| 185437323918 | 94 | 47... Qb2+ | excellent | best | precision | best | 0.0000 | 0.876 | yes | Qb2+ | - | -9.07 | -9.89 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.091 | yes | Kc6 | Ka6 | -M17 | -8.54 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0073 | 0.880 | no | Qf6+ | - | -M16 | -10.73 |
| 185437323918 | 98 | 49... Qb7+ | good | excellent | precision | excellent | 0.0041 | 0.876 | no | Qg8+ | - | -8.99 | -8.21 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0081 | 0.875 | no | Qb6 | - | -10.7 | -8.03 |
| 185437323918 | 101 | 51. Ke6 | good | best | precision | best | 0.0000 | 0.133 | yes | Ke6 | - | -M6 | -9.74 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2120 | 0.212 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | good | precision | good | 0.0314 | 0.512 | no | Nf3 | - | -0.01 | -0.32 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.519 | yes | h6 | - | -0.01 | -0.21 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.488 | yes | Bh4 | - | -0.01 | -0.20 |
| 185438707002 | 19 | 10. Nf3 | excellent | best | precision | best | 0.0000 | 0.483 | yes | Nf3 | - | -0.52 | -0.36 |
| 185438707002 | 20 | 10... Be6 | inaccuracy | good | precision | good | 0.0468 | 0.521 | no | Nh7 | g4 | +0.37 | +0.43 |
| 185438707002 | 26 | 13... O-O-O | miss | inaccuracy | precision | inaccuracy | 0.0881 | 0.635 | no | Rg8 | Rg8 | -0.69 | -0.63 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.575 | yes | c3 | - | +1.35 | +1.50 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0843 | 0.412 | no | Bb6 | - | +2.65 | +3.03 |
| 185438707002 | 40 | 20... Rxh8 | best | excellent | precision | excellent | 0.0032 | 0.263 | no | e5 | - | +3.97 | +4.32 |
| 185438707002 | 42 | 21... Nb6 | good | excellent | precision | excellent | 0.0066 | 0.279 | no | Ne5 | - | +3.99 | +4.15 |
| 185438707002 | 46 | 23... e5 | best | excellent | precision | excellent | 0.0034 | 0.282 | no | Rf8 | - | +3.82 | +3.97 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0097 | 0.719 | no | Rd2 | - | +3.82 | +3.49 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | excellent | precision | excellent | 0.0128 | 0.745 | no | Rhd1 | Qf6 | +3.70 | +4.03 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0025 | 0.704 | no | Qf3 | - | +3.78 | +3.78 |
| 185438707002 | 54 | 27... Rf8 | mistake | inaccuracy | precision | inaccuracy | 0.0884 | 0.290 | no | Re8 | Rh7 | +5.73 | +5.81 |
| 185438707002 | 55 | 28. Rd8+ | miss | inaccuracy | precision | inaccuracy | 0.0855 | 0.799 | no | Qxf8+ | Qxf8+ | +3.74 | +4.02 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.706 | yes | Qxd8+ | - | +3.69 | +3.57 |
| 185438707002 | 59 | 30. Qxh4 | excellent | good | precision | good | 0.0215 | 0.720 | no | Qd2 | - | +3.68 | +3.55 |
| 185438707002 | 63 | 32. b4 | good | excellent | precision | excellent | 0.0133 | 0.633 | no | Rd2 | - | +1.87 | +1.64 |
| 185438707002 | 68 | 34... Qb2+ | great | excellent | precision | excellent | 0.0056 | 0.690 | no | Qa2+ | - | -3.65 | -3.31 |
| 185438707002 | 75 | 38. Kg1 | best | good | precision | good | 0.0203 | 0.306 | no | Qg4 | - | -3.38 | -3.60 |
| 185438707002 | 76 | 38... Qd1+ | good | inaccuracy | precision | inaccuracy | 0.0530 | 0.701 | no | b6 | - | -2.61 | -2.91 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0033 | 0.867 | no | e4 | - | -8.73 | -7.80 |
| 185438707002 | 91 | 46. Kh4 | best | mistake | precision | mistake | 0.1378 | 0.138 | no | c4 | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | good | precision | good | 0.0490 | 0.395 | no | e6 | e6 | +1.09 | +1.00 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0102 | 0.654 | no | Nf3 | - | +0.96 | +0.95 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0056 | 0.325 | no | d5 | - | +1.01 | +1.24 |
| 185456088510 | 9 | 5. Nc3 | excellent | good | precision | good | 0.0266 | 0.688 | no | c4 | - | +0.95 | +1.12 |
| 185456088510 | 10 | 5... g6 | good | excellent | precision | excellent | 0.0028 | 0.329 | no | Nd7 | - | +1.14 | +1.03 |
| 185456088510 | 11 | 6. h4 | good | excellent | precision | excellent | 0.0072 | 0.658 | no | Bf4 | - | +0.95 | +0.98 |
| 185456088510 | 13 | 7. a4 | inaccuracy | mistake | precision | mistake | 0.1013 | 0.708 | no | Be3 | Qe2 | +0.87 | +0.68 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0029 | 0.645 | no | d5 | - | +0.81 | +0.92 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0159 | 0.358 | no | Bg7 | - | +0.81 | +0.90 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.648 | yes | Ng3 | - | +0.65 | +0.66 |
| 185456088510 | 22 | 11... Bg7 | inaccuracy | good | precision | good | 0.0365 | 0.374 | no | h5 | h5 | +1.10 | +1.06 |
| 185456088510 | 23 | 12. c3 | inaccuracy | good | precision | good | 0.0440 | 0.663 | no | h5 | h5 | +0.70 | +0.80 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.678 | yes | h5 | - | +1.12 | +1.24 |
| 185456088510 | 29 | 15. e5 | inaccuracy | good | precision | good | 0.0352 | 0.795 | no | Nh4 | Qe2 | +1.58 | +1.46 |
| 185456088510 | 34 | 17... Qe7 | miss | blunder | precision | blunder | 0.2638 | 0.448 | no | Bxe4 | Bxe4 | +1.83 | +2.34 |
| 185456088510 | 42 | 21... Bxa6 | best | excellent | precision | excellent | 0.0129 | 0.168 | no | h5 | - | +2.36 | +2.38 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0651 | 0.188 | no | g5 | - | +2.89 | +2.73 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0000 | 0.851 | no | a5 | - | +2.89 | +3.15 |
| 185456088510 | 48 | 24... Qc7 | excellent | best | precision | best | 0.0000 | 0.119 | yes | Qc7 | - | +3.01 | +3.04 |
| 185456088510 | 52 | 26... Rxd1+ | good | excellent | precision | excellent | 0.0180 | 0.204 | no | Nxe3 | - | +2.14 | +2.30 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.909 | yes | Nxe3 | - | -4.25 | -3.88 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0006 | 0.460 | no | Na4 | - | -0.94 | -0.83 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0111 | 0.492 | no | Ne5 | - | +0.60 | +0.40 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0323 | 0.472 | no | Kf8 | - | +0.61 | +1.05 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | excellent | precision | excellent | 0.0068 | 0.427 | no | dxe5 | dxe5 | +1.53 | +1.71 |
| 185468039834 | 22 | 11... Be6 | good | inaccuracy | precision | inaccuracy | 0.0696 | 0.442 | no | Rh7 | - | +1.84 | +2.24 |
| 185468039834 | 25 | 13. Nf6+ | good | best | precision | best | 0.0000 | 0.430 | yes | Nf6+ | - | -1.28 | -1.02 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.718 | yes | Rf8 | - | -3.36 | -3.38 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0062 | 0.287 | no | bxc5 | - | -3.39 | -4.12 |
| 185468039834 | 36 | 18... a5 | good | inaccuracy | precision | inaccuracy | 0.0555 | 0.698 | no | Rf7 | - | -2.75 | -2.52 |
| 185468614210 | 6 | 3... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0985 | 0.519 | no | Nxe4 | Nxe4 | +1.50 | +1.37 |
| 185468614210 | 9 | 5. d4 | book | best | precision | best | 0.0000 | 0.515 | yes | d4 | - | +0.15 | +0.20 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.488 | yes | exd4 | - | +0.15 | +0.21 |
| 185468614210 | 11 | 6. cxd4 | book | excellent | precision | excellent | 0.0035 | 0.512 | no | e5 | - | 0.00 | -0.10 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.506 | yes | Bb4+ | - | 0.00 | +0.10 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0169 | 0.506 | no | Bd2 | - | -0.35 | -0.46 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0387 | 0.469 | no | Nxe4 | Nxe4 | +1.21 | +1.28 |
| 185468614210 | 18 | 9... Ne7 | excellent | best | precision | best | 0.0000 | 0.421 | yes | Ne7 | - | +1.36 | +1.54 |
| 185468614210 | 25 | 13. Bd3 | good | excellent | precision | excellent | 0.0076 | 0.479 | no | Bxd6 | - | -0.61 | -0.62 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0401 | 0.489 | no | Kg8 | Kg8 | +1.21 | +0.87 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0366 | 0.551 | no | Qh5+ | Qh5+ | +0.18 | +0.21 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.488 | yes | Kg8 | - | +0.18 | +0.30 |
| 185468614210 | 42 | 21... b6 | best | excellent | precision | excellent | 0.0088 | 0.501 | no | Rad8 | - | +0.14 | +0.15 |
| 185468614210 | 44 | 22... Rc6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Rc6 | - | +0.08 | +0.19 |
| 185468614210 | 47 | 24. Qxa7 | best | excellent | precision | excellent | 0.0058 | 0.504 | no | Qe7 | - | +0.14 | +0.09 |
| 185468614210 | 48 | 24... Rxc3 | best | excellent | precision | excellent | 0.0006 | 0.495 | no | Rd2 | - | +0.14 | +0.23 |
| 185475865432 | 3 | 2. Nf3 | book | good | precision | good | 0.0237 | 0.553 | no | d4 | - | +0.74 | +0.63 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.463 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.537 | yes | Nc3 | - | +0.74 | +0.63 |
| 185475865432 | 6 | 3... e6 | book | excellent | precision | excellent | 0.0058 | 0.463 | no | Nf6 | - | +0.74 | +0.65 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0064 | 0.465 | no | d5 | - | +0.55 | +0.71 |
| 185475865432 | 11 | 6. Bb3 | inaccuracy | good | precision | good | 0.0290 | 0.541 | no | Bd3 | - | -0.37 | +0.10 |
| 185475865432 | 17 | 9. d5 | good | excellent | precision | excellent | 0.0191 | 0.540 | no | e5 | - | +0.31 | +0.36 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0028 | 0.576 | no | c4 | - | +0.82 | +0.96 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0888 | 0.553 | no | Nf4 | Ng3 | -0.76 | -0.62 |
| 185475865432 | 23 | 12. Bf4 | inaccuracy | good | precision | good | 0.0488 | 0.470 | no | e5 | - | -1.49 | -1.37 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0000 | 0.410 | no | Re1 | - | -1.49 | -1.53 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0134 | 0.608 | no | Bd6 | - | -1.25 | -1.59 |
| 185475865432 | 46 | 23... Ba6 | good | excellent | precision | excellent | 0.0170 | 0.424 | no | Be5 | - | +1.85 | +1.62 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0767 | 0.677 | no | Rxe6 | Rxe6 | +1.47 | +1.74 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0549 | 0.629 | no | Bc4 | - | +0.50 | +0.47 |
| 185962590893 | 10 | 5... Bg4 | good | inaccuracy | precision | inaccuracy | 0.0593 | 0.426 | no | e5 | - | +0.80 | +0.86 |
| 185962590893 | 12 | 6... Bxf3 | excellent | best | precision | best | 0.0000 | 0.398 | yes | Bxf3 | - | +0.82 | +0.72 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.407 | yes | e5 | - | +0.67 | +0.44 |
| 185962590893 | 19 | 10. Bd2 | good | excellent | precision | excellent | 0.0125 | 0.570 | no | Bg5 | - | +0.50 | +0.42 |
| 185962590893 | 23 | 12. Ne3 | inaccuracy | mistake | precision | mistake | 0.1003 | 0.653 | no | Ba5 | Ba5 | +0.66 | +0.61 |
| 185962590893 | 24 | 12... O-O | best | excellent | precision | excellent | 0.0031 | 0.404 | no | Nc5 | - | +0.66 | +0.50 |
| 185962590893 | 27 | 14. Nxe7+ | miss | good | precision | good | 0.0411 | 0.725 | no | Bh6 | Bh6 | +1.01 | +1.45 |
| 185962590893 | 35 | 18. g5 | best | inaccuracy | precision | inaccuracy | 0.0783 | 0.671 | no | Rxd7 | - | +0.96 | +0.86 |
| 185962590893 | 37 | 19. Rxd1 | best | excellent | precision | excellent | 0.0015 | 0.601 | no | Bxd1 | - | +0.96 | +1.11 |
| 185962590893 | 40 | 20... Nfd7 | best | excellent | precision | excellent | 0.0014 | 0.337 | no | Ne8 | - | +0.96 | +1.01 |
| 185962590893 | 43 | 22. Bd2 | good | excellent | precision | excellent | 0.0175 | 0.653 | no | Qe2 | - | +0.86 | +0.87 |
| 185962590893 | 44 | 22... Ne6 | excellent | best | precision | best | 0.0000 | 0.365 | yes | Ne6 | - | +0.92 | +0.82 |
| 185962590893 | 45 | 23. Qd3 | good | excellent | precision | excellent | 0.0015 | 0.628 | no | Qc3 | - | +0.71 | +0.78 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0134 | 0.378 | no | Nd7 | - | +0.86 | +0.87 |
| 185962590893 | 48 | 24... Nd7 | best | good | precision | good | 0.0380 | 0.375 | no | h6 | - | +0.86 | +0.91 |
| 185962590893 | 49 | 25. Bg4 | excellent | good | precision | good | 0.0208 | 0.641 | no | Be3 | - | +0.82 | +0.77 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.622 | yes | Qe3 | Qf3 | +0.47 | +0.74 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0816 | 0.384 | no | Nf4 | Nf4 | +1.15 | +1.23 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2498 | 0.686 | no | f4 | - | -0.39 | -0.40 |
| 185962590893 | 55 | 28. Kb2 | mistake | inaccuracy | precision | inaccuracy | 0.0878 | 0.437 | no | Kb1 | Kd1 | -1.21 | -1.29 |
| 185962590893 | 56 | 28... Nxd2 | miss | mistake | precision | mistake | 0.1787 | 0.695 | no | Na5 | Na5 | -0.23 | -0.19 |
| 185962590893 | 59 | 30. Bxe6 | great | best | precision | best | 0.0000 | 0.467 | yes | Bxe6 | - | -0.23 | -0.16 |
| 185962590893 | 61 | 31. f4 | best | excellent | precision | excellent | 0.0159 | 0.484 | no | h5 | - | -0.23 | -0.13 |
| 185962590893 | 62 | 31... exf4 | good | excellent | precision | excellent | 0.0159 | 0.521 | no | b4 | - | -0.08 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | -0.13 |
| 185962590893 | 78 | 39... Qd1+ | best | good | precision | good | 0.0207 | 0.521 | no | g6 | - | 0.00 | +0.00 |

### `miss_detector` (7)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (tactic) | miss_detector | mistake | 0.1316 | 0.639 | no | g4 | - | -0.01 | +0.06 |
| 184759554082 | 27 | 14. cxd5 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1135 | 0.239 | no | Bb2 | Bb2 | -3.24 | -3.05 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1666 | 0.806 | no | Rxf6+ | Rxf6+ | +2.74 | +2.54 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.3880 | 0.762 | no | Rxf6+ | - | -2.81 | -2.27 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2123 | 0.729 | no | Kg7 | - | -0.17 | -0.29 |
| 185437323918 | 107 | 54. Ke8 | excellent | miss (opportunity) | miss_detector | mistake | 0.1408 | 0.141 | no | Kf6 | - | -M1 | -M1 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2495 | 0.250 | no | Kd2 | - | -M1 | -M1 |

### `mate_override` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 129 | 65. Qh6+ | best | good | mate_override | good | 0.0000 | 1.000 | no | Rg5 | - | M3 | M6 |
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M7 |
| 185209623352 | 151 | 76. Qd8+ | excellent | good | mate_override | good | 0.0000 | 1.000 | no | Qe6+ | - | M3 | M5 |

### `losing_material_hardened` (3)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 59 | 30. g5+ | good | mistake | losing_material_hardened | good | 0.0202 | 0.211 | no | Rf1 | - | -6.55 | -6.19 |
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | good | 0.0271 | 0.165 | no | Kxb7 | - | -8.94 | -7.17 |
| 185438707002 | 89 | 45. g3 | inaccuracy | mistake | losing_material_hardened | excellent | 0.0177 | 0.142 | no | Kh4 | g5 | -M7 | -8.17 |

### `blunder_softened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2366 | 0.875 | no | Qxg2 | Qxg2 | -0.96 | -1.33 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | blunder_softened | blunder | 0.2043 | 0.628 | no | Nxc7+ | Nxc7+ | -0.91 | -1.33 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0107 | 0.470 | no | Nf6 | - | +0.82 | +0.86 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | good | 0.0420 | 0.523 | no | Nxe5 | Nxe5 | -0.62 | -0.33 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.519 | yes | Bxe5 | - | +0.18 | +0.49 |
| 185438343298 | 15 | 8. g3 | best | great | great_find_event | best | 0.0000 | 0.225 | yes | g3 | - | -5.11 | -5.49 |

