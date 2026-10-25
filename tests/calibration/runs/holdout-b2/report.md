# Calibration report: holdout-b2

- Generated: 2026-10-18T11:17:49+00:00
- Commit: `27fafb5b0f3b` + uncommitted backend changes (diff sha256 `78d53b3a9776`)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 18 requested, 18 compared, 0 skipped (list: `tests/calibration/holdout.txt`)
- Plies: 1248 aligned, 1248 scored, 0 excluded (none)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 65.7% (820/1248) |
| Within one step | 88.0% (1098/1248) |
| Brilliant precision / recall | 0.50 / 0.33 |
| Great precision / recall | 0.78 / 0.17 |
| Brilliant per 100 moves (app / ours) | 0.24 / 0.16 |
| Great per 100 moves (app / ours) | 3.37 / 0.72 |
| Accuracy mean abs. difference | 3.14 (n=36, max 10.10) |
| Accuracy bias (ours - app) | +1.93 |
| Best move = app's suggestion | 79.4% (170/214 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 2 | . | . | . | . | . | . | . | 3 |
| **great** | . | **7** | 34 | 1 | . | . | . | . | . | . | 42 |
| **best** | 1 | 2 | **351** | 54 | 7 | . | . | . | . | . | 415 |
| **excellent** | . | . | 60 | **95** | 28 | 1 | 3 | 3 | . | . | 190 |
| **good** | . | . | 12 | 41 | **78** | . | 27 | 3 | 4 | . | 165 |
| **book** | . | . | 20 | 10 | 3 | **102** | . | . | . | . | 135 |
| **inaccuracy** | . | . | 3 | 5 | 37 | 1 | **72** | 16 | 2 | . | 136 |
| **mistake** | . | . | 3 | 4 | 1 | . | 10 | **64** | 7 | 2 | 91 |
| **miss** | . | . | . | 1 | 2 | . | 5 | 4 | **29** | 2 | 43 |
| **blunder** | . | . | . | . | . | . | . | 3 | 4 | **21** | 28 |
| **total** | 2 | 9 | 485 | 211 | 156 | 104 | 117 | 93 | 46 | 25 | 1248 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 2 | 1 | 0.500 | 0.333 | 0.400 |
| great | 42 | 9 | 7 | 0.778 | 0.167 | 0.275 |
| best | 415 | 485 | 351 | 0.724 | 0.846 | 0.780 |
| excellent | 190 | 211 | 95 | 0.450 | 0.500 | 0.474 |
| good | 165 | 156 | 78 | 0.500 | 0.473 | 0.486 |
| book | 135 | 104 | 102 | 0.981 | 0.756 | 0.854 |
| inaccuracy | 136 | 117 | 72 | 0.615 | 0.529 | 0.569 |
| mistake | 91 | 93 | 64 | 0.688 | 0.703 | 0.696 |
| miss | 43 | 46 | 29 | 0.630 | 0.674 | 0.652 |
| blunder | 28 | 25 | 21 | 0.840 | 0.750 | 0.792 |

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
| 185476493194 | white | 61.7 | 57.4 | -4.3 |
| 185476493194 | black | 56.1 | 50.4 | -5.7 |
| 994221268 | white | 87.7 | 89.8 | +2.1 |
| 994221268 | black | 93.4 | 95.7 | +2.3 |
| 184740374128 | white | 56.2 | 55.8 | -0.4 |
| 184740374128 | black | 64.2 | 66.0 | +1.8 |
| 185101208706 | white | 52.3 | 49.4 | -2.9 |
| 185101208706 | black | 58.9 | 57.2 | -1.7 |
| 185137444946 | white | 79.0 | 80.2 | +1.2 |
| 185137444946 | black | 65.6 | 69.8 | +4.2 |
| 185151408586 | white | 82.3 | 86.4 | +4.1 |
| 185151408586 | black | 80.6 | 81.9 | +1.3 |
| 185221110711 | white | 78.2 | 85.2 | +7.0 |
| 185221110711 | black | 88.1 | 84.3 | -3.8 |
| 185311691496 | white | 81.4 | 87.4 | +6.0 |
| 185311691496 | black | 64.8 | 67.9 | +3.1 |
| 185344445308 | white | 60.1 | 64.2 | +4.1 |
| 185344445308 | black | 60.5 | 58.2 | -2.3 |
| 185362589181 | white | 65.5 | 75.6 | +10.1 |
| 185362589181 | black | 70.0 | 75.3 | +5.3 |
| 185363112760 | white | 83.0 | 84.4 | +1.4 |
| 185363112760 | black | 88.5 | 89.9 | +1.4 |
| 185468237512 | white | 71.7 | 75.8 | +4.1 |
| 185468237512 | black | 69.9 | 72.9 | +3.0 |
| 185961991257 | white | 91.6 | 94.1 | +2.5 |
| 185961991257 | black | 84.1 | 88.9 | +4.8 |
| 186393389351 | white | 89.3 | 90.7 | +1.4 |
| 186393389351 | black | 86.0 | 88.5 | +2.5 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 185387411150 | 57 | 57 | 64.9% | 75.4% | reviewed | 47.3 |
| 185425961522 | 47 | 47 | 76.6% | 91.5% | reviewed | 45.8 |
| 185439816356 | 15 | 15 | 93.3% | 100.0% | reviewed | 16.1 |
| 185466827454 | 62 | 62 | 61.3% | 83.9% | reviewed | 47.8 |
| 185476493194 | 43 | 43 | 67.4% | 81.4% | reviewed | 30.7 |
| 994221268 | 86 | 86 | 66.3% | 90.7% | reviewed | 90.5 |
| 184740374128 | 58 | 58 | 70.7% | 89.7% | reviewed | 53.3 |
| 185101208706 | 46 | 46 | 69.6% | 89.1% | reviewed | 44.2 |
| 185137444946 | 57 | 57 | 71.9% | 91.2% | reviewed | 61.8 |
| 185151408586 | 42 | 42 | 85.7% | 97.6% | reviewed | 40.7 |
| 185221110711 | 98 | 98 | 58.2% | 85.7% | reviewed | 91.9 |
| 185311691496 | 37 | 37 | 67.6% | 91.9% | reviewed | 42.7 |
| 185344445308 | 92 | 92 | 59.8% | 88.0% | reviewed | 72.9 |
| 185362589181 | 128 | 128 | 69.5% | 88.3% | reviewed | 122.7 |
| 185363112760 | 84 | 84 | 50.0% | 79.8% | reviewed | 80.4 |
| 185468237512 | 112 | 112 | 77.7% | 94.6% | reviewed | 89.0 |
| 185961991257 | 95 | 95 | 51.6% | 86.3% | reviewed | 80.9 |
| 186393389351 | 89 | 89 | 61.8% | 88.8% | reviewed | 65.8 |

## Mismatches by rule (428)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 395 | excellent -> best x60, best -> excellent x54, good -> excellent x41, inaccuracy -> good x37, great -> best x34, excellent -> good x27 |
| `miss_detector` | 13 | mistake -> miss x7, blunder -> miss x4, inaccuracy -> miss x2 |
| `mate_override` | 8 | good -> miss x4, excellent -> inaccuracy x1, excellent -> good x1, mistake -> inaccuracy x1, good -> inaccuracy x1 |
| `losing_material_hardened` | 7 | excellent -> mistake x3, good -> mistake x3, inaccuracy -> mistake x1 |
| `great_find_event` | 2 | best -> great x2 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `brilliant_event` | 1 | best -> brilliant x1 |

