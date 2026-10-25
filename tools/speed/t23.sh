#!/bin/bash
# t23.sh : time main vs new binaries (fixes 2+3) on the 8 bench games, real searches, default settings.
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
O=$HOME/work/sp/t23
mkdir -p $O
cd $D
node -e "require('./bench-games.json').forEach(g=>console.log(g.id))" 2>/dev/null > $O/games.txt || \
  python3 -c "import json;[print(g['id']) for g in json.load(open('bench-games.json'))]" > $O/games.txt
for v in "$@"; do
  case $v in
    main4) BIN=main; P=4 ;;
    main8) BIN=main; P=8 ;;
    new4) BIN=new; P=4 ;;
    new8) BIN=new; P=8 ;;
  esac
  POOL=$P python3 $D/e2e2.py $v $HOME/cargo-target/sp-clean-$BIN/release/review-server $O/$v $O/games.txt \
    | tee -a $O/times.jsonl
done
sleep 1
