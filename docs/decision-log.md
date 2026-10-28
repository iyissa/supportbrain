# Decision Log: KB design session (cumulative, Oct 28, 2026)

Replaces `decision-log-additions.md`. Append to the existing `decision-log.md`, below the entries already there.

**Format:** decision / reason / what would change my mind.
**Owner:** **Ayo** = decided by Ayo. **Proposed** = decided by Claude on Ayo's delegation ("make all domain decisions, I'll document"). Accept or edit each Proposed entry.
**NEEDS TRIGGER** = no "what would change my mind" line yet. Suggested lines are marked "Suggested" and are Ayo's to accept or replace.

**Renumbering note:** the fees-article decisions earlier called F6-F10 are now **Fe6-Fe10**, to stop them clashing with the failed-payments rules. Failed-payments decisions are F1-F5 and F11-F18 (F6-F10 are intentionally unused).

---

## A. Account suspension

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| A1 | One state, "restricted," replaces restricted/suspended. | Both froze the balance and allowed login, so nothing separated them. | NEEDS TRIGGER. Suggested: a behavior that differs between the two states. | Ayo |
| A2 | Balance is visible but untouchable. "Move" means any transaction on the available balance (airtime, transfers, withdrawals). | Blocks outflow from flagged accounts (compliance). | Verified, long-history customers whose frozen balances cause hardship the freeze can't justify. Exception process is out of v1 scope. | Ayo |
| A3 | In-flight payments reverse to the sender. Reversed funds return to the balance but stay frozen. | No money in limbo. FinFlow takes no burden toward recipients. | NEEDS TRIGGER. Suggested: recipient disputes, or compliance requiring in-flight funds be held. | Ayo |
| A4 | Reversal arrives within 2-3 business days. Customer is notified when it lands. Email support after 2-3 days with transaction details, account number, restriction date. | Silence recreates the "where is my money" fear. | NEEDS TRIGGER. Suggested: a timeline in another article that contradicts it. | Ayo (notification), Proposed (range) |
| A5 | Restriction ends when the recommended action is completed (or review finishes). | The flag persists until resolved. | NEEDS TRIGGER. | Ayo |
| A6 | Customer-facing reasons are generic banner categories (compliance, documentation, etc.). | Some reasons can't be disclosed (sanctions, fraud, legal). | NEEDS TRIGGER. | Ayo |
| A7 | Cross-category content is pointed to, not duplicated. Short facts a section needs to stand alone are repeated. Pointers carry the target's exact title plus a one-line summary. | Detail in one place. Sections must stand alone for retrieval. | If repeated facts drift out of sync, centralize more. | Ayo (point), Proposed (repeat the minimum) |
| A8 | 17 flag reasons split by **who moves first**. Resolvable (13): customer moves first. Not resolvable (4): potential fraud, sanctions, legal/regulatory hold, ToS violation. | The customer wants to know "is it me or FinFlow doing something next?" | NEEDS TRIGGER. Suggested: a row whose ownership is ambiguous in practice. | Ayo |
| A9 | Sanctions: FinFlow reviews first, then asks for enhanced verification. | Customer doesn't move first. | NEEDS TRIGGER. | Ayo |
| A10 | Customer stays in a problem section as ownership changes (act, then wait), not moved between articles. | Avoids switching articles mid-journey. | NEEDS TRIGGER. | Ayo |
| A11 | Durations are ranges, not exact times. First contact after review is 3-5 business days. Follow-up email after 5 business days. | Ranges avoid false promises. | NEEDS TRIGGER. Also needs the single source of truth (section G). | Ayo (ranges), Proposed (numbers) |
| A12 | No expedite path in v1. Customers email only after the 5-day range passes. | Expediting needs a per-situation rule that doesn't exist. | A situation (e.g. ToS review) being defined as expeditable. | Ayo |
| A13 | Size limit raised for the suspension article. **No ceiling set.** | Four sections plus repeated facts don't fit 250-400 words. | NEEDS TRIGGER. Suggested ceiling: 800-1,000 words. | Ayo |
| A14 | Opening section names only the reasons the article covers, plus a pointer elsewhere. | Avoids an all-17-reasons chunk that matches every restriction query. | If Act 1 shows customers can't self-route. | Ayo |
| A15 | Vocabulary bridge in the opening chunk: FinFlow says "restricted," customers may say "suspended" or "banned." The same chunk says what restricted means. | Semantic-gap risk named before Act 1. | If Act 1 shows the bridge doesn't help retrieval. | Ayo |
| A16 | Failed-login lockout is **not** "restricted." It lives in the 2FA article. | A locked-out customer can't log in. A restricted one can. | A regulator or real data requiring different treatment. | Proposed |
| A17 | Confirmed sanctions match or legal/regulatory hold: funds stay frozen and are handled as the relevant authority (court, regulator) instructs. No release date promised. Covered by Section 4 of the article. | Honest expectation-setting. FinFlow doesn't control the outcome. | Legal advice, or a regulator requiring return of funds. | Proposed |
| A18 | Banners asking for identity documents or information point to the KYC article. Other fixable reasons say "follow your banner" and "a full article is coming soon." | The fixable-restrictions article is cut from v1. | That article being written. | Proposed |
| A19 | Confirmed fraud or a serious ToS violation: FinFlow may keep the restriction or close the account. Support says which, and what happens to the balance, at first contact. | Matches the flag table without promising an outcome. | A fixed policy on closed-account balances. | Proposed |