### `precision` (395)

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
| 184740374128 | 6 | 3... Bb4 | book | excellent | precision | excellent | 0.0124 | 0.491 | no | Nc6 | - | +0.45 | +0.42 |
| 184740374128 | 7 | 4. Nxe5 | book | best | precision | best | 0.0000 | 0.526 | yes | Nxe5 | - | +0.45 | +0.39 |
| 184740374128 | 10 | 5... Qe7 | good | excellent | precision | excellent | 0.0105 | 0.480 | no | O-O | - | +0.76 | +0.59 |
| 184740374128 | 14 | 7... Qxe4+ | inaccuracy | good | precision | good | 0.0384 | 0.526 | no | Nxe4 | Nxe4 | +0.41 | +0.52 |
| 184740374128 | 15 | 8. Be3 | best | excellent | precision | excellent | 0.0025 | 0.532 | no | Be2 | - | +0.41 | +0.44 |
| 184740374128 | 21 | 11. c4 | inaccuracy | good | precision | good | 0.0479 | 0.568 | no | Kd2 | Kd2 | +0.28 | +0.32 |
| 184740374128 | 22 | 11... d5 | excellent | best | precision | best | 0.0000 | 0.480 | no | Nc6 | - | +0.41 | +0.51 |
| 184740374128 | 29 | 15. a5 | inaccuracy | good | precision | good | 0.0464 | 0.659 | no | Qb1 | Qd2 | +1.31 | +1.85 |
| 184740374128 | 38 | 19... Rxd5 | excellent | good | precision | good | 0.0309 | 0.712 | no | Nf4 | - | -2.48 | -3.14 |
| 184740374128 | 39 | 20. Be4 | mistake | blunder | precision | blunder | 0.2170 | 0.315 | no | Re1 | - | -4.92 | -8.97 |
| 184740374128 | 45 | 23. Rab1 | inaccuracy | mistake | precision | mistake | 0.1852 | 0.500 | no | Rfb1 | Rfb1 | -0.84 | -3.14 |
| 184740374128 | 48 | 24... Rh5 | great | excellent | precision | excellent | 0.0045 | 0.762 | no | Rd5 | - | -4.47 | -4.92 |
| 184740374128 | 55 | 28. Kh2 | excellent | best | precision | best | 0.0000 | 0.137 | yes | Kh2 | - | -7.50 | -7.87 |
| 184740374128 | 56 | 28... Rxh4+ | best | excellent | precision | excellent | 0.0038 | 0.875 | no | Rb8 | - | -7.50 | -7.52 |
| 185101208706 | 6 | 3... Nf6 | good | excellent | precision | excellent | 0.0104 | 0.523 | no | d5 | - | -0.10 | -0.20 |
| 185101208706 | 7 | 4. d4 | good | excellent | precision | excellent | 0.0007 | 0.486 | no | e4 | - | -0.48 | -0.28 |
| 185101208706 | 17 | 9. Ng5 | good | inaccuracy | precision | inaccuracy | 0.0791 | 0.796 | no | Qe5+ | - | +3.08 | +3.35 |
| 185101208706 | 18 | 9... Qe7+ | excellent | good | precision | good | 0.0273 | 0.283 | no | Bxc2 | - | +3.45 | +3.85 |
| 185101208706 | 19 | 10. Be2 | best | excellent | precision | excellent | 0.0129 | 0.744 | no | Kd1 | - | +3.45 | +3.68 |
| 185101208706 | 20 | 10... h6 | excellent | good | precision | good | 0.0231 | 0.265 | no | Bxc2 | - | +3.71 | +4.12 |
| 185101208706 | 23 | 12. Nh3 | good | inaccuracy | precision | inaccuracy | 0.0582 | 0.684 | no | Nf3 | - | +1.85 | +2.00 |
| 185101208706 | 24 | 12... O-O-O | best | excellent | precision | excellent | 0.0077 | 0.365 | no | h5 | - | +1.85 | +1.80 |
| 185101208706 | 28 | 14... Qe4 | best | good | precision | good | 0.0247 | 0.331 | no | Qh4 | - | +2.35 | +2.95 |
| 185101208706 | 29 | 15. O-O | great | best | precision | best | 0.0000 | 0.694 | yes | O-O | - | +2.35 | +2.83 |
| 185101208706 | 30 | 15... Bd6 | good | inaccuracy | precision | inaccuracy | 0.0642 | 0.313 | no | c6 | - | +3.24 | +3.98 |
| 185101208706 | 37 | 19. Bxf5+ | mistake | excellent | precision | excellent | 0.0046 | 0.151 | no | Bxf4 | - | -6.56 | -6.36 |
| 185101208706 | 40 | 20... Bxh2+ | brilliant | best | precision | best | 0.0000 | 1.000 | yes | Bxh2+ | - | -M4 | -M4 |
| 185137444946 | 4 | 2... e6 | book | best | precision | best | 0.0000 | 0.438 | yes | e6 | - | +0.92 | +0.92 |
| 185137444946 | 11 | 6. Nf3 | good | excellent | precision | excellent | 0.0099 | 0.595 | no | Be3 | - | +1.06 | +1.18 |
| 185137444946 | 12 | 6... h6 | inaccuracy | good | precision | good | 0.0404 | 0.415 | no | d6 | d6 | +1.61 | +1.76 |
| 185137444946 | 13 | 7. Be2 | excellent | good | precision | good | 0.0214 | 0.626 | no | Bd3 | - | +1.49 | +1.45 |
| 185137444946 | 14 | 7... Nf6 | good | inaccuracy | precision | inaccuracy | 0.0563 | 0.396 | no | Bb4 | - | +1.94 | +2.28 |
| 185137444946 | 26 | 13... Ba8 | inaccuracy | good | precision | good | 0.0424 | 0.290 | no | exd5 | exd5 | +3.71 | +3.81 |
| 185137444946 | 34 | 17... cxd6 | great | best | precision | best | 0.0000 | 0.418 | yes | cxd6 | - | +0.96 | +0.85 |
| 185137444946 | 36 | 18... Bf6 | great | best | precision | best | 0.0000 | 0.429 | yes | Bf6 | - | +0.96 | +1.01 |
| 185137444946 | 37 | 19. Qe2 | miss | mistake | precision | mistake | 0.1285 | 0.573 | no | cxb5 | cxb5 | -0.66 | -0.76 |
| 185137444946 | 38 | 19... Nc6 | miss | inaccuracy | precision | inaccuracy | 0.0611 | 0.555 | no | bxc4 | bxc4 | +0.87 | +0.17 |
| 185137444946 | 39 | 20. Nd5 | best | excellent | precision | excellent | 0.0036 | 0.512 | no | cxb5 | - | +0.87 | +0.08 |
| 185137444946 | 41 | 21. Bxf6 | good | inaccuracy | precision | inaccuracy | 0.0909 | 0.675 | no | Nxf6+ | - | +1.56 | +1.16 |
| 185137444946 | 43 | 22. Nc7+ | good | inaccuracy | precision | inaccuracy | 0.0558 | 0.631 | no | f5 | - | +1.28 | +1.13 |
| 185137444946 | 44 | 22... Rxc7 | excellent | good | precision | good | 0.0385 | 0.418 | no | Kf8 | - | +1.48 | +1.39 |
| 185137444946 | 49 | 25. Qb2 | best | excellent | precision | excellent | 0.0080 | 0.701 | no | Rac1 | - | +2.80 | +3.10 |
| 185137444946 | 53 | 27. Rac1 | best | excellent | precision | excellent | 0.0149 | 0.700 | no | Bf3 | - | +2.85 | +2.73 |
| 185151408586 | 12 | 6... Qe7 | mistake | inaccuracy | precision | inaccuracy | 0.0957 | 0.471 | no | Nf6 | c6 | +1.74 | +1.73 |
| 185151408586 | 13 | 7. O-O | inaccuracy | good | precision | good | 0.0364 | 0.624 | no | Bf4 | Bf4 | +1.18 | +1.21 |
| 185151408586 | 16 | 8... g6 | excellent | good | precision | good | 0.0354 | 0.455 | no | c6 | - | +0.86 | +1.11 |
| 185151408586 | 32 | 16... Nxc3 | best | excellent | precision | excellent | 0.0000 | 0.783 | no | Bxc3 | - | -4.29 | -4.54 |
| 185151408586 | 33 | 17. bxc3 | excellent | best | precision | best | 0.0000 | 0.209 | yes | bxc3 | - | -4.50 | -4.77 |
| 185151408586 | 35 | 18. Rxe5 | mistake | best | precision | best | 0.0000 | 0.200 | yes | Rxe5 | - | -4.52 | -4.64 |
| 185221110711 | 3 | 2. Nc3 | book | excellent | precision | excellent | 0.0062 | 0.584 | no | e4 | - | +0.58 | +0.55 |
| 185221110711 | 6 | 3... e5 | excellent | best | precision | best | 0.0000 | 0.380 | yes | e5 | - | +0.75 | +0.84 |
| 185221110711 | 8 | 4... Nd7 | excellent | best | precision | best | 0.0000 | 0.418 | yes | Nd7 | - | +0.59 | +0.55 |
| 185221110711 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.587 | yes | Nf3 | - | +0.53 | +0.52 |
| 185221110711 | 10 | 5... Ngf6 | book | excellent | precision | excellent | 0.0031 | 0.418 | no | Be7 | - | +0.56 | +0.60 |
| 185221110711 | 14 | 7... O-O | best | excellent | precision | excellent | 0.0047 | 0.429 | no | exd4 | - | +0.56 | +0.45 |
| 185221110711 | 17 | 9. Re1 | excellent | best | precision | best | 0.0000 | 0.594 | yes | Re1 | - | +0.60 | +0.61 |
| 185221110711 | 18 | 9... a5 | good | excellent | precision | excellent | 0.0152 | 0.404 | no | Re8 | - | +0.76 | +0.78 |
| 185221110711 | 19 | 10. Be3 | best | excellent | precision | excellent | 0.0015 | 0.622 | no | Ba2 | - | +0.76 | +0.74 |
| 185221110711 | 20 | 10... exd4 | best | excellent | precision | excellent | 0.0120 | 0.384 | no | h6 | - | +0.76 | +0.84 |
| 185221110711 | 24 | 12... Nxf3+ | good | excellent | precision | excellent | 0.0156 | 0.437 | no | Be6 | - | +0.56 | +0.48 |
| 185221110711 | 27 | 14. Be2 | inaccuracy | good | precision | good | 0.0486 | 0.584 | no | Bf4 | Bf4 | +0.24 | +0.22 |
| 185221110711 | 28 | 14... Rfd8 | inaccuracy | good | precision | good | 0.0393 | 0.465 | no | d5 | d5 | +0.53 | +0.52 |
| 185221110711 | 30 | 15... d5 | great | best | precision | best | 0.0000 | 0.588 | yes | d5 | - | -0.41 | -0.39 |
| 185221110711 | 31 | 16. e5 | good | inaccuracy | precision | inaccuracy | 0.0509 | 0.438 | no | exd5 | - | -0.64 | -0.72 |
| 185221110711 | 32 | 16... Nd7 | great | best | precision | best | 0.0000 | 0.613 | yes | Nd7 | - | -0.64 | -0.67 |
| 185221110711 | 35 | 18. Rf1 | inaccuracy | mistake | precision | mistake | 0.1026 | 0.481 | no | Qe3 | Qe3 | -0.80 | -0.78 |
| 185221110711 | 40 | 20... Rf8 | excellent | good | precision | good | 0.0226 | 0.626 | no | Bf7 | - | -0.79 | -0.70 |
| 185221110711 | 41 | 21. f5 | excellent | best | precision | best | 0.0000 | 0.390 | yes | f5 | - | -0.81 | -0.66 |
| 185221110711 | 47 | 24. Nxd5 | great | best | precision | best | 0.0000 | 0.475 | yes | Nxd5 | - | -0.18 | -0.11 |
| 185221110711 | 52 | 26... Re3 | great | best | precision | best | 0.0000 | 0.522 | yes | Re3 | - | -0.18 | -0.11 |
| 185221110711 | 54 | 27... Bxa4 | inaccuracy | good | precision | good | 0.0446 | 0.522 | no | Rc8 | - | +0.27 | +0.07 |
| 185221110711 | 70 | 35... Re2 | best | excellent | precision | excellent | 0.0077 | 0.927 | no | Rxc3 | - | -3.36 | -4.10 |
| 185221110711 | 71 | 36. Kg2 | good | best | precision | best | 0.0000 | 0.068 | yes | Kg2 | - | -4.18 | -4.12 |
| 185221110711 | 72 | 36... Rxc3 | best | excellent | precision | excellent | 0.0140 | 0.932 | no | Kg8 | - | -4.18 | -4.29 |
| 185221110711 | 76 | 38... gxf6 | excellent | good | precision | good | 0.0263 | 0.984 | no | d1=Q | - | -4.91 | -5.01 |
| 185221110711 | 77 | 39. gxf6 | excellent | good | precision | good | 0.0253 | 0.039 | no | Rxe2 | - | -6.89 | -7.13 |
| 185221110711 | 78 | 39... Nxf6 | excellent | good | precision | good | 0.0443 | 0.989 | no | d1=Q | - | -4.95 | -4.47 |
| 185221110711 | 82 | 41... Nd5 | excellent | best | precision | best | 0.0000 | 0.961 | yes | Nd5 | - | -4.93 | -4.91 |
| 185221110711 | 85 | 43. Kxf4 | best | excellent | precision | excellent | 0.0008 | 0.004 | no | Ke4 | - | -7.93 | -7.90 |
| 185221110711 | 89 | 45. Kf3 | excellent | best | precision | best | 0.0000 | 0.007 | yes | Kf3 | - | -9.29 | -11.97 |
| 185221110711 | 91 | 46. Kg4 | inaccuracy | excellent | precision | excellent | 0.0075 | 0.008 | no | Ke2 | Kf4 | -M9 | -12.31 |
| 185221110711 | 92 | 46... b5 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qe3 | - | -10.5 | -M10 |
| 185311691496 | 8 | 4... Bc5 | good | excellent | precision | excellent | 0.0178 | 0.524 | no | Bb4+ | - | +0.22 | -0.08 |
| 185311691496 | 9 | 5. e5 | best | excellent | precision | excellent | 0.0078 | 0.494 | no | O-O | - | +0.22 | -0.39 |
| 185311691496 | 13 | 7. Bxf6 | good | excellent | precision | excellent | 0.0071 | 0.511 | no | Bh4 | - | +0.10 | +0.04 |
| 185311691496 | 16 | 8... d6 | mistake | inaccuracy | precision | inaccuracy | 0.0895 | 0.484 | no | Nc6 | Nc6 | +1.55 | +1.51 |
| 185311691496 | 19 | 10. Re1+ | excellent | best | precision | best | 0.0000 | 0.596 | yes | Re1+ | - | +1.49 | +1.37 |
| 185311691496 | 22 | 11... Nc6 | good | excellent | precision | excellent | 0.0197 | 0.345 | no | Nd7 | - | +2.46 | +2.66 |
| 185311691496 | 25 | 13. Nxc5 | excellent | best | precision | best | 0.0000 | 0.678 | yes | Nxc5 | - | +2.21 | +2.59 |
| 185311691496 | 27 | 14. Bxe6 | great | best | precision | best | 0.0000 | 0.683 | yes | Bxe6 | - | +2.21 | +2.60 |
| 185311691496 | 30 | 15... Ne7 | inaccuracy | mistake | precision | mistake | 0.1114 | 0.332 | no | Kd7 | - | +3.98 | +4.44 |
| 185311691496 | 35 | 18. Nxf5 | excellent | best | precision | best | 0.0000 | 0.913 | yes | Nxf5 | - | +8.19 | +8.33 |
| 185344445308 | 3 | 2. Nf3 | book | good | precision | good | 0.0202 | 0.567 | no | d4 | - | +0.74 | +0.69 |
| 185344445308 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.450 | yes | Bb7 | - | +0.74 | +0.64 |
| 185344445308 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.547 | yes | Nc3 | - | +0.74 | +0.67 |
| 185344445308 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.451 | yes | e6 | - | +0.74 | +0.68 |
| 185344445308 | 13 | 7. d4 | excellent | best | precision | best | 0.0000 | 0.560 | no | O-O | - | +0.87 | +0.91 |
| 185344445308 | 15 | 8. Bd2 | inaccuracy | good | precision | good | 0.0298 | 0.597 | no | O-O | O-O | +0.81 | +0.92 |
| 185344445308 | 17 | 9. O-O | best | excellent | precision | excellent | 0.0028 | 0.597 | no | Qe2 | - | +1.32 | +1.21 |
| 185344445308 | 18 | 9... Nf6 | best | excellent | precision | excellent | 0.0176 | 0.413 | no | Ne7 | - | +1.32 | +1.46 |
| 185344445308 | 21 | 11. h3 | good | excellent | precision | excellent | 0.0161 | 0.608 | no | dxe6 | - | +1.18 | +1.28 |
| 185344445308 | 23 | 12. Re1 | good | inaccuracy | precision | inaccuracy | 0.0602 | 0.682 | no | dxe6 | - | +1.72 | +1.70 |
| 185344445308 | 27 | 14. Bxe7 | good | inaccuracy | precision | inaccuracy | 0.0580 | 0.730 | no | dxc6 | - | +2.26 | +2.36 |
| 185344445308 | 33 | 17. Kf1 | excellent | best | precision | best | 0.0000 | 0.436 | yes | Kf1 | - | -0.76 | -0.91 |
| 185344445308 | 38 | 19... O-O-O | good | excellent | precision | excellent | 0.0112 | 0.407 | no | Rh7 | - | +1.61 | +1.51 |
| 185344445308 | 43 | 22. Bd5 | good | excellent | precision | excellent | 0.0029 | 0.492 | no | Qe7 | - | -0.64 | -0.18 |
| 185344445308 | 45 | 23. Rad1 | miss | inaccuracy | precision | inaccuracy | 0.0753 | 0.641 | no | Bxc6 | Bxc6 | +0.48 | +0.46 |
| 185344445308 | 46 | 23... Qf4 | miss | mistake | precision | mistake | 0.1821 | 0.466 | no | Rf4 | Rf4 | +3.17 | +3.16 |
| 185344445308 | 53 | 27. Rxd5 | inaccuracy | good | precision | good | 0.0478 | 0.142 | no | exd5 | exd5 | -7.68 | -8.02 |
| 185344445308 | 60 | 30... Rh8 | good | best | precision | best | 0.0000 | 0.898 | yes | Rh8 | - | -7.19 | -7.70 |
| 185344445308 | 62 | 31... Qd2 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qd2 | - | -M8 | -M11 |
| 185344445308 | 69 | 35. Kg1 | inaccuracy | mistake | precision | mistake | 0.1055 | 0.105 | no | Kg3 | Kg3 | -M6 | -M9 |
| 185344445308 | 72 | 36... Qxc2+ | excellent | best | precision | best | 0.0000 | 0.880 | yes | Qxc2+ | - | -6.53 | -7.05 |
| 185344445308 | 73 | 37. Re2 | good | excellent | precision | excellent | 0.0012 | 0.113 | no | Ke3 | - | -7.46 | -8.36 |
| 185344445308 | 74 | 37... Qc5+ | excellent | best | precision | best | 0.0000 | 0.920 | yes | Qc5+ | - | -6.91 | -6.68 |
| 185344445308 | 76 | 38... Kb7 | good | inaccuracy | precision | inaccuracy | 0.0737 | 0.945 | no | Re8 | - | -6.68 | -6.54 |
| 185344445308 | 77 | 39. Kf3 | excellent | best | precision | best | 0.0000 | 0.129 | yes | Kf3 | - | -7.21 | -7.04 |
| 185344445308 | 80 | 40... Rd8 | best | excellent | precision | excellent | 0.0051 | 0.886 | no | Qh4+ | - | -7.21 | -6.85 |
| 185344445308 | 81 | 41. Re7+ | best | excellent | precision | excellent | 0.0120 | 0.119 | no | Rf3 | - | -7.21 | -7.26 |
| 185344445308 | 82 | 41... Kc8 | excellent | best | precision | best | 0.0000 | 0.893 | yes | Kc8 | - | -6.70 | -7.22 |
| 185344445308 | 83 | 42. Re2 | excellent | best | precision | best | 0.0000 | 0.108 | yes | Re2 | - | -7.24 | -8.16 |
| 185344445308 | 84 | 42... Qc5+ | best | good | precision | good | 0.0227 | 0.916 | no | Qh4+ | - | -7.24 | -7.20 |
| 185344445308 | 86 | 43... Kb7 | good | inaccuracy | precision | inaccuracy | 0.0638 | 0.934 | no | Rd3+ | - | -6.62 | -6.53 |
| 185344445308 | 87 | 44. g4 | inaccuracy | mistake | precision | mistake | 0.1293 | 0.129 | no | Re5 | Re5 | -M12 | -M13 |
| 185362589181 | 4 | 2... Bg7 | inaccuracy | good | precision | good | 0.0380 | 0.479 | no | Nf6 | Nf6 | +0.44 | +0.37 |
| 185362589181 | 8 | 4... d5 | best | excellent | precision | excellent | 0.0079 | 0.457 | no | h6 | - | +0.35 | +0.35 |
| 185362589181 | 9 | 5. Nc3 | good | inaccuracy | precision | inaccuracy | 0.0539 | 0.556 | no | e4 | - | +0.13 | +0.01 |
| 185362589181 | 18 | 9... d4 | great | best | precision | best | 0.0000 | 0.585 | yes | d4 | - | -0.58 | -0.46 |
| 185362589181 | 22 | 11... c5 | great | best | precision | best | 0.0000 | 0.566 | yes | c5 | - | -0.42 | -0.48 |
| 185362589181 | 23 | 12. g3 | mistake | inaccuracy | precision | inaccuracy | 0.0695 | 0.424 | no | b4 | b4 | -1.01 | -0.94 |
| 185362589181 | 24 | 12... Be6 | miss | inaccuracy | precision | inaccuracy | 0.0993 | 0.645 | no | a5 | a5 | -0.50 | -0.29 |
| 185362589181 | 32 | 16... a5 | good | best | precision | best | 0.0000 | 0.705 | yes | a5 | - | -1.25 | -1.32 |
| 185362589181 | 34 | 17... a4 | mistake | inaccuracy | precision | inaccuracy | 0.0629 | 0.759 | no | g5 | g5 | -1.01 | -1.30 |
| 185362589181 | 35 | 18. cxd4 | miss | good | precision | good | 0.0401 | 0.304 | no | bxa4 | bxa4 | -1.65 | -1.61 |
| 185362589181 | 39 | 20. Ra1 | inaccuracy | good | precision | good | 0.0225 | 0.240 | no | Ne1 | Nh2 | -2.01 | -1.95 |
| 185362589181 | 40 | 20... Rac8 | inaccuracy | good | precision | good | 0.0253 | 0.776 | no | Nb4 | Nb4 | -1.57 | -1.73 |
| 185362589181 | 45 | 23. Rfc1 | best | good | precision | good | 0.0316 | 0.201 | no | Ne1 | - | -2.10 | -2.50 |
| 185362589181 | 46 | 23... Qb5 | good | inaccuracy | precision | inaccuracy | 0.0839 | 0.831 | no | Rxc1+ | - | -1.78 | -1.70 |
| 185362589181 | 47 | 24. Bf1 | good | inaccuracy | precision | inaccuracy | 0.0720 | 0.253 | no | Nfxd4 | - | -2.15 | -2.37 |
| 185362589181 | 55 | 28. fxe5 | miss | good | precision | good | 0.0235 | 0.374 | no | Ra4 | Ra4 | -1.10 | -1.10 |
| 185362589181 | 58 | 29... Rf8 | excellent | best | precision | best | 0.0000 | 0.809 | yes | Rf8 | - | -1.94 | -1.63 |
| 185362589181 | 59 | 30. Ra4 | excellent | inaccuracy | precision | inaccuracy | 0.0679 | 0.261 | no | Rxc8 | - | -2.08 | -2.31 |
| 185362589181 | 62 | 31... Bd6 | inaccuracy | mistake | precision | mistake | 0.1030 | 0.816 | no | Nc6 | Nc6 | -1.53 | -1.43 |
| 185362589181 | 63 | 32. Nc4 | mistake | best | precision | best | 0.0000 | 0.287 | yes | Nc4 | - | -2.32 | -2.26 |
| 185362589181 | 68 | 34... Nc6 | blunder | mistake | precision | mistake | 0.1957 | 0.796 | no | Rf6 | Rf6 | -0.57 | -0.63 |
| 185362589181 | 72 | 36... Qf7 | best | excellent | precision | excellent | 0.0188 | 0.786 | no | Qd7 | - | -1.94 | -2.00 |
| 185362589181 | 75 | 38. g4 | best | excellent | precision | excellent | 0.0060 | 0.046 | no | Nd6 | - | -4.64 | -5.24 |
| 185362589181 | 82 | 41... f2+ | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qg1+ | - | -6.41 | -M16 |
| 185362589181 | 83 | 42. Kh2 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kh2 | Kg2 | -M9 | -10.73 |
| 185362589181 | 90 | 45... Rxf7 | good | inaccuracy | precision | inaccuracy | 0.0994 | 0.875 | no | Kxf7 | - | -2.13 | -2.19 |
| 185362589181 | 91 | 46. Nxd4 | excellent | best | precision | best | 0.0000 | 0.199 | yes | Nxd4 | - | -2.19 | -2.35 |
| 185362589181 | 93 | 47. Nxf3 | excellent | best | precision | best | 0.0000 | 0.303 | no | Kh2 | - | -1.35 | -1.12 |
| 185362589181 | 96 | 48... Rf6 | inaccuracy | excellent | precision | excellent | 0.0054 | 0.699 | no | Rf8 | Rf8 | -1.09 | -1.40 |
| 185362589181 | 107 | 54. d7 | mistake | excellent | precision | excellent | 0.0148 | 0.045 | no | Bb5 | Bb5 | -4.54 | -5.83 |
| 185362589181 | 109 | 55. Bh3 | good | excellent | precision | excellent | 0.0112 | 0.028 | no | Bb5 | - | -5.34 | -6.36 |
| 185362589181 | 113 | 57. Bg4 | excellent | best | precision | best | 0.0000 | 0.037 | yes | Bg4 | - | -4.48 | -5.70 |
| 185362589181 | 121 | 61. Bxg6 | miss | blunder | precision | blunder | 0.5080 | 0.973 | no | Kf4 | Kf4 | -0.06 | -0.22 |
| 185362589181 | 122 | 61... Kxg6 | excellent | best | precision | best | 0.0000 | 0.535 | yes | Kxg6 | - | 0.00 | -0.05 |
| 185362589181 | 123 | 62. Kf4 | best | excellent | precision | excellent | 0.0000 | 0.492 | no | Kf2 | - | 0.00 | -0.04 |
| 185362589181 | 124 | 62... Kf6 | best | excellent | precision | excellent | 0.0016 | 0.506 | no | Kxh6 | - | 0.00 | +0.00 |
| 185362589181 | 125 | 63. Kg3 | excellent | best | precision | best | 0.0000 | 0.500 | no | Kg4 | - | -0.01 | +0.00 |
| 185363112760 | 3 | 2. Nc3 | book | good | precision | good | 0.0205 | 0.562 | no | d4 | - | +0.31 | +0.26 |
| 185363112760 | 4 | 2... d5 | book | best | precision | best | 0.0000 | 0.459 | yes | d5 | - | +0.31 | +0.31 |
| 185363112760 | 5 | 3. e3 | book | excellent | precision | excellent | 0.0095 | 0.549 | no | cxd5 | - | +0.12 | +0.23 |
| 185363112760 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.463 | yes | Nf6 | - | +0.30 | +0.38 |
| 185363112760 | 8 | 4... g6 | book | good | precision | good | 0.0220 | 0.456 | no | Bf5 | - | +0.52 | +0.42 |
| 185363112760 | 11 | 6. Be2 | book | best | precision | best | 0.0000 | 0.565 | yes | Be2 | - | +0.42 | +0.46 |
| 185363112760 | 12 | 6... O-O | book | best | precision | best | 0.0000 | 0.427 | yes | O-O | - | +0.42 | +0.41 |
| 185363112760 | 13 | 7. O-O | book | best | precision | best | 0.0000 | 0.565 | yes | O-O | - | +0.42 | +0.50 |
| 185363112760 | 14 | 7... Bf5 | good | excellent | precision | excellent | 0.0031 | 0.421 | no | a6 | - | +0.66 | +0.52 |
| 185363112760 | 15 | 8. Qb3 | good | best | precision | best | 0.0000 | 0.582 | no | h3 | - | +0.51 | +0.52 |
| 185363112760 | 16 | 8... b6 | good | excellent | precision | excellent | 0.0139 | 0.418 | no | Qb6 | - | +0.69 | +0.62 |
| 185363112760 | 18 | 9... e6 | good | excellent | precision | excellent | 0.0110 | 0.448 | no | dxc4 | - | +0.76 | +0.50 |
| 185363112760 | 19 | 10. Rac1 | inaccuracy | good | precision | good | 0.0298 | 0.579 | no | Ne5 | Ne5 | +0.37 | +0.31 |
| 185363112760 | 21 | 11. h3 | good | excellent | precision | excellent | 0.0095 | 0.552 | no | Be1 | - | +0.23 | +0.21 |
| 185363112760 | 24 | 12... c5 | good | excellent | precision | excellent | 0.0145 | 0.358 | no | Rc8 | - | +1.05 | +0.95 |
| 185363112760 | 26 | 13... Qe7 | inaccuracy | good | precision | good | 0.0444 | 0.365 | no | Rc8 | Rc8 | +1.38 | +1.29 |
| 185363112760 | 30 | 15... Nxc5 | good | excellent | precision | excellent | 0.0109 | 0.434 | no | Bd5 | - | +0.56 | +0.56 |
| 185363112760 | 31 | 16. b4 | great | best | precision | best | 0.0000 | 0.588 | yes | b4 | - | +0.56 | +0.52 |
| 185363112760 | 32 | 16... Bd5 | great | best | precision | best | 0.0000 | 0.418 | yes | Bd5 | - | +0.56 | +0.48 |
| 185363112760 | 36 | 18... Nce4 | best | excellent | precision | excellent | 0.0172 | 0.441 | no | Nfe4 | - | +0.56 | +0.57 |
| 185363112760 | 40 | 20... Rfb8 | inaccuracy | best | precision | best | 0.0000 | 0.193 | no | Nd7 | d4 | +2.53 | +2.54 |
| 185363112760 | 41 | 21. Qc7 | excellent | best | precision | best | 0.0000 | 0.835 | yes | Qc7 | - | +2.48 | +2.59 |
| 185363112760 | 44 | 22... Nd7 | good | inaccuracy | precision | inaccuracy | 0.0632 | 0.179 | no | Bf8 | - | +2.96 | +3.19 |
| 185363112760 | 46 | 23... Qe8 | excellent | good | precision | good | 0.0387 | 0.142 | no | Rc8 | - | +3.33 | +3.54 |
| 185363112760 | 47 | 24. Rxd5 | best | excellent | precision | excellent | 0.0127 | 0.905 | no | Rxa6 | - | +3.33 | +3.61 |
| 185363112760 | 51 | 26. Rxc8 | great | best | precision | best | 0.0000 | 0.907 | yes | Rxc8 | - | +3.63 | +3.88 |
| 185363112760 | 52 | 26... Rxc8 | excellent | best | precision | best | 0.0000 | 0.078 | yes | Rxc8 | - | +3.87 | +4.09 |
| 185363112760 | 53 | 27. Rd1 | excellent | good | precision | good | 0.0218 | 0.931 | no | Re5 | - | +3.32 | +3.64 |
| 185363112760 | 57 | 29. Bb5 | excellent | good | precision | good | 0.0201 | 0.967 | no | Bc4 | - | +4.44 | +4.52 |
| 185363112760 | 60 | 30... Rb8 | best | excellent | precision | excellent | 0.0078 | 0.054 | no | Nxf2 | - | +4.37 | +4.39 |
| 185363112760 | 62 | 31... Rc8 | best | excellent | precision | excellent | 0.0006 | 0.054 | no | g5 | - | +4.26 | +4.64 |
| 185363112760 | 63 | 32. Qb6 | best | excellent | precision | excellent | 0.0031 | 0.951 | no | Qb7 | - | +4.26 | +4.45 |
| 185363112760 | 72 | 36... Nd5 | great | best | precision | best | 0.0000 | 0.380 | yes | Nd5 | - | +0.62 | +0.72 |
| 185363112760 | 75 | 38. Bc6 | mistake | blunder | precision | blunder | 0.2737 | 0.525 | no | Be1 | a5 | -1.70 | -1.71 |
| 185363112760 | 76 | 38... Nxb4 | great | best | precision | best | 0.0000 | 0.748 | yes | Nxb4 | - | -1.70 | -1.80 |
| 185363112760 | 77 | 39. Be4 | inaccuracy | good | precision | good | 0.0364 | 0.241 | no | Bb5 | Bb5 | -2.22 | -2.29 |
| 185363112760 | 80 | 40... Kg7 | excellent | good | precision | good | 0.0268 | 0.810 | no | Rc1+ | - | -2.10 | -2.10 |
| 185363112760 | 81 | 41. Bg3 | good | inaccuracy | precision | inaccuracy | 0.0839 | 0.208 | no | Be1 | - | -2.78 | -3.07 |
| 185363112760 | 82 | 41... Qc5 | good | inaccuracy | precision | inaccuracy | 0.0637 | 0.876 | no | Qe7 | - | -2.33 | -2.30 |
| 185363112760 | 83 | 42. Be5+ | inaccuracy | mistake | precision | mistake | 0.1342 | 0.188 | no | a5 | - | -4.34 | -4.51 |
| 185363112760 | 84 | 42... Bxe5 | great | best | precision | best | 0.0000 | 0.946 | yes | Bxe5 | - | -4.34 | -4.14 |
| 185468237512 | 12 | 6... Bxf3 | excellent | good | precision | good | 0.0239 | 0.503 | no | Nc6 | - | +0.18 | +0.29 |
| 185468237512 | 14 | 7... e6 | best | excellent | precision | excellent | 0.0051 | 0.488 | no | Nf6 | - | +0.18 | +0.22 |
| 185468237512 | 18 | 9... Nf6 | excellent | best | precision | best | 0.0000 | 0.481 | yes | Nf6 | - | +0.31 | +0.29 |
| 185468237512 | 23 | 12. Bxd5 | excellent | best | precision | best | 0.0000 | 0.631 | yes | Bxd5 | - | +1.57 | +1.89 |
| 185468237512 | 31 | 16. Bf4 | inaccuracy | good | precision | good | 0.0323 | 0.665 | no | Bxf6 | Bxf6 | +1.70 | +1.84 |
| 185468237512 | 41 | 21. Rxd8 | best | excellent | precision | excellent | 0.0051 | 0.804 | no | c4 | - | +4.75 | +4.75 |
| 185468237512 | 54 | 27... Rd2 | good | excellent | precision | excellent | 0.0170 | 0.239 | no | h5 | - | +4.34 | +4.39 |
| 185468237512 | 59 | 30. e7 | good | inaccuracy | precision | inaccuracy | 0.0571 | 0.717 | no | Ke4 | - | +2.28 | +2.29 |
| 185468237512 | 64 | 32... Rd6+ | excellent | good | precision | good | 0.0481 | 0.282 | no | Rc6 | - | +3.36 | +3.72 |
| 185468237512 | 65 | 33. Kc4 | excellent | best | precision | best | 0.0000 | 0.746 | yes | Kc4 | - | +3.24 | +3.37 |
| 185468237512 | 69 | 35. Kc6 | good | inaccuracy | precision | inaccuracy | 0.0750 | 0.805 | no | b3 | - | +3.39 | +3.43 |
| 185468237512 | 70 | 35... a4 | good | excellent | precision | excellent | 0.0085 | 0.270 | no | Rb8 | - | +4.28 | +4.32 |
| 185468237512 | 73 | 37. bxa3 | inaccuracy | mistake | precision | mistake | 0.1309 | 0.812 | no | b4 | b4 | +2.69 | +2.73 |
| 185468237512 | 78 | 39... g6+ | excellent | best | precision | best | 0.0000 | 0.385 | yes | g6+ | - | +1.72 | +1.65 |
| 185468237512 | 79 | 40. Kg4 | excellent | best | precision | best | 0.0000 | 0.617 | yes | Kg4 | - | +1.52 | +1.42 |
| 185468237512 | 81 | 41. Kg5 | great | best | precision | best | 0.0000 | 0.773 | yes | Kg5 | - | +4.46 | +4.62 |
| 185468237512 | 84 | 42... Ra6+ | good | best | precision | best | 0.0000 | 0.216 | yes | Ra6+ | - | +4.92 | +6.19 |
| 185468237512 | 91 | 46. Rd6 | great | best | precision | best | 0.0000 | 1.000 | yes | Rd6 | - | M2 | M2 |
| 185468237512 | 96 | 48... f4 | excellent | best | precision | best | 0.0000 | 0.176 | yes | f4 | - | +5.14 | +5.24 |
| 185468237512 | 101 | 51. Kxg5 | inaccuracy | good | precision | good | 0.0302 | 0.903 | no | Ke6 | - | +5.52 | +5.43 |
| 185468237512 | 102 | 51... Kxe7 | good | best | precision | best | 0.0000 | 0.172 | yes | Kxe7 | - | +5.89 | +7.15 |
| 185468237512 | 103 | 52. Kh6 | great | best | precision | best | 0.0000 | 0.888 | yes | Kh6 | - | +5.89 | +5.37 |
| 185468237512 | 104 | 52... Kf6 | excellent | best | precision | best | 0.0000 | 0.174 | no | Ke8 | - | +5.96 | +6.48 |
| 185468237512 | 105 | 53. Kxh7 | good | best | precision | best | 0.0000 | 0.867 | no | h4 | - | +5.30 | +5.53 |
| 185468237512 | 106 | 53... Kg5 | best | excellent | precision | excellent | 0.0110 | 0.168 | no | Kf5 | - | +5.30 | +5.38 |
| 185961991257 | 6 | 3... Nxd5 | book | best | precision | best | 0.0000 | 0.449 | yes | Nxd5 | - | +0.27 | +0.29 |
| 185961991257 | 7 | 4. Nf3 | book | excellent | precision | excellent | 0.0032 | 0.546 | no | Bc4 | - | +0.27 | +0.24 |
| 185961991257 | 8 | 4... Nxc3 | best | excellent | precision | excellent | 0.0079 | 0.462 | no | g6 | - | +0.27 | +0.16 |
| 185961991257 | 12 | 6... Bg7 | excellent | best | precision | best | 0.0000 | 0.521 | yes | Bg7 | - | -0.12 | -0.06 |
| 185961991257 | 13 | 7. d4 | good | excellent | precision | excellent | 0.0191 | 0.490 | no | Bg2 | - | -0.29 | -0.28 |
| 185961991257 | 14 | 7... O-O | good | excellent | precision | excellent | 0.0127 | 0.544 | no | Be6 | - | -0.16 | -0.01 |
| 185961991257 | 19 | 10. Rb1 | good | inaccuracy | precision | inaccuracy | 0.0652 | 0.541 | no | Bd2 | - | -0.03 | -0.15 |
| 185961991257 | 20 | 10... Rd8 | inaccuracy | best | precision | best | 0.0000 | 0.524 | yes | Rd8 | cxd4 | +0.39 | -0.10 |
| 185961991257 | 21 | 11. Qe1 | mistake | inaccuracy | precision | inaccuracy | 0.0692 | 0.484 | no | Ng5 | Ng5 | -0.57 | -0.54 |
| 185961991257 | 23 | 12. Be3 | good | inaccuracy | precision | inaccuracy | 0.0924 | 0.409 | no | Bg5 | - | -0.83 | -1.21 |
| 185961991257 | 32 | 16... e6 | mistake | good | precision | good | 0.0317 | 0.487 | no | Rb8 | Rb8 | +0.71 | +0.28 |
| 185961991257 | 33 | 17. c3 | miss | excellent | precision | excellent | 0.0095 | 0.544 | no | Red1 | Red1 | +0.07 | +0.15 |
| 185961991257 | 35 | 18. a4 | best | excellent | precision | excellent | 0.0175 | 0.538 | no | Re5 | - | +0.07 | +0.07 |
| 185961991257 | 37 | 19. a5 | good | excellent | precision | excellent | 0.0175 | 0.537 | no | Bxb7 | - | +0.17 | +0.09 |
| 185961991257 | 40 | 20... axb6 | best | excellent | precision | excellent | 0.0064 | 0.482 | no | Rxb6 | - | +0.19 | +0.15 |
| 185961991257 | 42 | 21... Rdc8 | good | excellent | precision | excellent | 0.0175 | 0.494 | no | b5 | - | +0.24 | +0.15 |
| 185961991257 | 43 | 22. Reb1 | inaccuracy | good | precision | good | 0.0398 | 0.524 | no | Ra1 | f4 | -0.07 | -0.10 |
| 185961991257 | 46 | 23... Kf8 | good | excellent | precision | excellent | 0.0080 | 0.495 | no | Bc6 | - | +0.20 | +0.08 |
| 185961991257 | 47 | 24. c4 | good | best | precision | best | 0.0000 | 0.513 | yes | c4 | - | +0.03 | +0.04 |
| 185961991257 | 49 | 25. cxb5 | excellent | best | precision | best | 0.0000 | 0.634 | yes | cxb5 | - | +1.13 | +0.87 |
| 185961991257 | 51 | 26. Rb4 | inaccuracy | mistake | precision | mistake | 0.1071 | 0.689 | no | Ra1 | Ra1 | +0.89 | +0.52 |
| 185961991257 | 52 | 26... Ke7 | good | inaccuracy | precision | inaccuracy | 0.0589 | 0.418 | no | Ra7 | - | +0.99 | +1.14 |
| 185961991257 | 53 | 27. Ra1 | excellent | best | precision | best | 0.0000 | 0.674 | yes | Ra1 | - | +0.94 | +0.90 |
| 185961991257 | 57 | 29. h4 | excellent | good | precision | good | 0.0327 | 0.590 | no | Bc4 | - | +0.64 | +0.36 |
| 185961991257 | 58 | 29... Kd6 | excellent | good | precision | good | 0.0419 | 0.443 | no | h6 | - | +0.67 | +0.63 |
| 185961991257 | 60 | 30... h5 | mistake | inaccuracy | precision | inaccuracy | 0.0745 | 0.434 | no | Bc8 | h6 | +1.13 | +0.91 |
| 185961991257 | 61 | 31. Be2 | miss | inaccuracy | precision | inaccuracy | 0.0761 | 0.641 | no | Bc4 | Kg2 | +0.54 | +0.41 |
| 185961991257 | 62 | 31... Ra4 | inaccuracy | good | precision | good | 0.0341 | 0.435 | no | Bc8 | Bc8 | +0.93 | +0.75 |
| 185961991257 | 65 | 33. R4b2 | good | excellent | precision | excellent | 0.0182 | 0.616 | no | Kf1 | - | +0.93 | +0.62 |
| 185961991257 | 66 | 33... Ra4 | good | best | precision | best | 0.0000 | 0.403 | yes | Ra4 | - | +1.07 | +0.84 |
| 185961991257 | 67 | 34. Rb4 | great | best | precision | best | 0.0000 | 0.631 | yes | Rb4 | - | +1.07 | +0.78 |
| 185961991257 | 68 | 34... Ra2 | excellent | best | precision | best | 0.0000 | 0.378 | no | Ra8 | - | +1.14 | +0.91 |
| 185961991257 | 69 | 35. Bf1 | mistake | inaccuracy | precision | inaccuracy | 0.0527 | 0.641 | no | Kf1 | Kf1 | +0.67 | +0.56 |
| 185961991257 | 70 | 35... Rd2 | inaccuracy | good | precision | good | 0.0454 | 0.412 | no | Bc8 | Bc8 | +0.96 | +0.86 |
| 185961991257 | 71 | 36. Ra1 | inaccuracy | good | precision | good | 0.0209 | 0.634 | no | Ra4 | R1b2 | +0.65 | +0.72 |
| 185961991257 | 72 | 36... Bc8 | inaccuracy | good | precision | good | 0.0341 | 0.387 | no | Bc6 | Bc6 | +1.03 | +0.95 |
| 185961991257 | 73 | 37. Ra7 | best | good | precision | good | 0.0357 | 0.647 | no | Rba4 | - | +1.03 | +0.99 |
| 185961991257 | 74 | 37... Bb7 | best | excellent | precision | excellent | 0.0000 | 0.347 | no | Bd7 | - | +1.03 | +0.85 |
| 185961991257 | 76 | 38... Rxd4 | excellent | best | precision | best | 0.0000 | 0.486 | yes | Rxd4 | - | +0.11 | +0.24 |
| 185961991257 | 77 | 39. Bg2 | excellent | best | precision | best | 0.0000 | 0.538 | yes | Bg2 | - | +0.06 | +0.08 |
| 185961991257 | 78 | 39... Bxg2 | inaccuracy | excellent | precision | excellent | 0.0111 | 0.487 | no | Kc7 | Kc7 | +0.40 | +0.35 |
| 185961991257 | 85 | 43. Rg7 | great | best | precision | best | 0.0000 | 0.673 | yes | Rg7 | - | +1.97 | +1.90 |
| 185961991257 | 86 | 43... g5 | inaccuracy | mistake | precision | mistake | 0.1707 | 0.230 | no | Rb8 | Rb8 | +2.70 | +4.35 |
| 185961991257 | 88 | 44... Rxg5 | inaccuracy | good | precision | good | 0.0404 | 0.060 | no | Rd5 | Rd5 | +5.51 | +6.17 |
| 185961991257 | 90 | 45... Ke5 | excellent | best | precision | best | 0.0000 | 0.005 | yes | Ke5 | - | +5.78 | +6.80 |
| 186393389351 | 8 | 4... Bb4 | book | best | precision | best | 0.0000 | 0.484 | yes | Bb4 | - | +0.10 | +0.03 |
| 186393389351 | 9 | 5. d3 | book | best | precision | best | 0.0000 | 0.505 | yes | d3 | - | +0.10 | -0.03 |
| 186393389351 | 10 | 5... d6 | book | best | precision | best | 0.0000 | 0.505 | yes | d6 | - | +0.10 | +0.02 |
| 186393389351 | 11 | 6. a3 | book | excellent | precision | excellent | 0.0048 | 0.503 | no | Be2 | - | +0.10 | +0.11 |
| 186393389351 | 16 | 8... Bg4 | excellent | best | precision | best | 0.0000 | 0.490 | yes | Bg4 | - | +0.11 | +0.06 |
| 186393389351 | 18 | 9... Bxf3 | excellent | best | precision | best | 0.0000 | 0.471 | yes | Bxf3 | - | +0.12 | +0.12 |
| 186393389351 | 20 | 10... Nd4 | best | excellent | precision | excellent | 0.0063 | 0.467 | no | O-O | - | +0.12 | +0.22 |
| 186393389351 | 21 | 11. Na4 | excellent | best | precision | best | 0.0000 | 0.535 | yes | Na4 | - | +0.04 | +0.17 |
| 186393389351 | 22 | 11... c6 | inaccuracy | good | precision | good | 0.0379 | 0.473 | no | Nxf3+ | Nxf3+ | +0.49 | +0.41 |
| 186393389351 | 23 | 12. O-O | inaccuracy | good | precision | good | 0.0458 | 0.565 | no | Nxb6 | Nxb6 | +0.03 | +0.06 |
| 186393389351 | 26 | 13... Qxb6 | good | excellent | precision | excellent | 0.0141 | 0.448 | no | Nxf3+ | - | +0.49 | +0.38 |
| 186393389351 | 28 | 14... a5 | good | excellent | precision | excellent | 0.0062 | 0.424 | no | Rfe8 | - | +0.66 | +0.52 |
| 186393389351 | 29 | 15. bxa5 | inaccuracy | good | precision | good | 0.0408 | 0.582 | no | b5 | b5 | +0.17 | +0.24 |
| 186393389351 | 30 | 15... Qc7 | good | excellent | precision | excellent | 0.0111 | 0.462 | no | Qxa5 | - | +0.33 | +0.33 |
| 186393389351 | 33 | 17. Bg4 | inaccuracy | mistake | precision | mistake | 0.1012 | 0.582 | no | Bc3 | h3 | -0.25 | -0.12 |
| 186393389351 | 35 | 18. axb6 | best | excellent | precision | excellent | 0.0016 | 0.489 | no | Rxb6 | - | -0.25 | -0.18 |
| 186393389351 | 38 | 19... Rxa3 | inaccuracy | good | precision | good | 0.0359 | 0.587 | no | Rxb1 | Rxb1 | -0.20 | -0.19 |
| 186393389351 | 41 | 21. Bg5 | inaccuracy | good | precision | good | 0.0344 | 0.393 | no | g3 | g3 | -1.08 | -0.91 |
| 186393389351 | 49 | 25. Qc1 | excellent | best | precision | best | 0.0000 | 0.293 | yes | Qc1 | - | -1.39 | -1.33 |
| 186393389351 | 52 | 26... Qe7 | great | best | precision | best | 0.0000 | 0.691 | yes | Qe7 | - | -1.39 | -1.34 |
| 186393389351 | 54 | 27... g6 | great | best | precision | best | 0.0000 | 0.803 | yes | g6 | - | -2.11 | -2.14 |
| 186393389351 | 56 | 28... Qf8 | miss | mistake | precision | mistake | 0.1766 | 0.798 | no | Qxe4 | Qxe4 | -0.99 | -0.81 |
| 186393389351 | 61 | 31. Qg4 | best | excellent | precision | excellent | 0.0067 | 0.101 | no | Qc1 | - | -2.90 | -3.20 |
| 186393389351 | 63 | 32. Qe2 | mistake | inaccuracy | precision | inaccuracy | 0.0600 | 0.117 | no | Bxg6 | - | -4.14 | -4.34 |
| 186393389351 | 64 | 32... Rd2 | great | best | precision | best | 0.0000 | 0.941 | yes | Rd2 | - | -4.14 | -4.50 |
| 186393389351 | 68 | 34... Qf4 | best | excellent | precision | excellent | 0.0013 | 0.948 | no | h4 | - | -4.41 | -4.53 |
| 186393389351 | 69 | 35. g3 | best | excellent | precision | excellent | 0.0085 | 0.053 | no | exd6 | - | -4.41 | -5.23 |
| 186393389351 | 74 | 37... Nd4 | excellent | good | precision | good | 0.0274 | 0.153 | no | Qe4 | - | +2.80 | +3.01 |
| 186393389351 | 75 | 38. Qe3 | good | inaccuracy | precision | inaccuracy | 0.0725 | 0.872 | no | Ra3 | - | +2.13 | +2.94 |
| 186393389351 | 76 | 38... Qf5 | inaccuracy | good | precision | good | 0.0361 | 0.133 | no | Qxe3 | Qxe3 | +3.24 | +3.30 |
| 186393389351 | 77 | 39. Qe8 | good | inaccuracy | precision | inaccuracy | 0.0683 | 0.891 | no | Kg2 | - | +2.40 | +2.41 |
| 186393389351 | 81 | 41. Kh3 | great | best | precision | best | 0.0000 | 0.792 | yes | Kh3 | - | +2.40 | +2.03 |
| 186393389351 | 82 | 41... Kf6 | inaccuracy | mistake | precision | mistake | 0.1773 | 0.215 | no | Qf3 | - | +5.29 | +5.07 |

