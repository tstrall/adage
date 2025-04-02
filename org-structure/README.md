# Organization Structure

This guide walks you through creating and organizing multiple AWS accounts (e.g., `dev`, `prod`) under a single AWS Organization using the AWS Organizations service.

This enables centralized governance, billing, tagging enforcement, and access control using IAM Identity Center.

---

## Overview

Organizing your accounts lets you:

- Apply security controls and tagging policies globally
- Separate workloads by environment (e.g., `dev`, `qa`, `prod`)
- Enable delegated administration and cross-account roles
- Consolidate billing and budget tracking

---

## Steps

### 1. Enable AWS Organizations

- In the management account, go to **AWS Organizations**
- Click **Create organization**
- Accept defaults (use consolidated billing)

This will enable your account to create and manage sub-accounts.

### 2. Create Organizational Units (OUs)

- In the Organizations console, create an OU named `prod`
- Create another OU named `dev`
- These help group accounts by environment or function

### 3. Create Accounts

- Under each OU, click **Add account**
- Choose **Create account**
  - Set an email address (must be unique)
  - Name the account (e.g., `Production`, `Development`)
- AWS will create the account and send email invitations

You’ll be able to assign roles and permission sets to users across these accounts once they're created.

### 4. Assign Permission Sets via Identity Center

- Go to **IAM Identity Center > AWS Accounts**
- Select the new account
- Assign users or groups and attach existing permission sets (e.g. `AdministratorAccess`)

You can now access the new accounts via the AWS SSO access portal.

---

## After This

Now that your org structure is in place, you can:

- [Set up cross-account access](../cross-account-access/README.md)
- [Define tagging policies](../tagging-policy/README.md)
- [Enable GuardDuty, CloudTrail, and security baselines](../security-baseline/README.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
