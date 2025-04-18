# AWS Login Strategy for Adage

This page explains the rationale behind the AWS login strategy used in the Adage deployment framework. It covers the decision to use AWS IAM Identity Center (SSO) in the management account, combined with cross-account role assumption (`OrganizationAccountAccessRole`) for all member accounts.

---

## Overview

In multi-account AWS environments, it’s essential to:

- Centralize access control
- Minimize credential sprawl
- Support automation (e.g., Terraform, scripts, CI/CD)
- Maintain auditability and security boundaries

Adage supports these goals with a hybrid login strategy:

- Use **IAM Identity Center (SSO)** to authenticate into the management account
- Use **standard role assumption** (via `OrganizationAccountAccessRole`) to access member accounts from that session

This strategy is used for both CLI and infrastructure automation.

---

## Why Not Use SSO in Every Account?

While AWS allows direct SSO access into any account, this strategy has tradeoffs:

| Direct SSO in Every Account | Why We Avoid It |
|-----------------------------|------------------|
| Requires `aws sso login` per account | Not scalable for scripts or automation |
| Short-lived sessions expire quickly | Adds friction for infrastructure loops |
| Doesn’t work cleanly in CI/CD | Most runners don't support SSO natively |
| Increased surface area | More permission sets, more complexity |

Instead, Adage assumes roles into member accounts from a single SSO session in the management account.

---

## Trust Model

All member accounts contain a default IAM role named `OrganizationAccountAccessRole`. By default, it is trusted only by the management account.

To allow SSO-based access, we update this trust policy to allow the Identity Center permission set (e.g., `AdministratorAccess`) to assume the role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<management-account-id>:role/aws-reserved/sso.amazonaws.com/<permission-set-id>"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

This enables `AWS_PROFILE=dev-iac` to work immediately after a single `aws sso login --profile management`.

---

## Benefits of This Strategy

- ✅ **Single sign-on** for all environments
- ✅ **Minimal credential setup** per developer or automation pipeline
- ✅ **Works with Terraform, scripts, GitHub Actions, Jenkins**
- ✅ **Easy to rotate, audit, and manage permissions** centrally
- ✅ **No need to define and assign separate permission sets in every account**

---

## Summary

The Adage login strategy is designed for real-world infrastructure workflows:

- Use IAM Identity Center to access the root/management account
- Assume `OrganizationAccountAccessRole` into all other accounts from there

This approach maximizes compatibility, minimizes overhead, and keeps your access control both scalable and secure.
