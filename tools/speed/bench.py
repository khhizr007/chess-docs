#!/usr/bin/env python3
"""Engine-cost bench for the review-speed study.

usage: bench.py <games.json> <config> <out.jsonl> [engine]
Searches every position of each game (as `position startpos moves ...`) with one config,
single thread, Hash 64, and writes one JSON line per search: wall ms, depth, nodes.
"""
import json, os, subprocess, sys, time
DEBUG = os.environ.get("BENCH_DEBUG") == "1"

CONFIGS = {
    # What the review server does today for every position.
    "ours_d18_mpv3_clear": dict(go="depth 18", mpv=3, clear=True),
    "d18_mpv1_clear": dict(go="depth 18", mpv=1, clear=True),
    "d18_mpv2_clear": dict(go="depth 18", mpv=2, clear=True),
    "d18_mpv3_warm": dict(go="depth 18", mpv=3, clear=False),
    "d18_mpv2_warm": dict(go="depth 18", mpv=2, clear=False),
    # chess.com Game Review presets (libcee 4.10.15 get_options_from_game_review_search_settings).
    "cc_standard_n600k_mpv2_clear": dict(go="nodes 600000", mpv=2, clear=True),
    "cc_standard_n600k_mpv2_warm": dict(go="nodes 600000", mpv=2, clear=False),
    # Same, walking the game from the last position back to the first.
    "cc_standard_n600k_mpv2_warm_rev": dict(go="nodes 600000", mpv=2, clear=False, reverse=True),
    "cc_fast_n150k_mpv2_warm": dict(go="nodes 150000", mpv=2, clear=False),
    "cc_fast_n150k_mpv2_warm_rev": dict(go="nodes 150000", mpv=2, clear=False, reverse=True),
    "cc_fast_n150k_mpv2_clear": dict(go="nodes 150000", mpv=2, clear=True),
    "cc_deep_n1600k_mpv2_clear": dict(go="nodes 1600000", mpv=2, clear=True),
    # The coach's null-move threat search: ours (depth 10) vs chess.com's (40,000 nodes).
    "threat_d10_clear": dict(go="depth 10", mpv=1, clear=True, null=True),
    "threat_n40k_clear": dict(go="nodes 40000", mpv=1, clear=True, null=True),
}

class Engine:
    def __init__(self, path):
        self.p = subprocess.Popen([path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
        self.send("uci"); self.wait("uciok")
        self.send("setoption name Threads value 1"); self.send("setoption name Hash value 64")
        self.mpv = None
        self.ready()
    def send(self, s):
        if DEBUG: print(">>", s, file=sys.stderr, flush=True)
        self.p.stdin.write(s + "\n"); self.p.stdin.flush()
    def wait(self, prefix):
        lines = []
        while True:
            raw = self.p.stdout.readline()
            if raw == "":
                raise RuntimeError(f"engine closed stdout (exit {self.p.poll()}) waiting for {prefix}; last {lines[-3:]}")
            l = raw.strip(); lines.append(l)
            if l.startswith(prefix): return lines
    def ready(self): self.send("isready"); self.wait("readyok")
    def fen(self, moves):
        self.send("position startpos moves " + " ".join(moves) if moves else "position startpos")
        self.send("d")
        for l in self.wait("Checkers"):
            if l.startswith("Fen:"): fen = l[5:].strip()
        return fen, l.split(":", 1)[1].strip() != ""

def null_fen(fen):
    f = fen.split()
    f[1] = "b" if f[1] == "w" else "w"; f[3] = "-"
    return " ".join(f)

def main():
    games = json.load(open(sys.argv[1])); cfg = CONFIGS[sys.argv[2]]
    eng = Engine(sys.argv[4] if len(sys.argv) > 4 else os.path.expanduser("~/tools/sf18/sf18"))
    out = open(sys.argv[3], "w")
    if cfg["mpv"] != eng.mpv: eng.send(f"setoption name MultiPV value {cfg['mpv']}"); eng.mpv = cfg["mpv"]
    for g in games:
        eng.send("ucinewgame"); eng.ready()
        plies = range(len(g["moves"]) + 1)
        for ply in (reversed(plies) if cfg.get("reverse") else plies):
            fen, in_check = eng.fen(g["moves"][:ply])
            if cfg.get("null"):
                if in_check: continue
                fen = null_fen(fen)
            t0 = time.perf_counter()
            if cfg["clear"]:
                eng.send("ucinewgame"); eng.send("setoption name Clear Hash"); eng.ready()
            eng.send("position fen " + fen); eng.send("go " + cfg["go"])
            depth = seldepth = nodes = score = None; nlines = 0
            for l in eng.wait("bestmove"):
                if l.startswith("info") and " pv " in l and "bound" not in l:
                    t = l.split()
                    if "depth" in t: depth = int(t[t.index("depth") + 1])
                    if "seldepth" in t: seldepth = int(t[t.index("seldepth") + 1])
                    if "nodes" in t: nodes = int(t[t.index("nodes") + 1])
                    mpv = int(t[t.index("multipv") + 1]) if "multipv" in t else 1
                    if mpv == 1 and "score" in t:
                        k = t.index("score"); v = int(t[k + 2])
                        if fen.split()[1] == "b": v = -v
                        score = ("cp" if t[k + 1] == "cp" else "mate") + str(v)
            ms = (time.perf_counter() - t0) * 1000
            if l.split()[1] == "(none)": continue
            out.write(json.dumps(dict(game=g["id"], ply=ply, ms=round(ms, 1), depth=depth, seldepth=seldepth, nodes=nodes, score=score)) + "\n")
            out.flush()
    out.close(); eng.send("quit")

main()
