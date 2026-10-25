#!/usr/bin/env python3
"""Oracle check: apply the recovered precision rules to Chess.com's own scores.

Input: `tests/calibration/cc-reviews/<id>.sf.txt`, the compact dump of a Chess.com Game Review
(captured from the review page's /v2/game-review response; see docs/calibration/chesscom-review-protocol.md):

    eng 10 acc 72.7 72.7 cee 1.198.16
    <ply> <played uci> <label> <played score> <best uci|-> <best label|-> <best score|-> [K]

Scores are White-relative: `123@18` (centipawns at depth 18), `M3@40` (White mates in 3),
`-M2@30` (Black mates in 2), `S@` (stalemate). An `eNN` suffix names a non-SF18 engine.
When the played move is the engine's best move, the best columns are `-`.

The script grades every ply with our precision thresholds and mate rules on those scores and
compares the grade with Chess.com's label. Python 3 standard library only.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CC_DIR = REPO / "tests/calibration/cc-reviews"
GAMES_DIR = REPO / "tests/calibration/games"

VALUE_MATE = 32000
PREC = ["best", "excellent", "good", "inaccuracy", "mistake", "blunder"]
OUTCOME_T = [0.10, 0.20, 0.35, 0.65, 0.80, 0.90]


def slope(r: float) -> float:
    return 0.004 * ((r * 0.0685 - 12.0) / 100.0)


def ep(v: int, r: float) -> float:
    e = math.exp(-slope(r) * v)
    return (2.0 / (e + 1.0) - 1.0) * 0.5 + 0.5


def ep_to_cp(p: float, r: float) -> int:
    return int(math.log(1.0 / p - 1.0) / (-slope(r)))


def outcome(v: int, r: float) -> int:
    for i in range(5, -1, -1):
        if v >= ep_to_cp(OUTCOME_T[i], r):
            return i + 1
    return 0


class Score:
    """White-relative score of a position after a move."""

    def __init__(self, text: str):
        body, _, rest = text.partition("@")
        m = re.match(r"(\d*)", rest)
        self.depth = int(m.group(1)) if m and m.group(1) else None
        self.draw = body == "S"
        self.mate_white = self.mate_black = None
        self.cp = 0
        if body.startswith("-M"):
            self.mate_black = int(body[2:])
        elif body.startswith("M"):
            self.mate_white = int(body[1:])
        elif not self.draw:
            self.cp = int(body)

    def value(self, mover_white: bool) -> int:
        """Mover-perspective Value with the reference engine's mate encoding."""
        if self.mate_white is not None or self.mate_black is not None:
            winner_white = self.mate_white is not None
            n = min(self.mate_white if winner_white else self.mate_black, 499)
            if winner_white == mover_white:
                return VALUE_MATE - 2 * n
            return -(VALUE_MATE - (2 * max(n, 1) - 1))
        cp = max(-30999, min(30999, self.cp))
        return cp if mover_white else -cp


def is_mate(v: int) -> bool:
    return abs(v) >= 31000


