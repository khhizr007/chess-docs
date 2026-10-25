#!/usr/bin/env python3
"""Prototype: emulate Chess.com Game Review's search procedure and compare with its exact data.

Chess.com's /v2/game-review response (see docs/calibration/chesscom-review-protocol.md) shows that
the "Stockfish 16" review is scored by Stockfish 18 and that scores form a tree:

- a game position that lies on an earlier search's principal variation inherits that search's
  score, one ply shallower per step (404@20, 404@19, 404@18 ...);
- only when the game leaves the PV is the new position searched, with a budget (fresh searches
  reach depth 12-23, mean 17.4, so the limit is nodes or time, not depth).

This script reproduces that with any UCI engine and measures, against
`tests/calibration/cc-reviews/<id>.sf.txt`:
- how often our best move equals Chess.com's;
- the score error of played and best moves;
- precision-label agreement when our recovered precision rules are applied to the emulated scores.

Positions come from a cached review JSON (`tests/calibration/runs/<run>/<id>.json`, fields
`fen_before` / `fen_after`), so no chess library is needed. Standard library only.

    python3 tools/calibrate/emulate_search.py --engine ~/tools/sf18/sf18 --mode tree --nodes 1500000
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import os
import statistics
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CC = REPO / "tests/calibration/cc-reviews"
RUNS = REPO / "tests/calibration/runs"
PREC = ["excellent", "good", "inaccuracy", "mistake", "blunder"]


class Engine:
    def __init__(self, path: str, threads: int = 1, hash_mb: int = 64):
        self.p = subprocess.Popen([path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
        self.send("uci")
        self.wait("uciok")
        self.send(f"setoption name Threads value {threads}")
        self.send(f"setoption name Hash value {hash_mb}")
        self.send("isready")
        self.wait("readyok")

    def send(self, s: str):
        self.p.stdin.write(s + "\n")
        self.p.stdin.flush()

    def wait(self, token: str):
        lines = []
        while True:
            ln = self.p.stdout.readline()
            if not ln:
                raise RuntimeError("engine died")
            lines.append(ln.rstrip("\n"))
            if ln.startswith(token):
                return lines

    def search(self, fen: str, limit: str, fresh: bool = True):
        if fresh:
            self.send("ucinewgame")
            self.send("isready")
            self.wait("readyok")
        self.send(f"position fen {fen}")
        self.send(f"go {limit}")
        lines = self.wait("bestmove")
        info = None
        for ln in lines:
            t = ln.split()
            if t[:1] != ["info"] or "pv" not in t or "score" not in t or "lowerbound" in t or "upperbound" in t:
                continue
            if "multipv" in t and t[t.index("multipv") + 1] != "1":
                continue
            info = ln
        t = info.split()
        depth = int(t[t.index("depth") + 1])
        si = t.index("score")
        kind, val = t[si + 1], int(t[si + 2])
        pv = t[t.index("pv") + 1 :]
        stm_white = fen.split()[1] == "w"
        if kind == "cp":
            score = ("cp", val if stm_white else -val)
        else:  # mate relative to side to move
            winner_white = (val > 0) == stm_white
            score = ("mw" if winner_white else "mb", abs(val))
        return {"score": score, "depth": depth, "pv": pv}

    def close(self):
        try:
            self.send("quit")
        except Exception:
            pass


def parse_cc_score(t: str):
    body = t.split("@")[0]
    if body == "S":
        return ("cp", 0)
    if body.startswith("-M"):
        return ("mb", int(body[2:]))
    if body.startswith("M"):
        return ("mw", int(body[1:]))
    return ("cp", int(body))


def mover_value(score, mover_white: bool) -> int:
    kind, v = score
    if kind == "cp":
        cp = max(-30999, min(30999, v))
        return cp if mover_white else -cp
    winner_white = kind == "mw"
    n = min(v, 499)
    if winner_white == mover_white:
        return 32000 - 2 * n
    return -(32000 - (2 * max(n, 1) - 1))


def ep(v: int, r: float) -> float:
    k = 0.004 * ((r * 0.0685 - 12.0) / 100.0)
    return 1.0 / (1.0 + math.exp(-k * v))


def grade(best_v: int, played_v: int, r: float) -> str:
    lost = max(0.0, ep(best_v, r) - ep(played_v, r))
    for lab, t in zip(PREC, [0.02, 0.05, 0.10, 0.20]):
        if lost <= t:
            return lab
    return "blunder"


def load_game(gid: str):
    cc = [l.split() for l in (CC / f"{gid}.sf.txt").read_text().strip().splitlines()[1:]]
    src = None
    for run in ("b2-default", "holdout-b2", "book-anywhere", "holdout-book-anywhere"):
        f = RUNS / run / f"{gid}.json"
        if f.exists():
            src = json.loads(f.read_text())["result"]
            break
    if src is None:
        return None
    plies = src["plies"]
    elos = (src["game"].get("white_elo") or 0, src["game"].get("black_elo") or 0)
    return cc, plies, elos


def emulate(gid: str, engine: str, mode: str, limit: str, open_limit: str | None, open_plies: int):
    g = load_game(gid)
    if g is None:
        return None
    cc, plies, elos = g
    eng = Engine(engine)
    out = []
    try:
        node = None  # node for the position before ply i: dict(score, depth, pv)
        for i, (p, c) in enumerate(zip(plies, cc)):
            lim = open_limit if (open_limit and i < open_plies) else limit
            fen_b, fen_a = p["fen_before"], p["fen_after"]
            if mode == "fixed" or node is None or not node["pv"]:
                node = eng.search(fen_b, lim)
            best_uci = node["pv"][0]
            best = {"score": node["score"], "depth": node["depth"] - 1}
            played_uci = p["uci"]
            if played_uci == best_uci:
                child = {"score": node["score"], "depth": node["depth"] - 1, "pv": node["pv"][1:]}
            else:
                terminal = p["flags"]["checkmate"] or p["flags"]["stalemate"]
                if terminal:
                    sc = ("mw" if p["mover"] == "white" else "mb", 0) if p["flags"]["checkmate"] else ("cp", 0)
                    child = {"score": sc, "depth": 0, "pv": []}
                else:
                    lim2 = open_limit if (open_limit and i + 1 < open_plies) else limit
                    child = eng.search(fen_a, lim2)
            out.append({"ply": i + 1, "played": played_uci, "best": best_uci, "best_score": best["score"],
                        "played_score": child["score"], "pd": child["depth"], "bd": best["depth"]})
            node = child if mode == "tree" else None
            if mode == "tree" and (p["flags"]["checkmate"] or p["flags"]["stalemate"]):
                node = None
    finally:
        eng.close()
    return gid, out, cc, elos


def evaluate(results, offset: int, rmax: int):
    n = same_best = 0
    dp, db = [], []
    lab_n = lab_ok = 0
    for gid, out, cc, elos in results:
        r = max(1000, min(rmax, max(elos) + offset))
        for e, c in zip(out, cc):
            n += 1
            cc_best = c[1] if c[4] == "-" else c[4]
            same_best += e["best"] == cc_best
            ccp = parse_cc_score(c[3])
            ccb = parse_cc_score(c[6]) if c[6] != "-" else ccp
            if ccp[0] == "cp" and e["played_score"][0] == "cp":
                dp.append(abs(ccp[1] - e["played_score"][1]))
            if ccb[0] == "cp" and e["best_score"][0] == "cp":
                db.append(abs(ccb[1] - e["best_score"][1]))
            lab = {"forced": "best"}.get(c[2], c[2])
            if lab not in ["best"] + PREC:
                continue
            mover_white = e["ply"] % 2 == 1
            if e["played"] == e["best"]:
                pred = "best"
            else:
                pv = mover_value(e["played_score"], mover_white)
                bv = mover_value(e["best_score"], mover_white)
                pred = grade(bv, pv, r)
            # the material rules (blunder softening / losing hardening) are not modelled here
            if lab == "mistake" and pred == "blunder":
                continue
            lab_n += 1
            lab_ok += pred == lab
    q = lambda a, x: sorted(a)[int(x * (len(a) - 1))] if a else None
    return {
        "plies": n,
        "same_best": round(same_best / n, 4),
        "played_cp_err_med": statistics.median(dp) if dp else None,
        "played_cp_err_p90": q(dp, 0.9),
        "best_cp_err_med": statistics.median(db) if db else None,
        "prec_label_agree": round(lab_ok / max(lab_n, 1), 4),
        "prec_label_n": lab_n,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", required=True)
    ap.add_argument("--mode", choices=["tree", "fixed"], default="tree")
    ap.add_argument("--nodes", type=int, default=0)
    ap.add_argument("--depth", type=int, default=0)
    ap.add_argument("--open-nodes", type=int, default=0, help="budget for the first --open-plies positions")
    ap.add_argument("--open-plies", type=int, default=0)
    ap.add_argument("--games", default="", help="file with ids, or comma list (default: every capture)")
    ap.add_argument("--jobs", type=int, default=14)
    ap.add_argument("--save", default="", help="write per-ply emulation JSON here")
    args = ap.parse_args()
    limit = f"nodes {args.nodes}" if args.nodes else f"depth {args.depth or 18}"
    open_limit = f"nodes {args.open_nodes}" if args.open_nodes else None
    if args.games and os.path.exists(args.games):
        ids = [l.strip() for l in open(args.games) if l.strip() and not l.startswith("#")]
    elif args.games:
        ids = args.games.split(",")
    else:
        ids = sorted(p.name.split(".")[0] for p in CC.glob("*.sf.txt"))
    with ProcessPoolExecutor(args.jobs) as ex:
        results = [r for r in ex.map(emulate, ids, [args.engine] * len(ids), [args.mode] * len(ids),
                                     [limit] * len(ids), [open_limit] * len(ids), [args.open_plies] * len(ids)) if r]
    if args.save:
        Path(args.save).write_text(json.dumps({gid: out for gid, out, _, _ in results}))
    print(f"engine={os.path.basename(args.engine)} mode={args.mode} limit={limit} open={open_limit}/{args.open_plies} games={len(results)}")
    for off, rmax in [(0, 2500), (200, 2500), (150, 3200)]:
        print(f"  rating max+{off} clamp {rmax}:", evaluate(results, off, rmax))


if __name__ == "__main__":
    main()
