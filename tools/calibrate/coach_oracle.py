#!/usr/bin/env python3
"""Phase 0 of the coach: turn captured Chess.com Game Review coach speech into event labels.

Two steps, both on local files that must never enter the repository (they hold Chess.com text):

1. ``decode``: the raw `/v2/game-review` WebSocket frames captured from the review page
   (`<captures>/raw/<id>.json`, see docs/calibration/coach-log.md for the capture procedure) are
   decoded into one record per ply: the played move, its classification and score, and for the
   played move and the best alternative the speech (sentences of fragments with their arrows and
   squares), the show-moves buttons and the board markings. Output: `<captures>/<id>.coach.json`.
2. ``match``: every sentence is mapped back to the key of the coach text asset it came from
   (`[Circumstance-[Child-]]Tag[Piece]-Style-N`), using the locally decoded asset as an oracle.
   Composed sentences (a circumstance prefix plus an `InPlace<Tag><Piece>` verb phrase) are matched
   by their verb phrase. Output: `<captures>/<id>.keys.json` with, per ply, the matched keys and
   the parsed (circumstance chain, tag, piece) of each sentence, and the main event.

The `.keys.json` files hold key names and tag names only, never sentences, so the comparison
(`coach_compare.py`) never touches Chess.com text.

Python 3 standard library only. Typical use (WSL):

    python3 tools/calibrate/coach_oracle.py ingest pulled.json   # coach_capture.js output
    python3 tools/calibrate/coach_oracle.py decode
    python3 tools/calibrate/coach_oracle.py match --report

Paths default to `~/work/chesscom/oracle` (asset `coach_en_us.raw`, tag list `tag_names.txt`,
captures in `captures/`); override with --oracle-dir / --captures-dir.
"""

from __future__ import annotations

import argparse
import base64
import gzip
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_ORACLE = Path(os.path.expanduser("~/work/chesscom/oracle"))

# --------------------------------------------------------------------------- protobuf wire format


def _varint(b: bytes, i: int) -> tuple[int, int]:
    r = s = 0
    while True:
        x = b[i]
        i += 1
        r |= (x & 0x7F) << s
        s += 7
        if x < 0x80:
            return r, i


def fields(b: bytes) -> list[tuple[int, int, object]]:
    """Top-level (field, wire type, value) triples of a protobuf message."""
    i, out = 0, []
    while i < len(b):
        key, i = _varint(b, i)
        f, wt = key >> 3, key & 7
        if wt == 0:
            v, i = _varint(b, i)
        elif wt == 1:
            v, i = b[i : i + 8], i + 8
        elif wt == 5:
            v, i = b[i : i + 4], i + 4
        elif wt == 2:
            n, i = _varint(b, i)
            v, i = b[i : i + n], i + n
        else:
            raise ValueError(f"unsupported wire type {wt}")
        if i > len(b):
            raise ValueError("truncated message")
        out.append((f, wt, v))
    return out


def by_field(b: bytes) -> dict[int, list]:
    d: dict[int, list] = defaultdict(list)
    for f, _, v in fields(b):
        d[f].append(v)
    return d


def one(d: dict, f: int, default=None):
    v = d.get(f)
    return v[-1] if v else default


def zigzag(n: int) -> int:
    return (n >> 1) ^ -(n & 1)


def int32(n: int) -> int:
    return n - (1 << 64) if n >= 1 << 63 else n


# --------------------------------------------------------------------------- GameReview schema
# Field numbers from the client's explanation_engine.v1 / chess.v1 / engine.v1 schemas
# (docs/calibration/chesscom-review-protocol.md, docs/coach-analysis.md §3.2).

CLASSIFICATIONS = {
    1: "book", 2: "brilliant", 3: "great", 4: "best", 5: "excellent", 6: "good",
    7: "inaccuracy", 8: "mistake", 9: "blunder", 10: "miss", 11: "forced", 20: "tricky",
}
EMOTIONS = {0: None, 1: "idle", 2: "surprised", 3: "happy", 4: "impressed", 5: "shocked",
            6: "thinking", 7: "concerned", 8: "sad"}