def mate_moves(v: int) -> int:
    """Signed mate distance in mover moves (positive: mover mates)."""
    if v > 0:
        return (VALUE_MATE - v) // 2
    return -((VALUE_MATE + v + 1) // 2)


def mate_override(played: int, best: int, r: float):
    if is_mate(best):
        md_best = mate_moves(best)
        n_best = abs(md_best)
        if not is_mate(played) or (played > 0) != (best > 0):
            still = outcome(played, r) == 6
            return "good" if (n_best > 2 and still) else "missed_mate"
        n_played = abs(mate_moves(played))
        if played < 1:
            if (n_best > 2 and n_played == 1) or (n_best > 4 and n_played == 2):
                return "inaccuracy"
        else:
            if (md_best == 0 and n_played > 1) or (n_best == 1 and n_played > 3):
                return "missed_faster_mate"
            if (n_best == 1 and n_played > 2) or (n_best == 2 and n_played > 4) or (
                n_best == 3 and n_played > 6
            ):
                return "good"
        return None
    if is_mate(played) and outcome(best, r) == 0:
        n_played = abs(mate_moves(played))
        if n_played < 4:
            return "mistake"
        return "inaccuracy" if best > -1501 else "good"
    return None


def grade(played: int, best: int, played_draw: bool, best_draw: bool, r: float, th):
    """Returns (precision grade, ep lost, mate override or None)."""
    ep_b = 0.5 if best_draw else ep(best, r)
    ep_p = 0.5 if played_draw else ep(played, r)
    lost = max(0.0, ep_b - ep_p)
    if lost <= th[0]:
        g = "excellent"
    elif lost <= th[1]:
        g = "good"
    elif lost <= th[2]:
        g = "inaccuracy"
    elif lost <= th[3]:
        g = "mistake"
    else:
        g = "blunder"
    over = mate_override(played, best, r)
    if over in ("good", "inaccuracy", "mistake"):
        g = over
    return g, lost, over


def load_review(path: Path):
    lines = path.read_text().strip().splitlines()
    head = lines[0].split()
    meta = {"engine_req": int(head[1]), "acc_white": float(head[3]), "acc_black": float(head[4])}
    plies = []
    for ln in lines[1:]:
        t = ln.split()
        plies.append(
            {
                "ply": int(t[0]),
                "uci": t[1],
                "label": t[2],
                "played": Score(t[3]),
                "best_uci": None if t[4] == "-" else t[4],
                "best_label": None if t[5] == "-" else t[5],
                "best": None if t[6] == "-" else Score(t[6]),
                "key": len(t) > 7 and t[7] == "K",
            }
        )
    return meta, plies


def pgn_elos(game_id: str):
    txt = (GAMES_DIR / f"{game_id}.pgn").read_text()
    w = re.search(r'\[WhiteElo "(\d+)"\]', txt)
    b = re.search(r'\[BlackElo "(\d+)"\]', txt)
    return (int(w.group(1)) if w else 0), (int(b.group(1)) if b else 0)


def rating_for(game_id: str, mode: str, offset: int) -> float:
    w, b = pgn_elos(game_id)
    if mode == "max":
        base = max(w, b)
    elif mode == "min":
        base = min(w, b)
    elif mode == "avg":
        base = (w + b) / 2
    else:
        base = float(mode)
    return max(1000, min(2500, base + offset))


def evaluate(ids, mode, offset, th, verbose=False):
    conf = Counter()
    n_prec = agree = 0
    rows = []
    for gid in ids:
        meta, plies = load_review(CC_DIR / f"{gid}.sf.txt")
        r = rating_for(gid, mode, offset)
        for p in plies:
            lab = p["label"]
            mover_white = p["ply"] % 2 == 1
            if p["best"] is None:
                pred = "best"
                lost = 0.0
            else:
                pv = p["played"].value(mover_white)
                bv = p["best"].value(mover_white)
                pred, lost, _ = grade(pv, bv, p["played"].draw, p["best"].draw, r, th)
            conf[(lab, pred)] += 1
            if lab in PREC:
                n_prec += 1
                agree += lab == pred
                if lab != pred:
                    rows.append((gid, p["ply"], p["uci"], lab, pred, round(lost, 4), str(p["played"].cp), p["best"] and p["best"].cp))
    return conf, n_prec, agree, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ids", nargs="*", help="game ids (default: every capture)")
    ap.add_argument("--mode", default="max", help="rating base: max, min, avg or a number")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--scan", action="store_true", help="scan rating offsets")
    ap.add_argument("--mismatches", action="store_true")
    args = ap.parse_args()
    ids = args.ids or sorted(p.name.split(".")[0] for p in CC_DIR.glob("*.sf.txt"))
    th = [0.02, 0.05, 0.10, 0.20]
    if args.scan:
        for mode in ["max", "min", "avg"]:
            for off in range(-300, 701, 100):
                _, n, a, _ = evaluate(ids, mode, off, th)
                print(f"{mode:>4} {off:+5d}: {a}/{n} = {a / max(n, 1):.4f}")
        for fixed in ["1000", "1500", "2000", "2500"]:
            _, n, a, _ = evaluate(ids, fixed, 0, th)
            print(f"fixed {fixed}: {a}/{n} = {a / max(n, 1):.4f}")
        return
    conf, n, a, rows = evaluate(ids, args.mode, args.offset, th)
    print(f"games {len(ids)}  precision-label plies {n}  agree {a} ({a / max(n, 1):.4f})")
    labs = sorted({k[0] for k in conf})
    preds = PREC
    print("label \\ grade " + " ".join(f"{p[:5]:>6}" for p in preds))
    for lab in labs:
        print(f"{lab:>13} " + " ".join(f"{conf[(lab, p)]:>6}" for p in preds))
    if args.mismatches:
        for r in rows:
            print(*r)


if __name__ == "__main__":
    main()
