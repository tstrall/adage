# Getting Started

Welcome to the Adage deployment framework. This guide walks you through the initial steps needed to prepare your AWS environment for configuration-driven deployments.

---

## Prerequisites

Before proceeding, make sure you have:

- An AWS account with admin access
- [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed
- [Terraform](https://developer.hashicorp.com/terraform/downloads) installed
- `jq` installed for working with JSON on the command line
- Python 3.9+ for running helper scripts

---

## AWS SSO and CLI Profile Setup

You’ll need to configure named profiles in your AWS CLI for authentication.

Follow the guide here:

[AWS CLI Profile Setup →](./setup/aws-cli-profiles.md)

Once set up, you can log in:

```sh
aws sso login --profile management
```

---

## First-Time Account Bootstrapping

Next, set up your AWS Organization, create required accounts, and enable IAM Identity Center.

Follow the steps in:

[Account Bootstrapping →](./org-structure/README.md)

---

## When Things Go Wrong

If something doesn’t work as expected, check the following troubleshooting guide:

[Troubleshooting Common Issues →](./troubleshooting_common_issues.md)

---

Once these steps are complete, you can move on to deploying your first component using one of the Quickstarts.

[Serverless Static Site Quickstart →](./quickstarts/serverless-site.md)

