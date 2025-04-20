# AWS Organization Structure

This guide explains how to set up your AWS Organization and prepare accounts for use with the **Adage** deployment framework.

---

## Why Use AWS Organizations?

AWS Organizations lets you:

- Manage multiple AWS accounts under one “management” account
- Isolate environments (e.g., dev vs. prod) using separate accounts
- Centrally manage billing, identity, security, and governance

This is a foundational step toward production-grade infrastructure.

---

## Overview

The **Adage** deployment framework assumes your AWS accounts are created inside an AWS Organization and grouped into Organizational Units (OUs) based on environment (e.g., `dev`, `prod`).

Each OU represents a logical environment, and each account within the OU must declare its environment binding — a configuration that determines which Git repository and branch it uses for config and infrastructure.

---

## Steps to Set Up a New Environment

### 1. Create the AWS Organization

If you haven’t already, [create an AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) using the AWS Console.  
This will create the root (management) account and enable centralized control.

---

### 2. Define Organizational Units (OUs)

Create one OU per environment:

- `dev`
- `prod`

Each OU will contain the accounts associated with that environment.

---

### 3. Create Infrastructure Accounts Within Each OU

For each environment, create at least one AWS account to run Terraform deployments and store configuration:

- `dev-iac`
- `prod-iac`

To bootstrap with the minimal setup, you can start with:

- One OU: `prod`
- One account: `prod-iac`

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

Before running the setup scripts, make sure your AWS CLI is configured with a named profile for each target account:

- `AWS_PROFILE=dev-iac`
- `AWS_PROFILE=prod-iac`

See: [Configure AWS CLI Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)

---

### 4. Define the Environment Parameter in Each Account

Each AWS account must declare its environment before any configuration or infrastructure can be deployed.

Run the following from your local machine:

```bash
AWS_PROFILE=dev-iac python scripts/define_account_environment.py --env dev
```

For production:

```bash
AWS_PROFILE=prod-iac python scripts/define_account_environment.py --env prod
```

---

#### What It Does

- Loads the file `account_environments/<env>.json` from your repo
- Writes it to Systems Manager Parameter Store in the active AWS account
- The parameter name defaults to:  
  ```
  /iac/environment
  ```

You can override the prefix using the `--prefix` flag or the `IAC_PREFIX` environment variable:

```bash
IAC_PREFIX=/karma AWS_PROFILE=dev-iac python scripts/define_account_environment.py --env dev
```

Resulting in a parameter like:

```
/karma/environment
```

---

### Confirm the Parameter in AWS

Check in the AWS Console:

> **AWS Systems Manager → Parameter Store → Search for** `/iac/environment` (or your custom prefix)

This parameter is used by all **Adage** components and deployment scripts to determine the current environment context.

---

## Next Steps

If you're following the [AWS Bootstrap Checklist](../bootstrap-checklist.md), continue with:

- [Applying the Security Baseline](../security-baseline/README.md)
- [Defining Tagging and Cost Tracking](../tagging-policy/README.md)
- [Setting up Cost Management](../cost-management/README.md)

---

🔁 Return to [Adage: AWS Deployment Framework](../README.md)
