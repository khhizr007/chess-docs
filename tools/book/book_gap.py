"""Why our Book labels differ from Chess.com's.

Rebuilds our Book rule exactly as the server does (backend/crates/review-server/src/openings.rs
and analysis/mod.rs::book_flags): every position along every line of the lichess
`chess-openings` TSVs is "book"; a move is Book when the position after it is in that set
(transpositions count, `book_requires_unbroken` = false). Compares it, ply by ply, with
Chess.com's labels in tests/calibration/cc-reviews/*.sf.txt, then breaks the disagreements down.

Run (from the research repo root):
    uv run --with chess python tools/book/book_gap.py <path-to-openings-dir> > out.md
"""

from __future__ import annotations

import collections
import glob
import json
import os
import statistics
import sys

import chess

OPENINGS = sys.argv[1] if len(sys.argv) > 1 else "../chess-review-public/backend/data/openings"
CAL = "tests/calibration"


def key(b: chess.Board) -> str:
    return b.epd(en_passant="legal")


# ---------------------------------------------------------------- our book
book: dict[str, int] = {}  # epd -> shallowest ply it appears at
named: dict[str, str] = {}  # epd -> name, for line ends
children: dict[str, set[str]] = collections.defaultdict(set)  # epd -> book moves (uci) from it
line_count = 0
for path in sorted(glob.glob(os.path.join(OPENINGS, "*.tsv"))):
    for row in open(path, encoding="utf-8"):
        cols = row.rstrip("\n").split("\t")
        if len(cols) < 3 or cols[0] == "eco":
            continue
        b = chess.Board()
        ok = True
        seq = []
        for tok in cols[2].split():
            tok = tok.lstrip("0123456789.")
            if not tok:
                continue
            try:
                m = b.parse_san(tok)
            except ValueError:
                ok = False
                break
            parent = key(b)
            b.push(m)
            seq.append((parent, m.uci(), key(b), b.ply()))
        if not ok or not seq:
            continue
        line_count += 1
        for parent, uci, k, ply in seq:
            book[k] = min(book.get(k, 999), ply)
            children[parent].add(uci)
        named[seq[-1][2]] = f"{cols[0]} {cols[1]}"

# ---------------------------------------------------------------- games
def elo_band(e: int) -> str:
    for hi, name in ((1000, "<1000"), (1600, "1000-1599"), (2200, "1600-2199")):
        if e < hi:
            return name
    return "2200+"


rows = []  # one per ply
games = 0
skipped = 0
for sf in sorted(glob.glob(os.path.join(CAL, "cc-reviews", "*.sf.txt"))):
    gid = os.path.basename(sf).split(".")[0]
    try:
        meta = json.load(open(os.path.join(CAL, "games", f"{gid}.labels.json"), encoding="utf-8"))
        elo = max(int(meta.get("white_elo") or 0), int(meta.get("black_elo") or 0))
        tc = (meta.get("batch5") or {}).get("time_class") or "?"
    except (OSError, ValueError):
        elo, tc = 0, "?"
    b = chess.Board()
    plies = []
    good = True
    for line in open(sf, encoding="utf-8"):
        parts = line.split()
        if not parts or not parts[0].isdigit():
            continue
        uci, label = parts[1], parts[2]
        try:
            m = chess.Move.from_uci(uci)
            if m not in b.legal_moves:
                raise ValueError
        except ValueError:
            good = False
            break
        before = key(b)
        san = b.san(m)
        b.push(m)
        after = key(b)
        plies.append(
            dict(
                gid=gid,
                ply=b.ply(),
                san=san,
                uci=uci,
                cc=label == "book",
                cc_label=label,
                ours=after in book,
                before_in=before in book,
                before=before,
                after=after,
                elo=elo,
                band=elo_band(elo),
                tc=tc,
            )
        )
    if not good:
        skipped += 1
        continue
    games += 1
    # unbroken flag and per-game context
    run = True
    for p in plies:
        run = run and p["ours"]
        p["ours_unbroken"] = run
    rows.extend(plies)
    # per-game runs
