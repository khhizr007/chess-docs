#!/usr/bin/env python3
"""Build calibration dataset files from raw review captures.

Each raw capture (one JSON file per game) holds what was read from the
reference app's step-by-step review: one line per ply in the form
``move|node|san|icon|label|eval|arrows``, plus the per-player accuracy and
the classification counts table. The exact PGN comes from the public
Chess.com API monthly archive files (``--api`` may be given several times).

For every game this writes ``<games-dir>/<id>.pgn`` (unmodified) and
``<games-dir>/<id>.labels.json``, after checking that:

* the SAN sequence read from the review matches the PGN ply by ply;
* the labels read per move reproduce the counts table for both players.

A ply whose label was hidden in the review (for example behind a "Skill"
note) is filled from the counts table when that is unambiguous, and marked
``label_source: "counts"``; otherwise it is recorded as ``uncertain:?``.

Python 3 standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import os
import re
import sys

LABELS = ["brilliant", "great", "book", "best", "excellent", "good",
          "inaccuracy", "mistake", "miss", "blunder"]
DESC_TO_LABEL = {
    "brilliant": "brilliant", "great": "great", "great move": "great",
    "book": "book", "best": "best", "excellent": "excellent", "good": "good",
    "inaccuracy": "inaccuracy", "mistake": "mistake", "miss": "miss",
    "blunder": "blunder", "forced": "forced",
}
# Labels the app shows that are not rows of its counts table.
UNCOUNTED = {"forced"}
ICON_TO_LABEL = {
    "brilliant": "brilliant", "great_find": "great", "book": "book",
    "best": "best", "excellent": "excellent", "good": "good",
    "inaccuracy": "inaccuracy", "mistake": "mistake", "incorrect": "miss",
    "blunder": "blunder", "forced": "forced",
}
# Arrow colour the review uses for the suggested best move.
BEST_ARROW = "rgba(159,207,63"


def pgn_sans(pgn: str) -> list[str]:
    body = re.split(r"\n\s*\n", pgn.strip(), maxsplit=1)
    text = body[1] if len(body) > 1 else ""
    text = re.sub(r"\{[^}]*\}", " ", text)
    while re.search(r"\([^()]*\)", text):
        text = re.sub(r"\([^()]*\)", " ", text)
    text = re.sub(r";[^\n]*", " ", text)
    out = []
    for tok in text.split():
        if re.fullmatch(r"\d+\.(\.\.)?", tok) or tok.startswith("$"):
            continue
        if tok in ("1-0", "0-1", "1/2-1/2", "*"):
            continue
        tok = re.sub(r"^\d+\.(\.\.)?", "", tok)
        if tok:
            out.append(tok)
    return out


def norm_san(s: str) -> str:
    s = s.replace("0-0-0", "O-O-O").replace("0-0", "O-O")
    return re.sub(r"[+#!?=]", "", s)


def header(pgn: str, name: str) -> str | None:
    m = re.search(r'^\[%s "([^"]*)"\]' % re.escape(name), pgn, re.M)
    return m.group(1) if m else None


def load_api_pgns(paths: list[str]) -> dict[str, str]:
    by_id = {}
    for p in paths:
        for f in glob.glob(p):
            with open(f, encoding="utf-8") as fh:
                data = json.load(fh)
            for g in data.get("games", []):
                url = g.get("url", "")
                gid = url.rstrip("/").split("/")[-1]
                if gid and g.get("pgn"):
                    by_id[gid] = g["pgn"]
    return by_id


def parse_line(line: str) -> dict:
    parts = line.split("|")
    parts += [""] * (7 - len(parts))
    move, node, san, icon, desc, score, arrows = parts[:7]
    return {"move": int(move), "node": node, "san": san, "icon": icon,
            "desc": desc, "score": score, "arrows": arrows}


def build(raw: dict, pgn: str) -> tuple[dict, list[str]]:
    problems: list[str] = []
    # A capture may hold the reader's output verbatim as a JSON string: "dump": "{\"sum\":...,\"lines\":[...]}".
    if isinstance(raw.get("dump"), str):
        raw.update(json.loads(raw.pop("dump")))
    # Captures may carry the summary as {"sum": {"acc": [w, b], "c": {...}}}.
    summary = raw.get("sum") or {}
    if summary.get("acc"):
        raw.setdefault("white_accuracy", summary["acc"][0])
        raw.setdefault("black_accuracy", summary["acc"][1])
    if summary.get("c"):
        raw.setdefault("counts", summary["c"])
    sans = pgn_sans(pgn)
    lines = sorted((parse_line(x) for x in raw["lines"]), key=lambda r: r["move"])
    if len(lines) != len(sans):
        problems.append(f"ply count: review {len(lines)} vs pgn {len(sans)}")
    plies = []
    for i, san in enumerate(sans):
        r = lines[i] if i < len(lines) else None
        entry = {"ply": i + 1, "san": san, "label": "uncertain:?",
                 "app_best_san": None, "app_best_uci": None, "app_eval": None}
        if r is None:
            problems.append(f"ply {i + 1}: missing from review capture")
            plies.append(entry)
            continue
        if r["move"] != i or r["node"] != f"0-{i}":
            problems.append(f"ply {i + 1}: capture index {r['move']}/{r['node']}")
        if norm_san(r["san"]) != norm_san(san):
            problems.append(f"ply {i + 1}: SAN review {r['san']!r} vs pgn {san!r}")
        label = DESC_TO_LABEL.get(r["desc"].strip().lower())
        icon_label = ICON_TO_LABEL.get(r["icon"].lower())
        if label and icon_label and label != icon_label:
            problems.append(f"ply {i + 1}: label {label} vs icon {r['icon']}")
        if label is None and icon_label is not None:
            label = icon_label
        if label is not None:
            entry["label"] = label
        else:
            entry["hidden"] = r["desc"] or r["icon"] or "empty"
        # The last move shows the game result instead of an evaluation.
        if r["score"] and r["score"] not in ("1-0", "0-1", "1/2-1/2", "½-½"):
            entry["app_eval"] = r["score"]
        if label not in ("best", "book", "brilliant", "great", "forced"):
            for a in filter(None, r["arrows"].split(";")):
                uci, _, colour = a.partition("@")
                if colour.startswith(BEST_ARROW):
                    entry["app_best_uci"] = uci
                    break
        plies.append(entry)

    counts_tbl = raw.get("counts") or {}
    table = {"white": {}, "black": {}}
    for name, pair in counts_tbl.items():
        key = DESC_TO_LABEL.get(name.lower())
        if key is None or pair is None:
            continue
        table["white"][key], table["black"][key] = pair[0], pair[1]

    for side, parity in (("white", 1), ("black", 0)):
        side_plies = [p for p in plies if p["ply"] % 2 == parity]
        have = {k: 0 for k in LABELS}
        unknown = []
        for p in side_plies:
            if p["label"] in have:
                have[p["label"]] += 1
            elif p["label"] in UNCOUNTED:
                pass
            else:
                unknown.append(p)
        if not table[side]:
            continue
        deficit = {k: table[side].get(k, 0) - have[k] for k in LABELS}
        if any(v < 0 for v in deficit.values()):
            problems.append(f"{side}: more labels than counts table {deficit}")
            continue
        short = {k: v for k, v in deficit.items() if v > 0}
        if sum(short.values()) != len(unknown):
            problems.append(f"{side}: {len(unknown)} hidden labels but counts short by {short}")
            continue
        if unknown and len(short) == 1:
            label = next(iter(short))
            for p in unknown:
                p["label"] = label
                p["label_source"] = "counts"
        elif unknown:
            for p in unknown:
                p["label"] = "uncertain:" + "/".join(sorted(short))

    counts = {"white": {}, "black": {}}
    has_uncertain = {"white": False, "black": False}
    for p in plies:
        side = "white" if p["ply"] % 2 == 1 else "black"
        if p["label"] in LABELS:
            counts[side][p["label"]] = counts[side].get(p["label"], 0) + 1
        elif p["label"].startswith("uncertain"):
            has_uncertain[side] = True
    # A side with uncertain plies was already checked against the table above
    # (the hidden plies exactly cover the shortfall).
    if table["white"] and any(table[s].get(k, 0) != counts[s].get(k, 0)
                              for s in ("white", "black") if not has_uncertain[s]
                              for k in LABELS):
        problems.append(f"counts mismatch: table {table} vs labels {counts}")

    out = {
        "game_id": raw["game_id"],
        "source_url": raw.get("url"),
        "collected_at": raw.get("collected_at") or dt.date.today().isoformat(),
        "review_settings": {
            "strength": raw.get("strength"),
            "engine": raw.get("engine"),
            "notes": raw.get("notes"),
        },
        "white": header(pgn, "White"),
        "black": header(pgn, "Black"),
        "white_elo": header(pgn, "WhiteElo"),
        "black_elo": header(pgn, "BlackElo"),
        "time_control": header(pgn, "TimeControl"),
        "result": header(pgn, "Result"),
        "white_accuracy": raw.get("white_accuracy"),
        "black_accuracy": raw.get("black_accuracy"),
        "counts": table if table["white"] else counts,
        "plies": plies,
    }
    return out, problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--raw", required=True, help="directory of raw capture JSON files")
    ap.add_argument("--api", action="append", required=True,
                    help="Chess.com API monthly archive JSON (glob allowed); repeatable")
    ap.add_argument("--games-dir", default="tests/calibration/games")
    ap.add_argument("--only", nargs="*", help="limit to these game ids")
    args = ap.parse_args()

    pgns = load_api_pgns(args.api)
    os.makedirs(args.games_dir, exist_ok=True)
    bad = 0
    for f in sorted(glob.glob(os.path.join(args.raw, "*.json"))):
        with open(f, encoding="utf-8") as fh:
            raw = json.load(fh)
        gid = str(raw["game_id"])
        if args.only and gid not in args.only:
            continue
        pgn = pgns.get(gid)
        if pgn is None:
            print(f"{gid}: no PGN in API files", file=sys.stderr)
            bad += 1
            continue
        out, problems = build(raw, pgn)
        uncertain = sum(1 for p in out["plies"] if p["label"].startswith("uncertain"))
        derived = sum(1 for p in out["plies"] if p.get("label_source") == "counts")
        status = "OK" if not problems else "PROBLEMS"
        print(f"{gid}: {status} plies={len(out['plies'])} derived={derived} uncertain={uncertain}")
        for msg in problems:
            print(f"    {msg}")
        if problems:
            bad += 1
            continue
        with open(os.path.join(args.games_dir, f"{gid}.pgn"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(pgn if pgn.endswith("\n") else pgn + "\n")
        with open(os.path.join(args.games_dir, f"{gid}.labels.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
