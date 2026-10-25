# Coach agreement with Chess.com (Phase 0)

Run `coach-quickfix`, 142 games, 8638 plies, commit `cb1b475`. Reference: the main event of Chess.com's speech for the played move.

## Bad moves (Chess.com Inaccuracy, Mistake, Blunder, Miss)

| category | plies | share |
|---|---|---|
| exact | 485 | 24.4% |
| same tag, other circumstance | 66 | 3.3% |
| same family | 62 | 3.1% |
| different | 753 | 37.9% |
| they explain, we don't | 436 | 21.9% |
| we explain, they don't | 103 | 5.2% |
| neither | 83 | 4.2% |

Where both explain (1366 plies): exact 35.5%, same tag 40.3%, same family or better 44.9%.

### Plies both apps label bad (1641 of 1988)

Phase 1 explains only moves we label Inaccuracy, Mistake, Blunder or Miss, so this is the coach's own agreement, free of label disagreements.

| category | plies | share |
|---|---|---|
| exact | 485 | 29.6% |
| same tag, other circumstance | 43 | 2.6% |
| same family | 49 | 3.0% |
| different | 629 | 38.3% |
| they explain, we don't | 303 | 18.5% |
| we explain, they don't | 86 | 5.2% |
| neither | 46 | 2.8% |

Bad by Chess.com but not by us: 347 plies (our labels: {'good': 245, 'excellent': 65, 'best': 26, 'book': 11}).
Of the 1251 bad-move plies where we do not say Chess.com's tag, we detected it (in any circumstance) on 103.