## B. Scope and process

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| B1 | v1 KB is **7 articles, one per category.** (Ayo to confirm.) Cut to post-launch: the 13-section fixable-restrictions article, merchant refunds, wrong-person recall article, pending-reservations explainer. | Deadline Nov 1. Started the KB late on Oct 26. | Time allowing more. Add in this order: fixable restrictions, recalls, merchant refunds. | Proposed |
| B2 | Article length limits: 250-400 words is the default. Raised for the suspension article. Other articles run longer (failed payments about 700 words). Length judged acceptable. | Each section must pass the four rules, and length isn't a retrieval problem if chunks stand alone. | If Act 1 shows long articles split badly. | Ayo |
| B3 | **Revised Oct 28.** Claude makes FinFlow domain decisions; Ayo logs them and can override. Article prose is drafted by Claude from the domain rules and the Chunk-Safe Writing Checklist, with the design questions kept out of the drafting prompts. Ayo reviews and revises every section against the four rules. (Previously: Ayo writes all prose by hand.) | Time: the KB went from 1 article to 7 in a day. The skill the project demonstrates is the shape of the content and the review against the checklist, not typing the words. | If AI-drafted prose shows failure patterns the checklist doesn't catch. | Ayo |
| B4 | Reviews cover content only. Formatting (front matter, headings, list syntax, `related` slugs) is applied when saving to the repo. | Ayo's instruction. | n/a | Ayo |
| B6 | Act 1 run settings, fixed before any results: fixed-size chunking at 256 tokens with 20 overlap and no heading awareness; frontmatter stripped; `BAAI/bge-small-en-v1.5` embeddings; fresh in-memory ChromaDB; retrieval only. | Library defaults (1,024 tokens) would make most articles a single chunk, so the baseline would only test article-level retrieval and say nothing about structure. 256 tokens is still naive and is the mid-section splitting the checklist defends against. | n/a once results exist. Changing these after seeing results is fitting to the test. | Ayo |
| B7 | Scoring: a hit is a retrieved chunk that overlaps any labeled section (primary or alternate). Report hit-rate@3, hit-rate@5 and MRR@5, plus a primary-only number. Coverage-gap questions are excluded and reported separately. | Section-level labels survive chunking changes, so Act 1 and Act 2 are directly comparable. | A reviewer preferring stricter primary-only as the headline. | Ayo |
| B8 | Ground-truth section labels for the 23 design questions were drafted by Claude after the KB was frozen, before any retrieval ran, and reviewed by Ayo. Labeling found 1 coverage gap (Q14), 1 miscategorized question (Q22) and 5 ambiguous questions (Q04, Q11, Q15, Q23, Q28). | Labels have to exist before results, or they bend toward whatever was retrieved. | Ayo disagreeing with a label on review. | Ayo |
| B9 | **Act 1 runs without predictions, by choice.** **Update, Oct 28:** the first Act 2 change (B11) also ran without predictions, against this rule. It's disclosed rather than backfilled. The rule stands for every later change and for the held-out set. The corpus is still tagged `kb-v1` before the run, and the held-out questions stay in `sealed/`, never passed to the script. **Predictions are required before the Act 2 rerun and before unsealing the held-out set:** write them in `predictions.md`, commit, then run. | Time: the follow-up call is the next morning. Skipping predictions for Act 1 is disclosed rather than backfilled. | n/a. Predictions written after seeing results don't count and must not be added for Act 1. | Ayo |
| B10 | **Added after Act 1:** a strict measure, where a hit needs a chunk that's at least half correct-section text, plus the average share of correct text in the first matching chunk. Reported for Act 1 (re-scored, same settings) and Act 2. The original lenient measures stay as the headline definitions from B7. | Reading the Act 1 chunks showed 19 of 26 straddle two or three sections, so the lenient rule credits chunks that are mostly about something else. Disclosed as added after seeing results. | n/a | Ayo |
| B11 | Act 2 makes **one change only**: one chunk per heading section (`MarkdownNodeParser`). Same model, questions, labels and scoring. | Targets the chunk-dilution failure (Q10, partly Q12). A single change means the difference between runs can be attributed to it. Typos, competing bridges, the Q22 vocabulary trap and the Q14 coverage gap are left for later changes. | If heading chunks lose recall on questions that need two adjacent sections. | Ayo |
| B5 | Metadata uses controlled values. See section F. Front matter is raw YAML, not a code fence. | Consistent values make metadata filtering reliable. A fenced block would be read as body text. | A new category or resolution type. | Proposed |

