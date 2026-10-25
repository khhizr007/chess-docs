# Coach agreement with Chess.com (Phase 0)

Run `coach-main-e4ead28`, 142 games, 8638 plies, commit `e4ead28`. Reference: the main event of Chess.com's speech for the played move.

## Bad moves (Chess.com Inaccuracy, Mistake, Blunder, Miss)

| category | plies | share |
|---|---|---|
| exact | 371 | 18.7% |
| same tag, other circumstance | 57 | 2.9% |
| same family | 91 | 4.6% |
| different | 849 | 42.7% |
| they explain, we don't | 434 | 21.8% |
| we explain, they don't | 103 | 5.2% |
| neither | 83 | 4.2% |

Where both explain (1368 plies): exact 27.1%, same tag 31.3%, same family or better 37.9%.

### Plies both apps label bad (1641 of 1988)

Phase 1 explains only moves we label Inaccuracy, Mistake, Blunder or Miss, so this is the coach's own agreement, free of label disagreements.

| category | plies | share |
|---|---|---|
| exact | 371 | 22.6% |
| same tag, other circumstance | 34 | 2.1% |
| same family | 78 | 4.8% |
| different | 725 | 44.2% |
| they explain, we don't | 301 | 18.3% |
| we explain, they don't | 86 | 5.2% |
| neither | 46 | 2.8% |

Bad by Chess.com but not by us: 347 plies (our labels: {'good': 245, 'excellent': 65, 'best': 26, 'book': 11}).
Of the 1374 bad-move plies where we do not say Chess.com's tag, we detected it (in any circumstance) on 160.