### By Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| inaccuracy | 825 | 83 (10.1%) | 36 (4.4%) | 16 (1.9%) | 288 (34.9%) | 270 (32.7%) | 58 (7.0%) | 74 (9.0%) |
| mistake | 616 | 163 (26.5%) | 9 (1.5%) | 22 (3.6%) | 261 (42.4%) | 120 (19.5%) | 33 (5.4%) | 8 (1.3%) |
| blunder | 228 | 141 (61.8%) | 4 (1.8%) | 9 (3.9%) | 67 (29.4%) | 4 (1.8%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 98 (30.7%) | 17 (5.3%) | 15 (4.7%) | 137 (42.9%) | 42 (13.2%) | 9 (2.8%) | 1 (0.3%) |

### By phase

| phase | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| opening | 602 | 120 (19.9%) | 21 (3.5%) | 12 (2.0%) | 188 (31.2%) | 203 (33.7%) | 30 (5.0%) | 28 (4.7%) |
| middlegame | 921 | 251 (27.3%) | 26 (2.8%) | 37 (4.0%) | 388 (42.1%) | 147 (16.0%) | 43 (4.7%) | 29 (3.1%) |
| endgame | 465 | 114 (24.5%) | 19 (4.1%) | 13 (2.8%) | 177 (38.1%) | 86 (18.5%) | 30 (6.5%) | 26 (5.6%) |

## All plies by Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| brilliant | 25 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 19 (76.0%) | 5 (20.0%) | 1 (4.0%) | 0 (0.0%) |
| great | 321 | 141 (43.9%) | 4 (1.2%) | 12 (3.7%) | 129 (40.2%) | 33 (10.3%) | 2 (0.6%) | 0 (0.0%) |
| best | 2621 | 623 (23.8%) | 27 (1.0%) | 89 (3.4%) | 876 (33.4%) | 718 (27.4%) | 135 (5.2%) | 153 (5.8%) |
| excellent | 1473 | 306 (20.8%) | 8 (0.5%) | 21 (1.4%) | 335 (22.7%) | 541 (36.7%) | 89 (6.0%) | 173 (11.7%) |
| good | 1116 | 180 (16.1%) | 12 (1.1%) | 12 (1.1%) | 297 (26.6%) | 382 (34.2%) | 77 (6.9%) | 156 (14.0%) |
| book | 980 | 18 (1.8%) | 0 (0.0%) | 0 (0.0%) | 33 (3.4%) | 242 (24.7%) | 2 (0.2%) | 685 (69.9%) |
| forced | 114 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 114 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| inaccuracy | 825 | 83 (10.1%) | 36 (4.4%) | 16 (1.9%) | 288 (34.9%) | 270 (32.7%) | 58 (7.0%) | 74 (9.0%) |
| mistake | 616 | 163 (26.5%) | 9 (1.5%) | 22 (3.6%) | 261 (42.4%) | 120 (19.5%) | 33 (5.4%) | 8 (1.3%) |
| blunder | 228 | 141 (61.8%) | 4 (1.8%) | 9 (3.9%) | 67 (29.4%) | 4 (1.8%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 98 (30.7%) | 17 (5.3%) | 15 (4.7%) | 137 (42.9%) | 42 (13.2%) | 9 (2.8%) | 1 (0.3%) |

## Good moves (Chess.com brilliant, great, great_find, best, excellent, good; 5349 plies both apps label good)

| category | plies | share |
|---|---|---|
| exact | 1249 | 23.4% |
| same tag, other circumstance | 46 | 0.9% |
| same family | 130 | 2.4% |
| different | 1571 | 29.4% |
| they explain, we don't | 1610 | 30.1% |
| we explain, they don't | 279 | 5.2% |
| neither | 464 | 8.7% |

### Chess.com's main event on good moves, by family

| family | plies | share |
|---|---|---|
| positional | 1302 | 24.3% |
| defence | 1228 | 23.0% |
| trade | 889 | 16.6% |
| (none) | 743 | 13.9% |
| free material | 429 | 8.0% |
| mate | 306 | 5.7% |
| double attack | 237 | 4.4% |
| line tactic | 111 | 2.1% |
| game | 39 | 0.7% |
| sacrifice | 29 | 0.5% |
| defender tactic | 25 | 0.5% |
| promotion | 8 | 0.1% |
| other | 3 | 0.1% |

### Disagreement patterns on good moves (Chess.com → ours)

| Chess.com | ours | category | plies | examples |
|---|---|---|---|---|
| EvadesCheck | - | they explain, we don't | 174 | 142849919300 21.Ke3; 142849919300 23.Kc4; 142866059618 41.Kd6 |
| ObviousRecapture | - | they explain, we don't | 157 | 1011026868 15...Kxg7; 1034847688 13.Kxe2; 1034847688 18.hxg5 |
| DevelopsCenter | - | they explain, we don't | 126 | 1011026868 7.Be3; 1034847688 2...Nf6; 1034847688 7...Nc6 |
| EqualTrade | - | they explain, we don't | 115 | 1041474766 9.dxe5; 142849698970 10...Bxc4; 142866059618 7.Bxg6 |
| Kicks | threatens>free_piece | different | 109 | 1034847688 8.d5; 1041474766 11.a3; 142849698970 6.h3 |
| PreparesToCastleKingside | - | they explain, we don't | 70 | 1011026868 5.Bc4; 1011026868 7...Nge7; 142636591844 4.Bc4 |
| - | free_piece | we explain, they don't | 65 | 142636591844 9.Nxh7; 142849919300 13...Qxd3+; 142849919300 16...Qxh1 |
| CastlesKingSide | - | they explain, we don't | 60 | 1011026868 11...O-O; 1034847688 5...O-O; 1041474766 7.O-O |
| EqualTrade | prevents>free_piece | different | 60 | 1034847688 23.exf7+; 142873206408 35...Rxe4; 142917385540 3...exd3 |
| PreparesBishopDevelopment | - | they explain, we don't | 56 | 1011026868 4...g6; 1011026868 6.d3; 1034847688 3...g6 |
| CastlesSameSide | - | they explain, we don't | 50 | 1011026868 12.O-O; 1041474766 10...O-O; 147295227566 11...O-O |
| ObviousRecapture | prevents>free_piece | different | 42 | 1034847688 20.gxf3; 142849698970 9...Bxf7; 142866059618 16...bxa6 |
| WinsTempo | threatens>free_piece | different | 39 | 142849919300 8...Nb4; 142918703388 14.Bb6; 147234657424 20...Na5 |
| ImmediateRecapture | - | they explain, we don't | 37 | 142866059618 22...Rxd8; 145833178628 11...dxe4; 146658193946 14.dxe4 |
| EqualTrade | removes_defender | different | 36 | 1011026868 15.Bxg7; 1034847688 19...Nxf3; 142873206408 7...exf4 |
| StrikesAtCenter | - | they explain, we don't | 36 | 1041474766 8.d4; 142873206408 6...e5; 142918703388 15...d5 |
| wins_material>PileTrade | free_piece | different | 36 | 142866059618 14.Bxd4; 142873206408 19.Bxc3; 142918703388 7.Bxe6 |
| MovesToActiveSquare | - | they explain, we don't | 35 | 164188880582 15...Rfe8; 164462806840 12...Nb6; 164812402934 13...Re8 |
| OffersTrade | - | they explain, we don't | 34 | 164784324724 8...Nd4; 164784324724 26.Nf7+; 165974850998 8...Nd4 |
| - | material_gain | we explain, they don't | 33 | 142866059618 9.g5; 145833758308 27.exd6; 147234657424 10.Bxe6+ |
| PushesPassedPawnEndgame | - | they explain, we don't | 32 | 142866059618 36...f4; 142866059618 37...f3; 142866059618 43.e6 |
| StillMate | forced_mate | same family | 32 | 142866059618 51...Kc4; 145833178628 32...Qd3+; 147547838342 19...Re8 |
| PutsPawnInCenter | - | they explain, we don't | 31 | 1034847688 3.d4; 1041474766 7...e5; 147619991314 7.d4 |
| - | threatens>free_piece | we explain, they don't | 31 | 142873206408 44...Kh3; 145833758308 54.Ke7; 148224127998 25.Rb1 |
| ConnectsRooks | - | they explain, we don't | 29 | 1011026868 13.Qd2; 1011026868 13...Qd7; 142866059618 18...Ne7 |

## The best-move sentence on plies both label bad (1427 with a sentence on either side)

Chess.com's speech for the best alternative against our Misses-block event, without the "misses" step.

| category | plies | share |
|---|---|---|
| exact | 172 | 12.1% |
| same tag, other circumstance | 14 | 1.0% |
| same family | 13 | 0.9% |
| different | 299 | 21.0% |
| they explain, we don't | 869 | 60.9% |
| we explain, they don't | 60 | 4.2% |
| neither | 0 | 0.0% |

### Patterns (Chess.com → ours)

| Chess.com | ours | category | plies | examples |
|---|---|---|---|---|
| Retreat | - | they explain, we don't | 59 | 1041474766 12...Nxd5; 142849698970 15.Qf7; 142849919300 9.Na4 |
| DefendsPiece | - | they explain, we don't | 56 | 142636591844 3...Bd6; 142849698970 18...Qg5+; 146658193946 4...Ng4 |
| EscapesThreat | - | they explain, we don't | 53 | 142849919300 7...Nxd5; 142917385540 17.hxg4; 142917385540 18.Qxg4 |
| EvadesCheck | - | they explain, we don't | 47 | 1034847688 24...Ke8; 142849919300 12.Kd1; 142849919300 24.Nd3 |
| Kicks | - | they explain, we don't | 42 | 1034847688 16.Bxg7; 145833758308 8.e5; 147295227566 4...c5 |
| EqualTrade | - | they explain, we don't | 38 | 142849919300 10.Qh5; 142866059618 19...Nd5; 142873206408 12...O-O-O |
| DevelopsCenter | - | they explain, we don't | 31 | 142873206408 6.a3; 142873206408 7.b4; 145833758308 7.Bd2 |
| StrikesAtCenter | - | they explain, we don't | 30 | 1011026868 8.Rb1; 1011026868 9...b5; 1011026868 16...h6 |
| ObviousRecapture | - | they explain, we don't | 24 | 1034847688 16...Nxg7; 1034847688 23...Kxf7; 142866059618 13.Ke2 |
| BlocksChecker | - | they explain, we don't | 24 | 142636591844 17...Kg7; 142875589252 7...c6; 142875589252 15.Ne2 |
| MovesToActiveSquare | - | they explain, we don't | 24 | 164784324724 32...Rfe8; 167397747616 21...Rae8; 168148201932 19.Rfe1 |
| - | free_piece | we explain, they don't | 22 | 142918703388 24.Rxc5; 147295227566 9.Re1+; 166583201950 33.Qxe3 |
| ProtectsPiece | - | they explain, we don't | 21 | 145833758308 13.Be3; 147547838342 11.exd5; 147547838342 15.gxf3 |
| WinsTempo | - | they explain, we don't | 20 | 142873206408 16...Nb5; 147619991314 20...Be5; 147742438276 7...c5 |
| BlocksAttacker | - | they explain, we don't | 16 | 142849919300 11.h4; 142849919300 13.Ne4; 142917385540 10...f6 |
| AttacksPawnChain | - | they explain, we don't | 15 | 1034847688 15.Rad1; 1034847688 17.cxb5; 184449650784 14.Nfd2 |
| - | material_gain | we explain, they don't | 15 | 142918703388 5...a6; 148224127998 16.Bxd5; 173855642488 16.Qe2 |
| DevelopsMiddlegame | - | they explain, we don't | 15 | 166853117390 13...d5; 171887823168 16.Rfe1; 184271279368 14.Qf5+ |
| DevelopsOpening | - | they explain, we don't | 14 | 142849698970 8.Ng5; 147547838342 8...Nxc4; 147742438276 5...f6 |
| Critical | - | they explain, we don't | 13 | 165557442658 29.Kf1; 167397747616 38.Kh5; 171887823168 17...Ng8 |
| PreparesToCastleKingside | - | they explain, we don't | 12 | 1034847688 5.c4; 142636591844 4...Ne7; 142875589252 11...d5 |
| PreparesBishopDevelopment | - | they explain, we don't | 12 | 142849919300 6...d5; 142917385540 12...O-O-O; 167359572290 7...Bxd3 |
| CentralBreak | - | they explain, we don't | 12 | 142866059618 6.Bd3; 147234657424 5.Ng5; 173807034866 19...Qh4 |
| ConnectsRooks | - | they explain, we don't | 12 | 142866059618 17.Kd3; 147234657424 16.Qxc5; 147786569400 19...Nf6 |
| wins_material>PileTrade | free_piece | different | 11 | 142866059618 20...Nxc3; 148014224206 13...Nf6; 164462806840 14...b6 |

## Chess.com's main event on bad moves, by family

| family | plies | share |
|---|---|---|
| bad-move base | 374 | 18.8% |
| defence | 345 | 17.4% |
| positional | 344 | 17.3% |
| free material | 219 | 11.0% |
| (none) | 186 | 9.4% |
| double attack | 135 | 6.8% |
| mate | 117 | 5.9% |
| line tactic | 64 | 3.2% |
| trade | 60 | 3.0% |
| game | 50 | 2.5% |
| evaluation | 36 | 1.8% |
| sacrifice | 33 | 1.7% |
| defender tactic | 22 | 1.1% |
| other | 2 | 0.1% |
| promotion | 1 | 0.1% |

## Chess.com's most frequent main events on bad moves

| Chess.com event | plies | ours exact |
|---|---|---|
| permits>LosesMaterial | 235 | 74 |
| misses>CaptureThreat | 206 | 0 |
| - | 186 | 0 |
| permits>FreePiece | 97 | 70 |
| misses>FreePiece | 89 | 53 |
| permits>wins_material>Fork | 50 | 25 |
| permits>ForcesMate | 49 | 44 |
| HangsPiece | 48 | 42 |
| misses>Critical | 42 | 0 |
| RemovesOwnDefender | 38 | 34 |
| misses>EvadesCheck | 23 | 0 |
| misses>DevelopsCenter | 23 | 0 |
| misses>DefendsPiece | 22 | 0 |
| permits>wins_material>PileTrade | 22 | 0 |
| misses>wins_material>Fork | 21 | 10 |
| misses>DirectSacrificeCapture | 21 | 0 |
| misses>ObviousRetreat | 21 | 0 |
| permits>leads_to>Fork | 20 | 4 |
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
| misses>CaptureThreat | - | they explain, we don't | 53 | 0 | 142873206408 6.a3; 145833178628 3...Bc5; 145833178628 9.Qxb7; 145833178628 11.dxe4 |
| misses>CaptureThreat | misses>material_gain | different | 17 | 0 | 1011026868 8...a6; 142636591844 5.d3; 147295227566 24...fxe4; 148224127998 24.Ra4 |
| permits>LosesMaterial | permits>free_piece | different | 17 | 1 | 142849919300 9.Na4; 142875589252 15.Ne2; 142918703388 20...Bc5; 145833178628 21.Kc2 |
| misses>Critical | - | they explain, we don't | 17 | 0 | 147991742972 19...Rfd8; 166853117390 9.Bg3; 167397747616 38.Kh5; 184555832944 7...Nd6 |
| misses>CaptureThreat | threatens>free_piece | same tag, other circumstance | 14 | 0 | 1011026868 9...b5; 142866059618 17.Kd3; 145833758308 8.e5; 147991742972 5.f4 |
| MovesSamePieceInOpening | - | they explain, we don't | 14 | 0 | 142849698970 8.Ng5; 147991742972 8.Ke1; 173618554654 7.Nb5; 184555832944 8.Bb3 |
| misses>CaptureThreat | permits>material_gain | different | 13 | 0 | 1034847688 15.Rad1; 142918703388 5.d3; 165557442658 26.Qxf7; 168148201932 21.c4 |
| - | permits>material_gain | we explain, they don't | 13 | 0 | 147234657424 15.Qh5+; 164462806840 18...g4; 167359572290 9...O-O-O; 173667762936 11.Qc4 |
| misses>CastlesKingSide | - | they explain, we don't | 11 | 0 | 1034847688 5.c4; 147786569400 6...c5; 173618554654 8...dxc2; 173618554654 10...Bxf3 |
| - | misses>free_piece | we explain, they don't | 11 | 0 | 147295227566 9.Re1+; 147295227566 18...Bg5; 166853117390 16.Qh5+; 170185678278 6...Bc5 |
| permits>LosesMaterial | ignores_threat | same family | 10 | 4 | 145833758308 30.Nd5; 166853117390 12...c6; 172026321412 9...a6; 173620121124 19...Bh5 |
| misses>ObviousRetreat | - | they explain, we don't | 10 | 0 | 147991742972 19.Qxa7; 170185678278 9.Na4; 170185678278 9...Bd4; 171980080646 22...Qxa3 |
| permits>LosesMaterial | - | they explain, we don't | 9 | 0 | 1034847688 16.Bxg7; 145833758308 7...Ng6; 145833758308 35.Rg4; 171887823168 10...Qc7 |
| permits>LosesMaterial | permits>wins_material>discovered_attack | different | 8 | 1 | 146658193946 24...Ne4; 164008171476 13...Nbd7; 168426135116 15.Bxf6; 173570784620 29...Re8 |
| permits>LosesMaterial | misses>free_piece | different | 8 | 5 | 166583201950 21.f3; 167359572290 14...Bd6; 173667762936 19.Nc3; 184028735740 29...Kb6 |
| misses>DevelopsCenter | - | they explain, we don't | 8 | 0 | 173904334944 5.c3; 173904334944 7.Na3; 173905398948 12.Nd5; 174188274588 8...O-O |
| EqualToWorse | - | they explain, we don't | 8 | 0 | 184873703892 34...Qh3; 185277691132 7...Nb4; 185456088510 11...Bg7; 185456088510 12...c5 |
| misses>CaptureThreat | misses>free_piece | different | 7 | 0 | 142849698970 15...Ne2+; 142875589252 17...Bb4+; 147547838342 12...Bg4; 166583201950 11.Nd3 |
| - | permits>forced_mate | we explain, they don't | 7 | 0 | 142873206408 38...h5; 142873206408 42...Kg4; 164784324724 46...Kd8; 184678264914 32.Rxc7 |
| - | misses>material_gain | we explain, they don't | 7 | 0 | 142918703388 5...a6; 147786569400 8.h4; 173855642488 16.Qe2; 184028735740 31.Qxd4+ |
| permits>wins_material>Fork | permits>material_gain | different | 7 | 0 | 146658193946 11...Nbd7; 147547838342 15.gxf3; 165401252676 12...Bb6; 169217872990 17.Nc3 |
| - | permits>free_piece | we explain, they don't | 7 | 0 | 147234657424 7.Nxf7; 169217872990 19.Ne4; 169217872990 23.Qxe8; 173905398948 26...Rxc2 |
| permits>LosesMaterial | permits>forced_mate | different | 7 | 0 | 164784324724 41...a5; 165557442658 29.Kf1; 166583201950 30.Kf4; 171124015136 38...Kh8 |
| permits>LosesMaterial | permits>wins_material>removes_defender | different | 7 | 0 | 165974850998 21...Bc7; 165974850998 22...Bd6; 171841312410 16.O-O; 184678264914 20.Rb1 |
| IgnoresAttackedPiece | permits>free_piece | different | 7 | 7 | 166583201950 6...Bg4; 167479014786 23.Qe7; 168426135116 18...Qc6; 173905398948 13.Bf4 |
