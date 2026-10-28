# SupportBrain

**What happens to an AI support agent's answers when the knowledge it retrieves is designed deliberately instead of dumped in raw?**

SupportBrain is a context engineering project. I act as the context engineer for FinFlow, a fictional fintech, and design the knowledge layer behind its AI customer support agent. Then I measure what that design does to retrieval.

> **Status (work in progress):** knowledge base v1 is frozen. The Act 1 baseline has run and its failures are diagnosed. The first Act 2 change (one chunk per section) has run against the same questions. The held-out set is still sealed.

## The plan in three acts

1. **Act 1, naive baseline.** Fixed-size chunking, no metadata, no prompt design. Score it and document every failure.
2. **Act 2, engineered redesign.** Structure-aware chunking, metadata, retrieval-aware structure and a system prompt, introduced one change at a time. Every change traces back to a specific Act 1 failure.
3. **Act 3, failure analysis.** Diagnose the hardest cases by which context layer caused them, and recommend fixes.

## The knowledge base

Seven articles, one per support category: account restrictions, plan refunds, transaction disputes, failed payments, identity verification, fees and two-factor authentication. 38 sections in total.

The domain rules came from customer situations rather than topics. For example, FinFlow has a single "restricted" state, a frozen but visible balance, and restriction reasons split by who has to act next, the customer or FinFlow. Every rule is in the decision log with its reason and a "what would change my mind" line.

Every section is written to survive being chunked, using a checklist I built from four failure modes:

1. **Cut-off conditional:** an "if" and its "then" stay in the same unit.
2. **Severed sequence:** numbered steps state their count upfront and stay together.
3. **Reference failure:** no pronoun reaches across a section boundary.
4. **Low information density:** every section answers one real question, and its heading is that question.

**How the articles were written:** I made the domain decisions. The prose was drafted with AI from those rules and the checklist, then reviewed and revised by me section by section. That's deliberate: the skill this project is about is the shape of the content, not typing the words.

## How it's evaluated

- **30 questions** across the seven categories, written in formal and informal registers, including typos, vague questions and questions missing context.
- **23 design questions** are used for Act 1 and Act 2. **7 held-out questions** stay sealed until the Act 2 redesign is frozen, so the final results show whether the design generalizes rather than fitting to known failures.
- **Ground truth is labeled at the section level**, not the chunk level, so the labels stay valid when chunking changes between acts.
- **Metrics:** hit-rate@3, hit-rate@5 and MRR@5. A lenient hit means a retrieved chunk overlaps a labeled section. Also reported: primary section only, and a **strict** hit, where the chunk has to be at least half correct-section text. The strict measure was added after Act 1, once it was clear the lenient rule credits chunks that are mostly about something else (decision B10).
- **Predictions:** Act 1 and the first Act 2 change ran without written predictions, a time trade-off I chose to disclose rather than backfill. Predictions will be written and committed before the next Act 2 change and before the held-out set is unsealed.

### What labeling showed before anything ran

- **1 coverage gap (Q14):** it asks about merchant refunds, which v1 deliberately leaves out. It's scored separately. The real test is whether the agent admits it doesn't know or invents a timeline.
- **1 miscategorized question (Q22):** filed as account suspension, but "suspended after failed login attempts" describes a lockout, which the KB defines as *not* a restriction. Its answer lives in the 2FA article.
- **5 genuinely ambiguous questions** with more than one honest answer. For some of these, the best agent behavior is a clarifying question, which retrieval metrics can't measure.

## Results

Act 1 setup: 256-token chunks with no awareness of headings, frontmatter stripped, `BAAI/bge-small-en-v1.5` embeddings, ChromaDB, top 5. Act 2 changes **one thing**: one chunk per heading section. Full config, versions and article hashes are in `results/`.

| Scoring (22 answerable questions) | Act 1 hit@3 | Act 2 hit@3 | Act 1 hit@5 | Act 2 hit@5 | Act 1 MRR | Act 2 MRR |
|---|---|---|---|---|---|---|
| Lenient (chunk overlaps a correct section) | 0.864 | 0.909 | 0.955 | 0.955 | 0.717 | 0.739 |
| Strict (chunk is at least half correct text) | 0.682 | **0.909** | 0.727 | **0.955** | 0.549 | **0.739** |
| Primary section only | 0.864 | 0.773 | 0.955 | 0.955 | 0.634 | 0.564 |
| Share of first matching chunk that's correct | 59% | **100%** | | | | |