### By Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| inaccuracy | 825 | 58 (7.0%) | 34 (4.1%) | 27 (3.3%) | 304 (36.8%) | 270 (32.7%) | 58 (7.0%) | 74 (9.0%) |
| mistake | 616 | 113 (18.3%) | 7 (1.1%) | 30 (4.9%) | 306 (49.7%) | 119 (19.3%) | 33 (5.4%) | 8 (1.3%) |
| blunder | 228 | 105 (46.1%) | 4 (1.8%) | 14 (6.1%) | 98 (43.0%) | 4 (1.8%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 95 (29.8%) | 12 (3.8%) | 20 (6.3%) | 141 (44.2%) | 41 (12.9%) | 9 (2.8%) | 1 (0.3%) |

### By phase

| phase | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| opening | 602 | 87 (14.5%) | 16 (2.7%) | 21 (3.5%) | 218 (36.2%) | 202 (33.6%) | 30 (5.0%) | 28 (4.7%) |
| middlegame | 921 | 197 (21.4%) | 24 (2.6%) | 52 (5.6%) | 429 (46.6%) | 147 (16.0%) | 43 (4.7%) | 29 (3.1%) |
| endgame | 465 | 87 (18.7%) | 17 (3.7%) | 18 (3.9%) | 202 (43.4%) | 85 (18.3%) | 30 (6.5%) | 26 (5.6%) |

## All plies by Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| brilliant | 25 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 19 (76.0%) | 5 (20.0%) | 1 (4.0%) | 0 (0.0%) |
| great | 321 | 136 (42.4%) | 4 (1.2%) | 18 (5.6%) | 128 (39.9%) | 33 (10.3%) | 2 (0.6%) | 0 (0.0%) |
| best | 2621 | 615 (23.5%) | 28 (1.1%) | 98 (3.7%) | 875 (33.4%) | 717 (27.4%) | 135 (5.2%) | 153 (5.8%) |
| excellent | 1473 | 304 (20.6%) | 8 (0.5%) | 25 (1.7%) | 333 (22.6%) | 541 (36.7%) | 89 (6.0%) | 173 (11.7%) |
| good | 1116 | 180 (16.1%) | 12 (1.1%) | 13 (1.2%) | 296 (26.5%) | 382 (34.2%) | 77 (6.9%) | 156 (14.0%) |
| book | 980 | 18 (1.8%) | 0 (0.0%) | 0 (0.0%) | 33 (3.4%) | 242 (24.7%) | 2 (0.2%) | 685 (69.9%) |
| forced | 114 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 114 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| inaccuracy | 825 | 58 (7.0%) | 34 (4.1%) | 27 (3.3%) | 304 (36.8%) | 270 (32.7%) | 58 (7.0%) | 74 (9.0%) |
| mistake | 616 | 113 (18.3%) | 7 (1.1%) | 30 (4.9%) | 306 (49.7%) | 119 (19.3%) | 33 (5.4%) | 8 (1.3%) |
| blunder | 228 | 105 (46.1%) | 4 (1.8%) | 14 (6.1%) | 98 (43.0%) | 4 (1.8%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 95 (29.8%) | 12 (3.8%) | 20 (6.3%) | 141 (44.2%) | 41 (12.9%) | 9 (2.8%) | 1 (0.3%) |

## Good moves (Chess.com brilliant, great, great_find, best, excellent, good; 5349 plies both apps label good)

| category | plies | share |
|---|---|---|
| exact | 1234 | 23.1% |
| same tag, other circumstance | 47 | 0.9% |
| same family | 151 | 2.8% |
| different | 1565 | 29.3% |
| they explain, we don't | 1609 | 30.1% |
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
| EvadesCheck | - | they explain, we don't | 175 | 142849919300 21.Ke3; 142849919300 23.Kc4; 142866059618 41.Kd6 |
| ObviousRecapture | - | they explain, we don't | 156 | 1011026868 15...Kxg7; 1034847688 13.Kxe2; 1034847688 18.hxg5 |
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
| WinsTempo | threatens>free_piece | different | 38 | 142849919300 8...Nb4; 142918703388 14.Bb6; 147234657424 20...Na5 |
| ImmediateRecapture | - | they explain, we don't | 37 | 142866059618 22...Rxd8; 145833178628 11...dxe4; 146658193946 14.dxe4 |
| EqualTrade | removes_defender | different | 36 | 1011026868 15.Bxg7; 1034847688 19...Nxf3; 142873206408 7...exf4 |
| StrikesAtCenter | - | they explain, we don't | 36 | 1041474766 8.d4; 142873206408 6...e5; 142918703388 15...d5 |
| wins_material>PileTrade | free_piece | different | 36 | 142866059618 14.Bxd4; 142873206408 19.Bxc3; 142918703388 7.Bxe6 |
| MovesToActiveSquare | - | they explain, we don't | 35 | 164188880582 15...Rfe8; 164462806840 12...Nb6; 164812402934 13...Re8 |
| OffersTrade | - | they explain, we don't | 34 | 164784324724 8...Nd4; 164784324724 26.Nf7+; 165974850998 8...Nd4 |
| PushesPassedPawnEndgame | - | they explain, we don't | 32 | 142866059618 36...f4; 142866059618 37...f3; 142866059618 43.e6 |
| - | material_gain | we explain, they don't | 32 | 145833758308 27.exd6; 147234657424 10.Bxe6+; 147742438276 9...fxe5 |
| PutsPawnInCenter | - | they explain, we don't | 31 | 1034847688 3.d4; 1041474766 7...e5; 147619991314 7.d4 |
| - | threatens>free_piece | we explain, they don't | 31 | 142873206408 44...Kh3; 145833758308 54.Ke7; 148224127998 25.Rb1 |
| StillMate | forced_mate | same family | 30 | 142866059618 51...Kc4; 145833178628 32...Qd3+; 147547838342 19...Re8 |
| ConnectsRooks | - | they explain, we don't | 29 | 1011026868 13.Qd2; 1011026868 13...Qd7; 142866059618 18...Ne7 |
| EqualTrade | free_piece | different | 28 | 142849919300 9...Qxd5; 142866059618 34...Bxf4; 142873206408 35.Nxg7 |
| DevelopsMiddlegame | - | they explain, we don't | 24 | 1011026868 12...Rc8; 142866059618 19.Rd1; 145833758308 17.Rd1 |
| TakesOpenFile | - | they explain, we don't | 24 | 142873206408 26.Re1; 142917385540 12.Rad1; 164007452224 14.Rfe1 |
| DevelopsRecapture | - | they explain, we don't | 23 | 142918703388 12.Qxf3; 145833178628 8...Nbxd7; 165450446440 12...Qxf6 |
| ObviousRecapture | threatens>free_piece | different | 22 | 142918703388 8.Nxe6; 147234657424 6...exd5; 147619991314 11.dxe5 |

## The best-move sentence on plies both label bad (1427 with a sentence on either side)

Chess.com's speech for the best alternative against our Misses-block event, without the "misses" step.

| category | plies | share |
|---|---|---|
| exact | 170 | 11.9% |
| same tag, other circumstance | 12 | 0.8% |
| same family | 18 | 1.3% |
| different | 303 | 21.2% |
| they explain, we don't | 864 | 60.5% |
| we explain, they don't | 60 | 4.2% |
| neither | 0 | 0.0% |

### Patterns (Chess.com → ours)

| Chess.com | ours | category | plies | examples |
|---|---|---|---|---|
| Retreat | - | they explain, we don't | 58 | 1041474766 12...Nxd5; 142849698970 15.Qf7; 142849919300 9.Na4 |
| DefendsPiece | - | they explain, we don't | 57 | 142636591844 3...Bd6; 142849698970 18...Qg5+; 146658193946 4...Ng4 |
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
| CounterThreat | - | they explain, we don't | 11 | 142917385540 15.Be3; 142918703388 19...Qd2; 164007452224 21.c4 |
| CastlesKingSide | - | they explain, we don't | 11 | 148224127998 18...Nxe4; 168148201932 7.d4; 184028735740 8.Qxh7 |
| CentralizesKnight | - | they explain, we don't | 10 | 147234657424 21...Qe8; 147786569400 18...a5; 164812402934 8...Nf4 |
| MateThreat | - | they explain, we don't | 9 | 145833758308 30.Nd5; 147295227566 15.Qe3; 167479014786 23.Qe7 |
| BishopGainsScope | - | they explain, we don't | 9 | 148224127998 28.Rc7; 169217872990 15.Bg4; 174468507028 11.Nd2 |

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
| permits>LosesMaterial | 235 | 44 |
| misses>CaptureThreat | 206 | 0 |
| - | 186 | 0 |
| permits>FreePiece | 97 | 5 |
| misses>FreePiece | 89 | 52 |
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
| permits>FreePiece | ignores_threat | different | 56 | 55 | 1041474766 12...Nxd5; 142873206408 12...O-O-O; 142918703388 24.Rxc5; 147295227566 7.Bb5 |
| misses>CaptureThreat | - | they explain, we don't | 53 | 0 | 142873206408 6.a3; 145833178628 3...Bc5; 145833178628 9.Qxb7; 145833178628 11.dxe4 |
| permits>LosesMaterial | ignores_threat | same family | 22 | 2 | 142849919300 9.Na4; 142918703388 20...Bc5; 145833178628 21.Kc2; 147295227566 9...Be7 |
| misses>CaptureThreat | misses>material_gain | different | 17 | 0 | 1011026868 8...a6; 142636591844 5.d3; 147295227566 24...fxe4; 148224127998 24.Ra4 |
| misses>Critical | - | they explain, we don't | 17 | 0 | 147991742972 19...Rfd8; 166853117390 9.Bg3; 167397747616 38.Kh5; 184555832944 7...Nd6 |
| MovesSamePieceInOpening | - | they explain, we don't | 14 | 0 | 142849698970 8.Ng5; 147991742972 8.Ke1; 173618554654 7.Nb5; 184555832944 8.Bb3 |
| misses>CaptureThreat | threatens>free_piece | same tag, other circumstance | 13 | 0 | 1011026868 9...b5; 142866059618 17.Kd3; 145833758308 8.e5; 147991742972 5.f4 |
| permits>FreePiece | bad_trade | different | 13 | 1 | 142849919300 7...Nxd5; 148224127998 8...Bxa3; 164008171476 22.Bxe6+; 166096155098 5...Nxe4 |
| permits>LosesMaterial | permits>leads_to>fork | different | 12 | 2 | 147786569400 19...Nf6; 166583201950 31.Qe5+; 168148201932 22...Re8; 168426135116 15.Bxf6 |
| permits>ForcesMate | permits>back_rank_mate | same family | 12 | 0 | 166096155098 13...Bh3; 166096155098 14...Kf8; 166583201950 25.Rc1; 167316688806 22...Rfxb8 |
| permits>LosesMaterial | permits>free_piece | different | 11 | 0 | 142849919300 11.h4; 142849919300 12.Kd1; 142849919300 13.Ne4; 142875589252 15.Ne2 |
| - | misses>free_piece | we explain, they don't | 11 | 0 | 147295227566 9.Re1+; 147295227566 18...Bg5; 166853117390 16.Qh5+; 170185678278 6...Bc5 |
| misses>CastlesKingSide | - | they explain, we don't | 10 | 0 | 1034847688 5.c4; 147786569400 6...c5; 173618554654 8...dxc2; 173618554654 10...Bxf3 |
| - | permits>material_gain | we explain, they don't | 10 | 0 | 147234657424 15.Qh5+; 164462806840 18...g4; 167359572290 9...O-O-O; 173667762936 11.Qc4 |
| misses>ObviousRetreat | - | they explain, we don't | 10 | 0 | 147991742972 19.Qxa7; 170185678278 9.Na4; 170185678278 9...Bd4; 171980080646 22...Qxa3 |
| permits>LosesMaterial | - | they explain, we don't | 9 | 0 | 1034847688 16.Bxg7; 145833758308 7...Ng6; 145833758308 35.Rg4; 171887823168 10...Qc7 |
| HangsPiece | permits>free_piece | different | 8 | 8 | 142849698970 18...Qg5+; 165327199736 19.Qc2; 166583201950 20...Ne4; 166583201950 22...Ne4+ |
| permits>LosesMaterial | permits>wins_material>fork | different | 8 | 0 | 145833758308 30.Nd5; 184110410320 15.Kb1; 185117573448 26.Rxe5; 185216623720 25...Qxf2 |
| permits>LosesMaterial | misses>free_piece | different | 8 | 2 | 166583201950 21.f3; 167359572290 14...Bd6; 173667762936 19.Nc3; 184028735740 29...Kb6 |
| misses>DevelopsCenter | - | they explain, we don't | 8 | 0 | 173904334944 5.c3; 173904334944 7.Na3; 173905398948 12.Nd5; 174188274588 8...O-O |
| EqualToWorse | - | they explain, we don't | 8 | 0 | 184873703892 34...Qh3; 185277691132 7...Nb4; 185456088510 11...Bg7; 185456088510 12...c5 |
| misses>CaptureThreat | misses>free_piece | different | 7 | 0 | 142849698970 15...Ne2+; 142875589252 17...Bb4+; 147547838342 12...Bg4; 166583201950 11.Nd3 |
| - | permits>forced_mate | we explain, they don't | 7 | 0 | 142873206408 38...h5; 142873206408 42...Kg4; 164784324724 46...Kd8; 184678264914 32.Rxc7 |
| - | misses>material_gain | we explain, they don't | 7 | 0 | 142918703388 5...a6; 147786569400 8.h4; 173855642488 16.Qe2; 184028735740 31.Qxd4+ |
| permits>wins_material>Fork | permits>free_piece | different | 7 | 0 | 142918703388 16.b4; 146658193946 10...d4; 146658193946 11...Nbd7; 165401252676 12...Bb6 |
| permits>LosesMaterial | permits>wins_material>discovered_attack | different | 7 | 1 | 146658193946 24...Ne4; 164008171476 13...Nbd7; 173570784620 29...Re8; 184809655978 14.Qh8+ |
| permits>LosesMaterial | permits>leads_to>removes_defender | different | 7 | 1 | 164188880582 18.Re1; 164784324724 33...Re1; 167479014786 27.b4; 171124015136 22...Nc6 |
| permits>LosesMaterial | permits>forced_mate | different | 7 | 0 | 164784324724 41...a5; 165557442658 29.Kf1; 166583201950 30.Kf4; 171124015136 38...Kh8 |
| misses>ObviousRecapture | - | they explain, we don't | 6 | 0 | 1034847688 16...Nxg7; 1034847688 23...Kxf7; 171841312410 7...dxe5; 173620121124 15.Bb4+ |
| permits>LosesMaterial | bad_trade | same family | 6 | 4 | 142849698970 9.Nxf7; 165450446440 16.Qxf7+; 172996177054 14.Nxe6; 173068943088 17...Rxf3 |
