# Why our Book labels differ from Chess.com's (2026-11-14)

Question: the opening part of our reviews is "quite off" from Chess.com's. Why?

Short answer: Chess.com uses the same kind of rule on a much bigger, slightly different book.

- Its book has **51,752 "book" positions**. Ours has **7,982**. We hold 11.5% of its set.
- Its book also marks **2,220 positions "notable"**: named lines (traps, odd first moves) that are
  *not* Book. Our lichess list names many of the same lines and calls them Book.
- Its rule needs the position **before and after** the move to be in the book. Ours only checks
  the position after.

With Chess.com's own book and that rule, all 42,319 plies of the 577 calibration games match its
labels exactly (3,621 Book, 0 wrong). So nothing else is involved: no engine, rating or depth.

All numbers come from `tools/book/` (scripts) and `tools/book/results/` (their output).

## 1. How far off we are

577 calibration games (`tests/calibration/cc-reviews`), 42,319 plies, our shipped rule rebuilt in
Python (`book_gap.py`, same as `openings.rs` + `analysis/mod.rs::book_flags`).

| | Plies |
|---|---|
| Chess.com Book | 3,621 (6.3 per game) |
| Our Book | 3,039 (5.3 per game) |
| Book in both | 2,885 |
| Chess.com Book, ours not (missed) | 736 |
| Ours Book, Chess.com not (extra) | 154 |

Precision 0.95, recall 0.80. Per game, the last Book ply matches in 42% of games. Chess.com's book
runs longer in 42% (by 1-2 plies in 24%, 3-4 in 12%, 5+ in 6%, up to 18). Ours runs longer in 16%.

### It gets worse with rating

| Max Elo in the game | Games | Chess.com Book per game | Ours per game | Recall |
|---|---|---|---|---|
| < 1000 | 255 | 5.0 | 4.6 | 0.85 |
| 1000-1599 | 171 | 5.9 | 5.2 | 0.84 |
| 1600-2199 | 75 | 7.4 | 5.9 | 0.78 |
| 2200+ | 76 | 10.4 | 7.0 | 0.66 |

Strong players stay in theory longer, and our book stops sooner. In a titled game we miss about a
third of Chess.com's Book moves.

## 2. What the user sees (run `sp-base`, our defaults, 575 games)

`book_impact.py`:

- **The 736 missed Book moves get other icons:** Best 329, Excellent 229, Good 134,
  Inaccuracy 31, Great 7, Mistake 3, Forced 2, Brilliant 1. A Great or Brilliant on move 4 looks
  plainly wrong next to Chess.com. 686 of them also get a coach note.
- **The 154 extra Book moves hide real errors.** Chess.com grades them Best 44, Good 36,
  Inaccuracy 32, Excellent 18, Mistake 14, Great 6, Blunder 2, Miss 2. Typical lines: 1.e4 e5
  2.Qh5 (8 games), 2...Qf6, 3...h6, 2.c4.
- **Accuracy barely moves.** A missed Book move scores 96.2 on average instead of 100. If every
  Chess.com Book ply scored 100, 288 of 1,150 game sides would change, by +0.29 on average and at
  most +1.8 points. The gap is in the labels, not the accuracy number.

## 3. What Chess.com's book is

Source: `embedded_book` in `libcee.so` 4.10.15 (local oracle in WSL `~/work/re-great/out`, never
committed). Earlier work (mismatch-analysis.md §3) found the 53,972 records and the Polyglot keys.
This round decoded the rest:

- **Header:** record count 53,972, then 3,101 (the number of opening names).
- **Record (32 bytes):** Polyglot key, name id, family id, then three offsets into a string table:
  the **type**, the line's moves, the ECO code and the opening slug.
- **Type string:** offset 0 = `"book"` (51,752 records), offset 2801 = `"notable"` (2,220).
  The earlier note read the two id fields as "game counts". They are ids, not counts.
- **Moves:** Chess.com's TCN move encoding (two characters per move). All 53,972 lines decode to
  legal moves, and 53,970 replay to the record's own Polyglot key.
- **Names:** slugs like `Ruy-Lopez-Opening-Birds-Defense-4.Nxd4-exd4-5.O-O` (3,102 base names,
  491 ECO codes). These are the pages under `chess.com/openings/`. A game PGN's `ECOUrl` equals
  the slug of the last book position on the game's path in 483 of 576 games.
