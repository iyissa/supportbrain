---
title: "Failed payments: why a payment failed and what happens to your money"
topic: failed_payments
issue_type: troubleshooting
customer_segment: both
severity: medium
resolution_type: self-service
canonical: true
related:
  - kyc-verification
  - fee-explanations
  - restricted-account-review
---

## Why did my payment fail?

When a payment fails, FinFlow sends you a notification that names the reason. You may also see this described as a payment declined, a transaction failed, or money taken but the payment failed. There are 5 possible reasons:

1. Funds: there wasn't enough available money in your balance.
2. Limit: the payment would take you over your daily transfer limit.
3. Merchant: the shop or merchant declined the payment.
4. Network: a connection or processing problem stopped the payment.
5. Restriction: your account is restricted, so you can't make transactions.

If you're not sure which reason applies, check the notification for the failed payment. It always names one of these 5 reasons. If you haven't completed Tier 1 identity verification yet, you can't send payments at all, so a payment is never attempted and you won't get a failure notification. Read [Identity verification: documents, tiers, and review times]. It explains which documents to upload, how to submit them, and how long review takes.

## Did I lose money when my payment failed?

It depends on whether the money left your balance. To check, open your transaction history. A failed payment shows as "Failed," and a reversal appears as a separate credit line. If your balance dropped and no credit has appeared yet, the money is in transit. If the money never left your balance, nothing is lost and you don't need to do anything. If the money did leave your balance, the payment is reversed and the money returns to your balance within 2-3 business days, and you'll get a notification when it's back. If you don't see the reversed money in your balance within 2-3 business days, email the support team with the transaction details and your account number. If you paid a fee on the failed payment, the fee is refunded together with the payment. Read [Fees: what FinFlow charges for and when you get a fee back]. It explains which payments carry a fee, how much each fee is, and when a fee is refunded.

## Why does my payment say insufficient funds when my balance looks high enough?

A payment can fail for insufficient funds even when your balance looks high enough, because pending transactions reserve money until they settle. Money reserved for a pending transaction still shows in your balance, but you can't spend it on another payment. Once the pending transaction settles, the reserved money is no longer counted, and your available amount updates. To avoid this failure, wait for pending transactions to settle before sending a payment that needs most of your balance.

## Should I try the payment again?

Don't try the payment again while the money is still in transit, because sending it again can charge you twice. Money is in transit when the original payment shows as pending, or when a failed payment's reversal hasn't reached your balance yet. Once the original payment has failed and any reversed money is back in your balance, what to do next depends on the reason in the failure notification. If the reason is funds or limit, fix the cause and try again. If the reason is merchant, try again, use another payment method, or contact the merchant. If the reason is network, try again. If the reason is restriction, you can't retry until the restriction is lifted.

## Why did my payment fail because of a limit?

A payment fails because of a limit when it would take you over your daily transfer limit. Your daily transfer limit depends on your identity verification tier. The daily limits are $500 for Tier 1, $2,000 for Tier 2, and $10,000 for Tier 3. The limit resets at midnight in your account's time zone, so you can try again after it resets. To raise your limit, complete the next verification tier. If you're already on Tier 3, you're at the highest limit, so wait for the reset or use another payment method. Read [Identity verification: documents, tiers, and review times] to see what each tier needs. It explains the accepted documents, what each tier requires, and how long verification takes.

## Why did my payment fail because my account is restricted?

A payment fails with the restriction reason when your account is restricted. A restricted account means you can log in and see your balance, but you can't make transactions. If a payment was in progress when the restriction was placed, that payment is reversed to your balance and stays frozen until the restriction is lifted. To find out why your account is restricted and how the restriction ends, read [Restricted account: what happens when FinFlow reviews your case]. It explains what a restriction means, what you can do in the meantime, and how long a review takes.