cc_runs = collections.defaultdict(list)
for p in rows:
    cc_runs[p["gid"]].append(p)

# ---------------------------------------------------------------- report
out = []
w = out.append


def pr(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0
    r = tp / (tp + fn) if tp + fn else 0
    return p, r


def conf(sel, rule="ours"):
    tp = sum(1 for p in sel if p["cc"] and p[rule])
    fp = sum(1 for p in sel if not p["cc"] and p[rule])
    fn = sum(1 for p in sel if p["cc"] and not p[rule])
    tn = len(sel) - tp - fp - fn
    return tp, fp, fn, tn


w(f"Our book: {line_count} named lines, {len(book)} positions. Games: {games} ({skipped} skipped), plies {len(rows)}.\n")

w("## 1. Agreement\n")
w("| Rule | Book both | We say Book, CC not | CC says Book, we not | P | R |")
w("|---|---|---|---|---|---|")
for rule, name in (("ours", "position after the move is in our book (shipped rule)"), ("ours_unbroken", "unbroken from move 1")):
    tp, fp, fn, tn = conf(rows, rule)
    p, r = pr(tp, fp, fn)
    w(f"| {name} | {tp} | {fp} | {fn} | {p:.3f} | {r:.3f} |")
cc_total = sum(p["cc"] for p in rows)
w(f"\nChess.com Book plies: {cc_total} ({cc_total / games:.2f} per game). Ours: {sum(p['ours'] for p in rows)} ({sum(p['ours'] for p in rows) / games:.2f}).\n")

# per game: book length
w("## 2. Per game: how long each book lasts\n")
diffs = []
for gid, ps in cc_runs.items():
    cc_last = max((p["ply"] for p in ps if p["cc"]), default=0)
    our_last = max((p["ply"] for p in ps if p["ours"]), default=0)
    diffs.append(cc_last - our_last)
c = collections.Counter()
for d in diffs:
    c["CC longer by 5+" if d >= 5 else "CC longer by 3-4" if d >= 3 else "CC longer by 1-2" if d >= 1 else "same" if d == 0 else "ours longer"] += 1
w("| Last Book ply, Chess.com minus ours | Games |")
w("|---|---|")
for k in ("same", "CC longer by 1-2", "CC longer by 3-4", "CC longer by 5+", "ours longer"):
    w(f"| {k} | {c[k]} ({c[k] / games:.0%}) |")
w(f"\nMean {statistics.mean(diffs):+.2f} plies, median {statistics.median(diffs):+.0f}, max {max(diffs):+d}.\n")

# by rating band and time class
w("## 3. By rating band\n")
w("| Max Elo | Games | CC Book / game | Ours / game | Recall | Precision |")
w("|---|---|---|---|---|---|")
for band in ("<1000", "1000-1599", "1600-2199", "2200+"):
    sel = [p for p in rows if p["band"] == band]
    g = len({p["gid"] for p in sel})
    if not g:
        continue
    tp, fp, fn, tn = conf(sel)
    p, r = pr(tp, fp, fn)
    w(f"| {band} | {g} | {sum(x['cc'] for x in sel) / g:.1f} | {sum(x['ours'] for x in sel) / g:.1f} | {r:.2f} | {p:.2f} |")
w("")

# misses: what kind
w("## 4. Chess.com says Book, we do not (false negatives)\n")
fn_rows = [p for p in rows if p["cc"] and not p["ours"]]
kinds = collections.Counter()
for p in fn_rows:
    if p["before_in"]:
        kinds["a. sibling: position before is in our book, this move is not"] += 1
    else:
        kinds["b. deeper: position before is already out of our book"] += 1
w("| Kind | Plies |")
w("|---|---|")
for k, v in sorted(kinds.items()):
    w(f"| {k} | {v} ({v / len(fn_rows):.0%}) |")
plies_fn = collections.Counter(min(p["ply"], 30) for p in fn_rows)
w("\nPly of the missed Book move (30 = 30+):\n")
w("| Ply | " + " | ".join(str(k) for k in sorted(plies_fn)) + " |")
w("|---|" + "---|" * len(plies_fn))
w("| Missed | " + " | ".join(str(plies_fn[k]) for k in sorted(plies_fn)) + " |")
# how far past our book's end
past = []
for gid, ps in cc_runs.items():
    our_last = 0
    for p in ps:
        if p["ours"]:
            our_last = p["ply"]
        if p["cc"] and not p["ours"]:
            past.append(p["ply"] - our_last)
pc = collections.Counter(min(x, 8) for x in past)
w("\nPlies after our last Book ply (8 = 8+): " + ", ".join(f"{k}: {pc[k]}" for k in sorted(pc)) + "\n")
# most frequent missed positions (move sequence)
seqs = collections.Counter()
for gid, ps in cc_runs.items():
    for i, p in enumerate(ps):
        if p["cc"] and not p["ours"]:
            seqs[" ".join(x["san"] for x in ps[: i + 1])] += 1
            break  # first miss per game only
w("Most common first missed Book move (the whole line up to it):\n")
w("| Games | Line (last move is CC Book, not ours) |")
w("|---|---|")
for s, n in seqs.most_common(25):
    w(f"| {n} | {s} |")
w("")

# false positives
w("## 5. We say Book, Chess.com does not (false positives)\n")
fp_rows = [p for p in rows if p["ours"] and not p["cc"]]
lab = collections.Counter(p["cc_label"] for p in fp_rows)
w("Chess.com's label on those moves: " + ", ".join(f"{k} {v}" for k, v in lab.most_common()) + "\n")
fpk = collections.Counter()
for p in fp_rows:
    prev = [x for x in cc_runs[p["gid"]] if x["ply"] == p["ply"] - 1]
    prev_cc = prev[0]["cc"] if prev else True
    fpk["after CC already left book (transposition back in)" if not prev_cc else "CC's book stops here, ours goes on"] += 1
for k, v in fpk.most_common():
    w(f"- {k}: {v}")
seqs = collections.Counter()
for gid, ps in cc_runs.items():
    for i, p in enumerate(ps):
        if p["ours"] and not p["cc"]:
            seqs[" ".join(x["san"] for x in ps[: i + 1])] += 1
            break
w("\n| Games | Line (last move is our Book, not CC) |")
w("|---|---|")
for s, n in seqs.most_common(20):
    w(f"| {n} | {s} |")
w("")

# CC transpositions / continuity
w("## 6. Does Chess.com's Book come back after it stops?\n")
back = 0
gap_games = 0
for gid, ps in cc_runs.items():
    left = False
    hit = False
    for p in ps:
        if not p["cc"]:
            left = True
        elif left:
            back += 1
            hit = True
    gap_games += hit
w(f"Book plies after a non-Book ply: {back}, in {gap_games} games.\n")
# Book after a ply's labels include non-book for the other side? first move
first = collections.Counter((ps[0]["san"], ps[0]["cc"]) for ps in cc_runs.values() if ps)
w("First moves and whether CC called them Book: " + ", ".join(f"{s} {'Book' if b else 'not'} {n}" for (s, b), n in first.most_common(12)) + "\n")

# where CC's book is silent on positions in our book that are common
w("## 7. Last Chess.com Book ply per game\n")
lasts = [max((p["ply"] for p in ps if p["cc"]), default=0) for ps in cc_runs.values()]
lc = collections.Counter(min(x, 20) for x in lasts)
w("| Last CC Book ply | " + " | ".join(str(k) for k in sorted(lc)) + " |")
w("|---|" + "---|" * len(lc))
w("| Games | " + " | ".join(str(lc[k]) for k in sorted(lc)) + " |")
lasts_o = [max((p["ply"] for p in ps if p["ours"]), default=0) for ps in cc_runs.values()]
w(f"\nMedian last Book ply: Chess.com {statistics.median(lasts)}, ours {statistics.median(lasts_o)}. Mean {statistics.mean(lasts):.1f} vs {statistics.mean(lasts_o):.1f}.\n")

print("\n".join(out))
