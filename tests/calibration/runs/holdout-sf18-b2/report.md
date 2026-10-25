# Calibration report: holdout-sf18-b2

- Generated: 2026-10-18T14:15:18+00:00
- Commit: `740f5a2b4756` + uncommitted backend changes (diff sha256 `78d53b3a9776`)
- Engine: Stockfish 18; depth 18, multipv 3; config override: none
- Games: 18 requested, 18 compared, 0 skipped (list: `tests/calibration/holdout.txt`)
- Plies: 1248 aligned, 1248 scored, 0 excluded (none)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 68.0% (849/1248) |
| Within one step | 87.9% (1097/1248) |
| Brilliant precision / recall | 0.50 / 0.33 |
| Great precision / recall | 0.71 / 0.12 |
| Brilliant per 100 moves (app / ours) | 0.24 / 0.16 |
| Great per 100 moves (app / ours) | 3.37 / 0.56 |
| Accuracy mean abs. difference | 3.65 (n=36, max 11.12) |
| Accuracy bias (ours - app) | +2.63 |
| Best move = app's suggestion | 79.4% (170/214 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **1** | . | 2 | . | . | . | . | . | . | . | 3 |
| **great** | . | **5** | 37 | . | . | . | . | . | . | . | 42 |
| **best** | 1 | 2 | **362** | 45 | 5 | . | . | . | . | . | 415 |
| **excellent** | . | . | 46 | **112** | 27 | 1 | 2 | 2 | . | . | 190 |
| **good** | . | . | 10 | 45 | **78** | . | 25 | 4 | 3 | . | 165 |
| **book** | . | . | 23 | 7 | 3 | **102** | . | . | . | . | 135 |
| **inaccuracy** | . | . | 4 | 9 | 29 | 1 | **80** | 9 | 4 | . | 136 |
| **mistake** | . | . | 1 | 4 | 4 | . | 16 | **57** | 7 | 2 | 91 |
| **miss** | . | . | . | . | 4 | . | 4 | 2 | **32** | 1 | 43 |
| **blunder** | . | . | . | . | . | . | . | 4 | 4 | **20** | 28 |
| **total** | 2 | 7 | 485 | 222 | 150 | 104 | 127 | 78 | 50 | 23 | 1248 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 3 | 2 | 1 | 0.500 | 0.333 | 0.400 |
| great | 42 | 7 | 5 | 0.714 | 0.119 | 0.204 |
| best | 415 | 485 | 362 | 0.746 | 0.872 | 0.804 |
| excellent | 190 | 222 | 112 | 0.505 | 0.589 | 0.544 |
| good | 165 | 150 | 78 | 0.520 | 0.473 | 0.495 |
| book | 135 | 104 | 102 | 0.981 | 0.756 | 0.854 |
| inaccuracy | 136 | 127 | 80 | 0.630 | 0.588 | 0.608 |
| mistake | 91 | 78 | 57 | 0.731 | 0.626 | 0.675 |
| miss | 43 | 50 | 32 | 0.640 | 0.744 | 0.688 |
| blunder | 28 | 23 | 20 | 0.870 | 0.714 | 0.784 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 185387411150 | white | 77.9 | 78.8 | +0.9 |
| 185387411150 | black | 75.5 | 75.7 | +0.2 |
| 185425961522 | white | 58.9 | 62.7 | +3.8 |
| 185425961522 | black | 55.0 | 58.8 | +3.8 |
| 185439816356 | white | 59.1 | 62.9 | +3.8 |
| 185439816356 | black | 81.9 | 87.6 | +5.7 |
| 185466827454 | white | 73.1 | 78.1 | +5.0 |
| 185466827454 | black | 77.5 | 83.2 | +5.7 |
| 185476493194 | white | 61.7 | 58.7 | -3.0 |
| 185476493194 | black | 56.1 | 45.9 | -10.2 |
| 994221268 | white | 87.7 | 90.1 | +2.4 |
| 994221268 | black | 93.4 | 96.4 | +3.0 |
| 184740374128 | white | 56.2 | 58.3 | +2.1 |
| 184740374128 | black | 64.2 | 68.3 | +4.1 |
| 185101208706 | white | 52.3 | 49.7 | -2.6 |
| 185101208706 | black | 58.9 | 57.0 | -1.9 |
| 185137444946 | white | 79.0 | 82.8 | +3.8 |
| 185137444946 | black | 65.6 | 69.9 | +4.3 |
| 185151408586 | white | 82.3 | 85.9 | +3.6 |
| 185151408586 | black | 80.6 | 81.9 | +1.3 |
| 185221110711 | white | 78.2 | 84.7 | +6.5 |
| 185221110711 | black | 88.1 | 89.1 | +1.0 |
| 185311691496 | white | 81.4 | 86.5 | +5.1 |
| 185311691496 | black | 64.8 | 67.3 | +2.5 |
| 185344445308 | white | 60.1 | 65.6 | +5.5 |
| 185344445308 | black | 60.5 | 59.9 | -0.6 |
| 185362589181 | white | 65.5 | 76.6 | +11.1 |
| 185362589181 | black | 70.0 | 76.1 | +6.1 |
| 185363112760 | white | 83.0 | 85.0 | +2.0 |
| 185363112760 | black | 88.5 | 89.5 | +1.0 |
| 185468237512 | white | 71.7 | 74.4 | +2.7 |
| 185468237512 | black | 69.9 | 74.4 | +4.5 |
| 185961991257 | white | 91.6 | 93.9 | +2.3 |
| 185961991257 | black | 84.1 | 88.5 | +4.4 |
| 186393389351 | white | 89.3 | 92.5 | +3.2 |
| 186393389351 | black | 86.0 | 87.7 | +1.7 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 185387411150 | 57 | 57 | 68.4% | 75.4% | reviewed | 30.6 |
| 185425961522 | 47 | 47 | 74.5% | 93.6% | reviewed | 51.2 |
| 185439816356 | 15 | 15 | 93.3% | 100.0% | reviewed | 12.6 |
| 185466827454 | 62 | 62 | 64.5% | 85.5% | reviewed | 33.2 |
| 185476493194 | 43 | 43 | 69.8% | 88.4% | reviewed | 49.2 |
| 994221268 | 86 | 86 | 64.0% | 89.5% | reviewed | 60.8 |
| 184740374128 | 58 | 58 | 70.7% | 87.9% | reviewed | 58.2 |
| 185101208706 | 46 | 46 | 71.7% | 84.8% | reviewed | 62.8 |
| 185137444946 | 57 | 57 | 75.4% | 91.2% | reviewed | 62.3 |
| 185151408586 | 42 | 42 | 85.7% | 97.6% | reviewed | 38.7 |
| 185221110711 | 98 | 98 | 67.3% | 87.8% | reviewed | 77.8 |
| 185311691496 | 37 | 37 | 78.4% | 89.2% | reviewed | 37.2 |
| 185344445308 | 92 | 92 | 67.4% | 90.2% | reviewed | 60.3 |
| 185362589181 | 128 | 128 | 67.2% | 89.1% | reviewed | 97.9 |
| 185363112760 | 84 | 84 | 52.4% | 78.6% | reviewed | 75.3 |
| 185468237512 | 112 | 112 | 75.9% | 93.8% | reviewed | 97.9 |
| 185961991257 | 95 | 95 | 52.6% | 83.2% | reviewed | 87.8 |
| 186393389351 | 89 | 89 | 68.5% | 87.6% | reviewed | 72.3 |

## Mismatches by rule (399)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 366 | excellent -> best x46, best -> excellent x45, good -> excellent x45, great -> best x37, inaccuracy -> good x29, excellent -> good x26 |
| `miss_detector` | 15 | mistake -> miss x7, inaccuracy -> miss x4, blunder -> miss x4 |
| `mate_override` | 6 | good -> miss x3, excellent -> inaccuracy x1, excellent -> good x1, mistake -> inaccuracy x1 |
| `losing_material_hardened` | 5 | good -> mistake x3, excellent -> mistake x2 |
| `great_find_event` | 2 | best -> great x2 |
| `book` | 2 | excellent -> book x1, inaccuracy -> book x1 |
| `blunder_softened` | 2 | blunder -> mistake x2 |
| `brilliant_event` | 1 | best -> brilliant x1 |

