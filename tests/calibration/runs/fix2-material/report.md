# Calibration report: fix2-material

- Generated: 2026-10-17T19:21:22+00:00
- Commit: `c76a4ce061d2` + uncommitted backend changes (diff sha256 `b2072ef94854`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 68.0% (582/856) |
| Within one step | 88.7% (759/856) |
| Brilliant precision / recall | 0.50 / 0.33 |
| Great precision / recall | 0.67 / 0.15 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.23 |
| Great per 100 moves (app / ours) | 3.04 / 0.70 |
| Accuracy mean abs. difference | 3.16 (n=28, max 9.10) |
| Accuracy bias (ours - app) | +3.03 |
| Best move = app's suggestion | 78.1% (107/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | 1 | . | . | . | . | . | 3 |
| **great** | . | **4** | 22 | . | . | . | . | . | . | . | 26 |
| **best** | 1 | 2 | **272** | 34 | 7 | . | . | . | . | . | 316 |
| **excellent** | . | . | 38 | **68** | 18 | 1 | 1 | 1 | . | . | 127 |
| **good** | . | . | 6 | 33 | **55** | . | 8 | . | 1 | . | 103 |
| **book** | . | . | 9 | 6 | 3 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 5 | 5 | 22 | 1 | **54** | 4 | 1 | . | 92 |
| **mistake** | . | . | . | 2 | 2 | . | 12 | **24** | 3 | 1 | 44 |
| **miss** | . | . | . | . | 1 | . | 3 | 5 | **16** | 2 | 27 |
| **blunder** | . | . | . | . | . | . | . | 7 | 5 | **9** | 21 |
| **total** | 2 | 6 | 353 | 148 | 109 | 81 | 78 | 41 | 26 | 12 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 2 | 1 | 0.500 | 0.333 | 0.400 |
| great | 26 | 6 | 4 | 0.667 | 0.154 | 0.250 |
| best | 316 | 353 | 272 | 0.771 | 0.861 | 0.813 |
| excellent | 127 | 148 | 68 | 0.459 | 0.535 | 0.495 |
| good | 103 | 109 | 55 | 0.505 | 0.534 | 0.519 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 78 | 54 | 0.692 | 0.587 | 0.635 |
| mistake | 44 | 41 | 24 | 0.585 | 0.545 | 0.565 |
| miss | 27 | 26 | 16 | 0.615 | 0.593 | 0.604 |
| blunder | 21 | 12 | 9 | 0.750 | 0.429 | 0.545 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 82.0 | +8.3 |
| 1034847688 | black | 65.0 | 74.1 | +9.1 |
| 1041474766 | white | 98.0 | 97.4 | -0.6 |
| 1041474766 | black | 83.8 | 86.1 | +2.3 |
| 184759554082 | white | 81.2 | 86.6 | +5.4 |
| 184759554082 | black | 87.7 | 90.3 | +2.6 |
| 185209623352 | white | 72.7 | 75.4 | +2.7 |
| 185209623352 | black | 72.6 | 74.4 | +1.8 |
| 185324357184 | white | 73.0 | 74.4 | +1.4 |
| 185324357184 | black | 62.4 | 65.9 | +3.5 |
| 185436488062 | white | 98.6 | 98.4 | -0.2 |
| 185436488062 | black | 38.5 | 41.1 | +2.6 |
| 185437323918 | white | 69.5 | 73.7 | +4.2 |
| 185437323918 | black | 75.7 | 75.8 | +0.1 |
| 185438343298 | white | 46.9 | 47.1 | +0.2 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 76.9 | -0.9 |
| 185438707002 | black | 83.0 | 84.8 | +1.8 |
| 185456088510 | white | 78.4 | 82.1 | +3.7 |
| 185456088510 | black | 82.2 | 84.0 | +1.8 |
| 185468039834 | white | 80.0 | 85.5 | +5.5 |
| 185468039834 | black | 87.5 | 90.4 | +2.9 |
| 185468614210 | white | 70.8 | 74.8 | +4.0 |
| 185468614210 | black | 77.1 | 82.0 | +4.9 |
| 185475865432 | white | 78.1 | 84.2 | +6.1 |
| 185475865432 | black | 66.1 | 72.8 | +6.7 |
| 185962590893 | white | 90.8 | 92.0 | +1.2 |
| 185962590893 | black | 90.9 | 94.8 | +3.9 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 57.1% | 81.6% | reviewed | 74.9 |
| 1041474766 | 25 | 25 | 76.0% | 80.0% | reviewed | 36.3 |
| 184759554082 | 62 | 62 | 71.0% | 88.7% | reviewed | 75.0 |
| 185209623352 | 155 | 155 | 60.0% | 88.4% | reviewed | 88.0 |
| 185324357184 | 55 | 55 | 80.0% | 90.9% | reviewed | 55.9 |
| 185436488062 | 13 | 13 | 92.3% | 92.3% | reviewed | 8.5 |
| 185437323918 | 108 | 103 | 57.3% | 86.4% | reviewed | 47.3 |
| 185438343298 | 20 | 20 | 80.0% | 85.0% | reviewed | 7.0 |
| 185438707002 | 95 | 91 | 73.6% | 93.4% | reviewed | 96.9 |
| 185456088510 | 60 | 60 | 68.3% | 90.0% | reviewed | 73.8 |
| 185468039834 | 38 | 38 | 76.3% | 94.7% | reviewed | 55.2 |
| 185468614210 | 54 | 54 | 74.1% | 87.0% | reviewed | 51.8 |
| 185475865432 | 53 | 53 | 67.9% | 88.7% | reviewed | 54.2 |
| 185962590893 | 78 | 78 | 69.2% | 89.7% | reviewed | 47.2 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label equals the collector's guess for 0 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | best | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | best | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | good | mate_override |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (274)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 250 | excellent -> best x38, best -> excellent x34, good -> excellent x33, inaccuracy -> good x22, great -> best x22, excellent -> good x18 |
| `miss_detector` | 9 | blunder -> miss x5, mistake -> miss x3, inaccuracy -> miss x1 |
| `mate_override` | 5 | good -> miss x1, good -> inaccuracy x1, best -> good x1, excellent -> inaccuracy x1, excellent -> mistake x1 |
| `blunder_softened` | 5 | blunder -> mistake x4, miss -> mistake x1 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `great_find_event` | 2 | best -> great x2 |
| `brilliant_event` | 1 | best -> brilliant x1 |

### `precision` (250)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 4 | 2... Nf6 | excellent | best | precision | best | 0.0000 | 0.481 | yes | Nf6 | - | +0.33 | +0.32 |
| 1034847688 | 9 | 5. c4 | inaccuracy | good | precision | good | 0.0478 | 0.500 | no | Bd3 | Bd3 | -0.52 | -0.51 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0103 | 0.490 | no | Be2 | - | -0.10 | -0.23 |
| 1034847688 | 17 | 9. Qc2 | excellent | best | precision | best | 0.0000 | 0.520 | yes | Qc2 | - | +0.12 | +0.18 |
| 1034847688 | 18 | 9... b5 | good | excellent | precision | excellent | 0.0094 | 0.483 | no | a5 | - | +0.38 | +0.28 |
| 1034847688 | 19 | 10. h4 | good | excellent | precision | excellent | 0.0197 | 0.526 | no | Bd3 | - | +0.11 | +0.07 |
| 1034847688 | 20 | 10... Bg4 | inaccuracy | good | precision | good | 0.0431 | 0.493 | no | Na6 | Bf5 | +0.64 | +0.53 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0673 | 0.622 | no | cxb5 | cxb5 | +0.44 | +0.36 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.464 | yes | h6 | - | +0.90 | +0.45 |
| 1034847688 | 28 | 14... Nbd7 | miss | good | precision | good | 0.0241 | 0.575 | no | a4 | Qd7 | +0.53 | +0.27 |
| 1034847688 | 30 | 15... Nh5 | miss | blunder | precision | blunder | 0.2887 | 0.642 | no | bxc4 | a4 | +1.64 | +1.61 |
| 1034847688 | 37 | 19. Rh4 | mistake | inaccuracy | precision | inaccuracy | 0.0992 | 0.572 | no | Rh6 | Rh6 | -0.10 | -0.29 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.527 | yes | Nxf3 | - | -0.10 | -0.34 |
| 1034847688 | 40 | 20... Nf5 | inaccuracy | good | precision | good | 0.0403 | 0.540 | no | Qe8 | f5 | +0.50 | +0.00 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.523 | yes | dxe6 | - | +0.30 | +0.00 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0357 | 0.500 | no | fxe6 | - | +0.46 | +0.76 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.571 | yes | exf7+ | - | +0.09 | +0.97 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.410 | yes | Kxf7 | Rxf7 | +0.92 | +1.73 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M13 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0248 | 0.560 | no | Nf3 | - | +0.37 | +0.40 |
| 1041474766 | 8 | 4... Nf6 | book | best | precision | best | 0.0000 | 0.464 | yes | Nf6 | - | +0.38 | +0.59 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.552 | yes | Bg2 | - | +0.34 | +0.40 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0027 | 0.464 | no | e5 | - | +0.59 | +0.43 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0205 | 0.538 | no | Nf3 | - | +0.17 | +0.20 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.532 | yes | O-O | - | +0.28 | +0.34 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0413 | 0.535 | no | d5 | - | +0.08 | +0.04 |
| 184759554082 | 9 | 5. h4 | inaccuracy | good | precision | good | 0.0381 | 0.548 | no | Nc3 | Be2 | -0.11 | +0.06 |
| 184759554082 | 12 | 6... Bg7 | good | inaccuracy | precision | inaccuracy | 0.0524 | 0.549 | no | d5 | - | 0.00 | +0.02 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0382 | 0.530 | no | Nxh5 | - | +0.03 | +0.05 |
| 184759554082 | 15 | 8. hxg6 | good | excellent | precision | excellent | 0.0032 | 0.508 | no | Nc3 | - | -0.21 | -0.17 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.527 | yes | hxg6 | - | -0.13 | -0.14 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0980 | 0.688 | no | d5 | d5 | -0.52 | -0.49 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.604 | yes | d5 | - | -0.52 | -0.59 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1268 | 0.407 | no | cxd5 | cxd5 | -1.98 | -2.23 |
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | precision | mistake | 0.1985 | 0.857 | no | Qxg2 | Qxg2 | -0.96 | -1.21 |
| 184759554082 | 32 | 16... b6 | best | good | precision | good | 0.0343 | 0.677 | no | b5 | - | -0.96 | -1.09 |
| 184759554082 | 36 | 18... Qf6 | best | excellent | precision | excellent | 0.0043 | 0.658 | no | Re5 | - | -1.01 | -1.18 |
| 184759554082 | 37 | 19. Kb1 | good | excellent | precision | excellent | 0.0096 | 0.320 | no | Qb2 | - | -1.19 | -1.19 |
| 184759554082 | 38 | 19... Bf5 | excellent | good | precision | good | 0.0488 | 0.681 | no | Re5 | - | -1.10 | -0.85 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.709 | yes | Re6 | - | -1.31 | -1.38 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.722 | yes | a5 | - | -1.16 | -1.63 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0037 | 0.261 | no | f3 | f3 | -1.61 | -1.56 |
| 184759554082 | 57 | 29. Ka2 | good | excellent | precision | excellent | 0.0133 | 0.263 | no | Rhe1 | - | -1.73 | -1.88 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0445 | 0.547 | no | dxc6 | - | -0.08 | +0.04 |
| 185209623352 | 8 | 4... Nc6 | best | excellent | precision | excellent | 0.0011 | 0.498 | no | a6 | - | -0.08 | -0.05 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.497 | yes | Nf3 | - | -0.16 | -0.17 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.794 | yes | Nxe4 | - | +5.09 | +6.11 |
| 185209623352 | 20 | 10... dxe4 | mistake | excellent | precision | excellent | 0.0018 | 0.201 | no | Bxe4 | - | +6.16 | +5.81 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0721 | 0.788 | no | Nxc6 | Nxc6 | +4.00 | +4.30 |
| 185209623352 | 23 | 12. Qxd4 | best | good | precision | good | 0.0270 | 0.745 | no | Bxc6 | - | +4.04 | +4.38 |
| 185209623352 | 24 | 12... Nxd4 | best | excellent | precision | excellent | 0.0027 | 0.271 | no | Rxd4 | - | +4.04 | +4.39 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0333 | 0.730 | no | O-O-O | O-O-O | +3.00 | +3.54 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0404 | 0.310 | no | e5 | - | +4.18 | +4.41 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.257 | yes | Kc7 | - | +4.76 | +4.73 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0453 | 0.744 | no | Nd8 | Nd8 | +3.29 | +3.73 |
| 185209623352 | 40 | 20... Rd8 | inaccuracy | good | precision | good | 0.0355 | 0.317 | no | a6 | - | +3.82 | +4.14 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1832 | 0.718 | no | Bxe6 | - | +0.61 | +0.62 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.669 | yes | Rc5+ | - | +3.32 | +3.30 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.461 | yes | Nd3+ | - | +0.92 | +1.24 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.570 | yes | Nxd3 | Rxd3 | -0.61 | +1.32 |
| 185209623352 | 49 | 25. Rb5+ | excellent | best | precision | best | 0.0000 | 0.710 | yes | Rb5+ | - | +3.97 | +4.25 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0005 | 0.277 | no | Ka6 | - | +3.97 | +4.31 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0058 | 0.272 | no | Bc3 | - | +4.48 | +4.48 |
| 185209623352 | 56 | 28... d2 | excellent | best | precision | best | 0.0000 | 0.263 | yes | d2 | - | +4.65 | +4.70 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0035 | 0.743 | no | Kc3 | - | +4.14 | +4.49 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0053 | 0.768 | no | Rh5 | - | +4.64 | +5.17 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0334 | 0.767 | no | Rh5 | - | +4.51 | +4.54 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0243 | 0.295 | no | Kf5 | - | +4.38 | +4.53 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.736 | yes | Kc2 | - | +4.38 | +4.35 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0444 | 0.677 | no | Kd3 | - | +2.98 | +2.83 |
| 185209623352 | 77 | 39. Kb1 | inaccuracy | good | precision | good | 0.0415 | 0.640 | no | g4 | g4 | +1.67 | +1.77 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.632 | yes | Kc1 | - | +2.15 | +2.26 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0552 | 0.261 | no | Kd5 | - | +6.01 | +5.98 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1497 | 0.653 | no | Rhxe7 | Rhxe7 | -0.08 | -0.09 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1792 | 0.500 | no | Kf7 | - | +3.73 | +3.57 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.691 | yes | Rf1+ | - | +3.73 | +3.41 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.765 | yes | Kxb2 | - | +5.17 | +5.61 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0050 | 0.220 | no | Bxf4 | - | +5.65 | +5.74 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0153 | 0.210 | no | b5 | - | +6.38 | +6.28 |
| 185209623352 | 99 | 50. Rh7 | best | excellent | precision | excellent | 0.0032 | 0.805 | no | g4 | - | +6.38 | +6.28 |
| 185209623352 | 102 | 51... Kg6 | excellent | best | precision | best | 0.0000 | 0.188 | no | Bd8 | - | +6.33 | +6.61 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0044 | 0.188 | no | Bd8 | - | +6.33 | +6.55 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.815 | no | Kd3 | - | +6.30 | +6.57 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0000 | 0.822 | no | Rb6 | - | +6.59 | +6.95 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0003 | 0.822 | no | Rb6 | - | +6.54 | +6.76 |
| 185209623352 | 112 | 56... Bxe5 | excellent | best | precision | best | 0.0000 | 0.178 | yes | Bxe5 | - | +6.75 | +6.63 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.124 | yes | Kf6 | - | +7.19 | +12.76 |
| 185209623352 | 115 | 58. Rg5 | excellent | good | precision | good | 0.0304 | 0.947 | no | Re4 | - | +7.03 | +10.61 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0090 | 0.083 | no | Kf7 | Ke7 | +10.6 | M17 |
| 185209623352 | 117 | 59. h5 | good | best | precision | best | 0.0000 | 1.000 | yes | h5 | - | +8.42 | M14 |
| 185209623352 | 118 | 59... Kf7 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | Kf6 | Kf6 | M10 | M12 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | M10 |
| 185209623352 | 123 | 62. Rg8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rh4 | - | M7 | M10 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kf5 | - | M5 | M6 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kc3 | - | M3 | M6 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M7 |
| 185209623352 | 144 | 72... Ka5 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kb6 | - | M6 | M7 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ka6 | - | M5 | M5 |
| 185209623352 | 153 | 77. Qc7 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qc7 | - | M3 | M3 |
| 185324357184 | 7 | 4. h3 | miss | blunder | precision | blunder | 0.2487 | 0.690 | no | fxe5 | fxe5 | -1.29 | -1.03 |
| 185324357184 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0034 | 0.559 | no | Nc6 | - | -1.29 | -1.02 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0311 | 0.599 | no | Ng3 | Ng3 | -0.98 | -0.74 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0772 | 0.577 | no | Na6 | - | +0.29 | +0.08 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.505 | yes | Qg1 | - | +0.29 | +0.14 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.673 | yes | Re1 | - | +3.07 | +2.90 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0232 | 0.340 | no | Qh5 | - | +3.38 | +3.47 |
| 185324357184 | 39 | 20. Rf1 | great | best | precision | best | 0.0000 | 0.689 | yes | Rf1 | - | +3.38 | +3.63 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.502 | no | b3 | - | +0.26 | +0.22 |
| 185324357184 | 52 | 26... a5 | good | excellent | precision | excellent | 0.0171 | 0.538 | no | h6 | - | -0.29 | -0.36 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.611 | yes | Nxe5 | - | +1.74 | +1.96 |
| 185437323918 | 10 | 5... Kf8 | good | excellent | precision | excellent | 0.0149 | 0.441 | no | Ke7 | - | +1.39 | +1.47 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0313 | 0.316 | no | b4 | - | -3.51 | -3.95 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0823 | 0.287 | no | d4 | d3 | -5.55 | -5.83 |
| 185437323918 | 17 | 9. Qd3 | excellent | best | precision | best | 0.0000 | 0.207 | yes | Qd3 | - | -5.63 | -5.91 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0038 | 0.799 | no | Qe8 | - | -5.16 | -6.01 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0358 | 0.796 | no | Qe8 | - | -4.94 | -5.16 |
| 185437323918 | 23 | 12. Qg3 | mistake | inaccuracy | precision | inaccuracy | 0.0751 | 0.242 | no | Qe3 | - | -6.88 | -6.90 |
| 185437323918 | 26 | 13... Nxg3+ | excellent | best | precision | best | 0.0000 | 0.850 | yes | Nxg3+ | - | -6.67 | -7.23 |
| 185437323918 | 30 | 15... exd4 | best | excellent | precision | excellent | 0.0056 | 0.802 | no | Kg7 | - | -6.13 | -6.03 |
| 185437323918 | 33 | 17. bxc3 | good | excellent | precision | excellent | 0.0025 | 0.185 | no | Nf3 | - | -6.58 | -6.40 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0170 | 0.816 | no | Kg7 | - | -6.58 | -6.53 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0291 | 0.749 | no | Qf4 | - | -3.59 | -3.39 |
| 185437323918 | 51 | 26. a5 | excellent | best | precision | best | 0.0000 | 0.224 | yes | a5 | - | -4.88 | -5.24 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0172 | 0.772 | no | b6 | - | -4.41 | -4.83 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0327 | 0.681 | no | Bc2 | - | -2.41 | -2.59 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.799 | yes | Be4 | - | -5.61 | -6.35 |
| 185437323918 | 59 | 30. g5+ | good | excellent | precision | excellent | 0.0123 | 0.185 | no | Rg3 | - | -6.55 | -6.58 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0000 | 0.827 | no | Rf8 | - | -6.21 | -6.81 |
| 185437323918 | 64 | 32... Kxg5 | good | excellent | precision | excellent | 0.0197 | 0.811 | no | e4 | - | -5.64 | -5.81 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0030 | 0.799 | no | Kf4 | - | -5.11 | -5.83 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | excellent | precision | excellent | 0.0011 | 0.204 | no | Kg2 | Kg2 | -6.13 | -5.86 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | excellent | precision | excellent | 0.0175 | 0.797 | no | e4 | e4 | -5.01 | -5.41 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.205 | yes | Kf3 | - | -6.12 | -6.17 |
| 185437323918 | 74 | 37... Rf8+ | best | good | precision | good | 0.0226 | 0.808 | no | a5 | - | -6.12 | -5.57 |
| 185437323918 | 80 | 40... Kxg4 | best | excellent | precision | excellent | 0.0007 | 0.830 | no | Kh4 | - | -6.12 | -6.95 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0155 | 0.165 | no | c5 | - | -7.11 | -7.50 |
| 185437323918 | 84 | 42... a4 | best | good | precision | good | 0.0232 | 0.870 | no | Bg3 | - | -7.28 | -9.23 |
| 185437323918 | 85 | 43. Kxc7 | good | excellent | precision | excellent | 0.0000 | 0.104 | no | Ke6 | - | -8.05 | -8.78 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0058 | 0.886 | no | Bg3+ | - | -8.05 | -9.22 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.104 | yes | d6 | - | -8.99 | -9.13 |
| 185437323918 | 89 | 45. c5 | excellent | good | precision | good | 0.0257 | 0.105 | no | Kd7 | - | -8.94 | -9.02 |
| 185437323918 | 91 | 46. Kxb7 | excellent | good | precision | good | 0.0257 | 0.076 | no | Kc8 | - | -9.64 | -11.00 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.040 | yes | Kc6 | Ka6 | -M17 | -M18 |
| 185437323918 | 97 | 49. Kd5 | best | excellent | precision | excellent | 0.0065 | 0.044 | no | d8=N | - | -M16 | -M22 |
| 185437323918 | 101 | 51. Ke6 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd4 | - | -M6 | -M16 |
| 185437323918 | 105 | 53. Ke7 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kf8 | - | -M3 | -M13 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2187 | 0.219 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0095 | 0.507 | no | a4 | - | -0.01 | -0.05 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.503 | yes | h6 | - | -0.01 | +0.02 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.501 | yes | Bh4 | - | -0.01 | -0.08 |
| 185438707002 | 12 | 6... g5 | good | excellent | precision | excellent | 0.0172 | 0.505 | no | Na5 | - | +0.33 | +0.21 |
| 185438707002 | 26 | 13... O-O-O | miss | inaccuracy | precision | inaccuracy | 0.0862 | 0.627 | no | Rg8 | Rg8 | -0.69 | -0.57 |
| 185438707002 | 28 | 14... Nd4 | inaccuracy | mistake | precision | mistake | 0.1028 | 0.538 | no | Rhg8 | Rhg8 | +0.82 | +1.09 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.583 | yes | c3 | - | +1.35 | +1.43 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0714 | 0.416 | no | Bb6 | - | +2.65 | +2.48 |
| 185438707002 | 42 | 21... Nb6 | good | excellent | precision | excellent | 0.0122 | 0.295 | no | a5 | - | +3.99 | +3.93 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.719 | yes | Rxd4 | - | +3.82 | +4.01 |
| 185438707002 | 47 | 24. Rd3 | best | excellent | precision | excellent | 0.0140 | 0.724 | no | Rd2 | - | +3.82 | +3.49 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0689 | 0.304 | no | a6 | - | +4.87 | +4.97 |
| 185438707002 | 51 | 26. Rhd1 | excellent | best | precision | best | 0.0000 | 0.709 | yes | Rhd1 | - | +3.49 | +3.85 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0033 | 0.721 | no | Qg5 | - | +3.78 | +3.63 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.728 | yes | Qxd8+ | - | +3.69 | +3.95 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | good | precision | good | 0.0344 | 0.364 | no | c6 | Qb3 | +2.60 | +3.00 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.725 | yes | Qb2+ | - | -3.65 | -4.10 |
| 185438707002 | 74 | 37... Qxd5 | excellent | best | precision | best | 0.0000 | 0.730 | yes | Qxd5 | - | -3.38 | -3.81 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0372 | 0.679 | no | Qe2 | - | -2.36 | -2.45 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0000 | 0.881 | no | e4 | - | -8.73 | -9.03 |
| 185438707002 | 89 | 45. g3 | inaccuracy | mistake | precision | mistake | 0.1046 | 0.105 | no | g5 | g5 | -M7 | -M9 |
| 185438707002 | 91 | 46. Kh4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | g5 | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0569 | 0.407 | no | e6 | e6 | +1.09 | +0.97 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0015 | 0.650 | no | Nc3 | - | +0.96 | +0.93 |
| 185456088510 | 6 | 3... e6 | excellent | good | precision | good | 0.0244 | 0.356 | no | d6 | - | +1.01 | +1.02 |
| 185456088510 | 7 | 4. Nf3 | best | excellent | precision | excellent | 0.0043 | 0.657 | no | Nc3 | - | +1.01 | +1.17 |
| 185456088510 | 11 | 6. h4 | good | inaccuracy | precision | inaccuracy | 0.0557 | 0.688 | no | h3 | - | +0.95 | +0.85 |
| 185456088510 | 13 | 7. a4 | inaccuracy | mistake | precision | mistake | 0.1098 | 0.712 | no | Bf4 | Qe2 | +0.87 | +0.65 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0105 | 0.629 | no | d5 | - | +0.81 | +0.79 |
| 185456088510 | 18 | 9... Ngf6 | best | excellent | precision | excellent | 0.0015 | 0.401 | no | Bg7 | - | +0.65 | +0.66 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.604 | yes | Ng3 | - | +0.65 | +0.71 |
| 185456088510 | 22 | 11... Bg7 | inaccuracy | good | precision | good | 0.0375 | 0.366 | no | h5 | h5 | +1.10 | +1.12 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.666 | yes | h5 | - | +1.12 | +1.22 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.758 | yes | exd6 | - | +1.55 | +1.81 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0492 | 0.816 | no | Nh4 | - | +1.72 | +2.03 |
| 185456088510 | 42 | 21... Bxa6 | best | excellent | precision | excellent | 0.0134 | 0.162 | no | Qd5 | - | +2.36 | +2.54 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0729 | 0.154 | no | Rd6 | - | +2.89 | +3.82 |
| 185456088510 | 47 | 24. b4 | best | good | precision | good | 0.0234 | 0.919 | no | a5 | - | +2.89 | +3.38 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.917 | yes | Nxe3 | - | -4.25 | -4.85 |
| 185456088510 | 57 | 29. Nd4 | mistake | excellent | precision | excellent | 0.0071 | 0.044 | no | Qb5 | - | -4.77 | -5.14 |
| 185468039834 | 9 | 5. d4 | inaccuracy | good | precision | good | 0.0465 | 0.509 | no | d3 | d3 | -0.94 | -0.64 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0116 | 0.487 | no | Ne5 | - | +0.60 | +0.35 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0409 | 0.473 | no | Kf8 | - | +0.61 | +1.18 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0205 | 0.435 | no | dxe5 | dxe5 | +1.53 | +1.65 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.595 | yes | Qh5 | - | +1.48 | +1.62 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1814 | 0.617 | no | Nxc7+ | Nxc7+ | -0.91 | -1.11 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.564 | yes | c6 | - | -0.83 | -1.14 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0131 | 0.434 | no | b4 | - | -1.28 | -1.44 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.700 | yes | Rf8 | - | -3.36 | -3.48 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0053 | 0.509 | no | d3 | - | +0.15 | +0.08 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.495 | yes | exd4 | - | +0.15 | +0.00 |
| 185468614210 | 11 | 6. cxd4 | book | best | precision | best | 0.0000 | 0.500 | yes | cxd4 | - | 0.00 | +0.03 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.498 | yes | Bb4+ | - | 0.00 | +0.08 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0053 | 0.505 | no | Bd2 | - | -0.35 | -0.41 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0455 | 0.467 | no | Nxe4 | Nxe4 | +1.21 | +1.25 |
| 185468614210 | 18 | 9... Ne7 | excellent | good | precision | good | 0.0210 | 0.432 | no | Na5 | - | +1.36 | +1.68 |
| 185468614210 | 31 | 16. Qxd5 | best | excellent | precision | excellent | 0.0012 | 0.512 | no | Ng5+ | - | +0.25 | +0.21 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0372 | 0.488 | no | Kg8 | Kg8 | +1.21 | +0.85 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0407 | 0.549 | no | Qh5+ | Qh5+ | +0.18 | +0.21 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.488 | yes | Kg8 | - | +0.18 | +0.25 |
| 185468614210 | 47 | 24. Qxa7 | best | excellent | precision | excellent | 0.0023 | 0.500 | no | Re8+ | - | +0.14 | +0.00 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0098 | 0.548 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.460 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.537 | yes | Nc3 | - | +0.74 | +0.75 |
| 185475865432 | 6 | 3... e6 | book | excellent | precision | excellent | 0.0017 | 0.456 | no | c5 | - | +0.74 | +0.67 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0069 | 0.466 | no | Bb4 | - | +0.55 | +0.87 |
| 185475865432 | 17 | 9. d5 | good | excellent | precision | excellent | 0.0186 | 0.535 | no | e5 | - | +0.31 | +0.29 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0149 | 0.568 | no | e5 | - | +0.82 | +1.01 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0917 | 0.557 | no | Ng3 | Ng3 | -0.76 | -0.60 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0107 | 0.415 | no | Ng3 | - | -1.49 | -1.74 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0422 | 0.627 | no | Qxd1 | Qxd1 | -1.24 | -1.47 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0191 | 0.415 | no | hxg3 | - | -1.52 | -1.61 |
| 185475865432 | 32 | 16... Bf6 | good | best | precision | best | 0.0000 | 0.600 | yes | Bf6 | - | -1.25 | -1.38 |
| 185475865432 | 33 | 17. Qxd8+ | good | excellent | precision | excellent | 0.0192 | 0.420 | no | Re1 | - | -1.78 | -1.73 |
| 185475865432 | 42 | 21... Bxb2 | best | excellent | precision | excellent | 0.0062 | 0.408 | no | Rb8 | - | +1.50 | +1.65 |
| 185475865432 | 49 | 25. a6 | mistake | good | precision | good | 0.0497 | 0.683 | no | Rxe6 | Rxe6 | +1.47 | +2.34 |
| 185475865432 | 50 | 25... Bh5 | mistake | inaccuracy | precision | inaccuracy | 0.0956 | 0.367 | no | Be5 | - | +3.93 | +4.24 |
| 185475865432 | 51 | 26. a7 | excellent | best | precision | best | 0.0000 | 0.729 | yes | a7 | - | +3.79 | +4.08 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0722 | 0.628 | no | Bc4 | - | +0.50 | +0.35 |
| 185962590893 | 12 | 6... Bxf3 | excellent | best | precision | best | 0.0000 | 0.393 | yes | Bxf3 | - | +0.82 | +0.76 |
| 185962590893 | 15 | 8. Nc4 | inaccuracy | good | precision | good | 0.0306 | 0.616 | no | a4 | - | +0.40 | +0.54 |
| 185962590893 | 16 | 8... Ngf6 | inaccuracy | good | precision | good | 0.0410 | 0.415 | no | b5 | b5 | +0.82 | +0.79 |
| 185962590893 | 17 | 9. Bf4 | good | inaccuracy | precision | inaccuracy | 0.0583 | 0.623 | no | a4 | - | +0.67 | +0.52 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.418 | yes | e5 | - | +0.67 | +0.53 |
| 185962590893 | 19 | 10. Bd2 | good | best | precision | best | 0.0000 | 0.584 | yes | Bd2 | - | +0.50 | +0.37 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.441 | yes | Be7 | - | +0.55 | +0.43 |
| 185962590893 | 21 | 11. O-O-O | excellent | best | precision | best | 0.0000 | 0.568 | yes | O-O-O | - | +0.44 | +0.33 |
| 185962590893 | 22 | 11... b5 | inaccuracy | mistake | precision | mistake | 0.1341 | 0.448 | no | O-O | O-O | +0.92 | +1.23 |
| 185962590893 | 24 | 12... O-O | best | excellent | precision | excellent | 0.0016 | 0.421 | no | Nc5 | - | +0.66 | +0.46 |
| 185962590893 | 25 | 13. Nf5 | excellent | best | precision | best | 0.0000 | 0.573 | yes | Nf5 | - | +0.64 | +0.61 |
| 185962590893 | 26 | 13... Rfe8 | mistake | inaccuracy | precision | inaccuracy | 0.0523 | 0.404 | no | Nc5 | Nc5 | +1.62 | +1.65 |
| 185962590893 | 27 | 14. Nxe7+ | miss | mistake | precision | mistake | 0.1015 | 0.741 | no | Bh6 | Bh6 | +1.01 | +1.40 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0328 | 0.307 | no | Ne8 | Ne8 | +1.62 | +1.53 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0734 | 0.726 | no | Rxd8+ | Rxd8+ | +0.96 | +0.99 |
| 185962590893 | 35 | 18. g5 | best | good | precision | good | 0.0491 | 0.677 | no | Rxd7 | - | +0.96 | +0.82 |
| 185962590893 | 45 | 23. Qd3 | good | inaccuracy | precision | inaccuracy | 0.0510 | 0.670 | no | Qc3 | - | +0.71 | +0.57 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.611 | yes | Qe3 | Qf3 | +0.47 | +0.84 |
| 185962590893 | 52 | 26... Nd4 | mistake | good | precision | good | 0.0248 | 0.369 | no | Nf4 | Nf4 | +1.15 | +1.09 |
| 185962590893 | 62 | 31... exf4 | good | excellent | precision | excellent | 0.0175 | 0.529 | no | Kf7 | - | -0.08 | +0.00 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | a6 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `miss_detector` (9)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1188 | 0.647 | no | g4 | - | -0.01 | -0.06 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1423 | 0.794 | no | Rxf6+ | Rxf6+ | +2.74 | +2.73 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.4409 | 0.769 | no | Rxf6+ | - | -2.81 | -3.18 |
| 185437323918 | 35 | 18. Bb2 | mistake | miss (tactic) | miss_detector | mistake | 0.1791 | 0.179 | no | Nf3 | - | -M2 | -M2 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2172 | 0.728 | no | Kg7 | - | -0.17 | -0.19 |
| 185438343298 | 13 | 7. Ke1 | blunder | miss (tactic) | miss_detector | blunder | 0.3193 | 0.525 | no | Ke3 | - | -5.11 | -5.75 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2319 | 0.232 | no | Kd2 | - | -M1 | -M1 |
| 185456088510 | 33 | 17. Ne4 | mistake | miss (tactic) | miss_detector | mistake | 0.1777 | 0.735 | no | Qe2 | Qe2 | +0.65 | +0.36 |
| 185962590893 | 23 | 12. Ne3 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1044 | 0.686 | no | Ba5 | Ba5 | +0.66 | +0.50 |

### `mate_override` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M6 |
| 185209623352 | 142 | 71... Kb5 | good | inaccuracy | mate_override | inaccuracy | 0.0803 | 0.080 | no | Kb7 | - | M8 | M8 |
| 185437323918 | 96 | 48... Qb8 | best | good | mate_override | good | 0.0443 | 1.000 | no | Qd4 | - | -M16 | -13.18 |
| 185437323918 | 99 | 50. c6 | excellent | inaccuracy | mate_override | inaccuracy | 0.0554 | 0.055 | no | Kd4 | - | -10.7 | -12.66 |
| 185437323918 | 107 | 54. Ke8 | excellent | mistake | mate_override | mistake | 0.0371 | 0.037 | no | Kf6 | - | -M1 | -M1 |

### `blunder_softened` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2196 | 0.571 | no | Qxg3+ | Qxg3+ | +2.48 | +2.68 |
| 185437323918 | 11 | 6. O-O | blunder | mistake | blunder_softened | blunder | 0.2822 | 0.585 | no | Bb3 | - | -3.21 | -3.58 |
| 185438707002 | 67 | 34. Kc2 | blunder | mistake | blunder_softened | blunder | 0.3766 | 0.671 | no | Kd1 | - | -3.65 | -4.08 |
| 185438707002 | 81 | 41. h5 | blunder | mistake | blunder_softened | blunder | 0.2369 | 0.382 | no | Qg4 | - | -7.11 | -7.46 |
| 185468614210 | 49 | 25. Re7 | blunder | mistake | blunder_softened | blunder | 0.2862 | 0.509 | no | Rab1 | - | -5.18 | -5.36 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0050 | 0.459 | no | Nf6 | - | +0.82 | +0.83 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | good | 0.0426 | 0.523 | no | Nxe5 | Nxe5 | -0.62 | -0.34 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.500 | yes | Bxe5 | - | +0.18 | +0.34 |
| 185438343298 | 15 | 8. g3 | best | great | great_find_event | best | 0.0000 | 0.214 | yes | g3 | - | -5.11 | -5.84 |

### `brilliant_event` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 76 | 38... Rf4+ | best | brilliant | brilliant_event | best | 0.0000 | 0.803 | yes | Rf4+ | - | -6.12 | -7.15 |

