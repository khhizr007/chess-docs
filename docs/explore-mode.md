# Explore mode: play your own moves with a live engine

October 2026. This document analyses and plans a feature. Sources:
- Chess.com's analysis board, observed on 2026-10-21 in the in-app browser (bundle `client-packages/analysis/2026.10.3-hotfix`).
- This repository at `3889b56`.

**Status:**
- The hybrid design and the §5.1 principle change were approved on 2026-10-21.
- Phase 0 (the spike) is done. Its measurements are in §10, and the decisions it settled are folded into §5–§9.
- Phase 1, the sideline board, is built (§5.2).
- Phase 2, the live browser engine, is built (§5.3–5.6).
- Phase 3, classifying explored moves, is built (§5.5).
- Coach text on explored moves, the first Phase 4 item, is built (§5.5, "The coach's note").
- The explore panel was matched to Chess.com's Game Review on 2026-10-22: the bubble is a game
  move's, its buttons are Chess.com's (★ Best as a variation, 💡 the coach's line, ▶ Resume), and the
  engine lines are behind a header toggle (§2, §5.2, §5.4).
- The other Phase 4 items stay optional (§7).

## 1. Summary

**The feature.** On the review screen, the user drags any legal move from any position. The board
leaves the game and enters a sideline. The eval bar, the engine lines and the best-move arrow update
live as the engine searches deeper. Later, the explored move also gets a classification icon, as
Chess.com shows ("e4 is a book move", "Nf3 is an excellent move").

**How Chess.com does it.** The live engine runs entirely in the user's browser. It is Stockfish
compiled to WebAssembly, by default the 1.6 MB "Lite" build, in a Web Worker. Making a move sends no
request to Chess.com's servers. The server is used only for the full Game Review (§2).

**Recommendation.** Do the same: a **browser engine for the live evaluation**, so the server does no
extra engine work, plus a **small server endpoint that classifies an explored move from evals the
browser sends**. That endpoint runs the rules in `review-core` and starts no main search (§5.5). The
positions of the game itself keep showing the review's evals and use no engine at all.

**Feasibility: high.** Every hard part already exists as a mature open-source component.
- A GPL-3.0 Stockfish WASM build, which fits this project's GPL-3.0-or-later license.
- `chessops`, a TypeScript chess-rules library from the authors of `shakmaty`, which the backend already uses.
- The board, line chips, eval bar and expected-points curve the frontend already has.

The main cost is frontend work. One design decision needs your approval: the frontend would start
deciding chess facts (move legality, FENs and live evals). `architecture.md` currently says it never
does (§5.1).

**Why not run it on the server.** The review's own numbers make the case.
- **Cost per position.** A depth-18 MultiPV-3 search costs about 3–5 s of engine CPU
  (`implementation-notes.md`: 33 such searches take 100–180 s).
- **Cost per session.** A user who explores 30 positions costs the server about as much as one more full review.
- **Waiting.** The searches would queue behind running reviews in the same pool of at most 4 engines.
- **Scaling.** The cost grows with the number of users. A browser engine costs the server nothing however many users explore.

## 2. How Chess.com does it (observed 2026-10-21)

Everything below was read from the live analysis page (`chess.com/analysis`) and its bundles.
Game Review is served by the same `analysis` client package.

**Engines offered** (registry in `shared.eager.*.chunk.js`; versions come from the
`featuresConfig.stockfish_release_a` and `torch_release_a` objects):

| Option | Download | Notes |
|---|---|---|
| Stockfish 19 Lite (**default**) | 1.6 MB (brotli) | Small net "by Chris Bao (sscg13)". Header: "Stockfish.js 19 (c) 2026, Chess.com", based on `github.com/nmrugg/stockfish.js`, GPLv3. |
| Stockfish 19 | 95 MB | Full NNUE net. |
| Torch 4 Lite / Torch 4 | 6 MB / 73 MB | Chess.com's own engine. |
| Engine Off | — | |

- Each engine ships in several builds: `multiThreaded`, `singleThreaded`, `asm` (asm.js), and in
  older entries also `multiThreadedNoSIMD` and a no-Worker build. The client picks the best build the
  browser supports. Engines that need multithreading are hidden when it is not available.
- The page is `crossOriginIsolated` (COOP/COEP headers), which is what lets the multithreaded build
  use `SharedArrayBuffer`.
- The registry's default engine setting is `Threads: 1`.
- Other settings: up to 5 lines (`MaxLines = 5`) and depth presets `Fast: 18` and `Standard: 22`.
  An ECO opening book (`books/eco.json`) labels book moves.

**Behaviour measured on 1.e4 e5** (16-thread machine; the thread count the engine used was not measured):
- The first readout appeared at depth 8, immediately after the move.
- Depth 18 arrived about 1.9 s after the move and depth 20 about 4.3 s after it.
- The search stopped at depth 21 (about 4.9 s) and did not continue during the next 14 s.
- It shows 3 lines with depth, engine name and eval, for example "depth=20 | Stockfish 19 Lite".
- **No network request was made after the move.**

**Move feedback is also local.** Two pieces run in the browser:
- **The classification.** The engine wrapper has a classification mode. It forces `MultiPV 2` and tags
  results `mtype: "classification"`.
- **The coach text.** A separate `explanation-engine.wasm` (version 1.130.53) is downloaded. It is
  the web build of the `libcee` coach described in `coach-analysis.md` §3.

Feature flags such as `analysis_self_board_classifications` and `analysis_speech_from_cee_v2` gate this.

**What this means for us.** Chess.com accepts that the eval of a position explored in the browser
(Lite net, the user's CPU) can differ from the server's Game Review eval of the same position. It
labels the engine and depth on the analysis page so the user can see where a number comes from.

**Game Review's panel while exploring (observed 2026-10-22).** This was played on one of the user's
own games (`/analysis/game/live/185708236598/review`, desktop layout at 1400×900). The analysis page
above lists engine lines, but Game Review does not show them while exploring.
- **The coach bubble** has the same layout as for a game move. The 80 px coach avatar sits next to
  a speech bubble about 238 px wide.
  - **Header row.** The classification icon (24 px), the class name in 15 px semibold ("Book",
    "Inaccuracy", "Best") and the eval chip on the right ("+0.31", bold, light grey `#e7e6e5`).
  - **Body.** The coach's sentence, for example "e4 takes full control of the center, and allows
    the queen and light-squared bishop to develop." or "Your best move was to threaten to capture a pawn."
  - **What it leaves out.** There is no "Exploring X instead of Y" title, no hint about dragging
    pieces or the arrow keys, and no depth or engine name.
- **Buttons under the bubble** (`flow-buttons-component`, 40 px tall, 5 px radius):
  - **No better move** (a book move): a single full-width secondary button, "▶ Resume".
  - **A better move exists**: three icon-only buttons.
    - ★ (`circle-fill-star`, secondary) plays the best move as a variation, for example "2... e5 (2... d5)".
      The bubble then shows "Best".
    - 💡 (`device-bulb-fill`, secondary) plays the coach's explanation line, shown as "Explaining"
      with ‹ › ✓ buttons.
    - ▶ (`media-control-play`, primary green) is Resume.
  - **Resume** returns to the game position the line branches from. The line leaves the move list
    there but is kept, as §5.2 ("Explored lines are kept") found.
- **No engine lines and no depth readout** appear anywhere in the review panel. The only way to
  reach them is the header's "Go to Analysis" icon (`aria-label="Go to Analysis"`, right end of the
  header next to "Toggle Coach Audio"), which switches to the Analysis tab.
- **The board** shows the explored move's classification badge and a blue arrow for the engine's
  best reply.

## 3. What we have today

| Area | State | Gap for explore mode |
|---|---|---|
| Board (`BoardView.tsx:41-56`) | react-chessboard v5. Dragging is enabled only in Retry mode, for the mover's pieces. | Must accept any legal move on any ply. Needs a promotion picker. |
| Chess rules in the frontend | None. `lib/fen.ts` is display-only. Retry accepts only moves found in the engine lines (`lib/retry.ts:36-50`). | Legal moves, FEN after a move, SAN, check/capture flags for sounds. |
| Position analysis API | `POST /api/positions/analyze` exists (FEN → MultiPV lines with SAN/UCI/FEN). The client wrapper exists (`client.ts:72`) but nothing calls it. | No streaming, cannot be cancelled, shares the review pool, clears the hash before every search, default depth 18. |
| Engine layer (`engine/uci.rs`) | Stop and cancel work. An LRU cache keyed by request. `ucinewgame` and `Clear Hash` before each search. | Only the final result is returned; there are no per-depth updates. |
| Eval bar (`EvalBar.tsx`) | Fed from `review.graph[ply]`. `cpToExpectedPoints` exists in `lib/retry.ts:16-25`. | Needs a live source while exploring. |
| Lines UI | `LineView`, `ShowLineMoves` and `LinePreview` with sources `alternatives`/`next`/`coach` (`Coach.tsx`). | Can render engine lines if they come in the `Line`/`MoveRef` shape. |
| Navigation | One keydown handler (`ReviewScreen.tsx:227-253`): ←/→, Home/End, f, Esc. A preview has its own stepping. | Needs a sideline cursor. |
| Push channels | None. Reviews are polled every 500 ms. | Not needed if the engine is in the browser. |

## 4. Options and their compute cost

| | A. Server engine | B. Browser engine (Chess.com, lichess) | **C. Hybrid (recommended)** |
|---|---|---|---|
| Live eval runs on | Backend Stockfish pool | User's browser (WASM worker) | User's browser |
| Classification of explored move | Server search + rules | Rules ported to the browser | Server rules on browser evals: no main search |
| Server CPU per explored position | ~3–5 s (depth 18, MultiPV 3, cold hash) | 0 | ~0 (milliseconds of rules; at most a few depth-10 searches at ~0.04 s, see §5.5) |
| Server CPU for 30 explored positions | ~90–160 s, about one more review | 0 | well under 1 s |
| Latency to the first eval | HTTP round trip plus pool wait (behind reviews) | ~instant (depth 8 in tens of ms) | ~instant |
| Live deepening | Needs SSE/WebSocket and per-depth `info` plumbing | Built in | Built in |
| Engine matches the review | Yes | No (Lite or other net, different hardware) | No for live evals. Classification uses one engine consistently (§5.5). |
| New frontend weight | 0 | 1.85 MB WASM (1.1 MB brotli), loaded lazily and cached | Same as B |
| Rule duplication | None | Port `review-core` and the facts builder to WASM or TS | None |
| Breaks "frontend never decides chess facts" | No | Yes | Partly (legality and live evals only) |

Option A also needs a legality source for the drag (a server round trip, or a JS library anyway). It
needs real changes to the engine layer: streaming, client cancellation, a separate pool slot, and
keeping the hash between searches. It is the most backend work for the worst scaling.

Option B is what Chess.com does. Its weak point for us is the classification step. `MoveFacts`
(`review-core/src/classification.rs:198-219`) needs `events`, `material` and `missed` facts. Those are
built in `review-server` from board analysis (`analysis/see.rs`, detectors), not only from evals.
Porting that to the browser means compiling `shakmaty` plus the facts builder to WASM. That is
possible, but it is a second build target to maintain.

Option C takes B's zero-cost live engine and keeps the rules in one place, on the server.

## 5. Recommended design

### 5.1 Principle change (needs approval)

Amend `architecture.md` "The frontend is a renderer" as follows:
- **Exploration is the one exception.** The frontend may decide move legality, FENs and SAN of explored moves (with `chessops`), and may show its own engine's evals for explored positions.
- **Review data stays authoritative.** Classifications, accuracy, the coach and every review result
  still come from the backend.
- **The source is always labelled.** Live evals always show their source, for example "depth 19 · Stockfish Lite (in your browser)".

### 5.2 Board and sideline

- Add `chessops` (GPL-3.0, TypeScript, about 30 KB). It is from the same author as `shakmaty`, so FEN
  normalisation and SAN match the backend.
**Built in Phase 1.** The rules are in `lib/chess.ts`, the sideline model in `lib/explore.ts`, and
the wiring in `ReviewScreen.tsx`.

- **When dragging is allowed.** It is on whenever no Retry and no line preview is open. Retry keeps
  its own drag semantics (it is a quiz).
  - **Any piece, only legal moves.** Every piece can be picked up, clicked or dragged, of either side,
    with or without a move. Only the side to move's legal moves are played (§5.2 "Picking up any
    piece").
  - **From the report.** Dragging on the report screen switches to the review.
- **Castling.** The king can be dropped on its target square or on its rook. UCI follows the backend:
  king squares in standard chess, king-takes-rook in Chess960.
- **Promotion and clicks.**
  - **Our own promotion picker.** react-chessboard 5.12.1, the board until 2026-10-24, had no promotion
    dialog: its promotion code only animated a piece change, and `onPieceDrop` reported just the piece
    and the two squares (checked in Phase 0). Chessground has none either.
    - **How it works.** A pawn dropped on the last rank snaps back, and four pieces appear over the promotion file.
    - **Taking it back.** A click elsewhere or Esc takes the move back.
  - **Click-to-move and move hints (built 2026-10-22), as on Chess.com.** Clicking a piece picks it
    up, and clicking a highlighted square moves it there. A click on the piece again or on an empty
    square puts it down; a click on another piece picks that one up instead.
    - **The mouse acts on the press, not the release.**
      - **Pick-up.** The piece is picked up, with its hints, while the button is still down. In the
        browser that took 27–39 ms after the press. Before this, nothing showed until release, or
        until a drag started if the hand moved a pixel.
      - **Lift on the press (2026-10-24), as on Lichess.** Lichess (chessground) starts the drag on
        the press itself: measured on lichess.org/analysis, a press 6 px into the g1 square's corner
        got the `dragging` class at once, and the knight moved to centre under the pointer 1.7 ms
        later, before any mouse move. The board does the same with a mouse (a drag distance of 0
        under `(pointer: fine)`): a press anywhere in the square lifts the piece, centred under the
        pointer on the next frame, with its hints. A release where it was puts it back, still
        picked up. Touch keeps a 1 px threshold, so a tap stays a tap. A press on a piece the
        picked-up one can take is not a drag: it plays the capture.
        - **On chessground since 2026-10-24.** With react-chessboard the press cost 15–20 ms of
          React work in a production build, because every square, droppable and draggable
          re-rendered. The board is now chessground (Lichess's board, GPL-3.0-or-later), which
          moves pieces in the DOM itself. `BoardView` draws the selection, held outline, hints
          and refused flash straight into chessground's board element, so a press renders
          nothing in React. Measured on a page with `BoardView` alone (production build,
          minify off, headless Chrome 152, trusted mouse presses over the DevTools protocol, 20
          presses each, medians):

          | | react-chessboard | chessground |
          |---|---|---|
          | Press → selection and hints in the DOM | 19–22 ms | 1.0–1.3 ms |
          | Press → piece centred under the pointer | 19–22 ms | 2.3–3.6 ms (the next frame) |
          | Press → next paint (Event Timing `duration`) | 48 ms | 16–24 ms |
          | The same at 4× CPU throttling: lift / paint | 155 / 232 ms | 20 / 40 ms |

          The chessground figures match Lichess's ~2 ms. The DOM times come from a
          MutationObserver timed from the `pointerdown`'s timestamp; Event Timing rounds to 8 ms
          and reports nothing under 16 ms. The harness and scripts are not committed.
        - **What chessground does and BoardView adds.** Chessground picks up, moves on a press
          or drop on a target, glides moves (0.18 s, cubic ease-in-out) and handles touch.
          BoardView listens on the board just before and just after chessground's own press and
          release listeners to add Chess.com's rules: the red flash on a refused click or drop,
          a refused or off-board drop keeping the piece picked up, a drop on its own square
          counting as a click, and the right button putting the piece down. It gives chessground
          only the picked-up piece's moves (`movable.dests`), plus the king-onto-rook drop.
          The squares (colours, the review's highlights, the marks, the coordinates) and the
          arrows are React layers under and over chessground; they change with the position,
          not on a press. Right-click marks and drawn arrows are BoardView's own, drawn as
          react-chessboard drew them (bent knight arrows), since chessground's drawing differs.
        - **Pieces fill their square.** Inline SVG pieces were 7% taller than the square (the
          text baseline), so a lifted piece sat 2.5 px above the pointer. They are blocks now;
          chessground shows them as CSS backgrounds made from the same drawing
          (`lib/pieceShapes.ts`, `lib/boardPieces.ts`).
      - **Moving.** Pressing a target square plays the move at once.
      - **Putting down.** Clicking the piece again puts it down on the release, so a picked-up
        piece can still be dragged.
      - **Touch** keeps the tap path, because browsers send no mouse press for it.
    - **What a picked-up piece shows,** while dragging too. The values were read from Chess.com's
      stylesheets on 2026-10-22:
      - its square fills with a yellow circle growing from the centre (`#ffff33` at 50%, 0.2 s ease-out);
      - free target squares get a dot a third of the square wide (`rgba(0,0,0,.14)`), and pieces it
        can take get a ring. Both pop in over 0.15 s with a slight overshoot.
    - **Castling.** A castling king's hint is on its landing square in standard chess, and on its
      rook in Chess960.
    - **Moves glide with ease-in-out** over 0.18 s, Chess.com's duration and easing (chessground's
      cubic ease-in-out).
    - **Where it lives.** `BoardView` draws the layers (its `Layers` class, straight into
      chessground's board); `lib/chess.ts` `legalTargets` gives the targets. Retry shows the same hints: all legal moves,
      so nothing is given away.
    - **Not copied.** The captured piece's fade-out.
  - **Picking up any piece (built 2026-10-22), as on Chess.com.** Observed on 2026-10-22 on
    Chess.com's analysis board and in Game Review (a review of the user's own game, after
    "Start Review"), by logging the board's DOM changes and pointer events around real clicks and
    drags. Both boards behave the same.
    - **Any piece responds.** A press on any piece picks it up, whatever side is to move and
      whether or not it has a move. Its square gets the growing yellow circle. Hints appear only
      for the side to move's legal moves, so a piece of the side not to move (or a blocked piece)
      shows none.
    - **No moves out of turn.** A click on a square the piece cannot reach, or a drop there, is
      refused. The square flashes red: Chess.com's `vfx-illegal-move-tap`, an `rgb(230,57,70)`
      overlay fading from 0.55 over 0.7 s, plus a black circle growing from 0.6 to 1.5× while it
      fades from 0.07. This applies to any move by the side not to move, too: in Game Review, with
      Black to move, clicking the g1 knight and then f3 only flashed f3. Out-of-turn moves never
      switch the side to move.
    - **Clicks, with a piece picked up.**
      - A target square plays the move, on the press.
      - Another piece, of either side, is picked up instead, unless it is a capture target.
      - An empty square puts the piece down and flashes red.
      - The piece itself puts it down on the release, so it can still be dragged.
      - With nothing picked up, an empty square does nothing.
    - **Drags.**
      - A drag picks the piece up, with its hints, like a press.
      - A refused drop flashes red and the piece goes back, still picked up with its hints.
      - A drop off the board goes back without a flash, still picked up.
      - A drop back on its own square counts as a click: a piece picked up by this press stays
        picked up, and one picked up before is put down.
      - A king dropped on its own rook castles, as Chess.com does in standard chess too, though
        the hint is on the king's landing square.
    - **Right button.** The press puts the picked-up piece down. Its click marks the square in
      `rgb(235,97,80)` at 0.8, and a second right click on the square unmarks it. A left press or
      a new position (a move or a step) clears the marks. Right-drags still draw arrows.
    - **Outline and cursor.**
      - From the press until the release, the held piece's square has Chess.com's hover outline.
        This is a white `rgba(255,255,255,.65)` edge 5% of the square wide (theirs is an SVG rect
        with stroke 10 in a 100 box; ours is `0.625cqw`). During a drag, the outline follows the
        square under the piece.
      - Every piece shows the `grab` cursor, and a dragged one shows `grabbing`.
    - **Retry.** The same rules apply. An illegal move is refused on the board, so it no longer
      counts as a wrong answer.
    - **Where it lives.**
      - `BoardView` handles the press, click, drop and right-click rules.
      - `BoardMoves.legal` gives the legality check, `lib/chess.ts` `canPlay`, which counts a
        promotion and a king dropped on its rook.
    - **Not copied.** On a press, Chess.com lifts the piece in place and scales it with a short
      spring, then tilts it with the drag's speed. Ours lifts on the press (with a mouse) and
      snaps to `scale(1.12)` with a shadow, without the spring or tilt. A Shift+click does
      nothing: chessground keeps Shift+press for drawing, which the board does not use.
- **The variation tree (rebuilt 2026-10-22 to match Chess.com, see "Navigation as on Chess.com" below).**
  - **What is kept.** Every move the reader explores is kept for the session. `Explored` maps a game
    ply *p* to the moves played instead of game move *p + 1*. Each move has its own `next` moves, and
    `next[0]` continues its line.
  - **Where the board is.** `BoardState = { ply, path, explored }`. An empty `path` is a game
    position. Otherwise `path` holds the child indices down `explored[ply]` to the explored move shown.
  - **The `Sideline` view.** `sidelineOf` derives `Sideline = { fromPly, moves, cursor }`: the line
    through the shown move, continued along each move's `next[0]`. The engine, judge and coach panel
    read this view.
- **Playing a move** (`play`).
  - **The game's own next move** on a game position follows the game.
  - **A move already explored from the position** is entered again, with everything played after it.
  - **Any other move is added.** From a game position it starts a new line. At the end of a line it
    extends the line. Inside a line it becomes a variation. Nothing explored is ever dropped.
- **Move list.** It shows only the lines that replace one game move, under that move's row. They are
  listed while the board shows that game move or is inside one of the lines; on every other position
  they are hidden (`listedBranch`).
  - **One row per line,** in PGN order. A variation sits in brackets after the move it replaces, for
    example "2. e4 d5 (2... e5) 3. exd5".
  - **No current game move** is marked while the board is inside a line.
  - **Clicking a listed move** shows it, including from the game move the lines replace.
- **Navigation as on Chess.com (2026-10-22).** These are Game Review's rules. We read them in a live
  review (game 185708236598, exploring 2. e4 d5 3. exd5 instead of 2. Nf3) and in its move-list
  bundle (`shared.eager.*.chunk.js`).
  - **→ on a game position always follows the game,** even where lines were explored from it.
    - Live: from 3. exd5, ← ← ← landed on 1... c6, and → → went to 2. Nf3, then 2... d5, with the
      review's own coach and arrows.
    - Bundle: the keyboard plugin binds → to `openVariationsPopover() || moveForward()`. Its guard
      `Pw` returns false when the move list's variation visibility is `active` and the selected move
      is on the main line (`ids.line === 0`). The review's visibility is `active`.
  - **← from a line's first move lands on its branch.** That is the game position, where the line is
    hidden from the list and the review's coach returns.
  - **→ in a line follows it** and does nothing at its end.
  - **The variation picker.** → opens a picker under the shown move when variations were played after
    it. `Pw` is true only when the line's next move has sibling lines.
    - **The options.** The line's own move comes first and is preselected, then each variation, as
      in `entries = [{move: next}, ...next.lines]` with `selectedIndex = 0`. So → → continues the line.
    - **Keys.** ↑ and ↓ choose without wrapping, and → or Enter follows. Any other key closes the
      picker and acts as usual: ← closes it and steps back. (Chess.com's handler stops only those four
      keys.)
    - **Mouse.** Hovering a row chooses it and a click follows it. A click elsewhere, or scrolling the
      list, closes the picker.
    - **Esc closes only the picker.** This is our choice: Chess.com's handler passes Esc on.
    - **The look** is copied from Chess.com's stylesheet: fixed under the move, at least 120 px wide,
      a 3 px `#8b8987` top border, a `#262421` background, a `0 2px 5px` shadow, 13/20 px text, and
      the chosen row tinted 5% white with a → before it (`lib/explore.ts` `nextMoves`, `MoveList`
      `VariationPicker`).
  - **The ▶ button follows the line's own move** without the picker. Live, it went from 2. e4 to
    2... d5 with 2... e5 played there. Only the → key opens the picker.
  - **Explored lines are kept and can be re-entered.** Lines stayed in the tree (`getRawLines`) after
    the reader left them, through Resume, clicks on game moves, and later
    explorations. Playing 2. e4 again re-entered the line with 2... d5 3. exd5. A second move from the
    same position (2. f4) and a line from another ply (2... g6) were added beside it.
  - **Leaving.** Esc, "Resume" (which returns to the branch, as on Chess.com) and every
    game navigation (game moves, the graph, Home/End, autoplay) show a game position. The lines
    stay.
- **What the panel shows** (matched to Chess.com on 2026-10-22, §2):
  - **The coach bubble** looks as it does for a game move:
    - **Header.** The shown move's icon and verdict ("Qxf6 is a blunder") and the eval pill. Until
      the move is judged, the header shows only the move and the pill, and the body says "Judging the move…".
    - **Body.** The coach's sentences. Without sentences, it says "Qb3 was best." when the judgement
      shows the best move.
    - **Endings.** It names checkmate, stalemate, dead material and the fifty-move rule.
    - **Engine errors.** A browser engine that cannot start is reported in the bubble.
    - **What it leaves out.** There is no "Exploring … instead of …" title and no hint about dragging or the arrow keys.
  - **Buttons under the bubble,** as on Chess.com (§2):
    - **Nothing to show** (before the move is judged, or with no better move and no coach line):
      one labelled "▶ Resume" (secondary, full width). It goes back to the game, and its tooltip names Esc.
    - **Otherwise** they are icon-only and equally wide: ★, then 💡, then a green ▶ (Resume).
    - **★ Best** appears when the judgement shows a better move. It steps back to the position the
      shown move was played from and plays the best move there (`playBest`, the same `play` as a
      dragged move). So it lands beside the explored move as a variation, for example
      "8. Bxf7+ (8. Be3)", and shows it, judged as best. From the branch position, a best move that
      is the game's own move follows the game, as any played move does.
    - **💡 Explain** appears when the judgement's coach note has a show-line. It replays the first
      one with the game moves' line player (narration, ‹ Replay › and Hide). It does not add the
      line to the move list, as Chess.com does. Esc or Hide returns to the explored move; Esc again
      leaves the sideline.
  - **No engine lines by default.** The header's lines icon, in the slot of Chess.com's "Go to
    Analysis", shows them (§5.4).
  - **The eval bar** is fed by the live engine (§5.4).
  - **Last move.** The sideline's last move is highlighted, and a check is marked as on game moves.
- **Sounds.** Move, capture, check and castle sounds follow `docs/sound.md` ("Sidelines"), using
  chessops' move flags.
- **Engine lines are playable (Phase 2).** Clicking a move in a live line plays the line up to that
  move into the sideline, through the same path as dragged moves.

### 5.3 Browser engine

- **Package (decided in Phase 0).** npm `stockfish@19.0.1` (`nmrugg/stockfish.js`, GPL-3.0, published
  2026-10-10), build `stockfish-19-lite-single`.
  - **Size.** It is two files: a 28 KB `.js` and a 1.85 MB `.wasm` (1.20 MB gzip, 1.09 MB brotli).
  - **Same net as Chess.com.** It uses the net Chess.com's default "Stockfish 19 Lite" uses: `nn-61e7af4bb97d` by sscg13.
  - **The alternative.** The lichess `stockfish-web` builds were not needed.
**Built in Phase 2:** `lib/engine/uci.ts`, `lib/engine/controller.ts` and `hooks/useLiveEngine.ts`.

- **Hosting.** The two files are committed in `frontend/public/engine/`, marked `-text` in
  `.gitattributes` so they stay byte-identical.
  - **Who serves them.** Vite serves them in development, and the production build copies them to
    `dist/engine/`, which the backend's `STATIC_DIR` serves.
  - **A missing file looks like a page.** `ServeDir` has an `index.html` fallback (`lib.rs:29-30`), so
    a missing engine file comes back as HTML and the worker fails to load.
    - **What the reader sees.** The controller reports the worker's error once ("Engine unavailable"),
      and the panel says so.
    - **No retry.** It does not try to load the worker again.
    - **The backend is unchanged.**
  - **Compression is not done yet.** `ServeDir::precompressed_br()` could serve a shipped `.wasm.br`
    (1.09 MB instead of 1.85 MB).
  - **No CDN is needed.**
- **Single-threaded Lite, and stay there.**
  - **No setup.** It needs no COOP/COEP headers and works in every modern browser.
  - **Chess.com does the same.** It runs `Threads: 1` by default.
  - **Threads do not help here.** Phase 0 found that 4 threads barely shorten the time to a fixed depth
    and make the slow positions slower (§10.3), so multithreading is dropped from the plan.
- **`EngineController`** (`frontend/src/lib/engine/`) owns one Worker, which is created lazily on the first
  explore move, so users who never explore download nothing.
  - **API.**
    - `analyze(fen, depth, onUpdate)` reports each completed depth and then the final result.
    - `stop()` stops searching.
    - `setGame(chess960)` sends `ucinewgame` and `UCI_Chess960` before the next search, and clears the cache.
    - `dispose()` ends the worker.
    - The worker sits behind a small interface, so the tests drive a scripted fake.
  - **A new position supersedes the current one.**
    - The controller sends `stop` once, waits for `bestmove`, then sends `position fen … / go depth N`.
    - Output from a superseded or stopped search is never reported, though its result is cached.
  - **The hash is kept across positions.** The controller sends `ucinewgame` only when a new game opens.
    Neighbouring positions in a sideline share most of the tree, so a warm hash makes each new move
    much faster. This is the opposite of the server's deterministic cold searches, and it is fine for live use.
- **UCI parsing.** The parser:
  - skips `lowerbound`/`upperbound` scores, as `uci.rs:266` does;
  - converts mover-relative `cp`/`mate` to White's view;
  - plays PV moves with chessops into SAN and FENs, at most 12 plies, as the server caps them.

  It emits the existing `Line` shape, so `LineView`, the bar and arrows reuse their code.
- **When a depth counts as complete.** It is complete once every line of that depth has arrived. The
  number of lines expected is MultiPV, capped at the number of legal moves.
- **Throttling.** Each update is one completed depth, at most one every 100 ms. A revisited position
  never reports a depth shallower than its cached one.

### 5.4 Eval bar, lines, arrow

- **On a game ply.** Nothing changes: the bar, lines and arrow come from the review. No engine runs.
- **In a sideline (built in Phase 2).**
  - **Bar and pill.** The bar is fed from live line 1 through `expectedPointsFor` at the review's rating.
    The coach bubble shows the same eval as a pill.
  - **Lines.** They are hidden by default, because Chess.com's Game Review shows none (§2).
    - **The toggle.** It is a lines icon in the panel header, shown only while a sideline move is on
      the board. Its state is saved as `review.engineLines`.
    - **What it shows.** An "Engine" section under the coach bubble with the 3 live lines.
    - **The search runs either way.** The bar, the pill and the judgement need it.
  - **Readout.** The section header shows where the numbers come from:
    - "depth 16/18 · Stockfish 19 Lite, in your browser" while it searches, with a spinner;
    - "depth 18" once done.
  - **Go deeper.** The button appears once the search is done.
  - **Arrow.** The engine-arrow toggle uses live line 1.
- **Terminal positions.** chessops detects checkmate, stalemate and insufficient material, and the engine does not
  run for them.
  - **Checkmate.** The bar shows the result: full for the winner.
  - **Draws.** The bar shows half.
  - **The fifty-move rule.** It is claimable rather than automatic, so the engine still searches.

### 5.5 Move feedback: classify an explored move (Phase 3)

**Built in Phase 3.**
- **The endpoint.** `POST /api/reviews/{id}/judge` (`docs/api.md`, `analysis/sideline.rs`).
- **The request.**
  - `from_ply` and the sideline's UCI `moves` up to the judged move.
  - The browser engine's `before` lines and `after` best line, with full PVs (up to 40 plies; the
    display lines are cut at 12).
  - `previous_ep_lost`.
- **What it does.** It replays the review's game and the sideline, then builds `MoveFacts` with the
  same builder the review uses (`analysis/facts.rs`, extracted from `build_review`) and runs
  `review_core::classify`.
- **What it returns.** The classification, rule, `ep_lost`, the best move and whether to show it,
  and the explanation sentences (`SidelineJudgement`).
- **In the frontend (`hooks/useSidelineJudge.ts`).**
  - **Where it shows.** The judged move gets its icon and colours on the board, an icon in the
    sideline row, and a verdict in the coach bubble, for example "Bg5 is a blunder. dxe5 was best."
  - **Provisional verdicts.** These are marked "refining…".
  - **Failures.** A failed request (for example, a review the server no longer holds) leaves the
    move unmarked.
- **What the live engine searches (`useLiveEngine`).** It now also searches the position the shown
  move was played from, in this order:
  1. the shown position and the one before it, both to depth 14;
  2. the shown position to the cap;
  3. the position before it to the cap.

  The before-position is often already in the cache, because the reader was just there.

Rules for consistency:
- **Both evals must come from the same engine.** `before` comes from the browser engine searching the branch
  position too, not from the review's server eval. Mixing the server's full net with the browser's
  Lite net would shift scores and invent Inaccuracies. The branch position is analysed anyway while
  the user thinks, so this costs nothing extra.
- **The same depth.** `played_is_best_move` and `best` come from `before` line 1, judged at the same depth as `after`.
- **When it is sent: once, from shallow searches (changed 2026-10-22).**
  - **The judging depth.** A move played freely is judged as soon as both positions reach
    `JUDGE_DEPTH` = 8 and the threat searches are done. Depth 8 takes a median of 13 ms a position
    in the browser (§10.1).
  - **It is not re-judged deeper.** The shown position alone keeps deepening to the depth limit, for
    the eval bar and lines.
  - **The review's own moves keep the full-depth judgement.** The server's rules are unchanged; only
    the browser's searches are shallower.
  - **Measured, 5 random moves from a middlegame position.**

    | | Engine searches plus server judgement |
    |---|---|
    | Depth 8, threats at depth 8 (now) | 19–58 ms |
    | Depth 14, threats at depth 10 (before) | 159–727 ms; the depth-18 re-judge then took seconds more |

    The reader sees the verdict about 0.15–0.2 s after the drop, which includes the 120 ms
    stepping debounce.
  - **The cost.** 4 of the 5 labels were the same at both depths. One became Blunder instead of
    Miss, and some coach sentences picked a different line. A free move gets a quick opinion, not
    the review's full-depth verdict.
  - **Before this change:** a provisional verdict at depth 14 (median 0.43 s a position), then a
    final one at the depth cap.
- **Server cost: no engine search (confirmed in Phase 0, §10.5).** With the default config,
  classification needs only these engine inputs:
  - **Before-position lines, at least two.** The second line feeds Brilliant and Great Find.
  - **The after-position's best line.** Only when the played move is not among the before lines.
  - **Nothing else.** The threat searches serve the coach, not the classification, and the "easy"
    search is off (`easy_search_depth = 0`).
- **Context from the review.** The request carries `review_id`, the branch ply and the sideline's UCI moves instead of a bare FEN.
  The server then derives the rest from the stored review:
  - the rating for expected points and the highest Elo;
  - the repetition history;
  - the game phase, which only moves forward along the game;
  - whether the game is still in book;
  - the previous move's expected points lost: the game's for the first sideline move, else the previous `judge` result.

  A review evicted from memory (`MAX_STORED_REVIEWS`) returns 404, and the frontend hides the icon.
- **Refactor first (done).** The per-move facts were built inline in the `build_review` loop.
  `facts::judge_move` now holds them, and the review and `judge` both call it, so the two cannot drift.
  - **The refactor changes no output.** Full reviews of 10 calibration games (Stockfish 18,
    depth 10, 2.67 MB of JSON) are byte-identical before and after it.
  - **Test.** `tests/sideline.rs` asks every move of 9 fixture games as a one-move sideline, with
    the engine's own lines. It checks that each gets the review's classification, rule, `ep_lost`,
    best move and explanation.
  - **Lines must be full.** Lines cut to the 10 display plies changed one explanation sentence
    (material lost) in that test.
- **Trust.** The server trusts evals the client sends. That is acceptable for this app: it has no
  accounts, rankings or stored results that a fake eval could affect.

**The coach's note (built 2026-10-22).** `judge` also returns the coach's note for the move, the
same `CoachNote` a game move gets.
- **Shared code.** `facts::coach_note` was moved out of `build_review` and is shared, as `judge_move` is.
  - Full reviews of 10 calibration games stayed byte-identical (Stockfish 18, depth 10).
  - `tests/sideline.rs` asks every move of 9 fixture games as a one-move sideline, with the threat
    searches the review made, and gets the review's own note each time.
- **The threat searches run in the browser, so the server still searches nothing.** The coach needs
  three null-move searches around the move (`coach::CoachInput`):
  - after the move, its mover to move again;
  - before it, the opponent to move;
  - after the engine's best move, when that is not the played move.

  `useLiveEngine` runs them with one line, like the server, right after both positions reach
  `JUDGE_DEPTH`. Their depth is the review's `threat_search_depth` (10), capped at `JUDGE_DEPTH` (8).
  The best-move position is worked out when its step runs, from the latest result. Each search
  takes a few milliseconds.
- **Which searches the server uses.** `judge` takes each search with the FEN it searched.
  - It uses a search only when that FEN is the server's own null-move position (`board::null_move`)
    and the line starts with a legal move. Anything else is ignored, so the note falls back to what it can say without it.
  - As in the review, there is no "after" threat when the side to move after the move has no legal move.
- **When it is judged.** `useSidelineJudge` judges once, when both positions reach `JUDGE_DEPTH` and
  the threat searches are ready, so the note arrives with the verdict.
  - In the browser, at depth 14, "d6 is a miss. Qh4# was the move here: it is checkmate." appeared
    0.3 s after 1.f3 e5 2.g4 d6. The coach's arrows were drawn on the board.
- **Not done.**
  - The coach's "Show …" line buttons are not offered on explored moves.
  - The human-move model (Maia-2) is not asked, so the difficulty wording is left out, as it is when Maia-2 is off.

### 5.6 Guarding the user's CPU

- **Only when needed.** The engine runs only in a sideline and only while the tab is visible
  (`visibilitychange` → `stop`). It is never on the mainline by default; a "live engine on game moves"
  setting can come later.
- **Depth cap: 18, adaptive (decided in Phase 0).**
  - **The default.** 18 matches the review's Standard preset.
  - **Slow devices.** If the first search reports under 150k nodes/s, about half this PC's browser
    speed, the cap drops to 16 for the session. On this PC, depth 16 takes a median of 1.6 s, against
    3.0 s for depth 18 (§10.1).
  - **Going deeper.** A "go deeper" button continues to 20, then 22. There is never an unlimited search by default:
    one sample position needed 73 s to reach depth 20.
  - **Lines.** The engine shows 3 lines. One line reaches depth 18 about twice as fast (§10.2), but
    `judge` needs at least two. A 1/3/5 setting is not built.
  - **Built in Phase 2 (`useLiveEngine`).** The speed is judged once per page load, when a search first
    reaches depth 14.
- **Rapid stepping.** The controller waits about 120 ms after the last navigation before starting a search.
- **Results cache.** A per-session `Map<fen, result>` (about 500 entries) makes stepping back and forth free. A
  cached result at or above the cap is shown without searching.
- **Resources.** `Threads 1` and `Hash 16 MB` in v1. That means one core while searching for a few seconds, then idle.

### 5.7 Server fallback (optional, Phase 4)

Use this only if a browser cannot run WebAssembly workers, which is rare today. It would reuse
`/api/positions/analyze` with these fixes:
- **Cancellation.** Accept an `AbortSignal`, and tie the server's `CancellationToken` to the request so a dropped request stops the search.
- **Its own semaphore.** One or two engines, so exploring never starves reviews.
- **A depth cap.** At most 14.
- **Debounce on the client.**

Without these fixes, the endpoint should not be used for interactive exploration.

### 5.8 Licensing

The WASM engine is GPL-3.0 and the project is GPL-3.0-or-later, so they are compatible. Unlike the
native Stockfish today, it **would be distributed** with the frontend build. `THIRD_PARTY.md` gets a
new row with the upstream source URL and version, which meets the GPL's source obligation for an
unmodified build. `chessops` is GPL-3.0, so it is compatible too.

## 6. Compute budget

| | Server | User's machine |
|---|---|---|
| Opening a review, browsing game moves | unchanged | unchanged (no engine) |
| First explore move | 0 | one download of 1.85 MB (1.1 MB with brotli), then cached; engine ready in 130 ms |
| Each explored position | 0 (live eval) | one core: depth 14 in 0.43 s, depth 18 in 3.0 s (medians on this PC; about 4× longer on a 4×-slower device), then idle |
| Memory | 0 | about 62 MB with a 16 MB hash (the full net would need about 440 MB) |
| Each classified explored move (Phase 3) | rules only, no engine search | the branch and after searches, already running for the live eval |
| A user idle in explore mode | 0 | 0 once the cap is reached, or once the tab is hidden |

"This PC" is a 16-thread desktop. §10 has the full distributions.

## 7. Plan

Each phase ends in something usable and testable. Effort is relative (S < M < L).

| Phase | Scope | Exit criteria | Size |
|---|---|---|---|
| **0. Spike (done 2026-10-21)** | Load a candidate Stockfish WASM build in a worker inside our app (throwaway branch). Measure time to depth 12/16/18 and memory on this PC, and on a throttled profile. Check react-chessboard v5's promotion support. List which `MoveFacts` inputs need a server search. | Done; see §10. Build `stockfish@19.0.1` lite-single; cap 18, adaptive to 16; `judge` needs no search; we build the promotion picker. No phone was measured. | S |
| **1. Sideline board (done 2026-10-21)** | chessops; drag from any ply; promotion; sideline state, move-list rendering, navigation, sounds, "Back to game". No engine yet: the bar shows "–". | Done. Vitest covers rules (`chess.test.ts`), the sideline model (`explore.test.ts`), the sideline row (`MoveList.test.tsx`) and its sounds. Checked in the browser on the Opera Game and a promotion game: branching, stepping, Esc, castling onto the rook, following the game's own move, promotion to a knight. | M |
| **2. Live engine (done 2026-10-21)** | `EngineController` + worker, UCI parser, throttle, cache, visibility stop, depth cap and "go deeper", live bar, lines, arrow and depth readout. Lazy loading. `THIRD_PARTY.md` row. | Done. Vitest: `uci.test.ts` and `controller.test.ts`, a scripted fake worker covering the handshake, complete depths, superseding, cache, stop, throttle, new game and load failure. In the browser: engine ready in 151 ms and depth 14 in 0.8 s; lines, pill, bar and arrow update live; "Go deeper" goes 18 → 20; clicking a line move plays it; a revisited position answers from the cache; a hidden page pauses the search. No phone was measured. | M |
| **3. Move feedback (done 2026-10-21)** | `POST /api/reviews/{id}/judge`, ts-rs types, icon and verdict line for explored moves, book detection. | Done. The facts-builder refactor was confirmed byte-identical on 10 games. `tests/sideline.rs` covers every fixture move judged as the review judged it, a later sideline move and bad requests. `tests/api.rs` tests the route. `useSidelineJudge.test.ts` covers provisional then final, the previous move's loss, and a move that ends the game. In the browser: 1.d4 and 1...e5 were Book, and 2.Bg5 was "a blunder. dxe5 was best". Each judge request took 7–11 ms with no engine search. | M |
| **4. Later, each optional** | ~~Coach sentences for explored moves~~ (built 2026-10-22, §5.5); ~~Chess.com's ★ Best and 💡 explanation-line buttons under the explore bubble~~ (built 2026-10-22, §5.2); server fallback (§5.7); "live engine on game moves" setting; a choice between Lite and full net. The multithreaded build was dropped after Phase 0 (§10.3). | Per item. | S–L each |

Phases 1 and 2 are the feature as most users will see it. Phase 3 is what makes it feel like
Chess.com's explore mode.

## 8. Risks

- **Evals that disagree.** At the branch point the browser's eval can differ from the review's eval of the same
  position by a few tenths. Mitigations:
  - The sideline always shows the live source and depth.
  - The game positions keep the review's numbers.
  - Classification never mixes the two (§5.5).
- **Slow devices.** At 4× slower than this PC, depth 18 takes a median of about 12 s, and depth 14 about 1.7 s.
  Mitigations:
  - **The adaptive cap** (16 below 150k nodes/s).
  - **Visible deepening.** Depth 12 arrives in a median of 0.15 s here, and about 0.6 s at 4× slower.
  - **Explored moves are judged at depth 8** (§5.5), which costs little even on a slow device.

  No real phone has been measured yet, in Phase 0 or in Phase 2.
- **The Lite engine's numbers differ from the review's.**
  - **Balanced positions.** Lite and the server's Stockfish 18 agree within 14 cp (median, §10.4).
  - **Won positions.** Lite reports larger scores, for example +545 against +447. That is up to 0.07 in expected points: enough to change a
    class if the two engines were mixed, which §5.5 forbids.
  - **Best moves.** They differ in 5 of 27 positions.
  - **What the user sees.** The bar may jump by a few hundredths of expected points when the user enters a sideline.
- **Bundle and first-load size.** The engine is never in the main bundle. It is fetched only on the first explore move.
- **Scope creep.** Saving sidelines to PGN and a full analysis board are separate features. They are deliberately left out. The variation tree went in only as far as Chess.com's review shows it (§5.2).

## 9. Decisions needed

1. ~~Approve the §5.1 principle change.~~ Approved 2026-10-21.
2. ~~Approve the hybrid design.~~ Approved 2026-10-21.
3. ~~Default depth cap.~~ Settled in Phase 0: 18, dropping to 16 on slow devices (§5.6).
4. ~~Whether Phase 3 is in the first release.~~ Phase 3 is built (2026-10-21).

## 10. Phase 0 results (2026-10-21)

**Setup.**
- **Machine.** This PC: a 16-thread desktop, Windows 11. The runs went one at a time, never two at once.
- **Engine.** `stockfish@19.0.1`, `lite-single` unless noted: one thread, Hash 16 MB, MultiPV 3.
- **Cold searches.** Each search started with `ucinewgame` and `Clear Hash`, as the server does.
- **Positions.** 27 positions from the first 8 calibration games (`tests/calibration/games/`), at plies 12, 24, 36,
  48 and 60, so opening, middlegame and endgame are all included.
- **Reported numbers.** Medians, 90th percentiles and maxima of the time until depth *d* completed on line 1.
- **Where the runs happened.** Two environments, which searched identical node counts:
  - inside the app: a throwaway Vite page running the engine in a Web Worker, with the Browser pane visible;
  - Node 24, with the same WASM files.
- **Scripts and raw results.** These are in `tools/explore-bench/`, which is untracked like `tools/calibrate/`:
  - `positions.mjs`, `bench.cjs`, `native.sh` and `summarise.cjs`;
  - `spike-main.ts` and `spike.html`, the browser page;
  - `results/`, the raw output.

### 10.1 Time to depth in the browser (the number that matters)

| Depth | Median | p90 | Max |
|---|---|---|---|
| 8 | 13 ms | 45 ms | 66 ms |
| 10 | 28 ms | 119 ms | 181 ms |
| 12 | 154 ms | 298 ms | 399 ms |
| 14 | 433 ms | 931 ms | 1.7 s |
| 16 | 1.6 s | 2.4 s | 3.0 s |
| 18 | 3.0 s | 5.8 s | 13.9 s |

- **Engine start-up.** From `new Worker` to `readyok` took 130 ms.
- **Response headers.** Vite serves the WASM file as `application/wasm`.
- **Speed and work.** The browser searched about 330k nodes/s, with a median of 1.03M nodes to depth 18.
- **How often it is fast.** 25 of 27 positions reached depth 14 within 1 s, and 12 of 27 reached depth 18 within 3 s.
- **Node is a little faster.** It searched about 385k nodes/s with the same node counts, so the browser is about 15% slower.
  In Node, depth 18 took a median of 2.3 s.

**A 4×-slower device.** The in-app browser cannot apply DevTools CPU throttling, so these figures
are the times above multiplied by 4. That is valid here because the search is CPU-bound and its node counts are deterministic:
- depth 12 takes about 0.6 s;
- depth 14 takes about 1.7 s;
- depth 16 takes about 6.3 s;
- depth 18 takes about 12 s (median).

That is why the cap adapts (§5.6). No real phone was measured.

**The deep tail.** In Node, depth 20 took a median of 5.4 s and a 90th percentile of 10.7 s, and one position needed 73 s. This is why
there is no unlimited search by default.

### 10.2 What the knobs cost (Node, same 27 positions)

| Variant | Depth 18 median | p90 | Notes |
|---|---|---|---|
| Lite, 3 lines (default) | 2.3 s | 5.1 s | 1.03M nodes |
| Lite, 1 line | 1.25 s | 1.9 s | 0.42M nodes: about 2× faster |
| Full net (`single`, 99 MB), 3 lines, 10 positions | 3.9 s | 7.2 s | 213k nodes/s; 660 ms start-up; about 440 MB memory against 62 MB for Lite |

Warm hash along a sideline: 13 consecutive positions from one game.
- **With the hash kept**, depth 18 took a median of 3.65 s.
- **With the hash cleared**, it took 4.2 s.
- **So keeping the hash** saves about 13%: worth doing, but not decisive. Revisits are free anyway, because of the results cache.

### 10.3 Multithreaded Lite (browser, cross-origin isolated, 4 threads)

| | Depth 14 median / p90 | Depth 18 median / p90 / max | Nodes/s | Nodes to depth 18 |
|---|---|---|---|---|
| 1 thread | 0.43 / 0.93 s | 3.0 / 5.8 / 13.9 s | 330k | 1.03M |
| 4 threads | 0.63 / 1.94 s | 2.7 / 8.2 / 21.9 s | 1.57M | 4.97M |

- **More nodes, not more depth.** Four threads search 4.8× more nodes per second, but they also need 4.8× more nodes to complete a depth. Stockfish's
  Lazy SMP widens the search rather than deepening it sooner.
- **The cost.** It also starts in 764 ms instead of 130 ms, needs COOP/COEP headers, and uses four cores.
- **Decision:** single thread only.

### 10.4 Lite against the server's engine

- **Engines.** The same 27 positions at depth 18 with 3 lines, cold. Lite is compared with the server's native
  Stockfish 18 (`~/tools/sf18/sf18`, Threads 1, Hash 64).
- **The same best move** in 22 of 27 positions.
- **Balanced positions** (12 positions with |eval| ≤ 200 cp): the scores differed by a median of 14 cp, at most 19 cp.
- **Winning positions.** Lite gives larger scores, for example +545 against +447 and +620 against +440.
- **In expected points** (the frontend's `cpToExpectedPoints` at rating 1500), the difference was 0.016 at the median and 0.047 at
  the 90th percentile, with a maximum of 0.073.

That is enough to move a class boundary, hence the rule that `judge` never mixes the two engines (§5.5).

The native engine took a median of 1.4 s per position. That is about half of Lite in the browser. It
confirms that running this work on the server would cost a full server core for every explored position.

### 10.5 What classifying an explored move needs (code reading)

This comes from `build_review` (`analysis/mod.rs:493-717`) and `analyse_positions` (`:208-444`).

- **Engine inputs.**
  - The before-position lines.
  - The after-position's best line, only when the played move is not among the before lines (`:573-585`).
  - The before-position eval (line 1).
- **Board inputs.** Draw flags, material walks along the lines (`walk_line`), static
  sacrifice checks (`static_sacrifice`, `see.rs`), and the move tests: only escape, free capture, quiet retreat and recapture.
- **Game context.**
  - Ratings: `rating_for_expected_points` and the highest Elo.
  - Repetition history (`:218-228`).
  - Phase, which is monotonic (`phases`, `:475`).
  - Book continuity (`book_flags`).
  - `opponent_previous_ep_lost`.
- **Not needed for classification.**
  - The null-move threat searches and the best-move threat search: coach only.
  - The "easy" search: off by default (`easy_search_depth = 0`).
  - The Maia human odds: coach difficulty only.

So `judge` runs **no engine search** under the default config.
