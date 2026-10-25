# Calibration report: brcap-b4

- Generated: 2026-10-18T20:06:04+00:00
- Commit: `740f5a2b4756` + uncommitted backend changes (diff sha256 `fba14e3efec0`)
- Engine: Stockfish 18; depth 18, multipv 3; config override: none
- Games: 82 requested, 82 compared, 0 skipped (list: `/mnt/c/Users/khhizr/AppData/Local/Temp/claude/C--Users-khhizr-rea-projects-chess-review/d069afdb-b3fd-4d13-b5ca-b6d2f29a760a/scratchpad/b4_ids.txt`)
- Plies: 4498 aligned, 4498 scored, 0 excluded (none)

## Headline

| Metric | Value |
|---|---|
| Exact agreement | 69.7% (3133/4498) |
| Within one step | 88.2% (3967/4498) |
| Brilliant precision / recall | 0.50 / 0.38 |
| Great precision / recall | 0.33 / 0.01 |
| Brilliant per 100 moves (app / ours) | 0.36 / 0.27 |
| Great per 100 moves (app / ours) | 4.38 / 0.07 |
| Accuracy mean abs. difference | 4.65 (n=164, max 13.83) |
| Accuracy bias (ours - app) | +3.41 |
| Best move = app's suggestion | 72.8% (1759/2415 plies where the app recorded one) |

Per-100 rates use scored plies as the denominator. Within one step uses the scale best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss must match exactly. Our `forced` counts as best and `great_find` as great.

## Confusion matrix (rows = app, columns = ours)

| app \ ours | brilliant | great | best | excellent | good | book | inaccuracy | mistake | miss | blunder | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **brilliant** | **6** | . | 5 | 2 | 3 | . | . | . | . | . | 16 |
| **great** | 3 | **1** | 180 | 11 | 2 | . | . | . | . | . | 197 |
| **best** | 3 | 2 | **1153** | 147 | 11 | 12 | 2 | 2 | 1 | . | 1333 |
| **excellent** | . | . | 138 | **512** | 83 | 2 | 5 | 1 | 1 | . | 742 |
| **good** | . | . | 19 | 165 | **334** | 7 | 33 | 7 | 10 | . | 575 |
| **book** | . | . | 43 | 33 | 5 | **456** | . | . | . | . | 537 |
| **inaccuracy** | . | . | 4 | 20 | 133 | 3 | **221** | 24 | 6 | . | 411 |
| **mistake** | . | . | 7 | 9 | 12 | 2 | 78 | **194** | 23 | 12 | 337 |
| **miss** | . | . | . | . | . | . | 27 | 28 | **139** | 7 | 201 |
| **blunder** | . | . | . | . | . | . | . | 21 | 11 | **117** | 149 |
| **total** | 12 | 3 | 1549 | 899 | 583 | 482 | 366 | 277 | 191 | 136 | 4498 |

## Per label

| label | app | ours | both | precision | recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| brilliant | 16 | 12 | 6 | 0.500 | 0.375 | 0.429 |
| great | 197 | 3 | 1 | 0.333 | 0.005 | 0.010 |
| best | 1333 | 1549 | 1153 | 0.744 | 0.865 | 0.800 |
| excellent | 742 | 899 | 512 | 0.570 | 0.690 | 0.624 |
| good | 575 | 583 | 334 | 0.573 | 0.581 | 0.577 |
| book | 537 | 482 | 456 | 0.946 | 0.849 | 0.895 |
| inaccuracy | 411 | 366 | 221 | 0.604 | 0.538 | 0.569 |
| mistake | 337 | 277 | 194 | 0.700 | 0.576 | 0.632 |
| miss | 201 | 191 | 139 | 0.728 | 0.692 | 0.709 |
| blunder | 149 | 136 | 117 | 0.860 | 0.785 | 0.821 |

## Accuracy

| game | side | app | ours | ours - app |
|---|---|---:|---:|---:|
| 142636591844 | white | 76.1 | 83.3 | +7.2 |
| 142636591844 | black | 45.7 | 53.5 | +7.8 |
| 142849698970 | white | 74.2 | 74.8 | +0.6 |
| 142849698970 | black | 79.0 | 77.1 | -1.9 |
| 142849919300 | white | 64.0 | 57.8 | -6.2 |
| 142849919300 | black | 80.7 | 80.3 | -0.4 |
| 142866059618 | white | 71.3 | 73.0 | +1.7 |
| 142866059618 | black | 75.7 | 77.2 | +1.5 |
| 142873206408 | white | 80.3 | 83.6 | +3.3 |
| 142873206408 | black | 74.7 | 80.8 | +6.1 |
| 142875589252 | white | 77.8 | 78.8 | +1.0 |
| 142875589252 | black | 77.2 | 81.4 | +4.2 |
| 142917385540 | white | 60.5 | 65.1 | +4.6 |
| 142917385540 | black | 74.4 | 75.8 | +1.4 |
| 142918703388 | white | 54.9 | 56.3 | +1.4 |
| 142918703388 | black | 65.3 | 70.7 | +5.4 |
| 145833178628 | white | 59.9 | 69.3 | +9.4 |
| 145833178628 | black | 73.5 | 78.8 | +5.3 |
| 145833758308 | white | 70.9 | 57.4 | -13.5 |
| 145833758308 | black | 76.7 | 67.8 | -8.9 |
| 146658193946 | white | 88.3 | 90.5 | +2.2 |
| 146658193946 | black | 74.1 | 70.2 | -3.9 |
| 147234657424 | white | 66.7 | 68.3 | +1.6 |
| 147234657424 | black | 61.9 | 66.8 | +4.9 |
| 147295227566 | white | 65.2 | 70.4 | +5.2 |
| 147295227566 | black | 71.7 | 78.7 | +7.0 |
| 147547838342 | white | 65.6 | 71.0 | +5.4 |
| 147547838342 | black | 83.3 | 85.1 | +1.8 |
| 147619991314 | white | 72.1 | 75.4 | +3.3 |
| 147619991314 | black | 83.0 | 85.6 | +2.6 |
| 147742438276 | white | 90.4 | 89.3 | -1.1 |
| 147742438276 | black | 72.2 | 72.2 | -0.0 |
| 147786569400 | white | 83.0 | 84.8 | +1.8 |
| 147786569400 | black | 59.8 | 64.9 | +5.1 |
| 147991742972 | white | 44.8 | 58.5 | +13.7 |
| 147991742972 | black | 52.9 | 60.5 | +7.6 |
| 148014224206 | white | 62.4 | 65.3 | +2.9 |
| 148014224206 | black | 67.8 | 72.6 | +4.8 |
| 148224127998 | white | 53.6 | 57.1 | +3.5 |
| 148224127998 | black | 59.6 | 64.7 | +5.1 |
| 164007452224 | white | 73.0 | 74.8 | +1.8 |
| 164007452224 | black | 83.0 | 86.7 | +3.7 |
| 164008171476 | white | 82.6 | 86.4 | +3.8 |
| 164008171476 | black | 78.7 | 82.3 | +3.6 |
| 164188880582 | white | 80.0 | 83.8 | +3.8 |
| 164188880582 | black | 64.0 | 69.5 | +5.5 |
| 164462806840 | white | 88.1 | 90.7 | +2.6 |
| 164462806840 | black | 74.1 | 78.2 | +4.1 |
| 164784324724 | white | 83.4 | 82.4 | -1.0 |
| 164784324724 | black | 75.5 | 78.5 | +3.0 |
| 164812402934 | white | 84.0 | 83.5 | -0.5 |
| 164812402934 | black | 69.8 | 71.6 | +1.8 |
| 165327199736 | white | 72.0 | 75.6 | +3.6 |
| 165327199736 | black | 82.6 | 86.6 | +4.0 |
| 165401252676 | white | 70.5 | 73.0 | +2.5 |
| 165401252676 | black | 76.2 | 78.5 | +2.3 |
| 165450446440 | white | 63.1 | 70.0 | +6.9 |
| 165450446440 | black | 67.7 | 74.2 | +6.5 |
| 165557442658 | white | 76.9 | 78.9 | +2.0 |
| 165557442658 | black | 78.3 | 79.8 | +1.5 |
| 165974850998 | white | 78.6 | 81.5 | +2.9 |
| 165974850998 | black | 71.6 | 76.1 | +4.5 |
| 166096155098 | white | 85.4 | 80.1 | -5.3 |
| 166096155098 | black | 56.1 | 50.4 | -5.7 |
| 166583201950 | white | 53.1 | 52.1 | -1.0 |
| 166583201950 | black | 47.2 | 50.3 | +3.1 |
| 166853117390 | white | 64.9 | 68.0 | +3.1 |
| 166853117390 | black | 52.7 | 51.0 | -1.7 |
| 167316688806 | white | 84.8 | 88.0 | +3.2 |
| 167316688806 | black | 77.5 | 80.5 | +3.0 |
| 167359572290 | white | 76.1 | 70.7 | -5.4 |
| 167359572290 | black | 60.3 | 46.5 | -13.8 |
| 167396435524 | white | 71.4 | 74.3 | +2.9 |
| 167396435524 | black | 71.5 | 73.1 | +1.6 |
| 167397747616 | white | 73.5 | 77.6 | +4.1 |
| 167397747616 | black | 67.8 | 72.3 | +4.5 |
| 167479014786 | white | 72.1 | 77.2 | +5.1 |
| 167479014786 | black | 64.7 | 69.1 | +4.4 |
| 168148201932 | white | 55.1 | 61.2 | +6.1 |
| 168148201932 | black | 44.5 | 54.7 | +10.2 |
| 168426135116 | white | 79.9 | 81.3 | +1.4 |
| 168426135116 | black | 71.5 | 77.0 | +5.5 |
| 169217872990 | white | 69.8 | 72.3 | +2.5 |
| 169217872990 | black | 78.6 | 79.2 | +0.6 |
| 170185678278 | white | 52.3 | 59.8 | +7.5 |
| 170185678278 | black | 56.4 | 64.5 | +8.1 |
| 171124015136 | white | 69.3 | 60.7 | -8.6 |
| 171124015136 | black | 67.0 | 58.8 | -8.2 |
| 171708489350 | white | 66.5 | 74.9 | +8.4 |
| 171708489350 | black | 82.6 | 88.9 | +6.3 |
| 171841312410 | white | 35.3 | 46.1 | +10.8 |
| 171841312410 | black | 46.9 | 58.6 | +11.7 |
| 171887823168 | white | 63.7 | 70.3 | +6.6 |
| 171887823168 | black | 58.5 | 66.1 | +7.6 |
| 171932623366 | white | 73.2 | 79.7 | +6.5 |
| 171932623366 | black | 82.9 | 88.9 | +6.0 |
| 171980080646 | white | 87.2 | 89.4 | +2.2 |
| 171980080646 | black | 79.0 | 80.9 | +1.9 |
| 172026321412 | white | 80.4 | 84.9 | +4.5 |
| 172026321412 | black | 68.0 | 74.6 | +6.6 |
| 172349629492 | white | 79.5 | 83.6 | +4.1 |
| 172349629492 | black | 68.6 | 76.5 | +7.9 |
| 172996177054 | white | 71.7 | 78.3 | +6.6 |
| 172996177054 | black | 72.2 | 75.8 | +3.6 |
| 173068943088 | white | 59.8 | 64.9 | +5.1 |
| 173068943088 | black | 64.5 | 69.9 | +5.4 |
| 173570784620 | white | 76.4 | 78.4 | +2.0 |
| 173570784620 | black | 66.6 | 70.3 | +3.7 |
| 173618554654 | white | 85.2 | 88.4 | +3.2 |
| 173618554654 | black | 56.3 | 64.4 | +8.1 |
| 173620121124 | white | 52.7 | 62.6 | +9.9 |
| 173620121124 | black | 50.9 | 58.4 | +7.5 |
| 173667762936 | white | 47.7 | 46.4 | -1.3 |
| 173667762936 | black | 67.6 | 68.8 | +1.2 |
| 173807034866 | white | 53.6 | 59.3 | +5.7 |
| 173807034866 | black | 75.8 | 79.5 | +3.7 |
| 173855642488 | white | 75.5 | 80.7 | +5.2 |
| 173855642488 | black | 82.1 | 84.1 | +2.0 |
| 173904334944 | white | 55.9 | 58.3 | +2.4 |
| 173904334944 | black | 73.7 | 77.8 | +4.1 |
| 173905398948 | white | 76.8 | 82.3 | +5.5 |
| 173905398948 | black | 65.2 | 70.1 | +4.9 |
| 174188274588 | white | 77.3 | 82.9 | +5.6 |
| 174188274588 | black | 89.4 | 93.3 | +3.9 |
| 174336461820 | white | 49.3 | 54.7 | +5.4 |
| 174336461820 | black | 60.8 | 69.3 | +8.5 |
| 174468507028 | white | 73.7 | 77.3 | +3.6 |
| 174468507028 | black | 60.4 | 68.1 | +7.7 |
| 183978299106 | white | 65.4 | 68.5 | +3.1 |
| 183978299106 | black | 77.3 | 80.4 | +3.1 |
| 184028735740 | white | 44.5 | 49.9 | +5.4 |
| 184028735740 | black | 34.4 | 42.0 | +7.6 |
| 184110410320 | white | 55.8 | 52.3 | -3.5 |
| 184110410320 | black | 80.2 | 76.6 | -3.6 |
| 184271279368 | white | 59.9 | 59.8 | -0.1 |
| 184271279368 | black | 74.5 | 77.3 | +2.8 |
| 184449650784 | white | 69.3 | 74.7 | +5.4 |
| 184449650784 | black | 61.4 | 66.9 | +5.5 |
| 184555832944 | white | 46.3 | 49.3 | +3.0 |
| 184555832944 | black | 62.6 | 66.6 | +4.0 |
| 184797463690 | white | 77.3 | 78.3 | +1.0 |
| 184797463690 | black | 87.8 | 87.5 | -0.3 |
| 184809655978 | white | 59.2 | 61.7 | +2.5 |
| 184809655978 | black | 77.6 | 81.1 | +3.5 |
| 184809852108 | white | 54.2 | 64.3 | +10.1 |
| 184809852108 | black | 60.1 | 70.0 | +9.9 |
| 184810276410 | white | 54.9 | 64.6 | +9.7 |
| 184810276410 | black | 69.1 | 79.9 | +10.8 |
| 185069669434 | white | 55.3 | 62.7 | +7.4 |
| 185069669434 | black | 62.1 | 71.6 | +9.5 |
| 185097600644 | white | 79.2 | 77.7 | -1.5 |
| 185097600644 | black | 87.7 | 88.6 | +0.9 |
| 185099205950 | white | 66.7 | 75.4 | +8.7 |
| 185099205950 | black | 73.1 | 79.3 | +6.2 |
| 185102025164 | white | 66.5 | 68.3 | +1.8 |
| 185102025164 | black | 76.4 | 77.5 | +1.1 |
| 185198810006 | white | 77.8 | 84.2 | +6.4 |
| 185198810006 | black | 66.5 | 71.9 | +5.4 |
| 185216623720 | white | 65.6 | 72.9 | +7.3 |
| 185216623720 | black | 58.8 | 67.1 | +8.3 |
| 185492163944 | white | 98.1 | 96.3 | -1.8 |
| 185492163944 | black | 77.4 | 75.6 | -1.8 |
| 185498696400 | white | 80.5 | 85.4 | +4.9 |
| 185498696400 | black | 85.5 | 89.2 | +3.7 |

## Per game

| game | plies | scored | exact | within one | source | review s |
|---|---:|---:|---:|---:|---|---:|
| 142636591844 | 35 | 35 | 65.7% | 91.4% | reviewed | 49.8 |
| 142849698970 | 37 | 37 | 73.0% | 91.9% | reviewed | 127.7 |
| 142849919300 | 56 | 56 | 73.2% | 87.5% | reviewed | 84.0 |
| 142866059618 | 106 | 106 | 66.0% | 85.8% | reviewed | 120.1 |
| 142873206408 | 101 | 101 | 76.2% | 95.0% | reviewed | 138.2 |
| 142875589252 | 44 | 44 | 77.3% | 88.6% | reviewed | 112.0 |
| 142917385540 | 36 | 36 | 66.7% | 88.9% | reviewed | 107.5 |
| 142918703388 | 54 | 54 | 77.8% | 92.6% | reviewed | 80.4 |
| 145833178628 | 66 | 66 | 60.6% | 89.4% | reviewed | 101.4 |
| 145833758308 | 128 | 128 | 66.4% | 87.5% | reviewed | 132.5 |
| 146658193946 | 55 | 55 | 78.2% | 94.5% | reviewed | 92.9 |
| 147234657424 | 51 | 51 | 70.6% | 86.3% | reviewed | 105.4 |
| 147295227566 | 78 | 78 | 59.0% | 84.6% | reviewed | 103.9 |
| 147547838342 | 52 | 52 | 76.9% | 90.4% | reviewed | 75.8 |
| 147619991314 | 72 | 72 | 73.6% | 88.9% | reviewed | 122.0 |
| 147742438276 | 31 | 31 | 77.4% | 87.1% | reviewed | 55.7 |
| 147786569400 | 41 | 41 | 58.5% | 80.5% | reviewed | 88.8 |
| 147991742972 | 50 | 50 | 80.0% | 88.0% | reviewed | 92.4 |
| 148014224206 | 46 | 46 | 71.7% | 84.8% | reviewed | 76.8 |
| 148224127998 | 61 | 61 | 70.5% | 82.0% | reviewed | 107.4 |
| 164007452224 | 42 | 42 | 71.4% | 90.5% | reviewed | 53.7 |
| 164008171476 | 44 | 44 | 61.4% | 81.8% | reviewed | 81.8 |
| 164188880582 | 43 | 43 | 67.4% | 86.0% | reviewed | 50.7 |
| 164462806840 | 40 | 40 | 62.5% | 92.5% | reviewed | 73.2 |
| 164784324724 | 95 | 95 | 65.3% | 91.6% | reviewed | 86.3 |
| 164812402934 | 37 | 37 | 78.4% | 91.9% | reviewed | 64.2 |
| 165327199736 | 40 | 40 | 77.5% | 95.0% | reviewed | 75.3 |
| 165401252676 | 36 | 36 | 75.0% | 80.6% | reviewed | 41.6 |
| 165450446440 | 34 | 34 | 58.8% | 88.2% | reviewed | 65.7 |
| 165557442658 | 64 | 64 | 79.7% | 92.2% | reviewed | 73.8 |
| 165974850998 | 47 | 47 | 74.5% | 95.7% | reviewed | 69.8 |
| 166096155098 | 31 | 31 | 74.2% | 96.8% | reviewed | 53.2 |
| 166583201950 | 68 | 68 | 60.3% | 77.9% | reviewed | 80.8 |
| 166853117390 | 37 | 37 | 78.4% | 91.9% | reviewed | 43.6 |
| 167316688806 | 45 | 45 | 77.8% | 88.9% | reviewed | 82.3 |
| 167359572290 | 43 | 43 | 65.1% | 81.4% | reviewed | 70.8 |
| 167396435524 | 30 | 30 | 73.3% | 93.3% | reviewed | 38.1 |
| 167397747616 | 115 | 115 | 63.5% | 79.1% | reviewed | 155.6 |
| 167479014786 | 71 | 71 | 73.2% | 90.1% | reviewed | 88.9 |
| 168148201932 | 45 | 45 | 68.9% | 82.2% | reviewed | 139.0 |
| 168426135116 | 61 | 61 | 72.1% | 90.2% | reviewed | 111.9 |
| 169217872990 | 66 | 66 | 69.7% | 90.9% | reviewed | 59.7 |
| 170185678278 | 52 | 52 | 69.2% | 90.4% | reviewed | 118.9 |
| 171124015136 | 80 | 80 | 61.3% | 87.5% | reviewed | 70.8 |
| 171708489350 | 34 | 34 | 61.8% | 85.3% | reviewed | 78.8 |
| 171841312410 | 51 | 51 | 76.5% | 88.2% | reviewed | 71.3 |
| 171887823168 | 49 | 49 | 73.5% | 91.8% | reviewed | 72.7 |
| 171932623366 | 42 | 42 | 71.4% | 92.9% | reviewed | 95.9 |
| 171980080646 | 51 | 51 | 78.4% | 96.1% | reviewed | 59.3 |
| 172026321412 | 43 | 43 | 65.1% | 95.3% | reviewed | 71.8 |
| 172349629492 | 51 | 51 | 60.8% | 86.3% | reviewed | 64.7 |
| 172996177054 | 68 | 68 | 60.3% | 77.9% | reviewed | 110.4 |
| 173068943088 | 64 | 64 | 67.2% | 81.2% | reviewed | 95.3 |
| 173570784620 | 63 | 63 | 74.6% | 92.1% | reviewed | 113.9 |
| 173618554654 | 31 | 31 | 83.9% | 93.5% | reviewed | 46.2 |
| 173620121124 | 85 | 85 | 67.1% | 81.2% | reviewed | 116.9 |
| 173667762936 | 62 | 62 | 61.3% | 71.0% | reviewed | 65.8 |
| 173807034866 | 50 | 50 | 76.0% | 90.0% | reviewed | 103.4 |
| 173855642488 | 70 | 70 | 64.3% | 95.7% | reviewed | 98.9 |
| 173904334944 | 40 | 40 | 82.5% | 97.5% | reviewed | 76.8 |
| 173905398948 | 57 | 57 | 68.4% | 89.5% | reviewed | 104.9 |
| 174188274588 | 54 | 54 | 68.5% | 94.4% | reviewed | 71.8 |
| 174336461820 | 36 | 36 | 77.8% | 94.4% | reviewed | 93.3 |
| 174468507028 | 57 | 57 | 71.9% | 89.5% | reviewed | 75.8 |
| 183978299106 | 42 | 42 | 85.7% | 97.6% | reviewed | 89.3 |
| 184028735740 | 73 | 73 | 60.3% | 75.3% | reviewed | 135.9 |
| 184110410320 | 44 | 44 | 81.8% | 93.2% | reviewed | 61.7 |
| 184271279368 | 44 | 44 | 65.9% | 75.0% | reviewed | 76.8 |
| 184449650784 | 69 | 69 | 63.8% | 88.4% | reviewed | 111.8 |
| 184555832944 | 54 | 54 | 77.8% | 92.6% | reviewed | 58.7 |
| 184797463690 | 56 | 56 | 67.9% | 96.4% | reviewed | 102.8 |
| 184809655978 | 32 | 32 | 75.0% | 93.8% | reviewed | 38.1 |
| 184809852108 | 48 | 48 | 62.5% | 81.2% | reviewed | 67.7 |
| 184810276410 | 30 | 30 | 63.3% | 93.3% | reviewed | 36.6 |
| 185069669434 | 48 | 48 | 79.2% | 89.6% | reviewed | 79.2 |
| 185097600644 | 34 | 34 | 58.8% | 61.8% | reviewed | 34.6 |
| 185099205950 | 104 | 104 | 65.4% | 92.3% | reviewed | 109.8 |
| 185102025164 | 30 | 30 | 90.0% | 96.7% | reviewed | 38.1 |
| 185198810006 | 39 | 39 | 82.1% | 92.3% | reviewed | 59.7 |
| 185216623720 | 82 | 82 | 59.8% | 76.8% | reviewed | 124.4 |
| 185492163944 | 37 | 37 | 81.1% | 94.6% | reviewed | 39.6 |
| 185498696400 | 108 | 108 | 63.9% | 95.4% | reviewed | 106.3 |

## Mismatches by rule (1365)

| rule | mismatches | app -> ours |
|---|---:|---|
| `precision` | 1244 | great -> best x180, good -> excellent x165, best -> excellent x147, excellent -> best x138, inaccuracy -> good x133, excellent -> good x77 |
| `miss_detector` | 43 | mistake -> miss x23, blunder -> miss x11, inaccuracy -> miss x6, good -> miss x3 |
| `book` | 26 | best -> book x12, good -> book x7, inaccuracy -> book x3, excellent -> book x2, mistake -> book x2 |
| `mate_override` | 25 | good -> miss x7, excellent -> good x6, excellent -> inaccuracy x3, good -> inaccuracy x3, mistake -> inaccuracy x2, excellent -> miss x1 |
| `losing_material_hardened` | 17 | inaccuracy -> mistake x9, good -> mistake x5, best -> mistake x2, excellent -> mistake x1 |
| `brilliant_event` | 6 | great -> brilliant x3, best -> brilliant x3 |
| `blunder_softened` | 2 | blunder -> mistake x2 |
| `great_find_event` | 2 | best -> great x2 |