## C. Refund timelines

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| R1 | Article covers refunds after cancelling a FinFlow paid plan. Merchant refunds are out of v1. | One article, one situation. | Merchant refunds being more common in the KB. | Proposed |
| R2 | Refund is prorated by unused days, counted from the cancellation date. | Simple to state. | Non-refundable periods. | Proposed |
| R3 | Refund returns to the FinFlow balance, never to a card or bank account. | One destination, one timeline. | Plans payable by external card. | Proposed |
| R4 | Refund takes 3-5 business days after cancellation is confirmed. Labeled separately from the review first-contact range. | A calculation step makes it slower than a reversal. | A merchant-refund timeline that contradicts it. | Proposed |
| R5 | Refund is automatic. Customer is notified when it lands. | Matches the reversal-notification rule. | Compliance review needing customer input. | Proposed |
| R6 | Email support if no refund after 7 business days (plan name, cancellation date, account number). | Gives the customer a point to chase. | Support capacity. | Proposed |
| R7 | On a restricted account, the refund arrives but is frozen. Article points to the restriction article. | Consistent with A2. | Holding refunds during review. | Proposed |
| R8 | No cancellation fee on plan cancellations. | Answers "is there a deduction?" in the amount chunk. | FinFlow adding cancellation fees or non-refundable periods. | Proposed |
| R9 | The opening chunk bridges vocabulary: money back, cancellation refund, reimbursement. Article states that it doesn't cover how to cancel. | Customers will type "money back." | Act 1 retrieval results. | Proposed |

