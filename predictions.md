# Predictions

> **Not used for Act 1 (decision B9).** Act 1 ran without predictions, by choice. Use this template before the Act 2 rerun and again before unsealing the held-out set: fill it in, commit it, then run. Don't backfill Act 1.

Fill this in **before** running the baseline, then commit it, so the timestamp shows the predictions came first.

- **Hit?** Will a labeled section appear in the top k? (yes / no / unsure)
- **Rank:** if yes, roughly where (1, 2-3, 4-5)
- **Why:** the reason in a few words
- **Likely layer if it fails:** content, structure/chunking, vocabulary, ambiguity, or category mismatch

| qid | question | labeled answer | Hit? | Rank | Why | Likely layer if it fails |
|---|---|---|---|---|---|---|
| Q01 | I noticed a charge on my FinFlow account from a merchant I have never transacted with. What are the steps to file a dispute, and how long do I have to submit one? | transaction-disputes#3 (+transaction-disputes#1) |  |  |  |  |
| Q03 | some1 charged me twice at the same shop, how do i disptue it?? its been 3 days | transaction-disputes#3 (+transaction-disputes#1) |  |  |  |  |
| Q04 | so did they approve it yet? been waiting all week | transaction-disputes#4 |  |  |  |  |
| Q05 | can i dispute a transfer i sent to the wrong person or is that different from a card charge | transaction-disputes#2 |  |  |  |  |
| Q06 | My payment to a merchant failed with an "insufficient funds" error even though my balance was sufficient. What could cause this? | failed-payments#3 |  |  |  |  |
| Q08 | my paymnet keeps faling and the money left my acount, wat is hapening | failed-payments#2 (+failed-payments#1, failed-payments#4) |  |  |  |  |
| Q09 | why did it fail again? i already tried twice | failed-payments#1 (+failed-payments#4) |  |  |  |  |
| Q10 | Which documents does FinFlow accept for identity verification, and what are the file format requirements for uploading them? | kyc-verification#2 |  |  |  |  |
| Q11 | I am having difficulties with the verification process on my account and require assistance. | kyc-verification#6 (+kyc-verification#3, kyc-verification#5) |  |  |  |  |
| Q12 | my kyc got rejcted agan, i uploded my pasport like u said | kyc-verification#6 |  |  |  |  |
| Q14 | How long does a refund for a cancelled merchant purchase take to appear in my FinFlow balance? | (gap) (+plan-refunds#1) |  |  |  |  |
| Q15 | I was expecting a refund but I am unsure about its status. What should I understand about the process? | plan-refunds#3 (+plan-refunds#1) |  |  |  |  |
| Q17 | will i get it back in full or is there a deduction? | plan-refunds#2 |  |  |  |  |
| Q18 | What is the fee for an international transfer from a FinFlow personal account, and how is the exchange rate applied? | fee-explanations#3 (+fee-explanations#1) |  |  |  |  |
| Q19 | I noticed the amount deducted from my account was different from what I expected. Could you clarify the charges? | fee-explanations#4 (+fee-explanations#1, fee-explanations#3) |  |  |  |  |
| Q20 | why was i charged a fee?? nobody told me abou this charge on my transfar | fee-explanations#1 (+fee-explanations#2, fee-explanations#4) |  |  |  |  |
| Q22 | My account was suspended after multiple failed login attempts. What is the process for having it reinstated? | two-factor-authentication#6 |  |  |  |  |
| Q23 | I am unable to access my account and it appears that some restriction has been applied. What does this mean? | restricted-account-review#1 (+two-factor-authentication#6) |  |  |  |  |
| Q24 | my acount got suspnded this morning and i dont even know why | restricted-account-review#1 (+restricted-account-review#2) |  |  |  |  |
| Q25 | can i still get my money out? | restricted-account-review#2 (+restricted-account-review#4) |  |  |  |  |
| Q27 | How do I set up two-factor authentication using an authenticator app instead of SMS codes? | two-factor-authentication#3 (+two-factor-authentication#2) |  |  |  |  |
| Q28 | I am having trouble with the security code feature when logging in. Could you help? | two-factor-authentication#4 (+two-factor-authentication#5, two-factor-authentication#6) |  |  |  |  |
| Q29 | i lost my phone and cant get the 2fa code to login, wat do i do | two-factor-authentication#5 (+kyc-verification#3) |  |  |  |  |

## Overall predictions

- Hit-rate@3 for the 22 answerable questions: ___
- Hit-rate@5: ___
- MRR: ___
- The question I am least sure about, and why: ___
- What Q14 (the coverage gap) will retrieve, and whether the agent would invent an answer: ___