### `precision` (1244)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 142636591844 | 5 | 3. Nc3 | inaccuracy | good | precision | good | 0.0308 | 0.572 | no | d4 | d4 | +0.63 | +0.61 |
| 142636591844 | 6 | 3... Bd6 | mistake | inaccuracy | precision | inaccuracy | 0.0953 | 0.464 | no | d6 | d6 | +2.32 | +2.28 |
| 142636591844 | 8 | 4... Ne7 | mistake | inaccuracy | precision | inaccuracy | 0.0965 | 0.407 | no | Nf6 | Nf6 | +3.33 | +3.39 |
| 142636591844 | 10 | 5... b5 | inaccuracy | good | precision | good | 0.0432 | 0.447 | no | Bc7 | Bc7 | +1.67 | +1.66 |
| 142636591844 | 16 | 8... f5 | excellent | good | precision | good | 0.0261 | 0.252 | no | Ng8 | Ng8 | +4.95 | +5.17 |
| 142636591844 | 18 | 9... Rh8 | good | excellent | precision | excellent | 0.0168 | 0.232 | no | b4 | b4 | +5.41 | +5.49 |
| 142636591844 | 19 | 10. Ng5 | inaccuracy | good | precision | good | 0.0340 | 0.785 | no | Qh3 | Qh3 | +3.98 | +4.33 |
| 142636591844 | 20 | 10... Bb4 | mistake | good | precision | good | 0.0334 | 0.265 | no | Qc7 | Qc7 | +4.84 | +5.01 |
| 142636591844 | 24 | 12... d6 | good | inaccuracy | precision | inaccuracy | 0.0535 | 0.302 | no | c5 | Qa5 | +4.28 | +4.69 |
| 142636591844 | 25 | 13. exf5 | excellent | best | precision | best | 0.0000 | 0.751 | yes | exf5 | gxf5 | +4.15 | +4.38 |
| 142636591844 | 30 | 15... Bxf5 | mistake | good | precision | good | 0.0219 | 0.238 | no | Qd7 | Nxf5 | +5.42 | +5.47 |
| 142849698970 | 6 | 3... Bc5 | book | good | precision | good | 0.0322 | 0.490 | no | Nf6 | - | +0.72 | +0.65 |
| 142849698970 | 8 | 4... d6 | book | excellent | precision | excellent | 0.0013 | 0.490 | no | Nf6 | - | +0.21 | +0.26 |
| 142849698970 | 10 | 5... Bg4 | good | excellent | precision | excellent | 0.0136 | 0.493 | no | Na5 | Na5 | +0.38 | +0.32 |
| 142849698970 | 17 | 9. Nxf7 | blunder | mistake | precision | mistake | 0.1798 | 0.484 | no | Nf3 | Nf3 | -3.16 | -3.19 |
| 142849698970 | 22 | 11... Qf6 | best | excellent | precision | excellent | 0.0092 | 0.756 | no | Bb4 | - | -4.34 | -4.28 |
| 142849698970 | 23 | 12. O-O | excellent | good | precision | good | 0.0322 | 0.248 | no | Be3 | Be3 | -4.44 | -4.98 |
| 142849698970 | 30 | 15... Ne2+ | mistake | inaccuracy | precision | inaccuracy | 0.0613 | 0.901 | no | Qxg4+ | Qxg4+ | -4.93 | -6.39 |
| 142849698970 | 34 | 17... Qh4+ | excellent | best | precision | best | 0.0000 | 0.794 | yes | Qh4+ | Bb6 | -4.80 | -5.10 |
| 142849698970 | 37 | 19. Bxg5 | great | best | precision | best | 0.0000 | 0.821 | yes | Bxg5 | - | - | +6.15 |
| 142849919300 | 10 | 5... O-O | book | excellent | precision | excellent | 0.0019 | 0.487 | no | h6 | - | +0.19 | +0.20 |
| 142849919300 | 14 | 7... Nxd5 | blunder | mistake | precision | mistake | 0.1955 | 0.468 | no | Na5 | Na5 | +3.77 | +3.83 |
| 142849919300 | 18 | 9... Qxd5 | great | best | precision | best | 0.0000 | 0.551 | yes | Qxd5 | - | -0.67 | -0.85 |
| 142849919300 | 24 | 12... Nxa1 | miss | inaccuracy | precision | inaccuracy | 0.0800 | 0.916 | no | Qxd3+ | Qxd3+ | -5.88 | -6.30 |
| 142849919300 | 25 | 13. Ne4 | mistake | inaccuracy | precision | inaccuracy | 0.0695 | 0.166 | no | Nxc5 | Qf3 | -8.96 | -8.73 |
| 142849919300 | 30 | 15... Qxc1+ | best | good | precision | good | 0.0242 | 0.910 | no | Qxa4 | - | -8.96 | -7.97 |
| 142849919300 | 31 | 16. Ke2 | mistake | best | precision | best | 0.0000 | 0.115 | yes | Ke2 | Qd1 | -9.67 | -9.63 |
| 142849919300 | 33 | 17. Nxc5 | mistake | best | precision | best | 0.0000 | 0.061 | yes | Nxc5 | g3 | -10.12 | -10.66 |
| 142849919300 | 39 | 20. f3 | excellent | best | precision | best | 0.0000 | 0.033 | yes | f3 | Kf1 | -11.31 | -14.09 |
| 142849919300 | 41 | 21. Ke3 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Nf2 | Nf2 | -M8 | -M8 |
| 142849919300 | 42 | 21... Nc2+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rfd8 | - | -M7 | -M11 |
| 142849919300 | 44 | 22... Rad8+ | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rfd8+ | - | -M6 | -M8 |
| 142849919300 | 46 | 23... Qe2+ | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Ne3+ | Ne3+ | -13.10 | -M8 |
| 142866059618 | 8 | 4... Be4 | book | best | precision | best | 0.0000 | 0.497 | yes | Be4 | - | +0.29 | +0.20 |
| 142866059618 | 9 | 5. f3 | book | best | precision | best | 0.0000 | 0.513 | yes | f3 | - | +0.29 | +0.06 |
| 142866059618 | 10 | 5... Bg6 | book | best | precision | best | 0.0000 | 0.496 | yes | Bg6 | - | +0.29 | +0.14 |
| 142866059618 | 13 | 7. Bxg6 | best | excellent | precision | excellent | 0.0006 | 0.457 | no | Be3 | - | -0.50 | -0.52 |
| 142866059618 | 16 | 8... f5 | miss | mistake | precision | mistake | 0.1527 | 0.641 | no | Qh4+ | Qh4+ | +0.18 | +0.19 |
| 142866059618 | 17 | 9. g5 | excellent | best | precision | best | 0.0000 | 0.512 | yes | g5 | exf6 | +0.08 | +0.11 |
| 142866059618 | 18 | 9... Nd7 | excellent | best | precision | best | 0.0000 | 0.493 | yes | Nd7 | Na6 | +0.21 | +0.23 |
| 142866059618 | 19 | 10. Be3 | excellent | good | precision | good | 0.0230 | 0.515 | no | Nd2 | c3 | 0.00 | -0.13 |
| 142866059618 | 21 | 11. dxc5 | great | best | precision | best | 0.0000 | 0.732 | yes | dxc5 | - | +3.83 | +3.69 |
| 142866059618 | 25 | 13. Ke2 | mistake | blunder | precision | blunder | 0.2551 | 0.703 | no | Bxc5 | Bxc5 | -0.98 | -0.82 |
| 142866059618 | 35 | 18. Ke2 | excellent | best | precision | best | 0.0000 | 0.468 | yes | Ke2 | Kc4 | -0.71 | -0.73 |
| 142866059618 | 36 | 18... Ne7 | excellent | best | precision | best | 0.0000 | 0.547 | yes | Ne7 | Bxc3 | -0.59 | -0.60 |
| 142866059618 | 44 | 22... Rxd8 | good | best | precision | best | 0.0000 | 0.490 | yes | Rxd8 | Kxd8 | +0.47 | +0.00 |
| 142866059618 | 46 | 23... Bb2 | excellent | inaccuracy | precision | inaccuracy | 0.0579 | 0.500 | no | Bb4 | Ba5 | +0.69 | +0.91 |
| 142866059618 | 47 | 24. Rb1 | good | inaccuracy | precision | inaccuracy | 0.0579 | 0.558 | no | h4 | h4 | -0.04 | +0.00 |
| 142866059618 | 50 | 25... Rxd4 | great | best | precision | best | 0.0000 | 0.741 | yes | Rxd4 | - | -4.11 | -4.86 |
| 142866059618 | 51 | 26. c3 | inaccuracy | good | precision | good | 0.0343 | 0.224 | no | h4 | h4 | -5.18 | -5.68 |
| 142866059618 | 53 | 27. Ke2 | excellent | best | precision | best | 0.0000 | 0.204 | yes | Ke2 | Kf2 | -5.33 | -5.76 |
| 142866059618 | 55 | 28. Rb3 | good | inaccuracy | precision | inaccuracy | 0.0782 | 0.182 | no | Kf2 | Kd1 | -5.87 | -8.42 |
| 142866059618 | 59 | 30. Kd3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.110 | no | Kd2 | Kd2 | -7.66 | -8.15 |
| 142866059618 | 60 | 30... c5 | inaccuracy | excellent | precision | excellent | 0.0010 | 0.889 | no | Bc1 | Bc1 | -5.86 | -8.11 |
| 142866059618 | 61 | 31. Kc4 | inaccuracy | best | precision | best | 0.0000 | 0.112 | yes | Kc4 | Kc2 | -7.85 | -8.17 |
| 142866059618 | 62 | 31... Kb7 | best | excellent | precision | excellent | 0.0000 | 0.890 | no | Kc7 | - | -7.85 | -8.55 |
| 142866059618 | 64 | 32... a4 | good | excellent | precision | excellent | 0.0195 | 0.892 | no | a6+ | a6+ | -6.89 | -7.54 |
| 142866059618 | 65 | 33. Kxa4 | excellent | best | precision | best | 0.0000 | 0.127 | yes | Kxa4 | bxa4 | -7.28 | -8.02 |
| 142866059618 | 66 | 33... Bc1 | best | excellent | precision | excellent | 0.0008 | 0.886 | no | Bb2 | - | -7.28 | -7.88 |
| 142866059618 | 73 | 37. b4 | good | excellent | precision | excellent | 0.0050 | 0.068 | no | Kb5 | Kd6 | -8.00 | -10.58 |
| 142866059618 | 76 | 38... f2 | excellent | best | precision | best | 0.0000 | 0.951 | yes | f2 | Be7+ | -8.75 | -M12 |
| 142866059618 | 77 | 39. Kd6 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb4 | Kc4 | -M5 | -M7 |
| 142866059618 | 91 | 46. Kd4 | excellent | best | precision | best | 0.0000 | 0.000 | yes | Kd4 | Kf4 | -M4 | -M7 |
| 142866059618 | 96 | 48... Qd5 | excellent | best | precision | best | 0.0000 | 1.000 | no | Qe2 | Qe2 | -M4 | -M6 |
| 142866059618 | 100 | 50... Qd4 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Bg5+ | - | -M3 | -M7 |
| 142866059618 | 101 | 51. Kb1 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kc2 | - | -M3 | -M3 |
| 142873206408 | 3 | 2. e3 | book | excellent | precision | excellent | 0.0006 | 0.478 | no | Nf3 | - | -0.39 | -0.31 |
| 142873206408 | 10 | 5... Nd6 | excellent | best | precision | best | 0.0000 | 0.542 | yes | Nd6 | Nc5 | -0.61 | -0.69 |
| 142873206408 | 12 | 6... e5 | best | excellent | precision | excellent | 0.0037 | 0.601 | no | h6 | - | -1.55 | -1.46 |
| 142873206408 | 19 | 10. Qxe7+ | great | best | precision | best | 0.0000 | 0.388 | yes | Qxe7+ | - | -1.63 | -1.70 |
| 142873206408 | 23 | 12. Be2 | excellent | good | precision | good | 0.0280 | 0.367 | no | Kd2 | Kd2 | -2.48 | -2.41 |
| 142873206408 | 25 | 13. Bxg4+ | great | best | precision | best | 0.0000 | 0.736 | yes | Bxg4+ | - | +3.99 | +3.97 |
| 142873206408 | 35 | 18. Bd2 | good | excellent | precision | excellent | 0.0103 | 0.777 | no | Bxf5 | Bxf5 | +4.71 | +4.83 |
| 142873206408 | 37 | 19. Bxc3 | best | excellent | precision | excellent | 0.0055 | 0.766 | no | Nxc3 | - | +4.71 | +4.51 |
| 142873206408 | 41 | 21. Nxc3 | best | excellent | precision | excellent | 0.0126 | 0.798 | no | Nf3 | - | +5.04 | +5.12 |
| 142873206408 | 42 | 21... Bxb4 | excellent | best | precision | best | 0.0000 | 0.213 | yes | Bxb4 | Rhf8 | +5.06 | +5.09 |
| 142873206408 | 45 | 23. Bxe6+ | best | excellent | precision | excellent | 0.0014 | 0.768 | no | Bh3 | - | +4.81 | +4.70 |
| 142873206408 | 51 | 26. Re1 | excellent | good | precision | good | 0.0222 | 0.773 | no | Rf1 | Rf1 | +4.39 | +4.31 |
| 142873206408 | 59 | 30. Nf4 | best | excellent | precision | excellent | 0.0000 | 0.759 | no | Rg1 | - | +4.46 | +4.71 |
| 142873206408 | 64 | 32... R4d6 | good | excellent | precision | excellent | 0.0115 | 0.229 | no | Rxe4 | Rxe4 | +5.03 | +5.05 |
| 142873206408 | 67 | 34. Ne6 | best | excellent | precision | excellent | 0.0059 | 0.793 | no | Rde1 | - | +5.09 | +5.13 |
| 142873206408 | 72 | 36... Rxd1 | miss | inaccuracy | precision | inaccuracy | 0.0867 | 0.207 | no | Rxg6 | Rxg6 | +7.54 | +7.79 |
| 142873206408 | 74 | 37... Kd7 | excellent | best | precision | best | 0.0000 | 0.099 | yes | Kd7 | a6 | +7.65 | +8.29 |
| 142873206408 | 75 | 38. Nf5 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.893 | no | Nh5 | Nh5 | +6.17 | +9.15 |
| 142873206408 | 78 | 39... Ke6 | excellent | best | precision | best | 0.0000 | 0.000 | no | a6 | Kc7 | M5 | M5 |
| 142873206408 | 89 | 45. e5 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qh5 | Ke2 | +11.50 | M7 |
| 142873206408 | 90 | 45... Kxh2 | good | excellent | precision | excellent | 0.0000 | 0.000 | no | Kg2 | Kg4 | M4 | M7 |
| 142873206408 | 92 | 46... h3 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kg3 | Kg3 | M4 | M4 |
| 142873206408 | 94 | 47... Kg2 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kg3 | - | M4 | M4 |
| 142875589252 | 7 | 4. d5 | excellent | best | precision | best | 0.0000 | 0.580 | yes | d5 | dxe5 | +1.01 | +1.25 |
| 142875589252 | 8 | 4... Nd4 | miss | mistake | precision | mistake | 0.1063 | 0.421 | no | Nb8 | Nb8 | +3.10 | +3.05 |
| 142875589252 | 15 | 8. dxc6 | great | best | precision | best | 0.0000 | 0.733 | yes | dxc6 | - | +4.12 | +4.07 |
| 142875589252 | 23 | 12. exd5 | inaccuracy | good | precision | good | 0.0495 | 0.804 | no | Bg5 | Bg5 | +4.07 | +4.39 |
| 142875589252 | 27 | 14. Bxf6 | best | excellent | precision | excellent | 0.0043 | 0.753 | no | O-O-O | - | +4.15 | +4.26 |
| 142875589252 | 34 | 17... Bb4+ | mistake | inaccuracy | precision | inaccuracy | 0.0977 | 0.342 | no | Qxg2 | Qxg2 | +4.71 | +4.42 |
| 142875589252 | 36 | 18... Rxe2+ | mistake | excellent | precision | excellent | 0.0095 | 0.221 | no | Qh5 | Qh5 | +4.77 | +5.16 |
| 142875589252 | 39 | 20. Kf1 | best | excellent | precision | excellent | 0.0104 | 0.812 | no | Kd2 | - | +4.77 | +5.63 |
| 142875589252 | 40 | 20... Bb5+ | inaccuracy | excellent | precision | excellent | 0.0101 | 0.192 | no | Be7 | Qc4+ | +5.69 | +5.97 |
| 142875589252 | 44 | 22... Qe3# | great | best | precision | best | 0.0000 | 1.000 | yes | Qe3# | - | - | -# |
| 142917385540 | 11 | 6. h3 | excellent | good | precision | good | 0.0214 | 0.472 | no | Qb3 | Qb3 | -0.67 | -0.78 |
| 142917385540 | 14 | 7... c6 | excellent | best | precision | best | 0.0000 | 0.547 | yes | c6 | Nc6 | -0.62 | -0.64 |
| 142917385540 | 15 | 8. d4 | excellent | best | precision | best | 0.0000 | 0.460 | yes | d4 | Be2 | -0.83 | -0.82 |
| 142917385540 | 18 | 9... Qe5 | excellent | best | precision | best | 0.0000 | 0.543 | yes | Qe5 | Qf6 | -0.54 | -0.60 |
| 142917385540 | 19 | 10. Bc4 | excellent | best | precision | best | 0.0000 | 0.462 | yes | Bc4 | O-O-O | -0.73 | -0.79 |
| 142917385540 | 21 | 11. O-O | best | excellent | precision | excellent | 0.0069 | 0.708 | no | O-O-O | - | +3.40 | +3.54 |
| 142917385540 | 22 | 11... Nd7 | excellent | good | precision | good | 0.0234 | 0.289 | no | g5 | f5 | +3.46 | +4.34 |
| 142917385540 | 26 | 13... Qc5 | inaccuracy | excellent | precision | excellent | 0.0128 | 0.182 | no | Qxf4 | Qa5 | +5.84 | +6.28 |
| 142917385540 | 31 | 16. Bf5 | mistake | blunder | precision | blunder | 0.2465 | 0.686 | no | Qe4 | Qe4 | -0.86 | -0.96 |
| 142917385540 | 36 | 18... Qh2# | great | best | precision | best | 0.0000 | 1.000 | yes | Qh2# | - | - | -# |
| 142918703388 | 8 | 4... d6 | mistake | inaccuracy | precision | inaccuracy | 0.0952 | 0.509 | no | Nxe4 | Nxe4 | +1.29 | +1.35 |
| 142918703388 | 10 | 5... a6 | mistake | inaccuracy | precision | inaccuracy | 0.0953 | 0.495 | no | Na5 | Na5 | +1.49 | +1.58 |
| 142918703388 | 27 | 14. Bb6 | good | excellent | precision | excellent | 0.0079 | 0.624 | no | d4 | d4 | +1.77 | +1.83 |
| 142918703388 | 29 | 15. a4 | excellent | good | precision | good | 0.0255 | 0.633 | no | d4 | d4 | +1.90 | +1.70 |
| 142918703388 | 34 | 17... Qxb4 | great | best | precision | best | 0.0000 | 0.602 | yes | Qxb4 | - | -1.92 | -2.07 |
| 142918703388 | 40 | 20... Bc5 | miss | blunder | precision | blunder | 0.2359 | 0.711 | no | Nf6 | Nf6 | -0.49 | +0.30 |
| 142918703388 | 43 | 22. Qf5 | inaccuracy | good | precision | good | 0.0320 | 0.262 | no | Qxe5 | Qxe5 | -4.72 | -4.69 |
| 142918703388 | 44 | 22... Qxc2 | good | excellent | precision | excellent | 0.0000 | 0.770 | no | Qf4 | Qf4 | -3.88 | -4.81 |
| 142918703388 | 48 | 24... Qxf5 | great | best | precision | best | 0.0000 | 0.872 | yes | Qxf5 | - | -7.45 | -7.89 |
| 142918703388 | 50 | 25... Rf8 | excellent | best | precision | best | 0.0000 | 0.894 | yes | Rf8 | Re8 | -7.77 | -8.21 |
| 142918703388 | 51 | 26. h3 | inaccuracy | mistake | precision | mistake | 0.1075 | 0.108 | no | f3 | f3 | -M6 | -M7 |
| 145833178628 | 2 | 1... e5 | book | best | precision | best | 0.0000 | 0.491 | yes | e5 | - | +0.07 | +0.10 |
| 145833178628 | 4 | 2... Nf6 | excellent | best | precision | best | 0.0000 | 0.518 | yes | Nf6 | d5 | -0.08 | -0.32 |
| 145833178628 | 5 | 3. f3 | inaccuracy | good | precision | good | 0.0400 | 0.481 | no | d3 | Nf3 | -1.18 | -1.00 |
| 145833178628 | 7 | 4. Bc4 | mistake | inaccuracy | precision | inaccuracy | 0.0923 | 0.514 | no | d4 | d4 | -1.28 | -1.33 |
| 145833178628 | 12 | 6... cxd5 | excellent | good | precision | good | 0.0293 | 0.658 | no | b5 | b5 | -2.28 | -2.28 |
| 145833178628 | 13 | 7. Bb5+ | excellent | best | precision | best | 0.0000 | 0.368 | yes | Bb5+ | d4 | -2.38 | -2.20 |
| 145833178628 | 14 | 7... Bd7 | inaccuracy | excellent | precision | excellent | 0.0173 | 0.627 | no | Nc6 | Nc6 | -1.68 | -1.83 |
| 145833178628 | 15 | 8. Bxd7+ | good | excellent | precision | excellent | 0.0185 | 0.393 | no | Ne2 | Ne2 | -2.14 | -2.32 |
| 145833178628 | 22 | 11... dxe4 | excellent | good | precision | good | 0.0265 | 0.776 | no | Rb8 | Rb8 | -4.64 | -4.92 |
| 145833178628 | 26 | 13... exf3 | good | excellent | precision | excellent | 0.0080 | 0.814 | no | Rb8 | Rb8 | -5.52 | -6.27 |
| 145833178628 | 31 | 16. b4 | good | excellent | precision | excellent | 0.0167 | 0.246 | no | Nd2 | Nd2 | -5.20 | -5.47 |
| 145833178628 | 32 | 16... Bb6 | good | excellent | precision | excellent | 0.0085 | 0.785 | no | Be3 | Be3 | -4.75 | -5.25 |
| 145833178628 | 33 | 17. a4 | good | excellent | precision | excellent | 0.0000 | 0.224 | no | Nd2 | Nd2 | -5.15 | -5.06 |
| 145833178628 | 34 | 17... a5 | good | excellent | precision | excellent | 0.0094 | 0.768 | no | Re3 | Re3 | -4.66 | -4.84 |
| 145833178628 | 35 | 18. bxa5 | good | excellent | precision | excellent | 0.0030 | 0.241 | no | Ra2 | Ra2 | -5.35 | -5.30 |
| 145833178628 | 37 | 19. Nd2 | best | excellent | precision | excellent | 0.0038 | 0.206 | no | Ra2 | - | -5.35 | -5.33 |
| 145833178628 | 38 | 19... Qd6 | miss | inaccuracy | precision | inaccuracy | 0.0838 | 0.779 | no | Rae5 | Rae5 | -2.63 | -3.49 |
| 145833178628 | 54 | 27... gxf6 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Bxd4 | Bxd4 | -10.23 | -M11 |
| 145833178628 | 57 | 29. Qf4 | good | best | precision | best | 0.0000 | 0.000 | no | Kd3 | Qh5 | -M6 | -M10 |
| 145833178628 | 58 | 29... Bxd4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Qb2+ | Rxd4+ | -9.14 | -M6 |
| 145833178628 | 59 | 30. Qxh6+ | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Qxh6+ | Qxd4 | -M4 | -M5 |
| 145833178628 | 60 | 30... Ke7 | excellent | best | precision | best | 0.0000 | 1.000 | no | Kg8 | Kg8 | -M4 | -M5 |
| 145833758308 | 6 | 3... Nc6 | best | excellent | precision | excellent | 0.0057 | 0.436 | no | Bc5 | - | +1.09 | +1.11 |
| 145833758308 | 8 | 4... Nge7 | inaccuracy | good | precision | good | 0.0372 | 0.459 | no | Qg6 | Qg6 | +1.37 | +1.35 |
| 145833758308 | 10 | 5... exd4 | inaccuracy | good | precision | good | 0.0429 | 0.424 | no | d6 | h6 | +2.28 | +2.09 |
| 145833758308 | 12 | 6... Nb4 | good | inaccuracy | precision | inaccuracy | 0.0638 | 0.383 | no | d6 | d6 | +3.03 | +3.27 |
| 145833758308 | 14 | 7... Ng6 | mistake | inaccuracy | precision | inaccuracy | 0.0865 | 0.422 | no | d5 | d5 | +2.90 | +2.95 |
| 145833758308 | 18 | 9... Nd3+ | miss | inaccuracy | precision | inaccuracy | 0.0930 | 0.562 | no | Nc2+ | Nc2+ | +0.71 | +0.53 |
| 145833758308 | 19 | 10. Bxd3 | great | best | precision | best | 0.0000 | 0.531 | yes | Bxd3 | - | +0.71 | +0.50 |
| 145833758308 | 24 | 12... Nf5 | good | excellent | precision | excellent | 0.0142 | 0.578 | no | h6 | h6 | -1.00 | -1.21 |
| 145833758308 | 25 | 13. Be3 | blunder | mistake | precision | mistake | 0.1995 | 0.430 | no | Nf3 | Nf3 | -4.82 | -5.19 |
| 145833758308 | 26 | 13... Nxe3 | great | best | precision | best | 0.0000 | 0.769 | yes | Nxe3 | - | -4.82 | -5.04 |
| 145833758308 | 33 | 17. Rd1 | good | excellent | precision | excellent | 0.0127 | 0.235 | no | Qc2 | g4 | -5.20 | -5.40 |
| 145833758308 | 34 | 17... O-O | best | excellent | precision | excellent | 0.0028 | 0.778 | no | b5 | - | -5.20 | -5.32 |
| 145833758308 | 36 | 18... Qf4+ | excellent | best | precision | best | 0.0000 | 0.811 | yes | Qf4+ | Qf5+ | -5.57 | -6.19 |
| 145833758308 | 37 | 19. Ke1 | good | excellent | precision | excellent | 0.0018 | 0.192 | no | Ke2 | Ke2 | -6.25 | -6.38 |
| 145833758308 | 39 | 20. Kf1 | best | excellent | precision | excellent | 0.0077 | 0.202 | no | Ne2 | - | -5.90 | -6.30 |
| 145833758308 | 41 | 21. Re1 | mistake | inaccuracy | precision | inaccuracy | 0.0673 | 0.218 | no | Nd5 | Nd5 | -6.48 | -7.46 |
| 145833758308 | 42 | 21... Qd3+ | excellent | good | precision | good | 0.0243 | 0.850 | no | Qf4+ | Qf4+ | -6.39 | -6.57 |
| 145833758308 | 44 | 22... Bh4+ | inaccuracy | good | precision | good | 0.0355 | 0.821 | no | Qf5+ | Qf5+ | -5.33 | -5.59 |
| 145833758308 | 46 | 23... Qf5+ | best | good | precision | good | 0.0319 | 0.795 | no | Bg4 | - | -5.33 | -5.04 |
| 145833758308 | 48 | 24... Qh3+ | best | excellent | precision | excellent | 0.0029 | 0.768 | no | Bd7 | - | -5.33 | -5.19 |
| 145833758308 | 49 | 25. Kh1 | excellent | best | precision | best | 0.0000 | 0.231 | yes | Kh1 | Kf2 | -5.53 | -5.71 |
| 145833758308 | 58 | 29... Rfxe8 | great | excellent | precision | excellent | 0.0029 | 0.769 | no | Raxe8 | - | -5.00 | -5.08 |
| 145833758308 | 60 | 30... Re1+ | great | excellent | precision | excellent | 0.0042 | 0.872 | no | Qe4+ | - | -7.75 | -7.89 |
| 145833758308 | 67 | 34. Qh4 | good | inaccuracy | precision | inaccuracy | 0.0650 | 0.137 | no | Qf3 | Qf3 | -8.75 | -11.05 |
| 145833758308 | 68 | 34... Qe6+ | good | inaccuracy | precision | inaccuracy | 0.0570 | 0.929 | no | Rae8 | Qf5+ | -7.60 | -8.25 |
| 145833758308 | 91 | 46. Rg4 | inaccuracy | mistake | precision | mistake | 0.1015 | 0.101 | no | Qg3 | Qg3 | -M4 | -M4 |
| 145833758308 | 96 | 48... Re8 | excellent | best | precision | best | 0.0000 | 0.887 | yes | Re8 | Rc8 | -7.45 | -8.81 |
| 145833758308 | 97 | 49. Kg5 | inaccuracy | mistake | precision | mistake | 0.1146 | 0.115 | no | Kf3 | Kf3 | -M4 | -M4 |
| 145833758308 | 103 | 52. h4 | excellent | good | precision | good | 0.0256 | 0.126 | no | Ke7 | Ke7 | -9.04 | -9.07 |
| 145833758308 | 107 | 54. Ke7 | best | excellent | precision | excellent | 0.0000 | 0.102 | no | Kg5 | - | -8.82 | -8.69 |
| 145833758308 | 111 | 56. Kd8 | excellent | best | precision | best | 0.0000 | 0.000 | no | Ke7 | Kd7 | -M6 | -M8 |
| 145833758308 | 114 | 57... h1=Q | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Rd2 | - | -M4 | -M6 |
| 146658193946 | 6 | 3... Bc5 | book | excellent | precision | excellent | 0.0195 | 0.506 | no | c6 | - | +0.21 | +0.24 |
| 146658193946 | 7 | 4. Nf3 | book | best | precision | best | 0.0000 | 0.514 | yes | Nf3 | - | +0.21 | +0.22 |
| 146658193946 | 12 | 6... c6 | inaccuracy | good | precision | good | 0.0345 | 0.460 | no | O-O | O-O | +1.35 | +1.31 |
| 146658193946 | 13 | 7. h3 | inaccuracy | good | precision | good | 0.0368 | 0.575 | no | Bg5 | Bg5 | +0.72 | +0.69 |
| 146658193946 | 17 | 9. exd5 | excellent | best | precision | best | 0.0000 | 0.562 | yes | exd5 | Bb3 | +0.50 | +0.75 |
| 146658193946 | 22 | 11... Nbd7 | mistake | inaccuracy | precision | inaccuracy | 0.0568 | 0.286 | no | Qe7 | Qe7 | +5.01 | +5.30 |
| 146658193946 | 24 | 12... Qa5 | inaccuracy | good | precision | good | 0.0284 | 0.235 | no | Qe7 | Qe7 | +6.05 | +5.86 |
| 146658193946 | 27 | 14. dxe4 | excellent | best | precision | best | 0.0000 | 0.808 | yes | dxe4 | Qh5+ | +5.91 | +5.98 |
| 146658193946 | 28 | 14... Nf6 | excellent | best | precision | best | 0.0000 | 0.202 | yes | Nf6 | g6 | +5.93 | +6.10 |
| 146658193946 | 50 | 25... Ng3 | excellent | best | precision | best | 0.0000 | 0.097 | yes | Ng3 | Rxd1 | +9.39 | +9.51 |
| 147234657424 | 5 | 3. Bc4 | book | good | precision | good | 0.0215 | 0.524 | no | Bb5 | - | +0.07 | +0.05 |
| 147234657424 | 6 | 3... e6 | book | excellent | precision | excellent | 0.0006 | 0.497 | no | Nf6 | - | +0.12 | +0.17 |
| 147234657424 | 11 | 6. exd5 | good | excellent | precision | excellent | 0.0102 | 0.423 | no | Bd3 | Bd3 | -1.59 | -1.53 |
| 147234657424 | 13 | 7. Nxf7 | mistake | inaccuracy | precision | inaccuracy | 0.0758 | 0.413 | no | Bd3 | Bd3 | -3.14 | -2.90 |
| 147234657424 | 16 | 8... Nf6 | great | best | precision | best | 0.0000 | 0.796 | yes | Nf6 | - | -5.79 | -5.72 |
| 147234657424 | 24 | 12... Rf8 | miss | inaccuracy | precision | inaccuracy | 0.0888 | 0.635 | no | cxd4 | cxd4 | -0.80 | -0.79 |
| 147234657424 | 27 | 14. Bxf6 | great | best | precision | best | 0.0000 | 0.455 | yes | Bxf6 | - | -0.80 | -0.72 |
| 147234657424 | 29 | 15. Qh5+ | mistake | blunder | precision | blunder | 0.2176 | 0.500 | no | Qb3+ | Qb3+ | -3.95 | -4.00 |
| 147234657424 | 36 | 18... Bxf2+ | best | excellent | precision | excellent | 0.0020 | 0.781 | no | Ne5 | - | -5.52 | -5.35 |
| 147234657424 | 40 | 20... Na5 | good | excellent | precision | excellent | 0.0121 | 0.783 | no | Qd2 | Qd2 | -4.99 | -5.20 |
| 147234657424 | 41 | 21. Qg4 | best | excellent | precision | excellent | 0.0097 | 0.229 | no | Qe2 | - | -4.99 | -5.30 |
| 147234657424 | 44 | 22... Qd8 | good | excellent | precision | excellent | 0.0195 | 0.778 | no | Qe5 | Nc6 | -4.26 | -4.90 |
| 147234657424 | 46 | 23... Qc8 | good | excellent | precision | excellent | 0.0185 | 0.781 | no | Qe7 | Nc6 | -4.01 | -5.00 |
| 147234657424 | 51 | 26. Nf7# | great | best | precision | best | 0.0000 | 1.000 | yes | Nf7# | - | - | # |
| 147295227566 | 5 | 3. exd5 | book | best | precision | best | 0.0000 | 0.520 | yes | exd5 | - | +0.25 | +0.24 |
| 147295227566 | 6 | 3... exd5 | book | best | precision | best | 0.0000 | 0.485 | yes | exd5 | - | +0.25 | +0.29 |
| 147295227566 | 14 | 7... Bd7 | miss | mistake | precision | mistake | 0.1094 | 0.493 | no | Bxc5 | Bxc5 | +2.01 | +1.94 |
| 147295227566 | 17 | 9. Re1+ | mistake | inaccuracy | precision | inaccuracy | 0.0946 | 0.617 | no | Nxd5 | Nxd5 | +0.47 | +0.37 |
| 147295227566 | 23 | 12. Ng5 | inaccuracy | good | precision | good | 0.0274 | 0.595 | no | c3 | c3 | +0.94 | +1.11 |
| 147295227566 | 24 | 12... a6 | mistake | inaccuracy | precision | inaccuracy | 0.0526 | 0.432 | no | h6 | h6 | +2.07 | +2.00 |
| 147295227566 | 25 | 13. Bxc6 | miss | mistake | precision | mistake | 0.1067 | 0.620 | no | Bd3 | Bd3 | +0.26 | +0.22 |
| 147295227566 | 27 | 14. Qd4 | inaccuracy | good | precision | good | 0.0407 | 0.566 | no | Qd3 | Qd3 | +0.43 | +0.41 |
| 147295227566 | 28 | 14... Bf6 | inaccuracy | good | precision | good | 0.0298 | 0.475 | no | h6 | h6 | +1.10 | +0.90 |
| 147295227566 | 36 | 18... Bg5 | miss | mistake | precision | mistake | 0.1054 | 0.507 | no | Bxb2 | Bxb2 | +1.64 | +1.62 |
| 147295227566 | 39 | 20. Rxd2 | excellent | best | precision | best | 0.0000 | 0.592 | yes | Rxd2 | Qxd2 | +1.49 | +1.54 |
| 147295227566 | 41 | 21. Rdd1 | mistake | inaccuracy | precision | inaccuracy | 0.0692 | 0.580 | no | Qxd8 | Qxd8 | +0.19 | +0.18 |
| 147295227566 | 42 | 21... Qxd4 | excellent | best | precision | best | 0.0000 | 0.489 | yes | Qxd4 | Qe7 | +0.34 | +0.24 |
| 147295227566 | 44 | 22... Bg6 | good | inaccuracy | precision | inaccuracy | 0.0702 | 0.482 | no | Reb8 | Reb8 | +1.03 | +1.46 |
| 147295227566 | 46 | 23... f5 | great | best | precision | best | 0.0000 | 0.628 | yes | f5 | - | -1.99 | -2.10 |
| 147295227566 | 49 | 25. Rxg6 | great | best | precision | best | 0.0000 | 0.522 | yes | Rxg6 | - | +0.46 | +0.34 |
| 147295227566 | 52 | 26... Rxe1+ | great | best | precision | best | 0.0000 | 0.774 | yes | Rxe1+ | - | -5.20 | -5.07 |
| 147295227566 | 55 | 28. Rxc6 | best | excellent | precision | excellent | 0.0038 | 0.222 | no | b3 | - | -4.96 | -5.04 |
| 147295227566 | 56 | 28... Rxa2 | best | excellent | precision | excellent | 0.0009 | 0.775 | no | Rb8 | - | -4.96 | -4.97 |
| 147295227566 | 57 | 29. b3 | good | best | precision | best | 0.0000 | 0.228 | yes | b3 | Rb6 | -5.46 | -4.97 |
| 147295227566 | 58 | 29... Rb2 | good | excellent | precision | excellent | 0.0110 | 0.772 | no | Kh8 | a4 | -4.92 | -4.72 |
| 147295227566 | 61 | 31. Kg3 | good | excellent | precision | excellent | 0.0159 | 0.244 | no | Rc5 | f4 | -5.35 | -4.98 |
| 147295227566 | 62 | 31... h5 | good | best | precision | best | 0.0000 | 0.772 | yes | h5 | Rb1 | -4.89 | -4.99 |
| 147295227566 | 64 | 32... g6 | best | excellent | precision | excellent | 0.0000 | 0.771 | no | Rb1 | - | -5.05 | -5.02 |
| 147295227566 | 65 | 33. Kg5 | excellent | best | precision | best | 0.0000 | 0.226 | yes | Kg5 | Kg3 | -5.24 | -5.05 |
| 147295227566 | 66 | 33... Rb1 | inaccuracy | good | precision | good | 0.0495 | 0.775 | no | Ra7 | Ra7 | -4.10 | -3.97 |
| 147295227566 | 68 | 34... Kg8 | best | excellent | precision | excellent | 0.0081 | 0.739 | no | Kh8 | - | -4.10 | -4.13 |
| 147295227566 | 72 | 36... Rf8 | excellent | good | precision | good | 0.0362 | 0.759 | no | Rg2 | Rg2 | -3.91 | -3.91 |
| 147295227566 | 73 | 37. Rc3 | inaccuracy | mistake | precision | mistake | 0.1596 | 0.277 | no | Ra7 | Ra7 | -5.25 | -8.22 |
| 147295227566 | 77 | 39. Rc3 | mistake | blunder | precision | blunder | 0.2017 | 0.202 | no | Rc5 | Rc5 | -M1 | -M1 |
| 147295227566 | 78 | 39... Rf5# | great | best | precision | best | 0.0000 | 1.000 | yes | Rf5# | - | - | -# |
| 147547838342 | 10 | 5... O-O | book | excellent | precision | excellent | 0.0029 | 0.484 | no | d6 | - | +0.24 | +0.26 |
| 147547838342 | 11 | 6. b4 | book | excellent | precision | excellent | 0.0143 | 0.519 | no | O-O | - | 0.00 | +0.06 |
| 147547838342 | 12 | 6... Bb6 | book | good | precision | good | 0.0201 | 0.496 | no | Be7 | - | +0.39 | +0.34 |
| 147547838342 | 15 | 8. Nxe5 | inaccuracy | good | precision | good | 0.0426 | 0.419 | no | Bb3 | Bb3 | -2.09 | -1.76 |
| 147547838342 | 16 | 8... Nxc4 | mistake | inaccuracy | precision | inaccuracy | 0.0964 | 0.624 | no | d6 | Qe7 | -0.30 | -0.38 |
| 147547838342 | 19 | 10. Nxb6 | great | best | precision | best | 0.0000 | 0.479 | yes | Nxb6 | - | -0.30 | -0.08 |
| 147547838342 | 22 | 11... Re8+ | best | excellent | precision | excellent | 0.0007 | 0.645 | no | Bg4 | - | -2.44 | -2.42 |
| 147547838342 | 24 | 12... Bg4 | mistake | inaccuracy | precision | inaccuracy | 0.0874 | 0.657 | no | Nxd5 | Nxd5 | -1.03 | -0.98 |
| 147547838342 | 25 | 13. Qd2 | great | best | precision | best | 0.0000 | 0.430 | yes | Qd2 | - | -1.03 | -0.99 |
| 147547838342 | 37 | 19. Kg2 | excellent | best | precision | best | 0.0000 | 0.000 | no | Kf2 | Kf2 | -M6 | -M7 |
| 147619991314 | 7 | 4. Bc4 | book | excellent | precision | excellent | 0.0130 | 0.548 | no | d4 | - | +0.58 | +0.54 |
| 147619991314 | 15 | 8. Re1 | best | excellent | precision | excellent | 0.0037 | 0.521 | no | Nh4 | - | +0.28 | +0.28 |
| 147619991314 | 17 | 9. Bd2 | excellent | best | precision | best | 0.0000 | 0.514 | no | Ne2 | h3 | +0.20 | +0.23 |
| 147619991314 | 22 | 11... Ng4 | excellent | best | precision | best | 0.0000 | 0.511 | yes | Ng4 | Nd7 | +0.05 | -0.13 |
| 147619991314 | 25 | 13. Bf4 | good | excellent | precision | excellent | 0.0156 | 0.417 | no | Bf1 | Bf1 | -1.70 | -1.61 |
| 147619991314 | 26 | 13... Bd6 | great | best | precision | best | 0.0000 | 0.599 | yes | Bd6 | - | -1.70 | -1.85 |
| 147619991314 | 28 | 14... Nf3+ | brilliant | good | precision | good | 0.0314 | 0.624 | no | O-O-O | - | -1.62 | -1.51 |
| 147619991314 | 30 | 15... Bxf4 | great | best | precision | best | 0.0000 | 0.595 | yes | Bxf4 | - | -1.62 | -1.55 |
| 147619991314 | 32 | 16... O-O | inaccuracy | good | precision | good | 0.0496 | 0.660 | no | Bxh2+ | Bxh2+ | -1.80 | -1.86 |
| 147619991314 | 41 | 21. Rd7 | excellent | best | precision | best | 0.0000 | 0.389 | yes | Rd7 | g4 | -1.79 | -1.84 |
| 147619991314 | 48 | 24... Bxa7 | great | excellent | precision | excellent | 0.0117 | 0.811 | no | Bxe4 | - | -5.70 | -5.84 |
| 147619991314 | 49 | 25. Nd6 | excellent | best | precision | best | 0.0000 | 0.189 | yes | Nd6 | Bc4 | -5.76 | -5.77 |
| 147619991314 | 50 | 25... Qa6+ | excellent | best | precision | best | 0.0000 | 0.808 | no | Qb8 | Qb8 | -5.49 | -5.86 |
| 147619991314 | 52 | 26... Rd8 | inaccuracy | good | precision | good | 0.0361 | 0.819 | no | Qa3 | Qa5 | -4.12 | -5.14 |
| 147619991314 | 53 | 27. Bc4 | mistake | good | precision | good | 0.0376 | 0.218 | no | Nxf7 | Nxf7 | -6.08 | -6.09 |
| 147619991314 | 56 | 28... exf5 | best | excellent | precision | excellent | 0.0054 | 0.794 | no | Qxf2+ | - | -5.38 | -5.48 |
| 147619991314 | 61 | 31. Kh2 | best | good | precision | good | 0.0228 | 0.199 | no | Bf1 | - | -5.61 | -6.14 |
| 147619991314 | 65 | 33. Kh3 | mistake | blunder | precision | blunder | 0.2154 | 0.215 | no | g3 | g3 | -M2 | -M2 |
| 147619991314 | 66 | 33... Qh1+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qh1+ | - | -M1 | -M1 |
| 147742438276 | 12 | 6... Bd6 | good | excellent | precision | excellent | 0.0146 | 0.385 | no | Ne7 | Ne7 | +2.04 | +1.88 |
| 147742438276 | 13 | 7. Bc4 | good | excellent | precision | excellent | 0.0173 | 0.629 | no | f4 | f4 | +1.71 | +1.62 |
| 147742438276 | 20 | 10... d6 | excellent | good | precision | good | 0.0260 | 0.120 | no | Rf8 | d5 | +7.09 | +7.36 |
| 147742438276 | 26 | 13... Rf8 | mistake | excellent | precision | excellent | 0.0117 | 0.121 | no | Kc6 | Kc6 | +7.30 | +7.71 |
| 147742438276 | 28 | 14... Kc7 | mistake | good | precision | good | 0.0253 | 0.115 | no | Rg8 | Rg8 | +7.97 | +8.21 |
| 147786569400 | 5 | 3. e3 | book | best | precision | best | 0.0000 | 0.525 | yes | e3 | - | +0.43 | +0.44 |
| 147786569400 | 6 | 3... Bf5 | book | excellent | precision | excellent | 0.0019 | 0.472 | no | Nf6 | - | +0.43 | +0.39 |
| 147786569400 | 8 | 4... Nf6 | excellent | best | precision | best | 0.0000 | 0.480 | yes | Nf6 | e6 | +0.31 | +0.30 |
| 147786569400 | 10 | 5... e6 | best | excellent | precision | excellent | 0.0006 | 0.487 | no | Qb6 | - | +0.12 | +0.20 |
| 147786569400 | 14 | 7... Bd6 | inaccuracy | good | precision | good | 0.0378 | 0.439 | no | h5 | h5 | +1.61 | +1.55 |
| 147786569400 | 18 | 9... Be4 | mistake | inaccuracy | precision | inaccuracy | 0.0588 | 0.396 | no | Nxg4 | Nxg4 | +2.76 | +2.61 |
| 147786569400 | 19 | 10. f3 | great | best | precision | best | 0.0000 | 0.663 | yes | f3 | - | +2.76 | +2.70 |
| 147786569400 | 26 | 13... cxd4 | excellent | best | precision | best | 0.0000 | 0.229 | yes | cxd4 | Bxe5 | +4.81 | +4.96 |
| 147786569400 | 27 | 14. Bd3 | excellent | best | precision | best | 0.0000 | 0.783 | yes | Bd3 | exd4 | +4.67 | +4.69 |
| 147786569400 | 28 | 14... f5 | best | good | precision | good | 0.0237 | 0.229 | no | g6 | - | +4.67 | +5.20 |
| 147786569400 | 29 | 15. Qxb7 | good | inaccuracy | precision | inaccuracy | 0.0662 | 0.794 | no | gxf5 | gxf5 | +3.63 | +3.72 |
| 147786569400 | 34 | 17... fxg4 | mistake | inaccuracy | precision | inaccuracy | 0.0760 | 0.261 | no | Rb8 | Rb8 | +5.68 | +5.74 |
| 147786569400 | 36 | 18... a5 | mistake | inaccuracy | precision | inaccuracy | 0.0884 | 0.221 | no | Nf6 | Nf6 | +7.15 | +7.26 |
| 147786569400 | 37 | 19. Rdg1 | miss | inaccuracy | precision | inaccuracy | 0.0624 | 0.868 | no | Qe4 | Qe4 | +4.72 | +5.48 |
| 147786569400 | 39 | 20. Bxf6 | miss | inaccuracy | precision | inaccuracy | 0.0997 | 0.868 | no | Rxg4 | Rxg4 | +4.63 | +4.67 |
| 147786569400 | 41 | 21. Qxg7# | great | best | precision | best | 0.0000 | 1.000 | yes | Qxg7# | - | - | # |
| 147991742972 | 10 | 5... Neg4 | mistake | inaccuracy | precision | inaccuracy | 0.0847 | 0.672 | no | Nc6 | Nc6 | -1.34 | -1.37 |
| 147991742972 | 11 | 6. h3 | inaccuracy | good | precision | good | 0.0457 | 0.411 | no | e5 | e5 | -2.33 | -2.28 |
| 147991742972 | 13 | 7. Kxf2 | great | best | precision | best | 0.0000 | 0.607 | yes | Kxf2 | - | +1.80 | +1.65 |
| 147991742972 | 18 | 9... Qe7 | inaccuracy | good | precision | good | 0.0477 | 0.430 | no | Nd5 | Nd5 | +1.88 | +1.81 |
| 147991742972 | 32 | 16... f5 | good | inaccuracy | precision | inaccuracy | 0.0564 | 0.493 | no | g6 | Qc5 | +0.98 | +0.96 |
| 147991742972 | 41 | 21. g3 | great | best | precision | best | 0.0000 | 0.628 | yes | g3 | - | +1.84 | +2.03 |
| 147991742972 | 45 | 23. Qxb8+ | great | best | precision | best | 0.0000 | 0.771 | yes | Qxb8+ | - | +5.00 | +5.64 |
| 147991742972 | 48 | 24... Qc5+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qc5+ | - | -M1 | -M1 |
| 148014224206 | 8 | 4... Nf6 | book | best | precision | best | 0.0000 | 0.480 | no | Nc6 | - | +0.29 | +0.32 |
| 148014224206 | 9 | 5. Nc3 | excellent | good | precision | good | 0.0219 | 0.522 | no | c3 | c3 | 0.00 | +0.00 |
| 148014224206 | 17 | 9. Be3 | excellent | good | precision | good | 0.0328 | 0.531 | no | Re1 | Re1 | +0.08 | -0.03 |
| 148014224206 | 20 | 10... Bb4 | good | excellent | precision | excellent | 0.0198 | 0.499 | no | Bd6 | Qc7 | +0.36 | +0.31 |
| 148014224206 | 21 | 11. Nxd7 | best | excellent | precision | excellent | 0.0014 | 0.521 | no | Ne2 | - | +0.36 | +0.30 |
| 148014224206 | 23 | 12. Qg4 | best | excellent | precision | excellent | 0.0014 | 0.517 | no | Ne2 | - | +0.36 | +0.29 |
| 148014224206 | 26 | 13... Nf6 | miss | mistake | precision | mistake | 0.1763 | 0.560 | no | Qxd4 | Qxd4 | +1.86 | +1.73 |
| 148014224206 | 29 | 15. Rfe1 | inaccuracy | excellent | precision | excellent | 0.0136 | 0.624 | no | Nxd5 | Nxd5 | +1.29 | +1.74 |
| 148014224206 | 31 | 16. Nxd5 | mistake | blunder | precision | blunder | 0.2111 | 0.609 | no | Rad1 | Rad1 | -0.91 | -1.52 |
| 148014224206 | 32 | 16... Bxe1 | great | best | precision | best | 0.0000 | 0.603 | yes | Bxe1 | - | -0.91 | -1.34 |
| 148014224206 | 44 | 22... Qxf2+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qxf2+ | - | -M1 | -M1 |
| 148014224206 | 46 | 23... Qf1# | great | best | precision | best | 0.0000 | 1.000 | yes | Qf1# | - | - | -# |
| 148224127998 | 5 | 3. Bf4 | book | best | precision | best | 0.0000 | 0.526 | yes | Bf4 | - | +0.38 | +0.32 |
| 148224127998 | 6 | 3... Bf5 | book | best | precision | best | 0.0000 | 0.481 | yes | Bf5 | - | +0.46 | +0.36 |
| 148224127998 | 7 | 4. e3 | book | excellent | precision | excellent | 0.0077 | 0.521 | no | c4 | - | +0.25 | +0.24 |
| 148224127998 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0071 | 0.486 | no | e6 | - | +0.41 | +0.37 |
| 148224127998 | 9 | 5. c4 | book | best | precision | best | 0.0000 | 0.522 | yes | c4 | - | +0.41 | +0.45 |
| 148224127998 | 10 | 5... Qa5+ | good | excellent | precision | excellent | 0.0160 | 0.473 | no | Qb6 | Qb6 | +0.81 | +0.72 |
| 148224127998 | 11 | 6. Nc3 | excellent | best | precision | best | 0.0000 | 0.543 | no | Nfd2 | Nbd2 | +0.78 | +0.84 |
| 148224127998 | 12 | 6... dxc4 | good | excellent | precision | excellent | 0.0193 | 0.450 | no | Qb6 | Qb6 | +1.13 | +1.17 |
| 148224127998 | 13 | 7. Bxc4 | good | excellent | precision | excellent | 0.0099 | 0.569 | no | Nd2 | Ne5 | +0.89 | +1.02 |
| 148224127998 | 18 | 9... Qxc3+ | great | best | precision | best | 0.0000 | 0.526 | yes | Qxc3+ | - | -0.24 | -0.50 |
| 148224127998 | 19 | 10. Nd2 | great | best | precision | best | 0.0000 | 0.470 | yes | Nd2 | - | -0.24 | -0.37 |
| 148224127998 | 22 | 11... Qxa3 | great | best | precision | best | 0.0000 | 0.500 | yes | Qxa3 | - | 0.00 | +0.00 |
| 148224127998 | 25 | 13. Qd2 | excellent | best | precision | best | 0.0000 | 0.411 | yes | Qd2 | Nd2 | -1.56 | -1.54 |
| 148224127998 | 26 | 13... Qxd2+ | great | best | precision | best | 0.0000 | 0.591 | yes | Qxd2+ | - | -1.56 | -1.34 |
| 148224127998 | 46 | 23... Na5 | blunder | mistake | precision | mistake | 0.1819 | 0.718 | no | Rd7 | h6 | -0.54 | -0.60 |
| 148224127998 | 54 | 27... Ne7 | great | best | precision | best | 0.0000 | 0.741 | yes | Ne7 | - | -4.23 | -4.09 |
| 148224127998 | 55 | 28. Rc7 | mistake | inaccuracy | precision | inaccuracy | 0.0663 | 0.274 | no | Bd2 | Bd2 | -5.05 | -5.62 |
| 164007452224 | 8 | 4... Nf6 | excellent | good | precision | good | 0.0257 | 0.478 | no | Bc5 | Bc5 | +0.53 | +0.68 |
| 164007452224 | 22 | 11... d5 | miss | mistake | precision | mistake | 0.1050 | 0.505 | no | Nxe4 | Nxe4 | +1.64 | +1.73 |
| 164007452224 | 28 | 14... Qd6 | good | excellent | precision | excellent | 0.0087 | 0.440 | no | Qg5 | Qg5 | +1.28 | +1.27 |
| 164007452224 | 30 | 15... Qxc5 | great | best | precision | best | 0.0000 | 0.744 | yes | Qxc5 | - | -4.43 | -4.29 |
| 164007452224 | 31 | 16. Re4 | excellent | good | precision | good | 0.0241 | 0.267 | no | Bf1 | Bb3 | -4.57 | -4.83 |
| 164007452224 | 33 | 17. b4 | excellent | best | precision | best | 0.0000 | 0.251 | yes | b4 | Rae1 | -4.61 | -4.70 |
| 164007452224 | 36 | 18... Be6 | best | excellent | precision | excellent | 0.0026 | 0.754 | no | Re8 | - | -4.80 | -4.69 |
| 164007452224 | 37 | 19. Bxe6 | best | excellent | precision | excellent | 0.0026 | 0.249 | no | Bf1 | - | -4.80 | -4.74 |
| 164007452224 | 39 | 20. Rad1 | best | excellent | precision | excellent | 0.0022 | 0.251 | no | Re1 | - | -4.80 | -4.75 |
| 164007452224 | 40 | 20... Nd5 | excellent | best | precision | best | 0.0000 | 0.753 | yes | Nd5 | e5 | -4.69 | -4.63 |
| 164007452224 | 42 | 21... Rxf3 | great | best | precision | best | 0.0000 | 0.841 | yes | Rxf3 | - | - | -7.34 |
| 164008171476 | 5 | 3. Nf3 | book | excellent | precision | excellent | 0.0012 | 0.523 | no | e3 | - | +0.38 | +0.32 |
| 164008171476 | 6 | 3... Bf5 | book | best | precision | best | 0.0000 | 0.481 | yes | Bf5 | - | +0.46 | +0.36 |
| 164008171476 | 7 | 4. e3 | book | excellent | precision | excellent | 0.0076 | 0.521 | no | c4 | - | +0.25 | +0.24 |
| 164008171476 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0071 | 0.486 | no | e6 | - | +0.41 | +0.37 |
| 164008171476 | 9 | 5. c4 | book | best | precision | best | 0.0000 | 0.522 | yes | c4 | - | +0.41 | +0.45 |
| 164008171476 | 10 | 5... e6 | book | excellent | precision | excellent | 0.0059 | 0.474 | no | Qb6 | - | +0.52 | +0.49 |
| 164008171476 | 18 | 9... O-O | excellent | best | precision | best | 0.0000 | 0.443 | yes | O-O | Be7 | +1.07 | +1.11 |
| 164008171476 | 19 | 10. h3 | good | excellent | precision | excellent | 0.0075 | 0.565 | no | Be2 | Be2 | +0.83 | +0.84 |
| 164008171476 | 20 | 10... h5 | inaccuracy | good | precision | good | 0.0433 | 0.451 | no | Nbd7 | Nbd7 | +1.61 | +1.59 |
| 164008171476 | 24 | 12... Bd6 | good | excellent | precision | excellent | 0.0058 | 0.433 | no | Be7 | Be7 | +1.29 | +1.30 |
| 164008171476 | 27 | 14. Nd2 | miss | inaccuracy | precision | inaccuracy | 0.0964 | 0.632 | no | Nxc6 | Nxc6 | +0.69 | +0.61 |
| 164008171476 | 28 | 14... Nxe5 | blunder | mistake | precision | mistake | 0.1628 | 0.464 | no | Bc7 | Bc7 | +3.54 | +3.57 |
| 164008171476 | 36 | 18... Qc5 | inaccuracy | good | precision | good | 0.0444 | 0.322 | no | Qxf4 | Qxf4 | +4.25 | +4.07 |
| 164008171476 | 38 | 19... Rad8 | excellent | best | precision | best | 0.0000 | 0.287 | yes | Rad8 | a5 | +4.19 | +4.27 |
| 164008171476 | 40 | 20... f6 | good | inaccuracy | precision | inaccuracy | 0.0555 | 0.278 | no | Rd4 | Rd4 | +4.97 | +5.32 |
| 164008171476 | 41 | 21. Rac1 | brilliant | excellent | precision | excellent | 0.0062 | 0.778 | no | Ng6 | - | +4.97 | +5.44 |
| 164008171476 | 43 | 22. Bxe6+ | mistake | inaccuracy | precision | inaccuracy | 0.0931 | 0.774 | no | Ng6 | Qxf5 | +2.30 | +3.22 |
| 164188880582 | 9 | 5. Bg5 | book | excellent | precision | excellent | 0.0133 | 0.514 | no | Bd3 | - | -0.06 | +0.02 |
| 164188880582 | 11 | 6. Nc3 | best | excellent | precision | excellent | 0.0060 | 0.501 | no | Be2 | - | -0.06 | -0.16 |
| 164188880582 | 17 | 9. Be2 | excellent | best | precision | best | 0.0000 | 0.588 | no | Qe2 | Qe2 | +1.13 | +1.26 |
| 164188880582 | 18 | 9... Bg4 | inaccuracy | good | precision | good | 0.0389 | 0.425 | no | Qb4+ | Qb4+ | +1.87 | +1.93 |
| 164188880582 | 20 | 10... Bxf3 | inaccuracy | good | precision | good | 0.0499 | 0.385 | no | Re8 | h6 | +2.78 | +2.85 |
| 164188880582 | 26 | 13... Nxd4 | great | best | precision | best | 0.0000 | 0.490 | yes | Nxd4 | - | +0.20 | +0.11 |
| 164188880582 | 27 | 14. Qc1 | mistake | inaccuracy | precision | inaccuracy | 0.0920 | 0.507 | no | Re1 | Re1 | -1.45 | -1.43 |
| 164188880582 | 30 | 15... Rfe8 | good | excellent | precision | excellent | 0.0187 | 0.596 | no | Qe2 | Qe2 | -1.23 | -1.19 |
| 164188880582 | 34 | 17... Rd4 | best | excellent | precision | excellent | 0.0023 | 0.598 | no | Qe6 | - | -1.57 | -1.83 |
| 164188880582 | 39 | 20. Rxe8+ | great | best | precision | best | 0.0000 | 0.777 | yes | Rxe8+ | - | +5.05 | +5.42 |
| 164188880582 | 41 | 21. Qe3 | best | excellent | precision | excellent | 0.0052 | 0.794 | no | Kh1 | - | +5.05 | +5.45 |
| 164188880582 | 43 | 22. Qxc5 | great | best | precision | best | 0.0000 | 0.963 | yes | Qxc5 | - | - | M9 |
| 164462806840 | 5 | 3. Bc4 | book | excellent | precision | excellent | 0.0112 | 0.523 | no | d4 | - | +0.20 | +0.20 |
| 164462806840 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.488 | yes | Nf6 | - | +0.20 | +0.17 |
| 164462806840 | 7 | 4. Nc3 | book | best | precision | best | 0.0000 | 0.510 | yes | Nc3 | - | +0.20 | +0.16 |
| 164462806840 | 12 | 6... Bxf3 | inaccuracy | good | precision | good | 0.0406 | 0.464 | no | Be7 | Be7 | +1.30 | +1.31 |
| 164462806840 | 16 | 8... O-O | excellent | best | precision | best | 0.0000 | 0.426 | yes | O-O | Nc6 | +1.32 | +1.27 |
| 164462806840 | 17 | 9. Nxe7+ | best | excellent | precision | excellent | 0.0000 | 0.574 | no | Ne3 | - | +1.32 | +1.43 |
| 164462806840 | 20 | 10... h6 | best | excellent | precision | excellent | 0.0086 | 0.433 | no | Nc6 | - | +1.32 | +1.25 |
| 164462806840 | 21 | 11. Bh4 | inaccuracy | good | precision | good | 0.0483 | 0.573 | no | Bxf6 | Bxf6 | +0.49 | +0.42 |
| 164462806840 | 24 | 12... Nb6 | good | excellent | precision | excellent | 0.0193 | 0.471 | no | g5 | g6 | +0.88 | +0.83 |
| 164462806840 | 25 | 13. Bb3 | excellent | best | precision | best | 0.0000 | 0.549 | yes | Bb3 | Bxf6 | +0.83 | +0.79 |
| 164462806840 | 26 | 13... Nbd7 | best | excellent | precision | excellent | 0.0012 | 0.454 | no | g5 | - | +0.83 | +0.91 |
| 164462806840 | 27 | 14. d4 | good | inaccuracy | precision | inaccuracy | 0.0556 | 0.553 | no | Qf5 | Qf5 | +0.06 | -0.04 |
| 164462806840 | 30 | 15... dxe5 | excellent | best | precision | best | 0.0000 | 0.422 | yes | dxe5 | Nxe5 | +1.40 | +1.42 |
| 164462806840 | 33 | 17. Bd5 | inaccuracy | good | precision | good | 0.0460 | 0.593 | no | Bc4 | a4 | +0.88 | +0.81 |
| 164462806840 | 40 | 20... Kh8 | inaccuracy | good | precision | good | 0.0444 | 0.238 | no | Kg7 | Nxd5 | - | +6.07 |
| 164784324724 | 13 | 7. Nc3 | mistake | inaccuracy | precision | inaccuracy | 0.0788 | 0.482 | no | c3 | c3 | -1.69 | -1.44 |
| 164784324724 | 14 | 7... h6 | miss | inaccuracy | precision | inaccuracy | 0.0741 | 0.596 | no | Bg4 | Bg4 | -0.30 | -0.36 |
| 164784324724 | 21 | 11. h3 | best | excellent | precision | excellent | 0.0020 | 0.497 | no | Be3 | - | +0.01 | +0.01 |
| 164784324724 | 24 | 12... Bxe3 | best | excellent | precision | excellent | 0.0007 | 0.501 | no | Bb6 | - | -0.17 | +0.01 |
| 164784324724 | 26 | 13... c6 | excellent | best | precision | best | 0.0000 | 0.517 | yes | c6 | Bxf3 | -0.11 | -0.11 |
| 164784324724 | 28 | 14... d5 | excellent | best | precision | best | 0.0000 | 0.516 | yes | d5 | Re8 | -0.08 | -0.05 |
| 164784324724 | 30 | 15... cxd5 | excellent | best | precision | best | 0.0000 | 0.509 | yes | cxd5 | Bxf3 | +0.06 | -0.14 |
| 164784324724 | 33 | 17. Nxe5 | great | best | precision | best | 0.0000 | 0.625 | yes | Nxe5 | - | +1.77 | +1.70 |
| 164784324724 | 35 | 18. d4 | best | good | precision | good | 0.0270 | 0.629 | no | f4 | - | +1.77 | +1.61 |
| 164784324724 | 37 | 19. Qxg5 | great | best | precision | best | 0.0000 | 0.794 | yes | Qxg5 | - | +4.96 | +4.97 |
| 164784324724 | 43 | 22. Ra2 | inaccuracy | good | precision | good | 0.0415 | 0.824 | no | Bd1 | Bd1 | +4.57 | +4.71 |
| 164784324724 | 44 | 22... f5 | inaccuracy | good | precision | good | 0.0286 | 0.218 | no | Rd8 | Rd8 | +5.53 | +5.36 |
| 164784324724 | 45 | 23. Bxd5+ | inaccuracy | good | precision | good | 0.0235 | 0.811 | no | Bd1 | Bd1 | +4.53 | +4.82 |
| 164784324724 | 52 | 26... Kh7 | excellent | best | precision | best | 0.0000 | 0.189 | yes | Kh7 | Bxf7 | +5.23 | +5.32 |
| 164784324724 | 53 | 27. Ng5+ | best | excellent | precision | excellent | 0.0077 | 0.809 | no | Ne5 | - | +5.23 | +5.14 |
| 164784324724 | 56 | 28... Kh7 | good | excellent | precision | excellent | 0.0198 | 0.208 | no | Bxf7 | Bxf7 | +5.22 | +5.28 |
| 164784324724 | 61 | 31. Bd5 | best | excellent | precision | excellent | 0.0075 | 0.827 | no | Ba6 | - | +5.29 | +5.62 |
| 164784324724 | 63 | 32. f3 | inaccuracy | good | precision | good | 0.0415 | 0.853 | no | fxg3 | fxg3 | +4.95 | +5.38 |
| 164784324724 | 65 | 33. b4 | good | excellent | precision | excellent | 0.0099 | 0.843 | no | Ne4 | Ne4 | +5.62 | +5.93 |
| 164784324724 | 68 | 34... Rxf1+ | good | excellent | precision | excellent | 0.0000 | 0.169 | no | Bg6 | R1e3 | +6.08 | +5.68 |
| 164784324724 | 69 | 35. Bxf1 | best | excellent | precision | excellent | 0.0004 | 0.824 | no | Kxf1 | - | +6.08 | +6.65 |
| 164784324724 | 70 | 35... Re1 | excellent | best | precision | best | 0.0000 | 0.141 | no | Re3 | Bg6 | +6.32 | +6.65 |
| 164784324724 | 72 | 36... Ra1 | excellent | best | precision | best | 0.0000 | 0.161 | yes | Ra1 | Rc1 | +6.04 | +6.40 |
| 164784324724 | 73 | 37. Ne4 | best | excellent | precision | excellent | 0.0088 | 0.850 | no | d5 | - | +6.04 | +6.03 |
| 164784324724 | 76 | 38... Rxc3 | mistake | good | precision | good | 0.0360 | 0.164 | no | Bf7 | Bf7 | +6.87 | +7.08 |
| 164784324724 | 79 | 40. d5 | excellent | best | precision | best | 0.0000 | 0.878 | yes | d5 | Rd2 | +6.78 | +7.17 |
| 164784324724 | 84 | 42... axb4 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | a4 | Kh7 | M7 | M9 |
| 164784324724 | 86 | 43... Kg8 | inaccuracy | best | precision | best | 0.0000 | 0.000 | yes | Kg8 | Kh7 | M9 | M12 |
| 164784324724 | 90 | 45... Ke8 | excellent | best | precision | best | 0.0000 | 0.070 | yes | Ke8 | g5 | +8.07 | +9.98 |
| 164784324724 | 91 | 46. Be6 | excellent | good | precision | good | 0.0220 | 0.937 | no | Bb5+ | Bb5+ | +7.64 | +11.22 |
| 164784324724 | 93 | 47. Nd5 | best | excellent | precision | excellent | 0.0000 | 1.000 | no | Kf2 | - | M8 | M17 |
| 164812402934 | 10 | 5... d6 | good | excellent | precision | excellent | 0.0106 | 0.516 | no | Nd4 | Nd4 | +0.07 | +0.23 |
| 164812402934 | 21 | 11. d5 | mistake | inaccuracy | precision | inaccuracy | 0.0750 | 0.583 | no | Nd5 | Nd5 | +0.08 | +0.14 |
| 164812402934 | 25 | 13. Bxc4 | great | best | precision | best | 0.0000 | 0.711 | yes | Bxc4 | - | +3.51 | +3.69 |
| 164812402934 | 26 | 13... Re8 | good | excellent | precision | excellent | 0.0168 | 0.296 | no | a5 | g5 | +4.21 | +4.04 |
| 164812402934 | 34 | 17... Ba7 | best | excellent | precision | excellent | 0.0036 | 0.256 | no | axb4 | - | +4.51 | +4.86 |
| 164812402934 | 35 | 18. Bb5 | excellent | good | precision | good | 0.0236 | 0.758 | no | b5 | b5 | +4.34 | +4.33 |
| 164812402934 | 36 | 18... Be6 | mistake | good | precision | good | 0.0437 | 0.265 | no | Re6 | Rxe4 | +5.37 | +5.34 |
| 165327199736 | 16 | 8... a6 | best | excellent | precision | excellent | 0.0007 | 0.517 | no | h5 | - | -0.32 | -0.33 |
| 165327199736 | 19 | 10. Bb3 | inaccuracy | mistake | precision | mistake | 0.1029 | 0.527 | no | Nxb5 | Nxb5 | -0.99 | -1.04 |
| 165327199736 | 23 | 12. Bf4 | excellent | best | precision | best | 0.0000 | 0.426 | yes | Bf4 | Kh1 | -1.08 | -1.15 |
| 165327199736 | 28 | 14... Nxb3 | good | excellent | precision | excellent | 0.0170 | 0.493 | no | O-O | O-O | +0.42 | +0.41 |
| 165327199736 | 31 | 16. Nxb5 | excellent | best | precision | best | 0.0000 | 0.535 | yes | Nxb5 | Rxa8 | +0.25 | +0.46 |
| 165327199736 | 33 | 17. Rxa8 | best | excellent | precision | excellent | 0.0027 | 0.533 | no | Nd4 | - | +0.49 | +0.34 |
| 165327199736 | 36 | 18... Qb7 | great | excellent | precision | excellent | 0.0076 | 0.757 | no | Qb8 | - | -4.09 | -3.95 |
| 165327199736 | 40 | 20... Bxc2 | great | best | precision | best | 0.0000 | 0.877 | yes | Bxc2 | - | - | -7.09 |
| 165401252676 | 11 | 6. Bd3 | book | excellent | precision | excellent | 0.0018 | 0.509 | no | Nc3 | - | +0.10 | +0.18 |
| 165401252676 | 12 | 6... d5 | book | best | precision | best | 0.0000 | 0.489 | yes | d5 | - | +0.10 | +0.12 |
| 165401252676 | 17 | 9. Qe2 | good | excellent | precision | excellent | 0.0153 | 0.515 | no | Bxe4 | Bxe4 | -0.29 | -0.11 |
| 165401252676 | 19 | 10. Bxe4 | miss | inaccuracy | precision | inaccuracy | 0.0777 | 0.633 | no | Qxe4+ | Qxe4+ | +0.76 | +0.88 |
| 165401252676 | 20 | 10... O-O | great | best | precision | best | 0.0000 | 0.448 | yes | O-O | - | +0.76 | +0.83 |
| 165401252676 | 25 | 13. Bxc6 | great | best | precision | best | 0.0000 | 0.677 | yes | Bxc6 | - | +3.01 | +2.89 |
| 165401252676 | 29 | 15. b3 | mistake | blunder | precision | blunder | 0.3985 | 0.665 | no | Be3 | Be3 | -0.90 | -4.29 |
| 165401252676 | 32 | 16... Rg6 | great | best | precision | best | 0.0000 | 1.000 | yes | Rg6 | - | -M4 | -M4 |
| 165401252676 | 33 | 17. g3 | mistake | excellent | precision | excellent | 0.0000 | 0.000 | no | Qg4 | Qg4 | -M3 | -M3 |
| 165450446440 | 5 | 3. e3 | book | best | precision | best | 0.0000 | 0.523 | yes | e3 | - | +0.43 | +0.44 |
| 165450446440 | 6 | 3... Bf5 | book | excellent | precision | excellent | 0.0018 | 0.474 | no | Nf6 | - | +0.43 | +0.39 |
| 165450446440 | 11 | 6. f3 | inaccuracy | good | precision | good | 0.0414 | 0.592 | no | Nd2 | c3 | +0.99 | +0.86 |
| 165450446440 | 16 | 8... Nbd7 | best | excellent | precision | excellent | 0.0017 | 0.446 | no | Nd5 | - | +0.92 | +0.95 |
| 165450446440 | 18 | 9... e6 | excellent | good | precision | good | 0.0232 | 0.454 | no | Qa5 | Qa5 | +0.94 | +1.01 |
| 165450446440 | 20 | 10... Bb4 | inaccuracy | good | precision | good | 0.0311 | 0.493 | no | Nxe4 | Nxe4 | +0.72 | +0.65 |
| 165450446440 | 21 | 11. a3 | good | excellent | precision | excellent | 0.0140 | 0.538 | no | Nxf6+ | Nxf6+ | +0.36 | +0.43 |
| 165450446440 | 24 | 12... Qxf6 | excellent | best | precision | best | 0.0000 | 0.440 | yes | Qxf6 | Nxf6 | +1.06 | +1.02 |
| 165450446440 | 25 | 13. Rf1 | inaccuracy | good | precision | good | 0.0414 | 0.560 | no | Nh3 | Nh3 | +0.38 | +0.31 |
| 165450446440 | 28 | 14... Qe6 | best | excellent | precision | excellent | 0.0012 | 0.446 | no | Nxe5 | - | +1.04 | +1.05 |
| 165450446440 | 30 | 15... Qa2 | good | excellent | precision | excellent | 0.0017 | 0.442 | no | Rg8 | Rg8 | +1.37 | +1.16 |
| 165450446440 | 31 | 16. Qxf7+ | mistake | inaccuracy | precision | inaccuracy | 0.0965 | 0.568 | no | c4 | c4 | -0.59 | -0.49 |
| 165450446440 | 34 | 17... Qa1# | great | best | precision | best | 0.0000 | 1.000 | yes | Qa1# | - | - | -# |
| 165557442658 | 6 | 3... Bc5 | mistake | inaccuracy | precision | inaccuracy | 0.0812 | 0.508 | no | c6 | c6 | +1.27 | +1.25 |
| 165557442658 | 17 | 9. Bg5 | excellent | good | precision | good | 0.0235 | 0.508 | no | O-O | O-O | -0.17 | -0.27 |
| 165557442658 | 18 | 9... O-O | best | excellent | precision | excellent | 0.0029 | 0.516 | no | h6 | - | -0.17 | -0.15 |
| 165557442658 | 24 | 12... Bg4 | good | excellent | precision | excellent | 0.0188 | 0.519 | no | Be6 | Be6 | +0.07 | +0.00 |
| 165557442658 | 34 | 17... Re4 | excellent | best | precision | best | 0.0000 | 0.509 | yes | Re4 | h6 | -0.07 | -0.10 |
| 165557442658 | 39 | 20. Qe8+ | excellent | best | precision | best | 0.0000 | 0.500 | no | Qe3 | Qd2 | 0.00 | +0.00 |
| 165557442658 | 42 | 21... Bxd4 | excellent | best | precision | best | 0.0000 | 0.509 | yes | Bxd4 | Qf5 | -0.01 | -0.09 |
| 165557442658 | 45 | 23. Qe7 | inaccuracy | good | precision | good | 0.0411 | 0.496 | no | Qxf7 | Qxf7 | -0.86 | -0.84 |
| 165557442658 | 49 | 25. Qxa7 | miss | mistake | precision | mistake | 0.1489 | 0.500 | no | Qxf7 | Qxf7 | -2.50 | -2.61 |
| 165557442658 | 50 | 25... d3 | great | best | precision | best | 0.0000 | 0.649 | yes | d3 | - | -2.50 | -3.06 |
| 165557442658 | 53 | 27. Qf5+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qf5+ | - | 0.00 | +0.00 |
| 165557442658 | 60 | 30... Qe1+ | great | best | precision | best | 0.0000 | 0.847 | yes | Qe1+ | - | -6.32 | -6.91 |
| 165974850998 | 13 | 7. Bg5 | best | excellent | precision | excellent | 0.0087 | 0.509 | no | Na4 | - | +0.21 | +0.00 |
| 165974850998 | 23 | 12. Bc4 | good | excellent | precision | excellent | 0.0075 | 0.535 | no | Bb3 | Bb3 | +0.14 | +0.32 |
| 165974850998 | 24 | 12... Re8 | inaccuracy | good | precision | good | 0.0347 | 0.481 | no | a5 | a5 | +1.23 | +0.92 |
| 165974850998 | 25 | 13. c3 | mistake | inaccuracy | precision | inaccuracy | 0.0695 | 0.553 | no | Qh5 | Qh5 | -0.33 | -0.28 |
| 165974850998 | 26 | 13... dxc3 | good | excellent | precision | excellent | 0.0163 | 0.516 | no | Qf6 | b5 | +0.07 | +0.00 |
| 165974850998 | 31 | 16. Bb5 | best | excellent | precision | excellent | 0.0029 | 0.503 | no | Bb3 | - | -0.08 | -0.05 |
| 165974850998 | 36 | 18... Bb6 | excellent | best | precision | best | 0.0000 | 0.519 | no | Bf8 | Bd6 | -0.27 | -0.21 |
| 165974850998 | 38 | 19... Qd6 | good | excellent | precision | excellent | 0.0174 | 0.515 | no | Rxe1+ | Rxe1+ | -0.04 | +0.04 |
| 165974850998 | 40 | 20... Qb8 | inaccuracy | good | precision | good | 0.0360 | 0.513 | no | Re4 | Re4 | +0.63 | +0.39 |
| 165974850998 | 41 | 21. Qd7 | good | excellent | precision | excellent | 0.0133 | 0.523 | no | Qb5 | Qb5 | +0.25 | +0.15 |
| 165974850998 | 47 | 24. Qxd6 | great | excellent | precision | excellent | 0.0044 | 0.747 | no | Rxe8+ | - | - | +4.54 |
| 166096155098 | 13 | 7. O-O | excellent | best | precision | best | 0.0000 | 0.754 | yes | O-O | Nd5 | +4.65 | +4.58 |
| 166096155098 | 20 | 10... Qf6 | good | excellent | precision | excellent | 0.0017 | 0.179 | no | Qb6 | Qb6 | +6.58 | +6.49 |
| 166096155098 | 21 | 11. Nf3 | good | excellent | precision | excellent | 0.0150 | 0.824 | no | Ne4 | Ne4 | +5.97 | +6.07 |
| 166096155098 | 22 | 11... Qg6 | good | excellent | precision | excellent | 0.0150 | 0.191 | no | O-O | O-O | +6.41 | +6.49 |
| 166096155098 | 23 | 12. Bb5+ | best | excellent | precision | excellent | 0.0070 | 0.824 | no | Ne4 | - | +6.41 | +6.58 |
| 166096155098 | 25 | 13. dxc6 | inaccuracy | good | precision | good | 0.0326 | 0.826 | no | Bd3 | Bd3 | +5.54 | +5.64 |
| 166096155098 | 26 | 13... Bh3 | mistake | blunder | precision | blunder | 0.2068 | 0.207 | no | O-O | O-O | M3 | M3 |
| 166583201950 | 5 | 3. exd5 | book | best | precision | best | 0.0000 | 0.519 | yes | exd5 | - | +0.20 | +0.24 |
| 166583201950 | 6 | 3... Bd7 | mistake | inaccuracy | precision | inaccuracy | 0.0819 | 0.486 | no | exd5 | exd5 | +1.67 | +1.67 |
| 166583201950 | 8 | 4... Bb4 | inaccuracy | good | precision | good | 0.0392 | 0.410 | no | Nf6 | Nf6 | +2.16 | +2.28 |
| 166583201950 | 13 | 7. Nxb4 | great | best | precision | best | 0.0000 | 0.740 | yes | Nxb4 | - | +4.56 | +4.50 |
| 166583201950 | 16 | 8... Bxf3 | good | excellent | precision | excellent | 0.0167 | 0.244 | no | O-O | Qd6 | +5.24 | +5.27 |
| 166583201950 | 19 | 10. Qxb7 | inaccuracy | good | precision | good | 0.0389 | 0.780 | no | Qe2+ | Qe2+ | +3.83 | +4.52 |
| 166583201950 | 20 | 10... Qxc4 | excellent | best | precision | best | 0.0000 | 0.259 | yes | Qxc4 | O-O | +3.96 | +4.55 |
| 166583201950 | 24 | 12... Qc6 | mistake | inaccuracy | precision | inaccuracy | 0.0752 | 0.305 | no | Qd5 | Qd5 | +5.43 | +5.43 |
| 166583201950 | 25 | 13. Qc8+ | great | best | precision | best | 0.0000 | 0.779 | yes | Qc8+ | - | +5.43 | +5.93 |
| 166583201950 | 29 | 15. Qxh8 | great | best | precision | best | 0.0000 | 0.793 | yes | Qxh8 | - | +5.43 | +5.52 |
| 166583201950 | 30 | 15... Qxc2 | inaccuracy | good | precision | good | 0.0450 | 0.217 | no | Qa5+ | Qa5+ | +6.64 | +6.76 |
| 166583201950 | 32 | 16... Qe4+ | great | best | precision | best | 0.0000 | 0.652 | yes | Qe4+ | - | -2.09 | -2.95 |
| 166583201950 | 37 | 19. Qxa8 | great | best | precision | best | 0.0000 | 0.698 | yes | Qxa8 | - | +2.97 | +3.87 |
| 166583201950 | 39 | 20. Re1 | great | best | precision | best | 0.0000 | 0.838 | yes | Re1 | - | +6.95 | +7.25 |
| 166583201950 | 43 | 22. Kf2 | great | best | precision | best | 0.0000 | 0.854 | yes | Kf2 | - | +7.33 | +7.92 |
| 166583201950 | 46 | 23... Qf4+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qf4+ | - | 0.00 | +0.00 |
| 166583201950 | 50 | 25... Qxc1+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qxc1+ | - | -M2 | -M2 |
| 166583201950 | 53 | 27. Qd5 | inaccuracy | good | precision | good | 0.0306 | 0.262 | no | Qxa7 | Qxa7 | -5.68 | -5.68 |
| 166583201950 | 56 | 28... Qe3+ | best | excellent | precision | excellent | 0.0004 | 0.781 | no | Qf1+ | - | -5.68 | -5.34 |
| 166583201950 | 58 | 29... Qe2+ | inaccuracy | excellent | precision | excellent | 0.0165 | 0.799 | no | f6 | f6 | -4.70 | -5.50 |
| 166583201950 | 59 | 30. Kf4 | mistake | blunder | precision | blunder | 0.2179 | 0.218 | no | Kh4 | Kh4 | -8.78 | -M15 |
| 166583201950 | 64 | 32... Kc8 | good | excellent | precision | excellent | 0.0068 | 0.860 | no | Ke8 | Ke7 | -4.53 | -4.90 |
| 166853117390 | 21 | 11. h3 | good | excellent | precision | excellent | 0.0059 | 0.491 | no | Qd2 | a4 | -0.20 | -0.26 |
| 166853117390 | 23 | 12. Qxh5 | great | best | precision | best | 0.0000 | 0.739 | yes | Qxh5 | - | +4.29 | +4.21 |
| 166853117390 | 24 | 12... c6 | mistake | inaccuracy | precision | inaccuracy | 0.0916 | 0.269 | no | Kh7 | Kh7 | +5.88 | +6.46 |
| 166853117390 | 29 | 15. Bxe5+ | good | inaccuracy | precision | inaccuracy | 0.0554 | 0.845 | no | Qh6+ | Qh6+ | +5.69 | +6.86 |
| 166853117390 | 30 | 15... f6 | inaccuracy | good | precision | good | 0.0330 | 0.164 | no | Bxe5 | Bxe5 | +7.31 | +8.50 |
| 166853117390 | 32 | 16... Kg8 | mistake | good | precision | good | 0.0470 | 0.195 | no | Kg7 | Kg7 | +7.75 | +8.49 |
| 167316688806 | 5 | 3. Bc4 | book | excellent | precision | excellent | 0.0110 | 0.523 | no | d4 | - | +0.17 | +0.20 |
| 167316688806 | 6 | 3... Nc6 | book | excellent | precision | excellent | 0.0093 | 0.488 | no | Nf6 | - | +0.41 | +0.46 |
| 167316688806 | 7 | 4. Nc3 | book | excellent | precision | excellent | 0.0058 | 0.527 | no | d4 | - | +0.34 | +0.33 |
| 167316688806 | 21 | 11. Nxe5 | excellent | best | precision | best | 0.0000 | 0.488 | yes | Nxe5 | Bb3 | -0.35 | -0.32 |
| 167316688806 | 24 | 12... Nxc4 | excellent | best | precision | best | 0.0000 | 0.473 | yes | Nxc4 | Nc6 | +0.52 | +0.61 |
| 167316688806 | 26 | 13... O-O | inaccuracy | good | precision | good | 0.0381 | 0.479 | no | Bd7 | Bd7 | +1.28 | +1.03 |
| 167316688806 | 27 | 14. Re1 | inaccuracy | good | precision | good | 0.0439 | 0.560 | no | Qd2 | Qd2 | +0.24 | +0.27 |
| 167316688806 | 28 | 14... e5 | mistake | inaccuracy | precision | inaccuracy | 0.0779 | 0.484 | no | Bd7 | Bd7 | +1.57 | +1.63 |
| 167316688806 | 29 | 15. fxe5 | miss | inaccuracy | precision | inaccuracy | 0.0819 | 0.594 | no | f5 | f5 | +0.32 | +0.20 |
| 167316688806 | 43 | 22. Rb8 | great | best | precision | best | 0.0000 | 0.430 | yes | Rb8 | - | -1.09 | -1.09 |
| 167359572290 | 7 | 4. Nf3 | best | excellent | precision | excellent | 0.0012 | 0.557 | no | Nc3 | - | +0.90 | +0.90 |
| 167359572290 | 8 | 4... Bf5 | inaccuracy | good | precision | good | 0.0269 | 0.444 | no | e5 | e5 | +1.44 | +1.34 |
| 167359572290 | 12 | 6... Nxd3+ | best | excellent | precision | excellent | 0.0105 | 0.461 | no | Bxd3 | - | +0.61 | +0.57 |
| 167359572290 | 15 | 8. Qxd3 | great | best | precision | best | 0.0000 | 0.771 | yes | Qxd3 | - | +4.90 | +4.68 |
| 167359572290 | 17 | 9. O-O | excellent | good | precision | good | 0.0385 | 0.826 | no | Ne5 | Ne5 | +5.56 | +5.08 |
| 167359572290 | 23 | 12. Rxc6+ | best | excellent | precision | excellent | 0.0060 | 0.905 | no | Qf5+ | - | +8.64 | +8.86 |
| 167359572290 | 29 | 15. Rc1 | great | good | precision | good | 0.0410 | 0.958 | no | exd6 | - | +9.33 | +9.64 |
| 167359572290 | 30 | 15... fxe5 | good | best | precision | best | 0.0000 | 0.083 | yes | fxe5 | Bc7 | M16 | +12.30 |
| 167359572290 | 33 | 17. Qa6+ | good | excellent | precision | excellent | 0.0145 | 0.926 | no | Qc2 | Rxc7+ | +8.59 | +8.85 |
| 167359572290 | 36 | 18... Ke7 | inaccuracy | mistake | precision | mistake | 0.1021 | 0.102 | no | Bxe5 | Bxe5 | M4 | M4 |
| 167396435524 | 10 | 5... O-O | book | excellent | precision | excellent | 0.0018 | 0.488 | no | h6 | - | +0.19 | +0.20 |
| 167396435524 | 14 | 7... Nxd5 | best | excellent | precision | excellent | 0.0053 | 0.497 | no | h6 | - | +0.08 | +0.10 |
| 167396435524 | 19 | 10. Bxh6 | blunder | mistake | precision | mistake | 0.1877 | 0.526 | no | Bxc6 | Bxc6 | -2.73 | -2.83 |
| 167396435524 | 21 | 11. Nxd4 | excellent | good | precision | good | 0.0214 | 0.337 | no | Bxc6 | a4 | -2.98 | -3.25 |
| 167396435524 | 23 | 12. c3 | excellent | best | precision | best | 0.0000 | 0.312 | yes | c3 | Qd2 | -3.24 | -3.41 |
| 167396435524 | 26 | 13... Ng5 | inaccuracy | good | precision | good | 0.0478 | 0.724 | no | Nf4 | Qg5 | -2.98 | -3.10 |
| 167396435524 | 29 | 15. d4 | excellent | good | precision | good | 0.0244 | 0.312 | no | f4 | f4 | -3.47 | -3.82 |
| 167397747616 | 5 | 3. exd5 | book | best | precision | best | 0.0000 | 0.519 | yes | exd5 | - | +0.22 | +0.24 |
| 167397747616 | 6 | 3... exd5 | book | best | precision | best | 0.0000 | 0.486 | yes | exd5 | - | +0.22 | +0.29 |
| 167397747616 | 8 | 4... Bg4 | book | excellent | precision | excellent | 0.0187 | 0.487 | no | Nc6 | - | +0.54 | +0.54 |
| 167397747616 | 11 | 6. O-O | book | excellent | precision | excellent | 0.0006 | 0.519 | no | h3 | - | +0.32 | +0.31 |
| 167397747616 | 12 | 6... Be7 | book | best | precision | best | 0.0000 | 0.482 | yes | Be7 | - | +0.32 | +0.30 |
| 167397747616 | 17 | 9. Be2 | inaccuracy | good | precision | good | 0.0359 | 0.442 | no | Bb5+ | Bb5+ | -1.68 | -1.62 |
| 167397747616 | 26 | 13... c6 | great | best | precision | best | 0.0000 | 0.594 | yes | c6 | - | -1.55 | -1.65 |
| 167397747616 | 29 | 15. Re5 | good | excellent | precision | excellent | 0.0163 | 0.414 | no | Be5 | Be3 | -1.75 | -1.78 |
| 167397747616 | 31 | 16. Rg5 | inaccuracy | good | precision | good | 0.0449 | 0.399 | no | Ree1 | Ree1 | -2.65 | -2.58 |
| 167397747616 | 37 | 19. Nxe4 | great | best | precision | best | 0.0000 | 0.732 | yes | Nxe4 | - | +4.41 | +4.42 |
| 167397747616 | 38 | 19... Rxe4 | mistake | good | precision | good | 0.0267 | 0.263 | no | Kh7 | Kh7 | +5.00 | +5.24 |
| 167397747616 | 44 | 22... Re1+ | best | excellent | precision | excellent | 0.0029 | 0.455 | no | Qd6 | - | +0.70 | +0.85 |
| 167397747616 | 45 | 23. Rxe1 | excellent | good | precision | good | 0.0331 | 0.549 | no | Kh2 | Kh2 | +0.53 | +0.37 |
| 167397747616 | 50 | 25... Rxg6 | excellent | best | precision | best | 0.0000 | 0.346 | yes | Rxg6 | fxg6 | +2.83 | +2.39 |
| 167397747616 | 55 | 28. f4 | good | excellent | precision | excellent | 0.0075 | 0.651 | no | Qf6+ | Qf6+ | +2.43 | +2.99 |
| 167397747616 | 56 | 28... Qc7 | good | excellent | precision | excellent | 0.0046 | 0.332 | no | a5 | Qe7 | +2.95 | +3.49 |
| 167397747616 | 59 | 30. f5 | inaccuracy | good | precision | good | 0.0270 | 0.680 | no | Qh6+ | Qf6+ | +1.71 | +2.71 |
| 167397747616 | 63 | 32. g4 | excellent | good | precision | good | 0.0275 | 0.786 | no | b4 | b4 | +4.23 | +5.28 |
| 167397747616 | 65 | 33. Kh3 | inaccuracy | good | precision | good | 0.0358 | 0.803 | no | b4 | Kg3 | +2.81 | +5.11 |
| 167397747616 | 66 | 33... Kg5 | inaccuracy | good | precision | good | 0.0339 | 0.233 | no | c5 | c5 | +4.24 | +5.97 |
| 167397747616 | 67 | 34. Kg3 | mistake | good | precision | good | 0.0331 | 0.801 | no | b4 | b4 | +2.34 | +5.39 |
| 167397747616 | 68 | 34... a5 | inaccuracy | excellent | precision | excellent | 0.0111 | 0.221 | no | b4 | c5 | +3.98 | +5.96 |
| 167397747616 | 69 | 35. Kh3 | inaccuracy | excellent | precision | excellent | 0.0091 | 0.801 | no | b3 | a3 | +2.33 | +5.72 |
| 167397747616 | 70 | 35... c5 | inaccuracy | good | precision | good | 0.0236 | 0.208 | no | Kf6 | Kf6 | +3.62 | +5.30 |
| 167397747616 | 72 | 36... Kxf6 | great | best | precision | best | 0.0000 | 0.495 | yes | Kxf6 | - | 0.00 | -0.07 |
| 167397747616 | 73 | 37. Kh4 | good | mistake | precision | mistake | 0.1812 | 0.496 | no | c3 | Kg3 | -0.40 | -3.33 |
| 167397747616 | 76 | 38... Kg7 | miss | blunder | precision | blunder | 0.5260 | 0.781 | no | c4 | c4 | +1.92 | +4.58 |
| 167397747616 | 77 | 39. Kg5 | great | best | precision | best | 0.0000 | 0.745 | yes | Kg5 | - | +1.92 | +5.12 |
| 167397747616 | 78 | 39... c4 | inaccuracy | excellent | precision | excellent | 0.0033 | 0.232 | no | Kf7 | b4 | +3.62 | +4.71 |
| 167397747616 | 79 | 40. Kf4 | great | best | precision | best | 0.0000 | 0.750 | yes | Kf4 | - | +3.62 | +5.26 |
| 167397747616 | 80 | 40... d3 | good | best | precision | best | 0.0000 | 0.226 | yes | d3 | c3 | +4.68 | +4.99 |
| 167397747616 | 82 | 41... cxd3 | best | inaccuracy | precision | inaccuracy | 0.0546 | 0.229 | no | c3 | - | +4.68 | +5.75 |
| 167397747616 | 84 | 42... Kg6 | good | excellent | precision | excellent | 0.0000 | 0.149 | no | b4 | Kf6 | +5.19 | +6.04 |
| 167397747616 | 90 | 45... Kf3 | excellent | best | precision | best | 0.0000 | 0.048 | no | Kf5 | Kg5 | +6.90 | +7.43 |
| 167397747616 | 98 | 49... Kb2 | good | excellent | precision | excellent | 0.0083 | 0.054 | no | Kd3 | Kd3 | +9.79 | +12.99 |
| 167397747616 | 100 | 50... Kxa2 | good | best | precision | best | 0.0000 | 0.211 | yes | Kxa2 | Ka3 | +6.57 | +8.34 |
| 167397747616 | 101 | 51. b6 | inaccuracy | good | precision | good | 0.0448 | 0.875 | no | Ka4 | Kb4 | +5.42 | +5.34 |
| 167397747616 | 103 | 52. b7 | inaccuracy | best | precision | best | 0.0000 | 0.773 | yes | b7 | Kb5 | +5.37 | +5.12 |
| 167397747616 | 104 | 52... Ka2 | mistake | blunder | precision | blunder | 0.2321 | 0.232 | no | Kc3 | Kc2 | M5 | M5 |
| 167479014786 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.488 | yes | Nf6 | - | +0.20 | +0.17 |
| 167479014786 | 7 | 4. Nc3 | book | best | precision | best | 0.0000 | 0.510 | yes | Nc3 | - | +0.20 | +0.16 |
| 167479014786 | 11 | 6. O-O | best | excellent | precision | excellent | 0.0006 | 0.498 | no | a4 | - | 0.00 | -0.11 |
| 167479014786 | 16 | 8... Qe7 | good | excellent | precision | excellent | 0.0174 | 0.489 | no | h6 | h6 | +0.53 | +0.49 |
| 167479014786 | 26 | 13... f5 | mistake | inaccuracy | precision | inaccuracy | 0.0868 | 0.524 | no | Nc6 | Nc6 | +1.11 | +1.09 |
| 167479014786 | 27 | 14. exf5 | inaccuracy | good | precision | good | 0.0386 | 0.563 | no | Ng5 | Ng5 | +0.31 | +0.34 |
| 167479014786 | 28 | 14... Qxf5 | inaccuracy | good | precision | good | 0.0489 | 0.480 | no | Rxf5 | gxf5 | +1.08 | +1.19 |
| 167479014786 | 30 | 15... e4 | good | excellent | precision | excellent | 0.0134 | 0.513 | no | exd4 | exd4 | +0.52 | +0.06 |
| 167479014786 | 31 | 16. Ng5 | miss | inaccuracy | precision | inaccuracy | 0.0773 | 0.503 | no | Qb3+ | Qb3+ | -1.29 | -1.28 |
| 167479014786 | 32 | 16... h6 | inaccuracy | good | precision | good | 0.0263 | 0.574 | no | cxd4 | cxd4 | -0.73 | -0.85 |
| 167479014786 | 33 | 17. Qb3+ | inaccuracy | good | precision | good | 0.0200 | 0.451 | no | g4 | g4 | -1.42 | -1.29 |
| 167479014786 | 35 | 18. Ne6 | great | best | precision | best | 0.0000 | 0.663 | yes | Ne6 | - | +3.18 | +3.06 |
| 167479014786 | 39 | 20. Qxa8 | great | best | precision | best | 0.0000 | 0.691 | yes | Qxa8 | - | +3.42 | +3.39 |
| 167479014786 | 45 | 23. Qe7 | blunder | mistake | precision | mistake | 0.1706 | 0.731 | no | Bxf6 | Bxf6 | +1.09 | +1.14 |
| 167479014786 | 47 | 24. b4 | miss | mistake | precision | mistake | 0.1412 | 0.556 | no | Qxd6 | Qxd6 | -1.15 | -1.49 |
| 167479014786 | 56 | 28... Qxg3 | great | best | precision | best | 0.0000 | 0.439 | yes | Qxg3 | - | +0.93 | +0.94 |
| 167479014786 | 62 | 31... e3 | excellent | good | precision | good | 0.0281 | 0.423 | no | Be5 | Be5 | +1.35 | +1.84 |
| 167479014786 | 66 | 33... Rxc3 | mistake | inaccuracy | precision | inaccuracy | 0.0867 | 0.304 | no | Re8 | Re8 | +5.36 | +5.51 |
| 167479014786 | 69 | 35. d7 | excellent | best | precision | best | 0.0000 | 0.800 | yes | d7 | Rf8+ | +5.10 | +5.93 |
| 168148201932 | 6 | 3... Qxd5 | best | excellent | precision | excellent | 0.0100 | 0.442 | no | e4 | - | +1.07 | +1.22 |
| 168148201932 | 11 | 6. d3 | inaccuracy | good | precision | good | 0.0462 | 0.586 | no | O-O | O-O | +0.51 | +0.67 |
| 168148201932 | 21 | 11. Qxb7 | great | best | precision | best | 0.0000 | 0.585 | yes | Qxb7 | - | +1.41 | +1.53 |
| 168148201932 | 24 | 12... Nd6 | inaccuracy | good | precision | good | 0.0487 | 0.674 | no | O-O | O-O | -2.05 | -2.21 |
| 168148201932 | 25 | 13. Qf3 | inaccuracy | good | precision | good | 0.0475 | 0.371 | no | Qc6+ | Qc6+ | -3.13 | -3.10 |
| 168148201932 | 32 | 16... Bd6 | miss | blunder | precision | blunder | 0.3019 | 0.675 | no | Nxd5 | Nxd5 | +2.25 | +2.18 |
| 168148201932 | 36 | 18... Bxf4 | mistake | inaccuracy | precision | inaccuracy | 0.0891 | 0.624 | no | Qxf4 | Qxf4 | -0.81 | -0.70 |
| 168148201932 | 38 | 19... Nd6 | miss | mistake | precision | mistake | 0.1010 | 0.601 | no | Qxb2 | Qxb2 | 0.00 | +0.00 |
| 168148201932 | 39 | 20. Qxa6 | great | excellent | precision | excellent | 0.0077 | 0.500 | no | Qc6 | - | 0.00 | +0.00 |
| 168148201932 | 42 | 21... Bd2 | blunder | mistake | precision | mistake | 0.1788 | 0.621 | no | Qc2 | Qc2 | +1.01 | +0.98 |
| 168148201932 | 43 | 22. Re2 | great | best | precision | best | 0.0000 | 0.558 | yes | Re2 | - | +1.01 | +1.03 |
| 168426135116 | 21 | 11. d4 | best | excellent | precision | excellent | 0.0032 | 0.532 | no | h3 | - | +0.51 | +0.44 |
| 168426135116 | 26 | 13... dxe5 | great | best | precision | best | 0.0000 | 0.551 | yes | dxe5 | - | -0.83 | -0.81 |
| 168426135116 | 28 | 14... Bxd4 | miss | mistake | precision | mistake | 0.1217 | 0.617 | no | Qxd4 | Qxd4 | +0.21 | +0.08 |
| 168426135116 | 31 | 16. Qxd4 | great | best | precision | best | 0.0000 | 0.704 | yes | Qxd4 | - | +2.57 | +3.55 |
| 168426135116 | 32 | 16... Bf5 | inaccuracy | good | precision | good | 0.0377 | 0.287 | no | Rd8 | Rd8 | +4.18 | +4.30 |
| 168426135116 | 33 | 17. Nc3 | best | excellent | precision | excellent | 0.0063 | 0.751 | no | Qe3 | - | +4.18 | +4.30 |
| 168426135116 | 34 | 17... Rad8 | mistake | good | precision | good | 0.0272 | 0.249 | no | Rae8 | Rae8 | +4.72 | +4.89 |
| 168426135116 | 38 | 19... Rxd5 | mistake | inaccuracy | precision | inaccuracy | 0.0725 | 0.211 | no | Qb6 | Qb6 | +7.00 | +7.11 |
| 168426135116 | 39 | 20. Rxd5 | miss | inaccuracy | precision | inaccuracy | 0.0812 | 0.861 | no | Nxd5 | Nxd5 | +5.00 | +4.92 |
| 168426135116 | 45 | 23. Nb5 | good | excellent | precision | excellent | 0.0179 | 0.791 | no | Re4 | Re4 | +4.25 | +4.78 |
| 168426135116 | 46 | 23... Qe6 | good | excellent | precision | excellent | 0.0084 | 0.227 | no | a6 | a6 | +4.85 | +4.97 |
| 168426135116 | 48 | 24... Qe2 | excellent | good | precision | good | 0.0234 | 0.233 | no | Qg6 | Qg6 | +4.97 | +5.17 |
| 168426135116 | 49 | 25. Nxc7 | best | excellent | precision | excellent | 0.0056 | 0.790 | no | Rd2 | - | +4.97 | +5.21 |
| 168426135116 | 50 | 25... Rc8 | good | best | precision | best | 0.0000 | 0.208 | yes | Rc8 | Re5 | +5.44 | +5.23 |
| 168426135116 | 51 | 26. Rd2 | best | excellent | precision | excellent | 0.0077 | 0.793 | no | Qf5 | - | +5.44 | +5.11 |
| 168426135116 | 53 | 27. Ra3 | best | excellent | precision | excellent | 0.0000 | 0.794 | no | Rd3 | - | +5.44 | +5.32 |
| 168426135116 | 58 | 29... Rc1+ | good | excellent | precision | excellent | 0.0095 | 0.168 | no | Qe8 | Rf8 | +6.34 | +6.50 |
| 169217872990 | 7 | 4. Nf3 | best | excellent | precision | excellent | 0.0036 | 0.484 | no | Nc3 | - | -0.29 | -0.32 |
| 169217872990 | 9 | 5. Be2 | best | excellent | precision | excellent | 0.0006 | 0.493 | no | c4 | - | -0.10 | -0.16 |
| 169217872990 | 10 | 5... O-O | excellent | best | precision | best | 0.0000 | 0.510 | yes | O-O | c5 | -0.07 | -0.12 |
| 169217872990 | 11 | 6. O-O | excellent | best | precision | best | 0.0000 | 0.493 | yes | O-O | c4 | -0.13 | -0.13 |
| 169217872990 | 18 | 9... exd4 | best | excellent | precision | excellent | 0.0060 | 0.468 | no | Kh8 | - | +0.58 | +0.62 |
| 169217872990 | 19 | 10. Nxd4 | inaccuracy | good | precision | good | 0.0375 | 0.538 | no | Qxd4 | Qxd4 | -0.27 | -0.22 |
| 169217872990 | 22 | 11... f5 | inaccuracy | good | precision | good | 0.0405 | 0.492 | no | Ne5 | Ne5 | +0.92 | +0.81 |
| 169217872990 | 29 | 15. Bg4 | mistake | inaccuracy | precision | inaccuracy | 0.0712 | 0.506 | no | Nc3 | Bd5+ | -1.37 | -1.08 |
| 169217872990 | 30 | 15... Nb4 | inaccuracy | good | precision | good | 0.0488 | 0.565 | no | Bxg4 | Bxg4 | -0.38 | -0.31 |
| 169217872990 | 35 | 18. Kh2 | good | excellent | precision | excellent | 0.0176 | 0.418 | no | Kh1 | Kh1 | -1.84 | -2.00 |
| 169217872990 | 36 | 18... Nxc2 | miss | blunder | precision | blunder | 0.2008 | 0.619 | no | Rae8 | Qxc2 | +1.58 | +1.36 |
| 169217872990 | 38 | 19... Qf4+ | miss | inaccuracy | precision | inaccuracy | 0.0668 | 0.444 | no | Qxe1 | Qxe1 | +1.96 | +1.77 |
| 169217872990 | 40 | 20... Nxe1 | great | best | precision | best | 0.0000 | 0.818 | yes | Nxe1 | - | -5.52 | -5.95 |
| 169217872990 | 43 | 22. Nf6+ | mistake | excellent | precision | excellent | 0.0047 | 0.169 | no | Qa5 | Qa5 | -6.65 | -6.78 |
| 169217872990 | 55 | 28. Kg3 | excellent | best | precision | best | 0.0000 | 0.108 | yes | Kg3 | a3 | -8.62 | -8.70 |
| 169217872990 | 57 | 29. Kf2 | excellent | best | precision | best | 0.0000 | 0.099 | yes | Kf2 | a3 | -8.85 | -9.58 |
| 169217872990 | 59 | 30. Kf3 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.000 | no | h4 | Kg2 | -M7 | -M9 |
| 169217872990 | 63 | 32. f6 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kg3 | - | -M5 | -M5 |
| 170185678278 | 7 | 4. dxc6 | excellent | good | precision | good | 0.0270 | 0.518 | no | Nc3 | d4 | 0.00 | -0.15 |
| 170185678278 | 15 | 8. Nc3 | blunder | mistake | precision | mistake | 0.1939 | 0.432 | no | Be2 | Be2 | -5.08 | -4.95 |
| 170185678278 | 17 | 9. Na4 | miss | inaccuracy | precision | inaccuracy | 0.0869 | 0.494 | no | Be2 | Be2 | -1.66 | -1.60 |
| 170185678278 | 18 | 9... Bd4 | miss | inaccuracy | precision | inaccuracy | 0.0833 | 0.593 | no | Ba7 | Ba7 | -0.04 | -0.16 |
| 170185678278 | 19 | 10. Nxd4 | good | excellent | precision | excellent | 0.0100 | 0.491 | no | Be2 | Be2 | -0.58 | -0.53 |
| 170185678278 | 25 | 13. Nc5 | good | excellent | precision | excellent | 0.0070 | 0.508 | no | Bb2 | Bb2 | -0.32 | -0.24 |
| 170185678278 | 26 | 13... Qc7 | mistake | inaccuracy | precision | inaccuracy | 0.0793 | 0.514 | no | Bg4 | Bg4 | +1.15 | +1.12 |
| 170185678278 | 29 | 15. c5 | mistake | inaccuracy | precision | inaccuracy | 0.0900 | 0.602 | no | Bb2 | Bb2 | +0.33 | +0.20 |
| 170185678278 | 33 | 17. Rb1 | excellent | best | precision | best | 0.0000 | 0.580 | yes | Rb1 | a3 | +1.35 | +1.39 |
| 170185678278 | 37 | 19. Bb2 | inaccuracy | good | precision | good | 0.0476 | 0.569 | no | a3 | a3 | +0.30 | +0.32 |
| 170185678278 | 38 | 19... Nf6 | miss | inaccuracy | precision | inaccuracy | 0.0908 | 0.481 | no | Qxa2 | Qxa2 | +1.78 | +1.90 |
| 170185678278 | 39 | 20. Bc3 | mistake | inaccuracy | precision | inaccuracy | 0.0803 | 0.610 | no | Bc4 | Bxd4 | +0.42 | +0.50 |
| 170185678278 | 40 | 20... Qxa2 | great | best | precision | best | 0.0000 | 0.471 | yes | Qxa2 | - | +0.42 | +0.42 |
| 170185678278 | 43 | 22. Rxe8+ | excellent | best | precision | best | 0.0000 | 0.501 | yes | Rxe8+ | Rb6 | +0.06 | +0.01 |
| 170185678278 | 49 | 25. Rb5 | best | excellent | precision | excellent | 0.0082 | 0.508 | no | Qb3 | - | +0.06 | -0.01 |
| 170185678278 | 52 | 26... Qxe1+ | great | best | precision | best | 0.0000 | 0.870 | yes | Qxe1+ | - | - | -8.87 |
| 171124015136 | 8 | 4... Be7 | good | excellent | precision | excellent | 0.0110 | 0.476 | no | c5 | c5 | +0.84 | +0.61 |
| 171124015136 | 9 | 5. d3 | good | excellent | precision | excellent | 0.0191 | 0.535 | no | d4 | d4 | +0.27 | +0.28 |
| 171124015136 | 12 | 6... O-O | best | excellent | precision | excellent | 0.0006 | 0.482 | no | c5 | - | +0.21 | +0.31 |
| 171124015136 | 13 | 7. Nd5 | excellent | good | precision | good | 0.0267 | 0.518 | no | a4 | h3 | -0.09 | -0.15 |
| 171124015136 | 17 | 9. h4 | mistake | inaccuracy | precision | inaccuracy | 0.0876 | 0.509 | no | Bb3 | c3 | -1.27 | -1.36 |
| 171124015136 | 19 | 10. Bb3 | great | best | precision | best | 0.0000 | 0.451 | yes | Bb3 | - | -0.85 | -0.88 |
| 171124015136 | 23 | 12. cxb5 | good | excellent | precision | excellent | 0.0144 | 0.456 | no | Nh2 | Nh2 | -1.03 | -1.01 |
| 171124015136 | 26 | 13... b4 | good | excellent | precision | excellent | 0.0125 | 0.581 | no | Nc6 | Nc6 | -1.08 | -1.17 |
| 171124015136 | 27 | 14. a5 | inaccuracy | good | precision | good | 0.0477 | 0.432 | no | h5 | h5 | -2.11 | -2.02 |
| 171124015136 | 28 | 14... Ba6 | mistake | inaccuracy | precision | inaccuracy | 0.0695 | 0.615 | no | Nc6 | Nc6 | -0.86 | -0.79 |
| 171124015136 | 29 | 15. Bd5 | miss | mistake | precision | mistake | 0.1061 | 0.454 | no | Nh2 | Nh2 | -2.47 | -2.70 |
| 171124015136 | 33 | 17. Qb3 | inaccuracy | mistake | precision | mistake | 0.1023 | 0.379 | no | Bg5 | Bxh6 | -3.90 | -4.13 |
| 171124015136 | 37 | 19. Bxb7 | great | best | precision | best | 0.0000 | 0.737 | yes | Bxb7 | - | +4.26 | +4.51 |
| 171124015136 | 38 | 19... Bxf1 | good | excellent | precision | excellent | 0.0049 | 0.260 | no | Nbd7 | Nbd7 | +4.72 | +4.71 |
| 171124015136 | 43 | 22. a6 | miss | inaccuracy | precision | inaccuracy | 0.0659 | 0.808 | no | Bxe4 | Bxe4 | +3.93 | +4.56 |
| 171124015136 | 44 | 22... Nc6 | mistake | inaccuracy | precision | inaccuracy | 0.0758 | 0.257 | no | Nxa6 | Nxa6 | +6.26 | +6.48 |
| 171124015136 | 45 | 23. Bxc6 | best | excellent | precision | excellent | 0.0028 | 0.818 | no | Qb6 | - | +6.26 | +6.40 |
| 171124015136 | 46 | 23... Qxc6 | excellent | best | precision | best | 0.0000 | 0.184 | yes | Qxc6 | Nc5 | +6.34 | +6.26 |
| 171124015136 | 49 | 25. a7 | good | inaccuracy | precision | inaccuracy | 0.0522 | 0.820 | no | Qxe4 | Qxe4 | +5.54 | +5.31 |
| 171124015136 | 54 | 27... d5 | inaccuracy | mistake | precision | mistake | 0.1368 | 0.137 | no | Nh7 | Rxa8 | M7 | M8 |
| 171124015136 | 58 | 29... gxh6 | inaccuracy | mistake | precision | mistake | 0.1301 | 0.130 | no | Ng4 | Ng4 | M7 | M7 |
| 171124015136 | 60 | 30... Kg7 | best | good | precision | good | 0.0300 | 0.120 | no | Ne8 | - | +7.56 | +8.45 |
| 171124015136 | 65 | 33. Nxd4 | best | good | precision | good | 0.0283 | 0.884 | no | Ne5 | - | +7.68 | +8.14 |
| 171124015136 | 70 | 35... Nf6 | best | excellent | precision | excellent | 0.0147 | 0.113 | no | h5 | - | +8.00 | +10.06 |
| 171124015136 | 78 | 39... Kxg8 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kg7 | - | +8.97 | M18 |
| 171124015136 | 79 | 40. Qg4+ | excellent | best | precision | best | 0.0000 | 1.000 | no | b4 | Qc8+ | +8.60 | M17 |
| 171708489350 | 10 | 5... O-O | book | excellent | precision | excellent | 0.0019 | 0.487 | no | h6 | - | +0.19 | +0.20 |
| 171708489350 | 13 | 7. Bg5 | best | excellent | precision | excellent | 0.0122 | 0.516 | no | Na4 | - | +0.24 | +0.06 |
| 171708489350 | 15 | 8. Nxd4 | great | best | precision | best | 0.0000 | 0.642 | yes | Nxd4 | - | +2.55 | +2.31 |
| 171708489350 | 22 | 11... Bxb2 | good | excellent | precision | excellent | 0.0050 | 0.595 | no | c6 | c6 | -1.21 | -1.24 |
| 171708489350 | 24 | 12... Bd4 | great | best | precision | best | 0.0000 | 0.591 | yes | Bd4 | - | -1.21 | -1.40 |
| 171708489350 | 25 | 13. Ne3 | inaccuracy | good | precision | good | 0.0289 | 0.411 | no | c3 | c3 | -1.96 | -1.87 |
| 171708489350 | 26 | 13... a6 | good | excellent | precision | excellent | 0.0140 | 0.618 | no | Kh8 | c6 | -1.58 | -1.64 |
| 171708489350 | 27 | 14. Nf5 | best | excellent | precision | excellent | 0.0025 | 0.396 | no | Rfc1 | - | -1.58 | -1.67 |
| 171708489350 | 29 | 15. Bd5 | excellent | best | precision | best | 0.0000 | 0.432 | yes | Bd5 | Nxd4 | -1.15 | -1.03 |
| 171708489350 | 30 | 15... Rb8 | good | excellent | precision | excellent | 0.0088 | 0.566 | no | Bxf5 | Bxf5 | -0.81 | -1.01 |
| 171708489350 | 31 | 16. Qg4 | mistake | inaccuracy | precision | inaccuracy | 0.0819 | 0.436 | no | Nxd4 | Nxd4 | -2.22 | -2.35 |
| 171708489350 | 34 | 17... Bxh3 | great | best | precision | best | 0.0000 | 0.878 | yes | Bxh3 | - | - | -7.78 |
| 171841312410 | 7 | 4. Bc4 | inaccuracy | good | precision | good | 0.0494 | 0.544 | no | Nxe5 | Nxe5 | -0.04 | -0.09 |
| 171841312410 | 8 | 4... Nf6 | best | excellent | precision | excellent | 0.0038 | 0.506 | no | d6 | - | -0.04 | -0.02 |
| 171841312410 | 16 | 8... Bg4 | good | excellent | precision | excellent | 0.0006 | 0.501 | no | a6 | a6 | +0.30 | +0.00 |
| 171841312410 | 24 | 12... exd4 | good | inaccuracy | precision | inaccuracy | 0.0822 | 0.529 | no | Qe7 | Qe7 | +0.17 | +0.84 |
| 171841312410 | 30 | 15... Qb2 | miss | mistake | precision | mistake | 0.1277 | 0.619 | no | Bxf3 | Bxf3 | +0.53 | +0.13 |
| 171841312410 | 33 | 17. Qd3 | good | excellent | precision | excellent | 0.0013 | 0.520 | no | Qe3 | Qe3 | 0.00 | +0.29 |
| 171841312410 | 40 | 20... Rxe1 | great | best | precision | best | 0.0000 | 0.651 | yes | Rxe1 | - | -2.35 | -2.18 |
| 171841312410 | 42 | 21... Ng4 | miss | mistake | precision | mistake | 0.1063 | 0.635 | no | Qxa2 | Qxa2 | -0.44 | -0.45 |
| 171841312410 | 44 | 22... Re8 | excellent | best | precision | best | 0.0000 | 0.604 | yes | Re8 | Qb6+ | -1.57 | -1.55 |
| 171841312410 | 49 | 25. Rf1 | mistake | excellent | precision | excellent | 0.0000 | 0.000 | no | Qf1 | Qf1 | -M3 | -M3 |
| 171887823168 | 5 | 3. Bc4 | inaccuracy | good | precision | good | 0.0435 | 0.536 | no | c4 | c4 | -0.13 | -0.13 |
| 171887823168 | 14 | 7... e6 | excellent | best | precision | best | 0.0000 | 0.514 | yes | e6 | Nc6 | -0.17 | -0.18 |
| 171887823168 | 20 | 10... Qc7 | blunder | mistake | precision | mistake | 0.1789 | 0.545 | no | Nc6 | Nc6 | +2.40 | +2.36 |
| 171887823168 | 21 | 11. Nb5 | great | best | precision | best | 0.0000 | 0.634 | yes | Nb5 | - | +2.40 | +2.48 |
| 171887823168 | 22 | 11... Qd8 | best | excellent | precision | excellent | 0.0053 | 0.360 | no | Qb6 | - | +2.40 | +2.89 |
| 171887823168 | 23 | 12. Nxd6 | excellent | good | precision | good | 0.0200 | 0.662 | no | Nxf7 | Nxf7 | +2.37 | +2.46 |
| 171887823168 | 34 | 17... Ng8 | mistake | inaccuracy | precision | inaccuracy | 0.0657 | 0.393 | no | Qe7 | Qe7 | +3.07 | +3.11 |
| 171887823168 | 35 | 18. Qh3 | mistake | blunder | precision | blunder | 0.2004 | 0.673 | no | Qh5 | Qh5 | -0.88 | -0.67 |
| 171887823168 | 37 | 19. Rg3 | great | best | precision | best | 0.0000 | 0.607 | yes | Rg3 | - | +1.63 | +1.86 |
| 171887823168 | 40 | 20... Qxd4 | great | excellent | precision | excellent | 0.0052 | 0.530 | no | Qf4 | - | -0.35 | -0.46 |
| 171887823168 | 44 | 22... Qe4 | good | excellent | precision | excellent | 0.0172 | 0.670 | no | Qg7 | Qg7 | -2.22 | -2.74 |
| 171887823168 | 45 | 23. Rc1 | inaccuracy | good | precision | good | 0.0422 | 0.346 | no | Ne3 | Re3 | -3.46 | -3.57 |
| 171887823168 | 47 | 24. Bc2 | great | best | precision | best | 0.0000 | 0.578 | yes | Bc2 | - | +1.18 | +1.31 |
| 171932623366 | 12 | 6... d5 | inaccuracy | good | precision | good | 0.0395 | 0.431 | no | Qf6 | Qf6 | +1.95 | +1.90 |
| 171932623366 | 23 | 12. Bxe7 | great | best | precision | best | 0.0000 | 0.573 | yes | Bxe7 | - | +1.36 | +1.31 |
| 171932623366 | 26 | 13... Be6 | good | excellent | precision | excellent | 0.0198 | 0.423 | no | Qf6 | Qf6 | +1.69 | +1.54 |
| 171932623366 | 27 | 14. Qh5 | inaccuracy | good | precision | good | 0.0388 | 0.589 | no | Qe4 | Qe4 | +1.04 | +0.86 |
| 171932623366 | 29 | 15. Qb5 | inaccuracy | good | precision | good | 0.0459 | 0.550 | no | Qe5 | Qh6 | +0.10 | +0.07 |
| 171932623366 | 31 | 16. Rhe1 | good | excellent | precision | excellent | 0.0099 | 0.505 | no | h4 | h4 | -0.32 | -0.09 |
| 171932623366 | 32 | 16... Qf6 | inaccuracy | good | precision | good | 0.0396 | 0.505 | no | Be6 | Be6 | +0.92 | +0.82 |
| 171932623366 | 35 | 18. Rd2 | best | excellent | precision | excellent | 0.0004 | 0.246 | no | Re3 | - | -4.64 | -4.96 |
| 171932623366 | 38 | 19... Rfe8 | good | excellent | precision | excellent | 0.0142 | 0.762 | no | Rae8 | Rae8 | -4.38 | -4.66 |
| 171932623366 | 39 | 20. Rxe8+ | inaccuracy | good | precision | good | 0.0468 | 0.252 | no | Re3 | Re3 | -5.59 | -6.23 |
| 171932623366 | 41 | 21. b3 | mistake | best | precision | best | 0.0000 | 0.164 | yes | b3 | b4 | -6.45 | -7.07 |
| 171932623366 | 42 | 21... Re1+ | great | best | precision | best | 0.0000 | 0.839 | yes | Re1+ | - | - | -6.85 |
| 171980080646 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.498 | yes | c6 | Be6 | +0.15 | +0.21 |
| 171980080646 | 26 | 13... Qxb6 | excellent | best | precision | best | 0.0000 | 0.496 | yes | Qxb6 | axb6 | +0.21 | +0.12 |
| 171980080646 | 28 | 14... Be6 | excellent | good | precision | good | 0.0232 | 0.505 | no | Qc7 | Qc7 | +0.19 | +0.31 |
| 171980080646 | 31 | 16. Qe3 | excellent | good | precision | good | 0.0284 | 0.517 | no | Qg4 | Qd1 | -0.10 | -0.19 |
| 171980080646 | 33 | 17. a3 | excellent | best | precision | best | 0.0000 | 0.512 | yes | a3 | Qg5 | +0.04 | +0.06 |
| 171980080646 | 34 | 17... d5 | inaccuracy | good | precision | good | 0.0394 | 0.497 | no | h6 | Qb6 | +0.97 | +0.74 |
| 171980080646 | 41 | 21. Qc4+ | best | excellent | precision | excellent | 0.0073 | 0.591 | no | Qc3 | - | +1.54 | +1.60 |
| 171980080646 | 43 | 22. b4 | inaccuracy | good | precision | good | 0.0387 | 0.591 | no | Qc3 | Qc3 | +0.93 | +0.91 |
| 171980080646 | 44 | 22... Qxa3 | mistake | inaccuracy | precision | inaccuracy | 0.0767 | 0.447 | no | Qd8 | Qc7 | +2.23 | +2.28 |
| 171980080646 | 45 | 23. Rbe1 | miss | mistake | precision | mistake | 0.1294 | 0.629 | no | Ra1 | Ra1 | +0.09 | +0.00 |
| 171980080646 | 51 | 26. Qxf8# | great | best | precision | best | 0.0000 | 1.000 | yes | Qxf8# | - | - | # |
| 172026321412 | 10 | 5... Nf6 | good | excellent | precision | excellent | 0.0191 | 0.523 | no | Qe7+ | Qe7+ | 0.00 | -0.06 |
| 172026321412 | 13 | 7. Nc3 | excellent | good | precision | good | 0.0250 | 0.500 | no | O-O | O-O | -0.31 | -0.43 |
| 172026321412 | 15 | 8. O-O | good | excellent | precision | excellent | 0.0064 | 0.472 | no | Bg5 | Bg5 | -0.61 | -0.57 |
| 172026321412 | 18 | 9... a6 | mistake | inaccuracy | precision | inaccuracy | 0.0940 | 0.514 | no | Rxe1+ | Rxe1+ | +1.30 | +1.39 |
| 172026321412 | 21 | 11. a4 | good | inaccuracy | precision | inaccuracy | 0.0657 | 0.673 | no | Bxd5 | Nxd5 | +1.95 | +1.87 |
| 172026321412 | 23 | 12. Nxd5 | excellent | best | precision | best | 0.0000 | 0.632 | yes | Nxd5 | Bxf6 | +2.27 | +2.29 |
| 172026321412 | 26 | 13... Rxe7 | best | excellent | precision | excellent | 0.0015 | 0.309 | no | Nxe7 | - | +2.88 | +3.45 |
| 172026321412 | 27 | 14. Rxe7 | excellent | good | precision | good | 0.0202 | 0.690 | no | Ne5 | Bxf6 | +2.74 | +2.70 |
| 172026321412 | 29 | 15. Ne5 | inaccuracy | good | precision | good | 0.0389 | 0.663 | no | Qd3 | Qd3 | +1.81 | +2.18 |
| 172026321412 | 32 | 16... Bg4 | blunder | mistake | precision | mistake | 0.1656 | 0.390 | no | Qxe5 | Qxe5 | +5.73 | +5.33 |
| 172026321412 | 33 | 17. Bxf6 | good | excellent | precision | excellent | 0.0028 | 0.775 | no | exf6 | Qxg4 | +5.20 | +5.51 |
| 172026321412 | 34 | 17... Bxd1 | good | excellent | precision | excellent | 0.0131 | 0.218 | no | Qd7 | Qe6 | +5.90 | +5.85 |
| 172026321412 | 40 | 20... Bg6 | good | best | precision | best | 0.0000 | 0.179 | yes | Bg6 | a5 | +6.66 | +6.56 |
| 172026321412 | 41 | 21. Rd7 | best | excellent | precision | excellent | 0.0000 | 0.821 | no | a5 | - | +6.66 | +6.79 |
| 172349629492 | 15 | 8. Bg5 | good | excellent | precision | excellent | 0.0174 | 0.516 | no | Na4 | Na4 | -0.15 | -0.02 |
| 172349629492 | 16 | 8... Be6 | good | excellent | precision | excellent | 0.0197 | 0.501 | no | h6 | h6 | +0.18 | +0.32 |
| 172349629492 | 25 | 13. Bg3 | great | best | precision | best | 0.0000 | 0.741 | yes | Bg3 | - | +4.67 | +4.86 |
| 172349629492 | 26 | 13... c6 | good | excellent | precision | excellent | 0.0188 | 0.244 | no | Ne6 | Ne6 | +5.22 | +5.31 |
| 172349629492 | 27 | 14. Bb3 | good | excellent | precision | excellent | 0.0192 | 0.774 | no | Nxd4 | Nxd4 | +4.58 | +4.64 |
| 172349629492 | 28 | 14... d5 | inaccuracy | good | precision | good | 0.0491 | 0.254 | no | Nxb3 | Nxb3 | +5.97 | +5.84 |
| 172349629492 | 29 | 15. Nxe5 | inaccuracy | good | precision | good | 0.0332 | 0.795 | no | Nxd4 | Nxd4 | +4.88 | +5.12 |
| 172349629492 | 30 | 15... Qg5 | good | excellent | precision | excellent | 0.0090 | 0.233 | no | Qc8 | Qc8 | +5.27 | +5.71 |
| 172349629492 | 32 | 16... f5 | inaccuracy | excellent | precision | excellent | 0.0188 | 0.218 | no | Rae8 | Rae8 | +6.06 | +5.98 |
| 172349629492 | 33 | 17. dxc6+ | excellent | best | precision | best | 0.0000 | 0.800 | yes | dxc6+ | f4 | +5.79 | +5.91 |
| 172349629492 | 36 | 18... Rab8 | good | best | precision | best | 0.0000 | 0.200 | yes | Rab8 | Rae8 | +6.30 | +6.29 |
| 172349629492 | 37 | 19. Nf7+ | good | excellent | precision | excellent | 0.0109 | 0.812 | no | Rh1 | Rh1 | +5.62 | +6.02 |
| 172349629492 | 40 | 20... f4 | good | best | precision | best | 0.0000 | 0.190 | yes | f4 | Qf6 | +6.45 | +6.63 |
| 172349629492 | 45 | 23. Bxg6 | good | excellent | precision | excellent | 0.0193 | 0.853 | no | Qxc5 | Qxc5 | +5.99 | +7.17 |
| 172349629492 | 48 | 24... Qxg6 | mistake | good | precision | good | 0.0272 | 0.121 | no | Rxb7 | Rxb7 | +8.56 | +10.13 |
| 172349629492 | 49 | 25. Qxg6 | good | inaccuracy | precision | inaccuracy | 0.0570 | 0.913 | no | Be5+ | Qe5+ | +7.58 | +8.84 |
| 172349629492 | 51 | 26. Bxb8 | excellent | best | precision | best | 0.0000 | 0.883 | yes | Bxb8 | Be5+ | - | +9.11 |
| 172996177054 | 5 | 3. Bc4 | book | good | precision | good | 0.0234 | 0.527 | no | Bb5 | - | +0.07 | +0.05 |
| 172996177054 | 13 | 7. d5 | best | excellent | precision | excellent | 0.0025 | 0.549 | no | e5 | - | +0.78 | +0.79 |
| 172996177054 | 16 | 8... Nxe4 | great | best | precision | best | 0.0000 | 0.574 | yes | Nxe4 | - | -1.07 | -1.04 |
| 172996177054 | 21 | 11. Nc3 | excellent | best | precision | best | 0.0000 | 0.451 | yes | Nc3 | h4 | -0.71 | -0.71 |
| 172996177054 | 23 | 12. Ng5 | inaccuracy | good | precision | good | 0.0423 | 0.452 | no | a4 | Bf4 | -1.37 | -1.44 |
| 172996177054 | 24 | 12... e6 | inaccuracy | good | precision | good | 0.0335 | 0.590 | no | h6 | Bb7 | -0.81 | -0.90 |
| 172996177054 | 25 | 13. dxe6 | best | excellent | precision | excellent | 0.0050 | 0.443 | no | Bf4 | - | -0.81 | -1.13 |
| 172996177054 | 29 | 15. Bxe6+ | excellent | best | precision | best | 0.0000 | 0.288 | yes | Bxe6+ | Bd5 | -3.68 | -3.64 |
| 172996177054 | 32 | 16... Re8 | brilliant | good | precision | good | 0.0278 | 0.721 | no | Nac4 | - | -2.91 | -3.21 |
| 172996177054 | 33 | 17. Rxd6 | mistake | inaccuracy | precision | inaccuracy | 0.0866 | 0.307 | no | Rxe8+ | Rxe8+ | -5.00 | -4.98 |
| 172996177054 | 36 | 18... Qxd6 | great | best | precision | best | 0.0000 | 0.381 | yes | Qxd6 | - | +1.57 | +1.91 |
| 172996177054 | 38 | 19... Qb6 | inaccuracy | good | precision | good | 0.0479 | 0.395 | no | Qd7 | Qd7 | +2.23 | +2.42 |
| 172996177054 | 39 | 20. a4 | good | best | precision | best | 0.0000 | 0.649 | yes | a4 | Qe2 | +1.89 | +2.40 |
| 172996177054 | 42 | 21... Qxb5 | great | best | precision | best | 0.0000 | 0.685 | yes | Qxb5 | - | -2.79 | -3.06 |
| 172996177054 | 43 | 22. Qe6+ | best | excellent | precision | excellent | 0.0071 | 0.315 | no | Bf4 | - | -2.79 | -3.38 |
| 172996177054 | 44 | 22... Kh8 | excellent | best | precision | best | 0.0000 | 0.702 | yes | Kh8 | Kf8 | -2.59 | -3.48 |
| 172996177054 | 45 | 23. Bf4 | good | best | precision | best | 0.0000 | 0.293 | yes | Bf4 | h3 | -3.37 | -3.77 |
| 172996177054 | 52 | 26... Qa4 | best | good | precision | good | 0.0363 | 0.657 | no | Qe2 | - | -2.06 | -2.13 |
| 172996177054 | 54 | 27... Qxf4 | great | best | precision | best | 0.0000 | 0.770 | yes | Qxf4 | - | -4.49 | -5.12 |
| 172996177054 | 57 | 29. Qxe8+ | great | best | precision | best | 0.0000 | 0.843 | yes | Qxe8+ | - | +6.02 | +6.57 |
| 172996177054 | 59 | 30. Rd7+ | great | best | precision | best | 0.0000 | 0.827 | yes | Rd7+ | - | +6.02 | +6.31 |
| 172996177054 | 61 | 31. Qf8+ | great | best | precision | best | 0.0000 | 0.822 | yes | Qf8+ | - | +6.02 | +6.25 |
| 172996177054 | 65 | 33. Qe7+ | inaccuracy | good | precision | good | 0.0220 | 0.800 | no | h4+ | h4+ | +3.88 | +4.34 |
| 172996177054 | 66 | 33... Kh6 | mistake | inaccuracy | precision | inaccuracy | 0.0726 | 0.250 | no | Kf5 | Kf5 | +6.10 | +6.41 |
| 172996177054 | 67 | 34. Rxe5 | great | good | precision | good | 0.0235 | 0.836 | no | g3 | - | +6.10 | +6.86 |
| 173068943088 | 7 | 4. c3 | good | excellent | precision | excellent | 0.0162 | 0.543 | no | d4 | O-O | +0.38 | +0.51 |
| 173068943088 | 8 | 4... Bc5 | inaccuracy | good | precision | good | 0.0476 | 0.470 | no | Nf6 | Nf6 | +1.49 | +1.34 |
| 173068943088 | 12 | 6... Bb4+ | inaccuracy | good | precision | good | 0.0375 | 0.446 | no | Bb6 | Bb6 | +1.68 | +1.56 |
| 173068943088 | 14 | 7... Nf6 | excellent | best | precision | best | 0.0000 | 0.413 | yes | Nf6 | Nge7 | +1.74 | +1.56 |
| 173068943088 | 18 | 9... a6 | miss | mistake | precision | mistake | 0.1246 | 0.543 | no | Bxc3 | Bxc3 | +1.54 | +1.41 |
| 173068943088 | 19 | 10. e5 | best | excellent | precision | excellent | 0.0091 | 0.581 | no | d5 | - | +1.54 | +1.32 |
| 173068943088 | 20 | 10... Nh7 | excellent | good | precision | good | 0.0220 | 0.424 | no | Bxc3 | Bxc3 | +1.72 | +1.74 |
| 173068943088 | 25 | 13. exd6 | good | excellent | precision | excellent | 0.0191 | 0.535 | no | Qc3 | Qc3 | +0.26 | +0.28 |
| 173068943088 | 34 | 17... Rxf3 | miss | mistake | precision | mistake | 0.1075 | 0.607 | no | Re8 | Re8 | +0.03 | +0.00 |
| 173068943088 | 39 | 20. Nxf6+ | great | best | precision | best | 0.0000 | 0.726 | yes | Nxf6+ | - | +4.22 | +4.54 |
| 173068943088 | 43 | 22. Bf5 | inaccuracy | good | precision | good | 0.0480 | 0.737 | no | Qf5 | Qf5 | +3.23 | +3.44 |
| 173068943088 | 45 | 23. Bd7 | great | best | precision | best | 0.0000 | 0.685 | yes | Bd7 | - | +3.23 | +3.46 |
| 173068943088 | 47 | 24. gxh5 | excellent | best | precision | best | 0.0000 | 0.730 | yes | gxh5 | Qg5 | +3.65 | +3.93 |
| 173068943088 | 49 | 25. Qg5+ | great | best | precision | best | 0.0000 | 0.869 | yes | Qg5+ | - | +7.34 | +8.26 |
| 173068943088 | 52 | 26... Ke7 | great | best | precision | best | 0.0000 | 0.500 | yes | Ke7 | - | 0.00 | +0.00 |
| 173068943088 | 54 | 27... Rg8+ | great | best | precision | best | 0.0000 | 1.000 | yes | Rg8+ | - | -M3 | -M3 |
| 173068943088 | 58 | 29... Qxa1 | great | best | precision | best | 0.0000 | 0.741 | yes | Qxa1 | - | -4.27 | -4.72 |
| 173068943088 | 64 | 32... Rxe8+ | great | best | precision | best | 0.0000 | 1.000 | yes | Rxe8+ | - | - | -M11 |
| 173570784620 | 5 | 3. Bc4 | book | excellent | precision | excellent | 0.0120 | 0.525 | no | d4 | - | +0.20 | +0.20 |
| 173570784620 | 6 | 3... Nf6 | book | best | precision | best | 0.0000 | 0.487 | yes | Nf6 | - | +0.20 | +0.17 |
| 173570784620 | 7 | 4. Nc3 | book | best | precision | best | 0.0000 | 0.511 | yes | Nc3 | - | +0.20 | +0.16 |
| 173570784620 | 18 | 9... Rd8 | inaccuracy | good | precision | good | 0.0443 | 0.501 | no | h6 | h6 | +0.85 | +0.69 |
| 173570784620 | 22 | 11... Bxc4 | excellent | good | precision | good | 0.0247 | 0.488 | no | d5 | d5 | +0.52 | +0.58 |
| 173570784620 | 28 | 14... Qe6 | good | excellent | precision | excellent | 0.0171 | 0.414 | no | Nb8 | Re8 | +1.47 | +1.70 |
| 173570784620 | 29 | 15. b3 | inaccuracy | good | precision | good | 0.0425 | 0.606 | no | f4 | f4 | +0.92 | +1.05 |
| 173570784620 | 30 | 15... Re8 | good | excellent | precision | excellent | 0.0137 | 0.434 | no | Rf8 | Nxe4 | +1.27 | +1.48 |
| 173570784620 | 36 | 18... Nxg3 | excellent | good | precision | good | 0.0337 | 0.697 | no | Qxc3 | Qxc3 | -2.74 | -2.92 |
| 173570784620 | 42 | 21... Ne5 | best | excellent | precision | excellent | 0.0000 | 0.720 | no | Qxc3 | - | -3.43 | -3.80 |
| 173570784620 | 46 | 23... Qxf3 | best | excellent | precision | excellent | 0.0016 | 0.292 | no | Qh4 | - | +3.50 | +3.52 |
| 173570784620 | 54 | 27... Rf8 | best | excellent | precision | excellent | 0.0173 | 0.262 | no | Rd8 | - | +4.08 | +4.25 |
| 173570784620 | 55 | 28. Ne7+ | best | excellent | precision | excellent | 0.0078 | 0.746 | no | Re5 | - | +4.08 | +4.10 |
| 173570784620 | 61 | 31. Nc6 | good | excellent | precision | excellent | 0.0192 | 0.773 | no | Kg3 | Nd5 | +4.31 | +4.41 |
| 173570784620 | 63 | 32. Re8# | great | best | precision | best | 0.0000 | 1.000 | yes | Re8# | - | - | # |
| 173618554654 | 9 | 5. exd5 | excellent | best | precision | best | 0.0000 | 0.475 | yes | exd5 | Bd3 | -0.39 | -0.44 |
| 173618554654 | 14 | 7... d3 | inaccuracy | good | precision | good | 0.0435 | 0.590 | no | a6 | a6 | -0.80 | -0.72 |
| 173618554654 | 18 | 9... Bg4 | good | best | precision | best | 0.0000 | 0.493 | yes | Bg4 | a6 | +0.77 | +0.74 |
| 173618554654 | 28 | 14... Qxb2 | mistake | inaccuracy | precision | inaccuracy | 0.0635 | 0.245 | no | Bc5 | Qb4 | +5.77 | +5.78 |
| 173618554654 | 29 | 15. Bf5+ | great | best | precision | best | 0.0000 | 0.819 | yes | Bf5+ | - | +5.77 | +6.18 |
| 173620121124 | 11 | 6. Nc3 | good | excellent | precision | excellent | 0.0019 | 0.584 | no | Bd2 | Bd2 | +1.21 | +1.21 |
| 173620121124 | 12 | 6... c6 | inaccuracy | good | precision | good | 0.0263 | 0.422 | no | Ne7 | Ne7 | +1.79 | +1.63 |
| 173620121124 | 13 | 7. a3 | inaccuracy | good | precision | good | 0.0441 | 0.604 | no | Bd2 | Bd2 | +0.78 | +0.93 |
| 173620121124 | 14 | 7... Bxc3+ | great | best | precision | best | 0.0000 | 0.440 | yes | Bxc3+ | - | +0.78 | +0.93 |
| 173620121124 | 16 | 8... Nf6 | inaccuracy | good | precision | good | 0.0323 | 0.440 | no | Ne7 | Ne7 | +1.49 | +1.44 |
| 173620121124 | 18 | 9... Nxe4 | great | best | precision | best | 0.0000 | 0.536 | yes | Nxe4 | - | -0.61 | -0.83 |
| 173620121124 | 20 | 10... Nxc3 | inaccuracy | mistake | precision | mistake | 0.1200 | 0.548 | no | d5 | d5 | +0.90 | +1.12 |
| 173620121124 | 22 | 11... Qe7+ | miss | mistake | precision | mistake | 0.1980 | 0.577 | no | Nd5 | Nd5 | +1.85 | +1.91 |
| 173620121124 | 23 | 12. Qxe7+ | inaccuracy | good | precision | good | 0.0379 | 0.621 | no | Be3 | Be3 | +1.25 | +1.25 |
| 173620121124 | 26 | 13... Nb3 | great | best | precision | best | 0.0000 | 0.413 | yes | Nb3 | - | +1.25 | +1.36 |
| 173620121124 | 27 | 14. Bxc3 | brilliant | best | precision | best | 0.0000 | 0.587 | yes | Bxc3 | - | +1.25 | +1.30 |
| 173620121124 | 30 | 15... Kd8 | miss | blunder | precision | blunder | 0.2082 | 0.675 | no | d6 | d6 | +0.80 | +0.24 |
| 173620121124 | 33 | 17. Kd1 | great | best | precision | best | 0.0000 | 0.461 | yes | Kd1 | - | -0.65 | -0.31 |
| 173620121124 | 38 | 19... Bh5 | mistake | inaccuracy | precision | inaccuracy | 0.0674 | 0.629 | no | Re3 | Re3 | -0.81 | -0.88 |
| 173620121124 | 40 | 20... Re3 | best | excellent | precision | excellent | 0.0070 | 0.566 | no | Bg6 | - | -1.01 | -1.00 |
| 173620121124 | 41 | 21. Kc2 | inaccuracy | good | precision | good | 0.0316 | 0.436 | no | Bxh7 | Bxh7 | -1.70 | -1.63 |
| 173620121124 | 42 | 21... Bg6 | great | best | precision | best | 0.0000 | 0.604 | yes | Bg6 | - | -1.70 | -1.58 |
| 173620121124 | 55 | 28. Re1 | good | excellent | precision | excellent | 0.0120 | 0.420 | no | Bc1 | Bc1 | -1.57 | -1.44 |
| 173620121124 | 57 | 29. Ne6+ | good | best | precision | best | 0.0000 | 0.532 | yes | Ne6+ | Bc1 | 0.00 | +0.14 |
| 173620121124 | 58 | 29... Kd7 | great | best | precision | best | 0.0000 | 0.491 | yes | Kd7 | - | 0.00 | +0.06 |
| 173620121124 | 59 | 30. Nxg7 | mistake | inaccuracy | precision | inaccuracy | 0.0943 | 0.504 | no | Nc5+ | Bc1 | -1.48 | -1.41 |
| 173620121124 | 66 | 33... Kb6 | good | best | precision | best | 0.0000 | 0.346 | no | Kb7 | Kd7 | +1.96 | +2.30 |
| 173620121124 | 67 | 34. Bc5+ | great | best | precision | best | 0.0000 | 0.645 | yes | Bc5+ | - | +1.96 | +2.29 |
| 173620121124 | 68 | 34... Ka6 | excellent | inaccuracy | precision | inaccuracy | 0.0532 | 0.356 | no | Kb7 | Kb7 | +1.98 | +2.67 |
| 173620121124 | 82 | 41... Rhe2 | inaccuracy | good | precision | good | 0.0434 | 0.538 | no | Rf2 | h4 | +0.43 | +0.08 |
| 173667762936 | 11 | 6. Kf1 | book | best | precision | best | 0.0000 | 0.575 | yes | Kf1 | - | +0.76 | +1.12 |
| 173667762936 | 12 | 6... Qe7 | book | best | precision | best | 0.0000 | 0.425 | yes | Qe7 | - | +0.76 | +1.10 |
| 173667762936 | 13 | 7. Nxh8 | book | best | precision | best | 0.0000 | 0.573 | yes | Nxh8 | - | +0.76 | +1.37 |
| 173667762936 | 14 | 7... d5 | book | best | precision | best | 0.0000 | 0.409 | yes | d5 | - | +0.76 | +0.91 |
| 173667762936 | 15 | 8. exd5 | book | best | precision | best | 0.0000 | 0.561 | yes | exd5 | - | +0.76 | +1.10 |
| 173667762936 | 16 | 8... Bg4 | book | good | precision | good | 0.0351 | 0.427 | no | Nd4 | - | +1.79 | +1.56 |
| 173667762936 | 17 | 9. Be2 | great | best | precision | best | 0.0000 | 0.603 | yes | Be2 | - | +1.79 | +1.37 |
| 173667762936 | 18 | 9... Bxe2+ | great | best | precision | best | 0.0000 | 0.409 | yes | Bxe2+ | - | +1.79 | +1.28 |
| 173667762936 | 21 | 11. Qc4 | mistake | inaccuracy | precision | inaccuracy | 0.0951 | 0.591 | no | Qxf2 | Qxf2 | -1.01 | -0.06 |
| 173667762936 | 22 | 11... Ne4 | inaccuracy | excellent | precision | excellent | 0.0040 | 0.504 | no | O-O-O | O-O-O | 0.00 | +0.00 |
| 173667762936 | 24 | 12... Qf6 | brilliant | best | precision | best | 0.0000 | 0.851 | yes | Qf6 | - | -6.21 | -6.80 |
| 173667762936 | 32 | 16... b5 | mistake | inaccuracy | precision | inaccuracy | 0.0703 | 0.215 | no | Qxg2 | Qxg2 | +5.50 | +6.60 |
| 173667762936 | 34 | 17... Ne2+ | great | best | precision | best | 0.0000 | 0.719 | yes | Ne2+ | - | -3.37 | -3.43 |
| 173667762936 | 35 | 18. Kd1 | best | excellent | precision | excellent | 0.0022 | 0.284 | no | Kd2 | - | -3.37 | -3.41 |
| 173667762936 | 38 | 19... Nxc3+ | best | good | precision | good | 0.0206 | 0.816 | no | Ng1 | - | -4.93 | -5.27 |
| 173667762936 | 41 | 21. Rc1 | mistake | good | precision | good | 0.0323 | 0.176 | no | Rb1 | Rb1 | -6.36 | -6.99 |
| 173667762936 | 42 | 21... O-O-O | good | excellent | precision | excellent | 0.0119 | 0.868 | no | Qd4+ | Qd4+ | -5.54 | -6.63 |
| 173667762936 | 43 | 22. Nf7 | mistake | excellent | precision | excellent | 0.0185 | 0.144 | no | Rf1 | Rb1 | -7.21 | -7.19 |
| 173667762936 | 45 | 23. Nxe5 | inaccuracy | mistake | precision | mistake | 0.1248 | 0.125 | no | Rf1 | Rf1 | -M6 | -M6 |
| 173667762936 | 48 | 24... Rxf1+ | great | best | precision | best | 0.0000 | 1.000 | yes | Rxf1+ | - | -M5 | -M13 |
| 173667762936 | 52 | 26... Qxc1 | great | excellent | precision | excellent | 0.0000 | 1.000 | no | Rxc1 | - | -M7 | -M10 |
| 173807034866 | 13 | 7. Nf3 | great | best | precision | best | 0.0000 | 0.480 | yes | Nf3 | - | -0.34 | -0.39 |
| 173807034866 | 18 | 9... Bg4 | great | best | precision | best | 0.0000 | 0.729 | yes | Bg4 | - | -4.13 | -4.04 |
| 173807034866 | 31 | 16. Bb3 | excellent | good | precision | good | 0.0219 | 0.664 | no | Ba2 | Ba2 | +2.27 | +2.30 |
| 173807034866 | 32 | 16... Rfe8 | excellent | good | precision | good | 0.0253 | 0.358 | no | c4 | c4 | +2.56 | +2.74 |
| 173807034866 | 33 | 17. g4 | good | inaccuracy | precision | inaccuracy | 0.0514 | 0.667 | no | d4 | d4 | +1.81 | +1.86 |
| 173807034866 | 35 | 18. d3 | excellent | good | precision | good | 0.0211 | 0.669 | no | d4 | d4 | +2.29 | +2.35 |
| 173807034866 | 36 | 18... b5 | inaccuracy | good | precision | good | 0.0413 | 0.355 | no | c4 | c4 | +3.19 | +3.08 |
| 173807034866 | 37 | 19. f4 | mistake | inaccuracy | precision | inaccuracy | 0.0983 | 0.686 | no | axb5 | axb5 | +1.27 | +1.40 |
| 173807034866 | 38 | 19... Qh4 | miss | inaccuracy | precision | inaccuracy | 0.0861 | 0.412 | no | c4 | c4 | +2.69 | +2.86 |
| 173807034866 | 40 | 20... Qxg4+ | great | best | precision | best | 0.0000 | 0.578 | yes | Qxg4+ | - | -0.89 | -1.01 |
| 173807034866 | 41 | 21. Kh1 | mistake | inaccuracy | precision | inaccuracy | 0.0742 | 0.436 | no | Qg3 | Qg3 | -2.50 | -3.06 |
| 173807034866 | 48 | 24... Re2 | great | best | precision | best | 0.0000 | 1.000 | yes | Re2 | - | -M4 | -M4 |
| 173855642488 | 5 | 3. Bc4 | excellent | good | precision | good | 0.0209 | 0.545 | no | d4 | d4 | +0.32 | +0.40 |
| 173855642488 | 6 | 3... Nf6 | good | excellent | precision | excellent | 0.0146 | 0.475 | no | c5 | c5 | +0.67 | +0.63 |
| 173855642488 | 8 | 4... O-O | good | inaccuracy | precision | inaccuracy | 0.0616 | 0.531 | no | Nxe4 | Nxe4 | +0.33 | +0.57 |
| 173855642488 | 9 | 5. d4 | good | inaccuracy | precision | inaccuracy | 0.0502 | 0.536 | no | e5 | e5 | -0.21 | -0.22 |
| 173855642488 | 11 | 6. O-O | book | excellent | precision | excellent | 0.0045 | 0.517 | no | Qe2 | - | +0.27 | +0.25 |
| 173855642488 | 18 | 9... c6 | inaccuracy | good | precision | good | 0.0480 | 0.482 | no | Nc5 | Nc5 | +1.22 | +1.05 |
| 173855642488 | 20 | 10... cxd5 | best | excellent | precision | excellent | 0.0006 | 0.451 | no | Qc7 | - | +0.76 | +0.81 |
| 173855642488 | 25 | 13. Bb3 | good | excellent | precision | excellent | 0.0140 | 0.513 | no | Bf1 | Ba2 | -0.02 | -0.02 |
| 173855642488 | 28 | 14... h6 | blunder | mistake | precision | mistake | 0.1713 | 0.503 | no | Re8 | Re8 | +2.73 | +2.75 |
| 173855642488 | 29 | 15. Bxe7 | great | best | precision | best | 0.0000 | 0.668 | yes | Bxe7 | - | +2.73 | +2.54 |
| 173855642488 | 33 | 17. Bxf8 | mistake | inaccuracy | precision | inaccuracy | 0.0795 | 0.706 | no | Re3 | Re3 | +1.37 | +1.51 |
| 173855642488 | 37 | 19. Bxd6 | good | excellent | precision | excellent | 0.0173 | 0.594 | no | Bxg7 | Bxg7 | +1.05 | +1.33 |
| 173855642488 | 40 | 20... Rxd6 | good | excellent | precision | excellent | 0.0159 | 0.742 | no | Bxf3 | Bxf3 | -3.70 | -3.77 |
| 173855642488 | 48 | 24... Nb4 | best | excellent | precision | excellent | 0.0062 | 0.797 | no | Nc7 | - | -5.15 | -5.14 |
| 173855642488 | 49 | 25. f3 | excellent | good | precision | good | 0.0306 | 0.213 | no | Nf3 | h3 | -5.45 | -5.90 |
| 173855642488 | 50 | 25... Bxd5 | best | excellent | precision | excellent | 0.0065 | 0.818 | no | Bd3 | - | -5.45 | -5.80 |
| 173855642488 | 51 | 26. Bxd5 | inaccuracy | good | precision | good | 0.0368 | 0.186 | no | g3 | Bb5 | -6.57 | -6.84 |
| 173855642488 | 56 | 28... Nd3+ | best | excellent | precision | excellent | 0.0131 | 0.850 | no | Bxb2 | - | -6.46 | -6.59 |
| 173855642488 | 58 | 29... Nxb2 | good | excellent | precision | excellent | 0.0107 | 0.844 | no | Be5+ | Be5+ | -5.81 | -6.32 |
| 173855642488 | 63 | 32. f5 | best | excellent | precision | excellent | 0.0197 | 0.137 | no | Re7 | - | -6.77 | -7.42 |
| 173855642488 | 66 | 33... Rd4+ | inaccuracy | good | precision | good | 0.0387 | 0.903 | no | a2 | gxf5+ | -6.14 | -7.49 |
| 173855642488 | 67 | 34. Kg3 | good | best | precision | best | 0.0000 | 0.129 | yes | Kg3 | Kh3 | -7.26 | -7.57 |
| 173855642488 | 68 | 34... a2 | best | excellent | precision | excellent | 0.0037 | 0.873 | no | Rd3+ | - | -7.26 | -7.73 |
| 173904334944 | 10 | 5... d6 | good | inaccuracy | precision | inaccuracy | 0.0564 | 0.597 | no | Nf6 | Qh4 | -0.62 | -0.62 |
| 173904334944 | 11 | 6. b4 | excellent | good | precision | good | 0.0242 | 0.459 | no | Nf3 | Nf3 | -0.82 | -0.84 |
| 173904334944 | 13 | 7. Na3 | mistake | inaccuracy | precision | inaccuracy | 0.0624 | 0.437 | no | Nf3 | Nf3 | -2.05 | -1.94 |
| 173904334944 | 21 | 11. Bd3 | mistake | inaccuracy | precision | inaccuracy | 0.0844 | 0.454 | no | Kf2 | Kf2 | -2.02 | -2.02 |
| 173904334944 | 23 | 12. Nd2 | inaccuracy | mistake | precision | mistake | 0.1221 | 0.371 | no | Ne3 | Ne3 | -3.64 | -4.18 |
| 173904334944 | 28 | 14... Ne5 | excellent | best | precision | best | 0.0000 | 0.780 | yes | Ne5 | Qd6 | -3.81 | -4.03 |
| 173904334944 | 36 | 18... Rxe4+ | great | excellent | precision | excellent | 0.0115 | 0.874 | no | Nxe4 | - | -6.31 | -7.29 |
| 173905398948 | 9 | 5. d4 | best | excellent | precision | excellent | 0.0006 | 0.605 | no | Nf3 | - | +1.56 | +1.66 |
| 173905398948 | 10 | 5... Bb7 | good | excellent | precision | excellent | 0.0026 | 0.389 | no | c6 | c6 | +1.83 | +1.77 |
| 173905398948 | 11 | 6. Nf3 | excellent | best | precision | best | 0.0000 | 0.618 | yes | Nf3 | d5 | +1.69 | +1.68 |
| 173905398948 | 17 | 9. Bb5 | inaccuracy | good | precision | good | 0.0474 | 0.665 | no | Bf4 | Nb5 | +1.54 | +1.76 |
| 173905398948 | 18 | 9... O-O-O | excellent | good | precision | good | 0.0215 | 0.383 | no | e5 | a6 | +1.63 | +2.10 |
| 173905398948 | 22 | 11... Qxd6 | good | excellent | precision | excellent | 0.0188 | 0.559 | no | exd6 | exd6 | -0.36 | -0.60 |
| 173905398948 | 23 | 12. Nd5 | blunder | mistake | precision | mistake | 0.1710 | 0.459 | no | Qe2 | Be3 | -3.25 | -3.33 |
| 173905398948 | 26 | 13... Qxd5 | great | best | precision | best | 0.0000 | 0.775 | yes | Qxd5 | - | -4.35 | -4.51 |
| 173905398948 | 27 | 14. Qe2 | excellent | best | precision | best | 0.0000 | 0.227 | yes | Qe2 | O-O | -4.71 | -4.64 |
| 173905398948 | 29 | 15. Bc4 | mistake | excellent | precision | excellent | 0.0108 | 0.243 | no | O-O | O-O | -5.24 | -4.29 |
| 173905398948 | 30 | 15... Qd4 | inaccuracy | good | precision | good | 0.0228 | 0.762 | no | Qf5 | Qf5 | -4.04 | -3.84 |
| 173905398948 | 32 | 16... Qxb2 | excellent | good | precision | good | 0.0204 | 0.768 | no | Bd6 | Bd6 | -3.98 | -4.30 |
| 173905398948 | 36 | 18... Bd6 | excellent | good | precision | good | 0.0394 | 0.766 | no | a5 | a5 | -3.86 | -3.78 |
| 173905398948 | 42 | 21... Qd2 | inaccuracy | good | precision | good | 0.0346 | 0.787 | no | Qc3 | Nf6 | -3.00 | -4.10 |
| 173905398948 | 43 | 22. axb6 | inaccuracy | excellent | precision | excellent | 0.0148 | 0.248 | no | Rfd1 | Rad1 | -4.47 | -4.53 |
| 173905398948 | 53 | 27. Rxb7+ | great | best | precision | best | 0.0000 | 0.611 | yes | Rxb7+ | - | +1.53 | +1.59 |
| 173905398948 | 55 | 28. Rb2+ | great | best | precision | best | 0.0000 | 0.811 | yes | Rb2+ | - | +5.68 | +5.43 |
| 174188274588 | 11 | 6. h3 | best | excellent | precision | excellent | 0.0034 | 0.523 | no | O-O | - | +0.36 | +0.43 |
| 174188274588 | 13 | 7. g4 | best | excellent | precision | excellent | 0.0061 | 0.563 | no | a3 | - | +0.90 | +0.79 |
| 174188274588 | 17 | 9. Bxf6 | excellent | best | precision | best | 0.0000 | 0.585 | yes | Bxf6 | h4 | +1.28 | +1.28 |
| 174188274588 | 25 | 13. Rg1 | miss | mistake | precision | mistake | 0.1214 | 0.588 | no | gxh5 | gxh5 | -0.54 | -0.49 |
| 174188274588 | 26 | 13... c6 | excellent | good | precision | good | 0.0214 | 0.534 | no | Nd7 | Nd7 | -0.44 | -0.13 |
| 174188274588 | 27 | 14. Qf3 | excellent | good | precision | good | 0.0283 | 0.491 | no | Ne2 | Ne2 | -0.61 | -0.54 |
| 174188274588 | 28 | 14... Nd7 | excellent | best | precision | best | 0.0000 | 0.537 | yes | Nd7 | b5 | -0.54 | -0.56 |
| 174188274588 | 35 | 18. Rg3 | good | excellent | precision | excellent | 0.0141 | 0.421 | no | Ng1 | a4 | -1.57 | -1.36 |
| 174188274588 | 36 | 18... Bh5 | inaccuracy | good | precision | good | 0.0371 | 0.593 | no | Bxe2 | Bxe2 | -0.67 | -0.78 |
| 174188274588 | 37 | 19. O-O-O | blunder | mistake | precision | mistake | 0.1950 | 0.446 | no | f3 | f3 | -3.51 | -3.95 |
| 174188274588 | 38 | 19... d5 | great | excellent | precision | excellent | 0.0154 | 0.749 | no | Bxe2 | - | -3.51 | -4.01 |
| 174188274588 | 39 | 20. exd5 | good | excellent | precision | excellent | 0.0000 | 0.248 | no | Rdg1 | Rh1 | -3.94 | -3.89 |
| 174188274588 | 40 | 20... cxd5 | excellent | best | precision | best | 0.0000 | 0.746 | yes | cxd5 | Bxe2 | -3.77 | -4.25 |
| 174188274588 | 42 | 21... Bxe2 | great | best | precision | best | 0.0000 | 0.773 | yes | Bxe2 | - | -4.06 | -4.44 |
| 174188274588 | 43 | 22. Rdg1 | excellent | best | precision | best | 0.0000 | 0.227 | yes | Rdg1 | Re1 | -4.15 | -4.23 |
| 174188274588 | 48 | 24... Kg7 | best | excellent | precision | excellent | 0.0013 | 0.807 | no | Rad8 | - | -5.10 | -5.11 |
| 174188274588 | 52 | 26... Rad8+ | inaccuracy | good | precision | good | 0.0418 | 0.857 | no | Ne4+ | Ne4+ | -5.09 | -5.36 |
| 174336461820 | 2 | 1... e5 | book | best | precision | best | 0.0000 | 0.489 | yes | e5 | - | +0.07 | +0.10 |
| 174336461820 | 8 | 4... Bb6 | excellent | best | precision | best | 0.0000 | 0.525 | yes | Bb6 | Be7 | -0.20 | -0.41 |
| 174336461820 | 9 | 5. a4 | best | excellent | precision | excellent | 0.0033 | 0.473 | no | d4 | - | -0.20 | -0.35 |
| 174336461820 | 11 | 6. Ba3 | good | excellent | precision | excellent | 0.0099 | 0.473 | no | b5 | b5 | -0.58 | -0.49 |
| 174336461820 | 18 | 9... d5 | excellent | best | precision | best | 0.0000 | 0.413 | yes | d5 | e4 | +1.41 | +1.29 |
| 174336461820 | 24 | 12... Qe7 | good | inaccuracy | precision | inaccuracy | 0.0581 | 0.353 | no | Bxd4 | Bxd4 | +3.02 | +3.28 |
| 174336461820 | 32 | 16... Qe4 | good | best | precision | best | 0.0000 | 0.833 | yes | Qe4 | Nxc6 | -2.91 | -6.47 |
| 174336461820 | 33 | 17. f3 | blunder | mistake | precision | mistake | 0.1520 | 0.152 | no | Qf1 | Ne7+ | -M2 | -M2 |
| 174468507028 | 5 | 3. Bc4 | miss | inaccuracy | precision | inaccuracy | 0.0821 | 0.600 | no | Nxe5 | Nxe5 | +0.29 | +0.28 |
| 174468507028 | 8 | 4... Bg4 | inaccuracy | good | precision | good | 0.0439 | 0.478 | no | Nf6 | Nf6 | +1.04 | +1.04 |
| 174468507028 | 9 | 5. d4 | excellent | best | precision | best | 0.0000 | 0.566 | yes | d4 | Qb3 | +1.00 | +0.78 |
| 174468507028 | 13 | 7. dxc5 | great | best | precision | best | 0.0000 | 0.783 | yes | dxc5 | - | +5.01 | +4.96 |
| 174468507028 | 16 | 8... Nbd7 | best | excellent | precision | excellent | 0.0014 | 0.228 | no | a6 | - | +5.04 | +4.75 |
| 174468507028 | 27 | 14. Rfe1 | good | excellent | precision | excellent | 0.0194 | 0.736 | no | Bd3 | Be2 | +3.70 | +3.62 |
| 174468507028 | 31 | 16. a5 | good | excellent | precision | excellent | 0.0102 | 0.731 | no | Be2 | Be2 | +3.75 | +3.70 |
| 174468507028 | 34 | 17... c4 | great | best | precision | best | 0.0000 | 0.489 | yes | c4 | - | +0.27 | +0.25 |
| 174468507028 | 35 | 18. Bxc4 | good | excellent | precision | excellent | 0.0160 | 0.516 | no | Nc1 | Nc1 | -0.10 | -0.09 |
| 174468507028 | 37 | 19. Nd2 | great | best | precision | best | 0.0000 | 0.499 | yes | Nd2 | - | -0.10 | +0.00 |
| 174468507028 | 38 | 19... Rxb2 | good | excellent | precision | excellent | 0.0148 | 0.500 | no | Qc5 | Qc5 | +0.36 | +0.28 |
| 174468507028 | 46 | 23... Qc5 | best | excellent | precision | excellent | 0.0018 | 0.396 | no | Qc7 | - | +1.64 | +1.81 |
| 174468507028 | 47 | 24. Qg3 | excellent | best | precision | best | 0.0000 | 0.614 | yes | Qg3 | Rd6 | +1.63 | +2.04 |
| 174468507028 | 49 | 25. Nxh6+ | great | best | precision | best | 0.0000 | 0.742 | yes | Nxh6+ | - | +3.72 | +4.26 |
| 174468507028 | 50 | 25... Kg7 | blunder | mistake | precision | mistake | 0.1835 | 0.251 | no | Kh8 | Kh8 | +8.80 | +11.56 |
| 183978299106 | 13 | 7. Nc3 | excellent | best | precision | best | 0.0000 | 0.516 | yes | Nc3 | Bd3 | +0.05 | +0.12 |
| 183978299106 | 20 | 10... Be6 | excellent | good | precision | good | 0.0310 | 0.503 | no | Bxe3+ | Bxe3+ | +0.40 | +0.40 |
| 183978299106 | 25 | 13. b3 | excellent | good | precision | good | 0.0406 | 0.494 | no | a3 | a3 | -0.44 | -0.73 |
| 183978299106 | 31 | 16. Bxb5 | good | inaccuracy | precision | inaccuracy | 0.0556 | 0.456 | no | Qd4 | Qc1 | -1.17 | -1.57 |
| 183978299106 | 33 | 17. Nxb5 | good | excellent | precision | excellent | 0.0131 | 0.416 | no | Qd4 | Qe3 | -1.57 | -1.59 |
| 183978299106 | 42 | 21... Qxe1+ | great | best | precision | best | 0.0000 | 0.828 | yes | Qxe1+ | - | - | -6.50 |
| 184028735740 | 9 | 5. Qxg7 | great | best | precision | best | 0.0000 | 0.469 | yes | Qxg7 | - | -0.51 | -0.43 |
| 184028735740 | 10 | 5... Rf8 | great | best | precision | best | 0.0000 | 0.528 | yes | Rf8 | - | -0.51 | -0.43 |
| 184028735740 | 13 | 7. exd5 | inaccuracy | mistake | precision | mistake | 0.1029 | 0.507 | no | Bxd5 | Bxd5 | -1.09 | -1.34 |
| 184028735740 | 18 | 9... Bxg5 | great | best | precision | best | 0.0000 | 0.743 | yes | Bxg5 | - | -3.91 | -3.96 |
| 184028735740 | 19 | 10. h4 | good | excellent | precision | excellent | 0.0158 | 0.264 | no | Nc3 | Nc3 | -4.46 | -4.64 |
| 184028735740 | 27 | 14. Qg6+ | inaccuracy | good | precision | good | 0.0465 | 0.348 | no | a3 | a3 | -3.47 | -3.24 |
| 184028735740 | 28 | 14... Kd7 | inaccuracy | good | precision | good | 0.0360 | 0.698 | no | Ke7 | Ke7 | -2.28 | -2.14 |
| 184028735740 | 30 | 15... Nd5 | best | excellent | precision | excellent | 0.0184 | 0.650 | no | Ke7 | - | -2.28 | -2.30 |
| 184028735740 | 35 | 18. Qxf6 | great | best | precision | best | 0.0000 | 0.439 | yes | Qxf6 | - | -1.23 | -1.20 |
| 184028735740 | 36 | 18... Rf8 | mistake | inaccuracy | precision | inaccuracy | 0.0989 | 0.577 | no | Qg8 | Qg8 | +0.68 | +0.57 |
| 184028735740 | 38 | 19... Nb4 | mistake | inaccuracy | precision | inaccuracy | 0.0541 | 0.447 | no | Qe8 | Qe8 | +1.85 | +1.68 |
| 184028735740 | 39 | 20. Na3 | miss | mistake | precision | mistake | 0.1089 | 0.607 | no | O-O | O-O | -0.28 | -0.03 |
| 184028735740 | 41 | 21. Kd2 | mistake | inaccuracy | precision | inaccuracy | 0.0906 | 0.479 | no | Ke2 | Ke2 | -1.71 | -2.28 |
| 184028735740 | 42 | 21... Nxc1 | miss | mistake | precision | mistake | 0.1155 | 0.643 | no | Nxf2 | Nxf2 | -0.06 | +0.00 |
| 184028735740 | 46 | 23... Qa5+ | inaccuracy | good | precision | good | 0.0413 | 0.706 | no | Rxf2+ | Rxf2+ | -2.21 | -2.70 |
| 184028735740 | 51 | 26. Rhe1 | blunder | mistake | precision | mistake | 0.1951 | 0.321 | no | Rcd1 | Rhd1 | -7.53 | -7.48 |
| 184028735740 | 57 | 29. Nd4+ | miss | blunder | precision | blunder | 0.6670 | 0.813 | no | Qxe7 | Qxe7 | -7.06 | -6.82 |
| 184028735740 | 60 | 30... cxd4 | miss | inaccuracy | precision | inaccuracy | 0.0613 | 0.584 | no | Re8 | Re8 | -0.21 | -0.35 |
| 184028735740 | 63 | 32. Qxf2 | great | best | precision | best | 0.0000 | 0.706 | yes | Qxf2 | - | +3.42 | +3.77 |
| 184028735740 | 64 | 32... Qxa4 | inaccuracy | good | precision | good | 0.0447 | 0.274 | no | Rg8 | Rg8 | +4.64 | +4.69 |
| 184028735740 | 73 | 37. Qd3+ | great | best | precision | best | 0.0000 | 0.769 | yes | Qd3+ | - | - | +6.98 |
| 184110410320 | 12 | 6... Nxf3+ | excellent | good | precision | good | 0.0261 | 0.491 | no | d6 | d6 | +0.40 | +0.43 |
| 184110410320 | 20 | 10... Bg4 | great | best | precision | best | 0.0000 | 0.652 | yes | Bg4 | - | -2.30 | -2.37 |
| 184110410320 | 21 | 11. Qg3 | best | excellent | precision | excellent | 0.0024 | 0.346 | no | Qf2 | - | -2.30 | -2.28 |
| 184110410320 | 24 | 12... exd4 | excellent | good | precision | good | 0.0208 | 0.747 | no | Nxe4 | Nxe4 | -3.59 | -3.73 |
| 184110410320 | 27 | 14. Qh3 | excellent | good | precision | good | 0.0241 | 0.248 | no | Qf3 | Qf4 | -4.43 | -4.64 |
| 184110410320 | 32 | 16... Nxc4 | great | best | precision | best | 0.0000 | 0.847 | yes | Nxc4 | - | -6.33 | -6.59 |
| 184271279368 | 5 | 3. Nf3 | book | excellent | precision | excellent | 0.0013 | 0.526 | no | e3 | - | +0.38 | +0.32 |
| 184271279368 | 6 | 3... Bf5 | book | best | precision | best | 0.0000 | 0.479 | yes | Bf5 | - | +0.46 | +0.36 |
| 184271279368 | 7 | 4. e3 | book | excellent | precision | excellent | 0.0085 | 0.524 | no | c4 | - | +0.25 | +0.24 |
| 184271279368 | 8 | 4... Nf6 | book | excellent | precision | excellent | 0.0079 | 0.484 | no | e6 | - | +0.44 | +0.37 |
| 184271279368 | 9 | 5. Bd3 | book | excellent | precision | excellent | 0.0092 | 0.524 | no | c4 | - | +0.23 | +0.20 |
| 184271279368 | 16 | 8... Ne4 | good | inaccuracy | precision | inaccuracy | 0.0537 | 0.512 | no | Bxe5 | Bxe5 | +0.50 | +0.63 |
| 184271279368 | 20 | 10... f6 | inaccuracy | good | precision | good | 0.0360 | 0.503 | no | g6 | g6 | +0.73 | +0.50 |
| 184271279368 | 23 | 12. Qxf5 | brilliant | good | precision | good | 0.0425 | 0.543 | no | Nf3 | - | 0.00 | +0.00 |
| 184271279368 | 24 | 12... fxe5 | great | best | precision | best | 0.0000 | 0.500 | yes | fxe5 | - | 0.00 | +0.00 |
| 184271279368 | 25 | 13. Qxh7+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qxh7+ | - | 0.00 | +0.00 |
| 184271279368 | 28 | 14... Qf6 | great | best | precision | best | 0.0000 | 0.664 | yes | Qf6 | - | -2.65 | -2.60 |
| 184271279368 | 31 | 16. Qxb7 | great | best | precision | best | 0.0000 | 0.528 | yes | Qxb7 | - | -0.81 | -1.05 |
| 184271279368 | 32 | 16... Nd7 | blunder | mistake | precision | mistake | 0.1943 | 0.568 | no | Kg8 | Kg8 | +1.96 | +1.96 |
| 184271279368 | 36 | 18... Kg8 | good | inaccuracy | precision | inaccuracy | 0.0508 | 0.724 | no | exd4 | exd4 | -2.77 | -2.94 |
| 184271279368 | 38 | 19... Qxf2+ | great | best | precision | best | 0.0000 | 0.894 | yes | Qxf2+ | - | -6.89 | -7.46 |
| 184449650784 | 6 | 3... Bf5 | excellent | good | precision | good | 0.0242 | 0.543 | no | Qb6 | Qb6 | -0.37 | -0.29 |
| 184449650784 | 8 | 4... f6 | excellent | good | precision | good | 0.0223 | 0.533 | no | Nd7 | Nd7 | -0.12 | -0.16 |
| 184449650784 | 11 | 6. Nf3 | best | excellent | precision | excellent | 0.0013 | 0.461 | no | e3 | - | -0.53 | -0.59 |
| 184449650784 | 15 | 8. e3 | excellent | best | precision | best | 0.0000 | 0.514 | yes | e3 | h3 | +0.19 | +0.27 |
| 184449650784 | 16 | 8... c5 | mistake | inaccuracy | precision | inaccuracy | 0.0920 | 0.482 | no | a5 | g5 | +1.61 | +1.70 |
| 184449650784 | 18 | 9... a6 | excellent | best | precision | best | 0.0000 | 0.524 | yes | a6 | g5 | -0.07 | -0.11 |
| 184449650784 | 19 | 10. Bxd7+ | good | excellent | precision | excellent | 0.0151 | 0.493 | no | Bc6 | Bc6 | -0.45 | -0.35 |
| 184449650784 | 25 | 13. Rd1 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Rd1 | Rc1 | -0.16 | +0.01 |
| 184449650784 | 28 | 14... Bc2 | excellent | best | precision | best | 0.0000 | 0.494 | yes | Bc2 | Bd3 | +0.29 | +0.24 |
| 184449650784 | 29 | 15. Re1 | best | excellent | precision | excellent | 0.0072 | 0.516 | no | Rc1 | - | +0.29 | +0.00 |
| 184449650784 | 32 | 16... Bd6 | miss | mistake | precision | mistake | 0.1554 | 0.489 | no | e4 | e4 | +2.59 | +2.64 |
| 184449650784 | 34 | 17... Rb8 | mistake | inaccuracy | precision | inaccuracy | 0.0819 | 0.444 | no | Bc7 | Bc7 | +2.13 | +2.16 |
| 184449650784 | 35 | 18. Qxa6 | great | best | precision | best | 0.0000 | 0.638 | yes | Qxa6 | - | +2.13 | +2.13 |
| 184449650784 | 37 | 19. Bxd6 | best | excellent | precision | excellent | 0.0046 | 0.683 | no | Qxd6 | - | +3.02 | +2.84 |
| 184449650784 | 40 | 20... Rxb2 | excellent | good | precision | good | 0.0314 | 0.348 | no | Rc8 | Rd8 | +2.54 | +2.67 |
| 184449650784 | 43 | 22. Qc6+ | best | excellent | precision | excellent | 0.0030 | 0.651 | no | Qa3 | - | +2.10 | +2.19 |
| 184449650784 | 51 | 26. Bxe7+ | good | excellent | precision | excellent | 0.0199 | 0.693 | no | Ba3 | Ba3 | +2.47 | +2.68 |
| 184449650784 | 55 | 28. Na3 | great | best | precision | best | 0.0000 | 0.605 | yes | Na3 | - | +1.42 | +1.44 |
| 184449650784 | 56 | 28... Bd3 | great | best | precision | best | 0.0000 | 0.407 | yes | Bd3 | - | +1.42 | +1.47 |
| 184449650784 | 61 | 31. Kg2 | mistake | inaccuracy | precision | inaccuracy | 0.0865 | 0.627 | no | e4 | e4 | +0.25 | +0.26 |
| 184449650784 | 62 | 31... Be4+ | miss | mistake | precision | mistake | 0.1026 | 0.483 | no | f5 | f5 | +1.92 | +1.86 |
| 184449650784 | 63 | 32. Kg3 | great | best | precision | best | 0.0000 | 0.620 | yes | Kg3 | - | +1.92 | +1.60 |
| 184449650784 | 64 | 32... Kf5 | mistake | blunder | precision | blunder | 0.2174 | 0.397 | no | h5 | h5 | +5.24 | +5.80 |
| 184449650784 | 67 | 34. Nd6+ | great | best | precision | best | 0.0000 | 0.854 | yes | Nd6+ | - | +6.48 | +6.74 |
| 184555832944 | 9 | 5. Nxd4 | miss | inaccuracy | precision | inaccuracy | 0.0763 | 0.607 | no | Nxe5 | Nxe5 | +0.38 | +0.28 |
| 184555832944 | 19 | 10. O-O | excellent | best | precision | best | 0.0000 | 0.464 | yes | O-O | Qe2+ | -0.61 | -0.64 |
| 184555832944 | 29 | 15. g4 | best | excellent | precision | excellent | 0.0151 | 0.282 | no | h3 | - | -3.79 | -4.04 |
| 184555832944 | 30 | 15... d5 | brilliant | excellent | precision | excellent | 0.0061 | 0.742 | no | Qg5 | - | -3.79 | -3.93 |
| 184555832944 | 33 | 17. Re5 | excellent | good | precision | good | 0.0285 | 0.253 | no | Qg3 | Qf4 | -4.11 | -4.73 |
| 184555832944 | 34 | 17... Rh3 | excellent | best | precision | best | 0.0000 | 0.775 | yes | Rh3 | Rh5 | -4.04 | -4.30 |
| 184555832944 | 35 | 18. Qg2 | best | excellent | precision | excellent | 0.0077 | 0.245 | no | Qf4 | - | -4.04 | -4.68 |
| 184555832944 | 43 | 22. Re7 | good | excellent | precision | excellent | 0.0084 | 0.280 | no | c4 | f4 | -3.68 | -3.89 |
| 184555832944 | 45 | 23. R7e5 | good | inaccuracy | precision | inaccuracy | 0.0515 | 0.276 | no | Rxb7 | Rxb7 | -4.24 | -4.73 |
| 184555832944 | 46 | 23... Rah8 | brilliant | best | precision | best | 0.0000 | 0.775 | yes | Rah8 | - | -4.03 | -4.72 |
| 184555832944 | 47 | 24. Rxf5 | mistake | excellent | precision | excellent | 0.0121 | 0.225 | no | f4 | f4 | -5.16 | -4.99 |
| 184797463690 | 7 | 4. Nc3 | excellent | good | precision | good | 0.0218 | 0.562 | no | d4 | h3 | +0.63 | +0.71 |
| 184797463690 | 10 | 5... Bxf3 | best | excellent | precision | excellent | 0.0020 | 0.459 | no | Be6 | - | +0.63 | +0.51 |
| 184797463690 | 14 | 7... Be7 | good | excellent | precision | excellent | 0.0112 | 0.438 | no | b5 | b5 | +1.17 | +0.92 |
| 184797463690 | 15 | 8. O-O | good | excellent | precision | excellent | 0.0185 | 0.561 | no | a3 | a3 | +0.70 | +0.64 |
| 184797463690 | 17 | 9. Bg5 | excellent | good | precision | good | 0.0266 | 0.549 | no | a4 | a3 | +0.38 | +0.33 |
| 184797463690 | 26 | 13... a5 | excellent | best | precision | best | 0.0000 | 0.461 | yes | a5 | Qg6 | +0.72 | +0.58 |
| 184797463690 | 28 | 14... a4 | great | best | precision | best | 0.0000 | 0.689 | yes | a4 | - | -2.94 | -3.03 |
| 184797463690 | 29 | 15. Nh5 | good | excellent | precision | excellent | 0.0118 | 0.308 | no | h4 | Bxf7+ | -3.35 | -3.24 |
| 184797463690 | 33 | 17. Qh4 | best | excellent | precision | excellent | 0.0016 | 0.266 | no | Qe2 | - | -3.93 | -3.81 |
| 184797463690 | 35 | 18. Nxf6+ | good | inaccuracy | precision | inaccuracy | 0.0589 | 0.296 | no | Ng3 | Ng3 | -4.20 | -4.29 |
| 184797463690 | 36 | 18... Qxf6 | excellent | best | precision | best | 0.0000 | 0.759 | yes | Qxf6 | Rxf6 | -4.18 | -4.33 |
| 184797463690 | 42 | 21... exf4 | best | excellent | precision | excellent | 0.0088 | 0.763 | no | a3 | - | -4.28 | -4.22 |
| 184797463690 | 46 | 23... Qf6 | best | excellent | precision | excellent | 0.0118 | 0.764 | no | a3 | - | -4.28 | -4.15 |
| 184797463690 | 47 | 24. Qg4 | best | excellent | precision | excellent | 0.0132 | 0.248 | no | Qxf6 | - | -4.28 | -4.23 |
| 184797463690 | 48 | 24... Rf8 | mistake | inaccuracy | precision | inaccuracy | 0.0890 | 0.756 | no | Qe7 | Qe7 | -2.28 | -2.60 |
| 184797463690 | 50 | 25... Qd4+ | great | excellent | precision | excellent | 0.0022 | 0.886 | no | Qxf1+ | - | -6.98 | -7.07 |
| 184797463690 | 51 | 26. Kh1 | mistake | inaccuracy | precision | inaccuracy | 0.0549 | 0.131 | no | Kh2 | Kh2 | -8.66 | -9.12 |
| 184797463690 | 54 | 27... Rf7 | good | inaccuracy | precision | inaccuracy | 0.0534 | 0.925 | no | Qg1+ | Qg1+ | -6.92 | -7.14 |
| 184809655978 | 12 | 6... Bd7 | good | excellent | precision | excellent | 0.0120 | 0.517 | no | O-O | h6 | +0.15 | -0.08 |
| 184809655978 | 14 | 7... Nd4 | inaccuracy | good | precision | good | 0.0488 | 0.508 | no | a6 | a6 | +0.74 | +0.61 |
| 184809655978 | 15 | 8. Bxd7+ | best | excellent | precision | excellent | 0.0067 | 0.541 | no | Nxd4 | - | +0.74 | +0.56 |
| 184809655978 | 17 | 9. c3 | inaccuracy | good | precision | good | 0.0468 | 0.533 | no | Nxd4 | Bxf6 | -0.30 | -0.20 |
| 184809655978 | 18 | 9... Nxf3+ | good | excellent | precision | excellent | 0.0167 | 0.513 | no | Ne6 | Ne6 | +0.22 | +0.14 |
| 184809655978 | 23 | 12. Qxf6 | excellent | best | precision | best | 0.0000 | 0.578 | yes | Qxf6 | a4 | +1.20 | +1.12 |
| 184809655978 | 30 | 15... Qxh3 | great | best | precision | best | 0.0000 | 1.000 | yes | Qxh3 | - | -M2 | -M2 |
| 184809852108 | 5 | 3. Bf4 | book | best | precision | best | 0.0000 | 0.530 | yes | Bf4 | - | +0.38 | +0.32 |
| 184809852108 | 6 | 3... Bf5 | book | best | precision | best | 0.0000 | 0.478 | yes | Bf5 | - | +0.46 | +0.36 |
| 184809852108 | 11 | 6. e3 | best | excellent | precision | excellent | 0.0034 | 0.510 | no | c3 | - | +0.21 | +0.14 |
| 184809852108 | 15 | 8. Bd3 | inaccuracy | good | precision | good | 0.0498 | 0.581 | no | Ne5 | Ne5 | +0.33 | +0.46 |
| 184809852108 | 16 | 8... f6 | mistake | inaccuracy | precision | inaccuracy | 0.0840 | 0.469 | no | Nd7 | h4 | +1.88 | +1.74 |
| 184809852108 | 17 | 9. Bxe4 | miss | inaccuracy | precision | inaccuracy | 0.0627 | 0.615 | no | Rg1 | Rg1 | +0.55 | +0.78 |
| 184809852108 | 18 | 9... dxe4 | good | excellent | precision | excellent | 0.0172 | 0.448 | no | Bxe4 | Bxe4 | +1.16 | +1.13 |
| 184809852108 | 25 | 13. dxe5 | best | excellent | precision | excellent | 0.0045 | 0.594 | no | Bg3 | - | +1.36 | +1.85 |
| 184809852108 | 27 | 14. b3 | miss | blunder | precision | blunder | 0.2568 | 0.757 | no | exf6 | exf6 | -0.17 | +0.00 |
| 184809852108 | 30 | 15... Nd7 | miss | mistake | precision | mistake | 0.1489 | 0.575 | no | Qa5 | Qa5 | +1.47 | +1.67 |
| 184809852108 | 31 | 16. exf6 | miss | inaccuracy | precision | inaccuracy | 0.0876 | 0.610 | no | Nf5 | Nf5 | 0.00 | +0.43 |
| 184809852108 | 32 | 16... O-O-O | blunder | mistake | precision | mistake | 0.1649 | 0.471 | no | Nxf6 | Nxf6 | +4.73 | +5.50 |
| 184809852108 | 34 | 17... Nxf6 | great | best | precision | best | 0.0000 | 0.715 | yes | Nxf6 | - | -3.64 | -3.82 |
| 184809852108 | 35 | 18. Nxe4 | mistake | inaccuracy | precision | inaccuracy | 0.0577 | 0.264 | no | Qxd8+ | Na4 | -4.91 | -5.02 |
| 184809852108 | 39 | 20. Rfd1 | good | excellent | precision | excellent | 0.0196 | 0.196 | no | a3 | Rad1 | -5.10 | -5.72 |
| 184809852108 | 40 | 20... Rxd1+ | good | excellent | precision | excellent | 0.0088 | 0.823 | no | Qd8 | Be6 | -4.56 | -5.40 |
| 184809852108 | 43 | 22. g7 | inaccuracy | excellent | precision | excellent | 0.0189 | 0.197 | no | c3 | Kh2 | -5.68 | -5.68 |
| 184809852108 | 45 | 23. Nf5 | mistake | best | precision | best | 0.0000 | 0.173 | yes | Nf5 | Kh2 | -6.19 | -6.36 |
| 184810276410 | 7 | 4. Nc3 | inaccuracy | good | precision | good | 0.0494 | 0.540 | no | e5 | e5 | -0.30 | -0.39 |
| 184810276410 | 8 | 4... Qb6 | inaccuracy | mistake | precision | mistake | 0.1059 | 0.527 | no | d5 | d5 | +1.05 | +1.16 |
| 184810276410 | 9 | 5. d4 | excellent | good | precision | good | 0.0284 | 0.579 | no | e5 | Qe2 | +0.87 | +0.81 |
| 184810276410 | 12 | 6... Qb4+ | great | best | precision | best | 0.0000 | 0.673 | yes | Qb4+ | - | -2.41 | -2.54 |
| 184810276410 | 13 | 7. Bd2 | inaccuracy | good | precision | good | 0.0435 | 0.332 | no | Nd2 | Nd2 | -3.33 | -3.28 |
| 184810276410 | 17 | 9. dxc5 | good | excellent | precision | excellent | 0.0164 | 0.282 | no | b3 | b3 | -3.95 | -3.90 |
| 184810276410 | 22 | 11... Qxe5 | great | best | precision | best | 0.0000 | 0.844 | yes | Qxe5 | - | -5.93 | -5.98 |
| 184810276410 | 24 | 12... Qxb2 | good | excellent | precision | excellent | 0.0083 | 0.840 | no | d5 | Nc6 | -5.42 | -5.82 |
| 184810276410 | 25 | 13. Bd4 | inaccuracy | good | precision | good | 0.0215 | 0.168 | no | Rb1 | Qd3 | -6.73 | -6.41 |
| 184810276410 | 26 | 13... Qb5 | mistake | inaccuracy | precision | inaccuracy | 0.0518 | 0.854 | no | Nc3 | Nc3 | -4.22 | -5.08 |
| 184810276410 | 27 | 14. Bxg7 | inaccuracy | good | precision | good | 0.0409 | 0.198 | no | Qg4 | Qg4 | -6.06 | -6.10 |
| 185069669434 | 5 | 3. exd5 | book | best | precision | best | 0.0000 | 0.521 | yes | exd5 | - | +0.20 | +0.24 |
| 185069669434 | 7 | 4. Nc3 | best | excellent | precision | excellent | 0.0033 | 0.550 | no | Be2 | - | +0.79 | +0.72 |
| 185069669434 | 12 | 6... Qd8 | excellent | good | precision | good | 0.0205 | 0.421 | no | Qb6 | Qb6 | +1.62 | +1.58 |
| 185069669434 | 22 | 11... Nc6 | mistake | inaccuracy | precision | inaccuracy | 0.0523 | 0.476 | no | Nd7 | Nd7 | +1.61 | +1.17 |
| 185069669434 | 23 | 12. Qc1 | miss | inaccuracy | precision | inaccuracy | 0.0549 | 0.577 | no | Bxh7+ | Bxh7+ | +0.33 | +0.33 |
| 185069669434 | 31 | 16. Bg5 | excellent | best | precision | best | 0.0000 | 0.591 | yes | Bg5 | Be3 | +1.24 | +1.47 |
| 185069669434 | 34 | 17... Qh5 | good | excellent | precision | excellent | 0.0185 | 0.418 | no | Qc7 | Qc7 | +1.50 | +1.62 |
| 185069669434 | 37 | 19. Nxf8 | miss | inaccuracy | precision | inaccuracy | 0.0917 | 0.713 | no | Nxc5 | Nxc5 | +0.79 | +1.98 |
| 185069669434 | 42 | 21... f3 | brilliant | best | precision | best | 0.0000 | 0.857 | yes | f3 | - | -5.86 | -7.00 |
| 185069669434 | 44 | 22... Qh3 | great | best | precision | best | 0.0000 | 1.000 | yes | Qh3 | - | -M3 | -M3 |
| 185097600644 | 11 | 6. Kf1 | book | best | precision | best | 0.0000 | 0.574 | yes | Kf1 | - | +0.82 | +1.12 |
| 185097600644 | 12 | 6... Qe7 | book | best | precision | best | 0.0000 | 0.426 | yes | Qe7 | - | +0.82 | +1.10 |
| 185097600644 | 13 | 7. Nxh8 | book | best | precision | best | 0.0000 | 0.573 | yes | Nxh8 | - | +0.82 | +1.37 |
| 185097600644 | 14 | 7... d5 | book | best | precision | best | 0.0000 | 0.410 | yes | d5 | - | +0.82 | +0.91 |
| 185097600644 | 15 | 8. exd5 | book | best | precision | best | 0.0000 | 0.560 | yes | exd5 | - | +0.82 | +1.10 |
| 185097600644 | 16 | 8... Nd4 | book | best | precision | best | 0.0000 | 0.427 | yes | Nd4 | - | +0.82 | +0.78 |
| 185097600644 | 18 | 9... Bg4 | great | best | precision | best | 0.0000 | 0.625 | yes | Bg4 | - | -1.33 | -3.18 |
| 185097600644 | 19 | 10. Qa4+ | best | good | precision | good | 0.0224 | 0.300 | no | Bb5+ | - | -1.33 | -0.78 |
| 185097600644 | 21 | 11. Kxf2 | great | best | precision | best | 0.0000 | 0.267 | yes | Kxf2 | - | -1.33 | -2.24 |
| 185097600644 | 22 | 11... Qf6+ | inaccuracy | mistake | precision | mistake | 0.1450 | 0.645 | no | Qh4+ | Qh4+ | 0.00 | +0.00 |
| 185097600644 | 24 | 12... Qf5 | brilliant | best | precision | best | 0.0000 | 0.500 | yes | Qf5 | - | 0.00 | +0.00 |
| 185097600644 | 26 | 13... Qe4+ | great | best | precision | best | 0.0000 | 0.500 | yes | Qe4+ | - | 0.00 | +0.00 |
| 185097600644 | 30 | 15... Rf8+ | great | best | precision | best | 0.0000 | 1.000 | yes | Rf8+ | - | -M3 | -M3 |
| 185097600644 | 32 | 16... Qe1+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qe1+ | - | -M1 | -M1 |
| 185099205950 | 12 | 6... h6 | book | best | precision | best | 0.0000 | 0.495 | yes | h6 | - | +0.07 | +0.12 |
| 185099205950 | 23 | 12. Nd5 | best | excellent | precision | excellent | 0.0104 | 0.405 | no | Ne2 | - | -1.34 | -1.58 |
| 185099205950 | 30 | 15... cxd5 | mistake | inaccuracy | precision | inaccuracy | 0.0826 | 0.571 | no | Bxf3 | Bxf3 | +0.33 | +0.20 |
| 185099205950 | 32 | 16... Bxf3 | great | best | precision | best | 0.0000 | 0.638 | yes | Bxf3 | - | -1.87 | -2.07 |
| 185099205950 | 38 | 19... Qxf3+ | excellent | good | precision | good | 0.0259 | 0.755 | no | dxc3 | dxc3 | -3.83 | -3.68 |
| 185099205950 | 42 | 21... Rad8 | miss | mistake | precision | mistake | 0.1019 | 0.726 | no | Qxd3 | Qxd3 | -1.51 | -1.87 |
| 185099205950 | 43 | 22. Qc7 | miss | mistake | precision | mistake | 0.1340 | 0.376 | no | Qg3 | Qg3 | -4.13 | -4.50 |
| 185099205950 | 50 | 25... Qxh3+ | excellent | best | precision | best | 0.0000 | 0.802 | yes | Qxh3+ | Qxd3 | -4.76 | -5.20 |
| 185099205950 | 51 | 26. Rh2 | good | excellent | precision | excellent | 0.0181 | 0.197 | no | Qh2 | Qh2 | -5.29 | -5.53 |
| 185099205950 | 53 | 27. Rg1 | inaccuracy | good | precision | good | 0.0224 | 0.181 | no | Rg2 | Rf2 | -6.28 | -6.18 |
| 185099205950 | 54 | 27... Rc8 | inaccuracy | good | precision | good | 0.0499 | 0.841 | no | Qf3+ | Qf3+ | -5.16 | -4.94 |
| 185099205950 | 56 | 28... Qe4+ | good | excellent | precision | excellent | 0.0147 | 0.799 | no | Qe3 | Rxc4 | -4.72 | -4.79 |
| 185099205950 | 59 | 30. Rc1 | good | excellent | precision | excellent | 0.0172 | 0.214 | no | Rxh6 | Rxh6 | -5.27 | -5.20 |
| 185099205950 | 60 | 30... Rce8 | good | excellent | precision | excellent | 0.0131 | 0.803 | no | Rc5 | Rc5 | -4.55 | -4.90 |
| 185099205950 | 61 | 31. c5 | good | excellent | precision | excellent | 0.0153 | 0.210 | no | Rh3 | Rd2 | -5.33 | -5.25 |
| 185099205950 | 62 | 31... Re1+ | best | excellent | precision | excellent | 0.0043 | 0.805 | no | R4e5 | - | -5.33 | -5.05 |
| 185099205950 | 66 | 33... Re2+ | best | excellent | precision | excellent | 0.0000 | 0.796 | no | Re5 | - | -5.33 | -7.68 |
| 185099205950 | 67 | 34. Kg1 | best | excellent | precision | excellent | 0.0016 | 0.112 | no | Kg3 | - | -5.33 | -7.74 |
| 185099205950 | 68 | 34... Re6 | good | mistake | precision | mistake | 0.1007 | 0.890 | no | Rxh2 | Re5 | -4.96 | -4.89 |
| 185099205950 | 70 | 35... Rc6 | inaccuracy | good | precision | good | 0.0302 | 0.798 | no | Re1+ | d3 | -3.87 | -4.43 |
| 185099205950 | 71 | 36. Kf1 | good | excellent | precision | excellent | 0.0155 | 0.232 | no | Kf2 | Kf2 | -4.39 | -4.73 |
| 185099205950 | 72 | 36... Kf8 | good | excellent | precision | excellent | 0.0103 | 0.782 | no | d3 | d3 | -3.86 | -4.41 |
| 185099205950 | 78 | 39... g5 | inaccuracy | excellent | precision | excellent | 0.0000 | 0.725 | no | Kd7 | Kd7 | -2.31 | -3.75 |
| 185099205950 | 79 | 40. Re2+ | good | best | precision | best | 0.0000 | 0.266 | yes | Re2+ | Rh2 | -2.83 | -2.88 |
| 185099205950 | 80 | 40... Kf6 | inaccuracy | good | precision | good | 0.0268 | 0.685 | no | Kd7 | Kd7 | -1.86 | -2.50 |
| 185099205950 | 81 | 41. Rf2+ | inaccuracy | good | precision | good | 0.0487 | 0.337 | no | Kd5 | Kd5 | -2.76 | -3.34 |
| 185099205950 | 82 | 41... Kg6 | excellent | best | precision | best | 0.0000 | 0.711 | yes | Kg6 | Ke6 | -2.54 | -3.42 |
| 185099205950 | 83 | 42. Kd5 | best | excellent | precision | excellent | 0.0098 | 0.284 | no | Rb2 | - | -2.54 | -2.99 |
| 185099205950 | 87 | 44. Re5 | inaccuracy | good | precision | good | 0.0440 | 0.260 | no | Re6+ | Kd6 | -4.33 | -4.77 |
| 185099205950 | 90 | 45... Rd1 | good | inaccuracy | precision | inaccuracy | 0.0621 | 0.795 | no | g4 | f4 | -3.37 | -3.73 |
| 185099205950 | 94 | 47... Kh5 | best | excellent | precision | excellent | 0.0000 | 0.786 | no | Kg7 | - | -4.22 | -4.92 |
| 185099205950 | 95 | 48. c6 | good | excellent | precision | excellent | 0.0139 | 0.209 | no | Rf6 | Rf6 | -5.12 | -5.24 |
| 185099205950 | 97 | 49. Ka5 | excellent | best | precision | best | 0.0000 | 0.170 | no | Rf6 | Rf6 | -5.12 | -5.59 |
| 185099205950 | 98 | 49... f3 | good | excellent | precision | excellent | 0.0111 | 0.819 | no | g4 | g4 | -4.32 | -6.04 |
| 185102025164 | 16 | 8... Bxf5 | excellent | good | precision | good | 0.0212 | 0.562 | no | h5 | h5 | -0.71 | -0.73 |
| 185102025164 | 22 | 11... g6 | good | inaccuracy | precision | inaccuracy | 0.0587 | 0.259 | no | Ne5 | Ne5 | +4.63 | +4.86 |
| 185102025164 | 26 | 13... Qxf2+ | great | best | precision | best | 0.0000 | 1.000 | yes | Qxf2+ | - | -M2 | -M2 |
| 185198810006 | 9 | 5. Nbd2 | book | excellent | precision | excellent | 0.0000 | 0.519 | no | a4 | - | +0.28 | +0.31 |
| 185198810006 | 11 | 6. a3 | excellent | good | precision | good | 0.0207 | 0.524 | no | c3 | c3 | -0.02 | +0.04 |
| 185198810006 | 23 | 12. a4 | good | excellent | precision | excellent | 0.0184 | 0.564 | no | Bg5 | Bg5 | +0.61 | +0.56 |
| 185198810006 | 24 | 12... c5 | mistake | inaccuracy | precision | inaccuracy | 0.0726 | 0.460 | no | h6 | h6 | +1.94 | +1.60 |
| 185198810006 | 25 | 13. bxc6 | miss | inaccuracy | precision | inaccuracy | 0.0527 | 0.613 | no | Bg5 | Bg5 | +0.81 | +0.84 |
| 185198810006 | 27 | 14. Re1 | excellent | good | precision | good | 0.0241 | 0.556 | no | Bg5 | Bg5 | +0.53 | +0.44 |
| 185216623720 | 10 | 5... Ke8 | good | excellent | precision | excellent | 0.0027 | 0.615 | no | Kg8 | Kg8 | -1.46 | -1.52 |
| 185216623720 | 12 | 6... Bb6 | good | excellent | precision | excellent | 0.0109 | 0.599 | no | d6 | Be7 | -1.05 | -1.18 |
| 185216623720 | 13 | 7. Nc3 | inaccuracy | excellent | precision | excellent | 0.0143 | 0.418 | no | O-O | O-O | -1.72 | -1.22 |
| 185216623720 | 14 | 7... d6 | inaccuracy | good | precision | good | 0.0276 | 0.585 | no | Nc6 | Nc6 | -0.99 | -0.83 |
| 185216623720 | 16 | 8... Be6 | good | excellent | precision | excellent | 0.0090 | 0.557 | no | Nc6 | Nc6 | -0.74 | -0.55 |
| 185216623720 | 22 | 11... Bc4 | mistake | inaccuracy | precision | inaccuracy | 0.0746 | 0.446 | no | b5 | b5 | +1.74 | +1.87 |
| 185216623720 | 24 | 12... Nc6 | best | excellent | precision | excellent | 0.0118 | 0.375 | no | g5 | - | +1.74 | +1.88 |
| 185216623720 | 29 | 15. Qd1 | great | best | precision | best | 0.0000 | 0.397 | yes | Qd1 | - | -1.57 | -2.22 |
| 185216623720 | 32 | 16... Ba6 | mistake | inaccuracy | precision | inaccuracy | 0.0538 | 0.196 | no | Rd8 | Rd8 | +6.44 | +6.38 |
| 185216623720 | 35 | 18. Qa4+ | good | excellent | precision | excellent | 0.0000 | 0.870 | no | Qf4 | Qxd8+ | +5.99 | +6.87 |
| 185216623720 | 36 | 18... b5 | mistake | best | precision | best | 0.0000 | 0.126 | yes | b5 | Kf7 | +6.82 | +7.10 |
| 185216623720 | 37 | 19. Nxb5 | inaccuracy | good | precision | good | 0.0441 | 0.881 | no | Qf4 | exf6 | +5.54 | +5.80 |
| 185216623720 | 45 | 23. Bc3 | excellent | best | precision | best | 0.0000 | 0.246 | yes | Bc3 | Be5 | -3.61 | -4.20 |
| 185216623720 | 51 | 26. Qc8+ | great | best | precision | best | 0.0000 | 0.883 | yes | Qc8+ | - | +7.08 | +8.22 |
| 185216623720 | 57 | 29. Re1+ | mistake | excellent | precision | excellent | 0.0101 | 0.408 | no | Qxb6+ | Qa3 | -1.50 | -1.43 |
| 185216623720 | 58 | 29... Kf5 | miss | mistake | precision | mistake | 0.1951 | 0.599 | no | Kf7 | Kf7 | 0.00 | +1.25 |
| 185216623720 | 59 | 30. Qa3 | great | best | precision | best | 0.0000 | 0.587 | yes | Qa3 | - | 0.00 | +1.51 |
| 185216623720 | 60 | 30... Rhd8 | mistake | best | precision | best | 0.0000 | 0.395 | yes | Rhd8 | Kg6 | +1.49 | +1.43 |
| 185216623720 | 61 | 31. Qf3+ | great | best | precision | best | 0.0000 | 0.599 | yes | Qf3+ | - | +1.49 | +1.68 |
| 185216623720 | 62 | 31... Kg6 | great | best | precision | best | 0.0000 | 0.384 | yes | Kg6 | - | +1.49 | +1.43 |
| 185216623720 | 65 | 33. b3 | excellent | good | precision | good | 0.0225 | 0.391 | no | a3 | a3 | -1.81 | -1.94 |
| 185216623720 | 68 | 34... Kh8 | excellent | good | precision | good | 0.0224 | 0.602 | no | Kg8 | Kg8 | -1.24 | -1.23 |
| 185216623720 | 69 | 35. Bc3 | excellent | best | precision | best | 0.0000 | 0.414 | yes | Bc3 | Kb2 | -1.25 | -1.18 |
| 185216623720 | 71 | 36. Rxd1 | great | best | precision | best | 0.0000 | 0.452 | yes | Rxd1 | - | -0.70 | -0.67 |
| 185216623720 | 75 | 38. Qe8+ | great | best | precision | best | 0.0000 | 0.709 | yes | Qe8+ | - | +2.90 | +2.87 |
| 185216623720 | 77 | 39. Qe4+ | great | best | precision | best | 0.0000 | 0.692 | yes | Qe4+ | - | +2.90 | +2.88 |
| 185216623720 | 79 | 40. Qe8+ | best | excellent | precision | excellent | 0.0129 | 0.710 | no | Bxg7+ | - | +2.90 | +2.78 |
| 185216623720 | 81 | 41. Qe4+ | great | best | precision | best | 0.0000 | 0.685 | yes | Qe4+ | - | +2.90 | +2.92 |
| 185492163944 | 12 | 6... Nxd5 | excellent | best | precision | best | 0.0000 | 0.500 | no | Nxe4 | Nxe4 | +0.02 | +0.00 |
| 185492163944 | 17 | 9. Bb5+ | best | excellent | precision | excellent | 0.0099 | 0.506 | no | c3 | - | +0.02 | -0.15 |
| 185492163944 | 27 | 14. d4 | excellent | best | precision | best | 0.0000 | 0.681 | yes | d4 | a4 | +2.77 | +2.54 |
| 185492163944 | 28 | 14... exd4 | good | inaccuracy | precision | inaccuracy | 0.0603 | 0.327 | no | O-O | O-O | +3.43 | +3.56 |
| 185492163944 | 29 | 15. cxd4 | excellent | good | precision | good | 0.0234 | 0.733 | no | a4 | a4 | +3.13 | +3.24 |
| 185492163944 | 33 | 17. Qxg7 | great | best | precision | best | 0.0000 | 0.876 | yes | Qxg7 | - | +6.11 | +6.57 |
| 185492163944 | 36 | 18... Be6 | mistake | best | precision | best | 0.0000 | 0.020 | yes | Be6 | Kd8 | +11.45 | +13.13 |
| 185498696400 | 4 | 2... Bd6 | inaccuracy | good | precision | good | 0.0416 | 0.471 | no | Nc6 | Nc6 | +0.98 | +0.96 |
| 185498696400 | 5 | 3. Nc3 | good | excellent | precision | excellent | 0.0181 | 0.570 | no | d4 | d4 | +0.73 | +0.71 |
| 185498696400 | 6 | 3... Nf6 | good | excellent | precision | excellent | 0.0160 | 0.448 | no | c5 | c5 | +1.03 | +1.13 |
| 185498696400 | 9 | 5. d3 | best | excellent | precision | excellent | 0.0007 | 0.530 | no | O-O | - | +0.35 | +0.42 |
| 185498696400 | 14 | 7... d6 | excellent | best | precision | best | 0.0000 | 0.473 | yes | d6 | h6 | +0.39 | +0.44 |
| 185498696400 | 15 | 8. Nd5 | excellent | good | precision | good | 0.0272 | 0.532 | no | a3 | a3 | +0.08 | +0.07 |
| 185498696400 | 21 | 11. Bb3 | good | excellent | precision | excellent | 0.0103 | 0.498 | no | Nxe7+ | Nxe7+ | -0.28 | -0.31 |
| 185498696400 | 22 | 11... Nxb3 | best | excellent | precision | excellent | 0.0044 | 0.523 | no | Bg5 | - | -0.28 | -0.14 |
| 185498696400 | 23 | 12. axb3 | excellent | best | precision | best | 0.0000 | 0.490 | yes | axb3 | Nxe7+ | -0.30 | -0.30 |
| 185498696400 | 24 | 12... c6 | excellent | best | precision | best | 0.0000 | 0.522 | yes | c6 | Be6 | -0.22 | -0.24 |
| 185498696400 | 29 | 15. d5 | excellent | good | precision | good | 0.0206 | 0.485 | no | Qd3 | Qd3 | -0.51 | -0.48 |
| 185498696400 | 34 | 17... b6 | good | excellent | precision | excellent | 0.0177 | 0.518 | no | Qc7 | Qc7 | +0.20 | +0.00 |
| 185498696400 | 36 | 18... g5 | best | excellent | precision | excellent | 0.0015 | 0.505 | no | Re8 | - | -0.04 | -0.05 |
| 185498696400 | 43 | 22. h4 | good | excellent | precision | excellent | 0.0147 | 0.527 | no | Rf1 | Rf1 | +0.31 | +0.10 |
| 185498696400 | 47 | 24. Rxh4 | good | excellent | precision | excellent | 0.0029 | 0.503 | no | Rf1 | Rf1 | -0.56 | -0.50 |
| 185498696400 | 50 | 25... f5 | inaccuracy | good | precision | good | 0.0272 | 0.500 | no | Rag8 | Qg6 | +0.49 | +0.37 |
| 185498696400 | 52 | 26... Rf8 | excellent | good | precision | good | 0.0228 | 0.500 | no | Rag8 | Rag8 | +0.30 | +0.14 |
| 185498696400 | 59 | 30. Ke2 | excellent | best | precision | best | 0.0000 | 0.500 | yes | Ke2 | Ke1 | 0.00 | +0.02 |
| 185498696400 | 61 | 31. Kd3 | great | best | precision | best | 0.0000 | 0.537 | yes | Kd3 | - | +0.51 | +0.49 |
| 185498696400 | 65 | 33. Rh8+ | best | excellent | precision | excellent | 0.0074 | 0.655 | no | R1h6 | - | +2.12 | +2.13 |
| 185498696400 | 67 | 34. R1h7+ | good | excellent | precision | excellent | 0.0166 | 0.664 | no | R1h6 | R1h6 | +1.83 | +2.13 |
| 185498696400 | 71 | 36. Kb5 | excellent | best | precision | best | 0.0000 | 0.498 | yes | Kb5 | Kd3 | -0.24 | -0.14 |
| 185498696400 | 72 | 36... Rxb2 | good | excellent | precision | excellent | 0.0103 | 0.510 | no | Rxh7 | Rxh7 | +0.11 | +0.00 |
| 185498696400 | 73 | 37. Kc6 | excellent | good | precision | good | 0.0287 | 0.500 | no | Rh1 | Rh6 | -0.04 | -0.39 |
| 185498696400 | 74 | 37... Rxb3 | excellent | good | precision | good | 0.0287 | 0.529 | no | Rxh7 | Rxh7 | +0.17 | +0.00 |
| 185498696400 | 75 | 38. Kxd6 | excellent | good | precision | good | 0.0294 | 0.500 | no | Rh1 | Rh2 | -0.05 | -0.40 |
| 185498696400 | 76 | 38... Rxe3 | excellent | good | precision | good | 0.0250 | 0.529 | no | Rxh7 | Rxh7 | 0.00 | +0.00 |
| 185498696400 | 77 | 39. Kc6 | good | excellent | precision | excellent | 0.0015 | 0.500 | no | Rh5 | Rh1 | -0.33 | -0.02 |
| 185498696400 | 78 | 39... a4 | good | excellent | precision | excellent | 0.0015 | 0.501 | no | Rxh7 | Rxh7 | +0.01 | +0.00 |
| 185498696400 | 80 | 40... Rxh7 | good | excellent | precision | excellent | 0.0074 | 0.500 | no | Rd3 | Rd3 | +0.33 | +0.01 |
| 185498696400 | 82 | 41... Kg6 | great | best | precision | best | 0.0000 | 0.500 | yes | Kg6 | - | +0.33 | +0.12 |
| 185498696400 | 85 | 43. d7 | great | best | precision | best | 0.0000 | 0.800 | yes | d7 | - | +2.92 | +4.55 |
| 185498696400 | 88 | 44... a2 | miss | mistake | precision | mistake | 0.1769 | 0.707 | no | b5 | b5 | -0.30 | -0.33 |
| 185498696400 | 93 | 47. d8=Q | best | excellent | precision | excellent | 0.0051 | 0.089 | no | d8=R | - | -6.26 | -7.09 |
| 185498696400 | 94 | 47... Rxd8 | excellent | best | precision | best | 0.0000 | 0.890 | yes | Rxd8 | Qa7+ | -6.22 | -6.75 |
| 185498696400 | 96 | 48... Qa7+ | excellent | best | precision | best | 0.0000 | 0.905 | yes | Qa7+ | c4 | -6.18 | -6.70 |
| 185498696400 | 102 | 51... Qd4 | good | excellent | precision | excellent | 0.0000 | 1.000 | no | Kd6 | Kd6 | -M5 | -M6 |
| 185498696400 | 105 | 53. Kc7 | best | excellent | precision | excellent | 0.0000 | 0.000 | no | Kb5 | - | -M4 | -M6 |

