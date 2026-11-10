#!/bin/bash
# sp-run.sh <run> [extra compare.py args...]
# Builds $SRC (a chess-review backend dir) with the engine disk cache patch, starts it on $PORT and
# runs compare.py over $GAMES. Env: SRC, TARGET (cargo target name), GAMES, POOL, CACHE (cache file;
# "none" disables), CONC, PORT, APP (checkout for compare.py's git key).
set -euo pipefail
RUN="$1"; shift
RES=/mnt/c/Users/khhizr/rea_projects/chess-review-research
APP="${APP:-/mnt/c/Users/khhizr/rea_projects/chess-review-wt-speed}"
SRC="${SRC:-$APP/backend}"
TARGET="${TARGET:-sp}"
PORT="${PORT:-8097}"
POOL="${POOL:-8}"
CACHE="${CACHE:-$HOME/work/gr/engine-cache.jsonl}"
GAMES="${GAMES:-$HOME/work/gr/allgames.txt}"
W=$HOME/work/sp
export PATH=$HOME/work/phase0/gitwrap:$HOME/tools/bin:$HOME/.cargo/bin:$PATH
mkdir -p $W
B=$W/backend-$TARGET
rsync -a --delete --checksum --exclude target --exclude frontend "$SRC/" "$B/"
python3 $HOME/work/p4/diskcache.py "$B" >/dev/null
cd "$B"
CARGO_BUILD_JOBS=${CARGO_BUILD_JOBS:-4} CARGO_TARGET_DIR=$HOME/cargo-target/$TARGET \
  cargo build --release -p review-server 2>&1 | tail -1
export STOCKFISH_PATH=$HOME/tools/sf18/sf18 ENGINE_POOL_SIZE=$POOL BIND_ADDR=127.0.0.1:$PORT
export ANALYSIS_CACHE_ENTRIES=600000
if [ "$CACHE" != none ]; then export ANALYSIS_CACHE_FILE=$CACHE; fi
$HOME/cargo-target/$TARGET/release/review-server > $W/server-$RUN.log 2>&1 &
PID=$!
trap "kill $PID 2>/dev/null || true" EXIT
for i in $(seq 1 120); do curl -sf http://127.0.0.1:$PORT/api/health >/dev/null && break; sleep 1; done
grep -m1 'disk cache loaded' $W/server-$RUN.log | sed 's/\x1b\[[0-9;]*m//g' || true
cd $RES
CHESS_REVIEW_DIR=$APP python3 tools/calibrate/compare.py --url http://127.0.0.1:$PORT --games "$GAMES" \
  --run-name "$RUN" --concurrency "${CONC:-2}" --quiet --timeout 14400 "$@" | tail -2
sleep 1
