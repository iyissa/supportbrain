---
title: "Two-factor authentication: setup, codes, lost phones, and lockouts"
topic: two_factor_authentication
issue_type: process
customer_segment: both
severity: high
resolution_type: self-service
canonical: true
related:
  - kyc-verification
  - restricted-account-review
---

## Can I turn off two-factor authentication?

No. Two-factor authentication (2FA) is mandatory on every FinFlow account, so you can't turn it off. 2FA asks for a code as well as your password when you log in. You may also see it called two-step verification or a verification code.

## What 2FA methods can I use?

FinFlow offers 2 methods for getting a 2FA code:

1. An authenticator app, which is the recommended method.
2. SMS, where your code is sent by text message.

You also get 10 single-use backup codes when you set up 2FA. Backup codes aren't a method you choose. They're a fallback for when you can't use your authenticator app or SMS, for example if you lose your phone. Keep them somewhere safe. If you use all 10, you can generate new ones in Security after you log in.

## How do I set up or change my 2FA method?

You set up 2FA when you sign up for FinFlow. Later, you can change your method or view your setup in Security in the app. There are 4 steps to set up or change your 2FA method:

1. Open Security in the app.
2. Choose your 2FA method.
3. Scan the QR code or enter the setup key in your authenticator app. For SMS, confirm your phone number instead.
4. Enter the first code to confirm setup.

When you finish setup, you get 10 single-use backup codes. Save them somewhere safe before you leave the screen.

## Why didn't my SMS code arrive?

If your SMS code doesn't arrive, first check that the phone number on your account is correct. SMS codes expire after 5 minutes. You can request a new code after 60 seconds, up to 3 times in 10 minutes. After the third request, you have to wait for the 10 minutes to pass before you can request another code. In the meantime, log in with your authenticator app or one of your 10 backup codes instead.

## What do I do if I lost my phone?

If you lost your phone, log in with one of your 10 backup codes. Each backup code works only once. If you don't have a backup code, start from the login screen by choosing "Can't use your codes?" You don't need to be logged in. You then verify your identity in 4 steps: choose a document, upload it, take a selfie, and submit. Once your identity verification is approved, your 2FA is reset within 1-2 business days. If your 2FA hasn't been reset within 2 business days of your identity verification being approved, email the support team with your account number and the approval date. To see which documents you can use, read [Identity verification: documents, tiers, and review times]. It explains the accepted IDs, the selfie check, and how long verification takes.

## Why am I locked out of my account?

You're locked out of your account after 5 failed login attempts, counting both wrong passwords and wrong 2FA codes. A lockout means you can't log in, but your money is safe and your account isn't closed. The lockout lasts 30 minutes, and after that you can try to log in again. A lockout is not the same as a restricted account. A restricted account means you can log in and see your balance but can't make transactions, while a lockout stops you logging in at all. If you can log in but can't make transactions, your account may be restricted. Read [Restricted account: what happens when FinFlow reviews your case]. It explains what a restriction means, what you can do in the meantime, and how long a review takes.