COLOURS = {1: "red", 2: "blue", 3: "green", 4: "orange"}
PROMO = {1: "n", 2: "b", 3: "r", 4: "q"}


def square(n: int) -> str | None:
    if not 1 <= n <= 64:
        return None
    n -= 1
    return "abcdefgh"[n % 8] + str(n // 8 + 1)


def chess_move(b: bytes) -> str:
    d = by_field(b)
    uci = (square(one(d, 1, 0)) or "?") + (square(one(d, 2, 0)) or "?")
    if one(d, 3):
        uci += PROMO.get(one(d, 3), "?")
    return uci


def engine_score(b: bytes) -> dict:
    d = by_field(b)
    out = {"depth": one(d, 2), "engine": one(d, 3)}
    s = one(d, 1)
    if s is not None:
        sd = by_field(s)
        if 1 in sd:
            out["cp"] = zigzag(one(sd, 1))
        elif 2 in sd:
            out["mate"] = int32(one(sd, 2))
        elif 3 in sd:
            out["mate"] = -int32(one(sd, 3))
        elif 4 in sd:
            out["stalemate"] = True
        else:
            out["cp"] = 0
    return out


def arrows_and_squares(b: bytes) -> dict:
    d = by_field(b)
    arrows = []
    for a in d.get(1, []):
        ad = by_field(a)
        arrows.append([square(one(ad, 1, 0)), square(one(ad, 2, 0))])
    return {"arrows": arrows, "squares": [square(s) for s in _packed(d.get(2, []))]}


def _packed(vals: list) -> list[int]:
    out = []
    for v in vals:
        if isinstance(v, int):
            out.append(v)
        else:  # packed repeated enum
            i = 0
            while i < len(v):
                x, i = _varint(v, i)
                out.append(x)
    return out


def speech(b: bytes) -> list[list[dict]]:
    sentences = []
    for s in by_field(b).get(1, []):
        frags = []
        for fr in by_field(s).get(1, []):
            fd = by_field(fr)
            frag = {"text": one(fd, 1, b"").decode("utf-8")}
            if one(fd, 2) is not None:
                frag.update(arrows_and_squares(one(fd, 2)))
            frags.append(frag)
        sentences.append(frags)
    return sentences


def show_moves(b: bytes) -> dict:
    d = by_field(b)
    return {
        "moves": [chess_move(m) for m in d.get(1, [])],
        "show": one(d, 2, b"").decode("utf-8"),
        "hide": one(d, 3, b"").decode("utf-8"),
    }


def board_markings(b: bytes) -> dict:
    d = by_field(b)
    arrows, squares = [], []
    for a in d.get(1, []):
        ad = by_field(a)
        ar = by_field(one(ad, 1, b""))
        arrows.append([square(one(ar, 1, 0)), square(one(ar, 2, 0)), COLOURS.get(one(ad, 2))])
    for s in d.get(2, []):
        sd = by_field(s)
        squares.append([square(one(sd, 1, 0)), COLOURS.get(one(sd, 2))])
    return {"arrows": arrows, "squares": squares}


def review_move(b: bytes) -> dict:
    d = by_field(b)
    out = {
        "uci": chess_move(one(d, 1, b"")),
        "classification": CLASSIFICATIONS.get(one(d, 3), one(d, 3)),
    }
    if one(d, 4) is not None:
        out["score"] = engine_score(one(d, 4))
    out["speech"] = speech(one(d, 5, b""))
    out["buttons"] = [show_moves(x) for x in d.get(6, [])]
    out["markings"] = board_markings(one(d, 7, b""))
    return out


def played_move(b: bytes, depth: int = 0) -> dict:
    d = by_field(b)
    out = {
        "key_moment": bool(one(d, 1, 0)),
        "played": review_move(one(d, 2, b"")),
        "best": review_move(one(d, 3)) if one(d, 3) is not None else None,
        "colour": {1: "white", 2: "black"}.get(one(d, 4)),
        "emotion": EMOTIONS.get(one(d, 5, 0), one(d, 5)),
    }
    if depth == 0:
        out["explain_line"] = [played_move(x, 1) for x in d.get(7, [])]
    return out


def find_game_review(frame: bytes):
    """The GameReview inside a GameReviewResponse frame: the message whose field 3 (Review) holds
    the starting FEN (field 2) and the played moves (field 3)."""
    stack = [frame]
    while stack:
        b = stack.pop()
        try:
            d = by_field(b)
        except (ValueError, IndexError):
            continue
        rv = one(d, 3)
        if isinstance(rv, bytes):
            try:
                rd = by_field(rv)
                fen = one(rd, 2)
                if isinstance(fen, bytes) and fen.count(b"/") == 7 and rd.get(3):
                    return d
            except (ValueError, IndexError):
                pass
        stack.extend(v for vs in d.values() for v in vs if isinstance(v, bytes) and len(v) > 50)
    return None


def decode_capture(cap: dict) -> dict:
    frames = []
    for s in cap.get("sockets", []):
        for fr in s.get("in", []):
            if "b64" in fr:
                frames.append(base64.b64decode(fr["b64"]))
    frames.sort(key=len, reverse=True)
    for fr in frames:
        gr = find_game_review(fr)
        if gr is None:
            continue
        review = by_field(one(gr, 3))
        meta = by_field(one(gr, 5, b""))
        version = by_field(one(meta, 1, b""))
        plies = [played_move(x) for x in review.get(3, [])]
        engines = Counter(
            m["score"]["engine"]
            for p in plies
            for m in (p["played"], p["best"])
            if m and m.get("score")
        )
        return {
            "id": cap["id"],
            "captured_at": cap.get("captured_at"),
            "cee_version": ".".join(str(one(version, k, 0)) for k in (1, 2, 3)),
            "score_engines": {str(k): v for k, v in engines.items()},
            "starting_fen": one(review, 2, b"").decode(),
            "plies": [{"ply": i + 1, **p} for i, p in enumerate(plies)],
        }
    raise ValueError("no GameReview found in the captured frames")


# --------------------------------------------------------------------------- oracle

PIECES = ("Pawn", "Knight", "Bishop", "Rook", "Queen", "King")
# Styles a Game Review uses for the move speech. Others (hints, bot chat, takeaways, buttons) are
# only used when nothing in these styles matches.
REVIEW_STYLES = ("Personal", "OpposingPersonal", "Impersonal", "Explain", "Punish")


def camel(snake: str) -> str:
    return "".join(p.capitalize() for p in snake.lower().split("_"))


def load_tag_names(path: Path) -> dict[str, int]:
    """CamelCase tag name -> internal priority index (lower = said first)."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" not in line:
            continue
        idx, names = line.split("=", 1)
        for n in names.split("/"):
            out.setdefault(camel(n.strip()), int(idx))
    return out


def load_asset(path: Path) -> dict[str, str]:
    s = path.read_text(encoding="utf-8", errors="replace")
    return json.loads(s[: s.rindex("}") + 1])["speech_map"]


def norm(text: str) -> str:
    t = text.replace("*", "").replace("’", "'").replace("‘", "'")
    t = t.replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t.rstrip(" .!?")


def parse_key(key: str, tags: dict[str, int]) -> dict:
    """`[Circ-[Child-]]Tag[Piece]-Style-N` -> {chain, tag, piece, style}. FEN-keyed opening remarks
    become tag `OpeningRemark`."""
    if ":" in key and "/" in key.split(":")[0]:
        return {"chain": [], "tag": "OpeningRemark", "piece": None, "style": "Impersonal"}
    if key.startswith("InPlace"):
        body = key[len("InPlace") :].rsplit("-", 1)[0]
        chain = []
        for c in ("WinsMaterial", "LeadsTo", "Brilliant"):
            if body.startswith(c) and body != c:
                chain.append(c)
                body = body[len(c) :]
        tag, piece = split_piece(body, tags)
        return {"chain": chain, "tag": tag, "piece": piece, "style": "InPlace"}
    parts = key.split("-")
    if len(parts) >= 3 and parts[-1].isdigit():
        style, body = parts[-2], parts[:-2]
    else:
        style, body = None, parts
    # A style can be two tokens (`PuzzleGoal-Goal`); the tag is the last token that parses as one.
    for k in range(len(body) - 1, -1, -1):
        tag, piece = split_piece(body[k], tags)
        if tag in tags:
            return {"chain": body[:k], "tag": tag, "piece": piece, "style": style}
    tag, piece = split_piece(body[-1], tags)
    return {"chain": body[:-1], "tag": tag, "piece": piece, "style": style}


# Asset spellings of tags whose enum name differs.
TAG_ALIASES = {
    "Obvious(Recapture)": "ObviousRecapture",
    "Obvious(Retreat)": "ObviousRetreat",
    "ForcesIsolates": "ForcesIsolatedPawn",
    "ForcesDoublesPawns": "ForcesDoubledPawns",
    "ThreatensPinnedPiece": "ThreatensPinned",
    "BlockadesOppPushingSquare": "BlockadesOpponentPushingSquare",
    "BlockadesOppPromotionSquare": "BlockadesOpponentPromotionSquare",
    "DirectSacrificeEnPrise": "DirectSacrificeEnprise",
    "KeyMoment(BadFasterMate)": "KeymomentBadFasterMate",
    "KeyMoment(GoodFasterMate)": "KeymomentGoodFasterMate",
    "ForcesDoublesCastlePawns": "ForcesDoubledCastlePawns",
    "ForcesDoubledIsolated": "ForcesDoubledPawns",
    "ForcesIsolatesPawnOnSemiOpenFile": "ForcesIsolatedPawn",
    "ForcesMovesPawnInFrontOfKing": "MovesPawnInFrontOfKing",
    "EliminatesOppPassed": "EliminatesOpponentPassedPawn",
    "DirectSacrificeEnPriseMate": "DirectSacrificeEnpriseMate",
}


def split_piece(name: str, tags: dict[str, int]) -> tuple[str, str | None]:
    name = TAG_ALIASES.get(name, name)
    if name in tags or name.endswith("InFrontOfKing"):
        return name, None
    for p in PIECES:
        if name.endswith(p) and TAG_ALIASES.get(name[: -len(p)], name[: -len(p)]) in tags:
            return TAG_ALIASES.get(name[: -len(p)], name[: -len(p)]), p.lower()
    for p in PIECES:
        if name.endswith(p) and len(name) > len(p):
            return TAG_ALIASES.get(name[: -len(p)], name[: -len(p)]), p.lower()
    return name, None


class Oracle:
    def __init__(self, oracle_dir: Path):
        self.tags = load_tag_names(oracle_dir / "tag_names.txt")
        asset = load_asset(oracle_dir / "coach_en_us.raw")
        self.full: dict[str, list[str]] = defaultdict(list)
        self.inplace: dict[str, list[str]] = defaultdict(list)
        for key, text in asset.items():
            if not isinstance(text, str) or not text.strip():
                continue
            for variant in colour_variants(text):
                n = norm(variant)
                if key.startswith("InPlace"):
                    self.inplace[n].append(key)
                else:
                    self.full[n].append(key)
        # Longest verb phrases first, so a piece-specific phrase beats the generic one it ends with.
        self.inplace_sorted = sorted(self.inplace, key=len, reverse=True)

    def match(self, sentence: str) -> dict:
        n0 = norm(sentence)
        for n in text_variants(n0):
            if n in self.full:
                return {"kind": "full", "keys": pick_review_keys(self.full[n])}
        for n in text_variants(n0):
            for phrase in self.inplace_sorted:
                if len(phrase) < 8:
                    continue
                if n.endswith(phrase) and (len(n) == len(phrase) or n[-len(phrase) - 1] == " "):
                    prefix = n[: -len(phrase)].strip()
                    return {
                        "kind": "composed",
                        "keys": sorted(self.inplace[phrase]),
                        "prefix_circ": prefix_circumstance(prefix),
                        "prefix": prefix,
                    }
        # Verb phrases that are not in the embedded asset (the live asset is newer): a few generic
        # chess words decide the tag.
        prefix_circ = None
        m = PREFIX_SPLIT.match(n0)
        if m:
            prefix_circ = prefix_circumstance(m.group(1))
        for rx, tag in FALLBACK_TAGS:
            if rx.search(n0):
                return {"kind": "pattern", "keys": [f"InPlace{tag}-pattern"],
                        "prefix_circ": prefix_circ, "prefix": m.group(1) if m else ""}
        return {"kind": "none", "keys": []}

    def label(self, keys: list[str]) -> dict | None:
        """One (chain, tag, piece) for a set of candidate keys: the highest-priority tag; the
        candidates' chains are kept when they disagree."""
        parsed = [parse_key(k, self.tags) for k in keys]
        if not parsed:
            return None
        parsed.sort(key=lambda p: (self.tags.get(p["tag"], 999), len(p["chain"])))
        best = dict(parsed[0])
        best["ambiguous"] = len({(tuple(p["chain"]), p["tag"]) for p in parsed}) > 1
        return best


def colour_variants(text: str) -> list[str]:
    if "%color%" not in text and "%opposingcolor%" not in text:
        return [text]
    out = []
    for me, them in (("White", "Black"), ("Black", "White")):
        out.append(text.replace("%color%", me).replace("%opposingcolor%", them))
    return out


def pick_review_keys(keys: list[str]) -> list[str]:
    review = [k for k in keys if any(f"-{s}-" in k for s in REVIEW_STYLES)]
    return sorted(review or keys)


# The outer circumstance of a composed sentence, from single generic words of its prefix. Order
# matters: a prefix that stops or prevents something is Prevents even though it also says "able";
# one that mentions a missed or better option is Misses even though it also says "chance".
PREFIX_RULES = [
    (re.compile(r"\bprevent|\bstop"), "Prevents"),
    (re.compile(r"\bthreat"), "Threatens"),
    (re.compile(r"\bforc|\bhave to\b|\bmust\b"), "Forces"),
    (re.compile(r"\bmiss|\bbest\b|\bbetter\b|\bopportunity|\bcould have|\bshould have"), "Misses"),
    (re.compile(r"\ballow|\bpermit|\blets?\b|\bchance\b|\bable\b|\bcan now"), "Permits"),
]
# Splits "<prefix> to <verb phrase>" when the verb phrase is unknown: the prefix ends at the last
# "to" before the verb phrase's first word (the shortest prefix that does).
PREFIX_SPLIT = re.compile(r"^(.*?\bto)\s+(?!be\b)\w")
# Generic chess words for verb phrases missing from the embedded asset, most specific first.
FALLBACK_TAGS = [
    (re.compile(r"\bfork\b.*\bking and the queen|\bking and the queen\b.*\bfork"), "RoyalFork"),
    (re.compile(r"\btrapping\b|\btrapped\b"), "AttacksTrappedPiece"),
    (re.compile(r"\bpinned\b"), "PressuresPinnedPiece"),
    (re.compile(r"\ben prise\b"), "DirectSacrificeEnprise"),
    (re.compile(r"\bsacrific\w*\b.*\bcapture\b"), "DirectSacrificeCapture"),
    (re.compile(r"\bthreaten\w* to capture\b"), "CaptureThreat"),
    (re.compile(r"\bout of danger\b"), "EscapesThreat"),
    (re.compile(r"\brecapture toward the center\b"), "RecapturesTowardCenter"),
    (re.compile(r"\bsame line\b"), "CreatesBattery"),
    (re.compile(r"\binactive piece\b"), "GoodTrade"),
    (re.compile(r"\bcentral pawn push\b"), "PreparesCentralPush"),
    (re.compile(r"\bbreak in the center\b"), "CentralBreak"),
    (re.compile(r"\bpawn chain\b"), "AttacksPawnChain"),
    (re.compile(r"\bpawn in front of the king\b"), "MovesPawnInFrontOfKing"),
    (re.compile(r"\bzwischenzug\b"), "ZwischenzugBeforeThreatResolution"),
    (re.compile(r"\bpassed pawn\b.*\bpromotion\b"), "BlockadesOpponentPushingSquare"),
    (re.compile(r"\bpunish\w* (a|the|their|your)\b.*\bblunder\b"), "BlunderPunish"),
    (re.compile(r"\blure\b"), "Attraction"),
    (re.compile(r"\bequal\b.*\bnow\b.*\badvantage\b"), "EqualToWorse"),
]
_PIECE_NOUN = re.compile(r"\b(a|an|the|their|your) (pawn|knight|bishop|rook|queen)\b")


def text_variants(n: str) -> list[str]:
    """The sentence, then with piece names replaced by "piece" (the realiser fills piece names into
    generic wordings)."""
    out = [n]
    g = _PIECE_NOUN.sub(lambda m: ("a" if m.group(1) == "an" else m.group(1)) + " piece", n)
    if g != n:
        out.append(g)
    return out


def prefix_circumstance(prefix: str) -> str | None:
    for rx, circ in PREFIX_RULES:
        if rx.search(prefix):
            return circ
    return None


# Speech that carries no board event (classification remarks, encouragement, game status).
NON_EVENT_TAGS = {"OpeningRemark", "Classification"}


def label_sentences(oracle: Oracle, sentences: list[list[dict]]) -> list[dict]:
    out = []
    for frags in sentences:
        text = "".join(f["text"] for f in frags)
        m = oracle.match(text)
        lab = oracle.label(m["keys"]) if m["keys"] else None
        rec = {"kind": m["kind"], "keys": m["keys"][:12]}
        if lab:
            chain = list(lab["chain"])
            if m["kind"] in ("composed", "pattern") and m.get("prefix_circ"):
                chain = [m["prefix_circ"], *chain]
            rec.update(chain=chain, tag=lab["tag"], piece=lab["piece"], ambiguous=lab["ambiguous"],
                       tag_known=lab["tag"] in oracle.tags)
            if m["kind"] in ("composed", "pattern"):
                rec["prefix_circ"] = m.get("prefix_circ")
        out.append(rec)
    return out


# Remarks that frame the move ("the only good move") rather than explain it: the main event only
# when no other sentence names one.
FRAMING_TAGS = {"Critical"}


def main_event(labels: list[dict]) -> dict | None:
    """The first sentence that names a board event (a known tag, not an opening remark)."""
    events = [lab for lab in labels if lab.get("tag_known") and lab.get("tag") not in NON_EVENT_TAGS]
    events.sort(key=lambda lab: lab["tag"] in FRAMING_TAGS)
    if events:
        return {k: events[0][k] for k in ("chain", "tag", "piece", "ambiguous")}
    return None


# --------------------------------------------------------------------------- commands


def cmd_ingest(args) -> int:
    """Split `coachPull()` or `coachPullGz()` output (coach_capture.js) into <captures>/raw/<id>.json. The input may be
    the bare JSON string, or a saved tool result wrapping it (a JSON list of {text} parts holding a
    JSON-encoded string, optionally followed by padding on later lines)."""
    raw = args.captures_dir / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    for path in args.files:
        text = path.read_text(encoding="utf-8")
        if text.lstrip().startswith("["):
            text = "".join(x.get("text", "") for x in json.loads(text))
        if text.startswith('"'):
            text = json.JSONDecoder().raw_decode(text)[0]
        if text.startswith("GZ1:"):  # coachPullGz()
            text = gzip.decompress(base64.b64decode(text[4 : text.index("|")])).decode("utf-8")
        payload = json.JSONDecoder().raw_decode(text.lstrip())[0]
        for cap in payload["caps"]:
            if not cap or not cap.get("ok") or not re.fullmatch(r"\d+", str(cap.get("id"))):
                print(f"skipped {cap and cap.get('id')}", file=sys.stderr)
                continue
            (raw / f"{cap['id']}.json").write_text(json.dumps(cap), encoding="utf-8")
            print(f"saved {cap['id']}", file=sys.stderr)
    return 0


def cmd_decode(args) -> int:
    raw = args.captures_dir / "raw"
    n = 0
    for path in sorted(raw.glob("*.json")):
        out = args.captures_dir / f"{path.stem}.coach.json"
        if out.exists() and not args.force and out.stat().st_mtime >= path.stat().st_mtime:
            continue
        cap = json.loads(path.read_text(encoding="utf-8"))
        try:
            dec = decode_capture(cap)
        except ValueError as e:
            print(f"{path.stem}: {e}", file=sys.stderr)
            continue
        out.write_text(json.dumps(dec, ensure_ascii=False), encoding="utf-8")
        n += 1
    print(f"decoded {n} captures", file=sys.stderr)
    return 0


def cmd_match(args) -> int:
    oracle = Oracle(args.oracle_dir)
    stats = Counter()
    unmatched_prefix = Counter()
    unknown_tags = Counter()
    for path in sorted(args.captures_dir.glob("*.coach.json")):
        dec = json.loads(path.read_text(encoding="utf-8"))
        plies = []
        for p in dec["plies"]:
            rec = {
                "ply": p["ply"],
                "uci": p["played"]["uci"],
                "classification": p["played"]["classification"],
                "key_moment": p["key_moment"],
                "emotion": p["emotion"],
            }
            for side in ("played", "best"):
                mv = p.get(side)
                if not mv:
                    continue
                labels = label_sentences(oracle, mv["speech"])
                for lab in labels:
                    stats[f"{side}:{lab['kind']}"] += 1
                    if lab["kind"] == "composed" and not lab.get("prefix_circ"):
                        unmatched_prefix[lab.get("tag")] += 1
                    if lab.get("tag") and not lab.get("tag_known"):
                        unknown_tags[lab["tag"]] += 1
                rec[side] = {
                    "uci": mv["uci"],
                    "sentences": labels,
                    "main": main_event(labels),
                    "buttons": [
                        {"moves": b["moves"], "keys": button_keys(oracle, b)} for b in mv["buttons"]
                    ],
                    "markings": mv["markings"],
                }
            plies.append(rec)
        out = args.captures_dir / path.name.replace(".coach.json", ".keys.json")
        out.write_text(json.dumps({"id": dec["id"], "score_engines": dec["score_engines"],
                                   "cee_version": dec["cee_version"], "plies": plies}),
                       encoding="utf-8")
        stats["games"] += 1
    total = {side: sum(v for k, v in stats.items() if k.startswith(side + ":"))
             for side in ("played", "best")}
    print(f"games: {stats['games']}")
    for side in ("played", "best"):
        t = total[side] or 1
        print(f"{side} sentences: {total[side]}; " + ", ".join(
            f"{kind} {stats[side + ':' + kind]} ({stats[side + ':' + kind] / t:.1%})"
            for kind in ("full", "composed", "pattern", "none")))
    if args.report:
        print("composed sentences without a recognised prefix, by tag:", dict(unmatched_prefix))
        print("tags not in tag_names.txt:", dict(unknown_tags.most_common(30)))
    return 0


def button_keys(oracle: Oracle, button: dict) -> list[str]:
    n = norm(button["show"])
    return pick_review_keys(oracle.full.get(n, []))[:6] if n else []


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--oracle-dir", type=Path, default=DEFAULT_ORACLE)
    p.add_argument("--captures-dir", type=Path, default=None,
                   help="default: <oracle-dir>/captures")
    sub = p.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("ingest", help="coachPull() output -> <captures>/raw/<id>.json")
    i.add_argument("files", nargs="+", type=Path)
    d = sub.add_parser("decode", help="raw frames -> <id>.coach.json")
    d.add_argument("--force", action="store_true")
    m = sub.add_parser("match", help="<id>.coach.json -> <id>.keys.json via the text asset")
    m.add_argument("--report", action="store_true", help="also list unmatched prefixes and tags")
    args = p.parse_args(argv)
    if args.captures_dir is None:
        args.captures_dir = args.oracle_dir / "captures"
    return args


def main(argv=None) -> int:
    args = parse_args(argv)
    return {"ingest": cmd_ingest, "decode": cmd_decode, "match": cmd_match}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