### `miss_detector` (43)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 142849919300 | 20 | 10... h6 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1025 | 0.795 | no | Nxc2+ | Nxc2+ | -3.17 | -3.27 |
| 142866059618 | 28 | 14... Qa6+ | mistake | miss (tactic) | miss_detector | blunder | 0.2743 | 0.577 | no | O-O-O | Rd8 | +3.13 | +3.27 |
| 145833178628 | 21 | 11. dxe4 | mistake | miss (opportunity) | miss_detector | mistake | 0.1575 | 0.381 | no | d4 | d4 | -4.84 | -5.26 |
| 145833758308 | 73 | 37. Kf2 | good | miss (opportunity) | miss_detector | mistake | 0.1173 | 0.117 | no | Kg1 | Re4 | -M7 | -M7 |
| 145833758308 | 101 | 51. h3 | mistake | miss (opportunity) | miss_detector | mistake | 0.1382 | 0.138 | no | Ke7 | Ke7 | -M3 | -M3 |
| 147234657424 | 18 | 9... Be6 | mistake | miss (free_piece) | miss_detector | mistake | 0.1551 | 0.805 | no | Qxd5 | Qxd5 | -2.78 | -2.70 |
| 147295227566 | 48 | 24... fxe4 | mistake | miss (tactic) | miss_detector | mistake | 0.1537 | 0.632 | no | Kh7 | Bf7 | +0.46 | +0.36 |
| 147786569400 | 40 | 20... Qxd3 | blunder | miss (free_piece) | miss_detector | blunder | 0.2299 | 0.230 | no | Qxf6 | Qxf6 | M1 | M1 |
| 148014224206 | 43 | 22. Qxe5 | blunder | miss (free_piece) | miss_detector | blunder | 0.7453 | 0.745 | no | Rxe1 | Rxe1 | -M2 | -M2 |
| 148224127998 | 32 | 16... cxd5 | blunder | miss (free_piece) | miss_detector | blunder | 0.3646 | 0.643 | no | Nxd5 | Nxd5 | +4.04 | +4.01 |
| 164188880582 | 38 | 19... gxf6 | blunder | miss (tactic) | miss_detector | blunder | 0.2771 | 0.500 | no | Rxe1+ | Rxe1+ | +5.05 | +5.18 |
| 165450446440 | 33 | 17. Bxh8 | blunder | miss (free_piece) | miss_detector | blunder | 0.8806 | 0.881 | no | Qxa2 | Qxa2 | -M1 | -M1 |
| 165557442658 | 52 | 26... d2 | mistake | miss (tactic) | miss_detector | blunder | 0.3466 | 0.847 | no | Qb1+ | Qb1+ | 0.00 | +0.00 |
| 166583201950 | 21 | 11. Nd3 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1052 | 0.742 | no | Qxa8 | Be3 | +2.46 | +2.42 |
| 166583201950 | 34 | 17... Qxe5 | mistake | miss (tactic) | miss_detector | blunder | 0.2560 | 0.668 | no | Nbd7 | Nbd7 | +1.63 | +1.81 |
| 166583201950 | 62 | 31... Kd7 | good | miss (tactic) | miss_detector | mistake | 0.1151 | 0.871 | no | Kf8 | Kf8 | -5.15 | -6.52 |
| 167397747616 | 74 | 37... d4 | good | miss (opportunity) | miss_detector | mistake | 0.1718 | 0.685 | no | c4 | c4 | 0.00 | -0.23 |
| 167397747616 | 75 | 38. Kh5 | mistake | miss (opportunity) | miss_detector | blunder | 0.2679 | 0.487 | no | Kg3 | Kg3 | -3.63 | -5.45 |
| 168148201932 | 23 | 12. O-O | mistake | miss (tactic) | miss_detector | blunder | 0.2680 | 0.594 | no | Qc6+ | Qc6+ | -3.22 | -3.05 |
| 169217872990 | 39 | 20. Kh1 | blunder | miss (tactic) | miss_detector | blunder | 0.4241 | 0.606 | no | g3 | g3 | -5.52 | -6.20 |
| 171841312410 | 37 | 19. Nxf3 | mistake | miss (free_piece) | miss_detector | mistake | 0.1020 | 0.503 | no | gxf3 | gxf3 | -1.70 | -1.71 |
| 171841312410 | 39 | 20. Rae1 | blunder | miss (opportunity) | miss_detector | mistake | 0.1613 | 0.510 | no | Rfb1 | Rfb1 | -2.35 | -2.46 |
| 172349629492 | 20 | 10... Bxh3 | mistake | miss (free_piece) | miss_detector | mistake | 0.1242 | 0.453 | no | gxf6 | gxf6 | +2.94 | +3.07 |
| 172349629492 | 22 | 11... Bxg2 | blunder | miss (tactic) | miss_detector | blunder | 0.2034 | 0.476 | no | Bg4 | Bg4 | +4.04 | +4.22 |
| 172996177054 | 34 | 17... Re1+ | blunder | miss (free_piece) | miss_detector | blunder | 0.3803 | 0.780 | no | Qxd6 | Qxd6 | +1.57 | +1.61 |
| 173068943088 | 33 | 17. hxg4 | mistake | miss (free_piece) | miss_detector | mistake | 0.1024 | 0.499 | no | Qxe3 | Qxe3 | -1.81 | -1.88 |
| 173068943088 | 51 | 26. Qh6+ | mistake | miss (tactic) | miss_detector | blunder | 0.3585 | 0.858 | no | Re1 | Re1 | 0.00 | +0.00 |
| 173620121124 | 21 | 11. Qb4 | mistake | miss (opportunity) | miss_detector | mistake | 0.1424 | 0.572 | no | Qc2 | Qc2 | -1.22 | -1.19 |
| 173620121124 | 29 | 15. Bb4+ | mistake | miss (tactic) | miss_detector | blunder | 0.2606 | 0.585 | no | O-O | Bxa1 | -2.61 | -2.82 |
| 173620121124 | 85 | 43. Rg7+ | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1029 | 0.486 | no | Nxa5 | Nxa5 | - | -1.83 |
| 173667762936 | 37 | 19. Nc3 | mistake | miss (free_piece) | miss_detector | mistake | 0.1029 | 0.287 | no | Kxe2 | Kxe2 | -4.93 | -5.53 |
| 173905398948 | 50 | 25... Nb7 | blunder | miss (tactic) | miss_detector | blunder | 0.2747 | 0.773 | no | Kd6 | Kd6 | +0.10 | +0.03 |
| 184028735740 | 14 | 7... Nxd5 | mistake | miss (opportunity) | miss_detector | mistake | 0.1653 | 0.586 | no | Nb4 | Nb4 | +1.24 | +1.24 |
| 184028735740 | 45 | 23. Nb5 | blunder | miss (tactic) | miss_detector | blunder | 0.2056 | 0.500 | no | Rcf1 | Rcf1 | -3.45 | -3.38 |
| 184028735740 | 47 | 24. Kd3 | inaccuracy | miss (tactic) | miss_detector | mistake | 0.1012 | 0.332 | no | Ke2 | Ke2 | -4.06 | -4.37 |
| 184028735740 | 52 | 26... d3 | mistake | miss (tactic) | miss_detector | blunder | 0.5574 | 0.874 | no | Rg8 | Rg8 | +2.22 | +2.98 |
| 184028735740 | 54 | 27... d2 | inaccuracy | miss (opportunity) | miss_detector | mistake | 0.1165 | 0.727 | no | Qd2 | Rg8 | -1.89 | -1.65 |
| 184110410320 | 39 | 20. Rf1 | mistake | miss (opportunity) | miss_detector | mistake | 0.1223 | 0.122 | no | Ne3 | Nc3 | -9.22 | -M11 |
| 184449650784 | 38 | 19... exf3 | mistake | miss (tactic) | miss_detector | mistake | 0.1071 | 0.322 | no | Rd8 | Rxb2 | +4.73 | +4.94 |
| 185198810006 | 31 | 16. d5 | mistake | miss (opportunity) | miss_detector | mistake | 0.1761 | 0.645 | no | dxe5 | Bxf4 | -0.51 | -0.44 |
| 185216623720 | 18 | 9... cxb6 | inaccuracy | miss (free_piece) | miss_detector | mistake | 0.1189 | 0.548 | no | axb6 | axb6 | +0.79 | +1.03 |
| 185216623720 | 55 | 28. Qa6+ | mistake | miss (tactic) | miss_detector | blunder | 0.4186 | 0.895 | no | Qc6+ | Qc6+ | 0.00 | -0.09 |
| 185498696400 | 87 | 44. Kc7 | mistake | miss (tactic) | miss_detector | blunder | 0.5176 | 0.810 | no | d8=Q | d8=Q | -2.47 | -2.99 |

