# Design Principles: Environment and Account Strategy

This document explains the reasoning behind using one AWS account per environment (e.g., `dev-core`, `prod-core`) instead of splitting every concern (e.g., `dev-iac`, `dev-config`, `dev-lambda`) into separate accounts per organizational unit (OU).

This approach keeps the system simple and secure while leveraging Git, IAM, and AWS Parameter Store to provide isolation and governance.

---

## Guiding Principle

**"Use the minimum number of accounts needed to maintain security, clarity, and agility."**

More accounts = more isolation, but also more management overhead. Instead of going all-in on account sprawl, this system favors environment isolation first, and achieves separation of concerns via config and roles.

---

## What We Gain With One Account Per Environment

| Mechanism | Purpose |
|----------|---------|
| `prod-core`, `dev-core` | Full isolation of environments at the account level |
| Git repo structure (`/prod/vpc/nickname/config.json`) | Declarative separation of all infra by environment |
| IAM roles (e.g., `lambda-admin`, `config-writer`) | Restrict what services and humans can do within each account |
| Parameter Store with tags | Identify environment and config roles at runtime |

This lets us:
- Run CI/CD safely in `dev` without touching `prod`
- Use IAM to ensure no cross-contamination
- Run runtime routing (e.g., switchover) based on Parameter Store values
- Do all of this in a demo or portfolio without extra AWS accounts

---

## When to Use Multiple Accounts Per OU

Multiple accounts **can** be useful if you need:

| Scenario | Reason |
|----------|--------|
| PCI / PHI / secure data boundaries | Enforced audit/compliance and data segregation |
| Separation of billing by team or product | Clear chargebacks or spend visibility |
| Devs must be locked out of prod | Absolute permission boundaries |
| Partner orgs or external teams | Separate trust domains and access models |

For most internal or solo deployments (like `strall.com`), this is not necessary. IAM and disciplined config governance provide enough control.

---

## Summary

Start with one account per environment:

- ✅ Keeps things easy to manage
- ✅ Still provides real environment isolation
- ✅ Plays well with your config-driven, Git-backed deployment model
- ✅ Avoids cost and friction until you truly need more isolation

You can always expand to multiple accounts later — but you may never need to.