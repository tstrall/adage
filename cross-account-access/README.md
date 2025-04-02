# Cross-Account Access

This guide explains how to enable secure access across multiple AWS accounts using IAM Identity Center and permission sets.

In an AWS Organization, users can assume roles in any account where they have been assigned — without needing to manage IAM users or long-lived credentials.

---

## Overview

Cross-account access allows you to:

- Access multiple AWS accounts through a single login
- Assign different permission levels per account (e.g. read-only in `prod`, full access in `dev`)
- Eliminate direct IAM user management in child accounts
- Keep centralized control of access through your management account

---

## Steps

### 1. Create a Shared Permission Set (if needed)

If you haven't already created a permission set (e.g., `AdministratorAccess`, `DeveloperAccess`):

- Go to **IAM Identity Center > Permission sets**
- Create a new permission set using:
  - AWS-managed policy (e.g., `AdministratorAccess`) **or**
  - A custom JSON policy for finer control
- Optionally set session duration and tags

### 2. Assign Users to Additional Accounts

- Go to **IAM Identity Center > AWS Accounts**
- Select the target account (e.g., `dev`, `prod`)
- Choose **Assign users or groups**
- Select an existing user or group (e.g., `admin`)
- Attach one or more permission sets

### 3. Log In via the Access Portal

- Go to your organization’s AWS access portal (same URL for all accounts)
- Log in using your IAM Identity Center user
- You will now see tiles for every assigned account and role
- Click any tile to assume that role in the corresponding AWS account

---

## Tips

- You can assign **different permission sets** per account (e.g., `admin` in `dev`, `read-only` in `prod`)
- You can also create **groups** (e.g., `Developers`, `Analysts`) and assign those instead of individual users
- Permission sets are reusable — define once, assign many times

---

## After This

You now have centralized access control across all AWS accounts.

Next steps:

- [Define your tagging policy](../tagging-policy/README.md)
- [Enable organization-wide security monitoring](../security-baseline/README.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