**The short version:** Act 1 already found the right neighbourhood. But 19 of its 26 chunks straddled two or three sections, so on average 41% of what it handed back was about something else. Act 2 returns the right section on its own. The cost is that compound questions now split across sections, which is why primary-only MRR fell.

### Key findings

Full write-up: [`docs/failure-analysis-act1.md`](docs/failure-analysis-act1.md).

1. **Chunk dilution.** The documents section for Q10 shared a chunk with two neighbours and came 5th. With one chunk per section, it came 3rd.
2. **Typos defeat vocabulary bridges.** "Suspnded" never matches the bridge word "suspended" (Q24, 4th in both runs). Q12 ("my kyc got rejcted agan") missed entirely in both runs.
3. **The predicted vocabulary trap.** Q22 says "suspended" but describes a lockout. It ranked 2nd in both runs, and in Act 1 the restriction article came first.
4. **Bridges compete, partly because of dilution.** The disputes article's "charge" vocabulary beat fees on both fee questions in Act 1. With one chunk per section, fees won both.
5. **The coverage gap got the second-highest similarity score in Act 1.** Q14 (merchant refunds, out of scope) matched the plan refund article at 0.79, higher than 21 of the 22 questions the KB can actually answer. Similarity can't tell "the answer" from "something nearby," so this needs a prompt that abstains, not better retrieval.
6. **Smaller chunks are purer but split compound questions.** Q01 asks for the steps *and* the deadline. In Act 2 the deadline section came 1st and the steps section dropped to 5th.

## What's next

- **More Act 2 changes, one at a time, each tied to a failure Act 2 left:** retrieve a section's neighbours with it (compound questions), query rewriting or spelling correction (Q12, Q24), a system prompt that abstains on mismatched context (Q14), and intent-aware routing before any topic filter (Q22).
- Write predictions, then unseal the held-out set once and report it separately.
- Answer-quality scoring with a local LLM, the Act 3 write-up, a long-form article, and a one-page Context Engineering Audit Checklist.

## Known limitations

- **Held-out exposure.** The sealed questions and the design set were in the same working context where the domain rules were made. I based the rules on customer situations, not on those questions, but I can't prove independence, so I'm stating it here.
- **Ground truth was AI-drafted and human-reviewed.** Section labels were proposed with AI after the KB was frozen, then reviewed by me.
- **No predictions for Act 1 or the first Act 2 change.** I didn't write down expected results before either run, so neither can show predicted versus actual. The next change and the held-out run will.
- **One change at a time, so far.** The first Act 2 run changes only the chunking, so its effect can be attributed. Later changes will be layered one at a time, but interactions between them won't be fully isolated.
- **The strict measure was added after seeing Act 1.** It's disclosed in decision B10 and applied identically to both runs.
- **Small corpus.** Seven articles and 23 scored questions. The numbers show direction, not statistical certainty.
- **Known content gaps.** Some restriction types, plan cancellation and merchant refunds are out of v1. They're listed in `docs/known-gaps.md`.
- **Out of scope for v1:** cost and latency trade-offs, and conversation state and history.

## Reproduce it

```bash
git clone https://github.com/iyissa/supportbrain.git
cd supportbrain
bash run.sh     # Act 1
bash act2.sh    # Act 2, plus Act 1 re-scored with the strict measure
```

Needs Python 3.10 to 3.13. `run.sh` creates a virtual environment, installs pinned versions and runs Act 1 on the `kb-v1` corpus. `act2.sh` reuses that environment. Results go to `results/`.

## Repo layout

```
kb/            the 7 frozen articles (tag: kb-v1)
labels.csv     section-level ground truth for the 23 design questions
predictions.md predictions template, used from Act 2 onwards
act1_baseline.py, run.sh    the original Act 1 run
retrieval_eval.py, act2.sh  shared scoring for Act 1 and Act 2, with Act 2 options as flags
requirements.txt
results/       every run: summary, full JSON, chunk dump
docs/          failure analysis, decision log, section index, run decisions, metadata schema, known gaps
sealed/        held-out questions (not used until Act 2 is frozen)
```
