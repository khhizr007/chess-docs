#!/usr/bin/env python3
"""Phase 0 of the coach: does our coach pick the same explanation as Chess.com?

Compares, per ply, the main event of our coach (`PlyReview.coach`, from a calibration run made with
`compare.py`) with the main event of Chess.com's coach speech for the played move (the
`<id>.keys.json` files written by `coach_oracle.py match`). Only tag and circumstance names are
read on either side, so the report holds no Chess.com text.

Categories for a ply where both sides name an event:

- exact: same tag (per coach_tags.OUR_TAGS) and same circumstance chain;
- same tag, other circumstance;
- same family (coach_tags families);
- different.

Plus: Chess.com explains and we do not, we explain and Chess.com does not, neither.

Typical use (WSL, after the run and the capture):

    python3 tools/calibrate/coach_compare.py --run tests/calibration/runs/coach-phase0 \
        --out tests/calibration/runs/coach-phase0/coach-report.md
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coach_tags as ct  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
# The app's checkout, for the commit in the report: $CHESS_REVIEW_DIR, else ../chess-review.
APP_ROOT = Path(os.environ.get("CHESS_REVIEW_DIR") or REPO_ROOT.parent / "chess-review").resolve()
DEFAULT_ORACLE = Path(os.path.expanduser("~/work/chesscom/oracle"))
BAD = ("inaccuracy", "mistake", "blunder", "miss")
# Chess.com writes Great Find as "great", we write "great_find".
GOOD = ("brilliant", "great", "great_find", "best", "excellent", "good")
CATEGORIES = ("exact", "same tag, other circumstance", "same family", "different",
              "they explain, we don't", "we explain, they don't", "neither")


def load_tag_index(path: Path) -> dict[str, int]:
    out = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            idx, names = line.split("=", 1)
            for n in names.split("/"):
                out.setdefault("".join(p.capitalize() for p in n.strip().lower().split("_")), int(idx))
    return out


def our_main(coach: dict) -> dict | None:
    sents = coach.get("sentences") or []
    if not sents or sents[0].get("event") is None:
        return None
    return coach["events"][sents[0]["event"]]


def our_best(coach: dict) -> dict | None:
    """Our event for what the best move would have done: the first sentence event said as a miss
    (or "better was"), with the misses step removed so it reads like the best move's own speech."""
    events = coach.get("events") or []
    for s in coach.get("sentences") or []:
        i = s.get("event")
        if i is None:
            continue
        ev = events[i]
        if ev["chain"] and ev["chain"][0] in ("misses", "misses_same"):
            return {**ev, "chain": ev["chain"][1:]}
    return None


def fmt_ours(ev: dict | None) -> str:
    if not ev:
        return "-"
    chain = ct.our_chain(ev["chain"], ev["tag"])
    return ">".join([*chain, ev["tag"]])


def fmt_theirs(ev: dict | None) -> str:
    if not ev:
        return "-"
    return ">".join([*ct.cc_chain(ev["chain"], ev["tag"]), ev["tag"]])


def categorise(ours: dict | None, theirs: dict | None, tag_index: dict[str, int]) -> str:
    if ours is None and theirs is None:
        return "neither"
    if ours is None:
        return "they explain, we don't"
    if theirs is None:
        return "we explain, they don't"
    threat = ct.threat_match(ours["tag"], ct.our_chain(ours["chain"], ours["tag"]),
                             theirs["tag"], ct.cc_chain(theirs["chain"], theirs["tag"]))
    if threat == "exact":
        return "exact"
    if threat == "same tag":
        return "same tag, other circumstance"
    if ct.same_tag(ours["tag"], theirs["tag"]):
        if ct.our_chain(ours["chain"], ours["tag"]) == ct.cc_chain(theirs["chain"], theirs["tag"]):
            return "exact"
        return "same tag, other circumstance"
    if ct.our_family(ours["tag"]) == ct.cc_family(theirs["tag"], tag_index.get(theirs["tag"])):
        return "same family"
    return "different"


def ply_ref(gid: str, p: dict) -> str:
    dots = "." if p["mover"] == "white" else "..."
    return f"{gid} {p['move_number']}{dots}{p['san']}"


