# Organization Structure

This guide explains how to enable AWS Organizations and set up a clean account structure for managing multiple environments like `dev` and `prod`.

Using Organizations allows you to apply policies, manage accounts centrally, and prepare your environment for secure, multi-account deployments.

---

## Why Use AWS Organizations?

AWS Organizations lets you:

- Manage multiple accounts under one “management” account
- Apply Service Control Policies (SCPs) to restrict access at the org/unit/account level
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
- These let you group accounts by environment or purpose

You can later apply Service Control Policies (SCPs) to each OU for access control.

---

### 3. Create or Invite Member Accounts

You have two options:

- **Create a new AWS account** under your org
  - This creates a clean account owned by the organization
  - AWS will send an invitation email to the provided email address

- **Invite an existing AWS account**
  - Requires root access to the external account
  - The invited account must accept the invitation via email

Each member account can have its own Identity Center access rules and permission sets.

---

### 4. (Optional) Enable SCPs

If you want stronger org-wide security controls:

- Go to **Policies > Service control policies**
- Enable SCPs
- Create and attach policies to OUs or accounts

For example, you can:

- Deny access to certain services in `dev`
- Require specific tag keys
- Enforce regional restrictions

---

### Example: Deny Use of EC2 in Dev

This SCP blocks the use of EC2 in all accounts under the `dev` organizational unit:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyEC2InDev",
      "Effect": "Deny",
      "Action": "ec2:*",
      "Resource": "*"
    }
  ]
}
```

Attach this policy to the `dev` OU to prevent the accidental use of EC2 (useful in serverless-only accounts or to control cost).

📌 SCPs do not grant access — they set maximum boundaries on what users **can** do, even if their IAM permissions allow more.

---

## Recommended Structure

A minimal structure might look like:

```
[Root Account] (Management)
 ├── Organizational Unit: dev
 │    └── Account: dev-core
 ├── Organizational Unit: prod
 │    └── Account: prod-core
```

You can extend this to support staging, QA, security-only accounts, etc.

---

## Next Steps

Once your organization is set up, continue with:

- [Applying the Security Baseline](../security-baseline/README.md) — Enable CloudTrail, AWS Config, and GuardDuty
- [Defining a Tagging Strategy](../tagging-policy/README.md) — Standardize cost attribution and access control

---

📚 Return to the [AWS Deployment Guide](../README.md)
