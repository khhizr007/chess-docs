# Research notes: building a move-by-move chess *coach* (explanations, not just classifications)

Compiled 2026-10-19 for the chess-review app (Rust + Stockfish/UCI + shakmaty backend, React frontend).
Scope: academic work on chess commentary, open-source motif detectors, what is publicly known about Chess.com's Game Review coach and DecodeChess, and the pedagogy of move feedback.
Items marked **[UNVERIFIED]** could not be confirmed from a primary source.

---

## 0. TL;DR: what the evidence says to build

1. **Analysis first, language second.** Every serious system that works keeps the chess facts in a deterministic layer and uses language only to verbalise them. That includes CCC/NAACL 2025, ACT-Eval 2026, Take Take Take's coach (Magnus Carlsen's company, AI Engineer Europe 2026), TNG's AI chess channel, and the lichess/ChessBase/DecodeChess template systems. The layers are an engine plus symbolic detectors plus a human-likelihood model. The verbaliser can be templates or a small, fast LLM. Free-running LLMs hallucinate badly. GPT-5.4 without tools gets 22% of atomic chess sub-claims wrong, and small open models get more than 40% wrong (ACT-Eval, arXiv 2608.04240). Tool and fact grounding cuts that roughly in half, but it doesn't eliminate errors.
2. **Use a detector vocabulary like lichess's puzzle themes.** The lichess-puzzler tagger (`cook.py`) is the best open, documented detector set. It covers about 60 themes: fork, pin, skewer, discovered attack, hanging piece, trapped piece, deflection, attraction, interference, x-ray, clearance, intermezzo, capturing the defender, many named mates, zugzwang via null move, and more. It runs on a *forcing line* (the puzzle solution), which maps directly onto our use case. Run it on the engine PV that refutes the played move ("what you allowed") and on the best-move PV ("what you missed"). The code is **AGPL-3.0**, so reimplement it in Rust/shakmaty from the algorithmic descriptions below rather than porting the code verbatim. The puzzle *data* is CC0.
3. **Add positional "concepts" as eval-term deltas.** CCC (Kim et al., NAACL 2025) and McGrath et al. (PNAS 2022) both use the *Stockfish 8 classical evaluation terms*: Material, Imbalance, Pawns, Knights, Bishops, Rooks, Queens, Mobility, King safety, Threats, Passed pawns, Space. They rank which concepts a move changed most and feed the top ones to the LLM as hints. Stockfish 16+ removed the classical eval, so we'd have to compute these ourselves, either in Rust or by running an old SF (≤15.1, GPL-3) `eval` trace in a side process.
4. **Prioritise ruthlessly: one reason per move.** Pick the single most important reason, name the motif, and show the refutation or the missed line. Chess.com's coach, DecodeChess ("Idea / Problem / Solution"), and the pedagogy literature (Shute 2008; Hattie and Timperley 2007) all point the same way.
5. **Make it rating-aware with Maia.** Maia-2 (MIT) or Maia-3 (AGPL-3.0) gives P(move | rating). Use it to say "this was a hard move to find at your level" versus "a natural move that loses to …". Take Take Take and TNG both do this.
6. **Offer a Socratic retry mode.** Lichess "Learn from your mistakes" and Chess.com "Retry" ask the player to find a better move before revealing it. Self-explanation and prediction research in chess novices (de Bruin et al. 2007) supports adding a "why" prompt. Hint ladders (pointing hint → teaching hint → bottom-out hint, VanLehn 2006) give the structure.
7. **Chess.com's explanation engine is not documented publicly.** The Game Review launch post credits an "explanation engine" team (@dwcoates, @DanTheCabin, @2tp, @dpervov, @nollaversioit) and nothing more. I found **no evidence that Chess.com acquired DecodeChess**. DecodeChess's only known platform deal was with Chessify (Jan 2023 to Jan 2024). The "CEE / ~250 board-event tags / coach speech" description in our brief has no public source I could find **[UNVERIFIED publicly]**.

---

## 1. Academic work on move commentary and explanation

### 1.1 Jhamtani et al., ACL 2018: "Learning to Generate Move-by-Move Commentary for Chess Games from Large-Scale Social Forum Data"
- Paper: https://aclanthology.org/P18-1154/ (PDF https://aclanthology.org/P18-1154.pdf). Code and crawler: https://github.com/harsh19/ChessCommentaryGeneration. The repo has **no licence** and needs Python 2.7, PyTorch 0.3, and PyQt4. It ships a GameKnot crawler, not the data itself.
- **Data:** about 298K move/comment pairs from about 11.6K annotated GameKnot games, split 7:1:2 by game. This "GameKnot Chess Commentary" set became the benchmark that most later work uses.
- **Comment categories** (with a classifier to split the data):
  - Move Description: 8%
  - Quality: 3.7%
  - Comparative: 31%
  - Planning/Rationale: 12.6%
  - Contexts (game state, aggression/defence)
  - General (idioms, emotions)
- **Features** (extracted with python-chess plus Stockfish, embedded, then "feature conjunctions" through a BiLSTM and a selection/attention mechanism into an LSTM decoder, the GAC model):
  - *Move features:* piece type, from-square, to-square, captured piece, castling, check.
  - *Threat features:* which opposing pieces attack the moved piece before and after the move, and which opposing pieces the moved piece attacks.
  - *Score features:* Stockfish eval before and after the move, and average pawn rank of each side.
- **Baselines** included hand-written templates (TEMP). Templates were rated fluent and correct, but repetitive (low n-gram entropy).
- **Results:** BLEU scores are tiny on most categories (for example, Description BLEU ≈ 1–3). In a human study, GAC(M+T) was not significantly different from the human ground truth on correctness, and it was more fluent.
- **Key observation:** about 30% of the *human* ground-truth comments were judged "not valid for the given board move". Forum data is noisy, so learning end-to-end from it is a poor path to a trustworthy coach.
- **Takeaway for us:** threat features (attackers of the moved piece before and after, pieces newly attacked) carried most of the signal. Those are trivially computable with shakmaty.

### 1.2 Zang, Yu, Wan, ACL 2019: "Automated Chess Commentator Powered by Neural Chess Engine" (SCC)
- arXiv: https://arxiv.org/abs/1909.10413. Code was promised at https://github.com/zhyack/SCC (no licence). Kim et al. 2025 report it **could not be reproduced**.
- **Idea:** jointly train an internal neural engine and per-category LSTM generators.
  - The engine is a CNN over 20 feature planes with policy and win-rate heads. It was pretrained on 36M FICS positions from players rated 2000 or higher.
  - The engine supplies board encodings, an alternative "best" move for Comparison, simulated continuations for Planning and Contexts, and the win-rate change for Quality.
- **Results:** Quality BLEU-4 was 20.06 (versus 16.90 for GAC). Human Overall was 3.61/5 (ground truth 3.84, templates 3.56). Templates scored *higher on accuracy* (4.03 vs 3.91).
- **Takeaway:** neural generation barely beats templates on overall quality and loses on accuracy.

### 1.3 Lee, Wu, Dinan, Lewis (Meta), 2022: "Improving Chess Commentaries by Combining Language Models with Symbolic Reasoning Engines"
- arXiv: https://arxiv.org/abs/2212.08195. No code released.
- **Symbolic engine:** Leela Chess Zero.
- **LM input:**
  - PGN history.
  - The board as a piece list ("White R_c5").
  - An "attack state" list of attacker$attacked pairs ("White R_a1$P_a2").
  - The move in SAN.
  - Control tags as prefixes: `[Commentary Type]`, `[Move Quality]` (bucketed from Leela win-probability loss, "similar to Chess.com classifications"), `[Suggested Move]` (Leela best move), and a length tag.
- **Model:** BART trained on about 374K GameKnot triplets.
- **Tag extractor:** pre-trained on 56K forum Q&A pairs, then fine-tuned on 1.8K/610/830 manual labels.
- **Human A/B preference vs Jhamtani:**
  - Move Description: 72%
  - Move Quality: 75%
  - Comparative: 72%