### `book` (26)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 142636591844 | 4 | 2... c6 | inaccuracy | book | book | good | 0.0490 | 0.477 | no | Nc6 | Nc6 | +1.23 | +1.23 |
| 142917385540 | 5 | 3. Nc3 | good | book | book | good | 0.0240 | 0.490 | no | dxe4 | dxe4 | -0.52 | -0.48 |
| 145833178628 | 3 | 2. e4 | good | book | book | good | 0.0237 | 0.506 | no | d4 | d4 | -0.31 | -0.30 |
| 145833758308 | 4 | 2... Qf6 | inaccuracy | book | book | good | 0.0494 | 0.477 | no | Nc6 | Nc6 | +1.21 | +1.25 |
| 145833758308 | 5 | 3. Bc4 | excellent | book | book | excellent | 0.0085 | 0.572 | no | Nc3 | Nc3 | +1.09 | +1.11 |
| 147991742972 | 7 | 4. Nxe5 | mistake | book | book | mistake | 0.1151 | 0.507 | no | h3 | d4 | -1.58 | -1.66 |
| 147991742972 | 8 | 4... Nxe5 | best | book | book | best | 0.0000 | 0.608 | yes | Nxe5 | - | -1.58 | -1.58 |
| 164007452224 | 6 | 3... h6 | good | book | book | good | 0.0293 | 0.485 | no | Bc5 | Bc5 | +0.74 | +0.75 |
| 164188880582 | 3 | 2. d4 | best | book | book | best | 0.0000 | 0.520 | yes | d4 | - | +0.22 | +0.29 |
| 164812402934 | 7 | 4. Nc3 | best | book | book | best | 0.0000 | 0.501 | yes | Nc3 | - | -0.09 | -0.13 |
| 165974850998 | 11 | 6. d3 | best | book | book | best | 0.0000 | 0.508 | yes | d3 | - | +0.18 | +0.11 |
| 166853117390 | 11 | 6. d3 | best | book | book | best | 0.0000 | 0.508 | yes | d3 | - | +0.18 | +0.11 |
| 167359572290 | 4 | 2... c6 | excellent | book | book | excellent | 0.0161 | 0.456 | no | Qxd5 | Qxd5 | +0.90 | +0.84 |
| 167359572290 | 5 | 3. dxc6 | best | book | book | best | 0.0000 | 0.552 | yes | dxc6 | - | +0.90 | +0.95 |
| 167359572290 | 6 | 3... Nxc6 | best | book | book | best | 0.0000 | 0.441 | yes | Nxc6 | - | +0.90 | +0.91 |
| 167396435524 | 11 | 6. O-O | best | book | book | excellent | 0.0042 | 0.512 | no | Bg5 | - | +0.19 | +0.13 |
| 168148201932 | 4 | 2... d5 | inaccuracy | book | book | good | 0.0360 | 0.477 | no | Nc6 | Nc6 | +1.07 | +1.00 |
| 168148201932 | 5 | 3. exd5 | best | book | book | best | 0.0000 | 0.559 | yes | exd5 | - | +1.07 | +0.98 |
| 171708489350 | 11 | 6. O-O | best | book | book | excellent | 0.0045 | 0.513 | no | Bg5 | - | +0.19 | +0.13 |
| 172026321412 | 4 | 2... Nc6 | good | book | book | good | 0.0399 | 0.487 | no | d5 | d5 | +0.85 | +0.92 |
| 173068943088 | 6 | 3... h6 | good | book | book | good | 0.0289 | 0.485 | no | Bc5 | Bc5 | +0.74 | +0.75 |
| 174468507028 | 4 | 2... Bc5 | mistake | book | book | inaccuracy | 0.0750 | 0.475 | no | Nc6 | Nc6 | +1.62 | +1.58 |
| 184028735740 | 3 | 2. Qh5 | good | book | book | good | 0.0478 | 0.523 | no | Nf3 | Nf3 | -0.37 | -0.39 |
| 184028735740 | 4 | 2... Nc6 | best | book | book | best | 0.0000 | 0.525 | yes | Nc6 | - | -0.37 | -0.37 |
| 184028735740 | 5 | 3. Bc4 | best | book | book | best | 0.0000 | 0.476 | yes | Bc4 | - | -0.37 | -0.32 |
| 185216623720 | 5 | 3. Nf3 | good | book | book | good | 0.0492 | 0.513 | no | Nc3 | d3 | -0.62 | -0.52 |

