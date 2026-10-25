#!/usr/bin/env python3
"""Checks the coach's tactic detectors against the lichess puzzle themes.

The lichess puzzle database (https://database.lichess.org/#puzzles, CC0) labels every puzzle with
themes such as fork, pin or hangingPiece. This tool takes a stratified sample of it, runs our
detectors on each solution line (the `puzzle_tags` example of review-server) and measures, per
theme, how often our tags agree. See docs/calibration/detector-check.md.

A puzzle is the opponent's move (the first of `Moves`) and then the solution: the solver's moves
and the opponent's forced replies. Our example plays the opponent's move and reads the solution as
a line, the way coach/circ.rs reads an engine line, in two ways:

- fired: every tactic a detector finds on one of the solver's moves;
- said: the event the coach says for the line as a best move (MISSES: the tactic behind the
  material it wins, WINS_MATERIAL or LEADS_TO), and as the reply to the opponent's move (PERMITS:
  a tactic named on the first move only).

Typical use (WSL; the database stays outside the repo):

    python3 tools/calibrate/puzzle_check.py sample --db ~/work/lichess-puzzles/lichess_db_puzzle.csv.zst \
        --out ~/work/lichess-puzzles/sample.jsonl --ids tools/calibrate/puzzle_ids.tsv
    python3 tools/calibrate/puzzle_check.py run --sample ~/work/lichess-puzzles/sample.jsonl \
        --out ~/work/lichess-puzzles/tags.jsonl
    python3 tools/calibrate/puzzle_check.py report --sample ~/work/lichess-puzzles/sample.jsonl \
        --tags ~/work/lichess-puzzles/tags.jsonl --out ~/work/lichess-puzzles/report.md

`sample --from-ids tools/calibrate/puzzle_ids.tsv` rebuilds the committed sample from a database.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import random
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
# The app's checkout, where the example is built: $CHESS_REVIEW_DIR, else ../chess-review.
APP_ROOT = Path(os.environ.get("CHESS_REVIEW_DIR") or REPO_ROOT.parent / "chess-review").resolve()

# The sampled themes: the tactics our detectors claim, and the mates and defender tactics.
THEMES = (
    "fork", "pin", "skewer", "hangingPiece", "discoveredAttack", "doubleCheck", "trappedPiece",
    "backRankMate", "mateIn1", "mateIn2", "attraction", "deflection", "capturingDefender",
    "promotion",
)
RANDOM = "random"
# A free piece as lichess's hangingPiece means it: a non-pawn taken undefended.
HANGING = "free_piece:hanging"

# Our tag -> the lichess themes that say the same thing. Mates differ by reading: on a solver's
# move, Checkmate fires on the mating move of any mate; said for a line, Checkmate and
# BackRankMate mean the first move mates, ForcedMate a longer mate.
FIRED_MAP: dict[str, tuple[str, ...]] = {
    "back_rank_mate": ("backRankMate",),
    "checkmate": ("mate",),
    "free_piece": ("hangingPiece",),
    HANGING: ("hangingPiece",),
    "trapped_piece": ("trappedPiece",),
    "double_check": ("doubleCheck",),
    "royal_fork": ("fork",),
    "fork": ("fork",),
    "discovered_check": ("discoveredAttack",),
    "discovered_attack": ("discoveredAttack",),
    "skewer": ("skewer",),
    "exploits_pin": ("pin",),
    "pin": ("pin",),
    "removes_defender": ("capturingDefender",),
    "overloaded": ("deflection",),
    "attraction": ("attraction",),
    "promotion": ("promotion",),
}
SAID_MAP: dict[str, tuple[str, ...]] = {
    **FIRED_MAP,
    "checkmate": ("mateIn1",),
    "back_rank_mate": ("backRankMate",),
    "forced_mate": ("mateIn2", "mateIn3", "mateIn4", "mateIn5"),
}
# The tags of each theme, for recall.
THEME_TAGS: dict[str, dict[str, set[str]]] = {
    reading: {t: {tag for tag, ths in mapping.items() if t in ths} for t in THEMES}
    for reading, mapping in (("fired", FIRED_MAP), ("said", SAID_MAP), ("permits", SAID_MAP))
}
for t in ("mateIn1", "mateIn2"):
    # A mate puzzle's mating move is found on the board, whatever its length.
    THEME_TAGS["fired"][t] = {"checkmate", "back_rank_mate"}
# Tags with a precision target.
TARGETS = ("fork", "pin", "skewer", "free_piece", HANGING, "discovered_attack")
TARGET_PRECISION = 0.9


def open_db(path: str):
    """The puzzle CSV, from the .zst the site serves or a plain .csv."""
    if path.endswith(".zst"):
        from compression import zstd  # Python 3.14

        return io.TextIOWrapper(zstd.open(path, "rb"), encoding="utf-8", newline="")
    return open(path, encoding="utf-8", newline="")


def puzzle_record(row: dict[str, str], strata: list[str]) -> dict:
    return {
        "id": row["PuzzleId"],
        "fen": row["FEN"],
        "moves": row["Moves"],
        "themes": row["Themes"].split(),
        "rating": int(row["Rating"]),
        "strata": strata,
    }


def cmd_sample(args) -> None:
    out = Path(args.out)
    if args.from_ids:
        wanted: dict[str, list[str]] = {}
        for line in Path(args.from_ids).read_text(encoding="utf-8").splitlines():
            if line and not line.startswith("#"):
                pid, strata_text = line.split("\t")
                wanted[pid] = strata_text.split(",")
        with open_db(args.db) as f, out.open("w", encoding="utf-8") as w:
            found = 0
            for row in csv.DictReader(f):
                if row["PuzzleId"] in wanted:
                    w.write(json.dumps(puzzle_record(row, wanted[row["PuzzleId"]])) + "\n")
                    found += 1
        print(f"{found} of {len(wanted)} puzzles found")
        return

    rng = random.Random(args.seed)
    size = {t: args.per_theme for t in THEMES} | {RANDOM: args.random}
    reservoir: dict[str, list[dict]] = {s: [] for s in size}
    seen = Counter()
    with open_db(args.db) as f:
        for row in csv.DictReader(f):
            if int(row["NbPlays"]) < args.min_plays or int(row["Popularity"]) < args.min_popularity:
                continue
            themes = set(row["Themes"].split())
            for s in [t for t in THEMES if t in themes] + [RANDOM]:
                seen[s] += 1
                r = reservoir[s]
                if len(r) < size[s]:
                    r.append(row)
                else:
                    j = rng.randrange(seen[s])
                    if j < size[s]:
                        r[j] = row
    strata: dict[str, list[str]] = defaultdict(list)
    rows: dict[str, dict] = {}
    for s, r in reservoir.items():
        for row in r:
            strata[row["PuzzleId"]].append(s)
            rows[row["PuzzleId"]] = row
    with out.open("w", encoding="utf-8") as w:
        for pid in sorted(rows):
            w.write(json.dumps(puzzle_record(rows[pid], strata[pid])) + "\n")
    if args.ids:
        with Path(args.ids).open("w", encoding="utf-8", newline="\n") as w:
            w.write("# Lichess puzzle ids (CC0, database.lichess.org) sampled by "
                    "tools/calibrate/puzzle_check.py:\n")
            w.write(f"# seed {args.seed}, {args.per_theme} per theme, {args.random} at random, "
                    f"NbPlays >= {args.min_plays}, Popularity >= {args.min_popularity}.\n")
            w.write("# id<TAB>strata (the themes it was sampled for, or random)\n")
            for pid in sorted(rows):
                w.write(f"{pid}\t{','.join(strata[pid])}\n")
    print(f"{len(rows)} puzzles; eligible per stratum: "
          + ", ".join(f"{s} {seen[s]}" for s in size))


def default_binary() -> str:
    target = os.environ.get("CARGO_TARGET_DIR", str(APP_ROOT / "backend" / "target"))
    return str(Path(target) / "release" / "examples" / "puzzle_tags")


def cmd_run(args) -> None:
    binary = args.binary or default_binary()
    subprocess.run([binary, args.sample, args.out], check=True)


def load(sample: str, tags: str) -> list[dict]:
    puzzles = {}
    for line in Path(sample).read_text(encoding="utf-8").splitlines():
        p = json.loads(line)
        puzzles[p["id"]] = p
    out = []
    for line in Path(tags).read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        p = puzzles[r.pop("id")]
        p.update(r)
        out.append(p)
    return out


def names(f: dict) -> set[str]:
    """A found tag, plus `free_piece:hanging` for a free non-pawn taken undefended (lichess's
    hangingPiece)."""
    out = {f["tag"]}
    if f["tag"] == "free_piece" and f.get("role") != "p" and f.get("defended") is False:
        out.add(HANGING)
    return out


def tags_of(p: dict, reading: str) -> set[str]:
    if reading == "fired":
        return {t for f in p.get("fired", []) for t in names(f)}
    e = p.get("misses" if reading == "said" else "permits")
    return names(e) if e else set()


def fired_text(p: dict) -> str:
    by_ply = defaultdict(list)
    for f in p.get("fired", []):
        by_ply[f["ply"]].append(f["tag"])
    return "; ".join(f"{k}: {' '.join(v)}" for k, v in sorted(by_ply.items())) or "-"


def said_text(p: dict, key: str) -> str:
    e = p.get(key)
    if not e:
        return "-"
    return f"{e['tag']} {'/'.join(e['chain'])} @{e['ply']}"


def solution_san(p: dict) -> str:
    return p["moves"]


def pct(n: int, d: int) -> str:
    return f"{n / d:.2f}" if d else "-"


def cmd_report(args) -> None:
    puzzles = [p for p in load(args.sample, args.tags) if "error" not in p]
    errors = [p for p in load(args.sample, args.tags) if "error" in p]
    out: list[str] = []
    w = out.append
    w(f"Puzzles: {len(puzzles)} checked, {len(errors)} skipped "
      f"({Counter(p['error'] for p in errors).most_common()}).\n")
    random_set = [p for p in puzzles if RANDOM in p["strata"]]

    for reading, mapping in (("said", SAID_MAP), ("fired", FIRED_MAP), ("permits", SAID_MAP)):
        w(f"\n## Precision per tag ({reading})\n")
        w("| our tag | lichess theme | fires (sample) | precision (sample) | fires (random) "
          "| precision (random) |")
        w("|---|---|---:|---:|---:|---:|")
        for tag, themes in mapping.items():
            hits = [p for p in puzzles if tag in tags_of(p, reading)]
            ok = [p for p in hits if set(themes) & set(p["themes"])]
            rh = [p for p in random_set if tag in tags_of(p, reading)]
            ro = [p for p in rh if set(themes) & set(p["themes"])]
            mark = " **(target)**" if tag in TARGETS else ""
            w(f"| {tag}{mark} | {', '.join(themes)} | {len(hits)} | {pct(len(ok), len(hits))} "
              f"| {len(rh)} | {pct(len(ro), len(rh))} |")
        w(f"\n## Recall per theme ({reading})\n")
        w("| lichess theme | puzzles | our tags | recall |")
        w("|---|---:|---|---:|")
        for theme in THEMES:
            ours = THEME_TAGS[reading][theme]
            have = [p for p in puzzles if theme in p["themes"]]
            ok = [p for p in have if ours & tags_of(p, reading)]
            w(f"| {theme} | {len(have)} | {', '.join(sorted(ours))} | {pct(len(ok), len(have))} |")

    w("\n## Confusion: what the coach says for each sampled theme (said, MISSES)\n")
    w("Share of the theme's stratum; the five most common events.\n")
    w("| stratum | n | events |")
    w("|---|---:|---|")
    for s in THEMES + (RANDOM,):
        group = [p for p in puzzles if s in p["strata"]]
        c = Counter(p["misses"]["tag"] if p.get("misses") else "(none)" for p in group)
        top = ", ".join(f"{t} {n / len(group):.0%}" for t, n in c.most_common(5))
        w(f"| {s} | {len(group)} | {top} |")

    w("\n## Circumstances (said, MISSES)\n")
    c = Counter("/".join(p["misses"]["chain"]) if p.get("misses") else "(none)" for p in puzzles)
    w(", ".join(f"{k} {v}" for k, v in c.most_common()))

    w("\n## Examples\n")
    for tag in SAID_MAP:
        for reading, mapping in (("said", SAID_MAP), ("fired", FIRED_MAP)):
            themes = mapping.get(tag)
            if themes is None:
                continue
            fp = [p for p in puzzles if tag in tags_of(p, reading)
                  and not set(themes) & set(p["themes"])]
            if not fp:
                continue
            w(f"\n### {tag}: {reading}, theme absent ({len(fp)})\n")
            # A draw of its own per list, so lists do not shift when another changes.
            for p in random.Random(f"{tag} {reading}").sample(fp, min(args.examples, len(fp))):
                w(f"- `{p['id']}` `{p['fen']}` `{p['moves']}` themes {' '.join(p['themes'])}; "
                  f"said {said_text(p, 'misses')}; fired {fired_text(p)}")
    for theme in THEMES:
        ours = THEME_TAGS["said"][theme]
        fn = [p for p in puzzles if theme in p["themes"] and not ours & tags_of(p, "said")]
        if not fn:
            continue
        w(f"\n### {theme}: theme present, not said ({len(fn)})\n")
        for p in random.Random(theme).sample(fn, min(args.examples, len(fn))):
            w(f"- `{p['id']}` `{p['fen']}` `{p['moves']}` themes {' '.join(p['themes'])}; "
              f"said {said_text(p, 'misses')}; fired {fired_text(p)}")
    text = "\n".join(out) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sample", help="take a stratified sample of the puzzle database")
    s.add_argument("--db", required=True, help="lichess_db_puzzle.csv.zst (or .csv)")
    s.add_argument("--out", required=True, help="sample, JSON lines")
    s.add_argument("--ids", help="also write the sampled ids (with their strata) here")
    s.add_argument("--from-ids", help="take exactly these ids instead of sampling")
    s.add_argument("--per-theme", type=int, default=300)
    s.add_argument("--random", type=int, default=10000, help="puzzles taken at random")
    s.add_argument("--seed", type=int, default=20261021)
    s.add_argument("--min-plays", type=int, default=100)
    s.add_argument("--min-popularity", type=int, default=50)
    r = sub.add_parser("run", help="run our detectors on the sample")
    r.add_argument("--sample", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--binary", help="puzzle_tags example (default: $CARGO_TARGET_DIR/release/...)")
    p = sub.add_parser("report", help="precision, recall, confusion and examples")
    p.add_argument("--sample", required=True)
    p.add_argument("--tags", required=True)
    p.add_argument("--out")
    p.add_argument("--examples", type=int, default=10)
    args = ap.parse_args()
    {"sample": cmd_sample, "run": cmd_run, "report": cmd_report}[args.cmd](args)


if __name__ == "__main__":
    main()