- **Takeaway:** conditioning the LM on *engine-derived control codes* (quality bucket, suggested move) plus an explicit attack list is what produced the gain. This is the earliest clean "symbolic facts → controllable LM" design.

### 1.4 Kim, Goh, Hwang, Cho, Ok (POSTECH/KRAFTON), NAACL 2025: "Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation" (CCC and GCC-Eval)
- arXiv: https://arxiv.org/abs/2410.20811. ACL: https://aclanthology.org/2025.naacl-long.481.pdf. Code: https://github.com/ml-postech/concept-guided-chess-commentary. The repo has **no licence file**, so it is all rights reserved by default.
- **Concept vocabulary:** 22 concepts taken from **Stockfish 8 eval terms**: Material, Imbalance, Pawns, then White/Black for each of Knights, Bishop(s), Rooks, Queens, Mobility, King safety, Threats, Space, and Passed pawns. The authors say fork, pin, doubled pawns, open file, and similar were *not* used, for lack of labels.
- **Concept extraction:**
  1. Score 200K Lichess positions with each SF8 term.
  2. Take the top 5% as positives and the bottom 5% as negatives.
  3. Train a linear SVM per concept on **LeelaChessZero T78** activations at layer 40, just before the policy and value heads.
  4. The SVM normal is the concept vector, and the signed distance is the concept score. Probe accuracy averages about 0.91 (bishops and queens are worst, at about 0.75).
- **Prioritisation:** concept score after the move minus before; the largest |Δ| ranks first.
- **Prompt (from `02_ccc_generation.ipynb`):** GPT-4o at temperature 0.01–0.1, with a system message roughly: "chess commentary assistant consists of board, move, evaluation by stockfish, important concept candidates and comment… generate correct, clear, concise and self-contained comment for the move, using concept candidates as a hint." Each user turn contains:
  - `board: <FEN>`
  - `actual move: 18... Qc5+`
  - `evaluation: actual move - Qc5+ 361cp, best move - Qc5+ 342cp, second best move - Bxc2 -6cp`
  - `concept candidates: fork, White king, White bishop`
  - Few-shot assistant turns first write a chain-of-thought "concept evaluation:" that validates or rejects each candidate ("White rook – it does not engage in attack. It is irrelevant concept."), then a `comment:`.
  - The paper also describes feeding "an enumeration of all existing attacks". The `get_all_attacks` helper lists every pseudo-legal capture for both sides in LAN, to stop references to non-existent pieces.
- **Human eval** (5 raters rated 1500+ on Chess.com, 50 moves, scores 0–1):

  | System | Correctness | Relevance | Completeness | Clarity | Fluency |
  |---|---|---|---|---|---|
  | GPT-4o alone | 0.36 | 0.49 | 0.40 | 0.72 | 0.84 |
  | GPT-4o + engine | 0.43 | 0.56 | 0.49 | — | — |
  | CCC (engine + concepts) | 0.60 | 0.67 | 0.59 | 0.80 | 0.91 |
  | Human reference | 0.62 | 0.52 | 0.30 | — | — |
  | GAC (Jhamtani) | 0.63 | — | — | — | — |

- **Error analysis** (rate of each error type: GPT-4o → +engine → +concepts):

  | Error type | GPT-4o | + engine | + concepts |
  |---|---|---|---|
  | Illegal move / nonexistent piece | 0.46 | 0.28 | 0.20 |
  | Tactical misunderstanding | 0.46 | 0.40 | 0.26 |
  | Positional misunderstanding | 0.28 | 0.26 | 0.28 |
  | Wrong evaluation | 0.32 | 0.30 | 0.34 |

  Grounding fixes *factual and tactical* errors but not deeper positional reasoning.
- **GCC-Eval:** a G-Eval-style GPT-4 judge that scores relevance and completeness with engine hints (actual move cp, expected reply, best and second-best move) plus clarity and fluency, as a probability-weighted 1–5 score. Pearson correlation with humans is 0.40–0.56, far better than BLEU/ROUGE.
- **Mate-in-1 side experiment:** adding the engine answer makes all LLMs about 98% correct (trivially). A "mate-in-one" concept hint alone lifts GPT-4o by 17 points.
- **Limitations the authors state:** experts only, no novice study, concept set limited to SF8 terms, low inter-annotator agreement.

### 1.5 Feng et al., NeurIPS 2023 Datasets and Benchmarks: "ChessGPT: Bridging Policy Learning and Language Modeling"
- arXiv: https://arxiv.org/abs/2306.09200. Code, models, and data: https://github.com/waterhorse1/ChessGPT (**Apache-2.0** code; some data subsets, such as Megabase and chesspublishing, are commercial and not released).
- **Data:** 28M documents, including 17.5M Lichess games, 3.2M puzzles, about 245K annotated games (1.3M board/language pairs), YouTube, books, forums, and Reddit.
- **Models:** ChessCLIP (board ↔ annotation contrastive) and ChessGPT-Base/Chat (2.8B, from RedPajama-3B).
- **Evaluation:** state tracking (85–99%), UCI→FEN, value multiple choice, annotation multiple choice (ChessCLIP 63.6%), mate-in-1 (Base 71%). Elo conditioning has almost no effect.
- **Not evaluated:** open-ended explanation quality.
- **Takeaway:** a useful corpus and baseline, but a 3B chess-LM is not a reliable explainer. Kim et al. found ChessGPT weaker than GPT-4o even with hints.

### 1.6 Wang et al., NAACL 2025 (short): "Explore the Reasoning Capability of LLMs in the Chess Testbed" (MATE dataset)
- arXiv: https://arxiv.org/abs/2411.06655. Site: https://mate-chess.github.io. Dataset licence not stated **[UNVERIFIED]**.
- **Data:** about 1M Lichess positions, each with 2 candidate moves (Stockfish score gap above a threshold), annotated with:
  - *Strategy:* rule-based from expert-written rules, in five categories (material count, piece activity, pawn structure, space, king safety), each with about 20 linguistic templates.
  - *Tactic:* a Stockfish line plus a factual description (pins, forks, x-rays, windmills, …).
- **Result:** Llama-3-8B fine-tuned on strategy plus tactic explanations reached 95.2% at picking the better move, versus 76.6% for o1-preview.
- **Takeaway:** for *us* the useful parts are the five strategic category names and the evidence that expert-rule templates produce high-quality supervision text.

### 1.7 Wen, Tang, Anderson (U. Toronto CSSLab), 2025: "ChessQA: Evaluating Large Language Models for Chess Understanding"
- arXiv: https://arxiv.org/abs/2510.23948. Code (**MIT**): https://github.com/CSSLab/chessqa-benchmark. Data: https://huggingface.co/datasets/wieeii/ChessQA-Benchmark.
- **Categories:**
  - Structural (piece arrangement, check, capture/control/protect squares, legal moves, state tracking)
  - Motifs (pins, skewers, forks, batteries, discovered checks, double checks), with custom python-chess ray-scan detectors
  - Short Tactics (Lichess puzzles by theme)
  - Position Judgment (cp buckets)
  - Semantic (pick the true comment among distractors, built from ChessBase 17 commentary)
- **Results:** GPT-5 (thinking) scores 79% overall. Structural is about 97%, Position Judgment only about 40%, and Short Tactics averages 17%.
- **Takeaway:** even frontier LLMs cannot be trusted to find tactics or judge positions. They *can* read board facts that are handed to them.

