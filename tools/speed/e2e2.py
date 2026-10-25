#!/usr/bin/env python3
"""Whole-review timing plus exact output capture.

usage: e2e2.py <label> <bin> <out-dir> <games-file> [body-json]
env: POOL (ENGINE_POOL_SIZE, default 8), PORT (default 8093), REPS (default 1).
Starts <bin> once with an empty analysis cache, reviews each game id of <games-file> one at a time
(REPS times; reps after the first are cache hits, so only rep 1 counts for timing when REPS=1),
writes <out-dir>/<id>.json (the `plies` array and summary) and prints one JSON line per review.
"""
import hashlib, json, os, subprocess, sys, time, urllib.request

label, BIN, OUT, GAMES_FILE = sys.argv[1:5]
BODY = json.loads(sys.argv[5]) if len(sys.argv) > 5 else {}
PORT = int(os.environ.get("PORT", "8093"))
GAMES_DIR = "/mnt/c/Users/khhizr/rea_projects/chess-review-research/tests/calibration/games"
OPENINGS = "/mnt/c/Users/khhizr/rea_projects/chess-review-wt-speed/backend/data/openings"
ids = [l.strip() for l in open(GAMES_FILE) if l.strip() and not l.startswith("#")]
os.makedirs(OUT, exist_ok=True)


def call(method, path, body=None):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}{path}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


env = dict(os.environ, STOCKFISH_PATH=os.path.expanduser("~/tools/sf18/sf18"),
           BIND_ADDR=f"127.0.0.1:{PORT}", ENGINE_POOL_SIZE=os.environ.get("POOL", "8"),
           RUST_LOG="info", OPENINGS_DIR=OPENINGS, ANALYSIS_CACHE_ENTRIES="200000")
env.pop("ANALYSIS_CACHE_FILE", None)
log = open(os.path.join(OUT, f"server-{label}.log"), "w")
srv = subprocess.Popen([BIN], env=env, stdout=log, stderr=subprocess.STDOUT)
try:
    for _ in range(200):
        try:
            call("GET", "/api/health"); break
        except Exception:
            time.sleep(0.2)
    for gid in ids:
        pgn = open(f"{GAMES_DIR}/{gid}.pgn").read()
        t0 = time.perf_counter()
        st = call("POST", "/api/reviews", dict(pgn=pgn, **BODY))
        while st["state"] not in ("completed", "failed", "cancelled"):
            time.sleep(0.05); st = call("GET", f"/api/reviews/{st['id']}")
        wall = time.perf_counter() - t0
        res = call("GET", f"/api/reviews/{st['id']}/result") if st["state"] == "completed" else {}
        digest = None
        if res:
            keep = {"plies": res["plies"], "white": res["white"], "black": res["black"],
                    "key_moments": res["key_moments"], "critical_moments": res["critical_moments"]}
            text = json.dumps(keep, sort_keys=True)
            digest = hashlib.sha256(text.encode()).hexdigest()[:16]
            open(os.path.join(OUT, f"{gid}.json"), "w").write(text)
        print(json.dumps(dict(label=label, game=gid, state=st["state"], error=st.get("error"),
                              plies=res.get("game", {}).get("ply_count"), searches=st["progress"]["total"],
                              wall_s=round(wall, 2), sha=digest)), flush=True)
finally:
    srv.terminate(); srv.wait(10)
