#!/bin/bash
# tnodes.sh : whole-review time of the new binary (pool 8, free-engine queue) per search setting.
D=/mnt/c/Users/khhizr/rea_projects/chess-review-research/tools/speed
O=$HOME/work/sp/tn
mkdir -p $O
BIN=$HOME/cargo-target/sp-clean-new/release/review-server
G=$HOME/work/sp/t23/games.txt
POOL=8 python3 $D/e2e2.py n600m2 $BIN $O/n600m2 $G '{"nodes":600000,"multipv":2}' | tee -a $O/times.jsonl
POOL=8 python3 $D/e2e2.py n600m3 $BIN $O/n600m3 $G '{"nodes":600000,"multipv":3}' | tee -a $O/times.jsonl
POOL=8 python3 $D/e2e2.py n1100m3 $BIN $O/n1100m3 $G '{"nodes":1100000,"multipv":3}' | tee -a $O/times.jsonl
sleep 1
