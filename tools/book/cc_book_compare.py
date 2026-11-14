"""Compare our opening book with Chess.com's embedded book, position by position.

Input 1: a TSV export of Chess.com's embedded book, made from the local libcee oracle (never
committed): polyglot key, name id, family id, flag, TCN move list, ECO, opening slug.
Input 2: our lichess `chess-openings` TSV directory (the book the server ships).

Run (from the research repo root):
    uv run --no-project --with chess python tools/book/cc_book_compare.py <ccbook.tsv> <openings-dir>

Only aggregate numbers and short opening names are printed.
"""

from __future__ import annotations

import collections
import glob
import json
import os
import re
import statistics
import sys

import chess
import chess.polyglot

CCBOOK, OPENINGS = sys.argv[1], sys.argv[2]
EXTRA = sys.argv[3:]  # optional extra books: name=path-to-tsv-dir-or-json
CAL = "tests/calibration"
TCN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?{~}(^)[_]@#$,./&-*++="


def tcn_moves(s: str):
    for i in range(0, len(s), 2):
        f, t = TCN.index(s[i]), TCN.index(s[i + 1])
        promo = None
        if t > 63:
            promo = "qnrbkp"[(t - 64) // 3]
            t = f + (-8 if f < 16 else 8) + (t - 1) % 3 - 1
        yield chess.Move(f, t, chess.Piece.from_symbol(promo).piece_type if promo else None)


def zh(b: chess.Board) -> int:
    return chess.polyglot.zobrist_hash(b)


# ------------------------------------------------------------------ Chess.com book
cc = {}  # key -> (depth, eco, slug, flag, family)
bad = 0
cc_keys_raw = set()
for row in open(CCBOOK, encoding="latin1"):
    k, a, fam, flag, tcn, eco, slug = row.rstrip("\n").split("\t")
    key = int(k, 16)
    cc_keys_raw.add(key)
    b = chess.Board()
    try:
        for m in tcn_moves(tcn):
            if m not in b.legal_moves:
                raise ValueError
            b.push(m)
    except ValueError:
        bad += 1
        continue
    cc[key] = (b.ply(), eco, slug, flag, fam, b.fen())
ok = sum(1 for k, v in cc.items() if zh(chess.Board(v[5])) == k)

# prefix closure: is every position along each record's line also a record?
missing_prefix = 0
lines_with_gap = 0
for row in open(CCBOOK, encoding="latin1"):
    tcn = row.rstrip("\n").split("\t")[4]
    b = chess.Board()
    gap = False
    for m in list(tcn_moves(tcn))[:-1]:
        b.push(m)
        if zh(b) not in cc_keys_raw:
            missing_prefix += 1
            gap = True
    lines_with_gap += gap

# ------------------------------------------------------------------ our book
ours = {}  # key -> depth
ours_lines = []
for path in sorted(glob.glob(os.path.join(OPENINGS, "*.tsv"))):
    for row in open(path, encoding="utf-8"):
        cols = row.rstrip("\n").split("\t")
        if len(cols) < 3 or cols[0] == "eco":
            continue
        b = chess.Board()
        try:
            for tok in cols[2].split():
                tok = tok.lstrip("0123456789.")
                if tok:
                    b.push_san(tok)
                    k = zh(b)
                    ours[k] = min(ours.get(k, 99), b.ply())
        except ValueError:
            continue
        ours_lines.append((cols[0], cols[1], b.ply(), zh(b)))

out = []
w = out.append
w(f"Chess.com records: {len(cc_keys_raw)}; decoded {len(cc)} ({bad} failed); polyglot key matches the decoded line: {ok}.")
w(f"Prefix closure: {missing_prefix} prefix positions missing, in {lines_with_gap} lines.")
w(f"Distinct ECO codes: CC {len({v[1] for v in cc.values()})}. Flag values: {collections.Counter(v[3] for v in cc.values())}.")
base_names = collections.Counter(re.split(r"-\d+\.|\.\.\.", v[2])[0] for v in cc.values())
w(f"Distinct base names (slug before the move suffix): {len(base_names)}. Our named lines: {len(ours_lines)}, positions {len(ours)}.\n")

# depth histograms
w("## Positions per ply depth\n")
dc = collections.Counter(min(v[0], 30) for v in cc.values())
do = collections.Counter(min(d, 30) for d in ours.values())
w("| Ply | " + " | ".join(str(i) for i in range(1, 31)) + " |")
w("|---|" + "---|" * 30)
w("| Chess.com | " + " | ".join(str(dc[i]) for i in range(1, 31)) + " |")
w("| Ours | " + " | ".join(str(do[i]) for i in range(1, 31)) + " |")
w(f"\nMedian depth: CC {statistics.median(v[0] for v in cc.values())}, ours {statistics.median(ours.values())}. Max: CC {max(v[0] for v in cc.values())}, ours {max(ours.values())}.\n")

# overlap
cck = set(cc)
ok_ = set(ours)
both = cck & ok_
w("## Overlap\n")
w(f"| Set | Positions |\n|---|---|\n| In both | {len(both)} |\n| Only Chess.com | {len(cck - ok_)} |\n| Only ours | {len(ok_ - cck)} |\n")
w(f"Our positions found in Chess.com's book: {len(both) / len(ok_):.1%}. Chess.com's found in ours: {len(both) / len(cck):.1%}.\n")

# which of our lines CC lacks: line ends not in CC, grouped by first name word
w("Our named line ends that Chess.com's book lacks (examples):\n")
lack = [(eco, name, d) for eco, name, d, k in ours_lines if k not in cck]
w(f"{len(lack)} of {len(ours_lines)} line ends. By depth: " + ", ".join(f"{d}: {n}" for d, n in sorted(collections.Counter(min(x[2], 12) for x in lack).items())))
for eco, name, d in sorted(lack, key=lambda x: x[2])[:30]:
    w(f"- {eco} {name} (ply {d})")
w("")

# flagged records
w("## Records with the 2801 flag (sample)\n")
fl = [v for v in cc.values() if v[3] != "0"]
w(f"{len(fl)} records; depth median {statistics.median(v[0] for v in fl) if fl else '-'}.")
for v in sorted(fl, key=lambda v: v[0])[:12]:
    w(f"- ply {v[0]} {v[1]} {v[2][:90]}")
w("")


# ------------------------------------------------------------------ calibration games
def load_extra(spec):
    name, path = spec.split("=", 1)
    keys = set()
    if os.path.isdir(path):
        files = glob.glob(os.path.join(path, "*.tsv")) + glob.glob(os.path.join(path, "*.json"))
    else:
        files = [path]
    for f in files:
        if f.endswith(".json"):
            data = json.load(open(f, encoding="utf-8"))
            for fen, entry in data.items():
                # every position along the entry's move list (eco.json keys are FENs,
                # sometimes without counters; replaying the moves covers both)
                b = chess.Board()
                try:
                    for tok in (entry.get("moves") or "").split():
                        tok = tok.lstrip("0123456789.")
                        if tok:
                            b.push_san(tok)
                            keys.add(zh(b))
                except ValueError:
                    pass
            continue
        for row in open(f, encoding="utf-8"):
            cols = row.rstrip("\n").split("\t")
            if len(cols) < 3 or cols[0] == "eco":
                continue
            b = chess.Board()
            try:
                for tok in cols[-1].split() if "." in cols[-1] or " " in cols[-1] else []:
                    tok = tok.lstrip("0123456789.")
                    if tok:
                        b.push_san(tok)
                        keys.add(zh(b))
            except ValueError:
                pass
    return name, keys


START = zh(chess.Board())
cc_book_only = {k for k, v in cc.items() if v[3] == "0"}  # records typed "book", not "notable"
notable = cck - cc_book_only
w(f"Record types: 'book' {len(cc_book_only)}, 'notable' {len(notable)} (the third field is an offset into the string table: 0 = \"book\", 2801 = \"notable\").")
w(f"Our positions that Chess.com types 'notable': {len(ok_ & notable)}; typed 'book': {len(ok_ & cc_book_only)}.\n")
books = {
    "ours (lichess chess-openings)": ok_ | {START},
    "Chess.com, all records": cck,
    "Chess.com, 'book' records only": cc_book_only,
}
for spec in EXTRA:
    n, k = load_extra(spec)
    books[n] = k | {START}
    books[n + " + ours"] = k | ok_ | {START}
w("| Book | Positions | Share of Chess.com 'book' set covered | Positions not in Chess.com's book |")
w("|---|---|---|---|")
for n, k in books.items():
    w(f"| {n} | {len(k)} | {len(k & cc_book_only) / len(cc_book_only):.1%} | {len(k - cck)} |")
w("")

plies = []
eco_url_hits = eco_url_total = 0
for sf in sorted(glob.glob(os.path.join(CAL, "cc-reviews", "*.sf.txt"))):
    gid = os.path.basename(sf).split(".")[0]
    b = chess.Board()
    seq = []
    for line in open(sf, encoding="utf-8"):
        p = line.split()
        if not p or not p[0].isdigit():
            continue
        before = zh(b)
        b.push(chess.Move.from_uci(p[1]))
        seq.append((before, zh(b), p[2] == "book"))
    plies.append((gid, seq))
    # does the PGN's ECOUrl name the last Chess.com-book position on the game's path?
    try:
        pgn = open(os.path.join(CAL, "games", f"{gid}.pgn"), encoding="utf-8").read()
        m = re.search(r'\[ECOUrl "https://www.chess.com/openings/([^"]+)"\]', pgn)
    except OSError:
        m = None
    if m:
        eco_url_total += 1
        slugs = [cc[a][2] for _, a, _ in seq if a in cc]
        if slugs and slugs[-1] == m.group(1):
            eco_url_hits += 1

w("## Calibration games (577): Book label agreement per book and rule\n")
w("| Book | Rule | TP | FP | FN | Precision | Recall | Plies agreeing |")
w("|---|---|---|---|---|---|---|---|")
total = sum(len(s) for _, s in plies)
for name, keys in books.items():
    for rule in ("after", "before+after"):
        tp = fp = fn = 0
        for _, seq in plies:
            for before, after, lab in seq:
                pred = after in keys and (rule == "after" or before in keys)
                tp += pred and lab
                fp += pred and not lab
                fn += lab and not pred
        w(f"| {name} | {rule} | {tp} | {fp} | {fn} | {tp / max(1, tp + fp):.3f} | {tp / max(1, tp + fn):.3f} | {1 - (fp + fn) / total:.4f} |")
w(f"\nPGN `ECOUrl` equals the slug of the game's last position found in Chess.com's book: {eco_url_hits} of {eco_url_total} games.\n")

# Remaining disagreements with the Chess.com book itself
fps = collections.Counter()
for gid, seq in plies:
    for i, (before, after, lab) in enumerate(seq):
        pred = after in cc_book_only and before in cc_book_only
        if pred != lab:
            fps["CC book has it, label is not Book" if pred else "label is Book, not in CC book"] += 1
w("Disagreements left with Chess.com's own book ('book' records, before+after rule): " + (", ".join(f"{k}: {v}" for k, v in fps.items()) or "none") + f" of {total} plies.\n")

print("\n".join(out))
