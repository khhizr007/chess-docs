# Where we stand against Chess.com

October 2026, at `main` `b517f5f` (explore mode merged). This compares the app with Chess.com's Game
Review and analysis board and ranks what to build next.

Sources:
- Chess.com, observed live:
  - the review summary of game 142636591844, on 2026-10-22;
  - the analysis board's bundles, on 2026-10-21 (`explore-mode.md` §2).
- Our own measurements:
  - [`parity.md`](parity.md) and [`calibration/log.md`](calibration/log.md) for the labels;
  - [`coach-gap-analysis.md`](coach-gap-analysis.md) §7 for the coach;
  - [`explore-mode.md`](explore-mode.md) for the live engine.

## 1. Summary

**The review itself is at parity in method and close in output.**
- **Same method.** Labels, accuracy, phases, key moments, retry, the coach and explore mode all use
  Chess.com's recovered rules or a measured equivalent.
- **Close output.**
  - Labels agree exactly on about 69% of moves and within one step on about 89%. The rest is mostly
    engine noise that cannot be reproduced (§3).
  - Our coach names the same reason as Chess.com's on 39% of bad moves and 58% of good ones, and is
    almost never silent where Chess.com speaks.
  - Its claims are fact-checked, with 0 false claims at the last run.

**The visible gaps are around the review, not in it.** The four that matter most:
1. There is no **Game Rating** or **Advanced Stats** on the report.
2. ~~There is no **game import by username**.~~ Done: a Chess.com or Lichess username lists your recent games (§4, #1).
3. ~~There is no **coach text on explored moves**.~~ Done: explored moves get the coach's note (`explore-mode.md` §5.5).
4. The **analysis board** allows only one sideline at a time.

## 2. Feature by feature

| Feature | Chess.com | Us | Status |
|---|---|---|---|
| Move labels: Brilliant, Great, Best, Excellent, Good, Book, Inaccuracy, Mistake, Miss, Blunder | Yes | Same recovered decision tree and thresholds | **Parity in method.** 69% exact, 89% within one step (§3) |
| Forced | Yes, counted as Best | Yes | Parity |
| Tricky | Yes | No: it needs their ML difficulty models (`open-questions.md` #6) | Gap, rarely seen |
| Accuracy (CAPS2) | Yes | Same formula | Parity in method. Ours is about 2–3 points higher, from engine differences |
| Class tallies, eval graph, eval bar | Yes | Yes | Parity |
| Phase accuracy (opening, middlegame, endgame) | Yes | Yes. The phase split is our own heuristic (`open-questions.md` #9) | Close |
| Key moments, critical moves | Yes | Yes. The final rule is partly heuristic (#10) | Close |
| One-line game summary ("You built a lead in the opening then …") | Yes | Our report summary and takeaways | Close. The wording differs |
| **Game Rating** per player (1400 and 150 in the sample game) | Yes | **No.** It is computed on their server, so no client has the formula (#11) | **Gap** |
| **Advanced Stats** per player (Opening, Tactics, Strategy) | Yes. The meaning of the numbers is not yet verified | No | **Gap** |
| Coach explanation per move | Yes, from their explanation engine | Our event-based coach: 39% / 58% the same reason, fact-checked | Close |
| Coach voice (speech) | Yes | No | Gap, minor |
| Show line, best move, retry with hints | Yes | Yes | Parity |
| Sounds | Yes | Same rules, our own sounds | Parity |
| Play your own moves with a live engine | Yes: Stockfish 19 Lite in the browser | Yes: the same build and net in the browser | **Parity** |
| Labels on explored moves | Yes, computed in the browser | Yes, on the server with the review's rules and no engine search | Parity |
| Coach text on explored moves | Yes (`explanation-engine.wasm`) | Yes: the review's own coach. The browser makes its threat searches, and the server makes none | **Close.** The coach's "Show …" line buttons are not offered on explored moves yet |
| Engine choice (full Stockfish, Torch), 1 to 5 lines, depth presets | Yes | Fixed: Lite, 3 lines, depth 18 with "Go deeper" | Minor gap |
| Several sidelines per position, saving, PGN export with variations | Yes | One sideline at a time, not saved | **Gap** |
| Opening explorer (games database) | Yes | Opening names only | Gap |
| **Your games appear automatically / import by username** | Yes | A Chess.com or Lichess username lists the 20 most recent games; one click imports one. You can also paste a PGN or open a file | **Close.** You type the username once; it is remembered |
| Account history and insights across games | Yes | No: one game at a time | Out of scope for now |
| Mobile | Apps and mobile web | Responsive web layout (breakpoints at 900 and 480 px). The live engine has not been timed on a phone | Partly |

## 3. How close the labels can get

- **Agreement now.** The labels agree exactly on 68.7% of moves over 142 games, and within one step on 88.7%.
- **The ceiling with their own numbers.** Even with Chess.com's own displayed evaluations, about one
  graded label in eight cannot be reproduced (`calibration/log.md`), so roughly 88% is the ceiling
  for exact agreement.
- **Most of what is left is noise.** Our engine's evaluations differ from theirs by a median of
  12–16 centipawns at every depth and version we tried. That alone flips about 15% of grades
  (`parity.md`).
- **What can still be gained.** Small amounts from the near-threshold hedge and from calibrating at
  other ratings (`coach-gap-analysis.md` §7.2, items 4 and 6). Large further gains are not expected.

## 4. What to build next

| # | Work | Why | Size | Feasibility |
|---|---|---|---|---|
| 1 | ~~**Import games by username**~~ **Done (2026-10-22)**: `lib/onlineGames.ts`, `components/OnlineImport.tsx` | The most visible gap. On Chess.com your games are just there | S | Built. The browser calls the public APIs directly (CORS allowed), so the username never reaches our server |
| 2 | **Game Rating estimate** | The headline number on Chess.com's report | M | Medium. The formula is server-side. Plan: capture "Game Rating" for the 142 calibration games from their review pages (the summary shows it), then fit an estimate from our per-game statistics and report its error. It must be labelled an estimate. All 142 games come from one account rated about 950, so a second rating band is needed before trusting it widely |
| 3 | ~~**Coach text on explored moves**~~ **Done (2026-10-22)** | Explored moves got a label but no "why" | M | Built. The browser runs the coach's threat searches, so the server still searches nothing |
| 4 | **Label and coach calibration at other ratings** (1200–2200), plus the near-threshold hedge | Everything is tuned on players rated about 950; also fixes about 440 praise-or-blame contradictions | M | High. The capture tooling exists |
| 5 | **Analysis board:** a variation tree (several sidelines), PGN export with variations | Exploring several ideas from one position | M–L | High |
| 6 | **Advanced Stats** (Opening, Tactics, Strategy) | A second report block on Chess.com | M | Low until we know what the numbers mean. Investigate alongside #2 |
| — | Later: engine and lines settings, full net, brotli for the engine file, phone timing, opening explorer, coach voice | Smaller or optional | S–L | — |

Items 1 and 2 can run in parallel: they touch different code (import panel; report and backend).
