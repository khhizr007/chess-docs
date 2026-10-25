# Why our game reviews are slower than Chess.com's

Study of 2026-10-25, branch `claude/review-speed-analysis`. App code at chess-review `main` b95562f.
Tools and raw results: `tools/speed/`.

## 1. Answer

On the same games, Chess.com finishes a review in 13–15 s; we take 19–31 s on this laptop. Almost all
of our time is engine search: about **530 ms per ply** for us against **about 107 ms per ply** for
Chess.com. The gap has four causes, largest first:

| # | Cause | Our setting | Chess.com (decoded from libcee 4.10.15) | Measured effect |
|---|---|---|---|---|
| 1 | Search budget per position | depth 18, MultiPV 3 (median 1.12 M nodes, worst 11 s) | fixed node budget, MultiPV 2 (STANDARD = 600 k nodes) | 1.75 s vs 0.88 s per position: **2.0×** |
| 2 | Engines per review | 4 engines × 1 thread (`ENGINE_POOL_SIZE` default `min(4, cpus/2)`) | engine pool, one worker per engine, size set by their servers | 107 ms/ply needs about 8–10 of our cores' worth of search (inference) |
| 3 | Positions searched | every position, book included | about 18% of positions come back at depth 25–34, so they are precomputed, not searched | ~10–18% of the work |
| 4 | Scheduling | `futures::buffered(4)`: in-order stream, one slow search stalls the other engines | shared task queue, the first free engine takes the next position | **−7 to −12%** wall time when fixed, identical output |

