# Polish gaps against Chess.com's Game Review

Audit of 2026-10-22 at `main` `2f5e41a` (PR #17 merged). This lists what still separates our review
from Chess.com's, in the look and feel rather than in the labels, which are covered by
[`parity.md`](parity.md) and [`chesscom-comparison.md`](chesscom-comparison.md).

## How it was compared

- **Game.** 142636591844 (khhizr7 – siddytopcoder, 18 moves, 1-0 by mate), the sample game in
  `chesscom-comparison.md`. Chess.com's own review of it was opened in the in-app browser, signed in.
  Ours was the same PGN with its `[%clk]` comments, reviewed at Standard (depth 18, Stockfish 18) by a
  fresh build of this commit.
- **States.** Loading, report, first move, a mistake, a check, the mate, Best, Explain, an explored
  move, keyboard, eval bar, and the 1200×760, 1440×900, 768×1024 and 375×812 viewports.
- **Measurements.** Sizes, fonts, colours and transitions were read from both pages' computed styles.
  For Chess.com's move list, square tints and arrows, every ply was clicked in turn and the DOM read.
- **Screenshots.** The paired screenshots (`cc-*` for Chess.com, `us-*` for ours) are kept outside
  the repository in the session notes folder `polish-audit-screens/`. They are not committed, because
  `THIRD_PARTY.md` keeps the reference site's material out of the repo. Each row below names its pair.
- **Not measured.**
  - Piece-move and drag timings: the pane was hidden, so `requestAnimationFrame` did not run.
    PR #17 already matched click-to-move easing; dragging is noted as unmatched in `explore-mode.md`.
  - Hover and pressed states.
  - Sounds: in progress, see (a) below.

## Already in progress (other sessions)

| | Gap | Session |
|---|---|---|
| (a) | Move and review sounds | chesscom-sounds |
| (b) | Explore panel cluttered with engine lines (Chess.com shows none in review explore, see #20) | explore-panel |
| (c) | → does not return to the game after an explored sideline | explore-rejoin |
| (d) | Clicking and selecting any piece on the board | board-click-any |

## Ranked gaps

- **Severity** (1–5) is how noticeable the gap is to a player: 5 means on every move of every game,
  1 means rarely seen.
- **Effort** is S (about a day or less, score ÷1), M (a few days, ÷2) or L (a week or more, ÷4).
- Rows are ordered by severity ÷ effort, with higher severity first on ties.

| # | Gap | Chess.com | Us | Evidence | Sev | Effort | Score |
|---|---|---|---|---|---|---|---|
| 1 | **PGN clock tags shown as a player comment** | `[%clk …]` is read as a clock and never shown as text | Every move's coach bubble ends with a quoted `"[%clk 0:09:57.5]"`. Every game imported from Chess.com or Lichess carries these tags | `us-05-move1`, `us-07-ply6`, `us-11-mate`. `backend/crates/review-server/src/pgn.rs:139` keeps the raw comment text, and `components/Coach.tsx:140` quotes it | 5 | S | 5.0 |
| 2 | **Accuracy below the fold on the report** | Order: one-line coach → eval graph (80 px) → players → accuracy → tallies → Game Rating → Advanced Stats → Start Review. Accuracy sits at y≈370 at 1440×900 | Order: four-sentence summary → four takeaway cards → graph → players → accuracy → tallies → phases. Accuracy is at y≈766 at 1440×900, and the panel must be scrolled to see it | `cc-02-report` vs `us-03-report`, `us-04-report-1200`. `components/ReportView.tsx:77-153` | 4 | S | 4.0 |
| 3 | **Review page scrolls** | Board and panel fit the window; no page scrollbar | At 1200×760 the document is 997 px tall. Screen-reader `.visually-hidden` spans in the move list are `position: absolute` with no positioned ancestor, so they stretch the page. The page gets a scrollbar and can scroll the board's top off screen | `us-06-ply21-page-scrolled`. `styles.css:180` (`.visually-hidden`), `styles.css:2124` (`.move-list` has no `position: relative`) | 3 | S | 3.0 |
| 4 | **Sound switch clipped at laptop widths** | The panel footer holds Skills and Share only. Sound and coach audio are header icons | Step through, Engine arrow and Sound sit in one row (x 764–1161) in a 360 px panel (x 750–1110), so Sound is cut off at 1200 px | `us-07-ply6` (bottom right). `components/ReviewScreen.tsx:1031-1066`, `styles.css:2377` | 3 | S | 3.0 |
| 5 | **Eval bar ignores Best and line previews** | Showing the best move moves the bar to that position (2.2 → 0.5) | The bar stays on the game position (2.3) while the board shows 3…d6 at +0.61 | `cc-07-best` vs `us-08-best`. `components/ReviewScreen.tsx:897-900` feeds only the sideline or the game ply | 3 | S | 3.0 |
| 6 | **Check, mate and game-end marks** | A king in check gets a solid red-orange square (`rgba(248,85,63,.8)`). At the end the mated king gets a red # badge and the winner's king a green crown ("Checkmate" and "Winner" pills on load) | A radial red glow on the king; no end-of-game badges | `cc-05-ply21-check`, `cc-11-mobile-load-badges`, `cc-13-tablet` vs `us-11-mate`. `components/ReviewScreen.tsx:75` (`CHECK_GLOW`) | 3 | S | 3.0 |
| 7 | **Too many arrows** | Arrows per ply on this game: 0 on book and best moves, 1 on most inaccuracies and mistakes, 2 at most. Never an arrow along the move just played | Coach "move" arrows trace the played move in orange, even on 1.e4 (book). Mistakes get the best-move arrow plus a coach arrow; 11.Bf7+ shows three | `cc-04-move1` (none) vs `us-05-move1` (e2–e4 arrow). `cc-06-ply6` vs `us-07-ply6`. `components/ReviewScreen.tsx:86-91, 516-525` | 3 | S | 3.0 |
| 8 | **No clocks in the player strips** | Each strip shows the clock left after the shown move (9:57, 5:49 …), with a clock icon on the side to move | Name and rating only, plus a "TO MOVE" pill. `%clk` is not parsed at all | `cc-04-move1`, `cc-05-ply21-check` vs `us-05-move1`. `components/PlayerStrip.tsx`. Parse the tags in `pgn.rs` together with #1 | 4 | M | 2.0 |
| 9 | **Coach bubble says too much** | The header ("Mistake", eval chip) and one short sentence, typed in word by word. "Explain" asks for more | Header plus two or three sentences, a win-chance line, up to two "Show …" buttons and the comment. On the mate, "checkmate" appears three times. The bubble scrolls, and at 1200×760 it pushes the action buttons out of view | `cc-06-ply6` vs `us-07-ply6`. `cc-10-mate` vs `us-11-mate`. `components/Coach.tsx` | 4 | M | 2.0 |
| 10 | **Phone and tablet: coach under the board** | At 375 and 768 px the coach bubble sits above the board. A bottom bar holds a large green Next button and ‹ ›. Coach, board and controls fit one screen | The coach is below the board and the player strip. At 375×812 the page is 1893 px tall, so you can read the coach or see the board, not both | `cc-12-mobile-move`, `cc-13-tablet` vs `us-13-mobile-move`, `us-14-tablet` | 4 | M | 2.0 |
| 11 | **Loading screen shows nothing of the game** | The board (final position, with end badges), both player strips and clocks, the eval bar and a coach quote appear at once, with progress in the panel | A centred card on an empty page: "Analyzing your game… Checked 5 of 62 positions" and a bar | `cc-01-loading-narrow`, `cc-11-mobile-load-badges` vs `us-02-loading` | 4 | M | 2.0 |
| 12 | Eval bar label at mate | Shows the result: `1-0` | Shows `#` | Read from both bars at ply 35. `components/EvalBar.tsx` | 2 | S | 2.0 |
| 13 | ↑ and ↓ keys | ↑ goes to the start and ↓ to the end (checked by key events; Home and End did nothing) | Home and End only; ↑ and ↓ do nothing | `components/ReviewScreen.tsx:322-353` | 2 | S | 2.0 |
| 14 | Move list marks too many moves | Icons on 9 of 35 plies here: the last book move (2.Nf3), the seven mistakes, and the key-moment best 9.Nxh7. No icon on its four inaccuracies or its miss (5.d3). This is probably key moments only; the rule is inferred from one game | Every "notable" class gets an icon: all book moves, inaccuracies, the miss and the blunder, 12 plies | DOM dump of `.node-annotation-icon` per ply. `lib/review.ts:36` (`showsListIcon`), `lib/format.ts:18-29` | 2 | S | 2.0 |
| 15 | Reload loses the move | The URL carries `?move=N` and a reload returns to it | The hash holds only the review id; a reload goes back to the report | `App.tsx:10-37` | 2 | S | 2.0 |
| 16 | Type and sizing | Titles and numbers in Chess Sans (their own font, not usable here): accuracy 17 px w700 in a 64×36 box, radius 5. Body 13–15 px. Move list 13 px w700, 30 px rows. Eval bar 30 px wide, `transform 1s ease-in` | System font throughout: accuracy 19.5 px w800 in 76×38. Moves 14.25 px w600, 32 px rows. Eval bar 22 px, `height 0.6s` ease-out | Computed styles from both pages | 2 | S | 2.0 |
| 17 | Coach text appears all at once | Words type in one by one (`typewriter-text-word`) | The bubble fades in (`bubble-in 0.2s`) with all its text | Chess.com DOM classes. `styles.css:1508` | 2 | S | 2.0 |
| 18 | "Explain" does a different thing | Plays the explanation line on the board. The line is shown inline in the move list, with ‹ › and "Got it!" | Opens a stats table (EVAL, WIN %, LOST, ACCURACY). "Show the line" is closer to Chess.com's Explain | `cc-08-explain` vs `us-09-explain` | 3 | M | 1.5 |
| 19 | "Best" flow | Plays the best move as a variation that stays in the move list. The coach says why it is best ("They defended their pawn…"). One "Resume" button | The coach text becomes instructions ("Showing move 1 of 10 in the engine's line. Use ← → …"). Two buttons (Back to game, Continue line). Nothing appears in the move list | `cc-07-best` vs `us-08-best`. `components/ReviewScreen.tsx:812` | 3 | M | 1.5 |
| 20 | Explore keeps the review's look | An explored move gets the normal coach header, class and sentence. A blue arrow shows the expected reply. The buttons are Best, Explain and Resume, and the variation sits inline in the move list. No engine lines and no instructions | "Exploring d4 instead of d3" header, a "Drag a piece…" instruction paragraph, Back to game, and an engine panel. The engine panel is (b) | `cc-09-explore-d4` vs `us-10-explore-d4`. Session (b) changes the bubble to the game-move style, adds a lone Resume and hides the engine lines (branch `claude/explore-panel-cleanup-4dc2a2`). Still missing after (b): the reply arrow, Best and Explain in explore, and inline variations (`explore-mode.md` §7) | 3 | M | 1.5 |
| 21 | Time to a finished review | Seconds: the review is computed on their servers and cached | About 56 s for this 18-move game (62 positions at depth 18, 4 engines) | Timed from `us-02-loading` to the report | 4 | L | 1.0 |
| 22 | Game Rating and Advanced Stats | Game Rating 1350 / 200. Advanced Stats: Opening, Tactics and Strategy, each a rating with a ± | Neither | `cc-02-report`. Already items #2 and #6 in `chesscom-comparison.md` §4 | 4 | L | 1.0 |
| 23 | Tally rows | Counts are always in their class colour, zeros included. Brilliant, Great, Book and Inaccuracy fold behind a chevron (as seen; the rule is not confirmed) | Zeros are grey and every row shows. Phase rows are added | `cc-02-report` vs `us-03-report` | 1 | S | 1.0 |
| 24 | Result after the last move | The move list ends with a `1-0` row | The empty Black cell shows `…`, and no result row | `cc-10-mate` vs `us-11-mate` | 1 | S | 1.0 |
| 25 | Retry everywhere | No Retry on any of the moves checked (4, 9, 24); only Explain, Best and Next | Retry is offered on every eligible move, making four buttons | Button lists read per ply | 1 | S | 1.0 |
| 26 | Coach character and voice | An animated (Rive) coach whose face reacts, and a coach-audio switch in the header | A static knight tile with a CSS hop or slump; no voice | Chess.com DOM (`animated-bot-avatar`, "Toggle Coach Audio") | 2 | L | 0.5 |

## Grouping for follow-up work

- **Clocks** (#1, #8): one change from `pgn.rs` to `PlayerStrip`. Parse `[%clk]` into the review,
  drop all `[%…]` commands from comments, and show the clock in the strips.
- **Small review-screen fixes** (#3–#7, #12–#15, #24). They are all S, and most are CSS or a few
  lines in `ReviewScreen.tsx`, `EvalBar.tsx`, `MoveList.tsx` and `lib/review.ts`. Sessions (b)–(d)
  are editing `ReviewScreen.tsx` and `BoardView.tsx` now, so start this after they merge.
- **Report and loading screen** (#2, #11, #16 for the report, #23).
- **Coach presentation** (#9, #17, #18, #19), then **mobile layout** (#10).
- **Large items** (#21, #22, #26) belong with the roadmap in `chesscom-comparison.md` §4.
