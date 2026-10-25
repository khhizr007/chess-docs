# Calibration report: baseline

- Generated: 2026-10-17T18:36:13+00:00
- Commit: `5bc590e235bb` (backend clean)
- Engine: Stockfish 17.1; depth 18, multipv 3; config override: none
- Games: 15 requested, 15 compared, 0 skipped (list: `/mnt/c/Users/khhizr/AppData/Local/Temp/claude/C--Users-khhizr--claude-spares-spare-OQFzGS/2b00c298-04cf-476c-a0ad-747be6deb84b/scratchpad/collected.txt`)
- Plies: 671 aligned, 671 scored, 0 excluded (none)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 65.7% (441/671) |
| Within one step | 82.0% (550/671) |
| Brilliant precision / recall | 0.04 / 1.00 |
| Great precision / recall | 1.00 / 0.14 |
| Brilliant per 100 moves (app / ours) | 0.30 / 8.20 |
| Great per 100 moves (app / ours) | 3.13 / 0.45 |
| Accuracy mean abs. difference | 3.53 (n=30, max 7.57) |
| Accuracy bias (ours - app) | +2.98 |
| Best move = app's suggestion | 82.5% (94/114 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **2** | . | . | . | . | . | . | . | . | . | 2 |
| **great** | 3 | **3** | 15 | . | . | . | . | . | . | . | 21 |
| **best** | 28 | . | **174** | 20 | 2 | . | . | 1 | . | . | 225 |
| **excellent** | 11 | . | 12 | **29** | 11 | . | . | . | . | . | 63 |
| **good** | 7 | . | 3 | 26 | **37** | . | 4 | . | . | . | 77 |
| **book** | 4 | . | 12 | 6 | 4 | **91** | . | . | . | . | 117 |
| **inaccuracy** | . | . | 2 | 2 | 21 | 1 | **46** | 1 | . | . | 73 |
| **mistake** | . | . | 1 | 2 | 2 | . | 9 | **25** | 5 | 2 | 46 |
| **miss** | . | . | . | . | . | . | 3 | 3 | **20** | . | 26 |
| **blunder** | . | . | . | . | . | . | . | 3 | 4 | **14** | 21 |
| **total** | 55 | 3 | 219 | 85 | 77 | 92 | 62 | 33 | 29 | 16 | 671 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 2 | 55 | 2 | 0.036 | 1.000 | 0.070 |
| great | 21 | 3 | 3 | 1.000 | 0.143 | 0.250 |
| best | 225 | 219 | 174 | 0.795 | 0.773 | 0.784 |
| excellent | 63 | 85 | 29 | 0.341 | 0.460 | 0.392 |
| good | 77 | 77 | 37 | 0.481 | 0.481 | 0.481 |
| book | 117 | 92 | 91 | 0.989 | 0.778 | 0.871 |
| inaccuracy | 73 | 62 | 46 | 0.742 | 0.630 | 0.681 |
| mistake | 46 | 33 | 25 | 0.758 | 0.543 | 0.633 |
| miss | 26 | 29 | 20 | 0.690 | 0.769 | 0.727 |
| blunder | 21 | 16 | 14 | 0.875 | 0.667 | 0.757 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 1034847688 | white | 73.7 | 79.2 | +5.5 |
| 1034847688 | black | 65.0 | 68.2 | +3.2 |
| 1041474766 | white | 98.0 | 97.1 | -0.9 |
| 1041474766 | black | 83.8 | 85.7 | +1.9 |
| 184759554082 | white | 81.2 | 85.5 | +4.3 |
| 184759554082 | black | 87.7 | 90.4 | +2.7 |
| 185324357184 | white | 73.0 | 76.6 | +3.6 |
| 185324357184 | black | 62.4 | 67.2 | +4.8 |
| 185387411150 | white | 77.9 | 78.3 | +0.4 |
| 185387411150 | black | 75.5 | 79.3 | +3.8 |
| 185425961522 | white | 58.9 | 64.3 | +5.4 |
| 185425961522 | black | 55.0 | 59.0 | +4.0 |
| 185436488062 | white | 98.6 | 98.0 | -0.6 |
| 185436488062 | black | 38.5 | 42.6 | +4.1 |
| 185438343298 | white | 46.9 | 47.1 | +0.2 |
| 185438343298 | black | 80.0 | 80.0 | +0.0 |
| 185439816356 | white | 59.1 | 63.2 | +4.1 |
| 185439816356 | black | 81.9 | 83.8 | +1.9 |
| 185466827454 | white | 73.1 | 80.5 | +7.4 |
| 185466827454 | black | 77.5 | 82.7 | +5.2 |
| 185468039834 | white | 80.0 | 85.4 | +5.4 |
| 185468039834 | black | 87.5 | 89.5 | +2.0 |
| 185468614210 | white | 70.8 | 76.8 | +6.0 |
| 185468614210 | black | 77.1 | 81.8 | +4.7 |
| 185475865432 | white | 78.1 | 83.4 | +5.3 |
| 185475865432 | black | 66.1 | 73.7 | +7.6 |
| 185476493194 | white | 61.7 | 57.6 | -4.1 |
| 185476493194 | black | 56.1 | 53.5 | -2.6 |
| 185962590893 | white | 90.8 | 93.1 | +2.3 |
| 185962590893 | black | 90.9 | 92.7 | +1.8 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 1034847688 | 49 | 49 | 63.3% | 81.6% | reviewed | 99.7 |
| 1041474766 | 25 | 25 | 56.0% | 64.0% | reviewed | 34.1 |
| 184759554082 | 62 | 62 | 61.3% | 80.6% | reviewed | 101.6 |
| 185324357184 | 55 | 55 | 67.3% | 83.6% | reviewed | 94.9 |
| 185387411150 | 57 | 57 | 63.2% | 75.4% | reviewed | 43.4 |
| 185425961522 | 47 | 47 | 74.5% | 89.4% | reviewed | 49.8 |
| 185436488062 | 13 | 13 | 92.3% | 100.0% | reviewed | 15.1 |
| 185438343298 | 20 | 20 | 80.0% | 85.0% | reviewed | 12.6 |
| 185439816356 | 15 | 15 | 86.7% | 93.3% | reviewed | 9.1 |
| 185466827454 | 62 | 62 | 48.4% | 83.9% | reviewed | 67.9 |
| 185468039834 | 38 | 38 | 65.8% | 81.6% | reviewed | 54.3 |
| 185468614210 | 54 | 54 | 63.0% | 70.4% | cache | 60.4 |
| 185475865432 | 53 | 53 | 64.2% | 81.1% | cache | 60.4 |
| 185476493194 | 43 | 43 | 62.8% | 74.4% | cache | 56.9 |
| 185962590893 | 78 | 78 | 75.6% | 93.6% | reviewed | 74.7 |

