#!/usr/bin/env python3
"""Compare the headline numbers of two or more calibration runs (their summary.json files).

    python3 tools/calibrate/diff_runs.py baseline fix1-brilliant fix2-material
    python3 tools/calibrate/diff_runs.py baseline fix1-brilliant --markdown

Each argument is a run name under --runs-dir, or a path to a run directory or summary.json.
The last column is the change from the first run to the last one. Python 3 standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LABELS = [
    "brilliant",
    "great",
    "best",
    "excellent",
    "good",
    "book",
    "inaccuracy",
    "mistake",
    "miss",
    "blunder",
]


def load(arg: str, runs_dir: Path) -> tuple[str, dict]:
    p = Path(arg)
    candidates = [p / "summary.json", p] if p.suffix == ".json" or p.is_dir() else []
    candidates.append(runs_dir / arg / "summary.json")
    for c in candidates:
        if c.is_file():
            data = json.loads(c.read_text(encoding="utf-8"))
            return data.get("run_name") or c.parent.name, data
    raise SystemExit(f"diff_runs.py: no summary.json for {arg!r} (looked in {runs_dir / arg})")


def get(d: dict, *path):
    for k in path:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


# (row label, value getter, kind) where kind is "pct" (0-1 shown as %), "num", "int" or "text".
def metric_rows():
    rows = [
        ("commit", lambda s: (s.get("git_commit") or "")[:10] + ("*" if s.get("backend_dirty") else ""), "text"),
        ("engine", lambda s: s.get("engine"), "text"),
        ("depth/multipv", lambda s: f"{get(s, 'settings', 'depth')}/{get(s, 'settings', 'multipv')}", "text"),
        ("config override", lambda s: "yes" if get(s, "settings", "config") else "no", "text"),
        ("games compared", lambda s: get(s, "games", "compared"), "int"),
        ("plies scored", lambda s: get(s, "plies", "scored"), "int"),
        ("exact", lambda s: s.get("exact_agreement"), "pct"),
        ("within one", lambda s: s.get("within_one_agreement"), "pct"),
        ("brilliant P", lambda s: get(s, "per_label", "brilliant", "precision"), "num"),
        ("brilliant R", lambda s: get(s, "per_label", "brilliant", "recall"), "num"),
        ("brilliant /100 ours (app)", lambda s: _per100(s, "brilliant"), "text"),
        ("great P", lambda s: get(s, "per_label", "great", "precision"), "num"),
        ("great R", lambda s: get(s, "per_label", "great", "recall"), "num"),
        ("great /100 ours (app)", lambda s: _per100(s, "great"), "text"),
        ("accuracy MAD", lambda s: get(s, "accuracy", "mad"), "num2"),
        ("accuracy bias", lambda s: get(s, "accuracy", "bias"), "signed"),
    ]
    rows += [(f"F1 {lab}", (lambda lab: lambda s: get(s, "per_label", lab, "f1"))(lab), "num") for lab in LABELS]
    return rows


def _per100(s: dict, lab: str) -> str:
    ours, app = get(s, "per_100_moves", lab, "ours"), get(s, "per_100_moves", lab, "app")
    if ours is None:
        return "-"
    return f"{ours:.2f} ({app:.2f})" if app is not None else f"{ours:.2f}"


def fmt(value, kind: str) -> str:
    if value is None:
        return "-"
    if kind == "pct":
        return f"{100 * value:.1f}%"
    if kind == "num":
        return f"{value:.3f}"
    if kind == "num2":
        return f"{value:.2f}"
    if kind == "signed":
        return f"{value:+.2f}"
    return str(value)


def delta(first, last, kind: str) -> str:
    if not isinstance(first, (int, float)) or not isinstance(last, (int, float)):
        return ""
    d = last - first
    if kind == "pct":
        return f"{100 * d:+.1f}pt"
    if kind in ("num", "num2", "signed"):
        return f"{d:+.3f}" if kind == "num" else f"{d:+.2f}"
    if kind == "int":
        return f"{d:+d}"
    return ""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("runs", nargs="+", help="run names (or run directories / summary.json paths)")
    ap.add_argument("--runs-dir", default=str(REPO_ROOT / "tests/calibration/runs"))
    ap.add_argument("--markdown", action="store_true", help="print a Markdown table")
    args = ap.parse_args(argv)
    if len(args.runs) < 2:
        ap.error("give at least two runs")
    runs = [load(r, Path(args.runs_dir)) for r in args.runs]

    header = ["metric"] + [name for name, _ in runs] + [f"delta ({runs[0][0]} -> {runs[-1][0]})"]
    table = []
    for label, getter, kind in metric_rows():
        values = [getter(s) for _, s in runs]
        table.append([label] + [fmt(v, kind) for v in values] + [delta(values[0], values[-1], kind)])

    if args.markdown:
        print("| " + " | ".join(header) + " |")
        print("|---|" + "|".join("---:" for _ in header[1:]) + "|")
        for row in table:
            print("| " + " | ".join(row) + " |")
    else:
        widths = [max(len(str(r[i])) for r in [header] + table) for i in range(len(header))]
        for n, row in enumerate([header] + table):
            print("  ".join(c.ljust(widths[i]) if i == 0 else c.rjust(widths[i]) for i, c in enumerate(row)))
            if n == 0:
                print("  ".join("-" * w for w in widths))

    id_sets = {name: tuple(get(s, "games", "compared_ids") or []) for name, s in runs}
    if len(set(id_sets.values())) > 1:
        print(
            "\nwarning: the runs compared different game sets; numbers are not directly comparable:",
            file=sys.stderr,
        )
        base = set(id_sets[runs[0][0]])
        for name, ids in id_sets.items():
            extra, missing = sorted(set(ids) - base), sorted(base - set(ids))
            if extra or missing:
                print(f"  {name}: +{extra} -{missing} vs {runs[0][0]}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
