#!/bin/bash
# launch-q.sh <queue-file-under-tools/speed> : run queue.sh detached.
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
tr -d '\r' < "$D/$1" > "$HOME/work/sp/$1"
setsid nohup bash $D/queue.sh "$HOME/work/sp/$1" > "$HOME/work/sp/$1.log" 2>&1 < /dev/null &
disown
sleep 3
echo "started $1"