- **Shape:** a closed tree. Every prefix of every line is also a record.
- **Notable records** are offbeat or trappy named lines: Kadas, Clemenz, Sodium, Barnes, Ware and
  Amar openings at ply 1, the Duras Gambit, 1...Na6 vs Réti, the Australian Defense, and so on
  (median depth 8).

### Size by depth

| Ply | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 24 | 30+ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Chess.com positions | 161 | 717 | 1,677 | 2,553 | 3,346 | 3,744 | 3,768 | 3,352 | 2,647 | 1,925 | 852 | 608 |
| Our positions | 134 | 400 | 621 | 631 | 627 | 531 | 410 | 265 | 180 | 109 | 33 | 7 |

Median depth: Chess.com 14 plies, ours 10. Max 42 vs 36. At ply 2 the two are close. At ply 4
Chess.com has 1.8 times our positions, at plies 6-14 3-9 times, and from ply 16 more than 10 times.

### Overlap

| | Positions |
|---|---|
| In both | 7,668 |
| Only Chess.com | 46,304 |
| Only ours | 314 |

96% of our positions are in Chess.com's book, but **1,699 of them (21%) are typed "notable"**.
115 of our 3,865 named line ends are not in its book at all (mostly gambits and side systems,
for example the Portuguese Gambit, Dinic Gambit, Kopec System).

## 4. The exact rule

`cc_book_residual.py`, all 42,319 plies, Chess.com's own book:

| Rule | Book both | Extra | Missed | Precision | Recall |
|---|---|---|---|---|---|
| Position after is in the book (any type) | 3,621 | 211 | 0 | 0.945 | 1.000 |
| Before and after in the book (any type) | 3,621 | 138 | 0 | 0.963 | 1.000 |
| After is a "book" record | 3,621 | 77 | 0 | 0.979 | 1.000 |
| Before in book, after is "book" | 3,621 | 8 | 0 | 0.998 | 1.000 |
| **Before and after are both "book" records** | **3,621** | **0** | **0** | **1.000** | **1.000** |

So: **a move is Book when the position before it and the position after it are both "book"
positions in Chess.com's book.** The start position is a "book" record. Transpositions count: of
Chess.com's Book plies, 131 (in 35 games) come after a non-Book ply. The 134 plies that land on a
"notable" position are never Book; Chess.com grades them normally (Good 39, Best 33, Inaccuracy
27, Excellent 15, Mistake 14, Great 3, Blunder 2, Miss 1).

This closes open question 3 (open-questions.md): the rule is known, and only the data differs.

## 5. Why each of our errors happens

### Missed Book moves (736)

| Cause | Plies |
|---|---|
| **Deeper:** we already left our book; Chess.com's line goes on | 460 (62%) |
| **Sibling:** the position before is in our book, but this common move is not | 276 (38%) |

A game's *first* missed Book move is nearly always a sibling, and the deeper misses follow it.
Common first misses: 1.e4 e6 2.Nf3 d5 3.exd5 (7 games), 1.e4 d5 2.e5 (5), 1.e4 b6 2.Nf3 (5),
1.e4 e5 2.Nf3 Nc6 3.Nc3 Bc5 (4), 1.e4 c5 2.Nf3 d6 3.Bc4 (4), 1.d4 d5 2.Bf4 e6 (3), and
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Bd3 (2).

The lichess list holds *named* lines. A common move that does not start a new name (3.exd5 in the
French with 2.Nf3, 2.e5 vs the Scandinavian, London move orders) has no line, so it is not Book.
Chess.com names nearly every position in its tree (`...-5...Nc5-6.Bg5-Be7`), so its tree holds
these moves.

Missed plies by distance past our last Book ply: 1 ply 276, 2 plies 168, 3 plies 107, 4 plies 69,
5+ plies 116.

### Extra Book moves (154)

| Cause | Plies |
|---|---|
| Chess.com's book stops here, ours goes on (mostly "notable" lines: 2.Qh5, 2...Qf6, 3...h6) | 91 |
| We transpose back into our book; Chess.com does not (its rule needs the position before) | 63 |

## 6. Things that do not explain it