### `mate_override` (25)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 142849919300 | 47 | 24. Nd3 | mistake | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kb3 | Kb3 | -M2 | -M2 |
| 142866059618 | 88 | 44... Qc6+ | excellent | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Bf6 | Bf6 | -M2 | -M6 |
| 142873206408 | 81 | 41. Qe8+ | excellent | good | mate_override | good | 0.0000 | 1.000 | no | Qg3+ | Ke2 | M6 | M9 |
| 145833178628 | 56 | 28... Kf8 | excellent | good | mate_override | good | 0.0527 | 1.000 | no | Kh8 | Kh8 | -9.60 | -M10 |
| 145833758308 | 71 | 36. Kg2 | best | inaccuracy | mate_override | inaccuracy | 0.0502 | 0.050 | no | Qg3 | - | -10.55 | -M12 |
| 145833758308 | 72 | 36... Qd5+ | best | miss (mate) | mate_override | mistake | 0.1173 | 1.000 | no | Rc8 | - | -10.55 | -8.70 |
| 145833758308 | 90 | 45... Qg1+ | good | miss (mate) | mate_override | mistake | 0.1015 | 1.000 | no | f6+ | f6+ | -8.46 | -9.40 |
| 145833758308 | 94 | 47... Qxg4+ | good | miss (mate) | mate_override | mistake | 0.1163 | 1.000 | no | Qe3+ | Qf2 | -7.49 | -8.74 |
| 145833758308 | 122 | 61... d5 | excellent | good | mate_override | good | 0.0000 | 1.000 | no | Rc2 | Rc2 | -M3 | -M10 |
| 145833758308 | 123 | 62. Ke8 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kc8 | a3 | -M2 | -M2 |
| 146658193946 | 53 | 27. Rxd2 | best | good | mate_override | good | 0.0684 | 1.000 | no | Qg4+ | - | +13.47 | +11.86 |
| 146658193946 | 54 | 27... Qxe3+ | good | inaccuracy | mate_override | inaccuracy | 0.0618 | 0.062 | no | Qe7 | Qe7 | M5 | M5 |
| 147547838342 | 35 | 18. Kf1 | good | inaccuracy | mate_override | inaccuracy | 0.0431 | 0.043 | no | Kd1 | Kd1 | -M6 | -M6 |
| 147547838342 | 36 | 18... Qxd3+ | excellent | good | mate_override | good | 0.0499 | 1.000 | no | Qf3+ | Qf3+ | -M7 | -M6 |
| 164784324724 | 85 | 43. Bc4 | good | miss (mate) | mate_override | mistake | 0.1043 | 1.000 | no | d6 | d6 | +8.56 | M12 |
| 167359572290 | 35 | 18. Nxe5+ | good | miss (mate) | mate_override | mistake | 0.1021 | 1.000 | no | Rxc7+ | Rxc7+ | +8.12 | +8.70 |
| 167397747616 | 111 | 56. Qc3+ | good | miss (faster_mate) | mate_override | excellent | 0.0000 | 1.000 | no | Kb3 | Kb3 | M3 | M5 |
| 169217872990 | 47 | 24. Rf1 | good | inaccuracy | mate_override | inaccuracy | 0.0575 | 0.058 | no | Rd1 | Rc1 | -M4 | -M4 |
| 171124015136 | 57 | 29. Bxh6 | good | miss (mate) | mate_override | mistake | 0.1301 | 1.000 | no | Nxe5 | Nxe5 | +8.17 | +8.18 |
| 171124015136 | 59 | 30. Qc8+ | good | miss (mate) | mate_override | mistake | 0.1202 | 1.000 | no | Nxe5 | Nxe5 | +7.56 | +8.57 |
| 171124015136 | 77 | 39. Nxg8 | excellent | good | mate_override | good | 0.0436 | 1.000 | no | Qxf7 | Qc8 | +8.97 | M20 |
| 173667762936 | 54 | 27... Qxc2 | excellent | good | mate_override | good | 0.0000 | 1.000 | no | Qd2+ | Rd1+ | -M4 | -M7 |
| 173667762936 | 55 | 28. Ke5 | excellent | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | a3 | d6 | -M2 | -M2 |
| 184110410320 | 43 | 22. Ka4 | mistake | inaccuracy | mate_override | inaccuracy | 0.0000 | 0.000 | no | Kb2 | Kb2 | -M1 | -M1 |
| 185099205950 | 103 | 52. c7 | excellent | inaccuracy | mate_override | inaccuracy | 0.0452 | 0.045 | no | Rd6 | Rd6 | -M6 | -M13 |