def compare(args) -> dict:
    tag_index = load_tag_index(args.oracle_dir / "tag_names.txt")
    records, skipped = [], {}
    for run_file in sorted(args.run.glob("[0-9]*.json")):
        gid = run_file.stem
        keys_file = args.captures_dir / f"{gid}.keys.json"
        if not keys_file.is_file():
            skipped[gid] = "no capture"
            continue
        ours = json.loads(run_file.read_text(encoding="utf-8"))["result"]["plies"]
        theirs = json.loads(keys_file.read_text(encoding="utf-8"))
        if theirs.get("score_engines") and set(theirs["score_engines"]) != {"13"}:
            skipped[gid] = f"capture scored by engines {theirs['score_engines']}, not Stockfish 18"
            continue
        tp = theirs["plies"]
        if len(tp) != len(ours) or any(a["uci"] != b["uci"] for a, b in zip(ours, tp)):
            skipped[gid] = "move lists differ"
            continue
        for p, t in zip(ours, tp):
            om = our_main(p.get("coach") or {})
            played = t.get("played") or {}
            tm = played.get("main")
            ob = our_best(p.get("coach") or {})
            tb = (t.get("best") or {}).get("main")
            their_tags = {s["tag"] for s in played.get("sentences", []) if s.get("tag_known")}
            our_tags = {e["tag"] for e in (p.get("coach") or {}).get("events", [])}
            records.append({
                "game": gid,
                "ply": p["ply"],
                "ref": ply_ref(gid, p),
                "phase": p.get("phase"),
                "cc_class": t["classification"],
                "our_class": p["classification"],
                "ours": fmt_ours(om),
                "theirs": fmt_theirs(tm),
                "our_tag": om["tag"] if om else None,
                "their_tag": tm["tag"] if tm else None,
                "their_ambiguous": bool(tm and tm.get("ambiguous")),
                "category": categorise(om, tm, tag_index),
                # Their main tag is among everything we detected (any circumstance): a priority
                # disagreement rather than a missing detector.
                "we_detected_theirs": bool(tm) and any(ct.same_tag(o, tm["tag"]) for o in our_tags),
                "their_family": ct.cc_family(tm["tag"], tag_index.get(tm["tag"])) if tm else None,
                "our_family": ct.our_family(om["tag"]) if om else None,
                "their_other_tags": sorted(their_tags - ({tm["tag"]} if tm else set())),
                # The best alternative's own sentence (Chess.com's best_alternative_move speech
                # against our Misses-block event), compared without the "misses" step.
                "ours_best": fmt_ours(ob),
                "theirs_best": fmt_theirs(tb),
                "best_category": categorise(ob, tb, tag_index) if (ob or tb) else None,
            })
    return {"records": records, "skipped": skipped}


def pct(n: int, d: int) -> str:
    return f"{n / d:.1%}" if d else "-"