## Mismatches by rule (230)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 164 | good -> excellent x26, inaccuracy -> good x21, best -> excellent x20, great -> best x15, excellent -> best x12, book -> best x12 |
| `brilliant_event` | 53 | best -> brilliant x28, excellent -> brilliant x11, good -> brilliant x7, book -> brilliant x4, great -> brilliant x3 |
| `miss_detector` | 9 | mistake -> miss x5, blunder -> miss x4 |
| `blunder_softened` | 2 | miss -> mistake x2 |
| `losing_material_hardened` | 1 | best -> mistake x1 |
| `book` | 1 | inaccuracy -> book x1 |

### `precision` (164)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 5 | 3. d4 | best | excellent | precision | excellent | 0.0009 | 0.524 | no | c4 | - | +0.33 | +0.27 |
| 1034847688 | 8 | 4... Bg7 | best | excellent | precision | excellent | 0.0028 | 0.504 | no | c5 | - | +0.13 | -0.04 |
| 1034847688 | 9 | 5. c4 | inaccuracy | good | precision | good | 0.0468 | 0.496 | no | c3 | f1d3 | -0.52 | -0.54 |
| 1034847688 | 14 | 7... Nc6 | good | inaccuracy | precision | inaccuracy | 0.0517 | 0.523 | no | cxd4 | - | +0.28 | +0.30 |
| 1034847688 | 17 | 9. Qc2 | excellent | good | precision | good | 0.0348 | 0.529 | no | a3 | - | +0.12 | -0.06 |
| 1034847688 | 21 | 11. Be2 | good | inaccuracy | precision | inaccuracy | 0.0512 | 0.572 | no | cxb5 | - | +0.24 | +0.22 |
| 1034847688 | 26 | 13... h6 | inaccuracy | excellent | precision | excellent | 0.0178 | 0.476 | no | a4 | - | +0.90 | +0.36 |
| 1034847688 | 38 | 19... Nxf3 | great | best | precision | best | 0.0000 | 0.531 | yes | Nxf3 | - | -0.10 | -0.29 |
| 1034847688 | 41 | 21. Rh3 | excellent | best | precision | best | 0.0000 | 0.538 | yes | Rh3 | - | +0.39 | +0.28 |
| 1034847688 | 43 | 22. dxe6 | excellent | best | precision | best | 0.0000 | 0.500 | yes | dxe6 | - | +0.30 | +0.00 |
| 1034847688 | 44 | 22... Qxg5 | excellent | good | precision | good | 0.0487 | 0.500 | no | fxe6 | - | +0.46 | +0.76 |
| 1034847688 | 45 | 23. exf7+ | good | best | precision | best | 0.0000 | 0.571 | yes | exf7+ | - | +0.09 | +0.88 |
| 1034847688 | 46 | 23... Kxf7 | inaccuracy | best | precision | best | 0.0000 | 0.418 | yes | Kxf7 | f8f7 | +0.92 | +0.55 |
| 1034847688 | 49 | 25. Qe4+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe4+ | - | M8 | M14 |
| 1041474766 | 7 | 4. g3 | book | good | precision | good | 0.0310 | 0.560 | no | d4 | - | +0.37 | +0.32 |
| 1041474766 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0027 | 0.471 | no | e5 | - | +0.38 | +0.38 |
| 1041474766 | 9 | 5. Bg2 | book | best | precision | best | 0.0000 | 0.534 | yes | Bg2 | - | +0.34 | +0.38 |
| 1041474766 | 10 | 5... c6 | book | excellent | precision | excellent | 0.0089 | 0.466 | no | e5 | - | +0.59 | +0.49 |
| 1041474766 | 11 | 6. Nge2 | book | good | precision | good | 0.0356 | 0.544 | no | d3 | - | +0.17 | +0.09 |
| 1041474766 | 16 | 8... Bb4 | good | excellent | precision | excellent | 0.0195 | 0.470 | no | Be7 | - | +0.76 | +0.62 |
| 1041474766 | 17 | 9. dxe5 | good | excellent | precision | excellent | 0.0168 | 0.555 | no | Bd2 | - | +0.39 | +0.39 |
| 184759554082 | 6 | 3... a6 | book | good | precision | good | 0.0302 | 0.532 | no | d5 | - | +0.08 | +0.02 |
| 184759554082 | 9 | 5. h4 | inaccuracy | good | precision | good | 0.0477 | 0.540 | no | Be2 | f1e2 | -0.11 | -0.05 |
| 184759554082 | 11 | 6. Be2 | good | excellent | precision | excellent | 0.0191 | 0.487 | no | Nc3 | - | -0.25 | -0.19 |
| 184759554082 | 14 | 7... O-O | excellent | good | precision | good | 0.0223 | 0.497 | no | Nxh5 | - | +0.03 | +0.16 |
| 184759554082 | 16 | 8... hxg6 | excellent | best | precision | best | 0.0000 | 0.514 | yes | hxg6 | - | -0.13 | -0.19 |
| 184759554082 | 22 | 11... d5 | great | best | precision | best | 0.0000 | 0.585 | yes | d5 | - | -0.52 | -0.47 |
| 184759554082 | 32 | 16... b6 | best | good | precision | good | 0.0226 | 0.680 | no | b5 | - | -0.96 | -1.08 |
| 184759554082 | 33 | 17. Qc2 | best | excellent | precision | excellent | 0.0071 | 0.334 | no | Qc1 | - | -0.96 | -0.93 |
| 184759554082 | 35 | 18. O-O-O | good | excellent | precision | excellent | 0.0030 | 0.369 | no | Qb2+ | - | -1.01 | -1.12 |
| 184759554082 | 38 | 19... Bf5 | excellent | good | precision | good | 0.0461 | 0.677 | no | Bh3 | - | -1.10 | -0.84 |
| 184759554082 | 40 | 20... Re6 | excellent | best | precision | best | 0.0000 | 0.714 | yes | Re6 | - | -1.31 | -1.41 |
| 184759554082 | 45 | 23. Rc1 | best | excellent | precision | excellent | 0.0065 | 0.287 | no | Rh1 | - | -1.28 | -1.38 |
| 184759554082 | 48 | 24... a5 | good | best | precision | best | 0.0000 | 0.711 | yes | a5 | - | -1.16 | -1.49 |
| 184759554082 | 49 | 25. a4 | inaccuracy | excellent | precision | excellent | 0.0089 | 0.279 | no | Rh1 | f2f3 | -1.61 | -1.72 |
| 184759554082 | 55 | 28. Rh1 | inaccuracy | good | precision | good | 0.0476 | 0.293 | no | Rc2 | f1g1 | -1.76 | -1.76 |
| 184759554082 | 56 | 28... Ree8 | good | excellent | precision | excellent | 0.0169 | 0.754 | no | Rxh1 | - | -1.61 | -1.53 |
| 184759554082 | 57 | 29. Ka2 | good | excellent | precision | excellent | 0.0162 | 0.274 | no | Rhd1 | - | -1.73 | -1.89 |
| 185324357184 | 6 | 3... Bc5 | blunder | mistake | precision | mistake | 0.1870 | 0.510 | no | d5 | - | +3.27 | +3.23 |
| 185324357184 | 15 | 8. Qb5+ | good | excellent | precision | excellent | 0.0066 | 0.294 | no | d4 | - | -4.03 | -3.95 |
| 185324357184 | 18 | 9... Bf5 | inaccuracy | good | precision | good | 0.0345 | 0.598 | no | Ng3 | h1g3 | -0.98 | -0.96 |
| 185324357184 | 20 | 10... Nd7 | mistake | inaccuracy | precision | inaccuracy | 0.0772 | 0.577 | no | Na6 | - | +0.29 | +0.16 |
| 185324357184 | 21 | 11. Qg1 | great | best | precision | best | 0.0000 | 0.509 | yes | Qg1 | - | +0.29 | +0.20 |
| 185324357184 | 38 | 19... Qf2 | excellent | good | precision | good | 0.0210 | 0.333 | no | Qh5 | - | +3.38 | +3.60 |
| 185324357184 | 39 | 20. Rf1 | great | best | precision | best | 0.0000 | 0.695 | yes | Rf1 | - | +3.38 | +3.58 |
| 185324357184 | 43 | 22. Re2 | best | excellent | precision | excellent | 0.0006 | 0.503 | no | Rh2 | - | +0.11 | +0.00 |
| 185324357184 | 47 | 24. Rc7 | best | excellent | precision | excellent | 0.0000 | 0.509 | no | g4 | - | +0.26 | +0.31 |
| 185324357184 | 49 | 25. c3 | good | inaccuracy | precision | inaccuracy | 0.0526 | 0.525 | no | b3 | - | -0.53 | -0.49 |
| 185324357184 | 52 | 26... a5 | good | excellent | precision | excellent | 0.0194 | 0.535 | no | h6 | - | -0.29 | -0.27 |
| 185387411150 | 8 | 4... Bxd3 | book | best | precision | best | 0.0000 | 0.492 | yes | Bxd3 | - | +0.19 | +0.21 |
| 185387411150 | 9 | 5. Qxd3 | book | best | precision | best | 0.0000 | 0.512 | yes | Qxd3 | - | +0.19 | +0.22 |
| 185387411150 | 16 | 8... Nd7 | excellent | best | precision | best | 0.0000 | 0.481 | yes | Nd7 | - | +0.63 | +0.52 |
| 185387411150 | 19 | 10. h5 | inaccuracy | good | precision | good | 0.0421 | 0.560 | no | Qh3 | d3h3 | +0.48 | +0.32 |
| 185387411150 | 25 | 13. c3 | inaccuracy | good | precision | good | 0.0404 | 0.640 | no | Nc3 | b1c3 | +1.24 | +1.58 |
| 185387411150 | 27 | 14. exf6 | great | best | precision | best | 0.0000 | 0.719 | yes | exf6 | - | +3.75 | +3.92 |
| 185387411150 | 28 | 14... d4 | best | excellent | precision | excellent | 0.0009 | 0.292 | no | gxf6 | - | +3.75 | +3.95 |
| 185387411150 | 32 | 16... Bb4 | good | excellent | precision | excellent | 0.0122 | 0.230 | no | Rd4 | - | +5.56 | +5.65 |
| 185387411150 | 35 | 18. fxg7 | great | best | precision | best | 0.0000 | 0.873 | yes | fxg7 | - | +8.32 | +8.74 |
| 185387411150 | 36 | 18... Rg8 | mistake | best | precision | best | 0.0000 | 0.122 | yes | Rg8 | - | +8.79 | +9.27 |
| 185387411150 | 39 | 20. Bg3+ | best | excellent | precision | excellent | 0.0160 | 0.879 | no | Qxg8 | - | +8.79 | +8.23 |
| 185387411150 | 41 | 21. Qf7+ | best | excellent | precision | excellent | 0.0189 | 0.887 | no | Bxd6+ | - | +8.79 | +8.65 |
| 185387411150 | 46 | 23... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 50 | 25... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 52 | 26... Qh5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qh5+ | - | 0.00 | +0.00 |
| 185387411150 | 54 | 27... Qc5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qc5+ | - | 0.00 | +0.00 |
| 185387411150 | 56 | 28... Qh5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qh5+ | - | 0.00 | +0.00 |
| 185425961522 | 12 | 6... Qe6 | mistake | inaccuracy | precision | inaccuracy | 0.0570 | 0.456 | no | Qb6 | - | +1.82 | +1.78 |
| 185425961522 | 17 | 9. Qf4 | miss | inaccuracy | precision | inaccuracy | 0.0870 | 0.701 | no | Nc3 | b1c3 | +1.74 | +2.01 |
| 185425961522 | 18 | 9... Qg6 | inaccuracy | good | precision | good | 0.0422 | 0.386 | no | Nh6 | g8h6 | +2.52 | +2.68 |
| 185425961522 | 20 | 10... d5 | blunder | mistake | precision | mistake | 0.1942 | 0.475 | no | Bxa3 | - | +3.29 | +4.08 |
| 185425961522 | 24 | 12... Rd8 | best | excellent | precision | excellent | 0.0114 | 0.247 | no | Rb8 | - | +4.41 | +4.83 |
| 185425961522 | 25 | 13. Be3 | inaccuracy | good | precision | good | 0.0435 | 0.753 | no | Nb5 | a3b5 | +3.14 | +3.57 |
| 185425961522 | 30 | 15... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0910 | 0.310 | no | Qa6 | - | +5.65 | +5.50 |
| 185425961522 | 47 | 24. d7 | best | excellent | precision | excellent | 0.0048 | 0.897 | no | Ne7+ | - | +9.38 | +9.13 |
| 185436488062 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0205 | 0.547 | no | h3 | - | +0.65 | +0.50 |
| 185438343298 | 17 | 9. d3 | mistake | blunder | precision | blunder | 0.2035 | 0.203 | no | hxg3 | h2g3 | -M2 | -M2 |
| 185439816356 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0214 | 0.550 | no | h3 | - | +0.65 | +0.50 |
| 185466827454 | 12 | 6... dxe4 | book | best | precision | best | 0.0000 | 0.508 | yes | dxe4 | - | -0.12 | -0.08 |
| 185466827454 | 13 | 7. Bxe4 | book | best | precision | best | 0.0000 | 0.495 | yes | Bxe4 | - | -0.12 | -0.12 |
| 185466827454 | 15 | 8. c3 | excellent | best | precision | best | 0.0000 | 0.523 | yes | c3 | - | +0.27 | +0.31 |
| 185466827454 | 16 | 8... Be6 | good | excellent | precision | excellent | 0.0054 | 0.482 | no | O-O | - | +0.60 | +0.40 |
| 185466827454 | 17 | 9. d4 | inaccuracy | good | precision | good | 0.0334 | 0.524 | no | O-O | - | -0.20 | -0.16 |
| 185466827454 | 19 | 10. cxd4 | excellent | good | precision | good | 0.0256 | 0.493 | no | O-O | - | -0.40 | -0.54 |
| 185466827454 | 21 | 11. Nxd4 | inaccuracy | good | precision | good | 0.0352 | 0.456 | no | Bxb7 | e4b7 | -1.39 | -1.63 |
| 185466827454 | 23 | 12. O-O | miss | inaccuracy | precision | inaccuracy | 0.0908 | 0.520 | no | Bxb7 | e4b7 | -1.52 | -1.69 |
| 185466827454 | 27 | 14. Bc6+ | good | excellent | precision | excellent | 0.0083 | 0.515 | no | Qa4+ | - | -0.08 | -0.06 |
| 185466827454 | 29 | 15. Qa4 | best | excellent | precision | excellent | 0.0024 | 0.495 | no | Qc2 | - | -0.08 | -0.01 |
| 185466827454 | 30 | 15... Qg6 | mistake | inaccuracy | precision | inaccuracy | 0.0926 | 0.501 | no | g5 | g7g5 | +1.33 | +1.56 |
| 185466827454 | 31 | 16. Qa3+ | inaccuracy | good | precision | good | 0.0391 | 0.592 | no | Be3 | f1d1 | +0.78 | +0.89 |
| 185466827454 | 34 | 17... Be5 | good | excellent | precision | excellent | 0.0112 | 0.454 | no | Bxe3 | - | +1.05 | +1.01 |
| 185466827454 | 35 | 18. f4 | good | excellent | precision | excellent | 0.0165 | 0.560 | no | Qxa7 | - | +0.61 | +0.73 |
| 185466827454 | 40 | 20... h6 | inaccuracy | good | precision | good | 0.0299 | 0.847 | no | Qa6 | d3a6 | -5.82 | -6.28 |
| 185466827454 | 43 | 22. Bf3 | mistake | good | precision | good | 0.0272 | 0.201 | no | f5 | - | -6.29 | -6.54 |
| 185466827454 | 45 | 23. Kh1 | inaccuracy | good | precision | good | 0.0375 | 0.207 | no | Bxc5 | - | -7.22 | -6.79 |
| 185466827454 | 46 | 23... Rxd1 | best | excellent | precision | excellent | 0.0067 | 0.835 | no | Qxf1+ | - | -7.22 | -7.50 |
| 185466827454 | 49 | 25. Rd8+ | good | excellent | precision | excellent | 0.0122 | 0.141 | no | f5 | - | -8.48 | -8.02 |
| 185466827454 | 53 | 27. Re1 | excellent | good | precision | good | 0.0431 | 0.117 | no | b4 | - | -8.57 | -10.58 |
| 185466827454 | 54 | 27... Bg4 | best | good | precision | good | 0.0224 | 0.926 | no | Re8 | - | -8.57 | -9.37 |
| 185466827454 | 55 | 28. Be4+ | excellent | best | precision | best | 0.0000 | 0.097 | yes | Be4+ | - | -9.21 | -10.51 |
| 185466827454 | 56 | 28... g6 | best | excellent | precision | excellent | 0.0158 | 0.925 | no | f5 | - | -9.21 | -11.13 |
| 185466827454 | 58 | 29... Bf2 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Re8 | - | -12.4 | -M13 |
| 185466827454 | 59 | 30. Rf1 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | hxg4 | - | -M7 | -M10 |
| 185466827454 | 60 | 30... Be2 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qxe4 | - | -10.4 | -M11 |
| 185466827454 | 61 | 31. Rxf2 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Rxf2 | - | -11.6 | -10.41 |
| 185468039834 | 11 | 6. Nd5 | best | excellent | precision | excellent | 0.0092 | 0.448 | no | Na4 | - | -0.94 | -0.95 |
| 185468039834 | 18 | 9... Ne5 | excellent | good | precision | good | 0.0380 | 0.467 | no | Kf8 | - | +0.61 | +1.22 |
| 185468039834 | 20 | 10... fxe5 | inaccuracy | good | precision | good | 0.0295 | 0.434 | no | dxe5 | d6e5 | +1.53 | +1.67 |
| 185468039834 | 21 | 11. Qh5 | excellent | best | precision | best | 0.0000 | 0.596 | yes | Qh5 | - | +1.48 | +1.34 |
| 185468039834 | 23 | 12. Qf3 | miss | mistake | precision | mistake | 0.1879 | 0.626 | no | Nxc7+ | d5c7 | -0.91 | -1.07 |
| 185468039834 | 25 | 13. Nf6+ | good | best | precision | best | 0.0000 | 0.434 | yes | Nf6+ | - | -1.28 | -1.15 |
| 185468039834 | 30 | 15... Rf8 | great | best | precision | best | 0.0000 | 0.692 | yes | Rf8 | - | -3.36 | -3.52 |
| 185468039834 | 33 | 17. Qh3 | best | excellent | precision | excellent | 0.0015 | 0.309 | no | Qd3 | - | -3.39 | -3.65 |
| 185468039834 | 36 | 18... a5 | good | excellent | precision | excellent | 0.0190 | 0.697 | no | Rf7 | - | -2.75 | -3.19 |
| 185468614210 | 10 | 5... exd4 | book | best | precision | best | 0.0000 | 0.498 | yes | exd4 | - | +0.15 | +0.02 |
| 185468614210 | 12 | 6... Bb4+ | book | best | precision | best | 0.0000 | 0.506 | yes | Bb4+ | - | 0.00 | +0.01 |
| 185468614210 | 13 | 7. Nc3 | book | good | precision | good | 0.0233 | 0.501 | no | Bd2 | - | -0.35 | -0.39 |
| 185468614210 | 16 | 8... Bxc3+ | inaccuracy | good | precision | good | 0.0410 | 0.471 | no | Nxe4 | f6e4 | +1.21 | +1.27 |
| 185468614210 | 32 | 16... Be6 | inaccuracy | good | precision | good | 0.0233 | 0.492 | no | Kg8 | h7g8 | +1.21 | +0.54 |
| 185468614210 | 33 | 17. Ng5+ | inaccuracy | good | precision | good | 0.0215 | 0.531 | no | Qh5+ | d5h5 | +0.18 | +0.16 |
| 185468614210 | 48 | 24... Rxc3 | best | excellent | precision | excellent | 0.0047 | 0.500 | no | g6 | - | +0.14 | +0.03 |
| 185475865432 | 3 | 2. Nf3 | book | excellent | precision | excellent | 0.0162 | 0.553 | no | d4 | - | +0.74 | +0.69 |
| 185475865432 | 4 | 2... Bb7 | book | best | precision | best | 0.0000 | 0.460 | yes | Bb7 | - | +0.74 | +0.64 |
| 185475865432 | 5 | 3. Nc3 | book | best | precision | best | 0.0000 | 0.537 | yes | Nc3 | - | +0.74 | +0.67 |
| 185475865432 | 6 | 3... e6 | book | best | precision | best | 0.0000 | 0.461 | yes | e6 | - | +0.74 | +0.68 |
| 185475865432 | 10 | 5... b5 | best | excellent | precision | excellent | 0.0081 | 0.467 | no | Bb4 | - | +0.55 | +0.70 |
| 185475865432 | 19 | 10. O-O | good | excellent | precision | excellent | 0.0097 | 0.568 | no | e5 | - | +0.82 | +1.00 |
| 185475865432 | 21 | 11. dxe6 | mistake | inaccuracy | precision | inaccuracy | 0.0825 | 0.546 | no | Ng3 | e2g3 | -0.76 | -0.63 |
| 185475865432 | 28 | 14... Nxg3 | inaccuracy | good | precision | good | 0.0392 | 0.616 | no | Qxd1 | d8d1 | -1.24 | -1.33 |
| 185475865432 | 29 | 15. Bxg3 | good | excellent | precision | excellent | 0.0141 | 0.423 | no | hxg3 | - | -1.52 | -1.63 |
| 185475865432 | 32 | 16... Bf6 | good | excellent | precision | excellent | 0.0023 | 0.593 | no | Bd6 | - | -1.25 | -1.45 |
| 185475865432 | 33 | 17. Qxd8+ | good | excellent | precision | excellent | 0.0141 | 0.416 | no | Re1 | - | -1.78 | -1.70 |
| 185475865432 | 34 | 17... Rxd8 | inaccuracy | good | precision | good | 0.0420 | 0.598 | no | Kxd8 | e8d8 | -0.89 | -0.96 |
| 185475865432 | 49 | 25. a6 | mistake | good | precision | good | 0.0452 | 0.685 | no | Rxe6 | d6e6 | +1.47 | +2.47 |
| 185475865432 | 50 | 25... Bh5 | mistake | inaccuracy | precision | inaccuracy | 0.0932 | 0.360 | no | Be5 | - | +3.93 | +4.34 |
| 185476493194 | 6 | 3... Bc5 | book | excellent | precision | excellent | 0.0036 | 0.495 | no | c6 | - | +0.21 | +0.22 |
| 185476493194 | 7 | 4. Nf3 | book | best | precision | best | 0.0000 | 0.513 | yes | Nf3 | - | +0.21 | +0.14 |
| 185476493194 | 8 | 4... Nc6 | book | excellent | precision | excellent | 0.0066 | 0.492 | no | O-O | - | +0.26 | +0.22 |
| 185476493194 | 9 | 5. O-O | book | best | precision | best | 0.0000 | 0.513 | yes | O-O | - | +0.26 | +0.15 |
| 185476493194 | 10 | 5... d6 | book | excellent | precision | excellent | 0.0006 | 0.491 | no | h6 | - | +0.27 | +0.25 |
| 185476493194 | 12 | 6... O-O | excellent | best | precision | best | 0.0000 | 0.491 | no | a6 | - | +0.21 | +0.17 |
| 185476493194 | 26 | 13... g5 | mistake | excellent | precision | excellent | 0.0104 | 0.245 | no | Qg4 | - | +5.10 | +5.33 |
| 185476493194 | 28 | 14... hxg5 | inaccuracy | good | precision | good | 0.0460 | 0.211 | no | Qg4 | g8h7 | +6.38 | +6.80 |
| 185476493194 | 34 | 17... Qe7 | blunder | mistake | precision | mistake | 0.1767 | 0.342 | no | Qd8 | - | +6.88 | +6.78 |
| 185476493194 | 39 | 20. c3 | good | excellent | precision | excellent | 0.0179 | 0.883 | no | Qg5+ | - | +7.53 | +7.98 |
| 185476493194 | 42 | 21... Bg6 | mistake | excellent | precision | excellent | 0.0179 | 0.098 | no | Kh8 | g8h7 | +9.17 | +10.26 |
| 185476493194 | 43 | 22. cxd4 | excellent | good | precision | good | 0.0412 | 0.921 | no | Qxg6+ | - | +8.14 | +8.47 |
| 185962590893 | 9 | 5. Nbd2 | good | inaccuracy | precision | inaccuracy | 0.0601 | 0.617 | no | Bc4 | - | +0.50 | +0.36 |
| 185962590893 | 18 | 9... e5 | great | best | precision | best | 0.0000 | 0.415 | yes | e5 | - | +0.67 | +0.62 |
| 185962590893 | 19 | 10. Bd2 | good | excellent | precision | excellent | 0.0139 | 0.597 | no | Bg5 | - | +0.50 | +0.35 |
| 185962590893 | 20 | 10... Be7 | excellent | best | precision | best | 0.0000 | 0.444 | yes | Be7 | - | +0.55 | +0.47 |
| 185962590893 | 22 | 11... b5 | inaccuracy | mistake | precision | mistake | 0.1413 | 0.451 | no | O-O | e8h8 | +0.92 | +1.26 |
| 185962590893 | 24 | 12... O-O | best | excellent | precision | excellent | 0.0078 | 0.423 | no | Nc5 | - | +0.66 | +0.55 |
| 185962590893 | 27 | 14. Nxe7+ | miss | inaccuracy | precision | inaccuracy | 0.0599 | 0.752 | no | Bh6 | d2h6 | +1.01 | +1.20 |
| 185962590893 | 32 | 16... Nb6 | inaccuracy | good | precision | good | 0.0364 | 0.304 | no | Nf8 | f6e8 | +1.62 | +1.58 |
| 185962590893 | 33 | 17. Be2 | mistake | inaccuracy | precision | inaccuracy | 0.0612 | 0.732 | no | Rxd8+ | d1d8 | +0.96 | +1.12 |
| 185962590893 | 43 | 22. Bd2 | good | excellent | precision | excellent | 0.0161 | 0.651 | no | Qe2 | - | +0.86 | +0.84 |
| 185962590893 | 46 | 23... Qe7 | good | excellent | precision | excellent | 0.0000 | 0.386 | no | Nd7 | - | +0.86 | +0.72 |
| 185962590893 | 51 | 26. Qe3 | inaccuracy | best | precision | best | 0.0000 | 0.613 | yes | Qe3 | d3f3 | +0.47 | +0.75 |
| 185962590893 | 52 | 26... Nd4 | mistake | inaccuracy | precision | inaccuracy | 0.0553 | 0.383 | no | Nf4 | e6f4 | +1.15 | +1.36 |
| 185962590893 | 53 | 27. c3 | mistake | blunder | precision | blunder | 0.2752 | 0.704 | no | f4 | - | -0.39 | -0.45 |
| 185962590893 | 55 | 28. Kb2 | mistake | inaccuracy | precision | inaccuracy | 0.0922 | 0.437 | no | Kd1 | c1d1 | -1.21 | -1.33 |
| 185962590893 | 61 | 31. f4 | best | excellent | precision | excellent | 0.0079 | 0.482 | no | h5 | - | -0.23 | -0.18 |
| 185962590893 | 64 | 32... e5 | excellent | best | precision | best | 0.0000 | 0.500 | no | a6 | - | 0.00 | +0.00 |
| 185962590893 | 77 | 39. Kb3 | great | best | precision | best | 0.0000 | 0.500 | yes | Kb3 | - | 0.00 | +0.00 |