### `miss_detector` (13)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185387411150 | 23 | 12. Bh4 | mistake | miss (tactic) | miss_detector | mistake | 0.1290 | 0.776 | no | Qg6+ | Qg6+ | +1.91 | +2.41 |
| 185387411150 | 45 | 23. fxg3 | mistake | miss (tactic) | miss_detector | blunder | 0.4286 | 0.929 | no | Qb3+ | Qb3+ | 0.00 | +0.00 |
| 185425961522 | 38 | 19... Nf4 | blunder | miss (tactic) | miss_detector | blunder | 0.5770 | 0.703 | no | Rd3 | Rd3 | +6.74 | +6.79 |
| 185466827454 | 22 | 11... Bxd4 | mistake | miss (free_piece) | miss_detector | mistake | 0.1045 | 0.611 | no | Qxd4 | Qxd4 | +0.32 | +0.23 |
| 185476493194 | 20 | 10... Bg4 | blunder | miss (tactic) | miss_detector | blunder | 0.5392 | 0.759 | no | g5 | - | +4.08 | +4.31 |
| 184740374128 | 34 | 17... h6 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1190 | 0.440 | no | Qd7 | Qd7 | +2.11 | +3.02 |
| 184740374128 | 40 | 20... Rg5+ | mistake | miss (tactic) | miss_detector | blunder | 0.4022 | 0.902 | no | Nf4 | Nf4 | 0.00 | +0.00 |
| 185101208706 | 16 | 8... Bf5 | mistake | miss (free_piece) | miss_detector | blunder | 0.2870 | 0.491 | no | dxe4 | - | +4.02 | +4.91 |
| 185221110711 | 62 | 31... Nh5 | blunder | miss (free_piece) | miss_detector | blunder | 0.3950 | 0.932 | no | Rxc4 | - | -0.21 | -0.23 |
| 185311691496 | 11 | 6. Bg5 | mistake | miss (opportunity) | miss_detector | mistake | 0.1881 | 0.707 | no | O-O | - | +0.58 | +0.27 |
| 185362589181 | 71 | 36. Nb5 | mistake | miss (opportunity) | miss_detector | mistake | 0.1146 | 0.329 | no | Bg2 | a5 | -1.94 | -2.04 |
| 185961991257 | 24 | 12... cxd4 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1172 | 0.684 | no | Be6 | Be6 | -0.44 | -0.42 |
| 186393389351 | 57 | 29. Qf4 | blunder | miss (opportunity) | miss_detector | blunder | 0.2553 | 0.374 | no | Qxf8+ | - | -2.90 | -3.15 |

