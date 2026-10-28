# SupportBrain

**What happens to an AI support agent's answers when the knowledge it retrieves is designed deliberately instead of dumped in raw?**

SupportBrain is a context engineering project. I act as the context engineer for FinFlow, a fictional fintech, and design the knowledge layer behind its AI customer support agent. Then I measure what that design does to retrieval.

> **Status (work in progress):** knowledge base v1 is finished and frozen. The Act 1 baseline has run. Act 2 (the redesign) and Act 3 (failure analysis) are next.

## The plan in three acts

1. **Act 1, naive baseline.** Fixed-size chunking, no metadata, no prompt design. Score it and document every failure.
2. **Act 2, engineered redesign.** Structure-aware chunking, metadata, retrieval-aware structure and a system prompt. Every change traces back to a specific Act 1 failure.
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
- **Metrics:** hit-rate@3, hit-rate@5 and MRR@5. A hit means a retrieved chunk overlaps a labeled section. Reported two ways: counting acceptable alternate sections, and primary section only.
- **Predictions:** Act 1 ran without written predictions, a time trade-off I chose to disclose rather than backfill. Predictions will be written and committed before the Act 2 rerun and before the held-out set is unsealed.

### What labeling showed before anything ran

- **1 coverage gap (Q14):** it asks about merchant refunds, which v1 deliberately leaves out. It's scored separately. The real test is whether the agent admits it doesn't know or invents a timeline.
- **1 miscategorized question (Q22):** filed as account suspension, but "suspended after failed login attempts" describes a lockout, which the KB defines as *not* a restriction. Its answer lives in the 2FA article.
- **5 genuinely ambiguous questions** with more than one honest answer. For some of these, the best agent behavior is a clarifying question, which retrieval metrics can't measure.

## Act 1 results

Setup: 256-token chunks with no awareness of headings, frontmatter stripped, `BAAI/bge-small-en-v1.5` embeddings, ChromaDB. Full config, versions and article hashes are in `results/`.

| Scoring | n | hit@3 | hit@5 | MRR@5 |
|---|---|---|---|---|
| Primary + alternates | 22 | [ ] | [ ] | [ ] |
| Primary only | 22 | [ ] | [ ] | [ ] |

### Key failures

[3 to 5 diagnoses: what was asked, what came back, and which layer caused it]

## What's next

- **Act 2:** [the targeted fix, tied to the Act 1 failure it addresses]
- Rerun the design set, then unseal the held-out set once and report both separately.
- Act 3 write-up, a long-form article, and a one-page Context Engineering Audit Checklist.

## Known limitations

- **Held-out exposure.** The sealed questions and the design set were in the same working context where the domain rules were made. I based the rules on customer situations, not on those questions, but I can't prove independence, so I'm stating it here.
- **Ground truth was AI-drafted and human-reviewed.** Section labels were proposed with AI after the KB was frozen, then reviewed by me.
- **No predictions for Act 1.** I didn't write down expected results before the baseline ran, so Act 1 can't show predicted versus actual. Act 2 and the held-out run will.
- **Not a clean ablation.** Act 2 changes several things at once, so improvements can't be pinned to a single change.
- **Small corpus.** Seven articles and 23 scored questions. The numbers show direction, not statistical certainty.
- **Known content gaps.** Some restriction types, plan cancellation and merchant refunds are out of v1. They're listed in `docs/known-gaps.md`.
- **Out of scope for v1:** cost and latency trade-offs, and conversation state and history.

## Reproduce it

```bash
git clone [repo url]
cd supportbrain
bash run.sh
```

Needs Python 3.10 to 3.13. The script creates a virtual environment, installs pinned versions, runs Act 1 on the `kb-v1` corpus and writes results to `results/`.

## Repo layout

```
kb/            the 7 frozen articles (tag: kb-v1)
labels.csv     section-level ground truth for the 23 design questions
predictions.md predictions template, used from Act 2 onwards
act1_baseline.py, run.sh, requirements.txt
results/       Act 1 output: summary, full JSON, chunk dump
docs/          section index, run decisions, metadata schema, known gaps
sealed/        held-out questions (not used until Act 2 is frozen)
```