### `precision` (366)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185387411150 | 7 | 4. Bd3 | book | good | precision | good | 0.0290 | 0.539 | no | Nf3 | - | +0.19 | +0.14 |
| 185387411150 | 8 | 4... Bxd3 | book | best | precision | best | 0.0000 | 0.490 | yes | Bxd3 | - | +0.19 | +0.23 |
| 185387411150 | 9 | 5. Qxd3 | book | best | precision | best | 0.0000 | 0.516 | yes | Qxd3 | - | +0.19 | +0.24 |
| 185387411150 | 17 | 9. Bg5 | good | inaccuracy | precision | inaccuracy | 0.0580 | 0.544 | no | Bf4 | - | -0.08 | -0.20 |
| 185387411150 | 25 | 13. c3 | inaccuracy | good | precision | good | 0.0473 | 0.649 | no | Nc3 | Nc3 | +1.24 | +1.62 |
| 185387411150 | 27 | 14. exf6 | great | best | precision | best | 0.0000 | 0.748 | yes | exf6 | - | +3.75 | +3.87 |
| 185387411150 | 34 | 17... Rd2 | mistake | inaccuracy | precision | inaccuracy | 0.0771 | 0.163 | no | gxf6 | - | +8.32 | +8.56 |
| 185387411150 | 35 | 18. fxg7 | great | best | precision | best | 0.0000 | 0.915 | yes | fxg7 | - | +8.32 | +8.64 |
| 185387411150 | 36 | 18... Rg8 | mistake | excellent | precision | excellent | 0.0179 | 0.084 | no | Qd8 | - | +8.79 | +9.58 |
| 185387411150 | 39 | 20. Bg3+ | best | good | precision | good | 0.0210 | 0.935 | no | Qxg8 | - | +8.79 | +8.98 |
| 185387411150 | 43 | 22. Qxg8 | best | excellent | precision | excellent | 0.0031 | 0.930 | no | Bxd6 | - | +8.79 | +9.70 |
| 185387411150 | 46 | 23... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 50 | 25... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 52 | 26... Qh5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qh5+ | - | 0.00 | +0.00 |
| 185387411150 | 54 | 27... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 56 | 28... Qh5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qh5+ | - | 0.00 | +0.00 |
| 185425961522 | 12 | 6... Qe6 | mistake | inaccuracy | precision | inaccuracy | 0.0907 | 0.462 | no | Qb6 | - | +1.82 | +1.84 |
| 185425961522 | 15 | 8. O-O | good | excellent | precision | excellent | 0.0080 | 0.629 | no | Nc3 | - | +1.73 | +1.58 |
| 185425961522 | 17 | 9. Qf4 | miss | inaccuracy | precision | inaccuracy | 0.0733 | 0.725 | no | Nc3 | Nc3 | +1.74 | +2.19 |
| 185425961522 | 18 | 9... Qg6 | inaccuracy | good | precision | good | 0.0236 | 0.348 | no | Nh6 | Nh6 | +2.52 | +2.47 |
| 185425961522 | 22 | 11... Be6 | blunder | mistake | precision | mistake | 0.1885 | 0.398 | no | c6 | - | +4.41 | +4.65 |
| 185425961522 | 40 | 20... Nh5 | mistake | inaccuracy | precision | inaccuracy | 0.0696 | 0.124 | no | Nxg2 | - | +8.57 | +9.99 |
| 185425961522 | 41 | 21. Nc6 | good | inaccuracy | precision | inaccuracy | 0.0511 | 0.946 | no | Qa8+ | - | +7.26 | +7.48 |
| 185425961522 | 42 | 21... O-O | best | excellent | precision | excellent | 0.0035 | 0.106 | no | Qg5 | - | +7.26 | +7.84 |
| 185425961522 | 43 | 22. Bd6 | excellent | good | precision | good | 0.0218 | 0.904 | no | Rac1 | - | +7.01 | +7.04 |
| 185425961522 | 47 | 24. d7 | best | excellent | precision | excellent | 0.0083 | 0.952 | no | Ne7+ | - | +9.38 | +9.90 |
| 185439816356 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0240 | 0.568 | no | d4 | - | +0.65 | +0.71 |
| 185466827454 | 11 | 6. Bd3 | book | best | precision | best | 0.0000 | 0.493 | yes | Bd3 | - | -0.12 | -0.24 |
| 185466827454 | 12 | 6... dxe4 | book | best | precision | best | 0.0000 | 0.518 | yes | dxe4 | - | -0.12 | -0.13 |
| 185466827454 | 13 | 7. Bxe4 | book | best | precision | best | 0.0000 | 0.490 | yes | Bxe4 | - | -0.12 | -0.12 |
| 185466827454 | 16 | 8... Be6 | good | excellent | precision | excellent | 0.0132 | 0.481 | no | a5 | - | +0.60 | +0.44 |
| 185466827454 | 19 | 10. cxd4 | excellent | good | precision | good | 0.0300 | 0.488 | no | Bxc6+ | - | -0.40 | -0.39 |
| 185466827454 | 27 | 14. Bc6+ | good | excellent | precision | excellent | 0.0081 | 0.511 | no | Qa4+ | - | -0.08 | -0.03 |
| 185466827454 | 34 | 17... Be5 | good | excellent | precision | excellent | 0.0130 | 0.445 | no | Bxe3 | - | +1.05 | +0.93 |
| 185466827454 | 40 | 20... h6 | inaccuracy | good | precision | good | 0.0302 | 0.889 | no | Qa6 | Qa6 | -5.82 | -6.16 |
| 185466827454 | 43 | 22. Bf3 | mistake | excellent | precision | excellent | 0.0151 | 0.151 | no | f5 | - | -6.29 | -6.35 |
| 185466827454 | 44 | 22... Bc5+ | good | excellent | precision | excellent | 0.0139 | 0.866 | no | Qxf4 | - | -5.74 | -5.96 |
| 185466827454 | 45 | 23. Kh1 | inaccuracy | good | precision | good | 0.0257 | 0.148 | no | Bxc5 | - | -7.22 | -6.60 |
| 185466827454 | 46 | 23... Rxd1 | best | excellent | precision | excellent | 0.0000 | 0.874 | no | Qxf1+ | - | -7.22 | -7.63 |
| 185466827454 | 53 | 27. Re1 | excellent | best | precision | best | 0.0000 | 0.068 | yes | Re1 | - | -8.57 | -9.12 |
| 185466827454 | 54 | 27... Bg4 | best | excellent | precision | excellent | 0.0000 | 0.936 | no | Rf8 | - | -8.57 | -M12 |
| 185466827454 | 55 | 28. Be4+ | excellent | best | precision | best | 0.0000 | 0.000 | yes | Be4+ | - | -9.21 | -14.00 |
| 185466827454 | 56 | 28... g6 | best | good | precision | good | 0.0252 | 0.984 | no | f5 | - | -9.21 | -M12 |
| 185466827454 | 57 | 29. h3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | Bd3 | - | -M7 | -M9 |
| 185466827454 | 59 | 30. Rf1 | good | best | precision | best | 0.0000 | 0.000 | yes | Rf1 | - | -M7 | -M9 |
| 185466827454 | 60 | 30... Be2 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qxe4 | - | -10.4 | -M11 |
| 185466827454 | 61 | 31. Rxf2 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Rxf2 | - | -11.6 | -12.21 |
| 185476493194 | 6 | 3... Bc5 | book | good | precision | good | 0.0250 | 0.507 | no | c6 | - | +0.21 | +0.24 |
| 185476493194 | 7 | 4. Nf3 | book | best | precision | best | 0.0000 | 0.518 | yes | Nf3 | - | +0.21 | +0.22 |
| 185476493194 | 13 | 7. Bg5 | best | excellent | precision | excellent | 0.0059 | 0.521 | no | Na4 | - | +0.21 | +0.24 |
| 185476493194 | 16 | 8... Nd4 | excellent | good | precision | good | 0.0257 | 0.516 | no | Bg4 | - | +0.26 | +0.31 |
| 185476493194 | 17 | 9. Nxd4 | excellent | best | precision | best | 0.0000 | 0.523 | yes | Nxd4 | - | +0.19 | +0.33 |
| 185476493194 | 26 | 13... g5 | mistake | inaccuracy | precision | inaccuracy | 0.0520 | 0.217 | no | Qg4 | - | +5.10 | +5.51 |
| 185476493194 | 33 | 17. Nf6 | inaccuracy | mistake | precision | mistake | 0.1153 | 0.786 | no | Qf6+ | - | +2.40 | +2.43 |
| 185476493194 | 39 | 20. c3 | good | excellent | precision | excellent | 0.0123 | 0.924 | no | Qg5+ | - | +7.53 | +7.93 |
| 185476493194 | 42 | 21... Bg6 | mistake | excellent | precision | excellent | 0.0091 | 0.048 | no | Kh8 | Kh7 | +9.17 | +10.52 |
| 185476493194 | 43 | 22. cxd4 | excellent | good | precision | good | 0.0249 | 0.956 | no | Qxg6+ | - | +8.14 | +8.85 |
| 994221268 | 6 | 3... a6 | book | excellent | precision | excellent | 0.0177 | 0.501 | no | c5 | - | +0.10 | +0.15 |
| 994221268 | 7 | 4. e3 | book | best | precision | best | 0.0000 | 0.517 | yes | e3 | - | +0.10 | +0.13 |
| 994221268 | 9 | 5. Be2 | good | inaccuracy | precision | inaccuracy | 0.0552 | 0.541 | no | Qd2 | - | -0.04 | -0.13 |
| 994221268 | 14 | 7... c5 | excellent | best | precision | best | 0.0000 | 0.525 | yes | c5 | - | -0.20 | -0.25 |
| 994221268 | 16 | 8... Nc6 | best | excellent | precision | excellent | 0.0154 | 0.543 | no | Be7 | - | -0.27 | -0.25 |
| 994221268 | 19 | 10. Nec3 | good | excellent | precision | excellent | 0.0154 | 0.473 | no | b3 | - | -0.49 | -0.38 |
| 994221268 | 23 | 12. Nc5 | excellent | good | precision | good | 0.0409 | 0.500 | no | b3 | - | -0.45 | -0.37 |
| 994221268 | 24 | 12... b6 | best | excellent | precision | excellent | 0.0055 | 0.541 | no | Qc7 | - | -0.45 | -0.39 |
| 994221268 | 25 | 13. N5a4 | great | best | precision | best | 0.0000 | 0.457 | yes | N5a4 | - | -0.45 | -0.41 |
| 994221268 | 26 | 13... Rb8 | excellent | good | precision | good | 0.0242 | 0.545 | no | Ne7 | - | -0.43 | -0.19 |
| 994221268 | 27 | 14. Qe2 | excellent | good | precision | good | 0.0308 | 0.479 | no | b3 | - | -0.47 | -0.47 |
| 994221268 | 36 | 18... Nxd4 | brilliant | best | precision | best | 0.0000 | 0.600 | yes | Nxd4 | - | -0.93 | -0.89 |
| 994221268 | 37 | 19. Rxd4 | excellent | best | precision | best | 0.0000 | 0.403 | yes | Rxd4 | - | -1.05 | -0.89 |
| 994221268 | 39 | 20. Qd1 | good | inaccuracy | precision | inaccuracy | 0.0673 | 0.409 | no | Qf2 | - | -1.27 | -1.48 |
| 994221268 | 41 | 21. Kh1 | good | excellent | precision | excellent | 0.0142 | 0.362 | no | Qd2 | - | -1.45 | -1.42 |
| 994221268 | 42 | 21... Rd7 | good | excellent | precision | excellent | 0.0152 | 0.652 | no | h6 | - | -1.17 | -1.19 |
| 994221268 | 44 | 22... Rfd8 | excellent | good | precision | good | 0.0205 | 0.645 | no | Re8 | - | -1.25 | -1.26 |
| 994221268 | 45 | 23. Rd1 | best | excellent | precision | excellent | 0.0132 | 0.364 | no | Re1 | - | -1.25 | -1.41 |
| 994221268 | 48 | 24... axb4 | good | best | precision | best | 0.0000 | 0.617 | yes | axb4 | - | -0.97 | -0.95 |
| 994221268 | 50 | 25... Qxb4 | excellent | best | precision | best | 0.0000 | 0.607 | yes | Qxb4 | - | -0.88 | -1.04 |
| 994221268 | 52 | 26... Qxd2 | great | best | precision | best | 0.0000 | 0.782 | yes | Qxd2 | - | -2.89 | -2.92 |
| 994221268 | 54 | 27... b4 | excellent | best | precision | best | 0.0000 | 0.820 | yes | b4 | - | -3.15 | -3.44 |
| 994221268 | 55 | 28. g4 | good | excellent | precision | excellent | 0.0083 | 0.179 | no | Rd1 | - | -3.55 | -3.57 |
| 994221268 | 57 | 29. h4 | best | excellent | precision | excellent | 0.0091 | 0.183 | no | Rd1 | - | -3.21 | -3.45 |
| 994221268 | 59 | 30. g5 | excellent | best | precision | best | 0.0000 | 0.199 | yes | g5 | - | -3.14 | -3.23 |
| 994221268 | 62 | 31... Nh5 | good | best | precision | best | 0.0000 | 0.808 | yes | Nh5 | - | -2.43 | -3.19 |
| 994221268 | 63 | 32. Kh2 | inaccuracy | excellent | precision | excellent | 0.0142 | 0.196 | no | Kg2 | Kg2 | -3.24 | -3.40 |
| 994221268 | 65 | 33. Ng3 | inaccuracy | excellent | precision | excellent | 0.0126 | 0.202 | no | Rh4 | - | -3.37 | -3.68 |
| 994221268 | 68 | 34... Red7 | best | excellent | precision | excellent | 0.0044 | 0.831 | no | Rb7 | - | -3.37 | -3.64 |
| 994221268 | 82 | 41... Ke6 | excellent | best | precision | best | 0.0000 | 0.910 | yes | Ke6 | - | -4.68 | -5.21 |
| 994221268 | 86 | 43... Kxf4 | excellent | best | precision | best | 0.0000 | 0.923 | yes | Kxf4 | - | -5.17 | -5.57 |
| 184740374128 | 6 | 3... Bb4 | book | excellent | precision | excellent | 0.0148 | 0.489 | no | Nc6 | - | +0.45 | +0.47 |
| 184740374128 | 7 | 4. Nxe5 | book | best | precision | best | 0.0000 | 0.529 | yes | Nxe5 | - | +0.45 | +0.42 |
| 184740374128 | 9 | 5. bxc3 | good | excellent | precision | excellent | 0.0062 | 0.527 | no | dxc3 | - | +0.04 | +0.17 |
| 184740374128 | 14 | 7... Qxe4+ | inaccuracy | good | precision | good | 0.0458 | 0.530 | no | Nxe4 | Nxe4 | +0.41 | +0.50 |
| 184740374128 | 21 | 11. c4 | inaccuracy | good | precision | good | 0.0449 | 0.560 | no | Kd2 | Kd2 | +0.28 | +0.25 |
| 184740374128 | 26 | 13... Nh5 | good | excellent | precision | excellent | 0.0186 | 0.504 | no | b6 | - | +0.38 | +0.37 |
| 184740374128 | 27 | 14. O-O | best | excellent | precision | excellent | 0.0019 | 0.523 | no | Kf1 | - | +0.38 | +0.38 |
| 184740374128 | 29 | 15. a5 | inaccuracy | good | precision | good | 0.0291 | 0.638 | no | Qd2 | Qd2 | +1.31 | +1.79 |
| 184740374128 | 30 | 15... a6 | mistake | inaccuracy | precision | inaccuracy | 0.0909 | 0.391 | no | Qf6 | - | +3.47 | +3.42 |
| 184740374128 | 33 | 17. Bg5 | miss | inaccuracy | precision | inaccuracy | 0.0964 | 0.656 | no | Qb3 | Rb1 | +0.98 | +0.97 |
| 184740374128 | 35 | 18. Bxf6 | mistake | blunder | precision | blunder | 0.2840 | 0.654 | no | Bf5+ | Bf5+ | -1.75 | -2.15 |
| 184740374128 | 38 | 19... Rxd5 | excellent | best | precision | best | 0.0000 | 0.696 | yes | Rxd5 | - | -2.48 | -3.54 |
| 184740374128 | 48 | 24... Rh5 | great | best | precision | best | 0.0000 | 0.766 | yes | Rh5 | - | -4.47 | -4.50 |
| 184740374128 | 56 | 28... Rxh4+ | best | excellent | precision | excellent | 0.0029 | 0.881 | no | g5 | - | -7.50 | -8.00 |
| 185101208706 | 6 | 3... Nf6 | good | excellent | precision | excellent | 0.0118 | 0.521 | no | d5 | - | -0.10 | -0.22 |
| 185101208706 | 7 | 4. d4 | good | excellent | precision | excellent | 0.0097 | 0.485 | no | e4 | - | -0.48 | -0.30 |
| 185101208706 | 17 | 9. Ng5 | good | inaccuracy | precision | inaccuracy | 0.0572 | 0.750 | no | Qe5+ | - | +3.08 | +2.94 |
| 185101208706 | 18 | 9... Qe7+ | excellent | good | precision | good | 0.0364 | 0.307 | no | f6 | - | +3.45 | +3.58 |
| 185101208706 | 20 | 10... h6 | excellent | good | precision | good | 0.0319 | 0.281 | no | O-O-O | - | +3.71 | +3.97 |
| 185101208706 | 24 | 12... O-O-O | best | good | precision | good | 0.0237 | 0.376 | no | h5 | - | +1.85 | +2.04 |
| 185101208706 | 28 | 14... Qe4 | best | excellent | precision | excellent | 0.0194 | 0.333 | no | Qg5 | - | +2.35 | +2.83 |
| 185101208706 | 29 | 15. O-O | great | best | precision | best | 0.0000 | 0.687 | yes | O-O | - | +2.35 | +3.32 |
| 185101208706 | 37 | 19. Bxf5+ | mistake | good | precision | good | 0.0247 | 0.130 | no | Bxf4 | - | -6.56 | -7.72 |
| 185101208706 | 40 | 20... Bxh2+ | brilliant | best | precision | best | 0.0000 | 1.000 | yes | Bxh2+ | - | -M4 | -M5 |
| 185137444946 | 4 | 2... e6 | book | best | precision | best | 0.0000 | 0.440 | yes | e6 | - | +0.92 | +0.98 |
| 185137444946 | 7 | 4. d5 | good | inaccuracy | precision | inaccuracy | 0.0553 | 0.553 | no | Bd3 | - | +0.04 | -0.03 |
| 185137444946 | 11 | 6. Nf3 | good | excellent | precision | excellent | 0.0050 | 0.588 | no | h4 | - | +1.06 | +1.15 |
| 185137444946 | 12 | 6... h6 | inaccuracy | good | precision | good | 0.0398 | 0.417 | no | d6 | d6 | +1.61 | +1.72 |
| 185137444946 | 17 | 9. h3 | excellent | best | precision | best | 0.0000 | 0.691 | yes | h3 | - | +2.60 | +2.70 |
| 185137444946 | 29 | 15. Bb2 | best | excellent | precision | excellent | 0.0019 | 0.689 | no | Ne2 | - | +2.55 | +2.75 |
| 185137444946 | 34 | 17... cxd6 | great | best | precision | best | 0.0000 | 0.421 | yes | cxd6 | - | +0.96 | +1.27 |
| 185137444946 | 36 | 18... Bf6 | great | best | precision | best | 0.0000 | 0.419 | yes | Bf6 | - | +0.96 | +1.00 |
| 185137444946 | 37 | 19. Qe2 | miss | mistake | precision | mistake | 0.1140 | 0.572 | no | cxb5 | cxb5 | -0.66 | -0.57 |
| 185137444946 | 38 | 19... Nc6 | miss | inaccuracy | precision | inaccuracy | 0.0780 | 0.542 | no | bxc4 | bxc4 | +0.87 | +0.50 |
| 185137444946 | 41 | 21. Bxf6 | good | inaccuracy | precision | inaccuracy | 0.0659 | 0.679 | no | Nxf6+ | - | +1.56 | +1.45 |
| 185137444946 | 43 | 22. Nc7+ | good | excellent | precision | excellent | 0.0091 | 0.599 | no | cxb5 | - | +1.28 | +1.28 |
| 185137444946 | 44 | 22... Rxc7 | excellent | good | precision | good | 0.0237 | 0.408 | no | Kf8 | - | +1.48 | +1.40 |
| 185137444946 | 50 | 25... Nxb5 | excellent | good | precision | good | 0.0250 | 0.323 | no | Qb6 | - | +2.85 | +3.07 |
| 185151408586 | 12 | 6... Qe7 | mistake | inaccuracy | precision | inaccuracy | 0.0853 | 0.471 | no | Nf6 | c6 | +1.74 | +1.59 |
| 185151408586 | 13 | 7. O-O | inaccuracy | good | precision | good | 0.0374 | 0.615 | no | Bf4 | Bf4 | +1.18 | +1.06 |
| 185151408586 | 16 | 8... g6 | excellent | good | precision | good | 0.0331 | 0.450 | no | c6 | - | +0.86 | +1.14 |
| 185151408586 | 17 | 9. Bg5 | good | inaccuracy | precision | inaccuracy | 0.0521 | 0.583 | no | Bb5+ | - | +0.51 | +0.57 |
| 185151408586 | 34 | 17... Qf6 | best | excellent | precision | excellent | 0.0033 | 0.803 | no | Bd7 | - | -4.50 | -4.90 |
| 185151408586 | 35 | 18. Rxe5 | mistake | excellent | precision | excellent | 0.0041 | 0.192 | no | Qe2 | - | -4.52 | -4.86 |
| 185221110711 | 3 | 2. Nc3 | book | best | precision | best | 0.0000 | 0.591 | no | e4 | - | +0.58 | +0.51 |
| 185221110711 | 6 | 3... e5 | excellent | best | precision | best | 0.0000 | 0.389 | yes | e5 | - | +0.75 | +0.86 |
| 185221110711 | 7 | 4. a4 | good | inaccuracy | precision | inaccuracy | 0.0578 | 0.634 | no | f4 | - | +0.58 | +0.48 |
| 185221110711 | 8 | 4... Nd7 | excellent | best | precision | best | 0.0000 | 0.424 | yes | Nd7 | - | +0.59 | +0.62 |
| 185221110711 | 9 | 5. Nf3 | excellent | best | precision | best | 0.0000 | 0.597 | yes | Nf3 | - | +0.53 | +0.58 |
| 185221110711 | 10 | 5... Ngf6 | book | best | precision | best | 0.0000 | 0.409 | yes | Ngf6 | - | +0.56 | +0.54 |
| 185221110711 | 19 | 10. Be3 | best | excellent | precision | excellent | 0.0015 | 0.614 | no | Ba2 | - | +0.76 | +0.69 |
| 185221110711 | 20 | 10... exd4 | best | excellent | precision | excellent | 0.0030 | 0.392 | no | h6 | - | +0.76 | +0.69 |
| 185221110711 | 21 | 11. Qxd4 | inaccuracy | good | precision | good | 0.0307 | 0.608 | no | Nxd4 | Nxd4 | +0.39 | +0.47 |
| 185221110711 | 30 | 15... d5 | great | best | precision | best | 0.0000 | 0.591 | yes | d5 | - | -0.41 | -0.54 |
| 185221110711 | 32 | 16... Nd7 | great | best | precision | best | 0.0000 | 0.597 | yes | Nd7 | - | -0.64 | -0.64 |
| 185221110711 | 43 | 22. g4 | good | inaccuracy | precision | inaccuracy | 0.0664 | 0.448 | no | Qb6 | - | -0.59 | -0.76 |
| 185221110711 | 47 | 24. Nxd5 | great | best | precision | best | 0.0000 | 0.478 | yes | Nxd5 | - | -0.18 | -0.10 |
| 185221110711 | 52 | 26... Re3 | great | best | precision | best | 0.0000 | 0.522 | yes | Re3 | - | -0.18 | -0.18 |
| 185221110711 | 54 | 27... Bxa4 | inaccuracy | good | precision | good | 0.0271 | 0.514 | no | Rc8 | - | +0.27 | +0.03 |
| 185221110711 | 59 | 30. Ne6 | good | inaccuracy | precision | inaccuracy | 0.0763 | 0.188 | no | g5 | - | -3.01 | -3.26 |
| 185221110711 | 60 | 30... Rc8 | great | best | precision | best | 0.0000 | 0.889 | yes | Rc8 | - | -3.01 | -3.68 |
| 185221110711 | 61 | 31. g5 | good | excellent | precision | excellent | 0.0119 | 0.088 | no | Bb5 | - | -3.87 | -3.93 |
| 185221110711 | 67 | 34. Rf2 | best | excellent | precision | excellent | 0.0120 | 0.085 | no | Bb4 | - | -3.52 | -3.99 |
| 185221110711 | 68 | 34... d3 | excellent | best | precision | best | 0.0000 | 0.927 | yes | d3 | - | -3.36 | -3.71 |
| 185221110711 | 71 | 36. Kg2 | good | best | precision | best | 0.0000 | 0.053 | yes | Kg2 | - | -4.18 | -4.67 |
| 185221110711 | 78 | 39... Nxf6 | excellent | good | precision | good | 0.0312 | 0.992 | no | d1=Q | - | -4.95 | -5.01 |
| 185221110711 | 85 | 43. Kxf4 | best | excellent | precision | excellent | 0.0013 | 0.002 | no | Ke4 | - | -7.93 | -11.58 |
| 185221110711 | 89 | 45. Kf3 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kf3 | - | -9.29 | -M12 |
| 185221110711 | 91 | 46. Kg4 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kg4 | Kf4 | -M9 | -M8 |
| 185221110711 | 92 | 46... b5 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qe3 | - | -10.5 | -M9 |
| 185311691496 | 13 | 7. Bxf6 | good | excellent | precision | excellent | 0.0057 | 0.514 | no | Bh4 | - | +0.10 | +0.08 |
| 185311691496 | 16 | 8... d6 | mistake | inaccuracy | precision | inaccuracy | 0.0878 | 0.493 | no | Nc6 | Nc6 | +1.55 | +1.35 |
| 185311691496 | 23 | 12. Ne4 | best | excellent | precision | excellent | 0.0051 | 0.661 | no | Bxe6 | - | +2.46 | +2.37 |
| 185311691496 | 27 | 14. Bxe6 | great | best | precision | best | 0.0000 | 0.655 | yes | Bxe6 | - | +2.21 | +2.37 |
| 185311691496 | 30 | 15... Ne7 | inaccuracy | mistake | precision | mistake | 0.1210 | 0.346 | no | Kd7 | - | +3.98 | +4.35 |
| 185344445308 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0130 | 0.566 | no | d4 | - | +0.74 | +0.68 |
| 185344445308 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.451 | yes | Bb7 | - | +0.74 | +0.68 |
| 185344445308 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.549 | yes | Nc3 | - | +0.74 | +0.73 |
| 185344445308 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.447 | yes | e6 | - | +0.74 | +0.66 |
| 185344445308 | 13 | 7. d4 | excellent | best | precision | best | 0.0000 | 0.573 | yes | d4 | - | +0.87 | +0.98 |
| 185344445308 | 15 | 8. Bd2 | inaccuracy | good | precision | good | 0.0478 | 0.599 | no | a4 | O-O | +0.81 | +0.71 |
| 185344445308 | 17 | 9. O-O | best | excellent | precision | excellent | 0.0021 | 0.591 | no | Qe2 | - | +1.32 | +1.21 |
| 185344445308 | 18 | 9... Nf6 | best | excellent | precision | excellent | 0.0000 | 0.413 | no | Bxc3 | - | +1.32 | +1.17 |
| 185344445308 | 20 | 10... Ng4 | inaccuracy | mistake | precision | mistake | 0.1109 | 0.493 | no | O-O | O-O | +1.43 | +1.64 |
| 185344445308 | 23 | 12. Re1 | good | inaccuracy | precision | inaccuracy | 0.0580 | 0.675 | no | hxg4 | - | +1.72 | +1.63 |
| 185344445308 | 27 | 14. Bxe7 | good | inaccuracy | precision | inaccuracy | 0.0531 | 0.708 | no | dxc6 | - | +2.26 | +2.27 |
| 185344445308 | 29 | 15. hxg4 | inaccuracy | good | precision | good | 0.0494 | 0.659 | no | a4 | a4 | +1.52 | +1.52 |
| 185344445308 | 38 | 19... O-O-O | good | excellent | precision | excellent | 0.0091 | 0.402 | no | Rh7 | - | +1.61 | +1.52 |
| 185344445308 | 41 | 21. dxc6 | excellent | best | precision | best | 0.0000 | 0.500 | no | Qe7 | - | -0.19 | +0.00 |
| 185344445308 | 43 | 22. Bd5 | good | excellent | precision | excellent | 0.0058 | 0.500 | no | Qe7 | - | -0.64 | -0.16 |
| 185344445308 | 53 | 27. Rxd5 | inaccuracy | excellent | precision | excellent | 0.0087 | 0.104 | no | exd5 | exd5 | -7.68 | -8.39 |
| 185344445308 | 54 | 27... Nxe4 | best | excellent | precision | excellent | 0.0011 | 0.921 | no | Rh1+ | - | -7.68 | -8.87 |
| 185344445308 | 60 | 30... Rh8 | good | best | precision | best | 0.0000 | 0.950 | yes | Rh8 | - | -7.19 | -8.86 |
| 185344445308 | 62 | 31... Qd2 | excellent | best | precision | best | 0.0000 | 1.000 | yes | Qd2 | - | -M8 | -M10 |
| 185344445308 | 73 | 37. Re2 | good | excellent | precision | excellent | 0.0032 | 0.105 | no | Kf3 | - | -7.46 | -8.63 |
| 185344445308 | 78 | 39... Qh5+ | best | excellent | precision | excellent | 0.0000 | 0.913 | no | Qc6+ | - | -7.21 | -9.38 |
| 185344445308 | 80 | 40... Rd8 | best | excellent | precision | excellent | 0.0000 | 0.895 | no | Qh4+ | - | -7.21 | -7.89 |
| 185344445308 | 83 | 42. Re2 | excellent | best | precision | best | 0.0000 | 0.071 | no | Re3 | - | -7.24 | -9.70 |
| 185344445308 | 84 | 42... Qc5+ | best | good | precision | good | 0.0267 | 0.944 | no | Qg4 | - | -7.24 | -8.26 |
| 185344445308 | 86 | 43... Kb7 | good | inaccuracy | precision | inaccuracy | 0.0616 | 0.958 | no | Qc6+ | - | -6.62 | -7.39 |
| 185344445308 | 87 | 44. g4 | inaccuracy | mistake | precision | mistake | 0.1036 | 0.104 | no | Re5 | Re5 | -M12 | -M15 |
| 185344445308 | 90 | 45... Qc3+ | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qc6+ | - | -9.32 | -M11 |
| 185344445308 | 91 | 46. Re3 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Ke4 | - | -M5 | -M6 |
| 185362589181 | 3 | 2. h4 | good | inaccuracy | precision | inaccuracy | 0.0758 | 0.576 | no | e4 | - | +0.14 | +0.00 |
| 185362589181 | 6 | 3... e5 | excellent | good | precision | good | 0.0218 | 0.440 | no | c5 | - | +0.54 | +0.56 |
| 185362589181 | 10 | 5... c6 | excellent | good | precision | good | 0.0302 | 0.495 | no | Bg4 | - | +0.16 | +0.22 |
| 185362589181 | 11 | 6. Bg5 | mistake | inaccuracy | precision | inaccuracy | 0.0905 | 0.535 | no | e4 | e4 | -0.58 | -0.35 |
| 185362589181 | 18 | 9... d4 | great | best | precision | best | 0.0000 | 0.579 | yes | d4 | - | -0.58 | -0.56 |
| 185362589181 | 22 | 11... c5 | great | best | precision | best | 0.0000 | 0.573 | yes | c5 | - | -0.42 | -0.44 |
| 185362589181 | 23 | 12. g3 | mistake | inaccuracy | precision | inaccuracy | 0.0625 | 0.430 | no | b4 | b4 | -1.01 | -0.85 |
| 185362589181 | 24 | 12... Be6 | miss | good | precision | good | 0.0485 | 0.632 | no | Nbc6 | a5 | -0.50 | -0.53 |
| 185362589181 | 27 | 14. O-O | good | excellent | precision | excellent | 0.0101 | 0.352 | no | a3 | - | -1.08 | -1.00 |
| 185362589181 | 33 | 17. Qc2 | inaccuracy | good | precision | good | 0.0471 | 0.289 | no | Nh2 | Nh2 | -1.78 | -1.79 |
| 185362589181 | 34 | 17... a4 | mistake | inaccuracy | precision | inaccuracy | 0.0936 | 0.758 | no | g5 | g5 | -1.01 | -1.07 |
| 185362589181 | 35 | 18. cxd4 | miss | inaccuracy | precision | inaccuracy | 0.0925 | 0.336 | no | bxa4 | bxa4 | -1.65 | -1.78 |
| 185362589181 | 39 | 20. Ra1 | inaccuracy | excellent | precision | excellent | 0.0173 | 0.246 | no | Ne1 | Nh2 | -2.01 | -2.09 |
| 185362589181 | 42 | 21... Nb4 | best | excellent | precision | excellent | 0.0126 | 0.736 | no | Kh8 | - | -1.57 | -1.60 |
| 185362589181 | 45 | 23. Rfc1 | best | excellent | precision | excellent | 0.0140 | 0.202 | no | Ne1 | - | -2.10 | -2.29 |
| 185362589181 | 46 | 23... Qb5 | good | inaccuracy | precision | inaccuracy | 0.0704 | 0.811 | no | Kh8 | - | -1.78 | -1.65 |
| 185362589181 | 47 | 24. Bf1 | good | inaccuracy | precision | inaccuracy | 0.0614 | 0.259 | no | Nexd4 | - | -2.15 | -2.20 |
| 185362589181 | 49 | 25. Nd2 | excellent | best | precision | best | 0.0000 | 0.215 | yes | Nd2 | - | -2.14 | -2.19 |
| 185362589181 | 53 | 27. f4 | inaccuracy | good | precision | good | 0.0489 | 0.258 | no | Ne3 | Ne3 | -2.06 | -2.09 |
| 185362589181 | 55 | 28. fxe5 | miss | good | precision | good | 0.0350 | 0.372 | no | Ra4 | Ra4 | -1.10 | -1.03 |
| 185362589181 | 60 | 30... Rxc1 | excellent | good | precision | good | 0.0322 | 0.819 | no | Nc6 | - | -1.93 | -1.97 |
| 185362589181 | 62 | 31... Bd6 | inaccuracy | good | precision | good | 0.0399 | 0.803 | no | Nc6 | Nc6 | -1.53 | -1.84 |
| 185362589181 | 72 | 36... Qf7 | best | excellent | precision | excellent | 0.0192 | 0.796 | no | Qd7 | - | -1.94 | -2.01 |
| 185362589181 | 75 | 38. g4 | best | excellent | precision | excellent | 0.0087 | 0.042 | no | Nd6 | - | -4.64 | -5.33 |
| 185362589181 | 77 | 39. Kf2 | mistake | good | precision | good | 0.0246 | 0.034 | no | Qd6 | - | -7.51 | -7.33 |
| 185362589181 | 83 | 42. Kh2 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.001 | no | Kg2 | Kg2 | -M9 | -9.20 |
| 185362589181 | 90 | 45... Rxf7 | good | inaccuracy | precision | inaccuracy | 0.0724 | 0.865 | no | Kxf7 | - | -2.13 | -2.32 |
| 185362589181 | 91 | 46. Nxd4 | excellent | best | precision | best | 0.0000 | 0.186 | yes | Nxd4 | - | -2.19 | -2.37 |
| 185362589181 | 96 | 48... Rf6 | inaccuracy | best | precision | best | 0.0000 | 0.761 | yes | Rf6 | Rf8 | -1.09 | -1.56 |
| 185362589181 | 107 | 54. d7 | mistake | best | precision | best | 0.0000 | 0.033 | yes | d7 | Bb5 | -4.54 | -5.38 |
| 185362589181 | 111 | 56. Ke3 | excellent | best | precision | best | 0.0000 | 0.035 | yes | Ke3 | - | -4.60 | -5.46 |
| 185362589181 | 112 | 56... Rd6 | excellent | best | precision | best | 0.0000 | 0.970 | yes | Rd6 | - | -4.45 | -5.65 |
| 185362589181 | 113 | 57. Bg4 | excellent | best | precision | best | 0.0000 | 0.027 | yes | Bg4 | - | -4.48 | -5.17 |
| 185362589181 | 118 | 59... Ke7 | good | excellent | precision | excellent | 0.0143 | 0.514 | no | Kg5 | - | 0.00 | +0.02 |
| 185362589181 | 121 | 61. Bxg6 | miss | blunder | precision | blunder | 0.4695 | 0.968 | no | Kf4 | Kf4 | -0.06 | -0.01 |
| 185362589181 | 122 | 61... Kxg6 | excellent | best | precision | best | 0.0000 | 0.502 | yes | Kxg6 | - | 0.00 | -0.01 |
| 185362589181 | 123 | 62. Kf4 | best | excellent | precision | excellent | 0.0016 | 0.498 | no | Kf3 | - | 0.00 | -0.05 |
| 185362589181 | 126 | 63... Kg6 | excellent | best | precision | best | 0.0000 | 0.500 | no | Kg5 | - | 0.00 | +0.00 |
| 185362589181 | 128 | 64... Kxh6 | best | excellent | precision | excellent | 0.0032 | 0.503 | no | Kh5 | - | 0.00 | +0.00 |
| 185363112760 | 3 | 2. Nc3 | book | excellent | precision | excellent | 0.0110 | 0.570 | no | Nf3 | - | +0.31 | +0.37 |
| 185363112760 | 4 | 2... d5 | book | best | precision | best | 0.0000 | 0.441 | yes | d5 | - | +0.31 | +0.33 |
| 185363112760 | 5 | 3. e3 | book | excellent | precision | excellent | 0.0063 | 0.552 | no | d4 | - | +0.12 | +0.19 |
| 185363112760 | 6 | 3... Nf6 | book | excellent | precision | excellent | 0.0174 | 0.470 | no | e5 | - | +0.30 | +0.31 |
| 185363112760 | 8 | 4... g6 | book | good | precision | good | 0.0329 | 0.451 | no | Nbd7 | - | +0.52 | +0.52 |
| 185363112760 | 11 | 6. Be2 | book | best | precision | best | 0.0000 | 0.565 | yes | Be2 | - | +0.42 | +0.50 |
| 185363112760 | 12 | 6... O-O | book | best | precision | best | 0.0000 | 0.421 | yes | O-O | - | +0.42 | +0.47 |
| 185363112760 | 13 | 7. O-O | book | best | precision | best | 0.0000 | 0.574 | yes | O-O | - | +0.42 | +0.48 |
| 185363112760 | 15 | 8. Qb3 | good | excellent | precision | excellent | 0.0108 | 0.596 | no | h3 | - | +0.51 | +0.54 |
| 185363112760 | 17 | 9. Bd2 | good | inaccuracy | precision | inaccuracy | 0.0547 | 0.593 | no | cxd5 | - | +0.56 | +0.24 |
| 185363112760 | 18 | 9... e6 | good | inaccuracy | precision | inaccuracy | 0.0578 | 0.462 | no | dxc4 | - | +0.76 | +0.74 |
| 185363112760 | 19 | 10. Rac1 | inaccuracy | good | precision | good | 0.0492 | 0.616 | no | Ne5 | Ne5 | +0.37 | +0.42 |
| 185363112760 | 20 | 10... Nbd7 | excellent | best | precision | best | 0.0000 | 0.434 | yes | Nbd7 | - | +0.42 | +0.35 |
| 185363112760 | 21 | 11. h3 | good | best | precision | best | 0.0000 | 0.556 | no | Rfd1 | - | +0.23 | +0.34 |
| 185363112760 | 22 | 11... dxc4 | mistake | inaccuracy | precision | inaccuracy | 0.0987 | 0.446 | no | Ne4 | Ne4 | +0.84 | +0.99 |
| 185363112760 | 24 | 12... c5 | good | excellent | precision | excellent | 0.0128 | 0.344 | no | Rc8 | - | +1.05 | +0.90 |
| 185363112760 | 26 | 13... Qe7 | inaccuracy | good | precision | good | 0.0469 | 0.342 | no | Rc8 | Rc8 | +1.38 | +1.37 |
| 185363112760 | 30 | 15... Nxc5 | good | excellent | precision | excellent | 0.0171 | 0.432 | no | Bd5 | - | +0.56 | +0.41 |
| 185363112760 | 31 | 16. b4 | great | best | precision | best | 0.0000 | 0.565 | yes | b4 | - | +0.56 | +0.44 |
| 185363112760 | 32 | 16... Bd5 | great | best | precision | best | 0.0000 | 0.430 | yes | Bd5 | - | +0.56 | +0.48 |
| 185363112760 | 36 | 18... Nce4 | best | good | precision | good | 0.0371 | 0.432 | no | Nfe4 | - | +0.56 | +0.57 |
| 185363112760 | 38 | 19... a6 | blunder | mistake | precision | mistake | 0.1940 | 0.407 | no | Nd6 | - | +1.76 | +2.05 |
| 185363112760 | 40 | 20... Rfb8 | inaccuracy | good | precision | good | 0.0334 | 0.215 | no | Nd7 | d4 | +2.53 | +2.49 |
| 185363112760 | 46 | 23... Qe8 | excellent | good | precision | good | 0.0431 | 0.141 | no | Rc8 | - | +3.33 | +3.52 |
| 185363112760 | 47 | 24. Rxd5 | best | excellent | precision | excellent | 0.0011 | 0.904 | no | Rxa6 | - | +3.33 | +3.56 |
| 185363112760 | 51 | 26. Rxc8 | great | best | precision | best | 0.0000 | 0.902 | yes | Rxc8 | - | +3.63 | +3.64 |
| 185363112760 | 54 | 27... Ra8 | good | inaccuracy | precision | inaccuracy | 0.0532 | 0.092 | no | Nc3 | - | +4.66 | +5.03 |
| 185363112760 | 59 | 30. a4 | excellent | best | precision | best | 0.0000 | 0.949 | yes | a4 | - | +4.37 | +4.43 |
| 185363112760 | 63 | 32. Qb6 | best | excellent | precision | excellent | 0.0063 | 0.945 | no | Qb7 | - | +4.26 | +4.45 |
| 185363112760 | 72 | 36... Nd5 | great | best | precision | best | 0.0000 | 0.396 | yes | Nd5 | - | +0.62 | +0.77 |
| 185363112760 | 75 | 38. Bc6 | mistake | blunder | precision | blunder | 0.2979 | 0.529 | no | Be1 | a5 | -1.70 | -1.89 |
| 185363112760 | 76 | 38... Nxb4 | great | best | precision | best | 0.0000 | 0.769 | yes | Nxb4 | - | -1.70 | -1.87 |
| 185363112760 | 77 | 39. Be4 | inaccuracy | good | precision | good | 0.0272 | 0.233 | no | Bb5 | Bb5 | -2.22 | -2.30 |
| 185363112760 | 78 | 39... Rc8 | great | best | precision | best | 0.0000 | 0.812 | yes | Rc8 | - | -2.22 | -2.14 |
| 185363112760 | 80 | 40... Kg7 | excellent | good | precision | good | 0.0332 | 0.802 | no | Rc1+ | - | -2.10 | -2.10 |
| 185363112760 | 81 | 41. Bg3 | good | inaccuracy | precision | inaccuracy | 0.0694 | 0.208 | no | Be1 | - | -2.78 | -2.87 |
| 185363112760 | 82 | 41... Qc5 | good | excellent | precision | excellent | 0.0176 | 0.862 | no | Qe7 | - | -2.33 | -2.50 |
| 185363112760 | 83 | 42. Be5+ | inaccuracy | mistake | precision | mistake | 0.1129 | 0.169 | no | a5 | - | -4.34 | -4.43 |
| 185363112760 | 84 | 42... Bxe5 | great | best | precision | best | 0.0000 | 0.944 | yes | Bxe5 | - | -4.34 | -4.67 |
| 185468237512 | 10 | 5... Bg4 | good | excellent | precision | excellent | 0.0138 | 0.504 | no | Nc6 | - | +0.35 | +0.23 |
| 185468237512 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0196 | 0.517 | no | h3 | - | 0.00 | -0.04 |
| 185468237512 | 26 | 13... bxc6 | best | excellent | precision | excellent | 0.0020 | 0.374 | no | Bxc3 | - | +1.71 | +1.74 |
| 185468237512 | 30 | 15... Qd6 | excellent | good | precision | good | 0.0227 | 0.350 | no | Bxh2+ | - | +2.58 | +2.59 |
| 185468237512 | 52 | 26... Ke8 | good | excellent | precision | excellent | 0.0147 | 0.245 | no | Ke7 | - | +4.09 | +4.16 |
| 185468237512 | 54 | 27... Rd2 | good | excellent | precision | excellent | 0.0169 | 0.239 | no | g5 | - | +4.34 | +4.33 |
| 185468237512 | 59 | 30. e7 | good | inaccuracy | precision | inaccuracy | 0.0675 | 0.718 | no | Ke4 | - | +2.28 | +2.14 |
| 185468237512 | 64 | 32... Rd6+ | excellent | good | precision | good | 0.0265 | 0.288 | no | Rc6 | - | +3.36 | +3.92 |
| 185468237512 | 65 | 33. Kc4 | excellent | best | precision | best | 0.0000 | 0.757 | yes | Kc4 | - | +3.24 | +3.89 |
| 185468237512 | 66 | 33... Ra6 | inaccuracy | good | precision | good | 0.0312 | 0.245 | no | Rb6 | Rb6 | +4.40 | +4.50 |
| 185468237512 | 67 | 34. Kb5 | best | excellent | precision | excellent | 0.0024 | 0.787 | no | b3 | - | +4.40 | +4.77 |
| 185468237512 | 69 | 35. Kc6 | good | inaccuracy | precision | inaccuracy | 0.0539 | 0.796 | no | b3 | - | +3.39 | +3.64 |
| 185468237512 | 73 | 37. bxa3 | inaccuracy | mistake | precision | mistake | 0.1247 | 0.810 | no | b4 | b4 | +2.69 | +2.38 |
| 185468237512 | 76 | 38... Ra6+ | best | excellent | precision | excellent | 0.0123 | 0.310 | no | Ra5 | - | +2.45 | +2.60 |
| 185468237512 | 79 | 40. Kg4 | excellent | best | precision | best | 0.0000 | 0.610 | yes | Kg4 | - | +1.52 | +1.57 |
| 185468237512 | 81 | 41. Kg5 | great | best | precision | best | 0.0000 | 0.788 | yes | Kg5 | - | +4.46 | +4.44 |
| 185468237512 | 84 | 42... Ra6+ | good | best | precision | best | 0.0000 | 0.217 | yes | Ra6+ | - | +4.92 | +5.48 |
| 185468237512 | 86 | 43... Rxa2 | excellent | best | precision | best | 0.0000 | 0.099 | yes | Rxa2 | - | +5.10 | +7.59 |
| 185468237512 | 91 | 46. Rd6 | great | best | precision | best | 0.0000 | 1.000 | yes | Rd6 | - | M2 | M2 |
| 185468237512 | 96 | 48... f4 | excellent | best | precision | best | 0.0000 | 0.187 | yes | f4 | - | +5.14 | +5.07 |
| 185468237512 | 97 | 49. Kf6 | best | excellent | precision | excellent | 0.0009 | 0.813 | no | Kd6 | - | +5.14 | +6.24 |
| 185468237512 | 98 | 49... f3 | inaccuracy | excellent | precision | excellent | 0.0131 | 0.141 | no | g5 | g5 | +7.03 | +6.63 |
| 185468237512 | 102 | 51... Kxe7 | good | best | precision | best | 0.0000 | 0.176 | yes | Kxe7 | - | +5.89 | +5.55 |
| 185468237512 | 103 | 52. Kh6 | great | best | precision | best | 0.0000 | 0.833 | yes | Kh6 | - | +5.89 | +5.36 |
| 185468237512 | 104 | 52... Kf6 | excellent | best | precision | best | 0.0000 | 0.175 | no | Ke6 | - | +5.96 | +5.16 |
| 185468237512 | 105 | 53. Kxh7 | good | excellent | precision | excellent | 0.0004 | 0.817 | no | h4 | - | +5.30 | +5.22 |
| 185961991257 | 6 | 3... Nxd5 | book | best | precision | best | 0.0000 | 0.465 | yes | Nxd5 | - | +0.27 | +0.34 |
| 185961991257 | 7 | 4. Nf3 | book | excellent | precision | excellent | 0.0126 | 0.554 | no | Bc4 | - | +0.27 | +0.27 |
| 185961991257 | 12 | 6... Bg7 | excellent | best | precision | best | 0.0000 | 0.521 | yes | Bg7 | - | -0.12 | -0.20 |
| 185961991257 | 13 | 7. d4 | good | excellent | precision | excellent | 0.0111 | 0.468 | no | Bg2 | - | -0.29 | -0.29 |
| 185961991257 | 14 | 7... O-O | good | excellent | precision | excellent | 0.0111 | 0.546 | no | c5 | - | -0.16 | -0.08 |
| 185961991257 | 17 | 9. O-O | best | excellent | precision | excellent | 0.0016 | 0.476 | no | Rb1 | - | -0.16 | -0.11 |
| 185961991257 | 19 | 10. Rb1 | good | inaccuracy | precision | inaccuracy | 0.0620 | 0.541 | no | Bg5 | - | -0.03 | -0.13 |
| 185961991257 | 20 | 10... Rd8 | inaccuracy | best | precision | best | 0.0000 | 0.521 | yes | Rd8 | cxd4 | +0.39 | -0.14 |
| 185961991257 | 21 | 11. Qe1 | mistake | inaccuracy | precision | inaccuracy | 0.0613 | 0.478 | no | d5 | Ng5 | -0.57 | -0.53 |
| 185961991257 | 23 | 12. Be3 | good | mistake | precision | mistake | 0.1177 | 0.416 | no | Ne5 | - | -0.83 | -1.34 |
| 185961991257 | 32 | 16... e6 | mistake | good | precision | good | 0.0223 | 0.500 | no | Rb8 | Rb8 | +0.71 | +0.14 |
| 185961991257 | 33 | 17. c3 | miss | good | precision | good | 0.0207 | 0.522 | no | Red1 | Red1 | +0.07 | +0.01 |
| 185961991257 | 35 | 18. a4 | best | excellent | precision | excellent | 0.0016 | 0.510 | no | Re5 | - | +0.07 | +0.02 |
| 185961991257 | 37 | 19. a5 | good | excellent | precision | excellent | 0.0159 | 0.529 | no | Bxb7 | - | +0.17 | +0.00 |
| 185961991257 | 38 | 19... b6 | excellent | good | precision | good | 0.0318 | 0.500 | no | Rdc8 | - | +0.19 | +0.15 |
| 185961991257 | 41 | 21. Rb3 | excellent | good | precision | good | 0.0270 | 0.527 | no | Rec1 | - | +0.09 | +0.00 |
| 185961991257 | 42 | 21... Rdc8 | good | excellent | precision | excellent | 0.0064 | 0.500 | no | b5 | - | +0.24 | +0.00 |
| 185961991257 | 43 | 22. Reb1 | inaccuracy | excellent | precision | excellent | 0.0143 | 0.500 | no | f4 | f4 | -0.07 | -0.09 |
| 185961991257 | 46 | 23... Kf8 | good | excellent | precision | excellent | 0.0016 | 0.494 | no | Ba4 | - | +0.20 | +0.05 |
| 185961991257 | 47 | 24. c4 | good | excellent | precision | excellent | 0.0048 | 0.508 | no | f3 | - | +0.03 | +0.00 |
| 185961991257 | 49 | 25. cxb5 | excellent | best | precision | best | 0.0000 | 0.654 | yes | cxb5 | - | +1.13 | +0.94 |
| 185961991257 | 50 | 25... Rb6 | excellent | inaccuracy | precision | inaccuracy | 0.0704 | 0.355 | no | Bc8 | - | +1.20 | +1.25 |
| 185961991257 | 54 | 27... Rcb7 | inaccuracy | good | precision | good | 0.0400 | 0.337 | no | g5 | Rc2 | +1.27 | +1.35 |
| 185961991257 | 55 | 28. Rab1 | mistake | inaccuracy | precision | inaccuracy | 0.0945 | 0.703 | no | f4 | - | +0.69 | +0.69 |
| 185961991257 | 61 | 31. Be2 | miss | good | precision | good | 0.0271 | 0.675 | no | Kg2 | Kg2 | +0.54 | +0.96 |
| 185961991257 | 62 | 31... Ra4 | inaccuracy | excellent | precision | excellent | 0.0029 | 0.352 | no | Bc8 | Bc8 | +0.93 | +0.98 |
| 185961991257 | 64 | 32... Ra2 | good | best | precision | best | 0.0000 | 0.355 | yes | Ra2 | - | +1.04 | +1.04 |
| 185961991257 | 65 | 33. R4b2 | good | best | precision | best | 0.0000 | 0.660 | yes | R4b2 | - | +0.93 | +0.86 |
| 185961991257 | 66 | 33... Ra4 | good | excellent | precision | excellent | 0.0044 | 0.366 | no | Ra3 | - | +1.07 | +0.99 |
| 185961991257 | 67 | 34. Rb4 | great | best | precision | best | 0.0000 | 0.653 | yes | Rb4 | - | +1.07 | +0.91 |
| 185961991257 | 69 | 35. Bf1 | mistake | good | precision | good | 0.0471 | 0.660 | no | Kf1 | Kf1 | +0.67 | +0.72 |
| 185961991257 | 70 | 35... Rd2 | inaccuracy | good | precision | good | 0.0500 | 0.387 | no | Bc8 | Bc8 | +0.96 | +1.06 |
| 185961991257 | 71 | 36. Ra1 | inaccuracy | good | precision | good | 0.0424 | 0.663 | no | Kg2 | R1b2 | +0.65 | +0.77 |
| 185961991257 | 72 | 36... Bc8 | inaccuracy | good | precision | good | 0.0353 | 0.380 | no | Bc6 | Bc6 | +1.03 | +1.01 |
| 185961991257 | 73 | 37. Ra7 | best | excellent | precision | excellent | 0.0072 | 0.656 | no | Rba4 | - | +1.03 | +1.05 |
| 185961991257 | 74 | 37... Bb7 | best | excellent | precision | excellent | 0.0141 | 0.339 | no | Bd7 | - | +1.03 | +0.98 |
| 185961991257 | 76 | 38... Rxd4 | excellent | best | precision | best | 0.0000 | 0.497 | yes | Rxd4 | - | +0.11 | +0.12 |
| 185961991257 | 78 | 39... Bxg2 | inaccuracy | good | precision | good | 0.0238 | 0.487 | no | Kc7 | Kc7 | +0.40 | +0.25 |
| 185961991257 | 85 | 43. Rg7 | great | best | precision | best | 0.0000 | 0.783 | yes | Rg7 | - | +1.97 | +2.30 |
| 185961991257 | 86 | 43... g5 | inaccuracy | mistake | precision | mistake | 0.1342 | 0.188 | no | Ra5 | Rb8 | +2.70 | +4.51 |
| 185961991257 | 90 | 45... Ke5 | excellent | best | precision | best | 0.0000 | 0.004 | yes | Ke5 | - | +5.78 | +7.87 |
| 185961991257 | 91 | 46. Kh3 | best | excellent | precision | excellent | 0.0036 | 0.993 | no | f4+ | - | +5.78 | +11.04 |
| 185961991257 | 94 | 47... Kg6 | excellent | best | precision | best | 0.0000 | 0.003 | yes | Kg6 | - | +8.00 | +11.04 |
| 185961991257 | 95 | 48. f4 | best | excellent | precision | excellent | 0.0001 | 0.999 | no | g4 | - | +8.00 | +13.93 |
| 186393389351 | 8 | 4... Bb4 | book | best | precision | best | 0.0000 | 0.486 | yes | Bb4 | - | +0.10 | +0.09 |
| 186393389351 | 9 | 5. d3 | book | best | precision | best | 0.0000 | 0.514 | yes | d3 | - | +0.10 | +0.08 |
| 186393389351 | 10 | 5... d6 | book | best | precision | best | 0.0000 | 0.487 | yes | d6 | - | +0.10 | +0.17 |
| 186393389351 | 11 | 6. a3 | book | best | precision | best | 0.0000 | 0.527 | yes | a3 | - | +0.10 | +0.10 |
| 186393389351 | 15 | 8. Be3 | excellent | best | precision | best | 0.0000 | 0.513 | yes | Be3 | - | +0.04 | +0.18 |
| 186393389351 | 16 | 8... Bg4 | excellent | best | precision | best | 0.0000 | 0.471 | yes | Bg4 | - | +0.11 | +0.13 |
| 186393389351 | 18 | 9... Bxf3 | excellent | best | precision | best | 0.0000 | 0.489 | yes | Bxf3 | - | +0.12 | +0.09 |
| 186393389351 | 21 | 11. Na4 | excellent | best | precision | best | 0.0000 | 0.522 | yes | Na4 | - | +0.04 | +0.24 |
| 186393389351 | 22 | 11... c6 | inaccuracy | good | precision | good | 0.0221 | 0.462 | no | O-O | Nxf3+ | +0.49 | +0.38 |
| 186393389351 | 23 | 12. O-O | inaccuracy | good | precision | good | 0.0364 | 0.560 | no | Nxb6 | Nxb6 | +0.03 | +0.13 |
| 186393389351 | 26 | 13... Qxb6 | good | excellent | precision | excellent | 0.0047 | 0.432 | no | Nxf3+ | - | +0.49 | +0.47 |
| 186393389351 | 28 | 14... a5 | good | excellent | precision | excellent | 0.0171 | 0.430 | no | Nxf3+ | - | +0.66 | +0.55 |
| 186393389351 | 39 | 20. Be3 | inaccuracy | mistake | precision | mistake | 0.1032 | 0.467 | no | Bb4 | Bb4 | -0.78 | -0.88 |
| 186393389351 | 41 | 21. Bg5 | inaccuracy | best | precision | best | 0.0000 | 0.366 | no | g3 | g3 | -1.08 | -0.86 |
| 186393389351 | 52 | 26... Qe7 | great | best | precision | best | 0.0000 | 0.682 | yes | Qe7 | - | -1.39 | -1.38 |
| 186393389351 | 53 | 27. Ra1 | mistake | inaccuracy | precision | inaccuracy | 0.0726 | 0.293 | no | Rb1 | Rb1 | -2.11 | -1.98 |
| 186393389351 | 54 | 27... g6 | great | best | precision | best | 0.0000 | 0.779 | yes | g6 | - | -2.11 | -1.87 |
| 186393389351 | 56 | 28... Qf8 | miss | mistake | precision | mistake | 0.1974 | 0.816 | no | Qxe4 | Qxe4 | -0.99 | -0.77 |
| 186393389351 | 63 | 32. Qe2 | mistake | inaccuracy | precision | inaccuracy | 0.0594 | 0.116 | no | Bxg6 | - | -4.14 | -4.43 |
| 186393389351 | 64 | 32... Rd2 | great | best | precision | best | 0.0000 | 0.944 | yes | Rd2 | - | -4.14 | -4.55 |
| 186393389351 | 67 | 34. e5 | excellent | best | precision | best | 0.0000 | 0.050 | yes | e5 | - | -4.41 | -4.62 |
| 186393389351 | 69 | 35. g3 | best | excellent | precision | excellent | 0.0003 | 0.050 | no | exd6 | - | -4.41 | -4.65 |
| 186393389351 | 74 | 37... Nd4 | excellent | good | precision | good | 0.0485 | 0.188 | no | Qe4 | - | +2.80 | +2.87 |
| 186393389351 | 76 | 38... Qf5 | inaccuracy | good | precision | good | 0.0474 | 0.167 | no | Qxe3 | Qxe3 | +3.24 | +3.23 |
| 186393389351 | 81 | 41. Kh3 | great | best | precision | best | 0.0000 | 0.818 | yes | Kh3 | - | +2.40 | +2.37 |
| 186393389351 | 82 | 41... Kf6 | inaccuracy | mistake | precision | mistake | 0.1475 | 0.181 | no | Qf3 | - | +5.29 | +5.28 |
| 186393389351 | 84 | 42... Ke7 | excellent | good | precision | good | 0.0307 | 0.039 | no | Kg6 | - | +6.67 | +7.50 |

