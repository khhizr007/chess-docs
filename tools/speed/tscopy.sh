#!/bin/bash
# tscopy.sh <name>... : copy regenerated bindings from the sp mirror into the speed worktree, keeping its line endings.
W=/mnt/c/Users/khhizr/rea_projects/chess-review-wt-speed/frontend/src/api/generated
M=$HOME/work/sp/mirror/frontend/src/api/generated
for n in "$@"; do
  if grep -q $'\r' "$W/$n.ts"; then sed 's/\r*$/\r/' "$M/$n.ts" > "$W/$n.ts"; else tr -d '\r' < "$M/$n.ts" > "$W/$n.ts"; fi
done