### `mate_override` (8)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185221110711 | 87 | 44. Kg3 | excellent | inaccuracy | mate_override | inaccuracy | 0.0043 | 0.004 | no | c4 | - | -12.3 | -M17 |
| 185221110711 | 88 | 44... Qc4 | excellent | good | mate_override | good | 0.0066 | 1.000 | no | b5 | - | -7.27 | -7.87 |
| 185221110711 | 93 | 47. Kh5 | mistake | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | h4 | Kf5 | -M2 | -M2 |
| 185344445308 | 56 | 28... Ng3+ | good | miss (mate) | mate_override | mistake | 0.1047 | 1.000 | no | Rh1+ | - | -8.58 | -7.79 |
| 185344445308 | 68 | 34... Rh8+ | good | miss (mate) | mate_override | mistake | 0.1055 | 1.000 | no | Qd2 | - | -6.82 | -7.32 |
| 185344445308 | 70 | 35... Qd1+ | good | miss (mate) | mate_override | mistake | 0.1326 | 1.000 | no | Qd4+ | - | -6.70 | -6.43 |
| 185344445308 | 91 | 46. Re3 | good | inaccuracy | mate_override | inaccuracy | 0.0545 | 0.055 | no | Ke4 | - | -M5 | -M9 |
| 185362589181 | 86 | 43... Bxg4 | good | miss (mate) | mate_override | mistake | 0.1318 | 1.000 | no | Qxg4 | - | -2.87 | -2.96 |