### `miss_detector` (15)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185387411150 | 23 | 12. Bh4 | mistake | miss (tactic) | miss_detector | mistake | 0.1358 | 0.764 | no | Qg6+ | Qg6+ | +1.91 | +1.98 |
| 185425961522 | 29 | 15. Bxa7 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1001 | 0.823 | no | Qa4+ | Qa4+ | +3.25 | +3.35 |
| 185425961522 | 38 | 19... Nf4 | blunder | miss (tactic) | miss_detector | blunder | 0.5448 | 0.673 | no | Rd3 | Rd3 | +6.74 | +6.72 |
| 185466827454 | 22 | 11... Bxd4 | mistake | miss (free_piece) | miss_detector | mistake | 0.1135 | 0.608 | no | Qxd4 | Qxd4 | +0.32 | +0.26 |
| 184740374128 | 40 | 20... Rg5+ | mistake | miss (tactic) | miss_detector | blunder | 0.4060 | 0.906 | no | Nf4 | Nf4 | 0.00 | +0.00 |
| 184740374128 | 45 | 23. Rab1 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1825 | 0.500 | no | Qb6 | Rfb1 | -0.84 | -3.09 |
| 185101208706 | 16 | 8... Bf5 | mistake | miss (free_piece) | miss_detector | blunder | 0.2421 | 0.492 | no | dxe4 | - | +4.02 | +3.97 |
| 185101208706 | 31 | 16. g5 | blunder | miss (tactic) | miss_detector | blunder | 0.4512 | 0.750 | no | Qa8+ | Qa8+ | -2.32 | -3.08 |
| 185311691496 | 11 | 6. Bg5 | mistake | miss (opportunity) | miss_detector | mistake | 0.1937 | 0.714 | no | O-O | - | +0.58 | +0.29 |
| 185311691496 | 31 | 16. Nxd4 | mistake | miss (opportunity) | miss_detector | mistake | 0.1446 | 0.775 | no | Qe2 | Qe2 | +1.72 | +1.88 |
| 185362589181 | 71 | 36. Nb5 | mistake | miss (opportunity) | miss_detector | mistake | 0.1154 | 0.319 | no | Bg2 | a5 | -1.94 | -2.14 |
| 185362589181 | 99 | 50. d4 | blunder | miss (opportunity) | miss_detector | mistake | 0.1923 | 0.261 | no | Kxf2 | Kxf2 | -3.41 | -4.08 |
| 185468237512 | 29 | 15. Rf3 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1274 | 0.780 | no | Ne4 | Ne4 | +2.43 | +2.14 |
| 185961991257 | 24 | 12... cxd4 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1380 | 0.701 | no | Be6 | Be6 | -0.44 | -0.40 |
| 186393389351 | 57 | 29. Qf4 | blunder | miss (opportunity) | miss_detector | blunder | 0.2639 | 0.380 | no | Qxf8+ | - | -2.90 | -3.19 |

