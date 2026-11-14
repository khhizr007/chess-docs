"""What the Book gap does to the rest of the review: our labels and per-move accuracy on the
plies where Chess.com says Book and we do not, and the game-accuracy shift if those were Book.

Run: python tools/book/book_impact.py [run-name]   (default sp-base, our defaults on 2026-11-11)
"""

import collections
import glob
import json
import os
import statistics
import sys

RUN = sys.argv[1] if len(sys.argv) > 1 else "sp-base"
CAL = "tests/calibration"

fn_labels = collections.Counter()
fp_labels = collections.Counter()
fp_precision = collections.Counter()
fn_acc = []
shift = []  # per side: accuracy with CC's Book plies at 100 minus ours
coach_fn = 0
games = 0
for path in sorted(glob.glob(os.path.join(CAL, "runs", RUN, "*.json"))):
    gid = os.path.basename(path).split(".")[0]
    if not gid.isdigit():
        continue
    sf = os.path.join(CAL, "cc-reviews", f"{gid}.sf.txt")
    if not os.path.exists(sf):
        continue
    cc = {}
    for line in open(sf, encoding="utf-8"):
        p = line.split()
        if p and p[0].isdigit():
            cc[int(p[0])] = p[2]
    plies = json.load(open(path, encoding="utf-8"))["result"]["plies"]
    games += 1
    acc = {"white": [], "black": []}
    acc_fixed = {"white": [], "black": []}
    for p in plies:
        lab = cc.get(p["ply"])
        ours = p["classification"]
        a = p.get("accuracy")
        if lab == "book" and ours != "book":
            fn_labels[ours] += 1
            if a is not None:
                fn_acc.append(a)
            if (p.get("coach") or {}).get("sentences"):
                coach_fn += 1
        if ours == "book" and lab is not None and lab != "book":
            fp_labels[lab] += 1
            fp_precision[p.get("precision")] += 1
        if a is not None:
            acc[p["mover"]].append(a)
            acc_fixed[p["mover"]].append(100.0 if lab == "book" else a)
    for side in ("white", "black"):
        if acc[side]:
            shift.append(statistics.mean(acc_fixed[side]) - statistics.mean(acc[side]))

print(f"Run {RUN}: {games} games.\n")
print("Our label where Chess.com says Book and we do not:", ", ".join(f"{k} {v}" for k, v in fn_labels.most_common()))
print(f"  mean per-move accuracy we gave them: {statistics.mean(fn_acc):.1f} (Chess.com: 100); coach note shown on {coach_fn}")
print("Chess.com's label where we say Book and it does not:", ", ".join(f"{k} {v}" for k, v in fp_labels.most_common()))
print("  our own precision grade on those plies:", ", ".join(f"{k} {v}" for k, v in fp_precision.most_common()))
nz = [s for s in shift if abs(s) > 1e-9]
print(f"\nGame accuracy if Chess.com's Book plies scored 100 (one value per side per game, {len(shift)} sides):")
print(f"  sides changed {len(nz)}; mean shift {statistics.mean(shift):+.2f}; mean over changed {statistics.mean(nz):+.2f}; max {max(shift):+.2f}")
print(f"  shift >= 1 point: {sum(s >= 1 for s in shift)}; >= 3 points: {sum(s >= 3 for s in shift)}")
