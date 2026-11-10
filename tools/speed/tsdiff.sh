#!/bin/bash
# tsdiff.sh : show ts-rs bindings regenerated in the sp mirror that differ from the speed worktree.
M=$HOME/work/sp/mirror
W=/mnt/c/Users/khhizr/rea_projects/chess-review-wt-speed
cd $M
for f in frontend/src/api/generated/*.ts; do
  if ! diff -q <(tr -d '\r' < "$f") <(tr -d '\r' < "$W/$f") >/dev/null; then
    echo "DIFF $f"; diff <(tr -d '\r' < "$W/$f") <(tr -d '\r' < "$f")
  fi
done
