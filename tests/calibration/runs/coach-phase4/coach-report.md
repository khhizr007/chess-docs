# Coach agreement with Chess.com (Phase 0)

Run `coach-phase4`, 142 games, 8638 plies, commit `118a076`. Reference: the main event of Chess.com's speech for the played move.

## Bad moves (Chess.com Inaccuracy, Mistake, Blunder, Miss)

| category | plies | share |
|---|---|---|
| exact | 643 | 32.3% |
| same tag, other circumstance | 55 | 2.8% |
| same family | 133 | 6.7% |
| different | 901 | 45.3% |
| they explain, we don't | 70 | 3.5% |
| we explain, they don't | 157 | 7.9% |
| neither | 29 | 1.5% |

Where both explain (1732 plies): exact 37.1%, same tag 40.3%, same family or better 48.0%.

### Plies both apps label bad (1641 of 1988)

Phase 1 explains only moves we label Inaccuracy, Mistake, Blunder or Miss, so this is the coach's own agreement, free of label disagreements.

| category | plies | share |
|---|---|---|
| exact | 643 | 39.2% |
| same tag, other circumstance | 21 | 1.3% |
| same family | 97 | 5.9% |
| different | 724 | 44.1% |
| they explain, we don't | 24 | 1.5% |
| we explain, they don't | 119 | 7.3% |
| neither | 13 | 0.8% |

Bad by Chess.com but not by us: 347 plies (our labels: {'good': 245, 'excellent': 65, 'best': 26, 'book': 11}).
Of the 1104 bad-move plies where we do not say Chess.com's tag, we detected it (in any circumstance) on 361.

