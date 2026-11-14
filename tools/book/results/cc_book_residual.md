start position in CC book: True flag 0
| Rule | TP | FP | FN | P | R |
|---|---|---|---|---|---|
| after in book | 3621 | 211 | 0 | 0.945 | 1.000 |
| before and after in book | 3621 | 138 | 0 | 0.963 | 1.000 |
| after in book, flag 0 | 3621 | 77 | 0 | 0.979 | 1.000 |
| before+after, after flag 0 | 3621 | 8 | 0 | 0.998 | 1.000 |
| before+after, both flag 0 | 3621 | 0 | 0 | 1.000 | 1.000 |
left after the flag rule: [(8, 'exd4', 'good', '2801', False), (5, 'Bc4', 'miss', '2801', False), (7, 'exd5', 'best', '2801', False), (5, 'g3', 'excellent', '2801', False), (6, 'e6', 'good', '2801', False), (8, 'Bc5', 'miss', '2801', False), (6, 'Nc6', 'inaccuracy', '2801', False), (4, 'd6', 'inaccuracy', '2801', False)]
| before+after, previous ply labelled Book | 3585 | 92 | 36 | 0.975 | 0.990 |

Residual (before+after in book, label not Book): 138
labels: [('good', 39), ('best', 33), ('inaccuracy', 28), ('excellent', 16), ('mistake', 14), ('miss', 3), ('great', 3), ('blunder', 2)]
after-flag: [('2801', 130), ('0', 8)]
previous ply Book: [(True, 92), (False, 46)]
ply: [(1, 3), (2, 5), (3, 32), (4, 33), (5, 22), (6, 15), (7, 10), (8, 4), (9, 1), (10, 4), (11, 4), (12, 3), (13, 1), (16, 1)]
forced (one legal reply irrelevant) / sample: [(2, 'Nc6', 'excellent'), (5, 'a3', 'good'), (4, 'c6', 'inaccuracy'), (3, 'e4', 'good'), (4, 'Qf6', 'inaccuracy'), (5, 'Bc4', 'excellent'), (7, 'Nxe5', 'mistake'), (8, 'Nxe5', 'best'), (6, 'h6', 'good'), (3, 'd4', 'best'), (4, 'c6', 'excellent'), (5, 'dxc6', 'best'), (6, 'Nxc6', 'best'), (4, 'd5', 'inaccuracy'), (5, 'exd5', 'best'), (4, 'Nc6', 'good'), (6, 'h6', 'good'), (3, 'e4', 'inaccuracy'), (3, 'Qh5', 'good'), (4, 'Nf6', 'excellent'), (3, 'Bc4', 'inaccuracy'), (4, 'd5', 'best'), (3, 'Qh5', 'good'), (4, 'c6', 'good'), (5, 'dxc6', 'best')]

Plies landing on a 2801-flag position: 134 [('good', 39), ('best', 33), ('inaccuracy', 27), ('excellent', 15), ('mistake', 14), ('great', 3), ('blunder', 2), ('miss', 1)]
