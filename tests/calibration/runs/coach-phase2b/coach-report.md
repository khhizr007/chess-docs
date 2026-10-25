# Coach agreement with Chess.com (Phase 0)

Run `coach-phase2b`, 142 games, 8638 plies, commit `14186c4`. Reference: the main event of Chess.com's speech for the played move.

## Bad moves (Chess.com Inaccuracy, Mistake, Blunder, Miss)

| category | plies | share |
|---|---|---|
| exact | 581 | 29.2% |
| same tag, other circumstance | 55 | 2.8% |
| same family | 70 | 3.5% |
| different | 870 | 43.8% |
| they explain, we don't | 226 | 11.4% |
| we explain, they don't | 126 | 6.3% |
| neither | 60 | 3.0% |

Where both explain (1576 plies): exact 36.9%, same tag 40.4%, same family or better 44.8%.

### Plies both apps label bad (1641 of 1988)

Phase 1 explains only moves we label Inaccuracy, Mistake, Blunder or Miss, so this is the coach's own agreement, free of label disagreements.

| category | plies | share |
|---|---|---|
| exact | 581 | 35.4% |
| same tag, other circumstance | 21 | 1.3% |
| same family | 54 | 3.3% |
| different | 737 | 44.9% |
| they explain, we don't | 116 | 7.1% |
| we explain, they don't | 106 | 6.5% |
| neither | 26 | 1.6% |

Bad by Chess.com but not by us: 347 plies (our labels: {'good': 245, 'excellent': 65, 'best': 26, 'book': 11}).
Of the 1166 bad-move plies where we do not say Chess.com's tag, we detected it (in any circumstance) on 244.