def table(header: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out


def category_rows(recs: list[dict], key, keys: list[str]) -> list[list]:
    rows = []
    groups = defaultdict(list)
    for r in recs:
        groups[key(r)].append(r)
    for k in keys:
        g = groups.get(k, [])
        if not g:
            continue
        c = Counter(r["category"] for r in g)
        rows.append([k, len(g), *[f"{c[cat]} ({pct(c[cat], len(g))})" for cat in CATEGORIES]])
    return rows


def git_head() -> str:
    try:
        return subprocess.run(["git", "-C", str(APP_ROOT), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "?"


def report(res: dict, args) -> str:
    recs = res["records"]
    bad = [r for r in recs if r["cc_class"] in BAD]
    games = sorted({r["game"] for r in recs})
    lines = [
        "# Coach agreement with Chess.com (Phase 0)",
        "",
        f"Run `{args.run.name}`, {len(games)} games, {len(recs)} plies, commit `{git_head()}`. "
        "Reference: the main event of Chess.com's speech for the played move.",
        "",
        "## Bad moves (Chess.com Inaccuracy, Mistake, Blunder, Miss)",
        "",
    ]
    c = Counter(r["category"] for r in bad)
    lines += table(["category", "plies", "share"],
                   [[cat, c[cat], pct(c[cat], len(bad))] for cat in CATEGORIES])
    both = [r for r in bad if r["ours"] != "-" and r["theirs"] != "-"]
    lines += ["", f"Where both explain ({len(both)} plies): exact {pct(sum(r['category'] == 'exact' for r in both), len(both))}, "
              f"same tag {pct(sum(r['category'] in ('exact', 'same tag, other circumstance') for r in both), len(both))}, "
              f"same family or better {pct(sum(r['category'] in ('exact', 'same tag, other circumstance', 'same family') for r in both), len(both))}."]
    both_bad = [r for r in bad if r["our_class"] in BAD]
    lines += ["", f"### Plies both apps label bad ({len(both_bad)} of {len(bad)})", "",
              "Phase 1 explains only moves we label Inaccuracy, Mistake, Blunder or Miss, so this is "
              "the coach's own agreement, free of label disagreements.", ""]
    c2 = Counter(r["category"] for r in both_bad)
    lines += table(["category", "plies", "share"],
                   [[cat, c2[cat], pct(c2[cat], len(both_bad))] for cat in CATEGORIES])
    lines += ["", f"Bad by Chess.com but not by us: {len(bad) - len(both_bad)} plies "
              f"(our labels: {dict(Counter(r['our_class'] for r in bad if r['our_class'] not in BAD).most_common())})."]
    det = [r for r in bad if r["theirs"] != "-" and r["category"] not in ("exact", "same tag, other circumstance")]
    lines += [f"Of the {len(det)} bad-move plies where we do not say Chess.com's tag, we detected it "
              f"(in any circumstance) on {sum(r['we_detected_theirs'] for r in det)}."]
    lines += ["", "### By Chess.com classification", ""]
    lines += table(["class", "plies", *CATEGORIES], category_rows(bad, lambda r: r["cc_class"], list(BAD)))
    lines += ["", "### By phase", ""]
    lines += table(["phase", "plies", *CATEGORIES],
                   category_rows(bad, lambda r: r["phase"], ["opening", "middlegame", "endgame"]))
    lines += ["", "## All plies by Chess.com classification", ""]
    classes = ["brilliant", "great", "best", "excellent", "good", "book", "forced", *BAD]
    lines += table(["class", "plies", *CATEGORIES], category_rows(recs, lambda r: r["cc_class"], classes))

    good = [r for r in recs if r["cc_class"] in GOOD]
    both_good = [r for r in good if r["our_class"] in GOOD]
    lines += ["", f"## Good moves (Chess.com {', '.join(GOOD)}; {len(both_good)} plies both apps label good)", ""]
    cg = Counter(r["category"] for r in both_good)
    lines += table(["category", "plies", "share"],
                   [[cat, cg[cat], pct(cg[cat], len(both_good))] for cat in CATEGORIES])
    lines += ["", "### Chess.com's main event on good moves, by family", ""]
    gf = Counter(r["their_family"] or "(none)" for r in both_good)
    lines += table(["family", "plies", "share"], [[f, n, pct(n, len(both_good))] for f, n in gf.most_common()])
    lines += ["", "### Disagreement patterns on good moves (Chess.com → ours)", ""]
    gp = defaultdict(list)
    for r in both_good:
        if r["category"] in ("exact", "neither"):
            continue
        gp[(r["theirs"], r["ours"], r["category"])].append(r)
    lines += table(["Chess.com", "ours", "category", "plies", "examples"],
                   [[t, o, cat, len(rs), "; ".join(x["ref"] for x in rs[:3])]
                    for (t, o, cat), rs in sorted(gp.items(), key=lambda kv: -len(kv[1]))[: args.top]])

    bb = [r for r in both_bad if r["best_category"]]
    lines += ["", f"## The best-move sentence on plies both label bad ({len(bb)} with a sentence on either side)", "",
              "Chess.com's speech for the best alternative against our Misses-block event, without the "
              "\"misses\" step.", ""]
    cb = Counter(r["best_category"] for r in bb)
    lines += table(["category", "plies", "share"], [[cat, cb[cat], pct(cb[cat], len(bb))] for cat in CATEGORIES])
    bp = defaultdict(list)
    for r in bb:
        if r["best_category"] in ("exact", "neither"):
            continue
        bp[(r["theirs_best"], r["ours_best"], r["best_category"])].append(r)
    lines += ["", "### Patterns (Chess.com → ours)", ""]
    lines += table(["Chess.com", "ours", "category", "plies", "examples"],
                   [[t, o, cat, len(rs), "; ".join(x["ref"] for x in rs[:3])]
                    for (t, o, cat), rs in sorted(bp.items(), key=lambda kv: -len(kv[1]))[: args.top]])

    lines += ["", "## Chess.com's main event on bad moves, by family", ""]
    fam = Counter(r["their_family"] or "(none)" for r in bad)
    lines += table(["family", "plies", "share"], [[f, n, pct(n, len(bad))] for f, n in fam.most_common()])
    lines += ["", "## Chess.com's most frequent main events on bad moves", ""]
    tc = Counter(r["theirs"] for r in bad)
    lines += table(["Chess.com event", "plies", "ours exact"],
                   [[t, n, sum(1 for r in bad if r["theirs"] == t and r["category"] == "exact")]
                    for t, n in tc.most_common(25)])

    lines += ["", "## Disagreement patterns on plies both apps label bad (Chess.com → ours)", ""]
    pats = defaultdict(list)
    for r in both_bad:
        if r["category"] in ("exact", "neither"):
            continue
        pats[(r["theirs"], r["ours"], r["category"])].append(r)
    rows = []
    for (t, o, cat), rs in sorted(pats.items(), key=lambda kv: -len(kv[1]))[: args.top]:
        refs = "; ".join(x["ref"] for x in rs[:4])
        rows.append([t, o, cat, len(rs), f"{sum(x['we_detected_theirs'] for x in rs)}", refs])
    lines += table(["Chess.com", "ours", "category", "plies", "we detected theirs", "examples"], rows)
    if res["skipped"]:
        lines += ["", "## Skipped games", ""]
        lines += [f"- {g}: {why}" for g, why in sorted(res["skipped"].items())]
    return "\n".join(lines) + "\n"


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--run", type=Path, required=True, help="calibration run directory (compare.py)")
    p.add_argument("--oracle-dir", type=Path, default=DEFAULT_ORACLE)
    p.add_argument("--captures-dir", type=Path, default=None, help="default: <oracle-dir>/captures")
    p.add_argument("--out", type=Path, default=None, help="markdown report (default: stdout)")
    p.add_argument("--records", type=Path, default=None, help="also write per-ply records (JSON)")
    p.add_argument("--top", type=int, default=25, help="disagreement patterns to list")
    args = p.parse_args(argv)
    if args.captures_dir is None:
        args.captures_dir = args.oracle_dir / "captures"
    return args


def main(argv=None) -> int:
    args = parse_args(argv)
    res = compare(args)
    text = report(res, args)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    if args.records:
        args.records.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(f"{len(res['records'])} plies compared, {len(res['skipped'])} games skipped", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
