# Failure analysis: baseline and Change 1

> **Note:** this is the detailed working analysis. "Act 1" means the baseline and "Act 2" means Change 1 in the README. In the Change 1 section, the strict scores and the "100% relevant" figure are partly guaranteed by how they were measured (each chunk is exactly one section), so they overstate the gain. The README uses the fairer comparison.


Run: `results/act1-20261028-220444` (corpus tag `kb-v1`). 256-token fixed chunks, no heading awareness, frontmatter stripped, `BAAI/bge-small-en-v1.5`, top 5.

## Headline

| Scoring | hit@3 | hit@5 | MRR@5 |
|---|---|---|---|
| Lenient (chunk overlaps a correct section) | 0.864 | 0.955 | 0.717 |
| Primary section only | 0.864 | 0.955 | 0.634 |
| Strict (chunk is at least half correct-section text) | 0.682 | 0.727 | 0.549 |

21 of 22 answerable questions had a matching chunk somewhere in the top 5. Only Q12 missed completely.

**That headline is flattering, and the main finding is why.** 256 tokens is roughly 190 words, while a typical section here is 60 to 120 words. So 19 of the 26 chunks straddle two or three sections. Under the lenient rule, a chunk that's mostly about something else still counts as a hit if a sliver of the right section is inside it. On average, only 59% of the first matching chunk's text belongs to a correct section. The rest is neighbouring material the agent would also be handed. The strict measure was added after Act 1 for exactly this reason (decision B10), and it's reported for both runs.

## Diagnoses

### 1. Chunk dilution: the right section is a minority of its chunk (structure/chunking)

**Q10:** "Which documents does FinFlow accept for identity verification, and what are the file format requirements?"

- **Answer:** `kyc-verification#2`, which covers documents and formats.
- **What happened:** that section sits in a chunk with "what can I do before verification" and the verification steps. It came 5th. The top result was the chunk holding the steps, tiers and timing, which is about verification in general but doesn't list the documents or formats.
- **Why:** the fixed splitter cut through section boundaries, so the documents section never got an embedding of its own. Its signal was averaged in with two neighbours.
- **This is the failure the Chunk-Safe Writing Checklist was built for.** The sections themselves pass all four rules. The splitter undoes that work by ignoring where they start and end.

### 2. The one complete miss: typos plus a diluted target (vocabulary + chunking)

**Q12:** "my kyc got rejcted agan, i uploded my pasport like u said"

- **Answer:** `kyc-verification#6`, the rejection section.
- **What happened:** no KYC chunk in the top 5. Disputes and failed payments came back instead, presumably because "rejected" sits close to "declined" and "failed."
- **Why:** three things stack up. The typos ("rejcted", "uploded", "pasport") weaken the match. The acronym "KYC" appears only once in the whole article, in the first section's synonym line. And the rejection section shares a chunk with verification timing and verification restrictions, so its own signal is diluted.

### 3. Typos break the vocabulary bridge (vocabulary)

**Q24:** "my acount got suspnded this morning and i dont even know why"

- **Answer:** `restricted-account-review#1`, which carries the bridge "you may also see it described as suspended or banned" (decision A15).
- **What happened:** it came 4th. Three failed-payments chunks ranked above it, led by "Why did my payment fail?", which matched the "why" framing.
- **Why:** the bridge depends on the customer's word appearing in the text. "Suspnded" isn't "suspended," so the bridge never fired. Bridges work for vocabulary differences, not for spelling.

### 4. The predicted vocabulary trap (category mismatch)

**Q22:** "My account was suspended after multiple failed login attempts. What is the process for having it reinstated?"

- **Answer:** `two-factor-authentication#6`, the lockout section. The KB deliberately says a lockout is not a restriction (decision A16).
- **What happened:** exactly as flagged during labeling. The restriction article came first, pulled by "suspended." The lockout answer came 2nd, inside a chunk shared with the lost-phone section.
- **Why it matters for Act 2:** routing questions by topic metadata would make this worse. A router reading the customer's word "suspended" sends Q22 to account suspension, which is the wrong article. Metadata only helps if routing understands intent, not keywords.

### 5. Vocabulary bridges compete across articles (vocabulary)

**Q19** ("the amount deducted was different from what I expected") and **Q20** ("why was I charged a fee?? nobody told me")

- **Answer:** the fees article.
- **What happened:** for both questions, the top result was the disputes article's first section. Fees came 2nd.
- **Why:** the disputes bridge ("charged twice, a double charge, an unauthorized or fraudulent charge") and the fees bridge ("a charge, a service charge, money deducted") both lean on the word "charge." Each bridge is right on its own. Together they compete for the same queries.

### 6. The coverage gap looks like one of the strongest matches in the run (coverage)

