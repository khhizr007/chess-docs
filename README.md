# chess-review research

Private research material for [chess-review](../chess-review), split out of that repository on
2026-10-25 from its `main` at commit `76bcb92`. The app does not depend on anything here.

| Folder | Content |
|---|---|
| `docs/` | Design notes, recovered-rule spec, calibration write-ups (was `chess-review/docs/`) |
| `tests/calibration/` | Reference review labels, captured reviews, split lists, run reports (was `chess-review/tests/calibration/`) |
| `tools/calibrate/` | Calibration and comparison scripts (was `chess-review/tools/calibrate/`) |

Paths inside the docs that start with `backend/`, `frontend/` or `tools/maia`, `tools/sounds` refer
to the app repository.

The scripts keep their old repository-relative paths for data (`tests/calibration/...`). Where they
need the app (its git state, or an example binary built in `backend/target`), they look in
`$CHESS_REVIEW_DIR`, else in `../chess-review` next to this folder.

Per-game run results (`tests/calibration/runs/*/[0-9]*.json`) and captured Chess.com data stay
untracked (see the `.gitignore` files). Never publish this repository: it holds the reference app's
review output and notes on its internals.