### `brilliant_event` (53)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 25 | 13. Kxe2 | best | brilliant | brilliant_event | best | 0.0000 | 0.538 | yes | Kxe2 | - | +0.44 | +0.26 |
| 1034847688 | 35 | 18. hxg5 | best | brilliant | brilliant_event | best | 0.0000 | 0.500 | yes | hxg5 | - | 0.00 | +0.00 |
| 1041474766 | 13 | 7. O-O | excellent | brilliant | brilliant_event | excellent | 0.0018 | 0.533 | no | d4 | - | +0.28 | +0.24 |
| 1041474766 | 19 | 10. Bd2 | excellent | brilliant | brilliant_event | excellent | 0.0053 | 0.532 | no | a3 | - | +0.25 | +0.28 |
| 1041474766 | 20 | 10... O-O | excellent | brilliant | brilliant_event | excellent | 0.0027 | 0.475 | no | Qd8 | - | +0.40 | +0.47 |
| 1041474766 | 22 | 11... Be7 | best | brilliant | brilliant_event | best | 0.0000 | 0.470 | yes | Be7 | - | +0.40 | +0.32 |
| 184759554082 | 17 | 9. Nf3 | good | brilliant | brilliant_event | excellent | 0.0158 | 0.470 | no | d3 | - | -0.39 | -0.29 |
| 184759554082 | 21 | 11. Nc3 | best | brilliant | brilliant_event | best | 0.0000 | 0.432 | yes | Nc3 | - | -0.52 | -0.54 |
| 184759554082 | 34 | 17... Qg5 | excellent | brilliant | brilliant_event | excellent | 0.0044 | 0.644 | no | Bf5 | - | -0.88 | -0.84 |
| 184759554082 | 36 | 18... Qf6 | best | brilliant | brilliant_event | best | 0.0000 | 0.671 | yes | Qf6 | - | -1.01 | -1.10 |
| 184759554082 | 37 | 19. Kb1 | good | brilliant | brilliant_event | excellent | 0.0014 | 0.332 | no | Qb2 | - | -1.19 | -1.16 |
| 184759554082 | 46 | 23... c6 | best | brilliant | brilliant_event | best | 0.0000 | 0.707 | yes | c6 | - | -1.28 | -1.21 |
| 185324357184 | 11 | 6. Nf3 | best | brilliant | brilliant_event | best | 0.0000 | 0.312 | yes | Nf3 | - | -3.32 | -3.73 |
| 185324357184 | 13 | 7. Qe2 | best | brilliant | brilliant_event | best | 0.0000 | 0.303 | yes | Qe2 | - | -3.32 | -3.83 |
| 185324357184 | 26 | 13... Nxe5 | best | brilliant | brilliant_event | best | 0.0000 | 0.435 | yes | Nxe5 | - | +1.30 | +1.57 |
| 185324357184 | 34 | 17... Rxe2 | good | brilliant | brilliant_event | excellent | 0.0113 | 0.348 | no | Bg4 | - | +3.07 | +2.96 |
| 185324357184 | 35 | 18. Bxe2 | best | brilliant | brilliant_event | best | 0.0000 | 0.663 | yes | Bxe2 | - | +3.07 | +3.12 |
| 185324357184 | 37 | 19. Re1 | great | brilliant | brilliant_event | best | 0.0000 | 0.665 | yes | Re1 | - | +3.07 | +3.03 |
| 185387411150 | 7 | 4. Bd3 | book | brilliant | brilliant_event | excellent | 0.0130 | 0.521 | no | Be2 | - | +0.19 | +0.15 |
| 185387411150 | 33 | 17. O-O | best | brilliant | brilliant_event | best | 0.0000 | 0.782 | yes | O-O | - | +5.56 | +5.36 |
| 185425961522 | 10 | 5... Qf6 | best | brilliant | brilliant_event | best | 0.0000 | 0.461 | yes | Qf6 | - | +0.73 | +0.72 |
| 185425961522 | 43 | 22. Bd6 | excellent | brilliant | brilliant_event | excellent | 0.0088 | 0.854 | no | Rac1 | - | +7.01 | +7.35 |
| 185438343298 | 14 | 7... Qh4+ | great | brilliant | brilliant_event | best | 0.0000 | 0.792 | yes | Qh4+ | - | -5.11 | -6.25 |
| 185438343298 | 16 | 8... Nxg3 | best | brilliant | brilliant_event | best | 0.0000 | 0.792 | yes | Nxg3 | - | -5.11 | -5.80 |
| 185439816356 | 11 | 6. f3 | good | brilliant | brilliant_event | excellent | 0.0101 | 0.309 | no | Be2 | - | -3.50 | -3.84 |
| 185466827454 | 11 | 6. Bd3 | book | brilliant | brilliant_event | best | 0.0000 | 0.488 | yes | Bd3 | - | -0.12 | -0.14 |
| 185466827454 | 18 | 9... exd4 | best | brilliant | brilliant_event | best | 0.0000 | 0.510 | yes | exd4 | - | -0.20 | -0.11 |
| 185466827454 | 20 | 10... Nxd4 | best | brilliant | brilliant_event | best | 0.0000 | 0.532 | yes | Nxd4 | - | -0.40 | -0.74 |
| 185466827454 | 33 | 17. Be3 | best | brilliant | brilliant_event | best | 0.0000 | 0.552 | yes | Be3 | - | +0.78 | +0.78 |
| 185468039834 | 14 | 7... h6 | good | brilliant | brilliant_event | excellent | 0.0145 | 0.489 | no | Ne5 | - | +0.60 | +0.44 |
| 185468039834 | 24 | 12... c6 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.562 | yes | c6 | - | -0.83 | -1.14 |
| 185468039834 | 26 | 13... Ke7 | best | brilliant | brilliant_event | best | 0.0000 | 0.567 | yes | Ke7 | - | -1.28 | -1.17 |
| 185468039834 | 31 | 16. b4 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.306 | no | Qh3 | - | -3.61 | -3.62 |
| 185468614210 | 9 | 5. d4 | book | brilliant | brilliant_event | excellent | 0.0076 | 0.516 | no | b4 | - | +0.15 | +0.04 |
| 185468614210 | 11 | 6. cxd4 | book | brilliant | brilliant_event | best | 0.0000 | 0.501 | yes | cxd4 | - | 0.00 | -0.10 |
| 185468614210 | 15 | 8. d5 | excellent | brilliant | brilliant_event | excellent | 0.0070 | 0.538 | no | Bg5 | - | +0.51 | +0.49 |
| 185468614210 | 24 | 12... Nxd6 | best | brilliant | brilliant_event | best | 0.0000 | 0.513 | yes | Nxd6 | - | -0.24 | -0.32 |
| 185468614210 | 25 | 13. Bd3 | good | brilliant | brilliant_event | excellent | 0.0151 | 0.481 | no | Bxd6 | - | -0.61 | -0.53 |
| 185468614210 | 27 | 14. O-O | best | brilliant | brilliant_event | best | 0.0000 | 0.509 | yes | O-O | - | +0.15 | +0.14 |
| 185468614210 | 29 | 15. Bxh7+ | best | brilliant | brilliant_event | best | 0.0000 | 0.514 | yes | Bxh7+ | - | +0.25 | +0.21 |
| 185468614210 | 30 | 15... Kxh7 | best | brilliant | brilliant_event | best | 0.0000 | 0.488 | yes | Kxh7 | - | +0.25 | +0.15 |
| 185468614210 | 34 | 17... Kg8 | great | brilliant | brilliant_event | best | 0.0000 | 0.491 | yes | Kg8 | - | +0.18 | +0.16 |
| 185468614210 | 35 | 18. Nxe6 | best | brilliant | brilliant_event | best | 0.0000 | 0.509 | yes | Nxe6 | - | +0.18 | +0.16 |
| 185468614210 | 38 | 19... Qf6 | good | brilliant | brilliant_event | excellent | 0.0128 | 0.522 | no | b6 | - | -0.09 | -0.15 |
| 185475865432 | 15 | 8. Ne2 | best | brilliant | brilliant_event | best | 0.0000 | 0.476 | yes | Ne2 | - | -0.53 | -0.41 |
| 185475865432 | 22 | 11... dxe6 | best | brilliant | brilliant_event | best | 0.0000 | 0.537 | yes | dxe6 | - | -0.76 | -0.59 |
| 185475865432 | 25 | 13. Ne5 | best | brilliant | brilliant_event | excellent | 0.0118 | 0.416 | no | Re1 | - | -1.49 | -1.66 |
| 185475865432 | 37 | 19. Rad1 | excellent | brilliant | brilliant_event | excellent | 0.0028 | 0.600 | no | Bxa5 | - | +1.50 | +1.76 |
| 185475865432 | 38 | 19... Rxd1 | best | brilliant | brilliant_event | best | 0.0000 | 0.399 | yes | Rxd1 | - | +1.50 | +1.71 |
| 185476493194 | 14 | 7... h6 | best | brilliant | brilliant_event | best | 0.0000 | 0.500 | yes | h6 | - | +0.21 | +0.17 |
| 185476493194 | 16 | 8... Nd4 | excellent | brilliant | brilliant_event | best | 0.0000 | 0.490 | yes | Nd4 | - | +0.26 | +0.19 |
| 185476493194 | 17 | 9. Nxd4 | excellent | brilliant | brilliant_event | excellent | 0.0006 | 0.511 | no | Bxf6 | - | +0.19 | +0.19 |
| 185962590893 | 34 | 17... Red7 | best | brilliant | brilliant_event | excellent | 0.0056 | 0.329 | no | Rxd1+ | - | +0.96 | +1.14 |

