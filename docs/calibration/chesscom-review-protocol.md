# Chess.com Game Review: what the review page receives (captured October 2026)

This records what the live Chess.com web client sends and receives for a Game Review. It was
captured on 2026-10-18 from the analysis page of the account owner's own games (web client package
`analysis/2026.10.2`, CEE version `1.198.16`), by reading the page's own WebSocket traffic and the
protobuf schemas embedded in its JavaScript bundle. Nothing was sent to Chess.com beyond what the
page itself sends when a review is opened.

## Transport

- The review is requested over a binary WebSocket, `wss://analysis.chess.com/v2/game-review`
  (feature flag `game_review_ceac_idl_migration`; the older JSON socket
  `/v1/legacy/game-analysis` is no longer used by this account).
- Request: `chesscom.ceac.v2.GameReviewRequest`. Response: `chesscom.ceac.v2.GameReviewResponse`,
  whose `success.game_review` is a `chesscom.explanation_engine.v1.GameReview`.
- The `/callback/analysis/game/live/<id>/all` HTTP call returns no review data.

## Which engine reviews the game

The client chooses the engine with:

```
engine = flag("web_analysis_torch_human_v2")
           ? (setting == "stockfish16 nnue" ? ENGINE_SF16_1_NNUE : ENGINE_TORCH_HUMAN)
           : ENGINE_SF16_1_NNUE
```

and a setting that is neither Stockfish 16 nor Torch is forced to Torch. So **the site default is
Torch** (Chess.com's own engine), not Stockfish. In the account's in-app browser profile the setting
was `torch-human`.

Every returned score carries the engine that produced it (`chesscom.engine.v1.Score.engine`):

| Requested | Scores actually produced by |
|---|---|
| `ENGINE_SF16_1_NNUE` ("Stockfish 16" in the UI) | `ENGINE_SF18_NNUE` (13), i.e. **Stockfish 18** |
| `ENGINE_TORCH_HUMAN` (default) | `ENGINE_TORCH_3` (11) |

The two reviews of the same game differ (game 185209623352: accuracy 72.7/72.7 with Stockfish,
74.6/75.1 with Torch; 5 more Excellent and 4 fewer Inaccuracies for White with Torch). The
calibration dataset (`tests/calibration/games`) is the Stockfish review: all 4,081 scored plies of
the 59 games match a fresh capture exactly, and reopening a review returns the same stored result.

`gameEvaluationOptions.use_game_state_cache` is true for Stockfish and false for Torch.

## What a review contains per move

`Review.played_moves[i]` (`PlayedMove`):

- `played_move`: the move, its `move_classification` and its `score`;
- `best_alternative_move`: present only when the played move is not the engine's move; carries the
  best move, its classification (always Best) and its score;
- `is_key_moment`, `explain_line` (the principal variation, each node with its own score), coach
  speech and board markings.

`Score` = `{ chess.v1.Score score; int32 depth; int64 nodes; Engine engine; int32 variation;
Strength strength }`, and `chess.v1.Score` = `{ sint32 score_centipawns_white | int32 mate_in_white
| int32 mate_in_black | Stalemate }`. Scores are **White-relative** and zigzag-encoded; squares are
numbered 1..64 from a1.

Classification enum: 1 Book, 2 Brilliant, 3 Great Find, 4 Best, 5 Excellent, 6 Good,
7 Inaccuracy, 8 Mistake, 9 Blunder, 10 Miss, 11 Forced, 20 Tricky.

## How the scores are produced (inferred from 4,081 plies)

- **Best = the engine's move.** `best_alternative_move` is absent exactly when the played move is
  the engine's choice; those plies are Best, Book, Forced, Great or Brilliant, never Excellent.
- **Scores form a tree.** A game position that lies on an earlier search's principal variation
  inherits that search's score, one ply shallower per step (for example `404@20, 404@19, 404@18,
  404@17` down four consecutive plies). The best alternative's score always equals the score of
  the position before the move. A fresh search happens when the game leaves the principal variation.
- **Fast is not a fixed depth.** Fresh searches reach depth 12-23 (mean 17.4, mode 18-19) depending
  on the position, so the limit is a node or time budget. Opening positions carry much deeper
  scores (depth 26-35) from the game-state cache.
- No MultiPV index (`variation`) or node count is sent.

## Consequences for this project

- Our labels can only match the Stockfish setting; a Stockfish clone cannot reproduce Torch reviews.
- Stockfish 18, not 16.1 or 17.1, is the engine to match.
- Even with Chess.com's own scores, our recovered precision rules reproduce about 87% of the
  graded labels (Excellent to Blunder) at best; see `log.md`, "Exact-score oracle".

## Capture format (`tests/calibration/cc-reviews/<id>.sf.txt`)

```
eng 10 acc <white> <black> cee <version>
<ply> <played uci> <label> <played score> <best uci|-> <best label|-> <best score|-> [K]
```

Scores are White-relative: `123@18` is +1.23 at depth 18, `M3@40` White mates in 3, `-M2@30` Black
mates in 2, `S@` stalemate. `K` marks a key moment. `tools/calibrate/cc_oracle.py` applies our
precision rules to these scores; `tools/calibrate/emulate_search.py` emulates the search procedure.

## Coach speech

The same `GameReview` carries the coach's speech, show-moves buttons and board markings per move.
[`coach-log.md`](coach-log.md) describes how they are captured (`tools/calibrate/coach_capture.js`)
and mapped to event tags for the Phase 0 coach comparison. The captures hold Chess.com text and stay
outside the repository.
