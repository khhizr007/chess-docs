# Coach agreement with Chess.com (Phase 0)

Run `coach-phase0`, 142 games, 8638 plies, commit `f5f0b35`. Reference: the main event of Chess.com's speech for the played move.

## Bad moves (Chess.com Inaccuracy, Mistake, Blunder, Miss)

| category | plies | share |
|---|---|---|
| exact | 376 | 18.9% |
| same tag, other circumstance | 19 | 1.0% |
| same family | 76 | 3.8% |
| different | 687 | 34.6% |
| they explain, we don't | 644 | 32.4% |
| we explain, they don't | 81 | 4.1% |
| neither | 105 | 5.3% |

Where both explain (1158 plies): exact 32.5%, same tag 34.1%, same family or better 40.7%.

### Plies both apps label bad (1641 of 1988)

Phase 1 explains only moves we label Inaccuracy, Mistake, Blunder or Miss, so this is the coach's own agreement, free of label disagreements.

| category | plies | share |
|---|---|---|
| exact | 376 | 22.9% |
| same tag, other circumstance | 19 | 1.2% |
| same family | 76 | 4.6% |
| different | 687 | 41.9% |
| they explain, we don't | 351 | 21.4% |
| we explain, they don't | 81 | 4.9% |
| neither | 51 | 3.1% |

Bad by Chess.com but not by us: 347 plies (our labels: {'good': 245, 'excellent': 65, 'best': 26, 'book': 11}).
Of the 1407 bad-move plies where we do not say Chess.com's tag, we detected it (in any circumstance) on 160.

