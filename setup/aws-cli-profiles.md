# AWS CLI Profiles – Quickstart

This project assumes you are using **named AWS CLI profiles** to manage credentials for different AWS accounts.

Each script and tool in the framework supports:

```bash
AWS_PROFILE=dev-iac python <script>.py
```

Or, to avoid repetition:

```bash
export AWS_PROFILE=dev-iac
```

You can use profiles with either **SSO (recommended)** or **access keys**.

---

## Set Up a Profile Using AWS SSO (Recommended)

If you're using AWS IAM Identity Center (SSO):

```bash
aws configure sso --profile management
```

Then authenticate:

```bash
aws sso login --profile management
```

Other profiles (e.g., `dev-iac`, `prod-core`) can assume roles from this one by setting:

```ini
[profile dev-iac]
role_arn = arn:aws:iam::<ACCOUNT_ID>:role/OrganizationAccountAccessRole
source_profile = management
region = us-east-1
```

---

## Helpful AWS Docs

- [Configure Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)
- [Set Up SSO with AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html)

---

## Optional: Add AWS Profile + Git Branch to Bash Prompt

To improve visibility of your current `AWS_PROFILE` and Git branch, source this script in your `.bashrc`:

```bash
source /path/to/setup/bash-aws-profile-prompt.sh
```

The prompt will look like:

```
[iac-dev] ~/workspace/aws-iac (main)>
```

See [`setup/bash-aws-profile-prompt.md`](bash-aws-profile-prompt.md) for full details.
