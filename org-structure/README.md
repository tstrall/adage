# Organization Structure

This guide explains how to enable AWS Organizations and set up a clean account structure for managing multiple environments like `dev` and `prod`.

Using Organizations allows you to apply policies, manage accounts centrally, and prepare your environment for secure, multi-account deployments.

---

## Why Use AWS Organizations?

AWS Organizations lets you:

- Manage multiple accounts under one “management” account
- Isolate environments (e.g., dev vs. prod) using separate accounts
- Centrally manage billing, security, and governance

This is a critical step for creating production-grade infrastructure.

---

## Steps

### 1. Enable AWS Organizations

- Log in to the **management account** as the root user or an Identity Center user with admin privileges
- Go to **AWS Organizations** in the console
- Click **“Create organization”**

You’ll now have access to org units, consolidated billing, and account invites.

---

### 2. Create Organizational Units (OUs)

- In the Organizations console, click **Organize accounts**
- Create units like:
  - `dev`
  - `prod`

These let you group accounts by environment or purpose

---

### 3. Create Member Accounts

- **Create a new AWS account** under your org
  - This creates a clean account owned by the organization
  - AWS will send an invitation email to the provided email address
  - **Each account must use a unique email address**

> 🔪 For the simplest possible bootstrap, youn can start with just:
>
> - One OU: `prod`
> - One account: `prod-core`\
> That can handle all roles (config, iac, etc.) until you are ready to split responsibilities.

---

## Recommended Structure

A minimal structure might look like:

```
[Root Account] (Management)
 ├── Organizational Unit: dev
 │    └── Account: dev-core
 └── Organizational Unit: prod
      └── Account: prod-core
```

You can extend this to support staging, QA, security-only accounts, or divide responsibilities further (e.g. `prod-iac`, `prod-network`).

---

## Next Steps

Once your organization is set up, continue with:

- [Applying the Security Baseline](../security-baseline/README.md) — Enable CloudTrail, AWS Config, and GuardDuty
- [Defining a Tagging Strategy](../tagging-policy/README.md) — Standardize cost attribution and access control
- [Using org\_structure.py](../../scripts/bootstrap/org_structure.py) — Automate the creation of additional accounts and environment tagging

---

📚 Return to the [AWS Deployment Guide](../README.md)

