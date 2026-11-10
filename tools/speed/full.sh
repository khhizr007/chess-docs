#!/bin/bash
# full.sh : all 577 games with the new default (600k nodes, MultiPV 3), coach threat searches off
# (as in the m2-final baseline). Output: ~/work/sp/sp-full-n600m3.out
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
export GAMES=/home/khhizr/work/gr/allgames.txt POOL=6 CONC=3 CACHE=/home/khhizr/work/sp/cache2.jsonl
setsid nohup bash $D/go.sh sp-full-n600m3 cfg-nothreat.json --nodes 600000 --multipv 3 \
  > $HOME/work/sp/sp-full-n600m3.out 2>&1 < /dev/null &
disown
sleep 3
echo started