## D. Transaction disputes

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| D1 | Disputes cover unrecognized or duplicate charges. A transfer to the wrong person is a recall request, not a dispute. | FinFlow can't force a recipient to return money. | Adding transfer protection. | Proposed |
| D2 | Filing window is 60 days from the transaction date. | Clear deadline. | Regulation or support data. | Proposed |
| D3 | Filing has 4 steps (select the transaction, choose a reason, add details or evidence, submit). | Rule 2. | A change to the in-app flow. | Proposed |
| D4 | Decision takes 7-10 business days from submission. No provisional credit in v1. If upheld, funds return to the balance and the customer is notified. | Keeps v1 simple. | Hardship cases from missing credit. | Proposed |
| D5 | Reporting an unauthorized transaction can restrict the account. The article points to the restriction article. | Matches the flag table. | Dropping that flag reason. | Proposed |
| D6 | A recall request starts by emailing support with transaction details and account number. FinFlow contacts the recipient's bank. The money returns only if the recipient agrees. | Honest about FinFlow's limits. | Adding transfer protection, or a recall timeline. | Proposed |
| D7 | If a dispute isn't upheld, the charge stays and the customer is notified with an explanation. No appeal in v1. | Keeps v1 simple. | Customers repeatedly needing to challenge outcomes. | Proposed |
| D8 | If a dispute is upheld on a restricted account, the money returns to the balance but stays frozen. | Consistent with A2 and R7. | Releasing dispute refunds during review. | Proposed |
| D9 | A restricted customer can still file and track a dispute, because filing doesn't move money. | Consistent with "move = any transaction on the balance." | Fraud patterns abusing disputes while restricted. | Proposed |

## E. Failed payments

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| F1 | Two cases: money never left (nothing needed), or money left (reversed within 2-3 business days, same range as A4). | One source of truth for reversals. | Separate processing for failed payments. | Proposed |
| F2 | Pending transactions reserve funds until they settle, which explains "insufficient funds" on a balance that looks sufficient. | Realistic, explainable cause. | A system that doesn't reserve funds. | Proposed |
| F3 | Don't retry while money is in transit, to avoid a double charge. | Prevents the costliest mistake. | Reliable duplicate detection. | Proposed |
| F4 | Daily transfer limits depend on KYC tier. | Reuses the tier idea. | A flat limit. | Proposed |
| F5 | The failure notification names one reason category: funds, limit, merchant, network, or restriction. | Answers "why did it fail." | Privacy limits on merchant declines. | Proposed |
| F11 | The article lists all five reasons in plain words, and the notification always names one of them. | Answers "why" in one place. | Privacy limits on merchant declines. | Proposed |
| F12 | A fee charged on a failed payment is refunded with the payment, within the same 2-3 business days. The article points to the fees article. | Matches Fe8. | Separate fee-refund timing. | Proposed |
| F13 | Retrying is safe once the payment shows as failed and the balance is restored, or if the money never left. Otherwise wait for the reversal. | Gives the retry section a clear test. | Reliable duplicate detection. | Proposed |
| F14 | To check whether money left: open transaction history. A failed payment shows as "Failed." A reversal shows as a separate credit line. A dropped balance with no credit means the money is in transit. | Gives the customer a concrete check. | A different in-app display. | Proposed |
| F15 | Merchant failure: try again after the reversal, use another payment method, or contact the merchant. Network failure: try again after the reversal. | Tells each customer what to do next. | Real decline-code data. | Proposed |
| F16 | Daily limits: $500 for Tier 1, $2,000 for Tier 2, $10,000 for Tier 3. | Concrete numbers let the section answer "what's my limit?" | A risk model you prefer. Update the KYC article together. | Proposed |
| F17 | The daily limit resets at midnight in the account's time zone. | Gives the customer a "try again" time. | A rolling 24-hour window. | Proposed |
| F18 | Tier 3 is the highest tier, so there's no way to raise the limit further. | Closes a dead end. | Adding a higher tier or limit-increase request. | Proposed |

## F. Metadata: controlled values