Small or no effect: the coach's threat searches (0 to −3% when switched off), clearing the hash
before each search (a warm hash was not faster at fixed depth), and the human-move model (not
configured on the user's backend). Two threads per engine made reviews **slower** (+12 to +45%).

## 2. How Chess.com searches (decoded)

All from `libcee.so` 4.10.15 (APK), decompiled with Ghidra (project `~/work/chesscom/ghidra`, scripts
`~/work/re-great/ghidra_scripts`). Function addresses below are Ghidra's (file address + 0x100000).

- `TEP::api::get_options_from_game_review_search_settings` (0x14f27f0) builds the Game Review search
  options: **`num_lines = 2`** (MultiPV 2), a **node limit by Strength**, no depth limit, and a
  null-move search of **40,000 nodes, MultiPV 1**.
- The node tables (`get_nodes_for_strength` 0x14f2774, tables at file 0x6d73d0 / 0x6dcbc8):

  | Strength | Nodes |
  |---|---|
  | FAST | 150,000 |
  | STANDARD | 600,000 |
  | DEEP | 1,600,000 |
  | MAXIMUM | 6,250,000 |

  `get_nodes_for_preset` (0x14f27ac) adds PLAY_BOT_STANDARD 80,000 and PLAY_BOT_FAST 50,000.
- `EvaluateGameRequest` (protobuf) has `stream_progress_updates`, `reduce_nodes_on_successive_searches`,
  `reduce_nodes_on_successive_multisearch_searches`, `enable_soft_nodes_limit` and `engine_id`; its
  response carries `progress` and `evaluated_positions_count`. The captured `/v2/game-review` frames
  are these progress messages, one per ply.
- `TEP::ParallelEval::ParallelEval` (0x15f9840) creates one `EvalWorker` per engine in the
  `BorrowingEnginePool`. Each `EvalWorker::worker` (0x15f8e8c) loops on a shared
  `ThreadsafeQueue<EvalTask>::wait_and_pop`, so whichever engine is free takes the next position.
- `TEP::engine::Engine::reset_state` (0x139fabc) sends `ucinewgame`, `setoption name Clear Hash` and
  `setoption name ClearHash`. Its callers were not traced (calls go through the PLT/vtables), so it is
  **not known** whether Chess.com clears the hash per search or per game.
- Thread count, hash size and pool size are not in the library; they are set by Chess.com's servers.

Which Strength the website uses: Chess.com reports a depth for every score. Against SF 18 at each
budget (3 games, 137 positions, fresh hash, 1 thread), STANDARD matches best:

| Budget | Our depth − Chess.com depth (median) | Same depth |
|---|---|---|
| FAST 150 k | −3 | 4–5% |
| **STANDARD 600 k** | **−1** | **15–21%** |
| DEEP 1.6 M | +2 | 10% |

Exact scores never matched (2–6% of positions for every budget, warm or cold hash, forward or
reverse order), as found before in `calibration/mismatch-analysis.md`. Chess.com probably runs
several threads per engine, which makes its scores non-reproducible. The STANDARD match is therefore
a best fit, not a proof. 97% of the 285,688 captured scores carry engine id 13 (SF 18 NNUE).

### Precomputed positions

Chess.com's reported depth by ply over all 577 captured reviews (`tools/speed/ccdepth.cjs`):

| Plies | Depth p10/p50/p90 | Depth ≥ 25 |
|---|---|---|
| 1–10 | 20 / 29 / 32 | 89% |
| 11–20 | 16 / 18 / 29 | 21% |
| 21–40 | 15 / 18 / 20 | 1% |
| 41–60 | 16 / 18 / 20 | 1% |
| 61–80 | 16 / 18 / 21 | 4% |
| 81+ | 16 / 19 / 23 | 9% |

97% of Book moves and 18% of all positions come back at depth ≥ 25. SF 18 reaches only depth 16–17
on those opening positions with 600 k nodes, so these scores are not from the live search: they most
likely come from a store of deep evaluations (deep scores late in the game may instead be easy
endgame searches). We search every position, Book positions included.

## 3. How we search

`backend/crates/review-server/src/analysis/mod.rs::analyse_positions`, engine in `engine/{pool,uci}.rs`:

1. One search per position, `go depth 18`, `MultiPV 3`, after `ucinewgame` + `setoption name Clear
   Hash` + `isready` (so results do not depend on which process ran them).
2. One null-move threat search per coached position, `go depth 10`, MultiPV 1, in the same stream.
3. A second phase, started only after phase 1 ends: a threat search after the best move wherever the
   played move was not best.
4. The pool has `min(4, cpus/2)` engines (4 on the 16-thread laptop, so 4 of 8 physical cores),
   1 thread and 64 MB hash each. Each SF 18 process uses about 370 MB of RAM (NNUE + hash).
5. Both phases run through `futures::stream::iter(..).buffered(pool)`. `Buffered` counts finished
   results that wait behind an earlier, unfinished search as in flight (`FuturesOrdered::len` =
   in progress + queued outputs, futures-util 0.3.34 `futures_ordered.rs:128`), so one slow search
   stops new searches from starting.

Classification reads only `lines[0]` and `lines[1]` (`facts.rs` lines 238, 264, 490); the third line
is shown in the UI only.

## 4. Measurements

Machine: i7-11800H (8 cores, 16 threads), WSL, SF 18 (`~/tools/sf18/sf18`, 1.15 M nps single thread
on `bench`). Games: 8 captured reviews spread over game length (`tools/speed/bench-games.json`).

### 4.1 Cost of one search (`bench.py`, 450 positions, 1 thread, 64 MB)

Runs went 4–6 configurations at a time, so absolute times include that load; compare rows, not
against the `bench` nps.

| Search | Mean | p90 | Max | Nodes p50 |
|---|---|---|---|---|
| **Ours: depth 18, MultiPV 3, cleared** | **1,752 ms** | 2,841 ms | 11,312 ms | 1.12 M |
| depth 18, MultiPV 3, warm hash | 1,934 ms | 2,966 ms | 15,058 ms | 1.15 M |
| depth 18, MultiPV 2 | 1,289 ms | 2,124 ms | 11,718 ms | 0.76 M |
| depth 18, MultiPV 1 | 705 ms | 1,226 ms | 6,424 ms | 0.36 M |
| Chess.com FAST, 150 k, MultiPV 2 | 254 ms | 316 ms | 1,074 ms | 0.15 M |
| **Chess.com STANDARD, 600 k, MultiPV 2** | **880 ms** | 1,066 ms | 1,407 ms | 0.60 M |
| Chess.com DEEP, 1.6 M, MultiPV 2 | 1,991 ms | 2,568 ms | 3,116 ms | 1.60 M |
| Our threat search, depth 10 | 22 ms | 35 ms | 94 ms | 3 k |
| Chess.com null-move search, 40 k | 78 ms | 103 ms | 136 ms | 40 k |

MultiPV 3 costs 2.5× MultiPV 1 at the same depth. A depth limit also has a long tail (one position
took 11 s); a node limit caps every search.

### 4.2 Whole reviews (`e2e.py`, this checkout's release build, one review at a time)

Wall time from POST to `completed`, fresh server per variant (empty analysis cache).

| Variant | 51 plies | 57 plies | 37 plies | Change |
|---|---|---|---|---|
| **Default (pool 4, depth 18, MultiPV 3)** | 31.5 / 28.9 / 31.2 s | 27.2 / 24.5 / 25.0 s | 20.2 / 19.9 / 19.4 s | — |
| MultiPV 2 | 21.4 s | 18.4 s | 15.8 s | −20 to −30% |
| MultiPV 1 | 14.8 s | 9.3 s | 9.7 s | −51 to −64% |
| Coach threat searches off | 29.6 s | 25.0 s | 19.8 s | 0 to −3% |
| 2 threads per engine | 34.1 s | 29.2 s | 28.7 s | +12 to +45% |
| `buffer_unordered` (experiment, `patch_unordered.py`) | 27.5 s | 22.8 s | 18.2 s | −7 to −12% vs the same batch |
| Chess.com, same games (captured) | 14.0 s | 13.0 s | 13.3 s | |

Changes are against the mean of the three default runs; the `buffer_unordered` row is against the
default run of its own batch (31.2 / 25.0 / 19.4 s). The `buffer_unordered` build produced
byte-identical reviews (same SHA-256 of `plies`), as expected: every search is deterministic, only
the order of completion changes.

Chess.com over all 577 captures (`timing.cjs`): wall = **11.4 s + 107 ms × plies** (least squares;
median 14.0 s at median 65 plies). The 11.4 s is the capture's page load, connection and queueing;
the 107 ms/ply is the engine rate.

### 4.3 Schedule model (`sim.cjs`)

Replaying the measured per-search times through both schedulers (8 games, 442 plies):

| Search and pool | `buffered` (today) | Free-engine queue |
|---|---|---|
| Ours, pool 4 | 560 ms/ply | 472 ms/ply |
| Ours, pool 8 | 336 ms/ply | 260 ms/ply |
| STANDARD 600 k + 40 k null, pool 4 | 273 ms/ply | 260 ms/ply |
| STANDARD 600 k + 40 k null, pool 8 | 142 ms/ply | 131 ms/ply |

The model's 560 ms/ply matches the measured 450–600 ms/ply of §4.2. Pool 8 was not run end to end:
8 SF 18 processes need about 3 GB and the host was low on memory.

## 5. Other findings

- **A dead engine fails the whole review.** 3 of the 7 default runs of game 1009533214 failed with
  `engine process exited unexpectedly`, all engines closing their stdout at once; its 5 runs with
  other settings passed. Each failure was the first review of a batch started in the background from
  `wsl -e`, and 4 foreground runs passed, so the trigger was most likely the test harness (WSL can
  kill detached jobs of a closed launcher); the first one also coincided with a host memory-pressure
  alarm. But the server does not retry or respawn: a failed main search ends the review
  (`analysis/mod.rs`, `Err(e) => return Err(ReviewError::Engine(e))`), and the user must start
  again, which doubles the wait.
- **Memory.** Each SF 18 process holds about 370 MB, so the default pool needs about 1.5 GB. On a
  low-memory host, engines can fail to start or die.
- **Repeat reviews** of the same game hit the in-memory LRU (`ANALYSIS_CACHE_ENTRIES`, 20,000) and
  are fast; it is lost on restart.

## 6. What would close the gap

Each item is independent; numbers are from §4.

1. **Search a node budget with MultiPV 2** (e.g. 600 k, Chess.com's STANDARD): about −50% engine
   time and no 11 s outliers. Needs a `SearchLimit::Nodes` variant and a full re-calibration
   (`gr-run.sh`, all labels): the evaluations change, and the depth-18 choice was made for parity.
   STANDARD's depths are close to Chess.com's own (§2), so agreement may hold or improve; this is not
   measured yet.
2. **Use more engines.** Default the pool to the physical core count (8 here) and keep 1 thread each.
   Model: −40%. Watch memory (≈370 MB per engine).
3. **Replace `buffered` with a free-engine queue** (`buffer_unordered` plus index sort, as in
   `patch_unordered.py`): −7 to −12%, same output.
4. **Do not search what is already known.** Book positions need no live search for the Book label;
   a persistent evaluation cache (disk, keyed by FEN + search settings) would also make repeat
   reviews and common openings free.
5. **Stream partial results and retry a crashed engine once** before failing the review.

Model for 1 + 2 + 3: about 131 ms/ply (§4.3), close to Chess.com's 107 ms/ply.

## 7. Reproducing

All scripts are in `tools/speed/` (Node on Windows, Python 3 + SF 18 in WSL).

```sh
# Captured Chess.com reviews (raw frames in WSL ~/work/chesscom/oracle/captures/raw):
node scan.cjs <captures>       # engine ids and depths of every captured score
node timing.cjs <captures>     # wall time vs plies
node games.cjs <captures> 8    # bench-games.json (UCI moves per game)
node ccdepth.cjs               # Chess.com depth by ply (needs tests/calibration/cc-reviews)

# Engine bench (WSL); run at most ~4 at a time: each SF 18 holds ~370 MB.
python3 bench.py bench-games.json ours_d18_mpv3_clear out/ours_d18_mpv3_clear.jsonl
node summ.cjs out ; node match.cjs out ; node sim.cjs out ours_d18_mpv3_clear threat_d10_clear 4

# Whole reviews against a release build of backend/ (port 8091), from backend/:
BENCH_GAMES=../tools/speed/bench-games.json python3 ../tools/speed/e2e.py default_pool4 mpv2_pool4
```

Ghidra decompiles: `~/work/re-great/out/speed{1,2,3}` (pattern files `out/pats_speed*.txt`).


## 8. Fixes built (2026-10-26)

chess-review branch `claude/review-speed` (worktree `chess-review-wt-speed`), on main b95562f:

| Commit | Change | Output |
|---|---|---|
| 1bae87d | free-engine queue (`search_all`, replaces `buffered`) | byte-identical |
| 8c19811 | default pool `min(8, cpus/2)` (was 4) | byte-identical |
| dcc3d9b | optional `SearchLimit::Nodes` (`"nodes"` in the request); default unchanged | unchanged by default |

Whole reviews, 8 bench games, fresh server, real searches (`t23.sh`, `tnodes.sh`):

| Build and search | Total | vs main |
|---|---|---|
| main, pool 4, depth 18 MultiPV 3 | 255 s | — |
| main, pool 8 | 223 s | −12% |
| queue, pool 4 | 242 s | −5% |
| **queue, pool 8 (the new default)** | **159 s** | **−38%** |
| queue, pool 8, 600 k nodes, MultiPV 2 | 89 s | −65% |
| queue, pool 8, 600 k nodes, MultiPV 3 | 87 s | −66% |
| queue, pool 8, 1.1 M nodes, MultiPV 3 | 151 s | −41% |

All 8 reviews had the same SHA-256 in every depth-18 build. Node-budget reviews were identical
from fresh servers with pool 4 and pool 3 (`det.sh`).

Labels on the 142 original games (`sp-run.sh`, coach threat searches off; baseline `sp-base142`
equals fresh depth-18 reviews, `cachecheck.cjs`):

| Run | Exact | Brilliant P/R | Great P/R | Blunder F1 | Mistake F1 | Accuracy MAD |
|---|---|---|---|---|---|---|
| depth 18, MultiPV 3 (baseline) | 71.9% | 0.875 / 0.84 | 0.817 / 0.751 | 0.848 | 0.698 | 4.17 |
| depth 18, MultiPV 2 | 72.4% | 0.846 / 0.88 | 0.823 / 0.787 | 0.841 | 0.688 | 4.42 |
| 600 k, MultiPV 2 | 73.0% | 0.840 / 0.84 | 0.827 / 0.776 | 0.826 | 0.701 | 4.48 |
| 600 k, MultiPV 3 | 72.3% | 0.840 / 0.84 | 0.831 / 0.763 | 0.856 | 0.694 | 4.36 |
| 1.1 M, MultiPV 3 | 72.1% | 0.840 / 0.84 | 0.823 / 0.751 | 0.855 | 0.691 | 4.21 |

No search change kept every metric at or above the baseline. Any change moves 12–20% of labels
(1,057–1,753 plies), almost all to a neighbouring grade, and gains and losses nearly cancel
(`flips.cjs`). The Brilliant precision drop is one ply in every variant (185221110711 ply 72
Rxc3, Best for Chess.com): at depth 18 the second line is 71 cp worse, with node budgets only
20 cp, which crosses a Brilliant gate. One depth-limited review (184110410320, depth 18
MultiPV 2) hit the 60 s per-search timeout; node budgets cannot.

The search setting therefore stays depth 18, MultiPV 3 until a node budget is accepted with
these trade-offs, or passes on all 577 games.
