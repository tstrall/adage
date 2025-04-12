# Getting Started

## First-Time Setup

To prepare an AWS account for use with this framework, follow the 👉 [AWS Bootstrap Checklist](./bootstrap-checklist.md). It walks through:

- Security, identity, and billing setup
- Enabling organizations and account structure
- Required services like CloudTrail, Config, and GuardDuty
- Tagging and cost tracking policies

---

## AWS CLI Profile Setup

All framework scripts expect named AWS CLI profiles to target the correct account (e.g. `dev-iac`, `prod-core`). If you're using AWS SSO (recommended), run:

```bash
aws sso login --profile management
export AWS_PROFILE=dev-iac  # or whichever profile you need
```

Alternatively, pass the profile inline:

```bash
AWS_PROFILE=dev-iac python scripts/deploy_config.py ...
```

For a streamlined experience, you can also:

- Set up the [bash prompt to show your active AWS profile and Git branch](./setup/bash-aws-profile-prompt.md)
- Review the full [AWS CLI profile quickstart](./setup/aws-cli-profiles.md)

These setup steps apply to all repos in the **Adage** framework.

---
