# Calibration report: sf16.1-off0

- Generated: 2026-10-18T08:21:49+00:00
- Commit: `52ae25250d63` + uncommitted backend changes (diff sha256 `d19c6b081992`)
- Engine: Stockfish 16.1; depth 18, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 67.5% (578/856) |
| Within one step | 88.7% (759/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.60 / 0.12 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 0.58 |
| Accuracy mean abs. difference | 3.33 (n=28, max 7.49) |
| Accuracy bias (ours - app) | +3.21 |
| Best move = app's suggestion | 82.5% (113/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | 1 | . | . | . | . | . | 3 |
| **great** | . | **3** | 22 | 1 | . | . | . | . | . | . | 26 |
| **best** | . | 2 | **274** | 36 | 2 | . | 1 | . | 1 | . | 316 |
| **excellent** | . | . | 33 | **68** | 19 | 1 | 4 | 1 | 1 | . | 127 |
| **good** | . | . | 7 | 37 | **52** | . | 6 | . | 1 | . | 103 |
| **book** | . | . | 9 | 6 | 3 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 3 | 5 | 29 | 1 | **52** | 2 | . | . | 92 |
| **mistake** | . | . | . | 2 | 3 | . | 10 | **22** | 4 | 3 | 44 |
| **miss** | . | . | . | . | . | . | 5 | 4 | **16** | 2 | 27 |
| **blunder** | . | . | . | . | . | . | . | 6 | 4 | **11** | 21 |
| **total** | 1 | 5 | 349 | 155 | 109 | 81 | 78 | 35 | 27 | 16 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 5 | 3 | 0.600 | 0.115 | 0.194 |
| best | 316 | 349 | 274 | 0.785 | 0.867 | 0.824 |
| excellent | 127 | 155 | 68 | 0.439 | 0.535 | 0.482 |
| good | 103 | 109 | 52 | 0.477 | 0.505 | 0.491 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 78 | 52 | 0.667 | 0.565 | 0.612 |
| mistake | 44 | 35 | 22 | 0.629 | 0.500 | 0.557 |
| miss | 27 | 27 | 16 | 0.593 | 0.593 | 0.593 |
| blunder | 21 | 16 | 11 | 0.688 | 0.524 | 0.595 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.8 | +6.1 |
| 1034847688 | black | 65.0 | 70.6 | +5.6 |
| 1041474766 | white | 98.0 | 97.3 | -0.7 |
| 1041474766 | black | 83.8 | 85.4 | +1.6 |
| 184759554082 | white | 81.2 | 85.7 | +4.5 |
| 184759554082 | black | 87.7 | 91.2 | +3.5 |
| 185209623352 | white | 72.7 | 76.1 | +3.4 |
| 185209623352 | black | 72.6 | 74.0 | +1.4 |
| 185324357184 | white | 73.0 | 77.4 | +4.4 |
| 185324357184 | black | 62.4 | 68.4 | +6.0 |
| 185436488062 | white | 98.6 | 98.3 | -0.3 |
| 185436488062 | black | 38.5 | 44.5 | +6.0 |
| 185437323918 | white | 69.5 | 77.0 | +7.5 |
| 185437323918 | black | 75.7 | 76.6 | +0.9 |
| 185438343298 | white | 46.9 | 47.6 | +0.7 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 80.9 | +3.1 |
| 185438707002 | black | 83.0 | 82.4 | -0.6 |
| 185456088510 | white | 78.4 | 82.2 | +3.8 |
| 185456088510 | black | 82.2 | 84.8 | +2.6 |
| 185468039834 | white | 80.0 | 83.4 | +3.4 |
| 185468039834 | black | 87.5 | 89.1 | +1.6 |
| 185468614210 | white | 70.8 | 75.7 | +4.9 |
| 185468614210 | black | 77.1 | 81.4 | +4.3 |
| 185475865432 | white | 78.1 | 84.1 | +6.0 |
| 185475865432 | black | 66.1 | 72.9 | +6.8 |
| 185962590893 | white | 90.8 | 92.4 | +1.6 |
| 185962590893 | black | 90.9 | 93.0 | +2.1 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 67.3% | 87.8% | reviewed | 37.7 |
| 1041474766 | 25 | 25 | 80.0% | 80.0% | reviewed | 21.1 |
| 184759554082 | 62 | 62 | 62.9% | 90.3% | reviewed | 50.8 |
| 185209623352 | 155 | 155 | 56.1% | 87.1% | reviewed | 67.3 |
| 185324357184 | 55 | 55 | 74.5% | 90.9% | reviewed | 33.7 |
| 185436488062 | 13 | 13 | 92.3% | 92.3% | reviewed | 8.6 |
| 185437323918 | 108 | 103 | 57.3% | 87.4% | reviewed | 51.8 |
| 185438343298 | 20 | 20 | 85.0% | 90.0% | reviewed | 5.0 |
| 185438707002 | 95 | 91 | 67.0% | 89.0% | reviewed | 71.0 |
| 185456088510 | 60 | 60 | 65.0% | 90.0% | reviewed | 49.9 |
| 185468039834 | 38 | 38 | 76.3% | 89.5% | reviewed | 29.2 |
| 185468614210 | 54 | 54 | 79.6% | 85.2% | reviewed | 39.8 |
| 185475865432 | 53 | 53 | 67.9% | 92.5% | reviewed | 46.8 |
| 185962590893 | 78 | 78 | 79.5% | 91.0% | reviewed | 46.8 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label is one of the collector's candidates for 9 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | best | precision |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (278)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 259 | good -> excellent x37, best -> excellent x36, excellent -> best x33, inaccuracy -> good x29, great -> best x22, excellent -> good x19 |
| `miss_detector` | 8 | mistake -> miss x4, blunder -> miss x4 |
| `mate_override` | 4 | good -> miss x1, excellent -> miss x1, excellent -> inaccuracy x1, best -> miss x1 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `blunder_softened` | 2 | miss -> mistake x1, blunder -> mistake x1 |
| `great_find_event` | 2 | best -> great x2 |
| `losing_material_hardened` | 1 | excellent -> mistake x1 |

### `precision` (259)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0075 | 0.492 | no | Be2 | - | -0.10 | -0.19 |
| 1034847688 | 20 | 10... Bg4 | inaccuracy | good | precision | good | 0.0384 | 0.494 | no | Bf5 | Bf5 | +0.64 | +0.47 |
| 1034847688 | 22 | 11... a5 | mistake | inaccuracy | precision | inaccuracy | 0.0977 | 0.485 | no | Nbd7 | Nbd7 | +1.29 | +1.22 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0930 | 0.613 | no | cxb5 | cxb5 | +0.44 | +0.21 |
| 1034847688 | 26 | 13... h6 | inaccuracy | good | precision | good | 0.0468 | 0.491 | no | Qd7 | - | +0.90 | +0.60 |
| 1034847688 | 34 | 17... hxg5 | best | inaccuracy | precision | inaccuracy | 0.0531 | 0.482 | no | a4 | - | 0.00 | +0.93 |
| 1034847688 | 36 | 18... Ne5 | inaccuracy | good | precision | good | 0.0202 | 0.437 | no | f5 | a4 | +0.86 | +1.27 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.539 | yes | Nxf3 | - | -0.10 | +0.00 |
| 1034847688 | 42 | 21... e5 | best | excellent | precision | excellent | 0.0178 | 0.473 | no | f6 | - | +0.39 | +0.56 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.552 | yes | dxe6 | - | +0.30 | +0.42 |
| 1034847688 | 44 | 22... Qxg5 | excellent | best | precision | best | 0.0000 | 0.461 | yes | Qxg5 | - | +0.46 | +0.50 |
| 1034847688 | 45 | 23. exf7+ | good | excellent | precision | excellent | 0.0084 | 0.547 | no | Qc3 | - | +0.09 | +0.71 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | good | precision | good | 0.0229 | 0.434 | no | Rxf7 | Rxf7 | +0.92 | +0.93 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0292 | 0.562 | no | Nf3 | - | +0.37 | +0.37 |
| 1041474766 | 8 | 4... Nf6 | book | best | precision | best | 0.0000 | 0.467 | no | e5 | - | +0.38 | +0.57 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.551 | yes | Bg2 | - | +0.34 | +0.36 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0053 | 0.468 | no | e5 | - | +0.59 | +0.47 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0294 | 0.542 | no | Nf3 | - | +0.17 | +0.14 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0255 | 0.522 | no | d5 | - | +0.08 | +0.14 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0127 | 0.492 | no | Nc3 | - | -0.25 | -0.06 |
| 184759554082 | 12 | 6... Bg7 | good | excellent | precision | excellent | 0.0096 | 0.510 | no | d5 | - | 0.00 | +0.05 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0255 | 0.525 | no | gxh5 | - | +0.03 | +0.12 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.525 | yes | hxg6 | - | -0.13 | -0.13 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.593 | yes | d5 | - | -0.52 | -0.62 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1740 | 0.403 | no | cxd5 | cxd5 | -1.98 | -1.91 |
| 184759554082 | 26 | 13... Qxg5 | great | best | precision | best | 0.0000 | 0.777 | yes | Qxg5 | - | -1.98 | -1.93 |
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | precision | mistake | 0.1902 | 0.871 | no | Qxg2 | Qxg2 | -0.96 | -1.12 |
| 184759554082 | 34 | 17... Qg5 | excellent | good | precision | good | 0.0417 | 0.677 | no | Bg4 | - | -0.88 | -0.87 |
| 184759554082 | 35 | 18. O-O-O | good | inaccuracy | precision | inaccuracy | 0.0527 | 0.365 | no | Qb2+ | - | -1.01 | -1.12 |
| 184759554082 | 36 | 18... Qf6 | best | excellent | precision | excellent | 0.0113 | 0.671 | no | Re5 | - | -1.01 | -1.05 |
| 184759554082 | 37 | 19. Kb1 | good | best | precision | best | 0.0000 | 0.339 | yes | Kb1 | - | -1.19 | -1.16 |
| 184759554082 | 38 | 19... Bf5 | excellent | inaccuracy | precision | inaccuracy | 0.0520 | 0.677 | no | Rd8 | - | -1.10 | -0.80 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.708 | yes | Re6 | - | -1.31 | -1.39 |
| 184759554082 | 44 | 22... Rd6 | excellent | best | precision | best | 0.0000 | 0.722 | no | a5 | - | -1.28 | -1.41 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0026 | 0.289 | no | Rh1 | - | -1.28 | -1.49 |
| 184759554082 | 52 | 26... Rh8 | good | excellent | precision | excellent | 0.0175 | 0.740 | no | Bg4 | - | -1.41 | -1.50 |
| 184759554082 | 55 | 28. Rh1 | inaccuracy | good | precision | good | 0.0359 | 0.283 | no | Rc2 | Rg1 | -1.76 | -1.75 |
| 184759554082 | 56 | 28... Ree8 | good | excellent | precision | excellent | 0.0096 | 0.753 | no | Rxh1 | - | -1.61 | -1.58 |
| 184759554082 | 57 | 29. Ka2 | good | excellent | precision | excellent | 0.0086 | 0.268 | no | Rhd1 | - | -1.73 | -1.65 |
| 184759554082 | 58 | 29... Rc8 | inaccuracy | good | precision | good | 0.0252 | 0.741 | no | Rxh1 | Rxh1 | -1.36 | -1.45 |
| 184759554082 | 59 | 30. Rxh8 | inaccuracy | good | precision | good | 0.0419 | 0.284 | no | Rhd1 | Rhd1 | -1.74 | -1.79 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0468 | 0.547 | no | dxc6 | - | -0.08 | +0.00 |
| 185209623352 | 7 | 4. d4 | best | excellent | precision | excellent | 0.0006 | 0.501 | no | Nf3 | - | -0.08 | -0.09 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.501 | yes | Nf3 | - | -0.16 | -0.01 |
| 185209623352 | 12 | 6... Bf5 | good | excellent | precision | excellent | 0.0153 | 0.506 | no | Bg4 | - | +0.38 | +0.17 |
| 185209623352 | 17 | 9. Qd2 | inaccuracy | good | precision | good | 0.0364 | 0.670 | no | Bxc6 | Bxc6 | +2.14 | +2.19 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.771 | yes | Nxe4 | - | +5.09 | +5.39 |
| 185209623352 | 20 | 10... dxe4 | mistake | excellent | precision | excellent | 0.0055 | 0.228 | no | Qb4 | - | +6.16 | +5.61 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0686 | 0.780 | no | Nxc6 | Nxc6 | +4.00 | +3.84 |
| 185209623352 | 22 | 11... Qxd4 | excellent | good | precision | good | 0.0266 | 0.296 | no | Qd5 | - | +4.04 | +4.48 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0190 | 0.734 | no | Bxc6 | - | +4.04 | +4.00 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0324 | 0.721 | no | O-O-O | O-O-O | +3.00 | +3.57 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | excellent | precision | excellent | 0.0124 | 0.309 | no | e5 | - | +4.18 | +3.83 |
| 185209623352 | 27 | 14. Nxd8 | inaccuracy | good | precision | good | 0.0481 | 0.704 | no | Be3 | Be3 | +2.85 | +2.85 |
| 185209623352 | 29 | 15. Nf7 | excellent | best | precision | best | 0.0000 | 0.659 | yes | Nf7 | - | +2.76 | +2.86 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.265 | yes | Kc7 | - | +4.76 | +4.56 |
| 185209623352 | 40 | 20... Rd8 | inaccuracy | good | precision | good | 0.0385 | 0.358 | no | b6 | - | +3.82 | +3.76 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1510 | 0.701 | no | Bxe6 | - | +0.61 | +0.88 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.671 | yes | Rc5+ | - | +3.32 | +3.01 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.461 | yes | Nd3+ | - | +0.92 | +1.36 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.576 | yes | Nxd3 | Rxd3 | -0.61 | +1.25 |
| 185209623352 | 49 | 25. Rb5+ | excellent | best | precision | best | 0.0000 | 0.711 | yes | Rb5+ | - | +3.97 | +3.92 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0042 | 0.712 | no | Rd5 | - | +3.97 | +3.88 |
| 185209623352 | 54 | 27... Bh6+ | good | excellent | precision | excellent | 0.0051 | 0.294 | no | Bc3 | - | +4.48 | +4.19 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0064 | 0.723 | no | Rd5 | - | +4.14 | +4.11 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0111 | 0.751 | no | Rh5 | - | +4.64 | +4.63 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.720 | yes | Kc2 | - | +4.38 | +4.20 |
| 185209623352 | 70 | 35... Rxc4 | excellent | best | precision | best | 0.0000 | 0.275 | yes | Rxc4 | - | +4.77 | +4.40 |
| 185209623352 | 71 | 36. Rh6 | good | excellent | precision | excellent | 0.0191 | 0.730 | no | Rb1 | - | +4.11 | +3.98 |
| 185209623352 | 73 | 37. Kc2 | inaccuracy | good | precision | good | 0.0428 | 0.714 | no | Ke3 | - | +3.00 | +3.15 |
| 185209623352 | 77 | 39. Kb1 | inaccuracy | good | precision | good | 0.0452 | 0.654 | no | g4 | g4 | +1.67 | +1.96 |
| 185209623352 | 78 | 39... Rb2+ | good | excellent | precision | excellent | 0.0123 | 0.391 | no | Rg2 | - | +2.15 | +2.19 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.621 | yes | Kc1 | - | +2.15 | +2.12 |
| 185209623352 | 81 | 41. Re1+ | inaccuracy | good | precision | good | 0.0415 | 0.758 | no | Rxf6+ | Rxf6+ | +4.65 | +4.17 |
| 185209623352 | 82 | 41... Kf7 | mistake | good | precision | good | 0.0437 | 0.280 | no | Kd5 | - | +6.01 | +5.18 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1245 | 0.632 | no | Rhxe7 | Rhxe7 | -0.08 | -0.10 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1733 | 0.500 | no | Kf7 | - | +3.73 | +3.13 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.670 | yes | Rf1+ | - | +3.73 | +3.33 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.734 | yes | Kxb2 | - | +5.17 | +4.75 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0102 | 0.255 | no | Bxf4 | - | +5.65 | +4.99 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0090 | 0.243 | no | b5 | - | +6.38 | +5.24 |
| 185209623352 | 100 | 50... b5 | best | excellent | precision | excellent | 0.0000 | 0.224 | no | b6 | - | +6.38 | +5.27 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0048 | 0.773 | no | Rc7 | - | +6.33 | +5.48 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0008 | 0.225 | no | Bd8 | - | +6.33 | +5.30 |
| 185209623352 | 106 | 53... Kg6 | excellent | good | precision | good | 0.0324 | 0.228 | no | Bg7 | - | +6.59 | +6.25 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0146 | 0.804 | no | Rb6 | - | +6.59 | +5.86 |
| 185209623352 | 110 | 55... Kg6 | excellent | best | precision | best | 0.0000 | 0.198 | yes | Kg6 | - | +6.54 | +7.05 |
| 185209623352 | 111 | 56. Rbxe5 | best | good | precision | good | 0.0397 | 0.831 | no | Rexe5 | - | +6.54 | +5.90 |
| 185209623352 | 112 | 56... Bxe5 | excellent | good | precision | good | 0.0286 | 0.209 | no | Kg7 | - | +6.75 | +6.71 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.129 | no | Kg7 | - | +7.19 | +7.08 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0116 | 0.138 | no | Ke7 | Ke7 | +10.6 | M17 |
| 185209623352 | 117 | 59. h5 | good | best | precision | best | 0.0000 | 1.000 | yes | h5 | - | +8.42 | +7.16 |
| 185209623352 | 118 | 59... Kf7 | inaccuracy | mistake | precision | mistake | 0.1655 | 0.165 | no | Kf6 | Kf6 | M10 | M18 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | M12 |
| 185209623352 | 123 | 62. Rg8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rh4 | - | M7 | M12 |
| 185209623352 | 125 | 63. h7 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kd3 | - | M5 | M8 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke5 | - | M5 | M6 |
| 185209623352 | 127 | 64. h8=Q | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kd3 | - | M4 | M8 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 133 | 67. Re8+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kc3 | - | M2 | M5 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 141 | 71. g4 | good | best | precision | best | 0.0000 | 0.874 | yes | g4 | - | +10.4 | M12 |
| 185209623352 | 142 | 71... Kb5 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb7 | - | M8 | M11 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | no | Rf8 | - | M9 | M16 |
| 185209623352 | 153 | 77. Qc7 | excellent | best | precision | best | 0.0000 | 1.000 | no | Qd5+ | - | M3 | M3 |
| 185324357184 | 6 | 3... Bc5 | blunder | mistake | precision | mistake | 0.1799 | 0.501 | no | d5 | - | +3.27 | +3.27 |
| 185324357184 | 7 | 4. h3 | miss | blunder | precision | blunder | 0.2520 | 0.679 | no | fxe5 | fxe5 | -1.29 | -1.29 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0010 | 0.300 | no | d4 | - | -4.03 | -3.84 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0273 | 0.595 | no | Ng3 | Ng3 | -0.98 | -0.84 |
| 185324357184 | 19 | 10. Ne2 | good | excellent | precision | excellent | 0.0186 | 0.452 | no | Qe3 | - | -1.32 | -1.17 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0596 | 0.567 | no | Na6 | - | +0.29 | +0.10 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.506 | yes | Qg1 | - | +0.29 | +0.00 |
| 185324357184 | 22 | 11... O-O | inaccuracy | good | precision | good | 0.0485 | 0.500 | no | Bxc2 | Bxc2 | +1.17 | +1.22 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.658 | yes | Re1 | - | +3.07 | +2.86 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0297 | 0.342 | no | Qh5 | - | +3.38 | +3.24 |
| 185324357184 | 39 | 20. Rf1 | great | best | precision | best | 0.0000 | 0.677 | yes | Rf1 | - | +3.38 | +3.33 |
| 185324357184 | 46 | 23... b5 | excellent | best | precision | best | 0.0000 | 0.490 | no | b6 | - | +0.26 | +0.12 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0011 | 0.507 | no | Be3 | - | +0.26 | +0.37 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.600 | yes | Nxe5 | - | +1.74 | +1.90 |
| 185437323918 | 10 | 5... Kf8 | good | excellent | precision | excellent | 0.0161 | 0.444 | no | Ke7 | - | +1.39 | +1.37 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0270 | 0.326 | no | d4 | - | -3.51 | -3.66 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0794 | 0.302 | no | d4 | d3 | -5.55 | -5.36 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0122 | 0.782 | no | Qe8 | - | -5.16 | -5.21 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0265 | 0.782 | no | Qe8 | - | -4.94 | -4.84 |
| 185437323918 | 23 | 12. Qg3 | mistake | good | precision | good | 0.0312 | 0.236 | no | Qe3 | - | -6.88 | -6.32 |
| 185437323918 | 31 | 16. Nd2 | excellent | best | precision | best | 0.0000 | 0.211 | yes | Nd2 | - | -6.16 | -5.56 |
| 185437323918 | 32 | 16... dxc3 | excellent | best | precision | best | 0.0000 | 0.785 | yes | dxc3 | - | -5.87 | -5.79 |
| 185437323918 | 33 | 17. bxc3 | good | excellent | precision | excellent | 0.0019 | 0.206 | no | g4 | - | -6.58 | -6.12 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0074 | 0.806 | no | Rxh2+ | - | -6.58 | -5.92 |
| 185437323918 | 35 | 18. Bb2 | mistake | blunder | precision | blunder | 0.2010 | 0.201 | no | Nf3 | - | -M2 | -M2 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.790 | no | Qe2 | - | -5.96 | -6.18 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0404 | 0.740 | no | Qf4 | - | -3.59 | -3.69 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0813 | 0.297 | no | hxg3 | hxg3 | -5.85 | -5.55 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0140 | 0.758 | no | e4 | - | -4.41 | -4.57 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0348 | 0.660 | no | Bc2 | - | -2.41 | -2.14 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.763 | yes | Be4 | - | -5.61 | -5.10 |
| 185437323918 | 59 | 30. g5+ | good | excellent | precision | excellent | 0.0163 | 0.233 | no | Kg2 | - | -6.55 | -5.50 |
| 185437323918 | 61 | 31. Rf1 | excellent | best | precision | best | 0.0000 | 0.213 | yes | Rf1 | - | -7.00 | -5.79 |
| 185437323918 | 62 | 31... Bxf3+ | good | excellent | precision | excellent | 0.0008 | 0.794 | no | Rf8 | - | -6.21 | -5.64 |
| 185437323918 | 64 | 32... Kxg5 | good | excellent | precision | excellent | 0.0038 | 0.795 | no | e4 | - | -5.64 | -5.72 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0180 | 0.789 | no | Kf4 | - | -5.11 | -5.21 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | excellent | precision | excellent | 0.0184 | 0.229 | no | Kg2 | Kg2 | -6.13 | -5.75 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0332 | 0.793 | no | e4 | e4 | -5.01 | -4.93 |
| 185437323918 | 69 | 35. Rg4+ | good | excellent | precision | excellent | 0.0105 | 0.241 | no | c5 | - | -5.79 | -5.17 |
| 185437323918 | 71 | 36. Kg3 | excellent | best | precision | best | 0.0000 | 0.224 | yes | Kg3 | - | -5.97 | -5.46 |
| 185437323918 | 73 | 37. Kf3 | excellent | best | precision | best | 0.0000 | 0.225 | yes | Kf3 | - | -6.12 | -5.38 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0157 | 0.778 | no | Bb4 | - | -6.12 | -5.00 |
| 185437323918 | 80 | 40... Kxg4 | best | excellent | precision | excellent | 0.0000 | 0.782 | no | Kg5 | - | -6.12 | -5.63 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0003 | 0.849 | no | Bg3 | - | -7.28 | -7.76 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.141 | yes | Kxc7 | - | -8.05 | -7.76 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.133 | yes | d6 | - | -8.99 | -8.12 |
| 185437323918 | 91 | 46. Kxb7 | excellent | best | precision | best | 0.0000 | 0.140 | yes | Kxb7 | - | -9.64 | -8.21 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.112 | yes | Kc6 | Ka6 | -M17 | -M18 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -M25 |
| 185437323918 | 98 | 49... Qb7+ | good | excellent | precision | excellent | 0.0000 | 0.902 | no | Qe5+ | - | -8.99 | -M19 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.000 | yes | c6 | - | -10.7 | -8.63 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0020 | 0.882 | no | Qb6 | - | -10.7 | -M7 |
| 185437323918 | 101 | 51. Ke6 | good | best | precision | best | 0.0000 | 0.000 | yes | Ke6 | - | -M6 | -M7 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2336 | 0.234 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0148 | 0.505 | no | Nf3 | - | -0.01 | -0.17 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.510 | yes | h6 | - | -0.01 | -0.08 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.495 | yes | Bh4 | - | -0.01 | -0.01 |
| 185438707002 | 12 | 6... g5 | good | excellent | precision | excellent | 0.0142 | 0.501 | no | Na5 | - | +0.33 | +0.23 |
| 185438707002 | 26 | 13... O-O-O | miss | inaccuracy | precision | inaccuracy | 0.0833 | 0.627 | no | Rg8 | Rg8 | -0.69 | -0.73 |
| 185438707002 | 28 | 14... Nd4 | inaccuracy | mistake | precision | mistake | 0.1051 | 0.536 | no | Rhg8 | Rhg8 | +0.82 | +1.17 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.585 | yes | c3 | - | +1.35 | +1.59 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0622 | 0.407 | no | Bb6 | - | +2.65 | +2.71 |
| 185438707002 | 42 | 21... Nb6 | good | excellent | precision | excellent | 0.0005 | 0.296 | no | Rf8 | - | +3.99 | +3.67 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0511 | 0.302 | no | Rf8 | - | +4.87 | +4.62 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0373 | 0.750 | no | Qf6 | Qf6 | +3.70 | +3.82 |
| 185438707002 | 51 | 26. Rhd1 | excellent | good | precision | good | 0.0240 | 0.719 | no | Qf6 | - | +3.49 | +3.57 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.300 | yes | a6 | - | +3.78 | +3.74 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0084 | 0.708 | no | Qf3 | - | +3.78 | +3.57 |
| 185438707002 | 54 | 27... Rf8 | mistake | inaccuracy | precision | inaccuracy | 0.0835 | 0.300 | no | Rc8 | Rh7 | +5.73 | +5.42 |
| 185438707002 | 55 | 28. Rd8+ | miss | inaccuracy | precision | inaccuracy | 0.0815 | 0.783 | no | Qxf8+ | Qxf8+ | +3.74 | +3.73 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.711 | yes | Qxd8+ | - | +3.69 | +3.66 |
| 185438707002 | 59 | 30. Qxh4 | excellent | good | precision | good | 0.0283 | 0.707 | no | Qd2 | - | +3.68 | +3.15 |
| 185438707002 | 65 | 33. Rd5 | excellent | best | precision | best | 0.0000 | 0.609 | yes | Rd5 | - | +1.84 | +2.08 |
| 185438707002 | 66 | 33... Qxa3+ | inaccuracy | good | precision | good | 0.0318 | 0.379 | no | c6 | Qb3 | +2.60 | +2.66 |
| 185438707002 | 68 | 34... Qb2+ | great | excellent | precision | excellent | 0.0005 | 0.687 | no | Qa2+ | - | -3.65 | -3.22 |
| 185438707002 | 74 | 37... Qxd5 | excellent | best | precision | best | 0.0000 | 0.695 | yes | Qxd5 | - | -3.38 | -3.41 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0429 | 0.666 | no | Qe2 | - | -2.36 | -2.12 |
| 185438707002 | 80 | 40... Nd2 | good | excellent | precision | excellent | 0.0033 | 0.635 | no | Qf7 | - | -1.83 | -2.28 |
| 185438707002 | 81 | 41. h5 | blunder | mistake | precision | mistake | 0.1904 | 0.368 | no | Qg5 | - | -7.11 | -6.46 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.106 | yes | g4 | - | -8.80 | -M14 |
| 185438707002 | 89 | 45. g3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | g5 | g5 | -M7 | -M14 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0600 | 0.412 | no | e6 | e6 | +1.09 | +0.96 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0073 | 0.648 | no | Nf3 | - | +0.96 | +0.91 |
| 185456088510 | 6 | 3... e6 | excellent | good | precision | good | 0.0302 | 0.359 | no | Nc6 | - | +1.01 | +1.00 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0057 | 0.336 | no | d5 | - | +1.01 | +1.07 |
| 185456088510 | 11 | 6. h4 | good | inaccuracy | precision | inaccuracy | 0.0508 | 0.673 | no | O-O | - | +0.95 | +0.78 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0090 | 0.386 | no | Bg7 | - | +0.81 | +0.86 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.594 | yes | Ng3 | - | +0.65 | +0.58 |
| 185456088510 | 20 | 10... Ng4 | excellent | good | precision | good | 0.0229 | 0.409 | no | h5 | - | +0.74 | +0.94 |
| 185456088510 | 21 | 11. Bd2 | excellent | good | precision | good | 0.0372 | 0.645 | no | Bc1 | - | +0.70 | +0.64 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.675 | yes | h5 | - | +1.12 | +1.08 |
| 185456088510 | 31 | 16. exd6 | excellent | inaccuracy | precision | inaccuracy | 0.0530 | 0.753 | no | Qe2 | - | +1.55 | +1.72 |
| 185456088510 | 34 | 17... Qe7 | miss | blunder | precision | blunder | 0.2142 | 0.421 | no | Bxe4 | Bxe4 | +1.83 | +2.11 |
| 185456088510 | 35 | 18. Qe2 | best | excellent | precision | excellent | 0.0074 | 0.793 | no | Nh4 | - | +1.83 | +2.02 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0481 | 0.816 | no | Nh4 | - | +1.72 | +1.73 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0516 | 0.168 | no | Rd6 | - | +2.89 | +3.18 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0174 | 0.883 | no | a5 | - | +2.89 | +3.07 |
| 185456088510 | 48 | 24... Qc7 | excellent | good | precision | good | 0.0223 | 0.124 | no | Qc8 | - | +3.01 | +3.26 |
| 185456088510 | 54 | 27... e4 | inaccuracy | good | precision | good | 0.0334 | 0.177 | no | Rc6 | - | +2.96 | +2.99 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.944 | yes | Nxe3 | - | -4.25 | -4.91 |
| 185456088510 | 57 | 29. Nd4 | mistake | excellent | precision | excellent | 0.0000 | 0.042 | no | Qb5 | - | -4.77 | -4.71 |
| 185456088510 | 59 | 30. b5 | excellent | good | precision | good | 0.0216 | 0.036 | no | Qb5 | - | -6.85 | -6.58 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0035 | 0.447 | no | Na4 | - | -0.94 | -0.98 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0145 | 0.491 | no | Ne5 | - | +0.60 | +0.41 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0398 | 0.476 | no | Kf8 | - | +0.61 | +1.11 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | excellent | precision | excellent | 0.0188 | 0.434 | no | dxe5 | dxe5 | +1.53 | +1.58 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.591 | yes | Qh5 | - | +1.48 | +1.60 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1971 | 0.623 | no | Nxc7+ | Nxc7+ | -0.91 | -1.28 |
| 185468039834 | 25 | 13. Nf6+ | good | best | precision | best | 0.0000 | 0.427 | yes | Nf6+ | - | -1.28 | -1.29 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.715 | yes | Rf8 | - | -3.36 | -3.93 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0127 | 0.287 | no | Qd3 | - | -3.39 | -4.18 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0088 | 0.512 | no | d3 | - | +0.15 | +0.10 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.494 | yes | exd4 | - | +0.15 | +0.12 |
| 185468614210 | 11 | 6. cxd4 | book | excellent | precision | excellent | 0.0064 | 0.507 | no | e5 | - | 0.00 | +0.00 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.500 | yes | Bb4+ | - | 0.00 | +0.00 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0134 | 0.500 | no | Bd2 | - | -0.35 | -0.51 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0450 | 0.474 | no | Nxe4 | Nxe4 | +1.21 | +1.22 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0378 | 0.488 | no | Kg8 | Kg8 | +1.21 | +0.86 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0378 | 0.550 | no | Qh5+ | Qh5+ | +0.18 | +0.23 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.487 | yes | Kg8 | - | +0.18 | +0.13 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0127 | 0.545 | no | d4 | - | +0.74 | +0.61 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.465 | yes | Bb7 | - | +0.74 | +0.70 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.541 | yes | Nc3 | - | +0.74 | +0.70 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.459 | yes | e6 | - | +0.74 | +0.67 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0110 | 0.472 | no | Bb4 | - | +0.55 | +0.71 |
| 185475865432 | 11 | 6. Bb3 | inaccuracy | good | precision | good | 0.0372 | 0.541 | no | Bd3 | - | -0.37 | -0.37 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0126 | 0.575 | no | e5 | - | +0.82 | +0.82 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0929 | 0.548 | no | Nf4 | Ng3 | -0.76 | -0.78 |
| 185475865432 | 23 | 12. Bf4 | inaccuracy | good | precision | good | 0.0471 | 0.467 | no | Qxd8+ | - | -1.49 | -1.39 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0193 | 0.427 | no | Re1 | - | -1.49 | -1.60 |
| 185475865432 | 27 | 14. Ng3 | inaccuracy | good | precision | good | 0.0407 | 0.435 | no | Nxc6 | Qxd8+ | -1.91 | -1.92 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0314 | 0.610 | no | Qxd1 | Qxd1 | -1.24 | -1.36 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0079 | 0.421 | no | hxg3 | - | -1.52 | -1.59 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0045 | 0.587 | no | Bd6 | - | -1.25 | -1.41 |
| 185475865432 | 34 | 17... Rxd8 | inaccuracy | good | precision | good | 0.0476 | 0.605 | no | Kxd8 | Kxd8 | -0.89 | -0.97 |
| 185475865432 | 37 | 19. Rad1 | excellent | best | precision | best | 0.0000 | 0.596 | yes | Rad1 | - | +1.50 | +1.57 |
| 185475865432 | 49 | 25. a6 | mistake | inaccuracy | precision | inaccuracy | 0.0737 | 0.684 | no | Rxe6 | Rxe6 | +1.47 | +1.93 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0556 | 0.613 | no | Bc4 | - | +0.50 | +0.36 |
| 185962590893 | 10 | 5... Bg4 | good | inaccuracy | precision | inaccuracy | 0.0616 | 0.443 | no | e5 | - | +0.80 | +0.76 |
| 185962590893 | 14 | 7... Nd7 | best | excellent | precision | excellent | 0.0030 | 0.386 | no | Nf6 | - | +0.82 | +0.81 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.430 | yes | e5 | - | +0.67 | +0.54 |
| 185962590893 | 19 | 10. Bd2 | good | excellent | precision | excellent | 0.0015 | 0.585 | no | Bg5 | - | +0.50 | +0.45 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.429 | yes | Be7 | - | +0.55 | +0.45 |
| 185962590893 | 25 | 13. Nf5 | excellent | best | precision | best | 0.0000 | 0.594 | yes | Nf5 | - | +0.64 | +0.42 |
| 185962590893 | 27 | 14. Nxe7+ | miss | inaccuracy | precision | inaccuracy | 0.0608 | 0.746 | no | Bh6 | Bh6 | +1.01 | +1.26 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0923 | 0.751 | no | Rxd8+ | Rxd8+ | +0.96 | +1.00 |
| 185962590893 | 35 | 18. g5 | best | good | precision | good | 0.0264 | 0.653 | no | Rxd7 | - | +0.96 | +0.88 |
| 185962590893 | 49 | 25. Bg4 | excellent | inaccuracy | precision | inaccuracy | 0.0502 | 0.629 | no | Qc3 | - | +0.82 | +0.50 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.574 | yes | Qe3 | Qf3 | +0.47 | +0.72 |
| 185962590893 | 52 | 26... Nd4 | mistake | good | precision | good | 0.0283 | 0.387 | no | Nf4 | Nf4 | +1.15 | +1.16 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2323 | 0.677 | no | f4 | - | -0.39 | -0.35 |
| 185962590893 | 62 | 31... exf4 | good | excellent | precision | excellent | 0.0127 | 0.525 | no | Kf7 | - | -0.08 | -0.09 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `miss_detector` (8)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 29 | 15. Rad1 | mistake | miss (opportunity) | miss_detector | mistake | 0.1630 | 0.543 | no | h5 | h5 | -1.48 | -1.30 |
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1504 | 0.650 | no | g4 | - | -0.01 | -0.12 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1409 | 0.763 | no | Rxf6+ | Rxf6+ | +2.74 | +2.59 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.3636 | 0.734 | no | Rxf6+ | - | -2.81 | -2.34 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2137 | 0.717 | no | Kg7 | - | -0.17 | -0.05 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2539 | 0.254 | no | Kd2 | - | -M1 | -M1 |
| 185438707002 | 25 | 13. a3 | mistake | miss (tactic) | miss_detector | mistake | 0.1377 | 0.511 | no | Na4 | - | -2.10 | -2.19 |
| 185468614210 | 7 | 4. c3 | mistake | miss (tactic) | miss_detector | mistake | 0.1372 | 0.588 | no | Nxe5 | Nxe5 | -0.88 | -0.85 |

### `mate_override` (4)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M6 |
| 185437323918 | 94 | 47... Qb2+ | excellent | miss (mate) | mate_override | mistake | 0.1116 | 1.000 | no | Qd4 | - | -9.07 | -8.90 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |
| 185438707002 | 86 | 43... Qf7 | best | miss (mate) | mate_override | mistake | 0.1062 | 1.000 | no | e4 | - | -8.73 | -8.98 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | best | 0.0000 | 0.459 | yes | c6 | - | +0.82 | +0.83 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0565 | 0.525 | no | Nxe5 | Nxe5 | -0.62 | -0.54 |

### `blunder_softened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2033 | 0.563 | no | Qxg3+ | Qxg3+ | +2.48 | +2.53 |
| 185438707002 | 67 | 34. Kc2 | blunder | mistake | blunder_softened | blunder | 0.3081 | 0.653 | no | Kd1 | - | -3.65 | -3.31 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.517 | yes | Bxe5 | - | +0.18 | +0.28 |
| 185438343298 | 15 | 8. g3 | best | great | great_find_event | best | 0.0000 | 0.228 | yes | g3 | - | -5.11 | -5.24 |

### `losing_material_hardened` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | excellent | 0.0124 | 0.137 | no | Kb6 | - | -8.94 | -8.30 |

