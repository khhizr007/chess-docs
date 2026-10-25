#!/bin/bash
# det.sh : is a node-budget review reproducible across fresh servers and pool sizes?
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
O=$HOME/work/sp/det
mkdir -p $O
bash $D/build-clean.sh new /mnt/c/Users/khhizr/rea_projects/chess-review-wt-speed/backend
head -3 $HOME/work/sp/t23/games.txt > $O/games.txt
BODY='{"nodes":600000,"multipv":2}'
BIN=$HOME/cargo-target/sp-clean-new/release/review-server
POOL=4 python3 $D/e2e2.py n600a $BIN $O/a $O/games.txt "$BODY"
POOL=3 python3 $D/e2e2.py n600b $BIN $O/b $O/games.txt "$BODY"
sleep 1
