#!/bin/bash
# go.sh <run> <cfg-file|-> [extra compare.py args...]  (env passes through to sp-run.sh)
RUN="$1"; CFG="$2"; shift 2
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
cd ~
if [ "$CFG" = - ]; then
  timeout 20000 bash $D/sp-run.sh "$RUN" "$@" 2>&1 | tail -6
else
  timeout 20000 bash $D/sp-run.sh "$RUN" --config "$(tr -d '\r\n' < $D/$CFG)" "$@" 2>&1 | tail -6
fi
sleep 1