| Field | Allowed values |
|---|---|
| `topic` | `account_suspension`, `refund_timelines`, `transaction_disputes`, `failed_payments`, `kyc_verification`, `fee_explanations`, `two_factor_authentication` |
| `issue_type` | `process`, `informational`, `troubleshooting` |
| `resolution_type` | `self-service`, `agent-required`, `automatic` |
| `customer_segment` | `both` (the only value used so far) |
| `related` | file slugs: `plan-refunds`, `fee-explanations`, `transaction-disputes`, `failed-payments`, `kyc-verification`, `two-factor-authentication`, `restricted-account-review` |

## G. KYC verification

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| K1 ⚑ | Accepted: passport, national ID, or driver's licence, plus a selfie liveness check. JPG, PNG, or PDF, up to 10 MB. | Standard practice. | A regulatory requirement. | Proposed |
| K2 ⚑ | Tier 1: ID + selfie. Tier 2 adds proof of address. Tier 3 adds source of funds. Limits rise with each tier. | Matches the tier reasoning. | Fewer tiers. | Proposed |
| K3 ⚑ | Automated checks take up to 24 hours. Manual review takes 1-3 business days. | Two honest ranges. | Review backlog. | Proposed |
| K4 | A rejection shows a reason. After 3 rejected attempts in 24 hours, the case goes to manual review. | Stops resubmission loops. | Abuse patterns. | Proposed |
| K5 | Failed verification can restrict the account. The restriction article points here for steps. | Point, don't duplicate. | None. | Proposed |
| K6 | Verification has 4 steps (choose a document, upload it, take a selfie, submit). | Rule 2 needs a defined list. | A change to the in-app flow. | Proposed |
| K7 | Until Tier 1 is complete, you can log in and view your account but can't send payments. | Gives the tiers a floor. | A small default limit for unverified accounts. | Proposed |
| K8 ⚑ | Tier 2 proof of address: utility bill or bank statement dated within 3 months. Tier 3 source of funds: payslip or bank statement. | Makes tier requirements concrete. | Regulatory requirements. | Proposed |
| K9 | Article title is exactly "Identity verification: documents, tiers, and review times." File slug is `kyc-verification`. | Matches pointers in other articles. | Renaming, which means updating every pointer. | Proposed |
| K10 ⚑ | Tier 1 is usually automated (up to 24 hours). Tier 2 and 3 usually need manual review (1-3 business days). | Gives each tier an honest range. | Review backlog. | Proposed |
| K11 | If an automated check takes longer than 24 hours, it moves to manual review. | Closes the gap in the timing section. | Reliable automated-check SLAs. | Proposed |
| K12 | Email support if you haven't heard back within 4 business days of submitting. | Customers can see when they submitted, not when manual review began. | Faster review SLAs. | Proposed |
| K14 | Identity verification can start in the app, or from the login screen ("Can't use your codes?") for a customer who can't log in. The KYC article states both. | Removes a contradiction with the 2FA lost-phone path (T10). | A separate recovery flow for logged-out customers. | Proposed |
| K13 | **Unverified customers are blocked before they can attempt a payment, so they never reach a failure notification.** Confirmed by Ayo Oct 28. The clause is in section 1 of the failed payments article, with a pointer to the KYC article. | Closes the gap between K7 and F5 without adding a sixth failure reason. | Deciding that unverified payments can be attempted and fail. | Proposed |

