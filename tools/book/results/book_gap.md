Our book: 3865 named lines, 7982 positions. Games: 577 (0 skipped), plies 42319.

## 1. Agreement

| Rule | Book both | We say Book, CC not | CC says Book, we not | P | R |
|---|---|---|---|---|---|
| position after the move is in our book (shipped rule) | 2885 | 154 | 736 | 0.949 | 0.797 |
| unbroken from move 1 | 2771 | 133 | 850 | 0.954 | 0.765 |

Chess.com Book plies: 3621 (6.28 per game). Ours: 3039 (5.27).

## 2. Per game: how long each book lasts

| Last Book ply, Chess.com minus ours | Games |
|---|---|
| same | 242 (42%) |
| CC longer by 1-2 | 139 (24%) |
| CC longer by 3-4 | 67 (12%) |
| CC longer by 5+ | 37 (6%) |
| ours longer | 92 (16%) |

Mean +0.99 plies, median +0, max +18.

## 3. By rating band

| Max Elo | Games | CC Book / game | Ours / game | Recall | Precision |
|---|---|---|---|---|---|
| <1000 | 255 | 5.0 | 4.6 | 0.85 | 0.92 |
| 1000-1599 | 171 | 5.9 | 5.2 | 0.84 | 0.95 |
| 1600-2199 | 75 | 7.4 | 5.9 | 0.78 | 0.98 |
| 2200+ | 76 | 10.4 | 7.0 | 0.66 | 0.98 |

## 4. Chess.com says Book, we do not (false negatives)

| Kind | Plies |
|---|---|
| a. sibling: position before is in our book, this move is not | 276 (38%) |
| b. deeper: position before is already out of our book | 460 (62%) |

Ply of the missed Book move (30 = 30+):

| Ply | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Missed | 11 | 34 | 52 | 81 | 99 | 83 | 76 | 59 | 48 | 35 | 32 | 27 | 20 | 17 | 14 | 10 | 9 | 8 | 7 | 5 | 3 | 1 | 2 | 2 | 1 |

Plies after our last Book ply (8 = 8+): 1: 276, 2: 168, 3: 107, 4: 69, 5: 31, 6: 23, 7: 19, 8: 43

Most common first missed Book move (the whole line up to it):

| Games | Line (last move is CC Book, not ours) |
|---|---|
| 7 | e4 e6 Nf3 d5 exd5 |
| 5 | e4 d5 e5 |
| 5 | e4 b6 Nf3 |
| 4 | e4 e5 Nf3 Nc6 Nc3 Bc5 |
| 4 | e4 c5 Nf3 d6 Bc4 |
| 4 | e4 d5 exd5 Qxd5 Nc3 Qe5+ |
| 3 | e4 e5 Bc4 Nf6 d3 Bc5 |
| 3 | d4 c6 Nf3 d5 Bf4 |
| 3 | g3 e5 Bg2 |
| 3 | d4 d5 Bf4 e6 |
| 3 | d4 d5 Bf4 Nf6 |
| 2 | c3 e5 |
| 2 | e4 c5 Nf3 Nc6 Bc4 |
| 2 | d4 c6 Bf4 d5 e3 |
| 2 | e4 c6 Nf3 d5 exd5 cxd5 d4 Nf6 |
| 2 | d4 c6 Bf4 d5 Nf3 |
| 2 | e4 c5 Bc4 d6 Nf3 Nf6 |
| 2 | e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Bd3 |
| 2 | e4 e5 Nf3 Nc6 Bc4 Nf6 Ng5 Bc5 Nxf7 Bxf2+ Kf1 |
| 2 | d4 e6 Bf4 |
| 2 | e4 e5 Nf3 d6 Nc3 |
| 2 | e4 e6 d4 d5 Nc3 dxe4 Nxe4 Nf6 |
| 2 | e3 d5 |
| 2 | e4 c5 Bc4 Nc6 |
| 2 | e3 c5 |

## 5. We say Book, Chess.com does not (false positives)

Chess.com's label on those moves: best 44, good 36, inaccuracy 32, excellent 18, mistake 14, great 6, blunder 2, miss 2

- CC's book stops here, ours goes on: 91
- after CC already left book (transposition back in): 63

| Games | Line (last move is our Book, not CC) |
|---|---|
| 8 | e4 e5 Qh5 |
| 4 | e4 e5 Nf3 Qf6 |
| 4 | e4 e5 Nf3 Nc6 Bc4 h6 |
| 4 | e4 e5 Nf3 Bc5 |
| 4 | e4 e5 c4 |
| 3 | e4 d5 exd5 c6 |
| 3 | e4 d5 Nf3 |
| 2 | e4 e5 Nf3 d5 |
| 2 | e4 c6 Bc4 |
| 2 | e4 Nf6 Nf3 |
| 2 | h3 |
| 2 | e4 e5 Qf3 |
| 2 | e4 e5 Bc4 Nf6 Nf3 |
| 2 | e4 e5 Nf3 Nf6 Bc4 |
| 1 | e4 e5 Nc3 Nf6 a3 |
| 1 | e4 e5 Nf3 c6 |
| 1 | e4 d5 d3 dxe4 Nc3 |
| 1 | c3 e5 e4 |
| 1 | e4 e5 Nf3 Nc6 Nc3 Nf6 Nxe5 |
| 1 | e3 e5 d4 |

## 6. Does Chess.com's Book come back after it stops?

Book plies after a non-Book ply: 131, in 35 games.

First moves and whether CC called them Book: e4 Book 355, d4 Book 129, c4 Book 21, Nf3 Book 19, e3 Book 17, g3 Book 7, Nc3 Book 6, f4 Book 5, d3 Book 4, g4 Book 4, a3 Book 3, c3 Book 2

## 7. Last Chess.com Book ply per game

| Last CC Book ply | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Games | 3 | 17 | 62 | 63 | 53 | 72 | 64 | 53 | 48 | 34 | 35 | 20 | 14 | 10 | 2 | 7 | 6 | 2 | 1 | 2 | 9 |

Median last Book ply: Chess.com 6, ours 5. Mean 6.5 vs 5.5.

