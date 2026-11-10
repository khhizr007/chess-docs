#!/bin/bash
# bg.sh <run> <cfg-file|-> [compare args...] : go.sh detached; output in ~/work/sp/<run>.out
mkdir -p $HOME/work/sp
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
setsid nohup bash $D/go.sh "$@" > "$HOME/work/sp/$1.out" 2>&1 < /dev/null &
disown
sleep 3
echo "started $1"
