#!/usr/bin/env python3
"""End-to-end review timing against this checkout's review-server.

usage: e2e.py <variant>...   (variants below). Starts the server on 127.0.0.1:8091 per variant,
reviews each bench game once (fresh server = empty analysis cache) and prints wall time.
"""
import json, os, subprocess, sys, time, urllib.request

BIN = os.path.expanduser(os.environ.get("BIN", "~/cargo-target/speed/release/review-server"))
GAMES = os.environ.get("GAMES_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tests/calibration/games"))
IDS = [g["id"] for g in json.load(open(os.environ.get("BENCH_GAMES", "bench-games.json")))][: int(os.environ.get("NGAMES", "4"))]
PORT = 8091
VARIANTS = {
    "default_pool4": ({}, {}),
    "mpv2_pool4": ({}, {"multipv": 2}),
    "mpv1_pool4": ({}, {"multipv": 1}),
    "nothreat_pool4": ({}, {"config": {"coach": {"threat_search_depth": 0}}}),
    "default_pool8": ({"ENGINE_POOL_SIZE": "8"}, {}),
    "default_pool4_threads2": ({"ENGINE_THREADS": "2"}, {}),
}

def call(method, path, body=None):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}{path}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def run(variant):
    env_extra, body_extra = VARIANTS[variant]
    env = dict(os.environ, STOCKFISH_PATH=os.path.expanduser(os.environ.get("SF", "~/tools/sf18/sf18")), BIND_ADDR=f"127.0.0.1:{PORT}",
               ENGINE_POOL_SIZE="4", RUST_LOG="info", OPENINGS_DIR=os.path.expanduser(os.environ.get("OPENINGS_DIR", "data/openings")))
    env.update(env_extra)
    log = open(f"e2e-{variant}.log", "w")
    srv = subprocess.Popen([BIN], env=env, stdout=log, stderr=subprocess.STDOUT)
    try:
        for _ in range(100):
            try: call("GET", "/api/health"); break
            except Exception: time.sleep(0.2)
        for gid in IDS:
            pgn = open(f"{GAMES}/{gid}.pgn").read()
            t0 = time.perf_counter()
            st = call("POST", "/api/reviews", dict(pgn=pgn, **body_extra))
            while st["state"] not in ("completed", "failed", "cancelled"):
                time.sleep(0.1); st = call("GET", f"/api/reviews/{st['id']}")
            wall = time.perf_counter() - t0
            res = call("GET", f"/api/reviews/{st['id']}/result") if st["state"] == "completed" else {}
            plies = res.get("game", {}).get("ply_count")
            import hashlib
            digest = hashlib.sha256(json.dumps(res.get("plies"), sort_keys=True).encode()).hexdigest()[:12] if res else None
            print(json.dumps(dict(variant=variant, bin=os.path.basename(os.path.dirname(os.path.dirname(BIN))), game=gid, state=st["state"], error=st.get("error"), plies=plies, searches=st["progress"]["total"], wall_s=round(wall, 2), plies_sha=digest)), flush=True)
    finally:
        srv.terminate(); srv.wait(5)

for v in sys.argv[1:]:
    run(v)