### `mate_override` (6)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185101208706 | 41 | 21. Kxh2 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kh1 | - | -M2 | -M2 |
| 185221110711 | 88 | 44... Qc4 | excellent | good | mate_override | good | 0.0002 | 1.000 | no | Kg7 | - | -7.27 | -13.37 |
| 185221110711 | 93 | 47. Kh5 | mistake | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kf5 | Kf5 | -M2 | -M2 |
| 185344445308 | 70 | 35... Qd1+ | good | miss (mate) | mate_override | mistake | 0.1245 | 1.000 | no | Qd4+ | - | -6.70 | -6.68 |
| 185344445308 | 76 | 38... Kb7 | good | miss (mate) | mate_override | mistake | 0.1120 | 1.000 | no | Re8 | - | -6.68 | -7.09 |
| 185362589181 | 86 | 43... Bxg4 | good | miss (mate) | mate_override | mistake | 0.1303 | 1.000 | no | Qxg4 | - | -2.87 | -2.98 |

### `losing_material_hardened` (5)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185387411150 | 32 | 16... Bb4 | good | mistake | losing_material_hardened | good | 0.0246 | 0.193 | no | Qe5+ | - | +5.56 | +5.77 |
| 185476493194 | 40 | 20... Rae8 | good | mistake | losing_material_hardened | good | 0.0302 | 0.089 | no | Kg7 | - | +9.13 | +9.46 |
| 185221110711 | 75 | 38. f6 | good | mistake | losing_material_hardened | good | 0.0464 | 0.063 | no | Rxe2 | - | -6.68 | -6.60 |
| 185221110711 | 77 | 39. gxf6 | excellent | mistake | losing_material_hardened | good | 0.0295 | 0.038 | no | Rxe2 | - | -6.89 | -7.51 |
| 185363112760 | 56 | 28... h6 | excellent | mistake | losing_material_hardened | excellent | 0.0170 | 0.059 | no | Qf8 | - | +4.99 | +4.90 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185466827454 | 32 | 16... Kg8 | best | great | great_find_event | best | 0.0000 | 0.436 | yes | Kg8 | - | +0.78 | +0.82 |
| 185221110711 | 58 | 29... Kh8 | best | great | great_find_event | best | 0.0000 | 0.815 | yes | Kh8 | - | -2.29 | -2.30 |

### `book` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185476493194 | 11 | 6. Nc3 | excellent | book | book | excellent | 0.0154 | 0.522 | no | c3 | - | +0.18 | +0.09 |
| 185311691496 | 7 | 4. Bc4 | inaccuracy | book | book | inaccuracy | 0.0576 | 0.534 | no | e5 | e5 | -0.29 | -0.33 |

### `blunder_softened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185476493194 | 19 | 10. Qf3 | blunder | mistake | blunder_softened | blunder | 0.2758 | 0.524 | no | Bxf6 | - | -3.55 | -3.77 |
| 185221110711 | 62 | 31... Nh5 | blunder | mistake | blunder_softened | blunder | 0.4005 | 0.924 | no | Rxc4 | - | -0.21 | -0.15 |

### `brilliant_event` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184740374128 | 49 | 25. Qxb7+ | best | brilliant | brilliant_event | best | 0.0000 | 0.247 | yes | Qxb7+ | - | -4.47 | -4.22 |