### `losing_material_hardened` (17)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 142849698970 | 27 | 14. Qf3 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0720 | 0.216 | no | Kg2 | Kg2 | -6.48 | -6.90 |
| 142917385540 | 28 | 14... g5 | excellent | mistake | losing_material_hardened | good | 0.0311 | 0.174 | no | f5 | f5 | +6.00 | +7.17 |
| 145833178628 | 43 | 22. Nb3 | inaccuracy | mistake | losing_material_hardened | good | 0.0489 | 0.100 | no | Kd3 | Kd3 | -M13 | -12.61 |
| 145833758308 | 63 | 32. Kh3 | best | mistake | losing_material_hardened | excellent | 0.0043 | 0.145 | no | Rf3 | - | -7.75 | -8.15 |
| 147742438276 | 16 | 8... Ne7 | good | mistake | losing_material_hardened | excellent | 0.0172 | 0.131 | no | Qe7 | Qe7 | +7.26 | +7.29 |
| 147742438276 | 22 | 11... Rg8 | good | mistake | losing_material_hardened | good | 0.0301 | 0.109 | no | Kd7 | Kd7 | +8.28 | +8.74 |
| 164784324724 | 64 | 32... Rfe8 | inaccuracy | mistake | losing_material_hardened | good | 0.0317 | 0.189 | no | Bg6 | Bg6 | +6.03 | +6.20 |
| 166583201950 | 61 | 31. Qe5+ | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0718 | 0.195 | no | Qc5+ | Qc5+ | -5.78 | -8.21 |
| 166853117390 | 26 | 13... d5 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0580 | 0.243 | no | Qe7 | Qe7 | +5.79 | +6.25 |
| 167359572290 | 20 | 10... f6 | good | mistake | losing_material_hardened | good | 0.0388 | 0.136 | no | e5 | e5 | +8.64 | +8.92 |
| 171124015136 | 48 | 24... Qe8 | best | mistake | losing_material_hardened | excellent | 0.0021 | 0.186 | no | Qxb7 | - | +6.34 | +6.53 |
| 171124015136 | 64 | 32... e4 | good | mistake | losing_material_hardened | excellent | 0.0199 | 0.136 | no | Ng4 | Ng4 | +7.68 | +8.74 |
| 172349629492 | 44 | 22... g6 | inaccuracy | mistake | losing_material_hardened | inaccuracy | 0.0558 | 0.203 | no | Rxb7 | Rxb7 | +7.15 | +7.58 |
| 172996177054 | 68 | 34... Qc1+ | good | mistake | losing_material_hardened | excellent | 0.0198 | 0.149 | no | Nc4 | Nc4 | - | +6.85 |
| 173855642488 | 61 | 31. f4 | inaccuracy | mistake | losing_material_hardened | good | 0.0258 | 0.177 | no | Re7 | Re7 | -6.77 | -7.30 |
| 173855642488 | 65 | 33. Kg4 | inaccuracy | mistake | losing_material_hardened | good | 0.0247 | 0.122 | no | Kf2 | Kf2 | -8.10 | -8.76 |
| 185099205950 | 99 | 50. Kxa6 | inaccuracy | mistake | losing_material_hardened | good | 0.0300 | 0.164 | no | Rf6 | Rf6 | -6.17 | -8.26 |