| Idea | Result |
|---|---|
| Different position keys (en passant, castling) | No. Ours: EPD with legal en passant. Polyglot also counts en passant only when a capture is legal. |
| Chess.com stops Book after the first non-Book move | No. 131 Book plies come after a non-Book ply. Our "unbroken" option is worse (recall 0.77). |
| Chess.com drops bad moves from Book | No. Its Book includes moves we grade Inaccuracy or worse (78 plies). A "no Book for Inaccuracy or worse" filter would remove 64 extras but also 78 correct ones. |
| Engine, depth, rating | No. Book is decided before any of them (§4 is exact without them). |
| Our book file is out of date or differs between repos | No. The public and private repos ship the same five TSVs (3,865 lines) and the same code. |
| The "before and after" rule alone, on our book | No gain: agreement 97.90% → 97.84% (recall 0.80 → 0.78). It only helps with a bigger book. |

## 7. What would fix it

We cannot ship Chess.com's book: it is Chess.com's data, taken from its binary (THIRD_PARTY.md,
legal-risk notes). The fix is a bigger public book plus Chess.com's rule.

### Candidate books, measured (`cc_book_compare.py`)

| Book | Positions | Covers Chess.com's "book" set | Precision | Recall | Plies agreeing |
|---|---|---|---|---|---|
| Ours now (lichess `chess-openings`, CC0) | 7,983 | 11.5% | 0.949 | 0.797 | 97.90% |
| eco.json named (lichess + SCID + Wikipedia + Wikibooks + others) | 15,511 | 24.0% | 0.941 | 0.870 | 98.42% |
| eco.json + interpolated + ours | 15,979 | 24.6% | 0.941 | 0.873 | 98.45% |
| Chess.com's own (reference only) | 51,752 | 100% | 1.000 | 1.000 | 100% |

eco.json ([JeffML/eco.json](https://github.com/JeffML/eco.json), MIT for the package) is a quick
win: recall +7 points at the same precision. Risk: its data merges sources with their own terms
(SCID, Wikipedia and Wikibooks text is CC BY-SA). Check before shipping; this is not legal advice.

It still covers only a quarter of Chess.com's tree, because it is also a list of names.

### The real fix: a popularity book from CC0 games

Chess.com's tree looks like "every position reached often enough in real games, kept as a closed
tree". We can build the same from the lichess game database (CC0, [database.lichess.org](https://database.lichess.org)):

1. Stream one or more monthly dumps. Keep the first 30-40 plies of rated games.
2. Count each position (Polyglot key). Keep positions seen at least N times, and only when their
   parent is kept (a closed tree, like Chess.com's).
3. Choose N, the rating floor and the ply cap by comparing the **set** with Chess.com's book
   (size per depth, overlap), not with the labels. That keeps it free of label overfitting, as
   mismatch-analysis.md §8 asked.
4. Rare named traps (2.Qh5, Kadas) fall out by themselves, which copies the "notable" split.
5. Keep the lichess TSVs for opening **names** only.
6. Switch the rule to "before and after both in the book" (§4). Remember the start position.
7. Measure on the 577 games, then on the holdout split.

Cost and limits:

- One month of lichess games is about 30 GB compressed. This host is short of memory, so build
  on a bigger machine, or sample a few million games. Counting needs a hash map of tens of
  millions of keys; a two-pass or count-min approach keeps it small.
- The book ships as a file of about 50k keys (under 1 MB as sorted u64s).
- The lichess opening explorer API now returns 401 without a login, so a crawl needs a token and
  would take hours at its rate limit. The dump is simpler.
- Lichess players are not Chess.com players, so the tree will not match exactly. Expect most of
  the missing recall back, not all of it.

### Code changes for the rule (when the new book lands)

- `analysis/mod.rs::book_flags`: Book when `contains(before) && contains(after)`, with the start
  position counted as in book. Drop `book_requires_unbroken` or keep it as the strict option.
- `analysis/sideline.rs`: same rule for explored moves.
- `openings.rs`: load the new key set; keep TSV names for display.

## 8. Files

| File | What |
|---|---|
| `tools/book/book_gap.py` | Our rule vs Chess.com's labels: totals, rating bands, causes, examples |
| `tools/book/cc_book_compare.py` | Decodes the local Chess.com book export; size, depth, overlap; scores other books |
| `tools/book/cc_book_residual.py` | Finds the exact rule (before/after, "book" vs "notable") |
| `tools/book/book_impact.py` | What our labels and accuracy are on the disagreeing plies |
| `tools/book/results/*.md` | Output of the four scripts on 2026-11-14 |

The Chess.com book export (`ccbook.tsv`) was made in session scratch from the WSL oracle and is
not committed.