### `miss_detector` (9)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 1034847688 | 31 | 16. Bxg7 | blunder | miss (opportunity) | miss_detector | mistake | 0.1297 | 0.650 | no | g4 | - | -0.01 | +0.06 |
| 1034847688 | 37 | 19. Rh4 | mistake | miss (brilliant) | miss_detector | mistake | 0.1203 | 0.589 | no | Rh6 | h1h6 | -0.10 | -0.33 |
| 185387411150 | 23 | 12. Bh4 | mistake | miss (free_piece) | miss_detector | mistake | 0.1276 | 0.737 | no | exf6 | d3g6 | +1.91 | +2.57 |
| 185387411150 | 45 | 23. fxg3 | mistake | miss (tactic) | miss_detector | blunder | 0.3852 | 0.885 | no | Qb3+ | g8b3 | 0.00 | +0.00 |
| 185425961522 | 22 | 11... Be6 | blunder | miss (free_piece) | miss_detector | mistake | 0.1732 | 0.436 | no | Bxa3 | - | +4.41 | +4.46 |
| 185438343298 | 19 | 10. Kf1 | blunder | miss (tactic) | miss_detector | blunder | 0.2046 | 0.205 | no | Kd2 | - | -M1 | -M1 |
| 185466827454 | 22 | 11... Bxd4 | mistake | miss (free_piece) | miss_detector | mistake | 0.1080 | 0.596 | no | Qxd4 | d8d4 | +0.32 | +0.33 |
| 185468614210 | 7 | 4. c3 | mistake | miss (tactic) | miss_detector | mistake | 0.1468 | 0.595 | no | Nxe5 | f3e5 | -0.88 | -0.89 |
| 185476493194 | 24 | 12... Qd7 | blunder | miss (brilliant) | miss_detector | blunder | 0.2859 | 0.529 | no | c6 | - | +4.53 | +4.75 |

### `blunder_softened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 184759554082 | 28 | 14... Kxg7 | miss | mistake | blunder_softened | blunder | 0.2084 | 0.878 | no | Qxg2 | g5g2 | -0.96 | -0.79 |
| 185324357184 | 32 | 16... Qh5 | miss | mistake | blunder_softened | blunder | 0.2257 | 0.577 | no | Qxg3+ | h4g3 | +2.48 | +2.69 |

### `losing_material_hardened` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185425961522 | 42 | 21... O-O | best | mistake | losing_material_hardened | excellent | 0.0024 | 0.155 | no | Nf4 | - | +7.26 | +7.65 |

### `book` (1)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185468614210 | 5 | 3. Bc4 | inaccuracy | book | book | inaccuracy | 0.0606 | 0.527 | no | Nxe5 | f3e5 | -0.62 | -0.57 |

