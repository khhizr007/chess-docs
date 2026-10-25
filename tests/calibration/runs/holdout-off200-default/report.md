# Calibration report: holdout-off200-default

- Generated: 2026-10-18T08:30:11+00:00
- Commit: `52ae25250d63` + uncommitted backend changes (diff sha256 `0e2424872283`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 6 requested, 6 compared, 0 skipped (list: `tests/calibration/holdout.txt`)
- Plies: 310 aligned, 310 scored, 0 excluded (none)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 67.4% (209/310) |
| Within one step | 85.2% (264/310) |
| Brilliant precision / recall | - / 0.00 |
| Great precision / recall | 0.50 / 0.10 |
| Brilliant per 100 moves (app / ours) | 0.32 / 0.00 |
| Great per 100 moves (app / ours) | 3.23 / 0.65 |
| Accuracy mean abs. difference | 2.74 (n=12, max 5.77) |
| Accuracy bias (ours - app) | +0.92 |
| Best move = app's suggestion | 89.2% (33/37 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | . | . | 1 | . | . | . | . | . | . | . | 1 |
| **great** | . | **1** | 9 | . | . | . | . | . | . | . | 10 |
| **best** | . | 1 | **75** | 13 | 3 | . | . | . | . | . | 92 |
| **excellent** | . | . | 13 | **26** | 8 | . | 1 | 1 | . | . | 49 |
| **good** | . | . | 3 | 8 | **23** | . | 1 | 1 | . | . | 36 |
| **book** | . | . | 7 | 6 | . | **40** | . | . | . | . | 53 |
| **inaccuracy** | . | . | . | 2 | 6 | . | **15** | 3 | . | . | 26 |
| **mistake** | . | . | 1 | 2 | . | . | 1 | **16** | 3 | . | 23 |
| **miss** | . | . | . | . | . | . | 1 | 1 | **7** | 1 | 10 |
| **blunder** | . | . | . | . | . | . | . | 2 | 2 | **6** | 10 |
| **total** | 0 | 2 | 109 | 57 | 40 | 40 | 19 | 24 | 12 | 7 | 310 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 1 | 0 | 0 | - | 0.000 | - |
| great | 10 | 2 | 1 | 0.500 | 0.100 | 0.167 |
| best | 92 | 109 | 75 | 0.688 | 0.815 | 0.746 |
| excellent | 49 | 57 | 26 | 0.456 | 0.531 | 0.491 |
| good | 36 | 40 | 23 | 0.575 | 0.639 | 0.605 |
| book | 53 | 40 | 40 | 1.000 | 0.755 | 0.860 |
| inaccuracy | 26 | 19 | 15 | 0.789 | 0.577 | 0.667 |
| mistake | 23 | 24 | 16 | 0.667 | 0.696 | 0.681 |
| miss | 10 | 12 | 7 | 0.583 | 0.700 | 0.636 |
| blunder | 10 | 7 | 6 | 0.857 | 0.600 | 0.706 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 185387411150 | white | 77.9 | 78.3 | +0.4 |
| 185387411150 | black | 75.5 | 76.3 | +0.8 |
| 185425961522 | white | 58.9 | 63.3 | +4.4 |
| 185425961522 | black | 55.0 | 58.9 | +3.9 |
| 185439816356 | white | 59.1 | 61.4 | +2.3 |
| 185439816356 | black | 81.9 | 83.7 | +1.8 |
| 185466827454 | white | 73.1 | 77.1 | +4.0 |
| 185466827454 | black | 77.5 | 76.7 | -0.8 |
| 185476493194 | white | 61.7 | 57.3 | -4.4 |
| 185476493194 | black | 56.1 | 50.3 | -5.8 |
| 994221268 | white | 87.7 | 89.8 | +2.1 |
| 994221268 | black | 93.4 | 95.7 | +2.3 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 185387411150 | 57 | 57 | 64.9% | 75.4% | reviewed | 48.3 |
| 185425961522 | 47 | 47 | 76.6% | 91.5% | reviewed | 49.3 |
| 185439816356 | 15 | 15 | 93.3% | 100.0% | reviewed | 23.1 |
| 185466827454 | 62 | 62 | 61.3% | 83.9% | reviewed | 47.8 |
| 185476493194 | 43 | 43 | 62.8% | 76.7% | reviewed | 29.1 |
| 994221268 | 86 | 86 | 66.3% | 90.7% | reviewed | 53.3 |

## Mismatches by rule (101)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 93 | best -> excellent x13, excellent -> best x13, great -> best x9, good -> excellent x8, excellent -> good x8, book -> best x7 |
| `miss_detector` | 5 | mistake -> miss x3, blunder -> miss x2 |
| `losing_material_hardened` | 2 | excellent -> mistake x1, good -> mistake x1 |
| `great_find_event` | 1 | best -> great x1 |

### `precision` (93)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185387411150 | 7 | 4. Bd3 | book | excellent | precision | excellent | 0.0090 | 0.528 | no | Nf3 | - | +0.19 | +0.27 |
| 185387411150 | 8 | 4... Bxd3 | book | best | precision | best | 0.0000 | 0.481 | yes | Bxd3 | - | +0.19 | +0.17 |
| 185387411150 | 9 | 5. Qxd3 | book | excellent | precision | excellent | 0.0021 | 0.512 | no | cxd3 | - | +0.19 | +0.22 |
| 185387411150 | 11 | 6. Nf3 | best | excellent | precision | excellent | 0.0007 | 0.584 | no | Nc3 | - | +1.27 | +1.32 |
| 185387411150 | 13 | 7. Nxe5 | best | excellent | precision | excellent | 0.0093 | 0.600 | no | dxe5 | - | +1.47 | +1.36 |
| 185387411150 | 16 | 8... Nd7 | excellent | best | precision | best | 0.0000 | 0.470 | yes | Nd7 | - | +0.63 | +0.44 |
| 185387411150 | 27 | 14. exf6 | great | best | precision | best | 0.0000 | 0.763 | yes | exf6 | - | +3.75 | +4.05 |
| 185387411150 | 32 | 16... Bb4 | good | excellent | precision | excellent | 0.0122 | 0.185 | no | gxf6 | - | +5.56 | +5.46 |
| 185387411150 | 35 | 18. fxg7 | great | best | precision | best | 0.0000 | 0.911 | yes | fxg7 | - | +8.32 | +8.43 |
| 185387411150 | 36 | 18... Rg8 | mistake | excellent | precision | excellent | 0.0103 | 0.088 | no | Rhd8 | - | +8.79 | +8.92 |
| 185387411150 | 39 | 20. Bg3+ | best | good | precision | good | 0.0289 | 0.931 | no | Qxg8 | - | +8.79 | +8.88 |
| 185387411150 | 40 | 20... Bd6 | best | excellent | precision | excellent | 0.0014 | 0.079 | no | Kb6 | - | +8.79 | +8.83 |
| 185387411150 | 41 | 21. Qf7+ | best | excellent | precision | excellent | 0.0065 | 0.920 | no | Qxg8 | - | +8.79 | +7.90 |
| 185387411150 | 46 | 23... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 50 | 25... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 52 | 26... Qh5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qh5+ | - | 0.00 | +0.00 |
| 185387411150 | 54 | 27... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 56 | 28... Qh5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qh5+ | - | 0.00 | +0.00 |
| 185425961522 | 12 | 6... Qe6 | mistake | inaccuracy | precision | inaccuracy | 0.0739 | 0.448 | no | Qb6 | - | +1.82 | +1.80 |
| 185425961522 | 17 | 9. Qf4 | miss | inaccuracy | precision | inaccuracy | 0.0745 | 0.730 | no | Nc3 | Nc3 | +1.74 | +2.25 |
| 185425961522 | 18 | 9... Qg6 | inaccuracy | good | precision | good | 0.0315 | 0.345 | no | Nh6 | Nh6 | +2.52 | +2.86 |
| 185425961522 | 21 | 11. Bxd5 | miss | mistake | precision | mistake | 0.1283 | 0.737 | no | Nb5 | Nb5 | +0.90 | +1.50 |
| 185425961522 | 22 | 11... Be6 | blunder | mistake | precision | mistake | 0.1888 | 0.394 | no | c6 | - | +4.41 | +4.73 |
| 185425961522 | 24 | 12... Rd8 | best | good | precision | good | 0.0277 | 0.226 | no | Rb8 | - | +4.41 | +5.07 |
| 185425961522 | 29 | 15. Bxa7 | inaccuracy | mistake | precision | mistake | 0.1037 | 0.828 | no | Rac1 | Qa4+ | +3.25 | +3.38 |
| 185425961522 | 34 | 17... Ne7 | excellent | good | precision | good | 0.0217 | 0.266 | no | Qa6 | - | +3.65 | +3.70 |
| 185425961522 | 35 | 18. Bxc7 | inaccuracy | mistake | precision | mistake | 0.1103 | 0.742 | no | Nb5 | Nb5 | +1.98 | +1.89 |
| 185425961522 | 47 | 24. d7 | best | excellent | precision | excellent | 0.0042 | 0.944 | no | Ne7+ | - | +9.38 | +9.61 |
| 185439816356 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0313 | 0.564 | no | d4 | - | +0.65 | +0.50 |
| 185466827454 | 11 | 6. Bd3 | book | best | precision | best | 0.0000 | 0.490 | yes | Bd3 | - | -0.12 | -0.19 |
| 185466827454 | 12 | 6... dxe4 | book | best | precision | best | 0.0000 | 0.514 | yes | dxe4 | - | -0.12 | -0.10 |
| 185466827454 | 13 | 7. Bxe4 | book | best | precision | best | 0.0000 | 0.493 | yes | Bxe4 | - | -0.12 | -0.15 |
| 185466827454 | 15 | 8. c3 | excellent | best | precision | best | 0.0000 | 0.523 | yes | c3 | - | +0.27 | +0.24 |
| 185466827454 | 16 | 8... Be6 | good | excellent | precision | excellent | 0.0073 | 0.482 | no | O-O | - | +0.60 | +0.34 |
| 185466827454 | 17 | 9. d4 | inaccuracy | good | precision | good | 0.0396 | 0.525 | no | O-O | - | -0.20 | -0.20 |
| 185466827454 | 19 | 10. cxd4 | excellent | inaccuracy | precision | inaccuracy | 0.0533 | 0.494 | no | O-O | - | -0.40 | -0.81 |
| 185466827454 | 27 | 14. Bc6+ | good | excellent | precision | excellent | 0.0161 | 0.511 | no | Qa4+ | - | -0.08 | +0.00 |
| 185466827454 | 31 | 16. Qa3+ | inaccuracy | good | precision | good | 0.0440 | 0.610 | no | Rd1 | Rd1 | +0.78 | +0.91 |
| 185466827454 | 35 | 18. f4 | good | excellent | precision | excellent | 0.0181 | 0.563 | no | Qxa7 | - | +0.61 | +0.62 |
| 185466827454 | 36 | 18... Bd6 | good | excellent | precision | excellent | 0.0167 | 0.455 | no | Bf6 | - | +1.11 | +0.81 |
| 185466827454 | 40 | 20... h6 | inaccuracy | good | precision | good | 0.0382 | 0.887 | no | Qa6 | Qa6 | -5.82 | -5.87 |
| 185466827454 | 45 | 23. Kh1 | inaccuracy | good | precision | good | 0.0434 | 0.163 | no | Bxc5 | - | -7.22 | -6.80 |
| 185466827454 | 46 | 23... Rxd1 | best | excellent | precision | excellent | 0.0000 | 0.880 | no | Qxf1+ | - | -7.22 | -7.54 |
| 185466827454 | 49 | 25. Rd8+ | good | excellent | precision | excellent | 0.0177 | 0.094 | no | f5 | - | -8.48 | -8.51 |
| 185466827454 | 52 | 26... Qxf4 | excellent | best | precision | best | 0.0000 | 0.922 | yes | Qxf4 | - | -7.90 | -8.23 |
| 185466827454 | 54 | 27... Bg4 | best | excellent | precision | excellent | 0.0000 | 0.933 | no | Bf5 | - | -8.57 | -9.46 |
| 185466827454 | 55 | 28. Be4+ | excellent | best | precision | best | 0.0000 | 0.059 | yes | Be4+ | - | -9.21 | -10.97 |
| 185466827454 | 56 | 28... g6 | best | good | precision | good | 0.0205 | 0.962 | no | f5 | - | -9.21 | -M13 |
| 185466827454 | 57 | 29. h3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | Bd3 | - | -M7 | -M13 |
| 185466827454 | 59 | 30. Rf1 | good | best | precision | best | 0.0000 | 0.000 | yes | Rf1 | - | -M7 | -M12 |
| 185476493194 | 6 | 3... Bc5 | book | excellent | precision | excellent | 0.0081 | 0.493 | no | c6 | - | +0.21 | +0.17 |
| 185476493194 | 7 | 4. Nf3 | book | best | precision | best | 0.0000 | 0.512 | yes | Nf3 | - | +0.21 | +0.16 |
| 185476493194 | 8 | 4... Nc6 | book | excellent | precision | excellent | 0.0007 | 0.488 | no | d6 | - | +0.26 | +0.20 |
| 185476493194 | 9 | 5. O-O | book | best | precision | best | 0.0000 | 0.515 | yes | O-O | - | +0.26 | +0.21 |
| 185476493194 | 10 | 5... d6 | book | excellent | precision | excellent | 0.0029 | 0.485 | no | a6 | - | +0.27 | +0.18 |
| 185476493194 | 13 | 7. Bg5 | best | excellent | precision | excellent | 0.0029 | 0.515 | no | Na4 | - | +0.21 | +0.01 |
| 185476493194 | 16 | 8... Nd4 | excellent | good | precision | good | 0.0301 | 0.521 | no | Bg4 | - | +0.26 | +0.16 |
| 185476493194 | 17 | 9. Nxd4 | excellent | best | precision | best | 0.0000 | 0.512 | yes | Nxd4 | - | +0.19 | +0.15 |
| 185476493194 | 21 | 11. Qg3 | miss | blunder | precision | blunder | 0.4194 | 0.780 | no | Bxf6 | Bxf6 | -1.97 | -1.70 |
| 185476493194 | 26 | 13... g5 | mistake | best | precision | best | 0.0000 | 0.204 | yes | g5 | - | +5.10 | +5.33 |
| 185476493194 | 32 | 16... Kg7 | best | excellent | precision | excellent | 0.0025 | 0.218 | no | Qd8 | - | +4.16 | +4.43 |
| 185476493194 | 34 | 17... Qe7 | blunder | mistake | precision | mistake | 0.1757 | 0.307 | no | Qd8 | - | +6.88 | +6.43 |
| 185476493194 | 42 | 21... Bg6 | mistake | excellent | precision | excellent | 0.0119 | 0.060 | no | Kh7 | Kh7 | +9.17 | +9.77 |
| 185476493194 | 43 | 22. cxd4 | excellent | good | precision | good | 0.0284 | 0.946 | no | Qxg6+ | - | +8.14 | +8.20 |
| 994221268 | 6 | 3... a6 | book | excellent | precision | excellent | 0.0122 | 0.502 | no | Bf5 | - | +0.10 | +0.13 |
| 994221268 | 7 | 4. e3 | book | best | precision | best | 0.0000 | 0.514 | yes | e3 | - | +0.10 | +0.10 |
| 994221268 | 14 | 7... c5 | excellent | best | precision | best | 0.0000 | 0.520 | yes | c5 | - | -0.20 | -0.16 |
| 994221268 | 16 | 8... Nc6 | best | excellent | precision | excellent | 0.0055 | 0.525 | no | h6 | - | -0.27 | -0.18 |
| 994221268 | 20 | 10... Bd6 | excellent | good | precision | good | 0.0275 | 0.554 | no | b5 | - | -0.34 | -0.32 |
| 994221268 | 25 | 13. N5a4 | great | best | precision | best | 0.0000 | 0.458 | yes | N5a4 | - | -0.45 | -0.32 |
| 994221268 | 32 | 16... exd4 | excellent | best | precision | best | 0.0000 | 0.598 | yes | exd4 | - | -0.93 | -0.87 |
| 994221268 | 36 | 18... Nxd4 | brilliant | best | precision | best | 0.0000 | 0.591 | yes | Nxd4 | - | -0.93 | -0.92 |
| 994221268 | 37 | 19. Rxd4 | excellent | best | precision | best | 0.0000 | 0.400 | yes | Rxd4 | - | -1.05 | -0.99 |
| 994221268 | 39 | 20. Qd1 | good | inaccuracy | precision | inaccuracy | 0.0626 | 0.413 | no | Rd1 | - | -1.27 | -1.39 |
| 994221268 | 43 | 22. Qd2 | good | best | precision | best | 0.0000 | 0.371 | yes | Qd2 | - | -1.37 | -1.32 |
| 994221268 | 45 | 23. Rd1 | best | excellent | precision | excellent | 0.0154 | 0.374 | no | Re1 | - | -1.25 | -1.37 |
| 994221268 | 48 | 24... axb4 | good | excellent | precision | excellent | 0.0148 | 0.616 | no | cxb3 | - | -0.97 | -0.98 |
| 994221268 | 50 | 25... Qxb4 | excellent | best | precision | best | 0.0000 | 0.608 | yes | Qxb4 | - | -0.88 | -1.06 |
| 994221268 | 52 | 26... Qxd2 | great | best | precision | best | 0.0000 | 0.796 | yes | Qxd2 | - | -2.89 | -2.97 |
| 994221268 | 53 | 27. R1xd2 | good | excellent | precision | excellent | 0.0179 | 0.212 | no | R4xd2 | - | -3.25 | -3.46 |
| 994221268 | 54 | 27... b4 | excellent | best | precision | best | 0.0000 | 0.822 | yes | b4 | - | -3.15 | -3.31 |
| 994221268 | 56 | 28... h6 | excellent | good | precision | good | 0.0227 | 0.832 | no | Ne8 | - | -3.21 | -3.23 |
| 994221268 | 57 | 29. h4 | best | excellent | precision | excellent | 0.0167 | 0.193 | no | Rd1 | - | -3.21 | -3.52 |
| 994221268 | 58 | 29... Kf8 | excellent | good | precision | good | 0.0291 | 0.826 | no | Ne8 | - | -3.08 | -3.09 |
| 994221268 | 62 | 31... Nh5 | good | best | precision | best | 0.0000 | 0.793 | yes | Nh5 | - | -2.43 | -3.14 |
| 994221268 | 63 | 32. Kh2 | inaccuracy | good | precision | good | 0.0261 | 0.199 | no | Kg1 | Kg2 | -3.24 | -3.53 |
| 994221268 | 65 | 33. Ng3 | inaccuracy | excellent | precision | excellent | 0.0133 | 0.203 | no | Ng1 | - | -3.37 | -3.46 |
| 994221268 | 68 | 34... Red7 | best | excellent | precision | excellent | 0.0086 | 0.837 | no | Rb7 | - | -3.37 | -3.41 |
| 994221268 | 70 | 35... Rb8 | excellent | good | precision | good | 0.0205 | 0.827 | no | Ke7 | - | -3.17 | -3.22 |
| 994221268 | 71 | 36. Rxd5 | inaccuracy | mistake | precision | mistake | 0.1061 | 0.194 | no | Re2 | Re2 | -4.86 | -5.29 |
| 994221268 | 80 | 40... Ke7 | excellent | best | precision | best | 0.0000 | 0.909 | yes | Ke7 | - | -4.74 | -5.09 |
| 994221268 | 82 | 41... Ke6 | excellent | best | precision | best | 0.0000 | 0.921 | yes | Ke6 | - | -4.68 | -5.40 |
| 994221268 | 84 | 42... Kf5 | excellent | best | precision | best | 0.0000 | 0.927 | yes | Kf5 | - | -4.94 | -5.80 |

### `miss_detector` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185387411150 | 23 | 12. Bh4 | mistake | miss (tactic) | miss_detector | mistake | 0.1290 | 0.776 | no | Qg6+ | Qg6+ | +1.91 | +2.41 |
| 185387411150 | 45 | 23. fxg3 | mistake | miss (tactic) | miss_detector | blunder | 0.4286 | 0.929 | no | Qb3+ | Qb3+ | 0.00 | +0.00 |
| 185425961522 | 38 | 19... Nf4 | blunder | miss (tactic) | miss_detector | blunder | 0.5770 | 0.703 | no | Rd3 | Rd3 | +6.74 | +6.79 |
| 185466827454 | 22 | 11... Bxd4 | mistake | miss (free_piece) | miss_detector | mistake | 0.1045 | 0.611 | no | Qxd4 | Qxd4 | +0.32 | +0.23 |
| 185476493194 | 20 | 10... Bg4 | blunder | miss (tactic) | miss_detector | blunder | 0.5392 | 0.759 | no | g5 | - | +4.08 | +4.31 |

### `losing_material_hardened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185466827454 | 61 | 31. Rxf2 | excellent | mistake | losing_material_hardened | excellent | 0.0000 | 0.043 | no | Ra1 | - | -11.6 | -10.02 |
| 185476493194 | 40 | 20... Rae8 | good | mistake | losing_material_hardened | excellent | 0.0172 | 0.087 | no | Be2 | - | +9.13 | +8.80 |

### `great_find_event` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185466827454 | 32 | 16... Kg8 | best | great | great_find_event | best | 0.0000 | 0.434 | yes | Kg8 | - | +0.78 | +0.82 |