## H. Fee explanations

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| Fe1 | FinFlow-to-FinFlow transfers and card payments are free. Bank transfers carry a flat fee. International transfers carry a percentage fee plus an exchange-rate margin. | Covers the main fee situations. | A real pricing model. | Proposed |
| Fe2 ⚑ | The fee is shown on the confirmation screen before the customer commits. | Answers "no one told me." | A screen that can't show it. | Proposed |
| Fe3 | The fee is deducted as a separate line item on top of the amount sent. | Explains amount-sent vs. amount-deducted differences. | Fee-inclusive pricing. | Proposed |
| Fe4 | Fees are refunded when a payment fails or is reversed, not on completed transfers. | Consistent with reversals. | Policy cost. | Proposed |
| Fe5 ⚑ | No transaction fees accrue while restricted. Plan fees are not charged during a restriction. | Fair to the customer. | Revenue impact. | Proposed |
| Fe6 ⚑ | Bank transfer flat fee is $1.00. International transfers carry a 1.5% fee plus a 0.5% exchange-rate margin. The confirmation screen shows the fee and the final rate. | Concrete numbers let the article answer "what will I pay?" Update the facts table with any change. | A pricing model you prefer. | Proposed |
| Fe7 | A paid plan is charged from the FinFlow balance at the start of each billing period. The price shows on the plan page. | Consistent with R3. | Plans payable by external card. | Proposed |
| Fe8 | A refunded fee returns to the balance together with the payment, within 2-3 business days. | One source of truth for reversals. | Fees refunded on a separate schedule. | Proposed |
| Fe9 | Metadata uses the controlled lists in section F. | Consistent values make filtering reliable. | A new category or resolution type. | Proposed |
| Fe10 | During a restriction, the paid plan stays active and billing is paused. Billing resumes when the restriction is lifted, with no back-charge. | Avoids penalizing customers for a FinFlow-imposed freeze. | Revenue impact, or abuse. | Proposed |

## I. Two-factor authentication

| # | Decision | Reason | What would change my mind | Owner |
|---|---|---|---|---|
| T1 | Methods: authenticator app (recommended) and SMS. 10 single-use backup codes are a fallback, not a method. | Standard set. | A new method. | Proposed |
| T2 | Setup has 4 steps (open Security, choose the method, scan or enter the key, enter the first code). | Rule 2. | A change to the app flow. | Proposed |
| T3 ⚑ | SMS codes expire after 5 minutes, can be resent after 60 seconds, max 3 requests per 10 minutes. After the third request, wait for the 10 minutes to pass. Meanwhile use the authenticator or a backup code. | Gives the limit a consequence. | A carrier issue. | Proposed |
| T4 | Lost phone: use a backup code. Without one, start from the login screen ("Can't use your codes?") and re-verify identity. 2FA resets within 1-2 business days of approval. | One recovery path with no dead end. | Security review. | Proposed |
| T5 | 2FA is mandatory. The method can be switched, but 2FA can't be turned off. | Reduces fraud risk. | Customer friction data. | Proposed |
| T6 | **Superseded by T14.** Previously: lockout ends after 30 minutes or sooner via identity verification. | Identity verification takes longer than the lockout, so it could never shorten it. | n/a | Proposed |
| T7 | If you've used all 10 backup codes, generate new ones in Security after logging in. | Closes a recovery dead end. | A different recovery path. | Proposed |
| T8 | 2FA works as normal during a restriction, because logging in is allowed. | Consistent with the restricted-state rules. | Locking sensitive screens during review. | Proposed |
| T9 | Email support if 2FA hasn't been reset within 2 business days of identity verification being approved (account number, approval date). | Gives the 1-2 day range a "what if it passes" line. | Faster resets. | Proposed |
| T10 | A customer without their phone or backup codes starts recovery from the login screen without being logged in, and completes the 4 identity-verification steps. | Removes the lost-phone dead end. | A different recovery channel. | Proposed |
| T11 ⚑ | A lockout starts after 5 failed attempts, counting wrong passwords and wrong 2FA codes. | Gives the lockout a concrete trigger. | Abuse patterns. | Proposed |
| T12 | After the third SMS request in 10 minutes, wait for the 10 minutes to pass. | Gives the limit a consequence. | A carrier issue. | Proposed |
| T13 | New customers set up 2FA during sign-up. Security in the app is where you change your method or view your setup. | Matches "mandatory on every account." | A grace period for new accounts. | Proposed |
| T14 | A lockout lasts 30 minutes and can't be shortened. A lockout is not a restriction. | Verification takes longer than the lockout. | A support-assisted unlock option. | Proposed |

## J. Exposure note