### `brilliant_event` (6)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 142866059618 | 26 | 13... d4 | great | brilliant | brilliant_event | best | 0.0000 | 0.552 | yes | d4 | - | -0.98 | -1.02 |
| 142918703388 | 46 | 23... Qxd3 | best | brilliant | brilliant_event | best | 0.0000 | 0.776 | yes | Qxd3 | - | -4.28 | -4.35 |
| 166096155098 | 29 | 15. Qd8+ | best | brilliant | brilliant_event | best | 0.0000 | 1.000 | yes | Qd8+ | - | M1 | M1 |
| 166583201950 | 66 | 33... g5+ | great | brilliant | brilliant_event | best | 0.0000 | 0.879 | yes | g5+ | - | -8.35 | -8.25 |
| 173570784620 | 45 | 23. Qxf3 | great | brilliant | brilliant_event | best | 0.0000 | 0.714 | yes | Qxf3 | - | +3.50 | +3.50 |
| 184809655978 | 28 | 14... Ke7 | best | brilliant | brilliant_event | best | 0.0000 | 0.753 | yes | Ke7 | - | -3.71 | -4.70 |

### `blunder_softened` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 165327199736 | 35 | 18. Nc7 | blunder | mistake | blunder_softened | blunder | 0.2839 | 0.527 | no | Nd4 | Nd4 | -4.09 | -4.18 |
| 184555832944 | 20 | 10... Bh6 | blunder | mistake | blunder_softened | blunder | 0.2729 | 0.542 | no | Be7 | Nf5 | +3.71 | +3.82 |

### `great_find_event` (2)

| game | ply | move | app | ours | rule | precision | ep_lost | ep_before | played_is_best | our best | app best | app eval | our eval |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---:|---:|
| 185216623720 | 76 | 38... Kh7 | best | great | great_find_event | best | 0.0000 | 0.308 | yes | Kh7 | - | +2.90 | +2.87 |
| 185216623720 | 80 | 40... Kh7 | best | great | great_find_event | best | 0.0000 | 0.314 | yes | Kh7 | - | +2.90 | +2.76 |