### `losing_material_hardened` (7)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185466827454 | 61 | 31. Rxf2 | excellent | mistake | losing_material_hardened | excellent | 0.0000 | 0.043 | no | Ra1 | - | -11.6 | -10.02 |
| 185476493194 | 40 | 20... Rae8 | good | mistake | losing_material_hardened | excellent | 0.0172 | 0.087 | no | Be2 | - | +9.13 | +8.80 |
| 185221110711 | 61 | 31. g5 | good | mistake | losing_material_hardened | inaccuracy | 0.0641 | 0.132 | no | Bb5 | - | -3.87 | -4.10 |
| 185221110711 | 75 | 38. f6 | good | mistake | losing_material_hardened | inaccuracy | 0.0570 | 0.073 | no | Rxe2 | - | -6.68 | -6.42 |
| 185221110711 | 81 | 41. Nf4 | excellent | mistake | losing_material_hardened | excellent | 0.0020 | 0.041 | no | Nd4 | - | -4.99 | -5.01 |
| 185344445308 | 75 | 38. Re3 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0815 | 0.124 | no | Kf3 | - | -M5 | -9.72 |
| 185363112760 | 68 | 34... Rd8 | excellent | mistake | losing_material_hardened | excellent | 0.0034 | 0.059 | no | Qe7 | - | +4.30 | +4.84 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185466827454 | 32 | 16... Kg8 | best | great | great_find_event | best | 0.0000 | 0.434 | yes | Kg8 | - | +0.78 | +0.82 |
| 185221110711 | 58 | 29... Kh8 | best | great | great_find_event | best | 0.0000 | 0.806 | yes | Kh8 | - | -2.29 | -2.53 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185476493194 | 11 | 6. Nc3 | excellent | book | book | excellent | 0.0059 | 0.513 | no | a4 | - | +0.18 | +0.10 |
| 185311691496 | 7 | 4. Bc4 | inaccuracy | book | book | inaccuracy | 0.0597 | 0.536 | no | e5 | e5 | -0.29 | -0.34 |

### `brilliant_event` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184740374128 | 49 | 25. Qxb7+ | best | brilliant | brilliant_event | best | 0.0000 | 0.228 | yes | Qxb7+ | - | -4.47 | -4.46 |

