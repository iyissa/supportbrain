# SupportBrain

SupportBrain is a context engineering project. I designed a knowledge base from scratch for retrieval, tested how well an AI could find the right answers in it, and I'm using those test results to improve the knowledge base and, in turn, the AI support agent built on it.

**Status:** in progress. The knowledge base is built, the first baseline test has run, and its failures are documented. I'm now testing changes to the system one at a time.

## What you're looking at

FinFlow is a fictional fintech, and this is the knowledge base behind its AI customer support agent. It has seven articles, one for each support category: account restrictions, plan refunds, transaction disputes, failed payments, identity verification, fees and two-factor authentication.

The articles are built around customer situations rather than topics.

Before writing anything, I created a [checklist](docs/chunk-safe-writing-checklist.md) that protects content against the ways it breaks when it's split into chunks for retrieval. After testing the checklist, I gave it to AI to generate the articles, then reviewed every article myself. That's where information architecture comes in: generating words is easy now, and the real work is in how the content is structured.

## How it's evaluated

I wrote 30 questions the way real customers ask them: some formal, some casual, some with typos, some vague or missing context.

- **23 design questions** are used to test the knowledge base and decide what to change.
- **7 questions are set aside** and won't be used until all the changes are done. They're the final test, to check that the improvements work on questions the changes weren't based on.

Each question is matched to the section of the knowledge base that should answer it. A test then checks whether retrieval returns that section, and how near the top.

Matching questions to sections turned up problems before any test ran: one question the knowledge base deliberately can't answer, one filed under the wrong category, and a few with more than one honest answer.

## Results so far

**Baseline:** the articles were split into fixed-size chunks of about 190 words, regardless of where sections start and end.
**Change 1:** each section became its own chunk.

| | Correct section in the top 3 | Correct section in the top 5 |
|---|---|---|
| Baseline | 19 of 22 questions | 21 of 22 |
| Change 1 | 20 of 22 | 21 of 22 |

(One of the 23 questions can't be answered by the knowledge base on purpose, so it's scored separately.)

The baseline already found the right area for almost every question. But its chunks were bigger than most sections, so they usually mixed two or three sections together, and the AI would get a lot of unrelated text along with the answer. Splitting by section fixed that, though questions that ask two things now get split across sections. I haven't yet tested whether the improvement comes from following the article structure or just from using smaller chunks. That's the next test.

## What I've learned so far

- **A good score can hide a messy answer.** The first test found the right section almost every time. But the text it pulled back was often only half about the question. The rest came from nearby sections the customer didn't ask about.

- **Typos throw it off.** The restriction article mentions that customers might call it "suspended." When a customer typed "suspnded," the system missed that, and the right section came 4th.

- **The customer's words can point the wrong way.** Someone wrote "my account was suspended after I got my password wrong too many times." That's really about being locked out, which is a different article. But the word "suspended" pulled up the restriction article first.

- **A question with no answer can still look like a good match.** I asked about something the knowledge base deliberately doesn't cover: refunds from shops. The system confidently pulled up the article about plan refunds, which an AI could easily turn into a wrong answer. Search can't tell "this is the answer" from "this is close."

## What's next

- **Test chunk size on its own.** Run the baseline again with chunks about the size of a section, to see whether the improvement came from following the article structure or just from smaller chunks.
- **Keep related sections together.** When a question asks two things, bring back the sections around the best match too, so the AI gets the full answer.
- **Clean up questions before searching.** Add a step that fixes typos and rewrites casual wording into the knowledge base's terms, so "my kyc got rejcted" becomes "my identity verification was rejected."
- **Hand off to a human when unsure.** If a question isn't covered or the AI isn't confident, it passes the conversation to a support agent instead of guessing.
- **Log what the knowledge base can't answer.** Every handoff is recorded, so a technical writer can see which questions keep coming up and update the knowledge base.
- **Run the final test.** Once the changes are done, use the 7 set-aside questions to check the improvements hold up.

## Limitations

- **It's small.** Seven articles and 22 scored questions, so the results show a direction, not proof.
- **It only tests search so far.** It checks whether the right section comes back, not whether the AI's final answer is correct. Testing the answers comes later.
- **No predictions were written down before the tests.** I didn't record what I expected before running them, so I can't compare expectations with results. I'll do this for every test from now on.
- **The set-aside questions weren't completely hidden.** They were in front of me while I designed the knowledge base. I built it around customer situations, not those questions, but I can't fully prove they had no influence.
- **The question-to-section matches were drafted with AI,** then checked by me.
- **Some topics are left out on purpose,** like refunds from shops and some account restriction types. They're listed in [`docs/known-gaps.md`](docs/known-gaps.md).

## Run it yourself

```bash
git clone https://github.com/iyissa/supportbrain.git
cd supportbrain
bash run.sh    # the baseline test
bash act2.sh   # Change 1: one chunk per section
```

You'll need Python 3.10 to 3.13. Results are saved in the `results` folder.

## Where to find things

- **The knowledge base articles:** [`kb/`](kb/)
- **The chunk-safe writing checklist the articles were written to:** [`docs/chunk-safe-writing-checklist.md`](docs/chunk-safe-writing-checklist.md)
- **What failed and why, in detail:** [`docs/failure-analysis-act1.md`](docs/failure-analysis-act1.md)
- **Every design decision and the reasoning behind it:** [`docs/decision-log.md`](docs/decision-log.md)
- **Topics left out on purpose:** [`docs/known-gaps.md`](docs/known-gaps.md)