**Fact:** the sealed held-out file (7 questions) and the design set were shared in the same conversation in which Claude helped design the KB domain rules and outlines.
**What was affected:** domain rules and numbers were set by Claude after it had seen the questions. Rules in areas the sealed set may cover are marked ⚑ (K1, K2, K3, K8, K10, Fe2, Fe5, Fe6, T3, T11, plus the limits in F16).
**Mitigation:**
- Rules were derived from customer situations and what a real fintech must define, not from the questions.
- Article prose was drafted by Claude from the domain rules, with the design questions kept out of the drafting prompts, then reviewed and revised by Ayo (B3).
- Held-out results will be reported with and without Q26 (already planned).
- Ground-truth section labels were drafted by Claude after the KB was frozen and before any retrieval ran, then reviewed by Ayo (B8).
**State in the limitations section:** the exposure, that Claude made the domain rules after seeing the questions, that the prose and labels were AI-drafted and human-reviewed, and that independence can't be fully verified.
**What would change my mind:** n/a. This is a disclosure, not a choice.

## K. Facts table (one source of truth)

| Fact | Value | Where it appears |
|---|---|---|
| Review first contact | 3-5 business days | Suspension |
| Follow-up if no review contact | email after 5 business days | Suspension |
| Plan refund (separate process, same range) | 3-5 business days | Refunds |
| Refund follow-up | 7 business days after cancellation confirmed | Refunds |
| Reversal, failed-payment return, fee refund | 2-3 business days | Suspension, failed payments, fees |
| Dispute filing window | 60 days from transaction date | Disputes |
| Dispute decision | 7-10 business days from submission | Disputes |
| Dispute follow-up | 10 business days from submission | Disputes |
| KYC automated check | up to 24 hours | KYC |
| KYC manual review | 1-3 business days | KYC |
| KYC follow-up | 4 business days from submitting | KYC |
| KYC rejections to manual review | 3 in 24 hours | KYC |
| Daily limits | $500 Tier 1, $2,000 Tier 2, $10,000 Tier 3. Resets at midnight (account time zone). | Failed payments, KYC |
| Fees | $1.00 bank transfer, 1.5% international, 0.5% margin | Fees |
| Upload limit | JPG, PNG, PDF, up to 10 MB | KYC |
| SMS codes | expire 5 min, resend after 60 sec, 3 per 10 min | 2FA |
| Lockout | 5 failed attempts, 30 minutes | 2FA |
| 2FA reset | 1-2 business days after verification approved | 2FA |
| 2FA reset follow-up | 2 business days after approval | 2FA |
| Backup codes | 10 single-use | 2FA |

## L. Open items and known gaps

**Decisions needing Ayo**
- "What would change my mind" lines for A1, A3, A5, A6, A8, A9, A10, A11, A13.
- Confirm B1 (7-article target) and A13 (suspension word ceiling).
- Banner reason vs. exit action: the two taxonomies may not line up. Decide before Act 3.

**Known gaps (state in the limitations section)**
- The fixable-restrictions article is cut. Restrictions needing transaction information, device checks, duplicate-account closure, or dispute evidence have only a banner pointer.
- Wrong-person recall requests are covered in one section of the disputes article, not as their own article.
- Merchant refunds are out of scope.
- The KB is 7 articles, not the planned 15.

**Done**
- Ground-truth labeling for the 23 design questions (B8).
- Act 1 run settings fixed (B6, B7). Baseline script written and tested.

**Next steps**
- Tag `kb-v1` and run Act 1, without predictions (B9).
- Act 2 first change ran Oct 28 (results/act2-headings-20261028-224903), without predictions, against B9 (disclosed).
- **Before the next Act 2 change and before unsealing the held-out set: write predictions in `predictions.md` and commit them first (B9). Do not backfill predictions for runs that already happened.**
- Act 1 ran Oct 28 (results/act1-20261028-220444). Failure analysis in docs/failure-analysis-act1.md. Act 2 = heading-based chunking (B11).
- Smoke test for answer quality: Ollama runs Llama 3 (needed for answer-quality scoring, not for Act 1).