#!/usr/bin/env python3
"""Calibration harness: compare our review labels with the reference app's labels.

For every game id in a list file this script

1. reviews `<games-dir>/<id>.pgn` with the backend (POST /api/reviews, poll, GET .../result),
   caching the result in `<runs-dir>/<run-name>/<id>.json` under a cache key made of the git
   commit, a hash of the uncommitted `backend/` changes, the engine reported by /api/health, the
   search settings, the rule-config override and the PGN text;
2. aligns our plies with `<games-dir>/<id>.labels.json` by index and checks the SAN sequence;
3. writes `report.md` and `summary.json` into the run directory and prints a one-line summary.

The git commit and `backend/` changes are read from the app's checkout: `$CHESS_REVIEW_DIR`, else
`../chess-review` next to this repository.

Python 3 standard library only. Typical use (from this repository's root, server already running):

    python3 tools/calibrate/compare.py --run-name baseline --games tests/calibration/tuning.txt

The server must be rebuilt and restarted after backend code changes: the cache key tracks the
source tree, but the harness cannot see which binary is answering on --url.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
# The app's checkout (its git state is the cache key): $CHESS_REVIEW_DIR, else ../chess-review.
APP_ROOT = Path(os.environ.get("CHESS_REVIEW_DIR") or REPO_ROOT.parent / "chess-review").resolve()
HARNESS_VERSION = 1

# Reference labels in the fixed display order used for the confusion matrix.
LABELS = [
    "brilliant",
    "great",
    "best",
    "excellent",
    "good",
    "book",
    "inaccuracy",
    "mistake",
    "miss",
    "blunder",
]
# Ordinal scale for "within one step"; every other label must match exactly.
ORDINAL = ["best", "excellent", "good", "inaccuracy", "mistake", "blunder"]
# Our classification -> reference vocabulary.
OUR_LABEL_MAP = {"great_find": "great", "forced": "best"}
# Lenient spellings accepted in labels.json.
APP_LABEL_ALIASES = {"great_find": "great", "forced": "best"}

# Paths in `backend/` that do not affect the server and are left out of the diff hash.
DIFF_EXCLUDES = [":(exclude,glob)backend/crates/*/examples/**"]


class HarnessError(Exception):
    """A per-game failure (review failed, bad input); the game is skipped and reported."""


class FatalError(Exception):
    """Aborts the whole run."""


# --------------------------------------------------------------------------- HTTP

_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # never proxy localhost


def http_json(method: str, url: str, body=None, timeout: float = 30.0):
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with _OPENER.open(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        payload = e.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(payload)["error"]
            text = f"{err.get('code')}: {err.get('message')}"
        except Exception:
            text = payload[:500]
        raise HarnessError(f"{method} {url} -> HTTP {e.code} {text}") from None
    except (urllib.error.URLError, OSError) as e:
        raise HarnessError(f"{method} {url} failed: {e}") from None


# --------------------------------------------------------------------------- source state


def _git(*args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(APP_ROOT), *args], capture_output=True, check=False
    )
    if proc.returncode != 0:
        raise FatalError(
            f"git {' '.join(args)} failed: {proc.stderr.decode(errors='replace').strip()}"
        )
    return proc.stdout


def source_state() -> dict:
    """Git commit plus a hash of every uncommitted change under backend/ (tracked and untracked)."""
    commit = _git("rev-parse", "HEAD").decode().strip()
    pathspec = ["--", "backend", *DIFF_EXCLUDES]
    diff = _git("diff", "HEAD", "--binary", "--no-color", "--no-ext-diff", *pathspec)
    untracked = sorted(
        p
        for p in _git("ls-files", "--others", "--exclude-standard", "-z", *pathspec).split(b"\0")
        if p
    )
    h = hashlib.sha256()
    h.update(diff)
    for rel in untracked:
        h.update(b"\0untracked\0" + rel + b"\0")
        try:
            h.update(hashlib.sha256((APP_ROOT / rel.decode()).read_bytes()).digest())
        except OSError:
            h.update(b"<unreadable>")
    return {
        "git_commit": commit,
        "backend_diff_sha256": h.hexdigest(),
        "backend_dirty": bool(diff) or bool(untracked),
        "backend_untracked_files": [p.decode() for p in untracked],
    }


# --------------------------------------------------------------------------- inputs


def read_id_list(path: Path) -> list[str]:
    if not path.is_file():
        raise FatalError(f"game list {path} does not exist")
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line and line not in ids:
            ids.append(line)
    return ids


def load_config_override(text: str | None):
    if text is None:
        return None
    if text.startswith("@"):
        text = Path(text[1:]).read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError as e:
        raise FatalError(f"--config is not valid JSON: {e}") from None
    if not isinstance(value, dict):
        raise FatalError("--config must be a JSON object (a partial ReviewConfig)")
    return value


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


# --------------------------------------------------------------------------- reviewing


class Reviewer:
    def __init__(self, args, base_key: dict, run_dir: Path):
        self.args = args
        self.url = args.url.rstrip("/")
        self.base_key = base_key
        self.run_dir = run_dir
        self.stop = threading.Event()
        self.in_flight: set[str] = set()
        self.lock = threading.Lock()
        self.log_lock = threading.Lock()

    def log(self, msg: str) -> None:
        if not self.args.quiet:
            with self.log_lock:
                print(msg, file=sys.stderr, flush=True)

    def key_for(self, pgn: str) -> dict:
        return {**self.base_key, "pgn_sha256": sha256_text(pgn)}

    def cached(self, gid: str, key: dict):
        path = self.run_dir / f"{gid}.json"
        if not path.is_file() or self.args.refresh:
            return None
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        stored = entry.get("cache_key")
        if not isinstance(stored, dict):
            return None
        if self.args.offline:
            ignore = {"engine", "server_version"}
            same = {k: v for k, v in stored.items() if k not in ignore} == {
                k: v for k, v in key.items() if k not in ignore
            }
        else:
            same = stored == key
        return entry if same else None

    def review(self, gid: str, pgn: str, key: dict) -> dict:
        body = {"pgn": pgn, "multipv": self.args.multipv}
        if self.args.nodes:
            body["nodes"] = self.args.nodes
        else:
            body["depth"] = self.args.depth
        if self.args.config_override is not None:
            body["config"] = self.args.config_override
        if self.args.player_side:
            body["player_side"] = self.args.player_side
        started = time.monotonic()
        status = http_json("POST", f"{self.url}/api/reviews", body)
        rid = status["id"]
        with self.lock:
            self.in_flight.add(rid)
        try:
            last_log = 0.0
            while True:
                state = status.get("state")
                if state == "completed":
                    break
                if state in ("failed", "cancelled"):
                    raise HarnessError(
                        f"review {rid} ended as {state}: {status.get('error') or 'no error message'}"
                    )
                if self.stop.is_set():
                    raise HarnessError("interrupted")
                elapsed = time.monotonic() - started
                if elapsed > self.args.timeout:
                    self.cancel(rid)
                    raise HarnessError(f"review {rid} timed out after {self.args.timeout:.0f}s")
                if elapsed - last_log >= 30:
                    last_log = elapsed
                    prog = status.get("progress") or {}
                    self.log(
                        f"  {gid}: {state} {prog.get('done', 0)}/{prog.get('total', 0)} "
                        f"({elapsed:.0f}s)"
                    )
                time.sleep(self.args.poll_interval)
                status = http_json("GET", f"{self.url}/api/reviews/{rid}")
            result = http_json("GET", f"{self.url}/api/reviews/{rid}/result", timeout=300)
        finally:
            with self.lock:
                self.in_flight.discard(rid)
        seconds = time.monotonic() - started
        settings = result.get("settings") or {}
        limit = settings.get("limit") or {}
        want = {"nodes": self.args.nodes} if self.args.nodes else {"depth": self.args.depth}
        if any(limit.get(k) != v for k, v in want.items()) or settings.get("multipv") != self.args.multipv:
            raise HarnessError(
                f"server used settings {settings}, expected {want} "
                f"multipv {self.args.multipv}"
            )
        entry = {
            "game_id": gid,
            "cache_key": key,
            "cache_key_sha256": hashlib.sha256(canonical(key).encode()).hexdigest(),
            "reviewed_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "review_seconds": round(seconds, 2),
            "result": result,
        }
        tmp = self.run_dir / f".{gid}.json.tmp"
        tmp.write_text(json.dumps(entry, separators=(",", ":")), encoding="utf-8")
        os.replace(tmp, self.run_dir / f"{gid}.json")
        return entry

    def cancel(self, rid: str) -> None:
        try:
            http_json("DELETE", f"{self.url}/api/reviews/{rid}", timeout=5)
        except HarnessError:
            pass

    def cancel_all(self) -> None:
        self.stop.set()
        with self.lock:
            ids = list(self.in_flight)
        for rid in ids:
            self.cancel(rid)


def fetch_results(args, game_ids, reviewer: Reviewer):
    """Returns {gid: (labels, entry, source)} and {gid: reason} for skipped games."""
    inputs = {}
    skipped = {}
    for gid in game_ids:
        pgn_path = args.games_dir / f"{gid}.pgn"
        labels_path = args.games_dir / f"{gid}.labels.json"
        if not pgn_path.is_file():
            skipped[gid] = f"missing {pgn_path.name}"
            continue
        if not labels_path.is_file():
            skipped[gid] = f"missing {labels_path.name}"
            continue
        try:
            labels = json.loads(labels_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            skipped[gid] = f"{labels_path.name} is not valid JSON: {e}"
            continue
        pgn = pgn_path.read_text(encoding="utf-8")
        inputs[gid] = (pgn, labels)

    done = {}
    todo = []
    for gid, (pgn, labels) in inputs.items():
        key = reviewer.key_for(pgn)
        entry = reviewer.cached(gid, key)
        if entry is not None:
            done[gid] = (labels, entry, "cache")
        elif args.offline:
            skipped[gid] = "no cached result matching the current source and settings (--offline)"
        else:
            todo.append((gid, pgn, labels, key))

    if todo:
        reviewer.log(
            f"[{args.run_name}] {len(done)} cached, reviewing {len(todo)} game(s) "
            f"at depth {args.depth} multipv {args.multipv}, {args.concurrency} at a time"
        )
    t0 = time.monotonic()
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.concurrency))
    futures = {
        pool.submit(reviewer.review, gid, pgn, key): (gid, labels) for gid, pgn, labels, key in todo
    }
    try:
        for n, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            gid, labels = futures[fut]
            try:
                entry = fut.result()
            except HarnessError as e:
                skipped[gid] = f"review failed: {e}"
                reviewer.log(f"  [{n}/{len(todo)}] {gid}: FAILED {e}")
                continue
            done[gid] = (labels, entry, "reviewed")
            reviewer.log(
                f"  [{n}/{len(todo)}] {gid}: {len(entry['result']['plies'])} plies in "
                f"{entry['review_seconds']:.1f}s (elapsed {time.monotonic() - t0:.0f}s)"
            )
    except KeyboardInterrupt:
        reviewer.log("interrupted: cancelling in-flight reviews")
        reviewer.cancel_all()
        pool.shutdown(wait=False, cancel_futures=True)
        raise
    pool.shutdown(wait=True)
    return done, skipped


# --------------------------------------------------------------------------- comparison


def norm_san(san) -> str:
    s = str(san or "").strip().replace("0-0-0", "O-O-O").replace("0-0", "O-O")
    s = s.rstrip("+#!?").replace("=", "")
    return s


def norm_app_label(raw):
    """Returns (label, exclusion_reason)."""
    if raw is None:
        return None, "missing"
    s = str(raw).strip().lower()
    if s.startswith("uncertain"):
        return None, "uncertain"
    if s in ("", "none"):
        return None, "none"
    s = APP_LABEL_ALIASES.get(s, s)
    if s in LABELS:
        return s, None
    return None, "unknown"


def norm_our_label(raw) -> str:
    if raw is None:
        return "none"
    return OUR_LABEL_MAP.get(raw, raw)


def fmt_eval(ev) -> str | None:
    if not ev:
        return None
    if ev.get("kind") == "cp":
        return f"{ev['cp'] / 100:+.2f}"
    if ev.get("kind") == "mate":
        moves = ev.get("moves", 0)
        if moves == 0:
            return "#" if ev.get("winner") == "white" else "-#"
        return f"M{moves}" if ev.get("winner") == "white" else f"-M{moves}"
    return str(ev)


def check_alignment(app_plies: list, ours: list) -> str | None:
    for i, (a, o) in enumerate(zip(app_plies, ours)):
        if a.get("ply") is not None and a.get("ply") != i + 1:
            return f"labels entry {i} has ply {a.get('ply')}, expected {i + 1}"
        if norm_san(a.get("san")) != norm_san(o.get("san")):
            return f"SAN mismatch at ply {i + 1}: app {a.get('san')!r} vs ours {o.get('san')!r}"
    if len(app_plies) != len(ours):
        return f"ply count differs: labels have {len(app_plies)}, our review has {len(ours)}"
    return None


def compare_game(gid: str, labels: dict, result: dict) -> list[dict]:
    records = []
    for i, (a, o) in enumerate(zip(labels.get("plies") or [], result["plies"])):
        app, excluded = norm_app_label(a.get("label"))
        best = o.get("best_move") or {}
        dots = "." if o.get("mover") == "white" else "..."
        records.append(
            {
                "game": gid,
                "ply": i + 1,
                "move": f"{o.get('move_number')}{dots}",
                "san": o.get("san"),
                "mover": o.get("mover"),
                "app_raw": a.get("label"),
                "app": app,
                "excluded": excluded,
                "ours_raw": o.get("classification"),
                "ours": norm_our_label(o.get("classification")),
                "rule": o.get("rule"),
                "precision": o.get("precision"),
                "miss_kind": o.get("miss_kind"),
                "ep_before": o.get("ep_before"),
                "ep_lost": o.get("ep_lost"),
                "played_is_best": o.get("played_is_best"),
                "our_best": best.get("san"),
                "our_best_uci": best.get("uci"),
                "app_best_san": a.get("app_best_san"),
                "app_best_uci": a.get("app_best_uci"),
                "app_eval": a.get("app_eval"),
                "our_eval": fmt_eval(o.get("eval_after")),
            }
        )
    return records


def within_one(app: str, ours: str) -> bool:
    if app == ours:
        return True
    if app in ORDINAL and ours in ORDINAL:
        return abs(ORDINAL.index(app) - ORDINAL.index(ours)) <= 1
    return False


def ratio(num: float, den: float):
    return None if den == 0 else num / den


def f1(p, r):
    if p is None or r is None or p + r == 0:
        return None if p is None or r is None else 0.0
    return 2 * p * r / (p + r)


def analyse(records: list[dict]) -> dict:
    scored = [r for r in records if r["app"] is not None]
    excluded = Counter(r["excluded"] for r in records if r["app"] is None)
    uncertain_guess_hits = 0
    for r in records:
        if r["excluded"] == "uncertain":
            # The collector's guess may list several candidates: "uncertain:best/excellent".
            guesses = str(r["app_raw"]).split(":", 1)[-1].strip().lower().split("/")
            guesses = {APP_LABEL_ALIASES.get(g.strip(), g.strip()) for g in guesses}
            uncertain_guess_hits += r["ours"] in guesses

    confusion: dict[str, Counter] = {lab: Counter() for lab in LABELS}
    for r in scored:
        confusion[r["app"]][r["ours"]] += 1
    our_extra = sorted({r["ours"] for r in scored} - set(LABELS))

    exact = sum(r["app"] == r["ours"] for r in scored)
    near = sum(within_one(r["app"], r["ours"]) for r in scored)

    per_label = {}
    for lab in LABELS:
        tp = confusion[lab][lab]
        actual = sum(confusion[lab].values())
        predicted = sum(confusion[row][lab] for row in LABELS)
        p, rc = ratio(tp, predicted), ratio(tp, actual)
        per_label[lab] = {
            "app_count": actual,
            "our_count": predicted,
            "tp": tp,
            "precision": p,
            "recall": rc,
            "f1": f1(p, rc),
        }
    n = len(scored)
    per_100 = {
        lab: {
            "app": ratio(per_label[lab]["app_count"] * 100, n),
            "ours": ratio(per_label[lab]["our_count"] * 100, n),
        }
        for lab in ("brilliant", "great")
    }
    best_cmp = [r for r in scored if r["app_best_uci"] and r["our_best_uci"]]
    best_agree = sum(r["app_best_uci"] == r["our_best_uci"] for r in best_cmp)
    return {
        "scored": scored,
        "excluded": excluded,
        "uncertain_guess_hits": uncertain_guess_hits,
        "confusion": confusion,
        "our_extra": our_extra,
        "exact": exact,
        "near": near,
        "per_label": per_label,
        "per_100": per_100,
        "best_move": {"compared": len(best_cmp), "agree": best_agree},
    }


def accuracy_rows(compared: dict) -> list[dict]:
    rows = []
    for gid, (labels, entry, _src) in compared.items():
        res = entry["result"]
        for side in ("white", "black"):
            app = labels.get(f"{side}_accuracy")
            ours = ((res.get(side) or {}).get("accuracy") or {}).get("overall")
            rows.append(
                {
                    "game": gid,
                    "side": side,
                    "app": app,
                    "ours": ours,
                    "diff": None if app is None or ours is None else ours - app,
                }
            )
    return rows


# --------------------------------------------------------------------------- report


def pct(x) -> str:
    return "-" if x is None else f"{100 * x:.1f}%"


def num(x, digits: int = 3) -> str:
    return "-" if x is None else f"{x:.{digits}f}"


def md_cell(x) -> str:
    if x is None:
        return "-"
    if isinstance(x, bool):
        return "yes" if x else "no"
    if isinstance(x, float):
        return f"{x:.3f}"
    return str(x).replace("|", "\\|")


def table(header: list[str], rows: list[list], align: str = "") -> list[str]:
    """Markdown table; `align` has one character per column, "r" for right-aligned."""
    seps = ["---:" if align[i : i + 1] == "r" else "---" for i in range(len(header))]
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(seps) + "|"]
    for row in rows:
        out.append("| " + " | ".join(md_cell(c) for c in row) + " |")
    return out


def build_report(ctx: dict) -> tuple[str, dict]:
    a = ctx["analysis"]
    scored = a["scored"]
    n = len(scored)
    acc = [r for r in ctx["accuracy"] if r["diff"] is not None]
    mad = ratio(sum(abs(r["diff"]) for r in acc), len(acc))
    bias = ratio(sum(r["diff"] for r in acc), len(acc))
    max_abs = max((abs(r["diff"]) for r in acc), default=None)
    mismatches = [r for r in scored if r["app"] != r["ours"]]
    rule_counts = Counter(r["rule"] for r in mismatches)
    src = ctx["source"]
    pl = a["per_label"]

    summary = {
        "run_name": ctx["run_name"],
        "generated_at": ctx["generated_at"],
        "harness_version": HARNESS_VERSION,
        "git_commit": src["git_commit"],
        "backend_dirty": src["backend_dirty"],
        "backend_diff_sha256": src["backend_diff_sha256"],
        "engine": ctx["engine"],
        "settings": ctx["settings"],
        "games": {
            "requested": len(ctx["game_ids"]),
            "compared": len(ctx["compared"]),
            "compared_ids": list(ctx["compared"]),
            "skipped": ctx["skipped"],
            "from_cache": sum(1 for v in ctx["compared"].values() if v[2] == "cache"),
        },
        "plies": {
            "total": len(ctx["records"]),
            "scored": n,
            "excluded": dict(a["excluded"]),
            "uncertain_guess_matches_ours": a["uncertain_guess_hits"],
        },
        "exact_agreement": ratio(a["exact"], n),
        "within_one_agreement": ratio(a["near"], n),
        "per_label": pl,
        "per_100_moves": a["per_100"],
        "accuracy": {"mad": mad, "bias": bias, "max_abs": max_abs, "n": len(acc)},
        "best_move_agreement": {
            **a["best_move"],
            "rate": ratio(a["best_move"]["agree"], a["best_move"]["compared"]),
        },
        "confusion": {
            row: dict(a["confusion"][row]) for row in LABELS if a["confusion"][row]
        },
        "mismatch_rules": dict(rule_counts.most_common()),
    }

    L: list[str] = []
    s = ctx["settings"]
    L.append(f"# Calibration report: {ctx['run_name']}")
    L.append("")
    dirty = (
        f" + uncommitted backend changes (diff sha256 `{src['backend_diff_sha256'][:12]}`)"
        if src["backend_dirty"]
        else " (backend clean)"
    )
    L.append(f"- Generated: {ctx['generated_at']}")
    L.append(f"- Commit: `{src['git_commit'][:12]}`{dirty}")
    L.append(
        f"- Engine: {ctx['engine'] or 'unknown'}; {'nodes ' + str(s['nodes']) if s.get('nodes') else 'depth ' + str(s['depth'])}, multipv {s['multipv']}; "
        f"config override: {'`' + canonical(s['config']) + '`' if s['config'] else 'none'}"
    )
    L.append(
        f"- Games: {len(ctx['game_ids'])} requested, {len(ctx['compared'])} compared, "
        f"{len(ctx['skipped'])} skipped (list: `{ctx['games_file']}`)"
    )
    exc = a["excluded"]
    L.append(
        f"- Plies: {len(ctx['records'])} aligned, {n} scored, {sum(exc.values())} excluded "
        f"({', '.join(f'{k} {v}' for k, v in sorted(exc.items())) or 'none'})"
    )
    L.append("")

    L.append("## Headline")
    L.append("")
    rows = [
        ["Exact agreement", f"{pct(ratio(a['exact'], n))} ({a['exact']}/{n})"],
        ["Within one step", f"{pct(ratio(a['near'], n))} ({a['near']}/{n})"],
        [
            "Brilliant precision / recall",
            f"{num(pl['brilliant']['precision'], 2)} / {num(pl['brilliant']['recall'], 2)}",
        ],
        [
            "Great precision / recall",
            f"{num(pl['great']['precision'], 2)} / {num(pl['great']['recall'], 2)}",
        ],
        [
            "Brilliant per 100 moves (app / ours)",
            f"{num(a['per_100']['brilliant']['app'], 2)} / {num(a['per_100']['brilliant']['ours'], 2)}",
        ],
        [
            "Great per 100 moves (app / ours)",
            f"{num(a['per_100']['great']['app'], 2)} / {num(a['per_100']['great']['ours'], 2)}",
        ],
        ["Accuracy mean abs. difference", f"{num(mad, 2)} (n={len(acc)}, max {num(max_abs, 2)})"],
        ["Accuracy bias (ours - app)", "-" if bias is None else f"{bias:+.2f}"],
        [
            "Best move = app's suggestion",
            f"{pct(summary['best_move_agreement']['rate'])} "
            f"({a['best_move']['agree']}/{a['best_move']['compared']} plies where the app recorded one)",
        ],
    ]
    L += table(["Metric", "Value"], rows)
    L.append("")
    L.append(
        "Per-100 rates use scored plies as the denominator. Within one step uses the scale "
        "best > excellent > good > inaccuracy > mistake > blunder; book, brilliant, great and miss "
        "must match exactly. Our `forced` counts as best and `great_find` as great."
    )
    L.append("")

    L.append("## Confusion matrix (rows = app, columns = ours)")
    L.append("")
    cols = LABELS + a["our_extra"]
    rows = []
    for row in LABELS:
        counts = a["confusion"][row]
        total = sum(counts.values())
        rows.append(
            [f"**{row}**"]
            + [(f"**{counts[c]}**" if c == row and counts[c] else (counts[c] or ".")) for c in cols]
            + [total]
        )
    col_totals = [sum(a["confusion"][r][c] for r in LABELS) for c in cols]
    rows.append(["**total**"] + col_totals + [n])
    L += table(["app \\ ours"] + cols + ["total"], rows, "l" + "r" * (len(cols) + 1))
    L.append("")

    L.append("## Per label")
    L.append("")
    rows = [
        [lab, pl[lab]["app_count"], pl[lab]["our_count"], pl[lab]["tp"],
         num(pl[lab]["precision"]), num(pl[lab]["recall"]), num(pl[lab]["f1"])]
        for lab in LABELS
    ]
    L += table(["label", "app", "ours", "both", "precision", "recall", "F1"], rows, "lrrrrrr")
    L.append("")

    L.append("## Accuracy")
    L.append("")
    rows = [
        [r["game"], r["side"], num(r["app"], 1), num(r["ours"], 1),
         "-" if r["diff"] is None else f"{r['diff']:+.1f}"]
        for r in ctx["accuracy"]
    ]
    L += table(["game", "side", "app", "ours", "ours - app"], rows, "llrrr")
    L.append("")

    L.append("## Per game")
    L.append("")
    by_game = defaultdict(list)
    for r in scored:
        by_game[r["game"]].append(r)
    rows = []
    for gid, (labels, entry, source) in ctx["compared"].items():
        g = by_game.get(gid, [])
        ex = sum(r["app"] == r["ours"] for r in g)
        ne = sum(within_one(r["app"], r["ours"]) for r in g)
        rows.append(
            [gid, len(entry["result"]["plies"]), len(g), pct(ratio(ex, len(g))),
             pct(ratio(ne, len(g))), source, num(entry.get("review_seconds"), 1)]
        )
    L += table(["game", "plies", "scored", "exact", "within one", "source", "review s"], rows, "lrrrrlr")
    L.append("")

    if ctx["skipped"]:
        L.append("## Skipped games")
        L.append("")
        L += table(["game", "reason"], [[g, why] for g, why in ctx["skipped"].items()])
        L.append("")

    excluded_recs = [r for r in ctx["records"] if r["app"] is None]
    if excluded_recs:
        L.append("## Excluded plies")
        L.append("")
        L.append(
            f"{len(excluded_recs)} {'ply is' if len(excluded_recs) == 1 else 'plies are'} not scored: "
            + ", ".join(f"{k} {v}" for k, v in sorted(exc.items()))
            + f". Our label is one of the collector's candidates for {a['uncertain_guess_hits']} of the "
            f"{exc.get('uncertain', 0)} uncertain ones."
        )
        L.append("")
        rows = [[r["game"], r["ply"], f"{r['move']} {r['san']}", r["app_raw"], r["ours"], r["rule"]]
                for r in excluded_recs]
        L += table(["game", "ply", "move", "app label", "ours", "rule"], rows, "lrllll")
        L.append("")

    L.append(f"## Mismatches by rule ({len(mismatches)})")
    L.append("")
    if mismatches:
        rows = []
        for rule, cnt in rule_counts.most_common():
            pairs = Counter(f"{r['app']} -> {r['ours']}" for r in mismatches if r["rule"] == rule)
            rows.append([f"`{rule}`", cnt, ", ".join(f"{p} x{c}" for p, c in pairs.most_common(6))])
        L += table(["rule", "mismatches", "app -> ours"], rows, "lrl")
        L.append("")
        order = {gid: i for i, gid in enumerate(ctx["compared"])}
        header = ["game", "ply", "move", "app", "ours", "rule", "precision", "ep_lost", "ep_before",
                  "played_is_best", "our best", "app best", "app eval", "our eval"]
        for rule, cnt in rule_counts.most_common():
            L.append(f"### `{rule}` ({cnt})")
            L.append("")
            group = sorted((r for r in mismatches if r["rule"] == rule),
                           key=lambda r: (order.get(r["game"], 0), r["ply"]))
            rows = []
            for r in group:
                ours = r["ours"] + (f" ({r['miss_kind']})" if r["miss_kind"] else "")
                app_best = r["app_best_san"] or r["app_best_uci"]
                rows.append([r["game"], r["ply"], f"{r['move']} {r['san']}", r["app"], ours, r["rule"],
                             r["precision"], num(r["ep_lost"], 4), num(r["ep_before"], 3),
                             r["played_is_best"], r["our_best"], app_best, r["app_eval"], r["our_eval"]])
            L += table(header, rows, "lrlllllrrlllrr")
            L.append("")
    else:
        L.append("No mismatches.")
        L.append("")
    return "\n".join(L), summary


# --------------------------------------------------------------------------- main


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--url", default="http://127.0.0.1:8095", help="backend base URL")
    p.add_argument("--games", default=str(REPO_ROOT / "tests/calibration/tuning.txt"),
                   help="file with one game id per line (# comments allowed)")
    p.add_argument("--run-name", required=True, help="run directory name under --runs-dir")
    p.add_argument("--depth", type=int, default=18, help="search depth per position (1-40)")
    p.add_argument("--nodes", type=int, default=None,
                   help="node budget per position, replacing --depth")
    p.add_argument("--multipv", type=int, default=3, help="engine lines per position (1-5)")
    p.add_argument("--config", default=None,
                   help="partial ReviewConfig override as JSON, or @path/to/file.json (part of the cache key)")
    p.add_argument("--player-side", choices=("white", "black"), default=None,
                   help="review every game as this side's player (the coach's voice and rating gates; "
                        "part of the cache key)")
    p.add_argument("--games-dir", default=str(REPO_ROOT / "tests/calibration/games"))
    p.add_argument("--runs-dir", default=str(REPO_ROOT / "tests/calibration/runs"))
    p.add_argument("--concurrency", type=int, default=3,
                   help="reviews in flight at once (match the server's MAX_CONCURRENT_REVIEWS)")
    p.add_argument("--poll-interval", type=float, default=0.5, help="seconds between status polls")
    p.add_argument("--timeout", type=float, default=3600, help="seconds allowed per review")
    p.add_argument("--refresh", action="store_true", help="ignore cached results and review again")
    p.add_argument("--offline", action="store_true",
                   help="do not contact the server; use cached results only (engine not checked)")
    p.add_argument("--quiet", action="store_true", help="no progress output on stderr")
    args = p.parse_args(argv)
    if not 1 <= args.depth <= 40:
        p.error("--depth must be between 1 and 40")
    if not 1 <= args.multipv <= 5:
        p.error("--multipv must be between 1 and 5")
    if os.sep in args.run_name or "/" in args.run_name or args.run_name in (".", ".."):
        p.error("--run-name must be a plain directory name")
    args.games = Path(args.games)
    args.games_dir = Path(args.games_dir)
    args.runs_dir = Path(args.runs_dir)
    return args


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        args.config_override = load_config_override(args.config)
        game_ids = read_id_list(args.games)
        if not game_ids:
            raise FatalError(f"{args.games} lists no games")
        source = source_state()
        engine = server_version = None
        if not args.offline:
            try:
                health = http_json("GET", f"{args.url.rstrip('/')}/api/health", timeout=10)
            except HarnessError as e:
                raise FatalError(f"backend not reachable at {args.url}: {e}") from None
            if health.get("status") != "ok":
                raise FatalError(
                    f"backend at {args.url} is {health.get('status')}: {health.get('engine_error')}"
                )
            engine, server_version = health.get("engine"), health.get("version")
        settings = {"depth": args.depth, "multipv": args.multipv, "config": args.config_override}
        if args.nodes:
            settings = {"nodes": args.nodes, "multipv": args.multipv, "config": args.config_override}
        if args.player_side:
            settings["player_side"] = args.player_side
        base_key = {
            "harness_version": HARNESS_VERSION,
            "git_commit": source["git_commit"],
            "backend_diff_sha256": source["backend_diff_sha256"],
            "engine": engine,
            "server_version": server_version,
            **settings,
        }
        run_dir = args.runs_dir / args.run_name
        run_dir.mkdir(parents=True, exist_ok=True)
        reviewer = Reviewer(args, base_key, run_dir)
        t0 = time.monotonic()
        results, skipped = fetch_results(args, game_ids, reviewer)
    except FatalError as e:
        print(f"compare.py: error: {e}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 130

    # Compare in list order.
    compared = {}
    records = []
    for gid in game_ids:
        if gid not in results:
            continue
        labels, entry, src = results[gid]
        reason = check_alignment(labels.get("plies") or [], entry["result"]["plies"])
        if reason:
            skipped[gid] = reason
            continue
        compared[gid] = (labels, entry, src)
        records += compare_game(gid, labels, entry["result"])
    skipped = {gid: skipped[gid] for gid in game_ids if gid in skipped}

    if engine is None:
        engines = {e["result"].get("engine") for _, e, _ in compared.values()}
        engine = ", ".join(sorted(x for x in engines if x)) or None
    ctx = {
        "run_name": args.run_name,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "source": source,
        "engine": engine,
        "settings": settings,
        "games_file": str(args.games),
        "game_ids": game_ids,
        "compared": compared,
        "skipped": skipped,
        "records": records,
        "analysis": analyse(records),
    }
    ctx["accuracy"] = accuracy_rows(compared)
    report, summary = build_report(ctx)
    (run_dir / "report.md").write_text(report + "\n", encoding="utf-8")
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    pl = summary["per_label"]
    acc = summary["accuracy"]
    line = (
        f"[{args.run_name}] games {len(compared)}/{len(game_ids)}"
        f" ({len(skipped)} skipped, {summary['games']['from_cache']} cached)"
        f" | plies scored {summary['plies']['scored']}, excluded {sum(summary['plies']['excluded'].values())}"
        f" | exact {pct(summary['exact_agreement'])} | within-one {pct(summary['within_one_agreement'])}"
        f" | brilliant P {num(pl['brilliant']['precision'], 2)} R {num(pl['brilliant']['recall'], 2)}"
        f" | great P {num(pl['great']['precision'], 2)} R {num(pl['great']['recall'], 2)}"
        f" | acc MAD {num(acc['mad'], 2)} bias {'-' if acc['bias'] is None else format(acc['bias'], '+.2f')}"
        f" | {time.monotonic() - t0:.0f}s | {run_dir / 'report.md'}"
    )
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
