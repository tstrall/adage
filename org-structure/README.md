# AWS Organization Structure

This guide explains how to set up your AWS Organization and prepare accounts for use with the deployment framework.

## Why Use AWS Organizations?

AWS Organizations lets you:

- Manage multiple accounts under one “management” account
- Isolate environments (e.g., dev vs. prod) using separate accounts
- Centrally manage billing, security, and governance

This is a critical step for creating production-grade infrastructure.

---

## Overview

The AWS deployment framework assumes that your accounts are created inside an AWS Organization and grouped into Organizational Units (OUs) based on environment (e.g., `dev`, `prod`).

Each OU represents a logical environment, and each account inside that OU shares a common environment definition that controls what configuration can be deployed there.

## Steps to Set Up a New Environment

### 1. Create the AWS Organization

If you haven’t already, [create an AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) using the AWS Console. This process creates a root account and enables consolidated billing and centralized identity control.

### 2. Define Organizational Units (OUs)

Create one OU per environment (e.g., `dev`, `prod`). These will group related accounts and determine what configuration applies to them.

### 3. Create Core Accounts Within Each OU

For each environment, create one or more AWS accounts to fulfill different roles. for example:

- `dev-core`, `prod-core`

> ✅ For the simplest possible bootstrap, you can start with just:
>
> - One OU: `prod`
> - One account: `prod-core`\
> That can handle all roles (config, iac, etc.) until you are ready to split responsibilities.

You can name these accounts however you like, but consistent naming makes automation easier.

### Recommended Structure

A minimal structure might look like:

```
[Root Account] (Management)
 ├── Organizational Unit: dev
 │    └── Account: dev-core
 └── Organizational Unit: prod
      └── Account: prod-core
```

### 4. Define the Environment Parameter for Each Account

Each AWS account must declare its environment before configuration or deployment can occur. This is done by manually creating a single Systems Manager Parameter in the account:

- **Parameter Name:** `/aws-config/environment`
- **Type:** `String`
- **Value:** A full JSON blob that defines which Git repo and branch to use for configuration, along with other environment metadata.

#### How to Create It

1. **Download the Environment Configuration File:**
   - Navigate to your fork of the [`aws-config`](https://github.com/tstrall/aws-config) repository.
   - Go to the `account_environments/` directory.
   - Choose the appropriate file:
     - [`dev.json`](https://github.com/tstrall/aws-config/blob/main/account_environments/dev.json)
     - [`prod.json`](https://github.com/tstrall/aws-config/blob/main/account_environments/prod.json)
   - Click **Raw**, then right-click and choose **Save As...** to download the file.

2. **Create the Parameter in AWS Console:**
   - Sign in to the AWS Console for the target account.
   - Open the **Systems Manager** console.
   - Go to **Parameter Store** and click **Create parameter**.
   - Use the following:
     - **Name:** `/aws-config/environment`
     - **Type:** `String`
     - **Tier:** `Standard`
     - **Value:** Paste the contents of the JSON file you downloaded
   - Click **Create parameter** to save.

Once created, this parameter becomes the source of truth for what configuration and infrastructure this account is allowed to use. It is enforced automatically by all deployment scripts.

⚠️ **Reminder:** Only the root account or Org Admin can set the `/aws-config/environment` parameter.

---

## (Optional) Add More Accounts Later

Once your core environment is set up, you can add additional accounts to the same OU at any time.

For example, if you’ve already created `prod-core`, you might later add:

- `prod-iac` — Terraform deployment runner
- `prod-lambda` — Lambda runtime handler
- `prod-data` — Data pipelines or analytics

After creating the account:

1. Log in using a delegated role from the management account
2. Set the `/aws-config/environment` parameter (see Step 4)
3. Assign any required IAM roles or tagging standards

All added accounts will be governed by the same environment binding as their OU.

---

### For more on how framework configuration works, see: [aws-config README](https://github.com/tstrall/aws-config/blob/main/README.md)

---

## Next Steps

If you're following the [AWS Bootstrap Checklist](../bootstrap-checklist.md), continue with:

- [Applying the Security Baseline](../security-baseline/README.md) — Enable CloudTrail, GuardDuty, and more
- [Defining Tagging and Cost Tracking](../tagging-policy/README.md) and [Cost Management](../cost-management/README.md)

---

📚 Return to the [AWS Deployment Guide](../README.md)
