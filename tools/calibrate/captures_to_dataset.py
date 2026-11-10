#!/usr/bin/env python3
"""Turn captured Game Review frames into calibration dataset files (batch 5, 2026-10-23).

Needs python-chess. Work files are in $BATCH_DIR (default ~/work/batch5), next to sample_games.py's
meta.jsonl (which holds each game's PGN).

ingest <tool-result files...>   coachPullGz() / coachPull() output -> captures/raw/<id>.json
build                           raw + meta.jsonl -> out/games/<id>.{pgn,labels.json} and
                                out/cc-reviews/<id>.sf.txt

A game is rejected unless every score comes from engine 13 (Stockfish 18), every played move
matches the PGN, every best move is legal and the per-ply labels reproduce the review's tallies.
labels.json gets a `batch5` block with numbers only: selection stratum, Chess.com's per-side game
rating ("effective_rating"), phase accuracies, the report-card stats and the opening's ECO and name.
The raw frames hold Chess.com text: never commit them.
"""
import base64, gzip, io, json, os, re, struct, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools/calibrate"))
import coach_oracle as co  # noqa: E402
import chess, chess.pgn  # noqa: E402

W = Path(os.environ.get("BATCH_DIR", Path.home() / "work/batch5"))
RAW = W / "captures/raw"
OUT = W / "out"
LABELS = ["brilliant", "great", "book", "best", "excellent", "good", "inaccuracy", "mistake", "miss", "blunder"]
PHASES = {1: "opening", 2: "middlegame", 3: "endgame"}


def unwrap(text):
    if text.lstrip().startswith("["):
        text = "".join(x.get("text", "") for x in json.loads(text))
    if text.startswith('"'):
        text = json.JSONDecoder().raw_decode(text)[0]
    if text.startswith("GZ1:"):
        text = gzip.decompress(base64.b64decode(text[4:text.index("|")])).decode("utf-8")
    return json.JSONDecoder().raw_decode(text.lstrip())[0]


def cmd_ingest(files):
    RAW.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in files:
        for cap in unwrap(Path(f).read_text(encoding="utf-8"))["caps"]:
            if cap and cap.get("ok") and re.fullmatch(r"\d+", str(cap.get("id"))):
                (RAW / f"{cap['id']}.json").write_text(json.dumps(cap))
                n += 1
    print(f"ingested {n}; raw total {len(list(RAW.glob('*.json')))}")


def f32(b):
    return round(struct.unpack("<f", b)[0], 1) if isinstance(b, bytes) else None


def highlights(cap):
    """Accuracy, tallies, report card and opening from the GameReview (numbers and names only)."""
    for s in cap["sockets"]:
        for fr in sorted((base64.b64decode(x["b64"]) for x in s["in"] if "b64" in x), key=len, reverse=True):
            gr = co.find_game_review(fr)
            if gr is None:
                continue
            h = co.by_field(co.one(gr, 2, b""))
            acc = co.by_field(co.one(h, 3, b""))
            tal = co.by_field(co.one(h, 4, b""))
            rc = co.by_field(co.one(h, 5, b""))
            op = co.by_field(co.one(gr, 6, b""))
            out = {"accuracy": {"white": f32(co.one(acc, 1)), "black": f32(co.one(acc, 2))}, "tallies": {}, "report": {}}
            for side, k in (("white", 1), ("black", 2)):
                t = Counter()
                for x in tal.get(k, []):
                    d = co.by_field(x)
                    t[co.CLASSIFICATIONS.get(co.one(d, 1), str(co.one(d, 1)))] += co.one(d, 2, 0)
                out["tallies"][side] = dict(t)
                card = co.by_field(co.one(rc, k, b""))
                phases = {}
                for x in card.get(1, []):
                    d = co.by_field(x)
                    phases[PHASES.get(co.one(d, 2), co.one(d, 2))] = {
                        "accuracy": f32(co.one(d, 3)), "glyph": co.CLASSIFICATIONS.get(co.one(d, 1))}
                cats = []
                for x in card.get(2, []):
                    d = co.by_field(x)
                    cats.append({"stat": co.one(d, 1), "performance": co.CLASSIFICATIONS.get(co.one(d, 2)),
                                 "new_rating": co.int32(co.one(d, 3, 0)), "change": co.int32(co.one(d, 4, 0))})
                out["report"][side] = {"effective_rating": co.int32(co.one(card, 4, 0)), "phases": phases, "stats": cats}
            out["opening"] = {"name": co.one(op, 1, b"").decode(), "eco": co.one(op, 3, b"").decode()}
            return out
    return None


def score_txt(s):
    if not s:
        return "-"
    d = s.get("depth") or 0
    if s.get("stalemate"):
        t = "S@"
    elif "mate" in s:
        t = ("M" if s["mate"] > 0 else "-M") + f"{abs(s['mate'])}@{d}"
    else:
        t = f"{s.get('cp', 0)}@{d}"
    return t + ("" if s.get("engine") == 13 else f"e{s.get('engine')}")


def app_eval(s):
    if "mate" in s:
        return ("M" if s["mate"] > 0 else "-M") + str(abs(s["mate"]))
    if s.get("stalemate"):
        return "0.00"
    return f"{s.get('cp', 0) / 100:+.2f}"


