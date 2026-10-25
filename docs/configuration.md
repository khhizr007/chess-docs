# Configuration

## Backend (environment variables)

| Variable | Default | Meaning |
|---|---|---|
| `STOCKFISH_PATH` | `stockfish` found on `PATH` | UCI engine executable. Without one the server starts in "degraded" mode: import and parsing work, reviews return 503. |
| `BIND_ADDR` | `127.0.0.1:8080` | Listen address |
| `ENGINE_POOL_SIZE` | half the CPUs, 1–4 | Engine processes, which is also the maximum number of parallel searches |
| `ENGINE_THREADS` | `1` | `Threads` per engine process |
| `ENGINE_HASH_MB` | `64` | `Hash` per engine process |
| `ENGINE_SEARCH_TIMEOUT_SECS` | `60` | Hard limit per position |
| `ANALYSIS_CACHE_ENTRIES` | `20000` | LRU cache of position analyses (0 disables it) |
| `OPENINGS_DIR` | `./data/openings` if present | Opening TSVs. Without them, no move is classified as Book. |
| `MAX_CONCURRENT_REVIEWS` | `2` | Reviews that run at the same time; others queue |
| `MAX_STORED_REVIEWS` | `100` | Finished reviews kept in memory |
| `STATIC_DIR` | unset | Serve a built frontend (`frontend/dist`) from the backend |
| `CORS_ORIGIN` | unset | Allowed browser origin. Only needed when the frontend is served from another origin without the Vite proxy. |
| `MAIA_COMMAND` | unset | Command that starts the optional Maia-2 sidecar (see below). Without it the coach does not judge how hard a move was to find. |
| `RUST_LOG` | `info,tower_http=warn` | Log filter |

**CPU budget.** CPU use is about `ENGINE_POOL_SIZE × ENGINE_THREADS` cores while a review runs. On a
4-core machine the defaults (2 × 1) keep the desktop responsive. Increase them on bigger machines for
faster reviews.

## Review rules

The defaults are the recovered constants (`GET /api/config/defaults`). A review request may pass
`config` to override them, for example `{"great_find": {"critical_min_alternative_loss": 0.15}}` merged over
the defaults. The fields are documented in `backend/crates/review-core/src/config.rs`.

`coach.threat_search_depth` (default 10) sets the depth of the coach's null-move threat search, which
finds what a move threatens and what threat it stops. `{"coach": {"threat_search_depth": 0}}` turns it
off; classifications do not change, only the coach's notes. `coach.best_threat_search` (default
`true`) also runs it after the engine's best move wherever the played move was not that move, so the
coach can say what the better move would have threatened.

`coach.rating_gates` (default `true`) leaves out ideas above the player's level: each coach tag has a
`min_rating` in `backend/crates/review-server/src/coach/text/en.toml` (tactics and development are
said to everyone, activity from about 600–900, pawn structure from about 900–1100). The rating is the
player's Elo from the PGN when the request names `player_side`, else the rating the review uses for
expected points (the higher Elo plus 200, at least 1000). When the only idea of a move is gated, the
coach says nothing about it.

## Frontend

| Variable | Default | Meaning |
|---|---|---|
| `VITE_BACKEND_URL` | `http://127.0.0.1:8080` | Where the Vite dev server proxies `/api` |

## Maia-2 (optional)

[Maia-2](https://github.com/CSSLab/maia2) (MIT) predicts the moves human players of a given rating
make. With it, the coach says when the best move was hard to find at the player's level (P(best) below
0.10) and leads with the safety check when a Mistake or Blunder was a natural move (P(played) at least
0.30). It runs as a separate Python process, like Stockfish, and is not bundled.

`maia2` 0.10.0 pins exact versions (torch 2.8.0, numpy 2.1.3, pandas 2.2.3) that have wheels only up
to Python 3.13, so use Python 3.12 or 3.13. Where the system Python is newer, [uv](https://docs.astral.sh/uv/)
can provide one (installing `maia2 --no-deps` next to current torch, numpy and pandas on Python 3.14
also works: it gave the same predictions in our check):

```
uv venv --python 3.12 ~/maia312
uv pip install --python ~/maia312/bin/python torch==2.8.0 --index-url https://download.pytorch.org/whl/cpu
uv pip install --python ~/maia312/bin/python maia2==0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu --index-strategy unsafe-best-match
MAIA_COMMAND="$HOME/maia312/bin/python tools/maia/maia_sidecar.py --type rapid" ./target/release/review-server
```

On the first start the sidecar downloads the weights (the rapid model is 280 MB, from the location
the Maia-2 authors publish) into `~/.cache/maia2` (`--models-dir`). It uses 2 CPU threads by default
(`--threads`). The model is asked only from move 11 on: Maia-2 was trained without the first ten
moves of each game, and its opening predictions are not sound. If the sidecar fails to start or
answer, reviews go on without it (a warning is logged).

## Installing Stockfish

The server's Stockfish is GPL-3.0 and is **not** bundled. Install it from your package manager
(`apt install stockfish`, `brew install stockfish`) or from https://stockfishchess.org/download/.
Then point `STOCKFISH_PATH` at the binary. Any UCI engine with `MultiPV` support works. The
reference application used Stockfish 16.1.

The live engine for sidelines is a separate, bundled WebAssembly build (Stockfish 19 Lite,
`frontend/public/engine/`, see `THIRD_PARTY.md`). It runs in the reader's browser, needs no
configuration, and adds no work to the server (`docs/explore-mode.md`).
- **How it is served.** With `STATIC_DIR`, the backend serves it from `frontend/dist/engine/`.
- **Changing the server.** Any server that serves `.wasm` as `application/wasm` works.
