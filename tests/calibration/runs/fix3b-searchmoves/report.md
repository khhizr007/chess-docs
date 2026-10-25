# Calibration report: fix3b-searchmoves

- Generated: 2026-10-17T19:53:04+00:00
- Commit: `b9f8aada9809` + uncommitted backend changes (diff sha256 `26fae1f81bc2`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 14 requested, 14 compared, 0 skipped (list: `/mnt/c/Users/khhizr/rea_projects/chess-review/tests/calibration/tuning.txt`)
- Plies: 865 aligned, 856 scored, 9 excluded (uncertain 9)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 68.8% (589/856) |
| Within one step | 89.0% (762/856) |
| Brilliant precision / recall | 1.00 / 0.33 |
| Great precision / recall | 0.56 / 0.19 |
| Brilliant per 100 moves (app / ours) | 0.35 / 0.12 |
| Great per 100 moves (app / ours) | 3.04 / 1.05 |
| Accuracy mean abs. difference | 3.25 (n=28, max 9.07) |
| Accuracy bias (ours - app) | +2.82 |
| Best move = app's suggestion | 81.0% (111/137 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 1 | . | 1 | . | . | . | . | . | 3 |
| **great** | . | **5** | 21 | . | . | . | . | . | . | . | 26 |
| **best** | . | 4 | **266** | 39 | 5 | . | 1 | 1 | . | . | 316 |
| **excellent** | . | . | 34 | **71** | 18 | 1 | 2 | 1 | . | . | 127 |
| **good** | . | . | 5 | 31 | **57** | . | 7 | 1 | 2 | . | 103 |
| **book** | . | . | 8 | 8 | 2 | **79** | . | . | . | . | 97 |
| **inaccuracy** | . | . | 6 | 3 | 25 | 1 | **54** | 3 | . | . | 92 |
| **mistake** | . | . | . | 1 | 2 | . | 11 | **26** | 2 | 2 | 44 |
| **miss** | . | . | . | . | 1 | . | 5 | 5 | **16** | . | 27 |
| **blunder** | . | . | . | . | . | . | . | 3 | 4 | **14** | 21 |
| **total** | 1 | 9 | 341 | 153 | 111 | 81 | 80 | 40 | 24 | 16 | 856 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 1 | 1 | 1.000 | 0.333 | 0.500 |
| great | 26 | 9 | 5 | 0.556 | 0.192 | 0.286 |
| best | 316 | 341 | 266 | 0.780 | 0.842 | 0.810 |
| excellent | 127 | 153 | 71 | 0.464 | 0.559 | 0.507 |
| good | 103 | 111 | 57 | 0.514 | 0.553 | 0.533 |
| book | 97 | 81 | 79 | 0.975 | 0.814 | 0.888 |
| inaccuracy | 92 | 80 | 54 | 0.675 | 0.587 | 0.628 |
| mistake | 44 | 40 | 26 | 0.650 | 0.591 | 0.619 |
| miss | 27 | 24 | 16 | 0.667 | 0.593 | 0.627 |
| blunder | 21 | 16 | 14 | 0.875 | 0.667 | 0.757 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.8 | +6.1 |
| 1034847688 | black | 65.0 | 74.1 | +9.1 |
| 1041474766 | white | 98.0 | 97.3 | -0.7 |
| 1041474766 | black | 83.8 | 86.3 | +2.5 |
| 184759554082 | white | 81.2 | 86.9 | +5.7 |
| 184759554082 | black | 87.7 | 90.2 | +2.5 |
| 185209623352 | white | 72.7 | 74.6 | +1.9 |
| 185209623352 | black | 72.6 | 74.1 | +1.5 |
| 185324357184 | white | 73.0 | 75.3 | +2.3 |
| 185324357184 | black | 62.4 | 65.8 | +3.4 |
| 185436488062 | white | 98.6 | 97.6 | -1.0 |
| 185436488062 | black | 38.5 | 41.3 | +2.8 |
| 185437323918 | white | 69.5 | 73.9 | +4.4 |
| 185437323918 | black | 75.7 | 72.8 | -2.9 |
| 185438343298 | white | 46.9 | 46.8 | -0.1 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185438707002 | white | 77.8 | 76.4 | -1.4 |
| 185438707002 | black | 83.0 | 84.1 | +1.1 |
| 185456088510 | white | 78.4 | 83.0 | +4.6 |
| 185456088510 | black | 82.2 | 84.3 | +2.1 |
| 185468039834 | white | 80.0 | 85.0 | +5.0 |
| 185468039834 | black | 87.5 | 90.0 | +2.5 |
| 185468614210 | white | 70.8 | 76.3 | +5.5 |
| 185468614210 | black | 77.1 | 82.6 | +5.5 |
| 185475865432 | white | 78.1 | 84.2 | +6.1 |
| 185475865432 | black | 66.1 | 72.5 | +6.4 |
| 185962590893 | white | 90.8 | 92.7 | +1.9 |
| 185962590893 | black | 90.9 | 93.1 | +2.2 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 63.3% | 81.6% | reviewed | 97.6 |
| 1041474766 | 25 | 25 | 68.0% | 80.0% | reviewed | 65.3 |
| 184759554082 | 62 | 62 | 62.9% | 87.1% | reviewed | 101.1 |
| 185209623352 | 155 | 155 | 63.9% | 90.3% | reviewed | 91.6 |
| 185324357184 | 55 | 55 | 80.0% | 94.5% | reviewed | 67.0 |
| 185436488062 | 13 | 13 | 84.6% | 92.3% | reviewed | 28.2 |
| 185437323918 | 108 | 103 | 61.2% | 83.5% | reviewed | 41.3 |
| 185438343298 | 20 | 20 | 85.0% | 90.0% | reviewed | 33.2 |
| 185438707002 | 95 | 91 | 73.6% | 91.2% | reviewed | 87.5 |
| 185456088510 | 60 | 60 | 68.3% | 91.7% | reviewed | 69.4 |
| 185468039834 | 38 | 38 | 65.8% | 94.7% | reviewed | 49.3 |
| 185468614210 | 54 | 54 | 75.9% | 87.0% | reviewed | 54.7 |
| 185475865432 | 53 | 53 | 67.9% | 90.6% | reviewed | 59.7 |
| 185962590893 | 78 | 78 | 74.4% | 91.0% | reviewed | 53.2 |

## Excluded plies

9 plies are not scored: uncertain 9. Our label equals the collector's guess for 0 of the 9 uncertain ones.

| game | ply | move | app label | ours | rule |
|---|---:|---|---|---|---|
| 185437323918 | 24 | 12... Ne2+ | uncertain:best/excellent | best | precision |
| 185437323918 | 72 | 36... Be1+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 92 | 46... a1=Q | uncertain:best/excellent | best | precision |
| 185437323918 | 104 | 52... Qd5+ | uncertain:best/excellent | excellent | precision |
| 185437323918 | 106 | 53... Bd6+ | uncertain:best/excellent | good | mate_override |
| 185438707002 | 70 | 35... Qb1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 72 | 36... Qxe4+ | uncertain:best/great | best | precision |
| 185438707002 | 82 | 41... Nf1+ | uncertain:best/great | great | great_find_event |
| 185438707002 | 94 | 47... e1=Q | uncertain:best/great | best | precision |

## Mismatches by rule (267)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 247 | best -> excellent x39, excellent -> best x34, good -> excellent x31, inaccuracy -> good x25, great -> best x21, excellent -> good x18 |
| `miss_detector` | 6 | blunder -> miss x4, mistake -> miss x2 |
| `mate_override` | 5 | good -> miss x2, good -> inaccuracy x1, best -> inaccuracy x1, excellent -> inaccuracy x1 |
| `great_find_event` | 4 | best -> great x4 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `losing_material_hardened` | 2 | good -> mistake x1, excellent -> mistake x1 |
| `blunder_softened` | 1 | miss -> mistake x1 |

### `precision` (247)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 3 | 2. e3 | good | excellent | precision | excellent | 0.0196 | 0.550 | no | d4 | - | +0.31 | +0.20 |
| 1034847688 | 4 | 2... Nf6 | excellent | best | precision | best | 0.0000 | 0.481 | yes | Nf6 | - | +0.33 | +0.31 |
| 1034847688 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0009 | 0.504 | no | c5 | - | +0.13 | +0.12 |
| 1034847688 | 12 | 6... c5 | inaccuracy | good | precision | good | 0.0467 | 0.563 | no | e5 | e5 | -0.10 | -0.11 |
| 1034847688 | 13 | 7. Bb2 | best | excellent | precision | excellent | 0.0178 | 0.490 | no | Be2 | - | -0.10 | -0.21 |
| 1034847688 | 20 | 10... Bg4 | inaccuracy | good | precision | good | 0.0403 | 0.491 | no | Na6 | Bf5 | +0.64 | +0.69 |
| 1034847688 | 23 | 12. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0808 | 0.630 | no | cxb5 | cxb5 | +0.44 | +0.35 |
| 1034847688 | 26 | 13... h6 | inaccuracy | best | precision | best | 0.0000 | 0.467 | yes | h6 | - | +0.90 | +0.53 |
| 1034847688 | 28 | 14... Nbd7 | miss | inaccuracy | precision | inaccuracy | 0.0769 | 0.552 | no | bxc4 | Qd7 | +0.53 | +0.27 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.538 | yes | Nxf3 | - | -0.10 | -0.44 |
| 1034847688 | 40 | 20... Nf5 | inaccuracy | excellent | precision | excellent | 0.0094 | 0.509 | no | Nh5 | f5 | +0.50 | +0.38 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.536 | yes | Rh3 | - | +0.39 | +0.00 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.29 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0317 | 0.473 | no | fxe6 | - | +0.46 | +0.77 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.572 | yes | exf7+ | - | +0.09 | +0.89 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.417 | yes | Kxf7 | Rxf7 | +0.92 | +1.24 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M10 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0327 | 0.568 | no | d4 | - | +0.37 | +0.46 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0044 | 0.459 | no | e5 | - | +0.38 | +0.50 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.545 | yes | Bg2 | - | +0.34 | +0.43 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0009 | 0.462 | no | Nc6 | - | +0.59 | +0.46 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0205 | 0.541 | no | Nf3 | - | +0.17 | +0.17 |
| 1041474766 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.519 | no | d4 | - | +0.28 | +0.29 |
| 1041474766 | 17 | 9. dxe5 | good | excellent | precision | excellent | 0.0186 | 0.552 | no | Bd2 | - | +0.39 | +0.43 |
| 1041474766 | 20 | 10... O-O | excellent | best | precision | best | 0.0000 | 0.469 | yes | O-O | - | +0.40 | +0.27 |
| 184759554082 | 6 | 3... a6 | book | excellent | precision | excellent | 0.0191 | 0.537 | no | d5 | - | +0.08 | +0.04 |
| 184759554082 | 8 | 4... g6 | good | excellent | precision | excellent | 0.0175 | 0.484 | no | d5 | - | +0.32 | +0.34 |
| 184759554082 | 9 | 5. h4 | inaccuracy | good | precision | good | 0.0476 | 0.554 | no | Nc3 | Be2 | -0.11 | -0.22 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0000 | 0.475 | no | Nc3 | - | -0.25 | -0.21 |
| 184759554082 | 12 | 6... Bg7 | good | excellent | precision | excellent | 0.0191 | 0.533 | no | d5 | - | 0.00 | +0.09 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0398 | 0.505 | no | Nxh5 | - | +0.03 | +0.11 |
| 184759554082 | 15 | 8. hxg6 | good | excellent | precision | excellent | 0.0127 | 0.518 | no | d3 | - | -0.21 | -0.05 |
| 184759554082 | 17 | 9. Nf3 | good | inaccuracy | precision | inaccuracy | 0.0524 | 0.502 | no | Nc3 | - | -0.39 | -0.28 |
| 184759554082 | 20 | 10... Re8 | miss | inaccuracy | precision | inaccuracy | 0.0932 | 0.689 | no | d5 | d5 | -0.52 | -0.47 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.585 | yes | d5 | - | -0.52 | -0.57 |
| 184759554082 | 23 | 12. Nxd5 | blunder | mistake | precision | mistake | 0.1362 | 0.410 | no | cxd5 | cxd5 | -1.98 | -2.01 |
| 184759554082 | 34 | 17... Qg5 | excellent | good | precision | good | 0.0450 | 0.670 | no | Bg4 | - | -0.88 | -0.82 |
| 184759554082 | 37 | 19. Kb1 | good | excellent | precision | excellent | 0.0181 | 0.333 | no | Qb2 | - | -1.19 | -1.22 |
| 184759554082 | 38 | 19... Bf5 | excellent | inaccuracy | precision | inaccuracy | 0.0529 | 0.685 | no | Rh8 | - | -1.10 | -0.82 |
| 184759554082 | 44 | 22... Rd6 | excellent | best | precision | best | 0.0000 | 0.713 | no | a5 | - | -1.28 | -1.33 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0119 | 0.300 | no | Rh1 | - | -1.28 | -1.38 |
| 184759554082 | 47 | 24. Ka1 | best | good | precision | good | 0.0220 | 0.295 | no | b4 | - | -1.28 | -1.34 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.701 | yes | a5 | - | -1.16 | -1.56 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0062 | 0.270 | no | f3 | f3 | -1.61 | -1.73 |
| 184759554082 | 55 | 28. Rh1 | inaccuracy | good | precision | good | 0.0470 | 0.312 | no | Rc2 | Rg1 | -1.76 | -1.85 |
| 184759554082 | 56 | 28... Ree8 | good | excellent | precision | excellent | 0.0152 | 0.765 | no | Rxh1 | - | -1.61 | -1.58 |
| 184759554082 | 57 | 29. Ka2 | good | excellent | precision | excellent | 0.0099 | 0.268 | no | Rhe1 | - | -1.73 | -1.83 |
| 185209623352 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0489 | 0.556 | no | dxc6 | - | -0.08 | +0.07 |
| 185209623352 | 8 | 4... Nc6 | best | excellent | precision | excellent | 0.0006 | 0.497 | no | Nf6 | - | -0.08 | +0.02 |
| 185209623352 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.501 | yes | Nf3 | - | -0.16 | +0.00 |
| 185209623352 | 14 | 7... Qd6 | inaccuracy | good | precision | good | 0.0459 | 0.477 | no | Bd7 | Bd7 | +1.28 | +1.25 |
| 185209623352 | 17 | 9. Qd2 | inaccuracy | good | precision | good | 0.0488 | 0.689 | no | Bxc6 | Bxc6 | +2.14 | +2.44 |
| 185209623352 | 19 | 10. Nxe4 | great | best | precision | best | 0.0000 | 0.780 | yes | Nxe4 | - | +5.09 | +5.67 |
| 185209623352 | 20 | 10... dxe4 | mistake | excellent | precision | excellent | 0.0172 | 0.217 | no | Qxe5 | - | +6.16 | +6.23 |
| 185209623352 | 21 | 11. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0730 | 0.803 | no | Nxc6 | Nxc6 | +4.00 | +4.36 |
| 185209623352 | 23 | 12. Qxd4 | best | excellent | precision | excellent | 0.0080 | 0.733 | no | Bxc6 | - | +4.04 | +4.19 |
| 185209623352 | 25 | 13. Ba4 | inaccuracy | good | precision | good | 0.0423 | 0.731 | no | O-O-O | O-O-O | +3.00 | +3.64 |
| 185209623352 | 26 | 13... Ne6 | inaccuracy | good | precision | good | 0.0280 | 0.305 | no | b5 | - | +4.18 | +4.41 |
| 185209623352 | 32 | 16... Ne6 | inaccuracy | good | precision | good | 0.0492 | 0.329 | no | g6 | Nxg2 | +4.22 | +4.31 |
| 185209623352 | 34 | 17... Kc7 | good | best | precision | best | 0.0000 | 0.280 | yes | Kc7 | - | +4.76 | +4.53 |
| 185209623352 | 35 | 18. Rd5 | inaccuracy | good | precision | good | 0.0267 | 0.736 | no | Nd8 | Nd8 | +3.29 | +3.68 |
| 185209623352 | 41 | 21. c4 | blunder | mistake | precision | mistake | 0.1966 | 0.721 | no | Bxe6 | - | +0.61 | +0.53 |
| 185209623352 | 43 | 22. Rc5+ | great | best | precision | best | 0.0000 | 0.667 | yes | Rc5+ | - | +3.32 | +3.13 |
| 185209623352 | 46 | 23... Nd3+ | excellent | best | precision | best | 0.0000 | 0.432 | no | Bxe5 | - | +0.92 | +1.22 |
| 185209623352 | 47 | 24. Nxd3 | inaccuracy | best | precision | best | 0.0000 | 0.568 | yes | Nxd3 | Rxd3 | -0.61 | -0.51 |
| 185209623352 | 50 | 25... Kc7 | best | excellent | precision | excellent | 0.0126 | 0.280 | no | Ka6 | - | +3.97 | +4.15 |
| 185209623352 | 53 | 27. Rxf5 | best | excellent | precision | excellent | 0.0045 | 0.726 | no | Rd5 | - | +3.97 | +4.09 |
| 185209623352 | 55 | 28. Kb2 | excellent | best | precision | best | 0.0000 | 0.741 | yes | Kb2 | - | +4.39 | +4.46 |
| 185209623352 | 57 | 29. Rf7 | good | excellent | precision | excellent | 0.0181 | 0.743 | no | Rh5 | - | +4.14 | +4.56 |
| 185209623352 | 61 | 31. g3 | good | excellent | precision | excellent | 0.0045 | 0.768 | no | Rh5 | - | +4.64 | +4.97 |
| 185209623352 | 63 | 32. f4 | excellent | good | precision | good | 0.0315 | 0.769 | no | Rh5 | - | +4.51 | +4.86 |
| 185209623352 | 66 | 33... Rd3+ | excellent | good | precision | good | 0.0311 | 0.291 | no | Kf5 | - | +4.38 | +4.39 |
| 185209623352 | 67 | 34. Kc2 | great | best | precision | best | 0.0000 | 0.730 | yes | Kc2 | - | +4.38 | +4.63 |
| 185209623352 | 75 | 38. Kc1 | excellent | good | precision | good | 0.0366 | 0.676 | no | Kd3 | - | +2.98 | +2.43 |
| 185209623352 | 77 | 39. Kb1 | inaccuracy | good | precision | good | 0.0302 | 0.641 | no | g4 | g4 | +1.67 | +1.66 |
| 185209623352 | 79 | 40. Kc1 | great | best | precision | best | 0.0000 | 0.620 | yes | Kc1 | - | +2.15 | +2.41 |
| 185209623352 | 82 | 41... Kf7 | mistake | inaccuracy | precision | inaccuracy | 0.0857 | 0.270 | no | Kd5 | - | +6.01 | +6.31 |
| 185209623352 | 85 | 43. Rh3 | miss | mistake | precision | mistake | 0.1701 | 0.667 | no | Rhxe7 | Rhxe7 | -0.08 | -0.10 |
| 185209623352 | 88 | 44... Kxf5 | blunder | mistake | precision | mistake | 0.1963 | 0.501 | no | Kf7 | - | +3.73 | +3.26 |
| 185209623352 | 89 | 45. Rf1+ | great | best | precision | best | 0.0000 | 0.676 | yes | Rf1+ | - | +3.73 | +3.49 |
| 185209623352 | 93 | 47. Kxb2 | great | best | precision | best | 0.0000 | 0.767 | yes | Kxb2 | - | +5.17 | +5.33 |
| 185209623352 | 94 | 47... e5 | good | excellent | precision | excellent | 0.0141 | 0.231 | no | Bxf4 | - | +5.65 | +5.75 |
| 185209623352 | 98 | 49... Kg5 | good | excellent | precision | excellent | 0.0015 | 0.203 | no | b5 | - | +6.38 | +6.33 |
| 185209623352 | 101 | 51. Rb4 | excellent | best | precision | best | 0.0000 | 0.808 | yes | Rb4 | - | +6.27 | +6.30 |
| 185209623352 | 103 | 52. Rb7 | best | excellent | precision | excellent | 0.0007 | 0.808 | no | Rc7 | - | +6.33 | +6.54 |
| 185209623352 | 104 | 52... Kf5 | best | excellent | precision | excellent | 0.0027 | 0.186 | no | Bd8 | - | +6.33 | +6.47 |
| 185209623352 | 105 | 53. R7xb5 | excellent | best | precision | best | 0.0000 | 0.812 | yes | R7xb5 | - | +6.30 | +6.66 |
| 185209623352 | 107 | 54. h4 | best | excellent | precision | excellent | 0.0117 | 0.819 | no | Rc4 | - | +6.59 | +6.71 |
| 185209623352 | 111 | 56. Rbxe5 | best | excellent | precision | excellent | 0.0048 | 0.818 | no | Rb6 | - | +6.54 | +6.77 |
| 185209623352 | 114 | 57... Kf6 | excellent | best | precision | best | 0.0000 | 0.129 | yes | Kf6 | - | +7.19 | +8.34 |
| 185209623352 | 116 | 58... Ke6 | inaccuracy | excellent | precision | excellent | 0.0129 | 0.083 | no | Ke7 | Ke7 | +10.6 | +11.15 |
| 185209623352 | 121 | 61. Rg4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg8 | - | M8 | +12.25 |
| 185209623352 | 126 | 63... Kf7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke7 | - | M5 | M11 |
| 185209623352 | 129 | 65. Qh6+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rg5 | - | M3 | M6 |
| 185209623352 | 130 | 65... Kf5 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf5 | - | M2 | M2 |
| 185209623352 | 134 | 67... Kd4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kd5 | - | M2 | M2 |
| 185209623352 | 143 | 72. g5 | excellent | best | precision | best | 0.0000 | 1.000 | yes | g5 | - | M9 | M9 |
| 185209623352 | 146 | 73... Kb4 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Ka6 | - | M5 | M6 |
| 185324357184 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0028 | 0.554 | no | O-O | - | -1.29 | -1.17 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0089 | 0.294 | no | d4 | - | -4.03 | -4.09 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0464 | 0.598 | no | Ng3 | Ng3 | -0.98 | -0.88 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0827 | 0.585 | no | Na6 | - | +0.29 | +0.28 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.516 | yes | Qg1 | - | +0.29 | +0.15 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | precision | mistake | 0.1670 | 0.569 | no | Qxg3+ | Qxg3+ | +2.48 | +2.59 |
| 185324357184 | 37 | 19. Re1 | great | best | precision | best | 0.0000 | 0.672 | yes | Re1 | - | +3.07 | +2.85 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0317 | 0.343 | no | Qh5 | - | +3.38 | +3.51 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0034 | 0.513 | no | Rh2 | - | +0.11 | +0.03 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.513 | no | b3 | - | +0.26 | +0.40 |
| 185324357184 | 52 | 26... a5 | good | excellent | precision | excellent | 0.0080 | 0.544 | no | h6 | - | -0.29 | -0.17 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0244 | 0.550 | no | d4 | - | +0.65 | +0.50 |
| 185436488062 | 9 | 5. Nxe5 | brilliant | best | precision | best | 0.0000 | 0.612 | yes | Nxe5 | - | +1.74 | +1.97 |
| 185437323918 | 13 | 7. Bd5 | excellent | good | precision | good | 0.0331 | 0.315 | no | Nh7+ | - | -3.51 | -4.01 |
| 185437323918 | 15 | 8. Qf3 | mistake | inaccuracy | precision | inaccuracy | 0.0808 | 0.295 | no | c3 | d3 | -5.55 | -5.95 |
| 185437323918 | 18 | 9... Nxd5 | good | excellent | precision | excellent | 0.0080 | 0.797 | no | g4 | - | -5.16 | -5.46 |
| 185437323918 | 20 | 10... d6 | excellent | good | precision | good | 0.0206 | 0.799 | no | g4 | - | -4.94 | -4.80 |
| 185437323918 | 23 | 12. Qg3 | mistake | inaccuracy | precision | inaccuracy | 0.0641 | 0.220 | no | Qe3 | - | -6.88 | -6.71 |
| 185437323918 | 33 | 17. bxc3 | good | best | precision | best | 0.0000 | 0.196 | yes | bxc3 | - | -6.58 | -6.37 |
| 185437323918 | 34 | 17... Qe7 | best | excellent | precision | excellent | 0.0000 | 0.815 | no | Rxh2+ | - | -6.58 | -6.48 |
| 185437323918 | 38 | 19... Qxg3 | best | excellent | precision | excellent | 0.0000 | 0.798 | no | Qe2 | - | -5.96 | -5.97 |
| 185437323918 | 42 | 21... gxf3 | brilliant | good | precision | good | 0.0401 | 0.749 | no | Qf4 | - | -3.59 | -3.86 |
| 185437323918 | 43 | 22. Rxf3 | miss | inaccuracy | precision | inaccuracy | 0.0933 | 0.289 | no | hxg3 | hxg3 | -5.85 | -6.02 |
| 185437323918 | 52 | 26... Kh6 | good | excellent | precision | excellent | 0.0163 | 0.774 | no | b6 | - | -4.41 | -4.93 |
| 185437323918 | 56 | 28... Bb4 | excellent | good | precision | good | 0.0310 | 0.672 | no | Bc2 | - | -2.41 | -2.79 |
| 185437323918 | 58 | 29... Be4 | great | best | precision | best | 0.0000 | 0.798 | yes | Be4 | - | -5.61 | -6.12 |
| 185437323918 | 65 | 33. Rg3+ | excellent | best | precision | best | 0.0000 | 0.211 | yes | Rg3+ | - | -5.91 | -6.04 |
| 185437323918 | 66 | 33... Kh4 | good | excellent | precision | excellent | 0.0140 | 0.803 | no | Kf5 | - | -5.11 | -5.84 |
| 185437323918 | 67 | 34. Kh2 | inaccuracy | best | precision | best | 0.0000 | 0.204 | yes | Kh2 | Kg2 | -6.13 | -6.15 |
| 185437323918 | 68 | 34... Bxa5 | inaccuracy | good | precision | good | 0.0364 | 0.807 | no | e4 | e4 | -5.01 | -5.01 |
| 185437323918 | 74 | 37... Rf8+ | best | excellent | precision | excellent | 0.0194 | 0.805 | no | Bb4 | - | -6.12 | -6.39 |
| 185437323918 | 75 | 38. Ke4 | best | good | precision | good | 0.0310 | 0.184 | no | Ke2 | - | -6.12 | -6.33 |
| 185437323918 | 76 | 38... Rf4+ | best | good | precision | good | 0.0210 | 0.814 | no | Bc3 | - | -6.12 | -6.94 |
| 185437323918 | 81 | 41. Ke6 | good | excellent | precision | excellent | 0.0031 | 0.158 | no | d6 | - | -7.11 | -7.49 |
| 185437323918 | 83 | 42. Kd7 | excellent | good | precision | good | 0.0208 | 0.122 | no | Ke5 | - | -7.28 | -8.19 |
| 185437323918 | 84 | 42... a4 | best | excellent | precision | excellent | 0.0051 | 0.871 | no | Bb4 | - | -7.28 | -8.41 |
| 185437323918 | 85 | 43. Kxc7 | good | best | precision | best | 0.0000 | 0.123 | yes | Kxc7 | - | -8.05 | -8.68 |
| 185437323918 | 86 | 43... a3 | best | excellent | precision | excellent | 0.0012 | 0.883 | no | Bg3+ | - | -8.05 | -9.10 |
| 185437323918 | 87 | 44. d6 | excellent | best | precision | best | 0.0000 | 0.107 | yes | d6 | - | -8.99 | -9.08 |
| 185437323918 | 94 | 47... Qb2+ | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qb2+ | - | -9.07 | -M19 |
| 185437323918 | 95 | 48. Kc6 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kc6 | Ka6 | -M17 | -M20 |
| 185437323918 | 96 | 48... Qb8 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Qd4 | - | -M16 | -12.43 |
| 185437323918 | 99 | 50. c6 | excellent | best | precision | best | 0.0000 | 0.038 | no | Kd4 | - | -10.7 | -12.77 |
| 185437323918 | 100 | 50... Qb5+ | best | excellent | precision | excellent | 0.0080 | 0.952 | no | Qb3+ | - | -10.7 | -12.88 |
| 185437323918 | 101 | 51. Ke6 | good | excellent | precision | excellent | 0.0082 | 0.047 | no | Kd4 | - | -M6 | -M13 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2073 | 0.207 | no | hxg3 | hxg3 | -M2 | -M2 |
| 185438707002 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0154 | 0.511 | no | Nf3 | - | -0.01 | +0.04 |
| 185438707002 | 10 | 5... h6 | book | best | precision | best | 0.0000 | 0.498 | yes | h6 | - | -0.01 | -0.07 |
| 185438707002 | 11 | 6. Bh4 | book | best | precision | best | 0.0000 | 0.496 | yes | Bh4 | - | -0.01 | -0.02 |
| 185438707002 | 33 | 17. c3 | great | best | precision | best | 0.0000 | 0.589 | yes | c3 | - | +1.35 | +1.31 |
| 185438707002 | 34 | 17... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0730 | 0.423 | no | Bb6 | - | +2.65 | +2.85 |
| 185438707002 | 45 | 23. Rxd4 | excellent | best | precision | best | 0.0000 | 0.724 | yes | Rxd4 | - | +3.82 | +3.88 |
| 185438707002 | 48 | 24... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0513 | 0.296 | no | Rg8 | - | +4.87 | +4.95 |
| 185438707002 | 49 | 25. Qf5+ | inaccuracy | good | precision | good | 0.0354 | 0.764 | no | Qf6 | Qf6 | +3.70 | +4.06 |
| 185438707002 | 52 | 26... a6 | excellent | best | precision | best | 0.0000 | 0.293 | yes | a6 | - | +3.78 | +3.80 |
| 185438707002 | 53 | 27. Qf6 | best | excellent | precision | excellent | 0.0005 | 0.711 | no | Qf3 | - | +3.78 | +3.79 |
| 185438707002 | 54 | 27... Rf8 | mistake | inaccuracy | precision | inaccuracy | 0.0995 | 0.289 | no | Rh5 | Rh7 | +5.73 | +6.40 |
| 185438707002 | 55 | 28. Rd8+ | miss | inaccuracy | precision | inaccuracy | 0.0999 | 0.820 | no | Qxf8+ | Qxf8+ | +3.74 | +4.00 |
| 185438707002 | 57 | 29. Qxd8+ | excellent | best | precision | best | 0.0000 | 0.728 | yes | Qxd8+ | - | +3.69 | +3.97 |
| 185438707002 | 63 | 32. b4 | good | excellent | precision | excellent | 0.0124 | 0.656 | no | Rd2 | - | +1.87 | +1.72 |
| 185438707002 | 65 | 33. Rd5 | excellent | good | precision | good | 0.0219 | 0.649 | no | Rd8 | - | +1.84 | +2.23 |
| 185438707002 | 68 | 34... Qb2+ | great | best | precision | best | 0.0000 | 0.711 | yes | Qb2+ | - | -3.65 | -3.92 |
| 185438707002 | 75 | 38. Kg1 | best | excellent | precision | excellent | 0.0019 | 0.287 | no | f3 | - | -3.38 | -3.91 |
| 185438707002 | 76 | 38... Qd1+ | good | inaccuracy | precision | inaccuracy | 0.0612 | 0.717 | no | b6 | - | -2.61 | -3.10 |
| 185438707002 | 78 | 39... Qd5 | excellent | good | precision | good | 0.0385 | 0.675 | no | Qc2 | - | -2.36 | -2.54 |
| 185438707002 | 86 | 43... Qf7 | best | excellent | precision | excellent | 0.0000 | 0.879 | no | Qd1 | - | -8.73 | -8.64 |
| 185438707002 | 87 | 44. g4 | excellent | best | precision | best | 0.0000 | 0.114 | yes | g4 | - | -8.80 | -8.28 |
| 185438707002 | 89 | 45. g3 | inaccuracy | good | precision | good | 0.0449 | 0.104 | no | g5 | g5 | -M7 | -M10 |
| 185438707002 | 91 | 46. Kh4 | best | mistake | precision | mistake | 0.1103 | 0.110 | no | g5 | - | -M6 | -M6 |
| 185456088510 | 4 | 2... h6 | mistake | inaccuracy | precision | inaccuracy | 0.0561 | 0.395 | no | e6 | e6 | +1.09 | +0.97 |
| 185456088510 | 5 | 3. Bd3 | good | excellent | precision | excellent | 0.0146 | 0.650 | no | Nc3 | - | +0.96 | +0.84 |
| 185456088510 | 6 | 3... e6 | excellent | good | precision | good | 0.0363 | 0.369 | no | d6 | - | +1.01 | +0.99 |
| 185456088510 | 8 | 4... d6 | best | excellent | precision | excellent | 0.0071 | 0.334 | no | d5 | - | +1.01 | +1.15 |
| 185456088510 | 12 | 6... b6 | inaccuracy | good | precision | good | 0.0417 | 0.343 | no | Ne7 | Bg7 | +1.25 | +1.29 |
| 185456088510 | 15 | 8. Be3 | good | excellent | precision | excellent | 0.0030 | 0.631 | no | Qe2 | - | +0.81 | +0.75 |
| 185456088510 | 16 | 8... Nd7 | best | excellent | precision | excellent | 0.0045 | 0.383 | no | Bg7 | - | +0.81 | +0.98 |
| 185456088510 | 19 | 10. Ng3 | great | best | precision | best | 0.0000 | 0.614 | yes | Ng3 | - | +0.65 | +0.66 |
| 185456088510 | 20 | 10... Ng4 | excellent | good | precision | good | 0.0241 | 0.396 | no | h5 | - | +0.74 | +0.89 |
| 185456088510 | 21 | 11. Bd2 | excellent | best | precision | best | 0.0000 | 0.638 | yes | Bd2 | - | +0.70 | +0.77 |
| 185456088510 | 25 | 13. h5 | great | best | precision | best | 0.0000 | 0.680 | yes | h5 | - | +1.12 | +1.18 |
| 185456088510 | 31 | 16. exd6 | excellent | best | precision | best | 0.0000 | 0.748 | yes | exd6 | - | +1.55 | +1.32 |
| 185456088510 | 34 | 17... Qe7 | miss | mistake | precision | mistake | 0.1797 | 0.375 | no | Bxe4 | Bxe4 | +1.83 | +2.30 |
| 185456088510 | 37 | 19. dxc5 | excellent | good | precision | good | 0.0450 | 0.821 | no | Nh4 | - | +1.72 | +1.79 |
| 185456088510 | 46 | 23... Rhf8 | good | inaccuracy | precision | inaccuracy | 0.0801 | 0.165 | no | Rd6 | - | +2.89 | +3.05 |
| 185456088510 | 47 | 24. b4 | best | excellent | precision | excellent | 0.0035 | 0.875 | no | a5 | - | +2.89 | +3.36 |
| 185456088510 | 54 | 27... e4 | inaccuracy | mistake | precision | mistake | 0.1043 | 0.178 | no | Rc6 | - | +2.96 | +3.49 |
| 185456088510 | 56 | 28... Nxe3 | great | best | precision | best | 0.0000 | 0.927 | yes | Nxe3 | - | -4.25 | -5.02 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0185 | 0.462 | no | Na4 | - | -0.94 | -1.10 |
| 185468039834 | 14 | 7... h6 | good | excellent | precision | excellent | 0.0116 | 0.488 | no | Ne5 | - | +0.60 | +0.50 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0415 | 0.474 | no | Kf8 | - | +0.61 | +0.91 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0254 | 0.428 | no | dxe5 | dxe5 | +1.53 | +1.54 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.589 | yes | Qh5 | - | +1.48 | +1.58 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1714 | 0.622 | no | Nxc7+ | Nxc7+ | -0.91 | -1.42 |
| 185468039834 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.582 | yes | c6 | - | -0.83 | -1.10 |
| 185468039834 | 25 | 13. Nf6+ | good | excellent | precision | excellent | 0.0131 | 0.436 | no | b4 | - | -1.28 | -1.39 |
| 185468039834 | 27 | 14. Bxe6 | best | excellent | precision | excellent | 0.0085 | 0.420 | no | b3 | - | -1.28 | -1.44 |
| 185468039834 | 29 | 15. Rab1 | mistake | inaccuracy | precision | inaccuracy | 0.0929 | 0.402 | no | b4 | - | -3.36 | -3.49 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.693 | yes | Rf8 | - | -3.36 | -3.55 |
| 185468039834 | 32 | 16... Rxf6 | excellent | best | precision | best | 0.0000 | 0.695 | yes | Rxf6 | - | -3.39 | -3.58 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0005 | 0.303 | no | Qg3 | - | -3.39 | -3.70 |
| 185468614210 | 9 | 5. d4 | book | excellent | precision | excellent | 0.0117 | 0.514 | no | b4 | - | +0.15 | +0.09 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.495 | yes | exd4 | - | +0.15 | +0.07 |
| 185468614210 | 11 | 6. cxd4 | book | excellent | precision | excellent | 0.0053 | 0.504 | no | e5 | - | 0.00 | -0.06 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.504 | yes | Bb4+ | - | 0.00 | +0.07 |
| 185468614210 | 13 | 7. Nc3 | book | excellent | precision | excellent | 0.0181 | 0.504 | no | Bd2 | - | -0.35 | -0.42 |
| 185468614210 | 25 | 13. Bd3 | good | excellent | precision | excellent | 0.0180 | 0.485 | no | Bxd6 | - | -0.61 | -0.56 |
| 185468614210 | 28 | 14... Nxd5 | excellent | best | precision | best | 0.0000 | 0.488 | yes | Nxd5 | - | +0.25 | +0.18 |
| 185468614210 | 31 | 16. Qxd5 | best | excellent | precision | excellent | 0.0012 | 0.508 | no | Ng5+ | - | +0.25 | +0.24 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0343 | 0.486 | no | Kg8 | Kg8 | +1.21 | +0.78 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0326 | 0.545 | no | Qh5+ | Qh5+ | +0.18 | +0.20 |
| 185468614210 | 34 | 17... Kg8 | great | best | precision | best | 0.0000 | 0.488 | yes | Kg8 | - | +0.18 | +0.13 |
| 185468614210 | 38 | 19... Qf6 | good | excellent | precision | excellent | 0.0152 | 0.519 | no | b6 | - | -0.09 | -0.08 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0162 | 0.553 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.460 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.537 | yes | Nc3 | - | +0.74 | +0.67 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.461 | yes | e6 | - | +0.74 | +0.68 |
| 185475865432 | 7 | 4. Bc4 | good | excellent | precision | excellent | 0.0197 | 0.540 | no | d4 | - | +0.22 | +0.17 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0150 | 0.467 | no | Bb4 | - | +0.55 | +0.70 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0859 | 0.557 | no | Ng3 | Ng3 | -0.76 | -0.65 |
| 185475865432 | 25 | 13. Ne5 | best | excellent | precision | excellent | 0.0034 | 0.414 | no | c3 | - | -1.49 | -1.60 |
| 185475865432 | 26 | 13... Nc6 | good | excellent | precision | excellent | 0.0198 | 0.592 | no | O-O | - | -1.07 | -1.30 |
| 185475865432 | 27 | 14. Ng3 | inaccuracy | good | precision | good | 0.0497 | 0.425 | no | Qxd8+ | Qxd8+ | -1.91 | -1.97 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0342 | 0.613 | no | Qxd1 | Qxd1 | -1.24 | -1.16 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0141 | 0.598 | no | Bd6 | - | -1.25 | -1.48 |
| 185475865432 | 33 | 17. Qxd8+ | good | excellent | precision | excellent | 0.0168 | 0.415 | no | Qh5 | - | -1.78 | -1.93 |
| 185475865432 | 37 | 19. Rad1 | excellent | best | precision | best | 0.0000 | 0.592 | yes | Rad1 | - | +1.50 | +1.68 |
| 185475865432 | 44 | 22... Rc8 | excellent | best | precision | best | 0.0000 | 0.411 | yes | Rc8 | - | +1.57 | +1.73 |
| 185475865432 | 49 | 25. a6 | mistake | good | precision | good | 0.0280 | 0.680 | no | Rxe6 | Rxe6 | +1.47 | +1.74 |
| 185475865432 | 51 | 26. a7 | excellent | best | precision | best | 0.0000 | 0.730 | yes | a7 | - | +3.79 | +3.91 |
| 185962590893 | 8 | 4... Qc7 | inaccuracy | mistake | precision | mistake | 0.1024 | 0.478 | no | Qxd1+ | Qxd1+ | +0.72 | +0.76 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0522 | 0.619 | no | Bc4 | - | +0.50 | +0.45 |
| 185962590893 | 10 | 5... Bg4 | good | inaccuracy | precision | inaccuracy | 0.0505 | 0.429 | no | Nd7 | - | +0.80 | +0.70 |
| 185962590893 | 14 | 7... Nd7 | best | excellent | precision | excellent | 0.0060 | 0.377 | no | Nf6 | - | +0.82 | +0.77 |
| 185962590893 | 15 | 8. Nc4 | inaccuracy | good | precision | good | 0.0459 | 0.620 | no | a4 | - | +0.40 | +0.40 |
| 185962590893 | 16 | 8... Ngf6 | inaccuracy | good | precision | good | 0.0463 | 0.437 | no | b5 | b5 | +0.82 | +0.79 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.424 | yes | e5 | - | +0.67 | +0.59 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.432 | yes | Be7 | - | +0.55 | +0.48 |
| 185962590893 | 22 | 11... b5 | inaccuracy | mistake | precision | mistake | 0.1144 | 0.434 | no | O-O | O-O | +0.92 | +1.04 |
| 185962590893 | 25 | 13. Nf5 | excellent | best | precision | best | 0.0000 | 0.579 | yes | Nf5 | - | +0.64 | +0.52 |
| 185962590893 | 27 | 14. Nxe7+ | miss | good | precision | good | 0.0465 | 0.752 | no | Bh6 | Bh6 | +1.01 | +1.44 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0325 | 0.303 | no | Nf8 | Ne8 | +1.62 | +1.61 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0734 | 0.736 | no | Rxd8+ | Rxd8+ | +0.96 | +1.01 |
| 185962590893 | 35 | 18. g5 | best | good | precision | good | 0.0263 | 0.656 | no | Rxd7 | - | +0.96 | +0.87 |
| 185962590893 | 40 | 20... Nfd7 | best | good | precision | good | 0.0252 | 0.380 | no | Ne8 | - | +0.96 | +1.12 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.634 | yes | Qe3 | Qf3 | +0.47 | +0.78 |
| 185962590893 | 52 | 26... Nd4 | mistake | good | precision | good | 0.0424 | 0.378 | no | Nf4 | Nf4 | +1.15 | +1.23 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2482 | 0.686 | no | f4 | - | -0.39 | -0.56 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | b4 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `miss_detector` (6)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (tactic) | miss_detector | mistake | 0.1483 | 0.652 | no | g4 | - | -0.01 | +0.12 |
| 185209623352 | 83 | 42. Rh7+ | mistake | miss (free_piece) | miss_detector | mistake | 0.1656 | 0.806 | no | Rxf6+ | Rxf6+ | +2.74 | +2.69 |
| 185209623352 | 91 | 46. Rf4 | blunder | miss (free_piece) | miss_detector | blunder | 0.4327 | 0.776 | no | Rxf6+ | - | -2.81 | -2.68 |
| 185437323918 | 48 | 24... Re8 | blunder | miss (opportunity) | miss_detector | blunder | 0.2166 | 0.717 | no | Kg7 | - | -0.17 | -0.09 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2027 | 0.203 | no | Kd2 | - | -M1 | -M1 |
| 185456088510 | 33 | 17. Ne4 | mistake | miss (tactic) | miss_detector | mistake | 0.1853 | 0.752 | no | Qe2 | Qe2 | +0.65 | +0.80 |

### `mate_override` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 131 | 66. Qg6+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kd3 | - | M3 | M7 |
| 185209623352 | 142 | 71... Kb5 | good | inaccuracy | mate_override | inaccuracy | 0.0446 | 0.045 | no | Ka7 | - | M8 | M11 |
| 185437323918 | 97 | 49. Kd5 | best | inaccuracy | mate_override | inaccuracy | 0.0523 | 0.052 | no | d8=Q | - | -M16 | -M18 |
| 185437323918 | 98 | 49... Qb7+ | good | miss (mate) | mate_override | mistake | 0.1177 | 1.000 | no | Qe5+ | - | -8.99 | -13.81 |
| 185437323918 | 107 | 54. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf6 | - | -M1 | -M1 |

### `great_find_event` (4)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 41 | 21. Bxh8 | best | great | great_find_event | best | 0.0000 | 0.249 | yes | Bxh8 | - | -4.32 | -4.68 |
| 185437323918 | 45 | 23. Bxe5 | best | great | great_find_event | best | 0.0000 | 0.502 | yes | Bxe5 | - | +0.18 | -0.08 |
| 185438343298 | 15 | 8. g3 | best | great | great_find_event | best | 0.0000 | 0.202 | yes | g3 | - | -5.11 | -5.63 |
| 185438707002 | 84 | 42... Nxg3 | best | great | great_find_event | best | 0.0000 | 0.849 | yes | Nxg3 | - | -7.11 | -7.07 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185209623352 | 4 | 2... c6 | excellent | book | book | excellent | 0.0050 | 0.459 | no | Nf6 | - | +0.82 | +1.00 |
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | good | 0.0472 | 0.525 | no | d4 | Nxe5 | -0.62 | -0.38 |

### `losing_material_hardened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185437323918 | 59 | 30. g5+ | good | mistake | losing_material_hardened | excellent | 0.0050 | 0.194 | no | Rg3 | - | -6.55 | -6.66 |
| 185437323918 | 89 | 45. c5 | excellent | mistake | losing_material_hardened | good | 0.0251 | 0.104 | no | Kd7 | - | -8.94 | -8.54 |

### `blunder_softened` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2058 | 0.902 | no | Qxg2 | Qxg2 | -0.96 | -1.06 |