def cmd_build():
    meta = {json.loads(l)["id"]: json.loads(l) for l in open(W / "meta.jsonl")}
    (OUT / "games").mkdir(parents=True, exist_ok=True)
    (OUT / "cc-reviews").mkdir(parents=True, exist_ok=True)
    ok, bad, labels = [], [], Counter()
    for rf in sorted(RAW.glob("*.json")):
        gid = rf.stem
        m = meta.get(gid)
        try:
            cap = json.loads(rf.read_text())
            rev = co.decode_capture(cap)
            hl = highlights(cap)
            if set(rev["score_engines"]) != {"13"}:
                raise ValueError(f"score engines {rev['score_engines']} (review engine not Stockfish?)")
            game = chess.pgn.read_game(io.StringIO(m["pgn"]))
            moves = list(game.mainline_moves())
            plies = rev["plies"]
            if len(plies) != len(moves):
                raise ValueError(f"{len(plies)} review plies vs {len(moves)} PGN plies")
            b = game.board()
            sf = [f"eng 10 acc {hl['accuracy']['white']} {hl['accuracy']['black']} cee {rev['cee_version']}"]
            out_plies, counts = [], {"white": Counter(), "black": Counter()}
            for p, mv in zip(plies, moves):
                pl, best = p["played"], p["best"]
                if pl["uci"] != mv.uci():
                    raise ValueError(f"ply {p['ply']}: review {pl['uci']} vs PGN {mv.uci()}")
                bmv = chess.Move.from_uci(best["uci"]) if best else None
                if bmv and bmv not in b.legal_moves:
                    raise ValueError(f"ply {p['ply']}: illegal best {best['uci']}")
                lab = pl["classification"]
                side = "white" if b.turn else "black"
                if lab in LABELS:
                    counts[side][lab] += 1
                labels[lab] += 1
                sf.append(" ".join([str(p["ply"]), pl["uci"], lab, score_txt(pl.get("score")),
                                    best["uci"] if best else "-", best["classification"] if best else "-",
                                    score_txt(best.get("score")) if best else "-"] + (["K"] if p["key_moment"] else [])))
                out_plies.append({"ply": p["ply"], "san": b.san(mv), "label": lab,
                                  "app_best_san": b.san(bmv) if bmv else None,
                                  "app_best_uci": best["uci"] if best else None,
                                  "app_eval": app_eval(pl["score"]) if pl.get("score") and p["ply"] < len(moves) else None,
                                  "label_source": "chesscom-capture"})
                b.push(mv)
            for side in counts:
                tal = {k: v for k, v in hl["tallies"][side].items() if k in LABELS}
                if {k: v for k, v in counts[side].items() if v} != {k: v for k, v in tal.items() if v}:
                    raise ValueError(f"{side} per-ply labels {dict(counts[side])} != tallies {tal}")
            h = game.headers
            doc = {
                "game_id": gid, "source_url": f"https://www.chess.com/game/{m['kind']}/{gid}",
                "collected_at": cap["captured_at"][:10],
                "review_settings": {"strength": "Fast (18)", "engine": "stockfish16 nnue",
                                    "notes": f"batch 5 ({m['why']}); labels read from the /v2/game-review response (cc-reviews/{gid}.sf.txt)"},
                "white": h.get("White"), "black": h.get("Black"),
                "white_elo": h.get("WhiteElo"), "black_elo": h.get("BlackElo"),
                "time_control": h.get("TimeControl"), "result": h.get("Result"),
                "white_accuracy": hl["accuracy"]["white"], "black_accuracy": hl["accuracy"]["black"],
                "counts": {s: {k: counts[s].get(k, 0) for k in LABELS} for s in counts},
                "batch5": {"selection": m["why"], "time_class": m["tc"], "band": m["band"],
                           "sac_plies": m.get("sac_plies"),
                           "effective_rating": {s: hl["report"][s]["effective_rating"] for s in ("white", "black")},
                           "phase_accuracy": {s: hl["report"][s]["phases"] for s in ("white", "black")},
                           "stats": {s: hl["report"][s]["stats"] for s in ("white", "black")},
                           "eco": hl["opening"]["eco"], "opening": hl["opening"]["name"],
                           "tricky_plies": [p["ply"] for p in out_plies if p["label"] == "tricky"]},
                "plies": out_plies,
            }
            (OUT / "games" / f"{gid}.pgn").write_text(m["pgn"])
            (OUT / "games" / f"{gid}.labels.json").write_text(json.dumps(doc, indent=2) + "\n")
            (OUT / "cc-reviews" / f"{gid}.sf.txt").write_text("\n".join(sf) + "\n")
            ok.append(gid)
        except Exception as e:  # noqa: BLE001
            bad.append((gid, str(e)[:160]))
    print(f"built {len(ok)}, failed {len(bad)}")
    for g, e in bad:
        print("  FAIL", g, e)
    print("labels", dict(labels.most_common()))


if __name__ == "__main__":
    if sys.argv[1] == "ingest":
        cmd_ingest(sys.argv[2:])
    else:
        cmd_build()