### By Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| inaccuracy | 825 | 145 (17.6%) | 34 (4.1%) | 31 (3.8%) | 328 (39.8%) | 155 (18.8%) | 79 (9.6%) | 53 (6.4%) |
| mistake | 616 | 189 (30.7%) | 5 (0.8%) | 22 (3.6%) | 299 (48.5%) | 60 (9.7%) | 34 (5.5%) | 7 (1.1%) |
| blunder | 228 | 133 (58.3%) | 3 (1.3%) | 5 (2.2%) | 81 (35.5%) | 3 (1.3%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 114 (35.7%) | 13 (4.1%) | 12 (3.8%) | 162 (50.8%) | 8 (2.5%) | 10 (3.1%) | 0 (0.0%) |

### By phase

| phase | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| opening | 602 | 162 (26.9%) | 14 (2.3%) | 16 (2.7%) | 237 (39.4%) | 115 (19.1%) | 37 (6.1%) | 21 (3.5%) |
| middlegame | 921 | 282 (30.6%) | 21 (2.3%) | 37 (4.0%) | 435 (47.2%) | 74 (8.0%) | 55 (6.0%) | 17 (1.8%) |
| endgame | 465 | 137 (29.5%) | 20 (4.3%) | 17 (3.7%) | 198 (42.6%) | 37 (8.0%) | 34 (7.3%) | 22 (4.7%) |

## All plies by Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| brilliant | 25 | 9 (36.0%) | 0 (0.0%) | 2 (8.0%) | 11 (44.0%) | 2 (8.0%) | 1 (4.0%) | 0 (0.0%) |
| great | 321 | 175 (54.5%) | 4 (1.2%) | 13 (4.0%) | 123 (38.3%) | 4 (1.2%) | 2 (0.6%) | 0 (0.0%) |
| best | 2621 | 1324 (50.5%) | 22 (0.8%) | 122 (4.7%) | 566 (21.6%) | 299 (11.4%) | 150 (5.7%) | 138 (5.3%) |
| excellent | 1473 | 546 (37.1%) | 8 (0.5%) | 41 (2.8%) | 233 (15.8%) | 383 (26.0%) | 93 (6.3%) | 169 (11.5%) |
| good | 1116 | 315 (28.2%) | 17 (1.5%) | 23 (2.1%) | 237 (21.2%) | 291 (26.1%) | 83 (7.4%) | 150 (13.4%) |
| book | 980 | 39 (4.0%) | 0 (0.0%) | 4 (0.4%) | 12 (1.2%) | 238 (24.3%) | 5 (0.5%) | 682 (69.6%) |
| forced | 114 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 114 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| inaccuracy | 825 | 145 (17.6%) | 34 (4.1%) | 31 (3.8%) | 328 (39.8%) | 155 (18.8%) | 79 (9.6%) | 53 (6.4%) |
| mistake | 616 | 189 (30.7%) | 5 (0.8%) | 22 (3.6%) | 299 (48.5%) | 60 (9.7%) | 34 (5.5%) | 7 (1.1%) |
| blunder | 228 | 133 (58.3%) | 3 (1.3%) | 5 (2.2%) | 81 (35.5%) | 3 (1.3%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 114 (35.7%) | 13 (4.1%) | 12 (3.8%) | 162 (50.8%) | 8 (2.5%) | 10 (3.1%) | 0 (0.0%) |

## Good moves (Chess.com brilliant, great, great_find, best, excellent, good; 5349 plies both apps label good)

| category | plies | share |
|---|---|---|
| exact | 2368 | 44.3% |
| same tag, other circumstance | 39 | 0.7% |
| same family | 195 | 3.6% |
| different | 1073 | 20.1% |
| they explain, we don't | 931 | 17.4% |
| we explain, they don't | 294 | 5.5% |
| neither | 449 | 8.4% |

### Chess.com's main event on good moves, by family

| family | plies | share |
|---|---|---|
| defence | 1310 | 24.5% |
| positional | 1168 | 21.8% |
| trade | 941 | 17.6% |
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
| DevelopsCenter | - | they explain, we don't | 116 | 1011026868 7.Be3; 1034847688 2...Nf6; 1034847688 7...Nc6 |
| PreparesToCastleKingside | - | they explain, we don't | 70 | 1011026868 5.Bc4; 1011026868 7...Nge7; 142636591844 4.Bc4 |
| CastlesKingSide | - | they explain, we don't | 58 | 1011026868 11...O-O; 1034847688 5...O-O; 1041474766 7.O-O |
| PreparesBishopDevelopment | - | they explain, we don't | 56 | 1011026868 4...g6; 1011026868 6.d3; 1034847688 3...g6 |
| - | free_piece | we explain, they don't | 52 | 142636591844 9.Nxh7; 142849919300 13...Qxd3+; 142849919300 16...Qxh1 |
| CastlesSameSide | - | they explain, we don't | 48 | 1011026868 12.O-O; 1041474766 10...O-O; 147295227566 11...O-O |
| - | equal_trade | we explain, they don't | 48 | 142636591844 13...Bxc3+; 142866059618 22.Rxd8+; 142873206408 23.Bxe6+ |
| EqualTrade | recapture | same family | 39 | 142866059618 21.bxc3; 142873206408 36.dxe4; 146658193946 9...cxd5 |
| MovesToActiveSquare | - | they explain, we don't | 35 | 164188880582 15...Rfe8; 164462806840 12...Nb6; 164812402934 13...Re8 |
| PushesPassedPawnEndgame | - | they explain, we don't | 32 | 142866059618 36...f4; 142866059618 37...f3; 142866059618 43.e6 |
| StillMate | forced_mate | same family | 32 | 142866059618 51...Kc4; 145833178628 32...Qd3+; 147547838342 19...Re8 |
| PutsPawnInCenter | - | they explain, we don't | 31 | 1034847688 3.d4; 1041474766 7...e5; 147619991314 7.d4 |
| StrikesAtCenter | - | they explain, we don't | 29 | 1041474766 8.d4; 142873206408 6...e5; 142918703388 15...d5 |
| ConnectsRooks | - | they explain, we don't | 28 | 1011026868 13.Qd2; 1011026868 13...Qd7; 142866059618 18...Ne7 |
| PileTrade | free_piece | different | 25 | 142866059618 14.Bxd4; 147547838342 16...Rxe3+; 165327199736 14.axb5 |
| TakesOpenFile | - | they explain, we don't | 23 | 142873206408 26.Re1; 142917385540 12.Rad1; 164007452224 14.Rfe1 |
| - | material_gain | we explain, they don't | 22 | 142866059618 9.g5; 164784324724 27.Ng5+; 164784324724 33.b4 |
| FreePiece | recapture | different | 22 | 142875589252 19.Kxe2; 147234657424 7...Kxf7; 147786569400 11.Qxf3 |
| DevelopsMiddlegame | - | they explain, we don't | 21 | 1011026868 12...Rc8; 142866059618 19.Rd1; 145833758308 17.Rd1 |
| DevelopsOpening | - | they explain, we don't | 20 | 1011026868 10...Bb7; 1041474766 10.Bd2; 147991742972 13.Qe2 |
| forces>DoublesPawns | equal_trade | different | 20 | 147547838342 10.Nxb6; 164812402934 9.Bxf4; 165557442658 8.Bxc6+ |
| ObviousRecapture | equal_trade | same family | 18 | 142636591844 15.gxf5; 142875589252 8...bxc6; 171980080646 19...exd4 |
| EqualTrade | free_piece | different | 18 | 142849919300 9...Qxd5; 142866059618 34...Bxf4; 147295227566 8...Bxc5 |
| PreparesToCastleQueenside | - | they explain, we don't | 17 | 1034847688 9.Qc2; 142873206408 11...Bg4+; 142917385540 11...Nd7 |
| PseudoFork | wins_material>fork | same tag, other circumstance | 17 | 142849919300 14...Qc2+; 142866059618 26...Rd3+; 145833758308 18...Qf4+ |

## The best-move sentence on plies both label bad (1507 with a sentence on either side)

Chess.com's speech for the best alternative against our Misses-block event, without the "misses" step.

| category | plies | share |
|---|---|---|
| exact | 566 | 37.6% |
| same tag, other circumstance | 10 | 0.7% |
| same family | 69 | 4.6% |
| different | 495 | 32.8% |
| they explain, we don't | 227 | 15.1% |
| we explain, they don't | 140 | 9.3% |
| neither | 0 | 0.0% |

### Patterns (Chess.com → ours)

| Chess.com | ours | category | plies | examples |
|---|---|---|---|---|
| DevelopsCenter | - | they explain, we don't | 22 | 142873206408 6.a3; 142873206408 7.b4; 145833758308 7.Bd2 |
| - | only_move | we explain, they don't | 20 | 145833758308 51.h3; 147991742972 22.Kg1; 165557442658 26.Qxf7 |
| - | free_piece | we explain, they don't | 19 | 142918703388 24.Rxc5; 147295227566 9.Re1+; 166583201950 33.Qxe3 |
| StrikesAtCenter | - | they explain, we don't | 14 | 1011026868 8.Rb1; 1011026868 16...h6; 1034847688 6...c5 |
| PreparesBishopDevelopment | - | they explain, we don't | 11 | 142849919300 6...d5; 142917385540 12...O-O-O; 167359572290 7...Bxd3 |
| - | equal_trade | we explain, they don't | 11 | 142875589252 3...Nf6; 147786569400 8...O-O; 148224127998 14...Be4 |
| MovesToActiveSquare | - | they explain, we don't | 11 | 164784324724 32...Rfe8; 167397747616 21...Rae8; 171887823168 14.Bxh6 |
| - | sacrifice | we explain, they don't | 11 | 164812402934 15...c6; 165450446440 16.Qxf7+; 174336461820 17.f3 |
| DevelopsMiddlegame | - | they explain, we don't | 11 | 166853117390 13...d5; 184271279368 14.Qf5+; 184732665836 28...Nc2 |
| AttacksPawnChain | only_move | different | 10 | 1034847688 15.Rad1; 1034847688 17.cxb5; 184828162542 10...cxd4 |
| StrikesAtCenter | kicks | different | 9 | 1011026868 8...a6; 1011026868 9...b5; 145833178628 4.Bc4 |
| PreparesToCastleKingside | - | they explain, we don't | 9 | 1034847688 5.c4; 142636591844 4...Ne7; 142875589252 11...d5 |
| DefendsPiece | gains_tempo | same family | 9 | 147991742972 15.Qe4; 165974850998 21...Bc7; 165974850998 22...Bd6 |
| PileTrade | free_piece | different | 8 | 148014224206 13...Nf6; 164462806840 14...b6; 166853117390 14.Qxg5+ |
| BishopGainsScope | - | they explain, we don't | 8 | 148224127998 28.Rc7; 169217872990 15.Bg4; 174468507028 11.Nd2 |
| DefendsPiece | - | they explain, we don't | 8 | 166853117390 12...c6; 171124015136 29...gxh6; 173570784620 13.Ng5 |
| EqualTrade | free_piece | different | 7 | 1034847688 12.Ng5; 148014224206 18...Nde5; 165557442658 24...d4 |
| StillMate | forced_mate | same family | 7 | 142866059618 45...Be7; 147547838342 20...Qe4+; 169217872990 26...Re1 |
| - | material_gain | we explain, they don't | 7 | 142918703388 5...a6; 148224127998 16.Bxd5; 173855642488 16.Qe2 |
| CreatesLuft | - | they explain, we don't | 7 | 148224127998 23...Na5; 164007452224 9.d4; 164784324724 9.Ne2 |
| - | gains_tempo | we explain, they don't | 7 | 168426135116 30...e5; 171932623366 17.Bc4; 173807034866 22.dxe4 |
| DevelopsOpening | - | they explain, we don't | 6 | 142849698970 8.Ng5; 173905398948 10.Ba6+; 173905398948 11.d6 |
| PutsPawnInCenter | - | they explain, we don't | 6 | 142917385540 4...h5; 172026321412 3.Bc4; 173618554654 3.Bc4 |
| Kicks | - | they explain, we don't | 6 | 145833758308 8.e5; 167479014786 22...Qg4; 184449650784 8...c5 |
| ConnectsRooks | - | they explain, we don't | 6 | 147234657424 16.Qxc5; 147786569400 19...Nf6; 165450446440 10.Ne4 |

## Chess.com's main event on bad moves, by family

| family | plies | share |
|---|---|---|
| bad-move base | 374 | 18.8% |
| defence | 355 | 17.9% |
| positional | 333 | 16.8% |
| free material | 219 | 11.0% |
| (none) | 186 | 9.4% |
| double attack | 135 | 6.8% |
| mate | 117 | 5.9% |
| line tactic | 64 | 3.2% |
| trade | 61 | 3.1% |
| game | 50 | 2.5% |
| evaluation | 36 | 1.8% |
| sacrifice | 33 | 1.7% |
| defender tactic | 22 | 1.1% |
| other | 2 | 0.1% |
| promotion | 1 | 0.1% |

## Chess.com's most frequent main events on bad moves

| Chess.com event | plies | ours exact |
|---|---|---|
| permits>LosesMaterial | 235 | 59 |
| misses>CaptureThreat | 206 | 42 |
| - | 186 | 0 |
| permits>FreePiece | 97 | 72 |
| misses>FreePiece | 89 | 52 |
| permits>wins_material>Fork | 50 | 25 |
| permits>ForcesMate | 49 | 44 |
| HangsPiece | 48 | 42 |
| misses>Critical | 42 | 9 |
| RemovesOwnDefender | 38 | 34 |
| misses>EvadesCheck | 23 | 3 |
| misses>DevelopsCenter | 23 | 0 |
| misses>DefendsPiece | 22 | 4 |
| permits>PileTrade | 22 | 0 |
| misses>wins_material>Fork | 21 | 10 |
| misses>DirectSacrificeCapture | 21 | 13 |
| misses>ObviousRetreat | 21 | 13 |
| permits>leads_to>Fork | 20 | 4 |
| misses>EscapesThreat | 20 | 4 |
| misses>ObviousRecapture | 19 | 7 |
| MovesSamePieceInOpening | 19 | 0 |
| misses>CastlesKingSide | 18 | 0 |
| EqualToWorse | 18 | 5 |
| permits>Checkmate | 17 | 15 |
| MovesPawnInFrontOfKing | 15 | 0 |

## Disagreement patterns on plies both apps label bad (Chess.com → ours)

| Chess.com | ours | category | plies | we detected theirs | examples |
|---|---|---|---|---|---|
| permits>LosesMaterial | permits>free_piece | different | 26 | 1 | 142849698970 9.Nxf7; 142849919300 9.Na4; 142849919300 11.h4; 142849919300 12.Kd1 |
| misses>CaptureThreat | - | they explain, we don't | 13 | 0 | 142873206408 6.a3; 145833178628 3...Bc5; 167479014786 22...Qg4; 173620121124 30...h5 |
| misses>CaptureThreat | permits>material_gain | different | 12 | 4 | 1034847688 15.Rad1; 142918703388 5.d3; 165557442658 26.Qxf7; 168148201932 21.c4 |
| - | permits>material_gain | we explain, they don't | 12 | 0 | 147234657424 15.Qh5+; 164462806840 18...g4; 167359572290 9...O-O-O; 173667762936 11.Qc4 |
| permits>LosesMaterial | ignores_threat | same family | 10 | 1 | 142875589252 15.Ne2; 145833758308 30.Nd5; 166853117390 12...c6; 172026321412 9...a6 |
| - | misses>free_piece | we explain, they don't | 10 | 0 | 147295227566 9.Re1+; 147295227566 18...Bg5; 166853117390 16.Qh5+; 170185678278 6...Bc5 |
| misses>CastlesKingSide | - | they explain, we don't | 8 | 0 | 1034847688 5.c4; 173618554654 8...dxc2; 173618554654 10...Bxf3; 184028735740 8.Qxh7 |
| misses>CaptureThreat | misses>escapes_threat | same family | 8 | 4 | 145833178628 11.dxe4; 148224127998 24.Ra4; 173620121124 11.Qb4; 173855642488 4.Nc3 |
| permits>LosesMaterial | permits>wins_material>discovered_attack | different | 8 | 1 | 146658193946 24...Ne4; 164008171476 13...Nbd7; 168426135116 15.Bxf6; 173570784620 29...Re8 |
| misses>DevelopsCenter | - | they explain, we don't | 8 | 0 | 173904334944 5.c3; 173904334944 7.Na3; 173905398948 12.Nd5; 174188274588 8...O-O |
| misses>CaptureThreat | misses>free_piece | different | 7 | 2 | 142849698970 15...Ne2+; 142875589252 17...Bb4+; 147547838342 12...Bg4; 166583201950 11.Nd3 |
| - | permits>forced_mate | we explain, they don't | 7 | 0 | 142873206408 38...h5; 142873206408 42...Kg4; 164784324724 46...Kd8; 184678264914 32.Rxc7 |
| - | misses>equal_trade | we explain, they don't | 7 | 0 | 148224127998 14...Be4; 172026321412 12...Be7; 185117573448 22...Rf5; 185137444946 12...Ra7 |
| permits>LosesMaterial | permits>forced_mate | different | 7 | 0 | 164784324724 41...a5; 165557442658 29.Kf1; 166583201950 30.Kf4; 171124015136 38...Kh8 |
| permits>LosesMaterial | permits>wins_material>removes_defender | different | 7 | 0 | 165974850998 21...Bc7; 165974850998 22...Bd6; 171841312410 16.O-O; 184678264914 20.Rb1 |
| IgnoresAttackedPiece | permits>free_piece | different | 7 | 7 | 166583201950 6...Bg4; 167479014786 23.Qe7; 168426135116 18...Qc6; 173905398948 13.Bf4 |
| permits>LosesMaterial | misses>free_piece | different | 7 | 3 | 166583201950 21.f3; 167359572290 14...Bd6; 173667762936 19.Nc3; 184028735740 30.Rc2 |
| MovesSamePieceInOpening | - | they explain, we don't | 6 | 0 | 142849698970 8.Ng5; 184794204922 5...Nd4; 185137444946 8...Ng4; 185330935602 9.Qa4 |
| misses>EvadesCheck | permits>forced_mate | different | 6 | 6 | 142849919300 24.Nd3; 145833758308 39.Kf2; 145833758308 41.Kf2; 173620121124 37...Kb8 |
| misses>CaptureThreat | permits>removes_defender | different | 6 | 3 | 142873206408 7.b4; 167316688806 8...Ng4; 167397747616 30...Qf7; 185221110711 28.Bxa5 |
| misses>PutsPawnInCenter | - | they explain, we don't | 6 | 0 | 142917385540 4...h5; 172026321412 3.Bc4; 173618554654 3.Bc4; 184810276410 3.Bc4 |
| permits>wins_material>Fork | permits>free_piece | different | 6 | 0 | 146658193946 11...Nbd7; 165401252676 12...Bb6; 169217872990 17.Nc3; 173855642488 14...h6 |
| misses>CaptureThreat | misses>counter_threat | same family | 6 | 3 | 147295227566 37.Rc3; 172349629492 9...Qc8; 184449650784 7...b6; 184773009646 7.Nc3 |
| permits>PileTrade | hangs_pawn | different | 6 | 0 | 166853117390 13...d5; 174336461820 10...d4; 184028735740 16.d4; 184449650784 15...e5 |
| permits>LosesMaterial | permits>loses_trade | different | 6 | 2 | 171887823168 24...Nxf3+; 172996177054 17.Rxd6; 173618554654 11...Nxd4; 173807034866 22.dxe4 |
