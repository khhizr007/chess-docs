#!/bin/bash
# build-clean.sh <name> <backend-src-dir> : rsync to ~/work/sp/clean-<name>, release build, no patches.
set -euo pipefail
export PATH=$HOME/tools/bin:$HOME/.cargo/bin:$PATH
B=$HOME/work/sp/clean-$1
mkdir -p $B
rsync -a --delete --checksum --exclude target --exclude frontend "$2/" "$B/"
cd $B
CARGO_BUILD_JOBS=4 CARGO_TARGET_DIR=$HOME/cargo-target/sp-clean-$1 cargo build --release -p review-server 2>&1 | tail -1
grep -c 'disk cache loaded' $HOME/cargo-target/sp-clean-$1/release/review-server || true
