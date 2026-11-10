# Calibration dataset

Ground truth for comparing our review labels with Chess.com Game Review. See
`docs/calibration/agent-instructions.md` for the protocol and `docs/calibration/log.md` for results.

- `games/<id>.pgn`: the game exactly as the public API (`api.chess.com/pub/player/<user>/games/YYYY/MM`)
  returned it.
- `games/<id>.labels.json`: the reference app's per-move labels, in the format given in the
  instructions, plus the additions below.
- `tuning.txt` / `holdout.txt`: the split (see the header comment in each). Never tune on holdout games.
- `runs/<name>/`: harness output (`report.md`, `summary.json`; per-game review JSON is not committed).

## Collection

59 games in two batches, all reviewed with Game Review set to engine **Stockfish**
(`stockfish16 nnue` in the site's settings) at strength **Fast** (depth 18):

- Batch 1 (2026-10-17/18): 20 games. Games whose review already existed were shown again with the
  same accuracy after the engine switch; the rest were reviewed fresh.
- Batch 2 (2026-10-18): 39 games drawn at random (seed 2026) from the October archives of khhizr7,
  boy1956, PeterSouth1954, Hikaru, GothamChess and IMRosen, by source and time control, plus three
  draws; 2,915 moves.
- Batch 3 (2026-10-18): game 185058622904 (khhizr7, a Traxler counter-attack with two Brilliants),
  reported by the owner when our review gave it none. Its labels come straight from the captured
  `/v2/game-review` response (`label_source: "chesscom-capture"`); it is in the tuning split because the
  Brilliant rule was designed on it.
- Batch 4 (2026-10-19): 82 of khhizr7's rapid games (30+ plies, not already in the dataset) in
  `random.Random(2027)` order from the archives 2025/09 to 2026/10, reviewed one after another until
  the batch held 16 Brilliants (15 games). Labels, best moves and evaluations come straight from the
  captured `/v2/game-review` responses (`cc-reviews/<id>.sf.txt`, `label_source: "chesscom-capture"`);
  every played move was checked against the PGN's SAN and every best move for legality. The page
  reviewed each game with engine 10 (Stockfish setting) and every score came back from engine 13
  (Stockfish 18).

- Batch 5 (2026-10-23): 435 games not in the earlier batches, captured the
  same way as batch 4 (engine 10 requested, every score from engine 13), with their own split
  (`batch5-tuning.txt` 305 games, `batch5-holdout.txt` 130; per (selection, band) stratum,
  `random.Random(2030)`, 30% to holdout). The earlier batches are mostly one player at 800–1050 rapid,
  so this batch covers the whole rating range. `tools/calibrate/sample_games.py` samples players from
  the API's country lists plus 45 titled players, and reads their last two monthly archives (73,522
  candidate games, rated standard games of 30+ plies). From these it picks:
  - **strat** (285): 45 games per band of the players' mean rating (<700, 700–1000, 1000–1300,
    1300–1600, 1600–1900, 1900–2200, 2200+; the top two bands came out at 36 and 31), split 50/40/5/5
    rapid/blitz/bullet/daily, `random.Random(2029)`, at most 3 games per player. Use this stratum
    for unbiased label rates.
  - **sac** (150): rapid/blitz games with a move that leaves a piece en prise (value gap ≥ 2) and
    that Stockfish 18 at depth 14 rates within 30 cp of best. This stratum is enriched for
    Brilliants and is not a random sample.

  `tools/calibrate/captures_to_dataset.py` builds the files from the captured frames. It rejects a
  game unless every move matches the PGN, every best move is legal, every score is engine 13 and
  the per-ply labels reproduce the review's tallies (all 435 passed). In total the batch has 33,681
  plies: 73 Brilliant (strat 33, sac 40), 1,308 Great, 824 Blunder and 1,328 Miss. That is three
  times the Brilliants of batches 1–4 (25).

Labels were read move by move from the review panel (label text and icon), and the per-move labels
reproduce the counts table for both players in every game.

## Format additions

| Field | Meaning |
|---|---|
| `label: "forced"` | The app showed "Forced" (only legal or only sensible move). It is not a row of the counts table; the harness scores it as `best`. |
| `label: "uncertain:a/b"` | The label was hidden (the review showed a "Skill" note instead) and the counts table leaves more than one possibility. Excluded from scoring. |
| `hidden` | The note that hid the label, for example `"Skill"`. |
| `label_source: "counts"` | A hidden label recovered from the counts table because only one label was short. |
| `app_best_uci` / `app_best_san` | The green "best move" arrow, when the app drew one. `app_best_san` is filled by `tools/calibrate/fill_best_san.py`. |
| `batch5` | Batch 5 only, numbers and names from the review: `selection` (strat/sac), `time_class`, `band` (0–6), `sac_plies` (the screen's candidate plies), `effective_rating` (Chess.com's per-side "Game Rating"), `phase_accuracy` (accuracy and glyph per phase), `stats` (report-card categories), `eco`, `opening`, `tricky_plies`. |
| `app_eval` | The evaluation shown after the played move, from White's point of view (`+0.25`, `-1.40`, `M3`, `-M2`). `null` on the final move, where the app shows the result instead. |

Rebuild from raw captures with `tools/calibrate/build_dataset.py`, then run `fill_best_san.py` again
(the builder writes `app_best_san: null`).