### By Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| inaccuracy | 825 | 178 (21.6%) | 34 (4.1%) | 67 (8.1%) | 366 (44.4%) | 48 (5.8%) | 106 (12.8%) | 26 (3.2%) |
| mistake | 616 | 211 (34.3%) | 5 (0.8%) | 41 (6.7%) | 299 (48.5%) | 19 (3.1%) | 38 (6.2%) | 3 (0.5%) |
| blunder | 228 | 138 (60.5%) | 3 (1.3%) | 7 (3.1%) | 77 (33.8%) | 0 (0.0%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 116 (36.4%) | 13 (4.1%) | 18 (5.6%) | 159 (49.8%) | 3 (0.9%) | 10 (3.1%) | 0 (0.0%) |

### By phase

| phase | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| opening | 602 | 207 (34.4%) | 15 (2.5%) | 51 (8.5%) | 250 (41.5%) | 21 (3.5%) | 53 (8.8%) | 5 (0.8%) |
| middlegame | 921 | 296 (32.1%) | 20 (2.2%) | 54 (5.9%) | 448 (48.6%) | 31 (3.4%) | 61 (6.6%) | 11 (1.2%) |
| endgame | 465 | 140 (30.1%) | 20 (4.3%) | 28 (6.0%) | 203 (43.7%) | 18 (3.9%) | 43 (9.2%) | 13 (2.8%) |

## All plies by Chess.com classification

| class | plies | exact | same tag, other circumstance | same family | different | they explain, we don't | we explain, they don't | neither |
|---|---|---|---|---|---|---|---|---|
| brilliant | 25 | 9 (36.0%) | 0 (0.0%) | 2 (8.0%) | 11 (44.0%) | 2 (8.0%) | 1 (4.0%) | 0 (0.0%) |
| great | 321 | 178 (55.5%) | 4 (1.2%) | 14 (4.4%) | 119 (37.1%) | 4 (1.2%) | 2 (0.6%) | 0 (0.0%) |
| best | 2621 | 1587 (60.5%) | 21 (0.8%) | 148 (5.6%) | 526 (20.1%) | 51 (1.9%) | 177 (6.8%) | 111 (4.2%) |
| excellent | 1473 | 834 (56.6%) | 8 (0.5%) | 76 (5.2%) | 232 (15.8%) | 61 (4.1%) | 126 (8.6%) | 136 (9.2%) |
| good | 1116 | 522 (46.8%) | 21 (1.9%) | 59 (5.3%) | 228 (20.4%) | 53 (4.7%) | 115 (10.3%) | 118 (10.6%) |
| book | 980 | 221 (22.6%) | 0 (0.0%) | 12 (1.2%) | 31 (3.2%) | 29 (3.0%) | 608 (62.0%) | 79 (8.1%) |
| forced | 114 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 114 (100.0%) | 0 (0.0%) | 0 (0.0%) |
| inaccuracy | 825 | 178 (21.6%) | 34 (4.1%) | 67 (8.1%) | 366 (44.4%) | 48 (5.8%) | 106 (12.8%) | 26 (3.2%) |
| mistake | 616 | 211 (34.3%) | 5 (0.8%) | 41 (6.7%) | 299 (48.5%) | 19 (3.1%) | 38 (6.2%) | 3 (0.5%) |
| blunder | 228 | 138 (60.5%) | 3 (1.3%) | 7 (3.1%) | 77 (33.8%) | 0 (0.0%) | 3 (1.3%) | 0 (0.0%) |
| miss | 319 | 116 (36.4%) | 13 (4.1%) | 18 (5.6%) | 159 (49.8%) | 3 (0.9%) | 10 (3.1%) | 0 (0.0%) |

## Good moves (Chess.com brilliant, great, great_find, best, excellent, good; 5349 plies both apps label good)

| category | plies | share |
|---|---|---|
| exact | 3116 | 58.3% |
| same tag, other circumstance | 38 | 0.7% |
| same family | 283 | 5.3% |
| different | 1012 | 18.9% |
| they explain, we don't | 157 | 2.9% |
| we explain, they don't | 383 | 7.2% |
| neither | 360 | 6.7% |

### Chess.com's main event on good moves, by family

| family | plies | share |
|---|---|---|
| defence | 1293 | 24.2% |
| positional | 1170 | 21.9% |
| trade | 956 | 17.9% |
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
| - | free_piece | we explain, they don't | 52 | 142636591844 9.Nxh7; 142849919300 13...Qxd3+; 142849919300 16...Qxh1 |
| - | equal_trade | we explain, they don't | 46 | 142866059618 22.Rxd8+; 142873206408 23.Bxe6+; 145833178628 8.Bxd7+ |
| EqualTrade | recapture | same family | 38 | 142866059618 21.bxc3; 142873206408 36.dxe4; 146658193946 9...cxd5 |
| StillMate | forced_mate | same family | 32 | 142866059618 51...Kc4; 145833178628 32...Qd3+; 147547838342 19...Re8 |
| PileTrade | free_piece | different | 25 | 142866059618 14.Bxd4; 147547838342 16...Rxe3+; 165327199736 14.axb5 |
| - | king_activity | we explain, they don't | 25 | 142866059618 52.Kc2; 142873206408 39...Ke6; 169217872990 28.Kg3 |
| FreePiece | recapture | different | 22 | 142875589252 19.Kxe2; 147234657424 7...Kxf7; 147786569400 11.Qxf3 |
| - | material_gain | we explain, they don't | 20 | 142866059618 9.g5; 164784324724 27.Ng5+; 164784324724 33.b4 |
| ObviousRecapture | equal_trade | same family | 18 | 142636591844 15.gxf5; 142875589252 8...bxc6; 171980080646 19...exd4 |
| EqualTrade | free_piece | different | 18 | 142849919300 9...Qxd5; 142866059618 34...Bxf4; 147295227566 8...Bxc5 |
| PseudoFork | wins_material>fork | same tag, other circumstance | 17 | 142849919300 14...Qc2+; 142866059618 26...Rd3+; 145833758308 18...Qf4+ |
| - | gains_tempo | we explain, they don't | 17 | 142873206408 21...Bxb4; 164007452224 16...Nf6; 164784324724 38.Nxg3 |
| - | takes_open_file | we explain, they don't | 17 | 142875589252 14...Re8+; 147295227566 35...Rg1+; 147547838342 11...Re8+ |
| DevelopsOpening | pin | different | 15 | 142849698970 5...Bg4; 147234657424 11.Bg5; 164462806840 4...Bg4 |
| - | pin | we explain, they don't | 15 | 147619991314 8.Re1; 164188880582 16.Bg5; 166096155098 9...Qg6 |
| - | moves_to_active_square | we explain, they don't | 15 | 166583201950 27...Qe1+; 172996177054 22.Qe6+; 184028735740 34...Qa1 |
| CreatesPawnChain | - | they explain, we don't | 14 | 142873206408 29.c4; 147295227566 32...g6; 165557442658 6.c3 |
| StrikesAtCenter | kicks | different | 14 | 147234657424 5...d5; 147547838342 9...d5; 164784324724 14...d5 |
| EqualTrade | forces>forces_doubled_pawns | different | 13 | 1034847688 19...Nxf3; 142849698970 10...Bxc4; 142866059618 7.Bxg6 |
| RemovesAttacker | equal_trade | different | 12 | 142636591844 13.exf5; 145833178628 6.exd5; 147234657424 6.exd5 |
| wins_material>Fork | free_piece | different | 11 | 142849919300 11...Nxc2+; 142918703388 17...Qxb4; 146658193946 12.Nxf7 |
| - | forced_mate | we explain, they don't | 11 | 142849919300 23...Qe2+; 142849919300 24...Qxd3+; 164784324724 42.Rxb4 |
| PseudoFork | gains_tempo | different | 11 | 142873206408 9...Nd4; 142873206408 34.Ne6; 171708489350 10.Nd5 |
| PushesPassedPawnEndgame | forced_mate | different | 11 | 142873206408 39.g7; 142873206408 45.e5; 145833758308 55...h3 |
| MovesToActiveSquare | - | they explain, we don't | 11 | 164812402934 13...Re8; 173570784620 12...Qe6; 173570784620 14...Qe6 |

## The best-move sentence on plies both label bad (1545 with a sentence on either side)

Chess.com's speech for the best alternative against our Misses-block event, without the "misses" step.

| category | plies | share |
|---|---|---|
| exact | 710 | 46.0% |
| same tag, other circumstance | 10 | 0.6% |
| same family | 124 | 8.0% |
| different | 467 | 30.2% |
| they explain, we don't | 56 | 3.6% |
| we explain, they don't | 178 | 11.5% |
| neither | 0 | 0.0% |

### Patterns (Chess.com → ours)

| Chess.com | ours | category | plies | examples |
|---|---|---|---|---|
| - | free_piece | we explain, they don't | 19 | 142918703388 24.Rxc5; 147295227566 9.Re1+; 166583201950 33.Qxe3 |
| - | only_move | we explain, they don't | 17 | 145833758308 51.h3; 147991742972 22.Kg1; 167397747616 36.f6 |
| - | equal_trade | we explain, they don't | 11 | 142875589252 3...Nf6; 147786569400 8...O-O; 148224127998 14...Be4 |
| - | sacrifice | we explain, they don't | 11 | 164812402934 15...c6; 165450446440 16.Qxf7+; 174336461820 17.f3 |
| - | moves_to_active_square | we explain, they don't | 10 | 142849698970 13...O-O-O; 165557442658 26.Qxf7; 167397747616 30...Qf7 |
| StrikesAtCenter | kicks | different | 9 | 1011026868 8...a6; 1011026868 9...b5; 145833178628 4.Bc4 |
| DefendsPiece | gains_tempo | same family | 9 | 147991742972 15.Qe4; 165974850998 21...Bc7; 165974850998 22...Bd6 |
| PileTrade | free_piece | different | 8 | 148014224206 13...Nf6; 164462806840 14...b6; 166853117390 14.Qxg5+ |
| EqualTrade | free_piece | different | 7 | 1034847688 12.Ng5; 148014224206 18...Nde5; 165557442658 24...d4 |
| StillMate | forced_mate | same family | 7 | 142866059618 45...Be7; 147547838342 20...Qe4+; 169217872990 26...Re1 |
| - | gains_tempo | we explain, they don't | 7 | 168426135116 30...e5; 171932623366 17.Bc4; 173807034866 22.dxe4 |
| - | material_gain | we explain, they don't | 6 | 142918703388 5...a6; 148224127998 16.Bxd5; 173855642488 16.Qe2 |
| forces>IsolatesPawn | equal_trade | different | 6 | 148014224206 21.Qf6; 171841312410 17...Rad8; 184773009646 18...Bf6 |
| PseudoFork | wins_material>fork | same tag, other circumstance | 6 | 167359572290 14.dxe5; 169217872990 19.Ne4; 173620121124 25...b4 |
| Kicks | counter_threat | same family | 6 | 172349629492 9...Qc8; 173068943088 8.Bd2; 173570784620 17.fxe5 |
| AddsAttacker | material_gain | different | 5 | 142636591844 5.d3; 142918703388 5.d3; 168148201932 21...Bd2 |
| AddsAttacker | free_piece | different | 5 | 142636591844 16...Bxe6; 142875589252 17...Bb4+; 147547838342 12...Bg4 |
| DefendsPiece | free_piece | different | 5 | 142849698970 15...Ne2+; 142849919300 12...Nxa1; 185099205950 21...Rad8 |
| - | prevents>forced_mate | we explain, they don't | 5 | 147547838342 20.Kh1; 173667762936 13.dxe4; 184028735740 31.Qxd4+ |
| - | escapes_threat | we explain, they don't | 5 | 173620121124 11...Qe7+; 184449650784 19...exf3; 184773009646 6...Bb6 |
| OffersTrade | gains_tempo | different | 5 | 184678264914 28.Ra1; 184678264914 29.Ra7; 184873703892 37.Ka2 |
| BlunderPunish | - | they explain, we don't | 4 | 1011026868 9.a3; 184829980734 25.Qf4; 185110487484 50.Rh8 |
| - | develops_middlegame | we explain, they don't | 4 | 1034847688 11...a5; 173905398948 26...Rxc2; 185221110711 14.Be2 |
| wins_material>Fork | free_piece | different | 4 | 142849919300 10...h6; 142918703388 16...dxe4; 169217872990 17...Qxf2+ |
| ObviousRecapture | equal_trade | same family | 4 | 142866059618 13.Ke2; 167359572290 18...Ke7; 185137444946 24...Nd4 |

## Chess.com's main event on bad moves, by family

| family | plies | share |
|---|---|---|
| bad-move base | 374 | 18.8% |
| defence | 351 | 17.7% |
| positional | 334 | 16.8% |
| free material | 219 | 11.0% |
| (none) | 186 | 9.4% |
| double attack | 135 | 6.8% |
| mate | 117 | 5.9% |
| trade | 64 | 3.2% |
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
| permits>LosesMaterial | 235 | 70 |
| misses>CaptureThreat | 206 | 42 |
| - | 186 | 0 |
| permits>FreePiece | 97 | 69 |
| misses>FreePiece | 89 | 52 |
| permits>wins_material>Fork | 50 | 25 |
| permits>ForcesMate | 49 | 44 |
| HangsPiece | 48 | 42 |
| misses>Critical | 42 | 4 |
| RemovesOwnDefender | 38 | 34 |
| misses>EvadesCheck | 23 | 3 |
| misses>DevelopsCenter | 23 | 8 |
| misses>DefendsPiece | 22 | 4 |
| permits>PileTrade | 22 | 0 |
| misses>wins_material>Fork | 21 | 10 |
| misses>DirectSacrificeCapture | 21 | 13 |
| misses>ObviousRetreat | 21 | 13 |
| permits>leads_to>Fork | 20 | 4 |
| misses>EscapesThreat | 20 | 4 |
| misses>ObviousRecapture | 19 | 7 |
| MovesSamePieceInOpening | 19 | 3 |
| misses>CastlesKingSide | 18 | 5 |
| EqualToWorse | 18 | 3 |
| permits>Checkmate | 17 | 15 |
| MovesPawnInFrontOfKing | 15 | 1 |

## Disagreement patterns on plies both apps label bad (Chess.com → ours)

| Chess.com | ours | category | plies | we detected theirs | examples |
|---|---|---|---|---|---|
| misses>CaptureThreat | permits>material_gain | different | 13 | 4 | 1034847688 15.Rad1; 142918703388 5.d3; 165557442658 26.Qxf7; 168148201932 21.c4 |
| permits>LosesMaterial | ignores_threat | same family | 13 | 4 | 142875589252 15.Ne2; 145833758308 30.Nd5; 166853117390 12...c6; 172026321412 9...a6 |
| - | permits>material_gain | we explain, they don't | 13 | 0 | 147234657424 15.Qh5+; 164462806840 18...g4; 167359572290 9...O-O-O; 173667762936 11.Qc4 |
| permits>LosesMaterial | permits>free_piece | different | 12 | 1 | 142849919300 9.Na4; 142918703388 20...Bc5; 145833178628 21.Kc2; 148014224206 17...Kd8 |
| - | misses>free_piece | we explain, they don't | 10 | 0 | 147295227566 9.Re1+; 147295227566 18...Bg5; 166853117390 16.Qh5+; 170185678278 6...Bc5 |
| misses>CaptureThreat | misses>escapes_threat | same family | 8 | 4 | 145833178628 11.dxe4; 148224127998 24.Ra4; 173620121124 11.Qb4; 173855642488 4.Nc3 |
| permits>LosesMaterial | permits>wins_material>discovered_attack | different | 8 | 1 | 146658193946 24...Ne4; 164008171476 13...Nbd7; 168426135116 15.Bxf6; 173570784620 29...Re8 |
| misses>CaptureThreat | misses>free_piece | different | 7 | 2 | 142849698970 15...Ne2+; 142875589252 17...Bb4+; 147547838342 12...Bg4; 166583201950 11.Nd3 |
| - | permits>forced_mate | we explain, they don't | 7 | 0 | 142873206408 38...h5; 142873206408 42...Kg4; 164784324724 46...Kd8; 184678264914 32.Rxc7 |
| - | misses>equal_trade | we explain, they don't | 7 | 0 | 148224127998 14...Be4; 172026321412 12...Be7; 185117573448 22...Rf5; 185137444946 12...Ra7 |
| permits>LosesMaterial | permits>forced_mate | different | 7 | 0 | 164784324724 41...a5; 165557442658 29.Kf1; 166583201950 30.Kf4; 171124015136 38...Kh8 |
| permits>LosesMaterial | permits>wins_material>removes_defender | different | 7 | 0 | 165974850998 21...Bc7; 165974850998 22...Bd6; 171841312410 16.O-O; 184678264914 20.Rb1 |
| permits>LosesMaterial | misses>free_piece | different | 7 | 4 | 166583201950 21.f3; 167359572290 14...Bd6; 173667762936 19.Nc3; 184028735740 30.Rc2 |
| misses>EvadesCheck | permits>forced_mate | different | 6 | 6 | 142849919300 24.Nd3; 145833758308 39.Kf2; 145833758308 41.Kf2; 173620121124 37...Kb8 |
| misses>CaptureThreat | permits>removes_defender | different | 6 | 3 | 142873206408 7.b4; 167316688806 8...Ng4; 167397747616 30...Qf7; 185221110711 28.Bxa5 |
| permits>wins_material>Fork | permits>material_gain | different | 6 | 0 | 146658193946 11...Nbd7; 165401252676 12...Bb6; 169217872990 17.Nc3; 173855642488 14...h6 |
| misses>CaptureThreat | misses>counter_threat | same family | 6 | 3 | 147295227566 37.Rc3; 172349629492 9...Qc8; 184449650784 7...b6; 184773009646 7.Nc3 |
| IgnoresAttackedPiece | permits>free_piece | different | 6 | 6 | 166583201950 6...Bg4; 167479014786 23.Qe7; 168426135116 18...Qc6; 173905398948 13.Bf4 |
| permits>PileTrade | hangs_pawn | different | 6 | 0 | 166853117390 13...d5; 174336461820 10...d4; 184028735740 16.d4; 184449650784 15...e5 |
| permits>LosesMaterial | permits>loses_trade | different | 6 | 3 | 171887823168 24...Nxf3+; 172996177054 17.Rxd6; 173618554654 11...Nxd4; 173807034866 22.dxe4 |
| permits>LosesMaterial | permits>wins_material>fork | different | 6 | 0 | 184110410320 15.Kb1; 185117573448 26.Rxe5; 185216623720 25...Qxf2; 185363017994 48.Qa2 |
| misses>CaptureThreat | misses>material_gain | different | 5 | 0 | 142636591844 5.d3; 185193771738 14.b3; 185193771738 15.b4; 185438707002 14...Nd4 |
| KeymomentBadFasterMate | misses>forced_mate | same tag, other circumstance | 5 | 5 | 142866059618 45...Be7; 142873206408 43.Nxb7; 145833758308 39...Qe2+; 145833758308 60...Qf6+ |
| misses>CaptureThreat | misses>develops_center | different | 5 | 0 | 142873206408 6.a3; 145833178628 3...Bc5; 184829980734 3...g6; 185328167888 6...e4 |
| - | misses>material_gain | we explain, they don't | 5 | 0 | 142918703388 5...a6; 147786569400 8.h4; 173855642488 16.Qe2; 185193771738 18.Rd3 |
