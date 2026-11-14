"""The plies where Chess.com's own embedded book and its Book label still disagree.

Run: uv run --no-project --with chess python tools/book/cc_book_residual.py <ccbook.tsv>
"""

import collections
import glob
import os
import sys

import chess
import chess.polyglot


def zh(b):
    return chess.polyglot.zobrist_hash(b)


CCBOOK = sys.argv[1]
flag = {}
for row in open(CCBOOK, encoding="latin1"):
    k, a, fam, fl, tcn, eco, slug = row.rstrip("\n").split("\t")
    flag[int(k, 16)] = fl
start = zh(chess.Board())
print("start position in CC book:", start in flag, "flag", flag.get(start))

rows = []
for sf in sorted(glob.glob(os.path.join("tests/calibration", "cc-reviews", "*.sf.txt"))):
    b = chess.Board()
    prev_lab = True
    for line in open(sf, encoding="utf-8"):
        p = line.split()
        if not p or not p[0].isdigit():
            continue
        before = zh(b)
        m = chess.Move.from_uci(p[1])
        san = b.san(m)
        b.push(m)
        after = zh(b)
        rows.append(dict(ply=b.ply(), san=san, lab=p[2], before=flag.get(before), after=flag.get(after),
                         prev_book=prev_lab, legal=b.legal_moves.count()))
        prev_lab = p[2] == "book"


def score(name, pred):
    tp = sum(1 for r in rows if pred(r) and r["lab"] == "book")
    fp = sum(1 for r in rows if pred(r) and r["lab"] != "book")
    fn = sum(1 for r in rows if not pred(r) and r["lab"] == "book")
    print(f"| {name} | {tp} | {fp} | {fn} | {tp / (tp + fp):.3f} | {tp / (tp + fn):.3f} |")


print("| Rule | TP | FP | FN | P | R |\n|---|---|---|---|---|---|")
score("after in book", lambda r: r["after"] is not None)
score("before and after in book", lambda r: r["after"] is not None and r["before"] is not None)
score("after in book, flag 0", lambda r: r["after"] == "0")
score("before+after, after flag 0", lambda r: r["after"] == "0" and r["before"] is not None)
score("before+after, both flag 0", lambda r: r["after"] == "0" and r["before"] == "0")
left = [r for r in rows if r["after"] == "0" and r["before"] is not None and r["lab"] != "book"]
print("left after the flag rule:", [(r["ply"], r["san"], r["lab"], r["before"], r["prev_book"]) for r in left])
score("before+after, previous ply labelled Book", lambda r: r["after"] is not None and r["before"] is not None and r["prev_book"])

res = [r for r in rows if r["after"] is not None and r["before"] is not None and r["lab"] != "book"]
print("\nResidual (before+after in book, label not Book):", len(res))
print("labels:", collections.Counter(r["lab"] for r in res).most_common())
print("after-flag:", collections.Counter(r["after"] for r in res).most_common())
print("previous ply Book:", collections.Counter(r["prev_book"] for r in res).most_common())
print("ply:", sorted(collections.Counter(r["ply"] for r in res).items()))
print("forced (one legal reply irrelevant) / sample:", [(r["ply"], r["san"], r["lab"]) for r in res[:25]])
fl_book = [r for r in rows if r["after"] == "2801"]
print("\nPlies landing on a 2801-flag position:", len(fl_book), collections.Counter(r["lab"] for r in fl_book).most_common())
