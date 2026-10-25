#!/usr/bin/env python3
"""Pick games for a calibration batch from the public Chess.com API (batch 5, 2026-10-23).

Needs python-chess and a Stockfish binary ($STOCKFISH). Work files go to $BATCH_DIR
(default ~/work/batch5); API responses are cached under api/.

pool:   sample players from public country lists plus titled players, keep those active in the last
        120 days, read their last two monthly archives and keep standard rated games of 30+ plies
        that are not in tests/calibration/games -> pool.jsonl
pick:   stratified random sample (45 per rating band of the players' mean rating, split by time
        class), then a sacrifice-enriched stratum: rapid/blitz games with a move that leaves a piece
        en prise and that Stockfish (depth 14) rates within 30 cp of best -> games_strat.json,
        games_sac.json ([[id, kind], ...] for coachStart) and meta.jsonl. At most 3 games per player.
"""
import json, os, random, re, sys, time, urllib.request, glob, io
from pathlib import Path

W = Path(os.environ.get("BATCH_DIR", Path.home() / "work/batch5"))
API = W / "api"
UA = {"User-Agent": "chess-review-calibration (khhizr7)"}
REPO = Path(__file__).resolve().parents[2]
COUNTRIES = ["US", "IN", "GB", "DE", "FR", "BR", "RU", "PH", "ES", "CA", "TR", "PL", "NL", "AR", "ID", "EG"]
BANDS = [(0, 700), (700, 1000), (1000, 1300), (1300, 1600), (1600, 1900), (1900, 2200), (2200, 4000)]


def get(url, cache=None):
    if cache and (API / cache).exists():
        return json.loads((API / cache).read_text())
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                d = json.loads(r.read())
            break
        except Exception as e:
            if getattr(e, "code", None) == 404:
                d = None
                break
            time.sleep(2 + 3 * attempt)
    else:
        d = None
    if cache:
        (API / cache).write_text(json.dumps(d))
    return d


def band(e):
    for i, (lo, hi) in enumerate(BANDS):
        if lo <= e < hi:
            return i
    return len(BANDS) - 1


def plies(pgn):
    body = re.split(r"\n\s*\n", pgn.strip(), maxsplit=1)[-1]
    body = re.sub(r"\{[^}]*\}", " ", body)
    toks = [t for t in body.split() if not re.match(r"^\d+\.+$|^(1-0|0-1|1/2-1/2|\*)$", t)]
    return len(toks)


def cmd_pool(target_players=420):
    rng = random.Random(2028)
    names = []
    for c in COUNTRIES:
        d = get(f"https://api.chess.com/pub/country/{c}/players", f"country_{c}.json") or {}
        ps = d.get("players", [])
        names += rng.sample(ps, min(60, len(ps)))
    rng.shuffle(names)
    now = time.time()
    per_band = {}
    chosen = []
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(6) as ex:
        list(ex.map(lambda n: get(f"https://api.chess.com/pub/player/{n}/stats", f"stats_{n}.json"), names))
    for n in names:
        st = get(f"https://api.chess.com/pub/player/{n}/stats", f"stats_{n}.json") or {}
        best = None
        for tc in ("chess_rapid", "chess_blitz", "chess_bullet"):
            s = st.get(tc)
            if s and "last" in s and now - s["last"].get("date", 0) < 120 * 86400:
                best = best or (tc, s["last"]["rating"])
        if not best:
            continue
        b = band(best[1])
        if per_band.get(b, 0) >= target_players // len(BANDS) + 10:
            continue
        per_band[b] = per_band.get(b, 0) + 1
        chosen.append(n)
    # Titled players fill the top band, which country samples rarely reach.
    for t in ("FM", "IM", "GM"):
        d = get(f"https://api.chess.com/pub/titled/{t}", f"titled_{t}.json") or {}
        chosen += rng.sample(d.get("players", []), 15)
    print("players per band", sorted(per_band.items()), "total", len(chosen), file=sys.stderr)
    existing = {Path(p).stem for p in glob.glob(str(REPO / "tests/calibration/games/*.pgn"))}
    seen = set()
    with ThreadPoolExecutor(6) as ex:
        archs = list(ex.map(lambda n: get(f"https://api.chess.com/pub/player/{n}/games/archives", f"arch_{n}.json") or {}, chosen))
        urls = [(n, u) for n, a in zip(chosen, archs) for u in a.get("archives", [])[-2:]]
        list(ex.map(lambda nu: get(nu[1], f"games_{nu[0].lower()}_{'_'.join(nu[1].split('/')[-2:])}.json"), urls))
    with open(W / "pool.jsonl", "w") as out:
        for n in chosen:
            arch = get(f"https://api.chess.com/pub/player/{n}/games/archives", f"arch_{n}.json") or {}
            urls = arch.get("archives", [])[-2:]
            for u in urls:
                ym = "_".join(u.split("/")[-2:])
                g = get(u, f"games_{n.lower()}_{ym}.json") or {}
                for x in g.get("games", []):
                    m = re.search(r"/game/(live|daily)/(\d+)", x.get("url", ""))
                    if not m or m.group(2) in existing or m.group(2) in seen:
                        continue
                    if x.get("rules") != "chess" or not x.get("rated") or "pgn" not in x:
                        continue
                    if "[SetUp" in x["pgn"] or plies(x["pgn"]) < 30:
                        continue
                    seen.add(m.group(2))
                    we, be = x["white"]["rating"], x["black"]["rating"]
                    out.write(json.dumps({
                        "id": m.group(2), "kind": m.group(1), "tc": x.get("time_class"),
                        "white": x["white"]["username"], "black": x["black"]["username"],
                        "we": we, "be": be, "band": band((we + be) / 2), "src": n,
                        "plies": plies(x["pgn"]), "archive": u, "pgn": x["pgn"]}) + "\n")
    print("pool games", len(seen), file=sys.stderr)


