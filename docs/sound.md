# Sound

The review plays board and feedback sounds. **When** each sound plays follows the reference client,
recovered with REA on 2026-10-21. The audio comes from a local **sound pack** of recordings when one
is installed (below). Otherwise it is this project's own sounds, synthesised in the browser
(`frontend/src/lib/synth.ts`). The repository holds no audio files (see `THIRD_PARTY.md`).
The rules are in `frontend/src/lib/sound.ts` and are tested in `sound.test.ts`. The speaker icon
in the panel header (as on Chess.com) turns sound off; the setting is kept in `localStorage` (`review.sound`).

## Sound pack

A sound pack is the folder `frontend/public/sounds/`. It has one mp3 per sound, named after the sound:
`move`, `capture`, `castle`, `check`, `promote`, `brilliant`, `correct`, `incorrect`, `result_good`,
`result_ok` and `result_bad`. The folder is gitignored. `frontend/src/lib/samples.ts` fetches and
decodes every file once, when the app loads, and keeps each as a Web Audio `AudioBuffer`, so stepping
quickly with the arrow keys has no lag. A sound with no file, or one that fails to decode, is
synthesised instead. The vite dev server serves the folder as `/sounds/`, and `npm run build` copies
it into `dist/`.

To hear the reference client's own sounds, install the captured files from WSL. Run this from the
repository root:

```bash
wsl bash tools/sounds/install-sound-pack.sh
```

The source defaults to `~/work/chesscom/sounds/web`; pass another folder as the argument. The script
maps the reference client's files onto the names above:

| Sound | Reference file |
|---|---|
| move, capture, castle, check, promote | `default/move-self`, `capture`, `castle`, `move-check`, `promote` (the board's "default" sound theme) |
| brilliant, correct, incorrect | `assets-ds/brilliant-*`, `correct-*`, `incorrect-*` |
| result_good, result_ok, result_bad | `assets-ds/training-result-{good,ok,bad}-*` |

Never commit these files. No openly licensed set sounds close enough to ship as a default. Lichess's
standard set is listed as non-free in lila's `COPYING.md`. Its AGPL sets (futuristic, nes, piano,
sfx) are not wooden piece sounds.

## Sources

- **Web Game Review** (client 2026.10.3-hotfix). Analysed from its bundles: the move-sound chooser in
  the shared eager chunk, and the review and retry handlers in `analysis.js`. Also observed while
  stepping through a signed-in review with `AudioBufferSourceNode.start` hooked. Retry was read from
  code only.
- **Android 4.10.15** (JADX): `CBSoundPlayerImpl`, `soundandhaptics/impl/sound/*` and
  `GameReviewViewModel`. It agrees with the web client except where noted below.

## Move sound

Exactly one sound plays per move. The first rule that matches wins:

| Rule | Sound |
|---|---|
| SAN has `+` or `#` (so a mate counts as a check) | check |
| Promotion, including a capture that promotes | promote |
| Capture, including en passant | capture |
| Castling | castle |
| Anything else | move |

The web client also has a premove rule and an own/opponent split. Neither applies to review: no
"playing as" colour is set there, so quiet moves by both sides play the same sound. Reaching a mate
in review plays only the check sound, with no game-end sound.

## Navigation

| Action | Sound |
|---|---|
| Step forward (→, Next, autoplay) | the move arrived at |
| Click a move or jump to it (End, graph, move list), backwards jumps included | the move arrived at |
| Step back one move (←) | the move **taken back**, not the one landed on |
| Go to the start position (Home) | none |

## Sidelines

The reader's own moves (exploring a sideline, `docs/explore-mode.md`) follow the same rules.
- **Playing a move** plays its move sound.
- **Stepping back one move** plays the move taken back.
- **Stepping forward, or clicking a sideline move,** plays the move arrived at.
- **Brilliant** never sounds in a sideline, because sideline moves are not classified.
- **Playing the game's own move** follows the game and sounds like stepping forward.
- **Back from a line's first move** lands on its branch, a game position, and plays the move taken back.
  **→ from there** follows the game, with the game's sound.
- **Opening the variation picker** makes no sound. Following a choice plays the move arrived at.

This is this app's own choice. The reference client's analysis board was not examined for sound.

## Brilliant

The brilliant sound plays together with the move sound when all of these hold:

- the board arrives at a move classified Brilliant, by stepping forward or by selecting it (never by
  stepping back);
- the move is on the main line, not in a line preview or retry;
- the move was played by the reviewing player.

The reference client checks the last rule against the signed-in username. Here it uses the side
chosen under "This is me" at import, and either side counts when none was chosen.

No other classification has a sound. Great, best, miss, mistake, blunder and the rest are silent on
the web. The Android app gives some of them a haptic only.

## Retry

When a retry is finished, a sound plays for the classification of the move found:

| Retry move | Sound |
|---|---|
| Brilliant, Great, Tricky, Best | correct (two-part rising blip) |
| Excellent | result good (rising three notes) |
| Good, Book, Forced | result ok (up, then down) |
| Inaccuracy, Mistake, Blunder, Miss | result bad (falling three notes) |

The retry move also gets its normal move sound. This app only accepts best or excellent answers, so
"ok" and "bad" are mapped but never reached. A wrong attempt plays an "incorrect" sound. That part is
this app's own choice: the reference client was not observed doing it.

## Not reproduced

- Key Takeaways navigation sound: this app has no takeaway pages after the last move.
- Game start/end, illegal move, premove, low time and draw offer: these are play-only events.
- Engine and coach line previews here play each move's sound. The reference client's line previews
  were not examined.