### 1.8 Hebbar, Sheng, Oh, Viswanath, Aug 2026: "Hallucinations on the Board: Tool-Augmented Evaluation of LLM Chess Commentary" (ACT-Eval)
- arXiv: https://arxiv.org/abs/2608.04240. Code is said to be at https://github.com/hebbarashwin/act_eval, but that URL returned 404 when checked **[UNVERIFIED availability]**.
- **Method:**
  1. Decompose commentary into atomic claims and then sub-claims.
  2. A judge LLM verifies each one with **mandatory tool use** (15+ tools such as `get_piece_at`, `get_legal_moves`, `get_attackers`, `try_variation`, `eval_move`, `get_top_moves`, `get_engine_eval`; Stockfish 14.1 at depth 18–22).
  3. Match the verified claims to expert gold atoms to measure coverage.
- **Error taxonomy:** board comprehension, legality, quality evaluation, tactical reasoning, other.
- **Verification rules worth copying:**
  - Use the pre-move FEN for "was true before" claims and the post-move FEN for "creates".
  - "Prevents" means a tactical refutation, not illegality.
  - A forcedness claim must hold on *all* sampled opponent branches.
- **Results** (sub-claim error rate):

  | Model | No tools | With tools |
  |---|---|---|
  | GPT-5.4 | 22.0% | 9.2% |
  | Claude Opus 4.7 | 20.8% | 13.4% |
  | Gemini 3.1 Pro | 10.8% | 7.5% |
  | DeepSeek V4 Pro | 36.7% | 14.4% |
  | Qwen3-8B / 32B | 55% / 44% | — |

  Move-quality F1 jumps from about 12–23 to 64–98 with tools. Recall of expert ideas stays low (44–61%).
- **Takeaway:** a ready-made *test methodology* for our coach. It also shows that verified facts alone don't surface the key idea, so we still need a prioritiser.

### 1.9 Cui, Ling, Ng, Jul 2026: "Communicating Chess Strategies in Natural Language"
- arXiv: https://arxiv.org/abs/2607.11486.
- **Method:**
  - Build a pruned Stockfish-16 "strategy tree" for each Lichess puzzle: the best move for the solver and the top-k replies for the opponent.
  - An LLM (o3 or gpt-oss-120b) verbalises it under three conditions: tree only, lichess *theme keywords* only, or both. An optional self-critique loop runs 3 rounds.
  - Descriptions are evaluated by letting a player (an LLM, or 30 students) solve the puzzle with the description, against adversarial engine branches.
- **Findings:**
  - Verbalising the concrete tree helps almost as much as raw JSON (o3: 0.851 vs 0.877 optimal vs 0.622 with no help).
  - **Concept keywords alone give little gain.**
  - Self-critique helps strong models and hurts weak ones.
  - Humans benefited more from human-written solutions than from LLM ones.
- **Takeaway:** naming the motif isn't enough. The explanation must include the *concrete line*, including the opponent's best defences.

### 1.10 Tang, Wen, …, Anderson, 2026: "Grounded Chess Reasoning in Language Models via Master Distillation"
- arXiv: https://arxiv.org/abs/2603.20510.
- **Method:** distil an expert system's computation into chain-of-thought explanations with SFT plus RL, using theme-balanced sampling (lichess themes).
- **Result:** a 4B model, "C1", reaches 48.1% on their tactics benchmark. It beats open models and most frontier models while using about 100× fewer tokens.
- Code and weights were not linked on the abstract page **[UNVERIFIED]**.
- **Relevance:** a route to a small self-hosted explainer, long term.

### 1.11 Parfenova, BlackboxNLP@EMNLP 2026: "Do Chess Explanations Reflect Model Decisions?"
- arXiv: https://arxiv.org/abs/2609.22245.
- **Finding:** LLM explanations of their *own* chess moves are often not faithful. Plausible language ≠ the actual reasoning ≠ correctness.
- **Takeaway:** don't let the LLM pick or justify moves. Have it describe engine and detector facts only.

### 1.12 Concept probing and discovery in engines (positional-concept background)
- **McGrath, Kapishnikov, Tomašev, Pearce, Hassabis, Kim, Paquet, Kramnik, PNAS 2022: "Acquisition of chess knowledge in AlphaZero."**
  - arXiv: https://arxiv.org/abs/2111.09259. PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC9704706/.
  - Linear probes on AlphaZero activations for human concepts, largely the **Stockfish 8 public eval terms** plus custom concepts (material, mobility, king safety, threats, passed pawns, space, …).
  - Shows *when* in training and *where* in the network each concept appears (material emerges around 32K steps).
  - Exact custom concept list not re-verified here **[UNVERIFIED in detail]**.
- **Schut, Tomašev, McGrath, Hassabis, Paquet, Kim, arXiv 2023 / PNAS 2025: "Bridging the human–AI knowledge gap through concept discovery and transfer in AlphaZero."**
  - arXiv: https://arxiv.org/abs/2310.16410.
  - Finds *novel* concept vectors with convex optimisation, filtered for teachability and novelty.
  - Four top GMs (current or former world champions) improved on concept prototype puzzles after studying them.
  - Interesting, but not practical for a product coach.
