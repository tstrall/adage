# AWS Organization Structure

This guide explains how to set up your AWS Organization and prepare accounts for use with the **Adage** deployment framework.

## Why Use AWS Organizations?

AWS Organizations lets you:

- Manage multiple AWS accounts under one “management” account
- Isolate environments (e.g., dev vs. prod) using separate accounts
- Centrally manage billing, identity, security, and governance

This is a foundational step toward production-grade infrastructure.

---

## Overview

The **Adage** deployment framework assumes your AWS accounts are created inside an AWS Organization and grouped into Organizational Units (OUs) based on environment (e.g., `dev`, `prod`).

Each OU represents a logical environment, and each account within the OU is expected to declare its environment binding — a configuration that determines which Git repository and branch it uses for config and infrastructure.

---

## Steps to Set Up a New Environment

### 1. Create the AWS Organization

If you haven’t already, [create an AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) using the AWS Console. This creates your root (management) account and enables centralized control.

---

### 2. Define Organizational Units (OUs)

Create one OU per environment:

- `dev`
- `prod`

Each OU will contain the accounts that operate within that environment.

---

### 3. Create IaC Accounts Within Each OU

For each environment, create one AWS account for deploying infrastructure and configuration:

- `dev-iac`
- `prod-iac`

For the simplest possible bootstrap, you can start with just:

- One OU: `prod`
- One account: `prod-iac`

You can name these accounts however you like, but consistent naming helps automation.

---

### Recommended Minimum Structure

```
[Root Account] (Management)
 ├── Organizational Unit: dev
 │    └── Account: dev-iac
 └── Organizational Unit: prod
      └── Account: prod-iac
```

---

### Prerequisite: AWS CLI Profile

Before running the setup scripts, make sure you have an AWS CLI named profile configured for the target account (e.g., `dev-iac` or `prod-iac`).

If you're unfamiliar with profiles, refer to the official AWS guide:  
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html


> Ensure your CLI profiles are correctly configured before running any bootstrap scripts.

---

### 4. Define the Environment Parameter for Each *-iac Account

Each AWS account must declare its environment binding before any configuration or infrastructure can be deployed.

Run the following from your local machine (with Python and the AWS CLI installed and configured):

```bash
AWS_PROFILE=dev-iac python scripts/define_account_environment.py --env dev
```

For production:

```bash
AWS_PROFILE=prod-iac python scripts/define_account_environment.py --env prod
```

---

#### What It Does

- Loads the file `account_environments/<env>.json` from the repo
- Writes it to Systems Manager Parameter Store in the currently active AWS account

You can confirm success by checking in the AWS Console:

AWS Systems Manager → Parameter Store → Search for `/iac/environment`

This parameter is used by all **Adage** deployment scripts to resolve environment-specific configuration.

---

## Next Steps

If you're following the [AWS Bootstrap Checklist](../bootstrap-checklist.md), continue with:

- [Applying the Security Baseline](../security-baseline/README.md)
- [Defining Tagging and Cost Tracking](../tagging-policy/README.md)
- [Setting up Cost Management](../cost-management/README.md)

---

Return to [Adage: AWS Deployment Framework](../README.md)
