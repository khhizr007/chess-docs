#!/usr/bin/env python3
"""Fill `app_best_san` in calibration labels files from their `app_best_uci` values.

Uses the `uci2san` example binary (backend/crates/review-server/examples/uci2san.rs), which plays
each UCI move in the position before that ply's move and prints its SAN. Build it first:

    cd ../chess-review/backend && cargo build --release -p review-server --example uci2san

then, from this repository's root:

    python3 tools/calibrate/fill_best_san.py                     # every *.labels.json
    python3 tools/calibrate/fill_best_san.py --games tests/calibration/tuning.txt --dry-run

Only plies whose `app_best_san` is null are filled unless --overwrite is given. Files are rewritten
with 2-space indentation, keeping key order. Python 3 standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
# The app's checkout, where the example is built: $CHESS_REVIEW_DIR, else ../chess-review.
APP_ROOT = Path(os.environ.get("CHESS_REVIEW_DIR") or REPO_ROOT.parent / "chess-review").resolve()


def default_bin() -> str:
    target = os.environ.get("CARGO_TARGET_DIR") or str(APP_ROOT / "backend/target")
    return str(Path(target) / "release/examples/uci2san")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--games-dir", default=str(REPO_ROOT / "tests/calibration/games"))
    ap.add_argument("--games", help="file with one game id per line (default: every labels file)")
    ap.add_argument("--bin", default=default_bin(),
                    help="uci2san binary (default: $CARGO_TARGET_DIR or backend/target, release/examples/uci2san)")
    ap.add_argument("--overwrite", action="store_true", help="replace existing app_best_san values")
    ap.add_argument("--dry-run", action="store_true", help="report changes without writing")
    args = ap.parse_args(argv)

    games_dir = Path(args.games_dir)
    if args.games:
        ids = [line.split("#", 1)[0].strip() for line in Path(args.games).read_text().splitlines()]
        ids = [i for i in ids if i]
    else:
        ids = sorted(p.name[: -len(".labels.json")] for p in games_dir.glob("*.labels.json"))
    if not Path(args.bin).is_file():
        print(f"fill_best_san.py: {args.bin} not found; build it with "
              "`cargo build --release -p review-server --example uci2san`", file=sys.stderr)
        return 2

    filled = errors = files_changed = 0
    for gid in ids:
        labels_path = games_dir / f"{gid}.labels.json"
        pgn_path = games_dir / f"{gid}.pgn"
        if not labels_path.is_file() or not pgn_path.is_file():
            print(f"{gid}: missing {labels_path.name} or {pgn_path.name}", file=sys.stderr)
            errors += 1
            continue
        proc = subprocess.run([args.bin, str(pgn_path), str(labels_path)],
                              capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            print(f"{gid}: uci2san failed: {proc.stderr.strip()}", file=sys.stderr)
            errors += 1
            continue
        sans = {item["ply"]: item for item in json.loads(proc.stdout)}
        labels = json.loads(labels_path.read_text(encoding="utf-8"))
        changed = 0
        for i, ply in enumerate(labels.get("plies") or []):
            item = sans.get(ply.get("ply", i + 1))
            if item is None:
                continue
            if item["error"]:
                print(f"{gid} ply {item['ply']}: {item['error']}", file=sys.stderr)
                errors += 1
                continue
            if ply.get("app_best_san") and not args.overwrite:
                if ply["app_best_san"] != item["san"]:
                    print(f"{gid} ply {item['ply']}: app_best_san {ply['app_best_san']!r} != "
                          f"{item['san']!r} from {item['uci']} (kept; use --overwrite)", file=sys.stderr)
                continue
            if ply.get("app_best_san") != item["san"]:
                ply["app_best_san"] = item["san"]
                changed += 1
        filled += changed
        if changed:
            files_changed += 1
            if not args.dry_run:
                labels_path.write_text(json.dumps(labels, indent=2, ensure_ascii=False) + "\n",
                                       encoding="utf-8")
        print(f"{gid}: {changed} filled")
    verb = "would fill" if args.dry_run else "filled"
    print(f"{verb} {filled} app_best_san value(s) in {files_changed} file(s); {errors} problem(s)")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