- **Palsson and Björnsson, IJCAI 2023: "Unveiling Concepts Learned by a World-Class Chess-Playing Agent"** (https://www.ijcai.org/proceedings/2023/541). Probes Stockfish NNUE for concepts.
- **"Towards Piece-by-Piece Explanations for Chess Positions with SHAP"** (arXiv 2510.25775, CEUR Vol-4097).
  - Attributes engine eval to individual pieces by ablation.
  - Gives a cheap "which piece matters" signal (for example, "your bishop on g7 is doing all the defensive work").
- **Puri et al., ICLR 2020: "Explain Your Move: Understanding Agent Actions Using Specific and Relevant Feature Attribution" (SARFA)** **[from memory, not re-verified]**. Perturbation-based saliency for Stockfish moves.
- **Sadikov, Možina, Guid, Krivec, Bratko, CG 2006 / LNCS 2007: "Automated Chess Tutor"** (DOI 10.1007/978-3-540-75538-8_2).
  - Probably the "Sadmine" reference in the brief: Sadikov et al.
  - Turned an engine's evaluation function into a commentator by attaching comments to *goals achieved or preserved* along the principal variation. Claims "relatively solid commenting of positional aspects".
  - I believe the engine was Crafty and that comments came from changes in eval-function features along the PV, but I could not access the full text **[UNVERIFIED]**.
  - The same Ljubljana group later used argument-based ML to learn concepts like "bad bishop".

### 1.13 Human-move models: "is this mistake natural at your rating?"
- **Maia (KDD 2020):** https://arxiv.org/abs/2006.01855.
- **Maia-2 (NeurIPS 2024):** https://arxiv.org/abs/2409.20553. Code: https://github.com/CSSLab/maia2 (**MIT**). pip `maia2`.
  - API: `inference_each(model, prepared, fen, elo_self, elo_oppo)` returns `move_probs` and `white_expected_score`.
  - A single skill-aware network (attention over Elo embeddings) is coherent across rating levels.
- **Maia-3 / "Chessformer"** (ICLR 2026, arXiv 2605.19091): https://github.com/CSSLab/maia3 (**AGPL-3.0**). A rating-conditioned transformer with 79M and 5M variants, trained on Lichess 2023–2025. It runs as a UCI engine. The README recommends Maia-3 for new projects.
- **Uses for a coach:**
  - (a) Difficulty of the best move: low P(best | rating) means it was "hard to find, don't feel bad".
  - (b) Temptation: high P(played | rating) for a blunder means "this is a natural-looking move, here's the trap".
  - (c) Pick the *human-plausible* opponent reply to show, not only the engine's.
  - Take Take Take and TNG both use Maia exactly this way (see §3.4).

### 1.14 Other relevant work
- **Shymanski, Brue, Sen, 2025: "Not All Explanations are Created Equal: Investigating the Pitfalls of Current XAI Evaluation"** (arXiv 2511.03730).
  - A chess-concept teaching agent compared no, placebic, and actionable explanations.
  - Finding: *almost any* explanation raises user satisfaction, so satisfaction surveys are not evidence that explanations teach anything.
  - Implication: evaluate with comprehension tests or retry success, not thumbs-up rates.
- **Caïssa AI** (KI 2025, Springer chapter 10.1007/978-3-032-02813-6_11): a neuro-symbolic agent that pairs a fine-tuned chess LLM with a Prolog rule engine, a Neo4j knowledge graph, and a LangGraph verification step. The full text was paywalled **[UNVERIFIED details]**.
- **ChessCoach (Chris Butner)**: https://github.com/chrisbutner/ChessCoach (**GPL-3.0**).
  - An AlphaZero-style engine (about 3450 Elo claimed) plus a separate neural commentary head with "COVET" sampling, trained on scraped annotated games.
  - The author says the commentary is "not very insightful and often wrong".
  - Evidence that end-to-end neural commentary from scraped data is a dead end.
- **AIcrowd "Global Chess Challenge 2025"** (https://www.aicrowd.com/challenges/global-chess-challenge-2025): text-only LLM chess where models must give a move plus a human-readable justification.
  - The associated HF dataset `aicrowd/ChessExplained` (about 500K positions, **MIT**) shows a cheap *template* approach:
    1. Extract features before and after Stockfish's best move.
    2. Diff them (checks, captures, pins, promotions, escaping attacks, newly attacked pieces).
    3. Fill "After {piece} {action} {square}, this causes {color} to {reason}. So {SAN} is the most logical. {eval-bucket}".
  - Its sample outputs are ungrammatical ("this causes Black to attacks the pawn on d4"). That is the quality floor of naive templates.
- **Community/LLM prototypes:**
  - `ronaldsuwandi/thinkfish` (MIT): Stockfish plus GPT-4o. Adding FEN before *and* after each move reduced hallucinations, but invented pieces and false threats persisted.
  - `pilipolio/chess-sandbox` (MIT): 12 human-commentary concepts (pin, fork, skewer, outpost, weak square, initiative, …) labelled from GameKnot with regex plus LLM validation (98K positions on HF), probed from Maia-1500 activations, and served to a Claude skill.

---

## 2. Open-source tactic, motif, and positional detection

### 2.1 lichess-puzzler tagger (`tagger/cook.py`, `util.py`, `zugzwang.py`)
- Repo: https://github.com/ornicar/lichess-puzzler. **AGPL-3.0.** Python and python-chess. About 1,000 lines of detectors.
- **Puzzle model:** `puzzle.mainline[0]` is the opponent's move that creates the puzzle (often the blunder). `mainline[1::2]` are the *solver's* moves, and `mainline[2::2]` are the forced opponent replies. `puzzle.pov` is the solver's colour, and `puzzle.cp` is the engine eval.
  - For our coach this maps directly. After a user's mistake, the opponent's engine refutation PV is a "puzzle" with the opponent as solver: "you allowed a fork". At a missed opportunity, the best-move PV is a puzzle with the user as solver: "you missed a fork".

**Helper semantics** (`util.py`; values P=1, N=3, B=3, R=5, Q=9, K=99 in `king_values`):
- `is_defended(board, piece, sq)`: true if any friendly attacker exists. It also counts *x-ray defence*: remove each enemy ray attacker on the square and re-check for friendly attackers.
- `is_hanging`: not defended.
- `can_be_taken_by_lower_piece`: there is a non-king enemy attacker worth less than the piece.
- `is_in_bad_spot(sq)`: attacked AND (hanging OR takeable by a lower-value piece).
- `is_trapped(sq)`:
  - Not in check, not pinned, and not a pawn or king.
  - The piece is in a bad spot.
  - Every legal move of that piece either lands in a bad spot or captures something worth less.
- `is_advanced_pawn_move`: reaches rank 5+ (relative), or any promotion. "Very advanced" means rank 6+.
- `attacked_opponent_squares(board, from_sq, pov)`: enemy pieces attacked from a square.
- `squares_are_collinear`.

**Detectors in `cook()`** (summaries of the logic, not the code):

*Evaluation buckets:*
- `crushing` if cp > 600, `advantage` if cp > 200, otherwise `equality` (only for non-mate puzzles).

*Mate tags:*
- **Mate:** if the line ends in checkmate, emit `mateIn1`–`mateIn5` by length, plus `mate`. Then try the named patterns in priority order:
  - **smotheredMate:** the knight gives mate and every king-adjacent square is occupied by the king's own pieces.
  - **backRankMate:** the king is on its home rank, and the three squares in front are each own-occupied or attacked. A checker sits on that rank.
  - **anastasiaMate:** the king is on an edge file, a queen or rook mates along the file, an own piece blocks, and a knight covers.
  - **hookMate:** an adjacent rook mates, guarded by a knight, which is guarded by a pawn.
  - **arabianMate:** the king is cornered, and an adjacent rook mates, guarded by a knight two squares diagonally away.
  - **bodenMate / doubleBishopMate:** all king-zone squares are covered only by bishops. Bishops on opposite sides of the king's file means Boden.
  - **dovetailMate:** a queen gives mate diagonally adjacent, and the remaining flight squares are empty and covered only by the queen.

*Tactics:*
- **fork:** for each solver move except the last, where the piece is not a king and its destination is *not* a bad spot, count attacked enemy non-pawns that are either (a) worth more than the forking piece (king counts as 99) or (b) hanging and not able to capture the forker. Two or more means fork.
- **hangingPiece:**
  - The solver's first move captures a non-pawn that was hanging before the capture.
  - It's excluded if the opponent was in check (unless the capture is a non-pawn), or if the opponent's previous move was itself an equal-or-greater capture on that square (a trade).
  - It's confirmed if the line is 1 move, or if material two plies later is still at least as good.
- **trappedPiece:** a solver capture of a non-pawn that was `is_trapped` in the position before the preceding solver move.
- **pin** (`pin_prevents_attack` OR `pin_prevents_escape`), checked on positions after solver moves:
  - (a) A pinned enemy piece attacks a solver piece *off* the pin ray, and that piece is either worth more or hanging. The pin stops the capture.
  - (b) A pinned enemy piece is attacked along the pin line by a solver piece, and it's either worth more than the attacker, or it's hanging and has moves off the line. The pin stops the escape.
- **skewer:** a ray piece captures. The opponent's previous move vacated a square between them, the piece that moved away was worth more than the captured piece, and the captured square was a bad spot.
- **discoveredAttack:** `discovered_check` (a checker other than the moved piece), or a solver capture whose ray was opened by the solver's previous move (castling excluded).
- **doubleCheck:** more than one checker.
- **xRayAttack:** the solver recaptures on the square where the opponent just captured, *through* the opponent's previous origin square.
- **attraction:**
  1. The solver moves to square S.
  2. The opponent's K, Q, or R captures on S.
  3. The solver's next move attacks S.
  4. Either the lured piece was the king, or the solver then captures on S.
- **deflection** (also used as "overloading"; `overloading()` is a stub returning False): an opponent capture or promotion pulls a defender away from guarding the square of the solver's next capture. Uses cheap-capture and square-reuse conditions.
- **interference:**
  - `interference`: a solver piece lands between a hanging enemy piece and its ray-piece defender.
  - `self_interference`: an opponent's own piece blocks the line.
- **intermezzo:** an in-between move before an expected recapture. Checks that the opponent's capture square wasn't defended by the solver's move and that a capture two plies earlier on that square was still legal.
- **capturingDefender:** the solver captures a piece of equal or lower value that was defending the target, then wins the target (or mates).
- **clearance:** a solver ray piece moves to an empty square along a line that the solver's previous non-checking move vacated.
- **quietMove:** a solver move (not the last) that gives or escapes no check, captures nothing, attacks no enemy piece, is not an advanced pawn push, and is not a king move.
- **defensiveMove:** the final solver move is non-checking, non-capturing, and non-attacking, with at least 3 legal alternatives (or a check escape under similar conditions).
- **sacrifice:** the solver's material drops by 2 or more at some solver-move position after the first, excluding opponent promotions.
- **exposedKing:** the enemy king is on the solver's far half, has no own pawns on the three squares in front, and the line contains a mid-line check.
- **kingsideAttack / queensideAttack:**
  - The enemy king is on its back rank in files f–h or a–c, there are at least 20 (kingside) or 18 (queenside) pieces, and the line has at least 1 check.
  - Scoring: +1 per check, +1 per capture near the corner, −1 per far move. A score of 2 or more qualifies.
  - Suppressed if `backRankMate` or `fork` already fired.
- **attackingF2F7:** a capture on f2 or f7 while the king is still on e1 or e8.
- **advancedPawn, promotion, underPromotion, enPassant, castling, collinearMove.**

*Endgame type:*
- `pawnEndgame`, `rookEndgame`, `bishopEndgame`, `knightEndgame`, `queenEndgame`, `queenRookEndgame` (only kings, pawns, and that piece type).

*Length:*
- `oneMove`, `short`, `long`, `veryLong`.

*Zugzwang* (`zugzwang.py`, engine-based):
- At each solver-move position not in check, with 15 or fewer legal moves, compare the engine eval for the side to move with the eval after a **null move**.
- If having to move is worse by more than 0.3 in win-chance units (out of [-1, 1]), tag `zugzwang`.
- Win chances use `2/(1+exp(-0.00368208·cp)) − 1`, the same sigmoid lichess uses everywhere.

**Full lichess puzzle theme vocabulary** (lila `translation/source/puzzleTheme.xml`). Some themes are human- or DB-assigned rather than produced by `cook.py`:
- Phase and type: opening, middlegame, endgame; pawn/knight/bishop/rook/queen/queenRook endgames.
- Evaluation: advantage, crushing, equality.
- Mates: mate, mateIn1–5, anastasiaMate, arabianMate, backRankMate, balestraMate, blindSwineMate, bodenMate, cornerMate, doubleBishopMate, dovetailMate, epauletteMate, hookMate, killBoxMate, morphysMate, operaMate, pillsburysMate, smotheredMate, swallowstailMate, triangleMate, vukovicMate.
  - The newer named mates (balestra, blindSwine, corner, epaulette, killBox, morphy, opera, pillsbury, swallowstail, triangle, vukovic) are *not* in the public `cook.py`. Their tagger source was not located **[UNVERIFIED]**.
- Tactics: advancedPawn, attackingF2F7, attraction, capturingDefender, castling, clearance, collinearMove, defensiveMove, deflection, discoveredAttack, discoveredCheck, doubleCheck, enPassant, exposedKing, fork, hangingPiece, interference, intermezzo, kingsideAttack, pin, promotion, queensideAttack, quietMove, sacrifice, skewer, trappedPiece, underPromotion, xRayAttack, zugzwang.
- Length: oneMove, short, long, veryLong.
- Source: master, masterVsMaster, superGM, playerGames.

**Official one-line definitions** (useful as coach glossary text; paraphrased from lila's translation source):
- *Fork:* a move where the moved piece attacks two opponent pieces at once.
- *Pin:* a piece is unable to move without revealing an attack on a higher-value piece.
- *Skewer:* a high-value piece is attacked, moves away, and allows a lower-value piece behind it to be captured or attacked. The inverse of a pin.
- *Discovered attack:* moving a piece that previously blocked an attack by a long-range piece out of the way of that piece.
- *Hanging piece:* an opponent piece that is undefended or insufficiently defended and free to capture.
- *Trapped piece:* a piece that cannot escape capture because it has limited moves.
- *Deflection:* a move that distracts an opposing piece from another duty it performs, such as guarding a key square. Sometimes called "overloading".
- *Attraction:* an exchange or sacrifice that forces an opponent piece to a square that allows a follow-up tactic.
- *Interference:* moving a piece between two opponent pieces to leave one or both undefended.
- *Clearance:* a move, often with tempo, that clears a square, file, or diagonal for a follow-up idea.
- *Intermezzo (Zwischenzug):* instead of the expected move, first interpose a move posing an immediate threat that must be answered.
- *X-ray:* a piece attacks or defends a square through an enemy piece.
- *Quiet move:* doesn't check, capture, or create an immediate threat to capture, but prepares a hidden, unavoidable threat.
- *Defensive move:* a precise move needed to avoid losing material or another advantage.
- *Capturing the defender:* removing a piece critical to the defence of another, allowing the now-undefended piece to be captured.
- *Exposed king:* a king with few defenders around it.
- *Back-rank mate:* the king is trapped on its home rank by its own pieces.
- *Zugzwang:* the opponent's moves are all limited and every move worsens their position.
- *Sacrifice:* giving up material short-term to regain an advantage after a forced sequence.

**Licence and porting note:** the code is AGPL-3.0. Copying it into our server would oblige us to offer our source to network users. The *ideas* (the predicates above) can be reimplemented independently in Rust on shakmaty. The lichess puzzle database (https://database.lichess.org/#puzzles, about 5M+ puzzles with themes) is **CC0**, so it's ideal as a *test oracle*: run our Rust detectors on lichess puzzles and measure agreement with their theme tags.

### 2.2 Lichess move judgement and "Learn from your mistakes"
- **Server-side annotation** (`lila/modules/tree/src/main/Advice.scala`, AGPL-3.0):
  - `winningChances(cp)` is in [-1, 1], the same sigmoid as above.
  - Δ (from the mover's POV) ≥ 0.3 is a **Blunder**, ≥ 0.2 a **Mistake**, and ≥ 0.1 an **Inaccuracy**. These are equivalent to 15, 10, and 5 win-percentage points.
  - **Mate sequences:**
    - "Checkmate is now unavoidable" (MateCreated). Judged an Inaccuracy if the previous eval was already below −999 cp, a Mistake if below −700, otherwise a Blunder.
    - "Lost forced checkmate sequence" (MateLost), with mirrored thresholds.
    - "Not the best checkmate sequence" (MateDelayed, not judged).
  - **Comment format:** `"(evalBefore → evalAfter) Mistake. Nf3 was best."` This is the "factual engine text" baseline we have today.
- **Learn from your mistakes** (`ui/analyse/src/retrospect/retroCtrl.ts`, `nodeFinder.ts`):
  - Candidate plies are the player's moves where |Δ winningChances| > 0.1, *or* a mate-in-≤3 was lost.
  - Candidates are skipped if the played move appears in the **masters opening explorer** with more than one game (so "book" moves aren't flagged).
  - The UI says "Find a better move for White / You can do better". The user's try is accepted if it's the engine's move, a master-explorer move, or mate. Otherwise it's evaluated locally, and accepted if it loses less than 0.04 winning-chance versus the pre-move eval ("Good move").
  - Otherwise the user can "Do it again", "View the solution" ("X was best"), or "Skip this move".
  - **Takeaway:** a mature, simple Socratic loop with a *tolerance band* (accept any move within 0.04), which avoids the "only the engine's top move counts" frustration.

### 2.3 Stockfish classical evaluation terms (positional features)
- Stockfish ≤ 15.1 (GPL-3.0; `src/evaluate.cpp`, `pawns.cpp`) has an `eval` UCI command that prints a trace table. Columns are MG/EG for White, Black, and Total, with these rows: **Material, Imbalance, Pawns, Knights, Bishops, Rooks, Queens, Mobility, King safety, Threats, Passed, Space, Winnable, Total**.
- **Sub-terms** (useful as named explanation reasons; from SF 15.1 source):
  - *Pieces:* Outpost, ReachableOutpost, UncontestedOutpost, MinorBehindPawn, BishopPawns (bad bishop: pawns on the same colour), BishopXRayPawns, LongDiagonalBishop, CorneredBishop, RookOnOpenFile/semi-open file, TrappedRook (worse without castling rights), WeakQueen (queen pinned or discovered), RookOnKingRing, BishopOnKingRing.
  - *King safety:* KingAttackWeights per piece type, kingFlankAttack/FlankAttacks, PawnlessFlank, pawn shelter and storm.
  - *Threats:* ThreatByMinor[pt], ThreatByRook[pt], ThreatByKing, **Hanging**, WeakQueenProtection, RestrictedPiece, ThreatBySafePawn, ThreatByPawnPush, SliderOnQueen, KnightOnQueen.
  - *Pawns:* Isolated, Backward, Doubled, Connected, WeakLever, WeakUnopposed, BlockedPawn, PassedFile, and passed-pawn rank bonuses.
- **Stockfish 16 (June 2023) removed the hand-crafted eval** and is NNUE-only, so a current SF build can't provide these terms. Options:
  - (a) Run SF 15.1 as a second UCI process just for `eval` traces. GPL-3, separate process, generally treated as aggregation; check with counsel.
  - (b) Reimplement a subset in Rust with shakmaty bitboards. These are short formulas: mobility area, king ring, passed-pawn masks, outposts, and so on.
- CCC (§1.4) and McGrath (§1.12) both validate these terms as the positional concept vocabulary. MATE (§1.6) collapses them into 5 human categories: material, piece activity, pawn structure, space, king safety.

### 2.4 Other libraries and tools (with licences)

| Tool | What it gives a coach | Licence |
|---|---|---|
| shakmaty (our board lib) | attack bitboards, checkers, legal moves, SAN; pins and x-rays must be built from slider-ray attack tables (exact API names not checked here) | **GPL-3.0** |
| python-chess | `is_pinned`, `pin`, `attackers`, `attacks` (used by every Python paper above) | GPL-3.0 |
| Stockfish | engine; ≤15.1 classical eval trace | GPL-3.0 |
| lichess-puzzler tagger | ~50 motif detectors | AGPL-3.0 |
| lila (lichess) | advice thresholds, retro UI | AGPL-3.0 |
| lichess puzzle DB | 5M+ themed puzzles (detector test set) | CC0 |
| lichess chess-openings (https://github.com/lichess-org/chess-openings) | ECO and opening names by EPD | CC0-1.0 |
| Maia-2 | human move probability by Elo | MIT |
| Maia-3 | newer, better human model | **AGPL-3.0** |
| ChessGPT | corpus and models | Apache-2.0 (some data non-free) |
| ChessQA | motif detectors (python-chess ray scans), benchmark | MIT |
| CCC repo | concept probing and prompts | no licence (all rights reserved) |
| En Croissant (https://github.com/franciscoBSalgueiro/en-croissant) | desktop GUI (Tauri/Rust + React). Game report with eval graph and classifications, no natural-language coach | GPL-3.0 |
| ChessCoach | neural engine plus commentary | GPL-3.0 |
| `chevy` (PyPI) | FEN → hand-crafted features (KingSafety, PawnStructure classes) | not checked |

- **shakmaty licence note:** our backend already links shakmaty (GPL-3.0). GPL obligations trigger on *distribution*, not on running a network service. AGPL would add the network clause. Copying AGPL lichess code would therefore change our obligations. Reimplementing doesn't.
- **En Croissant** is a Rust/Tauri + React app like ours, so it's useful to read for engine-orchestration patterns (GPL).

---

## 3. Commercial explainers and what is public about them

### 3.1 Chess.com Game Review and Coach (public facts)
- **Launch:** "Game Review Now Available For All Chess.com Members" (https://www.chess.com/news/view/chesscom-releases-new-game-review, last updated Nov 2022).
  - Describes a virtual Coach that explains why moves are good or bad, for example a move that "perfectly capitalizes on forced checkmate", "loses material", or "misses a chance to damage your opponent's pawn structure".
  - "Show Line" plays the engine continuation.
  - Book moves come with commentary "written by master-level players".
  - **Credits list an "Explanation engine" team: @dwcoates, @DanTheCabin, @2tp, @dpervov, @nollaversioit.** Back end: @PawnMorphy, @querylanguage. No technical description is given.
- **Game Review v2** (https://www.chess.com/news/view/chesscom-launches-game-review-v2, Mar 2023) added:
  - A report card: Coach summary, game rating, and per-phase grades.
  - **Visual explanations:** hovering or clicking highlighted words in the Coach text draws arrows and squares. This implies the text is generated from structured events with board references.
  - **Blunder recalibrated:** it must drop expected points significantly *and* lose material or allow mate.
  - A new **Miss** class: failing to take a tactical opportunity, missing mate, or failing to punish an opponent's mistake.
  - A cleaned-up book DB.
  - **"More detailed Coach explanations: describes the threats behind each move and whether they are prevented or allowed; names specific pieces."**
- **Help article** (https://support.chess.com/en/articles/8584089-how-does-game-review-work):
  - The Coach bubble offers buttons such as **"Show Fork", "Show Lost Piece", "Show Checkmate", "Show Idea"**, plus "Best" and "Retry".
  - Retry: a correct move shows your score, and a wrong one gets Coach feedback on the move you chose.
  - Key moments use "Next". The first key move is usually the last book move, with the opening name, your history with it, and a course suggestion.
  - The coach can read feedback aloud, and you can choose between coach avatars.
  - Those button names confirm a tag vocabulary that includes at least *fork*, *lost piece* (hanging/material loss), *checkmate*, and a generic *idea*.
- **Classification V2** (https://support.chess.com/en/articles/8572705-how-are-moves-classified-what-is-a-blunder-or-brilliant-and-etc):
  - Based on Expected Points (win probability from eval *and rating*). Expected-points loss bands:
    - Best: 0.00
    - Excellent: 0–0.02
    - Good: 0.02–0.05
    - Inaccuracy: 0.05–0.10
    - Mistake: 0.10–0.20
    - Blunder: ≥ 0.20
  - Great: a critical or only-move. Brilliant: a good piece sacrifice, more generous for new players.
  - The same move can get different labels at different ratings.
- **"Course check"** (https://www.chess.com/news/view/announcing-game-review-course-check): the coach tells you where you deviated from lines in courses you own.
- **Engine:** Chess.com funded **Torch** (July 2023; https://www.chess.com/news/view/torch-chess-engine) and said Game Review, puzzle generation, and bots are powered by its engines. The lead developer (Andrew Grant) later posted that strength-focused development had ended.
- **Hiring:** a Nov 2025 "Analysis Infrastructure Engineer" posting mentions "the world's largest chess game analysis cluster and its cross-platform C++ chess analysis library". No posting mentioning "CEE" or "explanation engine" was found.
- **User sentiment:** forum and blog users call the Coach a simplification that is sometimes misleading, for example "This loses a pawn" when the real problem is the uncastled king (ChessGrader). One blogger finds it "entirely unreliable" (chess.com/blog/Duckfest).
- **[UNVERIFIED]** Any public description of a "Chess Explanation Engine (CEE)", "board events", about 250 tags, "coach speech" templates, or prioritisation. I found none, and the brief's description presumably comes from inspecting the client. Also unverified: whether any LLM is used today. No 2024–2026 Chess.com announcement of an LLM coach was found.

### 3.2 DecodeChess (Decodea Ltd., Israel)
- Site: https://decodechess.com. About and team: https://decodechess.com/about/.
  - CEO Zeev Fine; R&D head Dr. Ofer Shamai; chief architect Ofer Faigon.
  - Marketed as "explainable AI" for players up to about 2000.
- **Approach** (their description): don't explain from the eval function, which gave "limited results". Use **Stockfish's deep search** to *verify* candidate concepts. A concept, such as an open file, is reported only if it "can be shown to affect the future course of the game". This is concept detection with search-based relevance verification. It's the same "is this tag actually relevant?" step that CCC does with an LLM chain of thought.
- **Output structure** (https://decodechess.com/chess-analysis-tips/, https://decodechess.com/chess-threat-analysis/, https://decodechess.com/faq/):
  - **Summary** tab: aggregates the other tabs, including "Opponent intentions" (a threat summary with arrows) and "Pay attention to" (from Concepts).
  - **Threats** tab: threats grouped by piece, each expandable to a verbal description plus annotated lines. It has a **before/after-best-move toggle** showing whether each threat is neutralised, and a "Solution" paragraph on how the best move handles it.
  - **Good Moves:** ranked. If the game move is still "good", it prefers explaining that move over a slightly better one.
  - **Plans:** attacking and defensive plans, sometimes several options.
  - **Functionality:** the role of each piece (defends X, attacks Y, blocks Z, …).
  - **Concepts:** x-rays, control of files and ranks, and other placement factors.
  - **Idea / Problem / Solution:** a step-by-step framework, not generated for every position.
  - **Best-line explanations:** up to 7 plies, each expandable to up to 18 annotated sub-variations.
- **Partnerships:** a Chessify add-on from Jan 2023, which **ended Jan 2024** (https://chessify.me/news/chessify-partnership-with-decodechess).
- **Acquisition by Chess.com: NOT FOUND.** No press release, news article, or DecodeChess page mentions it, and DecodeChess still presents itself as Decodea's product. Treat "Chess.com acquired DecodeChess" as **unsubstantiated**. The Chess.com Coach credits name Chess.com engineers, not Decodea staff.

### 3.3 ChessBase / Fritz
- Fritz 5 (1997) had "Explain all moves".
- **ChessBase 18 "engine variation with language"** (https://help.chessbase.com/CBase/18/Eng/engine_variant_with_language.htm) verbalises each engine line with motif phrases:
  - "perpetual check", "positional repetition"
  - material balance ("White wins the queen for rook and knight", "Black loses two pawns")
  - simplification into an endgame type
  - passed pawns ("dangerous passed pawn on e6"), pawn majorities, levers
  - sacrifices, "penetrating attack", "both kings are insecure"
  - piece manoeuvres ("Nd2-f1-e3-d5")
- The **Fritz 21 handbook** describes "Annotated Engine Variations" covering material, pawn structure, piece activity, king safety, and tactical motifs.
- **Fritz 20** advertises "AI-powered voice commentary featuring over 170 chess-related themes". "Fritz – Your Chess Coach 2" gives move hints with text and audio explanations.
- Implementation (templates vs LLM) is not documented **[UNVERIFIED]**. The "170 themes" figure suggests a tag-plus-template system of similar size to the one in our brief.
- **Komodo/Dragon:** no native commentary found. The "Komodo full analysis" text comments come from the ChessBase layer.

### 3.4 Take Take Take (Magnus Carlsen's app): the most detailed public architecture
Source: AI Engineer Europe 2026 talk "Building a chess coach that can explain the move" by Anant Dole and Asbjørn Steinskog (https://ai.engineer/talks/building-a-chess-coach, https://ai.engineer/talks/FlzpEGHNVKQ-building-chess-coach).

- **Pipeline:** Stockfish (best moves) → **tactical detectors** (forks, pins, skewers, …) → **positional detectors** (doubled pawns, …) → **Maia** P(move | rating), to tell "best but hard to find at 1500" apart → a **structured JSON fact contract** with the played move, engine verdict, threat, and response → **Gemini 3 Flash** verbalises it (about 1 s to first token, about 3 s total; target under 3 s).
  - Example: "f5 is bad because of a queen-trap threat; the defensive pawn capture frees an escape square".
- **Principles:**
  - "Analysis first, language generation second." The LLM only translates facts and never calculates.
  - Build the context JSON large first, then prune while measuring quality.
  - Hallucinations are reduced, not eliminated.
- **Evals:**
  - 16 real-game scenarios (tactics, blunders, hallucination bait such as "does it mention the knight fork when given the context?").
  - An LLM judge checks *use of supplied facts*, not fluency.
  - Model sweep via OpenRouter: Gemini Flash about 75% pass, Claude with extended thinking just under 60% at much higher latency, GPT-5 Mini lower.
  - Strong human players give the final sign-off.
- **Ops loop:** a user downvote goes to Slack and a Claude Code session with a "commentary triage" skill. The agent inspects the position, adjusts the prompt or detectors, regenerates, and opens a PR, with a human merge.
- A separate, slower "chat with your coach" mode is planned for reasoning models.

### 3.5 Other products
- **TNG "AI chess YouTube channel"** (Stephan Steinfurt, AI Engineer talk: https://ai.engineer/talks/running-a-chess-youtube-channel-entirely-by-ai-stephan-steinfurt-tng-technology-consulting):
  - A LangGraph agent (Gemini 3.1 Pro) with tools for legal moves, play/undo, engine eval, a **checks-captures-threats** scan, Maia human-move prediction, historical commentary, and web search.
  - About 1 in 20 videos has an error (informal estimate).
  - Lessons: give the agent an *interactive board*, and explain **tempting bad moves**, not only the best move.
- **Chessiro** (https://chessiro.com/blog/inside-chessiro-game-review):
  - Stockfish 18/19 in the browser.
  - Classes: genius, smart, best, good, book, inaccuracy, mistake, blunder, by win-probability loss.
  - Coach text with colour-coded arrows (green good, red mistakes, yellow key squares), follow-up Q&A, voice, 24 languages.
  - "Recommended training": themes missed vs handled well, with definitions and one-click drills.
  - The LLM and detectors are not disclosed.
- **Aimchess:** aggregate diagnosis over the last 40 games in six areas: **Openings, Tactics, Endgames, Advantage capitalization, Resourcefulness (holding bad positions), Time management**, each compared with peers of the same rating. Exact scoring is not public. A good template for a game-level or multi-game "insights" layer, as opposed to per-move commentary.
- **Chessify:** cloud engines. It hosted the DecodeChess add-on in 2023. No native explainer found.
- **Chessvision.ai:** no public documentation of an explanation feature found **[UNVERIFIED]**.
- **En Croissant:** GPL-3.0 desktop app with game reports (classifications, eval graph). No natural-language coach.

---

## 4. Pedagogy: what makes move feedback useful

1. **Safety check and anti-"hope chess" (Dan Heisman).**
   - "Hope chess" means making a move without checking the opponent's forcing replies (checks, captures, threats) and *hoping* you can answer whatever comes.
   - "Real chess" means doing that check on every move. "A move is safe if the opponent has no forcing reply that wins material or checkmates."
   - Sources: Heisman's Novice Nook columns, collected in *A Guide to Chess Improvement: The Best of Novice Nook* (review: https://forwardchess.com/blog/book-review-a-guide-to-chess-improvement/); *Is Your Move Safe?* (New in Chess, https://www.newinchess.com/is-your-move-safe); Chess.com article https://www.chess.com/article/view/passive-vs-basic-hope-chess.
   - *Coach implication:* for blunders, phrase the explanation as the missed safety check. "Before Nf6, ask: what are White's checks, captures, and threats? Bxf6 wins a piece because …". Track a per-user "missed opponent threat" rate.
2. **Name the motif, show the concrete line, keep it to one key reason.**
   - Nunn's study of puzzle-book errors grouped blunders into "harmless-looking" positions, false threats, and hidden threats (via https://www.chess.com/blog/alexandermatos/types-of-chess-blunders, secondary).
   - Cui et al. 2026 (§1.9): motif names alone barely help solvers, while concrete lines do. Show "Nd5! (fork) Qd7 Nxc7" plus the motif name.
   - Chess.com v2 made the coach name pieces and say whether threats are "prevented or allowed". DecodeChess uses a threat before/after toggle.
3. **Formative feedback design** (Shute 2008, "Focus on Formative Feedback", *Review of Educational Research* 78(1); PDF https://myweb.fsu.edu/vshute/pdf/shute%202008_b.pdf):
   - Focus on the task, not the learner.
   - Give elaborated feedback (why and how), not just verification (right or wrong).
   - Deliver it in manageable units, as simple as possible but no simpler.
   - Low-achieving and novice learners benefit from more directive, explicit, immediate feedback. Stronger learners do fine with facilitative or delayed feedback, such as hints and questions.
   - The guideline list was confirmed via secondary summaries. Wording is not quoted from the original **[partially verified]**.
   - *Coach implication:* rating-adaptive verbosity. Beginners get "this hangs your knight — it has no defender". 1800s get "after …Bxf6 you can't recapture because of the pin on the d-file".
4. **Feed up / feed back / feed forward; task, process, self-regulation** (Hattie and Timperley 2007, "The Power of Feedback", RER 77(1) 81–112; PDF https://www.uky.edu/~gmswan3/575/Hattie_Timperley_2007.pdf):
   - Feedback should say where you're going, how you're doing, and **what to do next**. Feed-forward is often the most powerful.
   - Process and self-regulation feedback ("check every capture before moving") transfers better than task-only feedback.
   - Praise of the person ("great job!") is least effective.
   - *Coach implication:* end key-moment explanations with a transferable habit ("Next time a knight can reach d5, check for forks").
5. **Self-explanation and prediction.** de Bruin, Rikers, Schmidt 2007, *Contemporary Educational Psychology* 32(2): 188–205 (https://repub.eur.nl/pub/66197).
   - Chess novices learning KR vs K who predicted the computer's moves *and self-explained them* learned the principles better and checkmated more often.
   - Prediction alone gave no advantage over watching.
   - *Coach implication:* a "Retry" mode (lichess Learn from your mistakes, Chess.com Retry), optionally followed by "Why does this move work?" with multiple-choice motif answers drawn from our detector tags.
6. **Hint ladders** (VanLehn 2006, "The Behavior of Tutoring Systems", IJAIED; PDF https://www.cs.uky.edu/~sgware/reading/papers/vanlehn2006behavior.pdf; summary https://learnlab.org/research/wiki/index.php/Hint_sequence):
   - Pointing hint ("look at the knight on c3"), then teaching hint ("a knight on d5 would attack two pieces — that's a fork"), then bottom-out hint ("Nd5").
   - Watch for students "clicking through" hints. One CogSci study found no learning difference between high-level and bottom-out hints, so the ladder's value is in engagement, not magic.
7. **Evaluate learning, not satisfaction.** Shymanski et al. 2025 (§1.14): any explanation raises satisfaction. Measure retry success, recurrence of the same motif error across later games, and puzzle performance on missed themes. Aimchess and Chessiro "missed themes → drills" is the product version of this.
8. **Rating-adaptivity via expected points and Maia.** Chess.com uses rating-dependent expected points, so the same move gets different labels by rating. Take Take Take and TNG use Maia to separate "objectively best" from "findable at your level". Combine them: don't scold a 1200 for missing a 5-move quiet combination (low Maia probability, so frame it as "a hard idea to learn"), but always flag a 1-move hanging piece.
9. **Don't over-flag.** Lichess skips moves found in the masters explorer and accepts any move within 0.04 winning-chance in retry. Chess.com's v2 Blunder requires *material loss or mate*, not only an eval drop. Pick about 3–6 key moments per game (DecodeChess recommends 5–8 positions per game).

---

## 5. A concrete design for our app, derived from the above

**A. Board-event layer (Rust, shakmaty, deterministic).** For each user move, with engine data (MultiPV ≥ 2 before and after the move, plus PVs):

1. *Static facts, pre- and post-move:*
   - Hanging pieces (`is_hanging` with x-ray defence), pieces en prise to lower-value attackers (`is_in_bad_spot`), trapped pieces.
   - Pins (absolute and relative, with pinner and pinned), checks, king zone attackers, pawn-shield holes.
   - Threats the opponent now has: the set of their captures that win material by a simple SEE, and mate-in-1/2 threats from the engine (null-move or MultiPV).
2. *Line-based motifs* using the lichess predicates, run on:
   - (a) The **refutation PV** of the played move (opponent as solver): "allowed fork / pin / skewer / discovered attack / back-rank mate / trapped piece".
   - (b) The **best-move PV** (user as solver): "missed fork / hanging piece / mate in N / deflection …".
   - (c) The played move's own PV when it's good: "Great: Nd5 forks queen and rook".
3. *Positional deltas:* a small Rust reimplementation of SF classical terms (mobility, king safety, passed pawns, space, outposts, bad bishop, open-file rooks, doubled/isolated/backward pawns). Report the top |Δ| terms, as CCC does, but only when no tactical event explains the eval swing.
4. *Human factor:* Maia-2 (MIT) P(played), P(best) at the user's rating.
5. *Opening:* lichess chess-openings (CC0) names. Masters-explorer membership suppresses "mistake" flags in book.

**B. Prioritiser** (tags → one primary reason plus at most 2 secondary). Suggested precedence:

1. Mate allowed or missed.
2. Material lost to a named tactic (fork, pin, skewer, discovered attack, trapped, hanging) or won with one.
3. Threat ignored: the opponent's threat existed before the move and was neither prevented nor answered. This mirrors Chess.com's "threats prevented or allowed".
4. Missed opportunity (the Miss class).
5. King safety collapse.
6. Positional term swings.
7. Generic "the engine's idea was X".

Weight by eval swing and by Maia probability.

**C. Verbaliser.**
- **Tier 1:** templates keyed on (tag, role = allowed/missed/played, piece types, squares), with variation pools to avoid the repetitiveness Jhamtani measured. Every noun phrase (piece, square, line) is bound to board highlights, like Chess.com v2's clickable words.
- **Tier 2 (optional):** a small fast LLM given *only* the JSON fact contract (Take Take Take style). Use a CCC-style "evaluate each candidate fact, then comment" prompt, the explicit attack list, and FEN before and after. Run a post-hoc verifier that parses SAN and squares in the output and rejects claims not in the facts. ACT-Eval-style tools can serve as an offline test harness.

**D. Pedagogy features.**
- Retry with a 0.04 win-chance tolerance (lichess).
- A hint ladder: pointing → motif → move.
- A safety-check prompt for blunders ("What does your opponent threaten?").
- Rating-adaptive verbosity.
- Per-user motif-miss stats feeding puzzle recommendations from the CC0 lichess puzzle DB filtered by theme.

**E. Evaluation.**
- *Detector accuracy:* run our Rust detectors on lichess puzzles and compare with their themes.
- *Explanation factuality:* an ACT-Eval-style atomic-claim check with tools.
- *Coverage of the key idea:* a small expert-labelled set, like the 16 Take Take Take scenarios.
- *Learning outcome:* retry success, and recurrence of the same motif error over later games.

---

## 6. Unverified or unresolved items
- Chess.com "CEE / explanation_engine", "~250 board events", "coach speech" templates and prioritisation: **no public source found.** Only the "Explanation engine" credits in the 2022 launch post, the v2 feature list, and the help-centre button names ("Show Fork / Lost Piece / Checkmate / Idea") are public.
- **Chess.com acquiring DecodeChess: not found; likely false.**
- Whether Chess.com's coach uses an LLM today: no announcement found.
- "Coach David / Danny voice" naming: not verified (the help centre only says coach avatars are selectable and can read feedback aloud).
- Sadikov et al. 2006 "Automated Chess Tutor" internals (Crafty, eval-feature-based goals): from memory, full text not accessed.
- SARFA (Puri et al., ICLR 2020) details: from memory.
- McGrath et al. 2022 exact concept list beyond the SF8 terms: not re-verified.
- ACT-Eval code repo (github.com/hebbarashwin/act_eval) returned 404.
- Source of lichess's newer named-mate themes (balestra, killBox, …): not in public `cook.py`.
- Fritz 20 "170 themes" voice commentary implementation (templates vs ML): undocumented.
- MATE dataset licence; Master-Distillation C1 code and weights; Caïssa AI details (paywalled).
- Chessvision.ai explanation feature: no documentation found.