VAL = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 0}


def sac_candidates(pgn, eng, limit):
    """Plies where the mover leaves a piece (N/B/R/Q) en prise and Stockfish rates the move best or
    near best without the mover being already far ahead: a cheap proxy for Chess.com's Brilliant."""
    import chess, chess.pgn, chess.engine
    game = chess.pgn.read_game(io.StringIO(pgn))
    b = game.board()
    hits = []
    for ply, mv in enumerate(game.mainline_moves(), 1):
        me = b.turn
        cap = b.piece_at(mv.to_square)
        capv = VAL[cap.piece_type] if cap else (1 if b.is_en_passant(mv) else 0)
        nb = b.copy()
        nb.push(mv)
        en_prise = 0
        for sq, p in nb.piece_map().items():
            if p.color != me or VAL[p.piece_type] < 3:
                continue
            atk = nb.attackers(not me, sq)
            if not atk:
                continue
            low = min(VAL[nb.piece_at(a).piece_type] or 99 for a in atk)
            if low < VAL[p.piece_type] or not nb.attackers(me, sq):
                en_prise = max(en_prise, VAL[p.piece_type] - (low if nb.attackers(me, sq) else 0))
        if en_prise - capv >= 2:
            info = eng.analyse(b, limit, multipv=2)
            best = info[0]["pv"][0]
            s_best = info[0]["score"].pov(me).score(mate_score=10000)
            if best == mv:
                s_mv = s_best
            else:
                s_mv = -eng.analyse(nb, limit)["score"].pov(not me).score(mate_score=10000)
            if s_best - s_mv <= 30 and -150 <= s_mv and s_best < 600:
                hits.append(ply)
        b.push(mv)
    return hits


def cmd_pick(n_strat=45, n_sac=150):
    import chess.engine
    rng = random.Random(2029)
    pool = [json.loads(l) for l in open(W / "pool.jsonl")]
    rng.shuffle(pool)
    per_player = {}
    picked, ids = [], set()

    def take(g, why):
        for p in (g["white"].lower(), g["black"].lower()):
            if per_player.get(p, 0) >= 3:
                return False
        for p in (g["white"].lower(), g["black"].lower()):
            per_player[p] = per_player.get(p, 0) + 1
        g["why"] = why
        picked.append(g)
        ids.add(g["id"])
        return True

    tc_quota = {"rapid": 0.5, "blitz": 0.4, "bullet": 0.05, "daily": 0.05}
    for bi in range(len(BANDS)):
        for tc, q in tc_quota.items():
            want = round(n_strat * q)
            for g in pool:
                if want <= 0:
                    break
                if g["band"] == bi and g["tc"] == tc and g["id"] not in ids and take(g, "strat"):
                    want -= 1
    # The stratified list is ready before the slower sacrifice screen, so capture can start at once.
    json.dump([[g["id"], g["kind"]] for g in picked], open(W / "games_strat.json", "w"))
    with open(W / "meta.jsonl", "w") as f:
        for g in picked:
            f.write(json.dumps(g) + "\n")
    print("strat", len(picked), file=sys.stderr, flush=True)
    eng = chess.engine.SimpleEngine.popen_uci(os.environ.get("STOCKFISH", str(Path.home() / "tools/sf18/sf18")))
    eng.configure({"Threads": 6, "Hash": 256})
    lim = chess.engine.Limit(depth=14)
    got = 0
    for g in pool:
        if got >= n_sac:
            break
        if g["id"] in ids or g["tc"] not in ("rapid", "blitz"):
            continue
        hits = sac_candidates(g["pgn"], eng, lim)
        if hits:
            g["sac_plies"] = hits
            if take(g, "sac"):
                got += 1
                print("sac", got, g["id"], hits, file=sys.stderr, flush=True)
                with open(W / "meta.jsonl", "a") as f:
                    f.write(json.dumps(g) + "\n")
    eng.quit()
    json.dump([[g["id"], g["kind"]] for g in picked if g["why"] == "sac"], open(W / "games_sac.json", "w"))
    from collections import Counter
    print(len(picked), Counter((g["why"], g["band"]) for g in picked), Counter(g["tc"] for g in picked), file=sys.stderr)


if __name__ == "__main__":
    {"pool": cmd_pool, "pick": cmd_pick}[sys.argv[1]]()
