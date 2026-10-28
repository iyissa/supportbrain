# Decision log and facts table updates

Paste these into the decision log and facts table. The reason and "what would change my mind" fields for T11 and K12 are left for you, since those changes were your calls.

## Decision log

| # | Decision | Reason | What would change my mind |
|---|---|---|---|
| T11 (revised) | A lockout starts after 5 failed attempts, counting wrong passwords and wrong 2FA codes. It lasts 30 minutes, after which the customer can try to log in again. Identity verification does not end it early. Replaces the earlier version, which let identity verification end the lockout sooner. | [your reason] | [your trigger] |
| K12 (revised follow-up) | If there's no verification decision within 4 business days of submitting documents, email support with the account number and submission date. Replaces the 3-business-day trigger counted from the start of manual review. | [your reason] | [your trigger] |
| K13 | Identity verification can start in the app, or from the login screen ("Can't use your codes?") for a customer who can't log in. The KYC article states both, so it matches the 2FA lost-phone path (T10). | Removes a contradiction between the KYC and 2FA articles. | A separate recovery flow for logged-out customers. |

## Facts table: new entries

Each gets its own label, separate from similar-looking numbers elsewhere.

| Label | Fact | Article |
|---|---|---|
| KYC decision follow-up | Email support after 4 business days from submitting documents | kyc-verification |
| 2FA reset follow-up | Email support after 2 business days from identity verification approval | two-factor-authentication |
| Lockout trigger | 5 failed attempts, wrong passwords and wrong 2FA codes combined | two-factor-authentication |
| Lockout duration | 30 minutes, no early exit | two-factor-authentication |
| Daily limit reset | Midnight in the account's time zone | failed-payments |
| Plan billing during restriction | Paused, resumes when the restriction is lifted, no charge for the paused period | fee-explanations |
| Outcome of confirmed fraud or serious ToS violation | Restriction may stay in place or the account may be closed; support explains which and what happens to the balance | restricted-account-review |
| Logged-out identity verification | Starts from the login screen via "Can't use your codes?" | kyc-verification, two-factor-authentication |