**Q14:** "How long does a refund for a cancelled merchant purchase take to appear in my FinFlow balance?"

- **Answer:** none. Merchant refunds are out of v1 (decision R1).
- **What happened:** the plan refunds article came back at a similarity of 0.79, **the second-highest top score in the run, beaten only by Q01 and higher than every other answerable question.**
- **Why it matters:** similarity can't tell "this is the answer" from "this is about something nearby." An agent handed that chunk could confidently say "3 to 5 business days," which is the plan refund timeline, not a merchant one. The chunk does say merchant refunds aren't covered and to contact the merchant, but that line sits next to a timeline that looks like an answer. Catching this needs the system prompt and answer-quality scoring, not retrieval.

## Behaving as expected

- **Ambiguous questions** went where the ambiguity pointed. Q04 ("did they approve it yet?") pulled KYC timing first and the disputes answer second. Q17 ("will I get it back in full?") pulled fees first and plan refunds third.
- **Q06:** the general "why did my payment fail?" section outranked the specific "insufficient funds" section, which came 2nd. Overview sections attract specific questions.
- **2FA questions (Q27 to Q29)** and most disputes questions hit at rank 1.

## What Act 2 changes, and why

**One change only: one chunk per heading section** (decision B11). Each section gets its own embedding, with nothing else changed: same model, same questions, same labels, same scoring.

- It targets diagnosis 1 directly (Q10), and partly diagnosis 2 (Q12's diluted target).
- It doesn't fix typos (diagnoses 2 and 3), competing bridges (5), the vocabulary trap (4) or the coverage gap (6). Those need different tools: query rewriting, intent-aware routing, or prompt-level abstention.
- Because it's a single change, any difference between the runs can be attributed to it.

## Act 2 results: one chunk per section

Run: `results/act2-headings-20261028-224903`. Act 1 was re-scored with identical settings in `results/act1-rescored-20261028-224849`, and every rank matched the original run, so the pipeline is reproducible.

| Scoring | Act 1 hit@3 | Act 2 hit@3 | Act 1 hit@5 | Act 2 hit@5 | Act 1 MRR | Act 2 MRR |
|---|---|---|---|---|---|---|
| Lenient | 0.864 | 0.909 | 0.955 | 0.955 | 0.717 | 0.739 |
| Strict (at least half correct text) | 0.682 | **0.909** | 0.727 | **0.955** | 0.549 | **0.739** |
| Primary section only | 0.864 | 0.773 | 0.955 | 0.955 | 0.634 | 0.564 |
| Share of first matching chunk that's correct | 59% | **100%** | | | | |

**What the change did:**

- **The lenient numbers barely moved, and the strict ones jumped.** Act 1 was already finding the right *neighbourhood*. Act 2 hands back the right section *on its own*. In Act 1, 41% of the text in the first matching chunk was about something else. In Act 2 it's none. That's the difference the agent would actually feel: less irrelevant text to answer from.
- **Q10 (dilution) improved, 5th to 3rd.** It isn't at the top yet: the tiers section, which also mentions documents, still edges it out.
- **Q06 moved from 2nd to 1st.** Without the overview section's text smeared across its chunk, the specific "insufficient funds" section wins.
- **Q19 and Q20 both moved from 2nd to 1st,** with fees now beating disputes. So diagnosis 5, the competing bridges, was partly a dilution problem too. Once the disputes bridge was no longer averaged together with two other sections, it stopped winning fee questions.

**What it didn't fix, as expected:**

- **Q12** is still a complete miss (typos plus the single mention of "KYC").
- **Q24** is still 4th (typos defeat the bridge).
- **Q22** is still 2nd. The top result is now a failed-payments section rather than the restriction article, but the lockout answer still isn't first.
- **Q14**, the coverage gap, still retrieves the plan refund timeline near the top.

**What it made worse:**

- **Primary-only MRR fell from 0.634 to 0.564.** With every section competing on its own, compound questions now split. Q01 asks for the steps *and* the deadline: the deadline section comes 1st and the steps section, the primary label, drops to 5th. Q28 is vague, so the lockout section beat the SMS section. The lenient measure counts these as hits, because an acceptable section came first, but they show a real trade-off: smaller chunks are purer, and one chunk can't answer a two-part question.
- **Q08 dropped from 1st to 3rd,** and **Q15 from 1st to 2nd.** The fee-refund section beat the plan refund section for "I was expecting a refund."

**Caveat:** 22 questions, so a single question moves hit@3 by about 4.5 points. These numbers show direction, not certainty.

**Next changes, each aimed at a failure Act 2 left:** retrieving a section's neighbours along with it (compound questions), query rewriting or spelling correction (Q12, Q24), a system prompt that abstains when the retrieved text doesn't match the question (Q14), and intent-aware routing before any topic filter (Q22).