### By Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| inaccuracy | 825 | 58 (7.0%) | 4 (0.5%) | 17 (2.1%) | 202 (24.5%) | 412 (49.9%) | 41 (5.0%) | 91 (11.0%) |
| mistake | 616 | 114 (18.5%) | 1 (0.2%) | 29 (4.7%) | 256 (41.6%) | 175 (28.4%) | 28 (4.5%) | 13 (2.1%) |
| blunder | 228 | 106 (46.5%) | 4 (1.8%) | 14 (6.1%) | 95 (41.7%) | 6 (2.6%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 98 (30.7%) | 10 (3.1%) | 16 (5.0%) | 134 (42.0%) | 51 (16.0%) | 9 (2.8%) | 1 (0.3%) |

### By phase

| phase | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| opening | 602 | 88 (14.6%) | 1 (0.2%) | 16 (2.7%) | 179 (29.7%) | 260 (43.2%) | 22 (3.7%) | 36 (6.0%) |
| middlegame | 921 | 200 (21.7%) | 9 (1.0%) | 47 (5.1%) | 340 (36.9%) | 253 (27.5%) | 36 (3.9%) | 36 (3.9%) |
| endgame | 465 | 88 (18.9%) | 9 (1.9%) | 13 (2.8%) | 168 (36.1%) | 131 (28.2%) | 23 (4.9%) | 33 (7.1%) |

## All plies by Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| brilliant | 25 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 1 (4.0%) | 23 (92.0%) | 0 (0.0%) | 1 (4.0%) |
| great | 321 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 319 (99.4%) | 0 (0.0%) | 2 (0.6%) |
| best | 2621 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 3 (0.1%) | 2330 (88.9%) | 1 (0.0%) | 287 (11.0%) |
| excellent | 1473 | 0 (0.0%) | 1 (0.1%) | 1 (0.1%) | 15 (1.0%) | 1194 (81.1%) | 3 (0.2%) | 259 (17.6%) |
| good | 1116 | 0 (0.0%) | 3 (0.3%) | 2 (0.2%) | 57 (5.1%) | 821 (73.6%) | 20 (1.8%) | 213 (19.1%) |
| book | 980 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 293 (29.9%) | 0 (0.0%) | 687 (70.1%) |
| forced | 114 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 114 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| inaccuracy | 825 | 58 (7.0%) | 4 (0.5%) | 17 (2.1%) | 202 (24.5%) | 412 (49.9%) | 41 (5.0%) | 91 (11.0%) |
| mistake | 616 | 114 (18.5%) | 1 (0.2%) | 29 (4.7%) | 256 (41.6%) | 175 (28.4%) | 28 (4.5%) | 13 (2.1%) |
| blunder | 228 | 106 (46.5%) | 4 (1.8%) | 14 (6.1%) | 95 (41.7%) | 6 (2.6%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 98 (30.7%) | 10 (3.1%) | 16 (5.0%) | 134 (42.0%) | 51 (16.0%) | 9 (2.8%) | 1 (0.3%) |

## Chess.com's main event on bad moves, by family

| family | plies | share |
|---|---|---|
| bad-move base | 374 | 18.8% |
| positional | 344 | 17.3% |
| defence | 338 | 17.0% |
| free material | 219 | 11.0% |
| (none) | 186 | 9.4% |
| double attack | 135 | 6.8% |
| mate | 117 | 5.9% |
| trade | 67 | 3.4% |
| line tactic | 64 | 3.2% |
| game | 50 | 2.5% |
| evaluation | 36 | 1.8% |
| sacrifice | 33 | 1.7% |
| defender tactic | 22 | 1.1% |
| other | 2 | 0.1% |
| promotion | 1 | 0.1% |

## Chess.com's most frequent main events on bad moves

| Chess.com event | plies | ours exact |
|---|---|---|
| permits>LosesMaterial | 235 | 44 |
| misses>CaptureThreat | 206 | 0 |
| - | 186 | 0 |
| permits>FreePiece | 97 | 7 |
| misses>FreePiece | 89 | 55 |
| permits>wins_material>Fork | 50 | 29 |
| permits>ForcesMate | 49 | 32 |
| HangsPiece | 48 | 34 |
| misses>Critical | 42 | 0 |
| RemovesOwnDefender | 38 | 30 |
| misses>EvadesCheck | 23 | 0 |
| misses>DevelopsCenter | 23 | 0 |
| misses>DefendsPiece | 22 | 0 |
| permits>wins_material>PileTrade | 22 | 0 |
| misses>wins_material>Fork | 21 | 10 |
| misses>DirectSacrificeCapture | 21 | 0 |
| misses>ObviousRetreat | 21 | 0 |
| permits>leads_to>Fork | 20 | 9 |
| misses>EscapesThreat | 20 | 0 |
| misses>ObviousRecapture | 19 | 0 |
| MovesSamePieceInOpening | 19 | 0 |
| misses>CastlesKingSide | 18 | 0 |
| EqualToWorse | 18 | 0 |
| permits>Checkmate | 17 | 16 |
| MovesPawnInFrontOfKing | 15 | 0 |

## Disagreement patterns on plies both apps label bad (Chess.com → ours)

| Chess.com | ours | category | plies | we detected theirs | examples |
|---|---|---|---|---|---|
| misses>CaptureThreat | - | they explain, we don't | 71 | 0 | 1011026868 9...b5; 142866059618 17.Kd3; 142873206408 6.a3; 145833178628 3...Bc5 |
| permits>FreePiece | ignores_threat | different | 56 | 55 | 1041474766 12...Nxd5; 142873206408 12...O-O-O; 142918703388 24.Rxc5; 147295227566 7.Bb5 |
| permits>LosesMaterial | ignores_threat | same family | 22 | 2 | 142849919300 9.Na4; 142918703388 20...Bc5; 145833178628 21.Kc2; 147295227566 9...Be7 |
| misses>Critical | - | they explain, we don't | 20 | 0 | 147991742972 19...Rfd8; 164784324724 7...h6; 166853117390 9.Bg3; 167397747616 38.Kh5 |
| misses>CaptureThreat | misses>material_gain | different | 17 | 0 | 1011026868 8...a6; 142636591844 5.d3; 147295227566 24...fxe4; 148224127998 24.Ra4 |
| MovesSamePieceInOpening | - | they explain, we don't | 14 | 0 | 142849698970 8.Ng5; 147991742972 8.Ke1; 173618554654 7.Nb5; 184555832944 8.Bb3 |
| permits>LosesMaterial | - | they explain, we don't | 13 | 0 | 1034847688 16.Bxg7; 145833758308 7...Ng6; 145833758308 35.Rg4; 165327199736 18.Nc7 |
| permits>FreePiece | bad_trade | different | 13 | 13 | 142849919300 7...Nxd5; 148224127998 8...Bxa3; 164008171476 22.Bxe6+; 166096155098 5...Nxe4 |
| permits>LosesMaterial | permits>leads_to>fork | different | 12 | 1 | 147786569400 19...Nf6; 166583201950 31.Qe5+; 168148201932 22...Re8; 168426135116 15.Bxf6 |
| misses>ObviousRetreat | - | they explain, we don't | 12 | 0 | 147991742972 19.Qxa7; 170185678278 9.Na4; 170185678278 9...Bd4; 171980080646 22...Qxa3 |
| permits>ForcesMate | permits>back_rank_mate | same family | 12 | 0 | 166096155098 13...Bh3; 166096155098 14...Kf8; 166583201950 25.Rc1; 167316688806 22...Rfxb8 |
| permits>LosesMaterial | permits>free_piece | different | 11 | 0 | 142849919300 11.h4; 142849919300 12.Kd1; 142849919300 13.Ne4; 142875589252 15.Ne2 |
| - | misses>free_piece | we explain, they don't | 11 | 0 | 147295227566 9.Re1+; 147295227566 18...Bg5; 166853117390 16.Qh5+; 170185678278 6...Bc5 |
| misses>CastlesKingSide | - | they explain, we don't | 10 | 0 | 1034847688 5.c4; 147786569400 6...c5; 173618554654 8...dxc2; 173618554654 10...Bxf3 |
| misses>DevelopsCenter | - | they explain, we don't | 10 | 0 | 145833758308 7.Bd2; 173904334944 5.c3; 173904334944 7.Na3; 173905398948 12.Nd5 |
| - | permits>material_gain | we explain, they don't | 10 | 0 | 147234657424 15.Qh5+; 164462806840 18...g4; 167359572290 9...O-O-O; 173667762936 11.Qc4 |
| EqualToWorse | - | they explain, we don't | 10 | 0 | 184740374128 17...h6; 184759290504 18.f4; 184873703892 34...Qh3; 185277691132 7...Nb4 |
| permits>LosesMaterial | misses>free_piece | different | 9 | 3 | 166583201950 21.f3; 166853117390 14...Kh8; 167359572290 14...Bd6; 173667762936 19.Nc3 |
| HangsPiece | permits>free_piece | different | 8 | 8 | 142849698970 18...Qg5+; 165327199736 19.Qc2; 166583201950 20...Ne4; 166583201950 22...Ne4+ |
| permits>LosesMaterial | permits>wins_material>fork | different | 8 | 0 | 145833758308 30.Nd5; 184110410320 15.Kb1; 185117573448 26.Rxe5; 185216623720 25...Qxf2 |
| misses>CaptureThreat | misses>free_piece | different | 7 | 0 | 142849698970 15...Ne2+; 142875589252 17...Bb4+; 147547838342 12...Bg4; 166583201950 11.Nd3 |
| - | permits>forced_mate | we explain, they don't | 7 | 0 | 142873206408 38...h5; 142873206408 42...Kg4; 164784324724 46...Kd8; 184678264914 32.Rxc7 |
| - | misses>material_gain | we explain, they don't | 7 | 0 | 142918703388 5...a6; 147786569400 8.h4; 173855642488 16.Qe2; 184028735740 31.Qxd4+ |
| permits>wins_material>Fork | permits>free_piece | different | 7 | 0 | 142918703388 16.b4; 146658193946 10...d4; 146658193946 11...Nbd7; 165401252676 12...Bb6 |
| permits>LosesMaterial | permits>wins_material>discovered_attack | different | 7 | 1 | 146658193946 24...Ne4; 164008171476 13...Nbd7; 173570784620 29...Re8; 184809655978 14.Qh8+ |
| permits>LosesMaterial | permits>leads_to>removes_defender | different | 7 | 1 | 164188880582 18.Re1; 164784324724 33...Re1; 167479014786 27.b4; 171124015136 22...Nc6 |
| permits>LosesMaterial | permits>forced_mate | different | 7 | 0 | 164784324724 41...a5; 165557442658 29.Kf1; 166583201950 30.Kf4; 171124015136 38...Kh8 |
| misses>DirectSacrificeCapture | - | they explain, we don't | 7 | 0 | 164812402934 5.Bb5; 165327199736 10.Bb3; 184829980734 17.Rcd1; 185334658860 13...Bg4 |
| TooEarlyQueenDevelopment | - | they explain, we don't | 7 | 0 | 184732665836 8...Qa5; 184809852108 13...Qb6; 184810276410 4...Qb6; 185151408586 6...Qe7 |
| misses>ObviousRecapture | - | they explain, we don't | 6 | 0 | 1034847688 16...Nxg7; 1034847688 23...Kxf7; 171841312410 7...dxe5; 173620121124 15.Bb4+ |
