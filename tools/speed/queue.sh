#!/bin/bash
# queue.sh : run several 142-game variants back to back (each line: <run> <compare args...>).
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
export GAMES=/home/khhizr/work/gr/all.txt POOL=6 CONC=3 CACHE=/home/khhizr/work/sp/cache2.jsonl
while read -r run args; do
  [ -z "$run" ] && continue
  bash $D/go.sh "$run" cfg-nothreat.json $args > "$HOME/work/sp/$run.out" 2>&1 < /dev/null
done < "$1"
sleep 1
