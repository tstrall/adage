# AWS Deployment Guide

## Core Design Principles

This project is guided by a fabric of interwoven ideas that enable scalable, secure, and flexible AWS infrastructure.

Each principle supports the others, forming a composable system where infrastructure, configuration, and services can evolve independently — yet always remain connected.

These principles include:

- **Build Once, Deploy Anywhere** – Reusable Terraform components across all environments.
- **Configuration Is the Source of Truth** – Git-controlled configs drive every deployment.
- **Immutable Infrastructure** – Replace rather than patch, enabling reliable rollouts.
- **Dynamic Dependency Resolution** – Services discover dependencies at runtime via nicknames.
- **Separation of Concerns** – Infra, config, and app code live in independent repos.
- **External System Referencing** – Reference systems you didn’t create as first-class citizens.
- **Git as the Gatekeeper** – Only what’s defined in Git gets deployed.
- **Optional Smart Caching** – Runtime refresh logic when failures occur.
- **LocalStack-Friendly by Default** – Develop and test locally with minimal cost.

➡️ [View the full explanation](./design-principles/README.md)

---

## First-Time Setup?

Start here if you're creating a brand new AWS account or setting up Identity Center for the first time:

👉 [AWS Bootstrap Checklist](./getting-started/bootstrap-checklist.md)

---

## Quickstart: Build a Serverless Static Website

Once your AWS account is bootstrapped and Identity Center is set up, follow this quickstart to explore the process of deploying a serverless static site using CloudFront and S3:

👉 [Serverless Static Website Quickstart](./quickstarts/serverless-site.md)

This guide explains the configuration-driven approach and planned Terraform modules required to deploy your own secure, static website.

---

## Overview

This repository explains how to implement a **Configuration-Driven AWS Deployment Model**, allowing you to:

- Build AWS infrastructure once, then deploy dynamically via configuration updates.
- Separate infrastructure (IaC), configuration (JSON), and application code (Lambdas).
- Resolve dependencies dynamically using AWS Parameter Store, eliminating hardcoded references.
- Ensure security and auditability by managing deployments through Git.

---

## How the Repositories Work Together

This model requires **three Git repositories** that interact to create a fully managed AWS environment:

- [`aws-iac`](https://github.com/tstrall/aws-iac) – Terraform-based Infrastructure as Code (VPC, RDS, IAM, etc.)
- [`aws-config`](https://github.com/tstrall/aws-config) – JSON-based configuration defining what gets deployed
- [`aws-lambda`](https://github.com/tstrall/aws-lambda) – Independent Lambda functions that dynamically resolve dependencies

This repository (**aws-deployment-guide**) serves as the **documentation hub**, providing a step-by-step guide for using these repos together.

---

## Implementation Guides

These guides walk through setup and configuration for each critical part of the system:

- [Identity Center Admin Setup](./identity-center/README.md)
- [Organization Structure: dev & prod accounts](./org-structure/README.md)
- [Cross-Account Access](./cross-account-access/README.md)
- [Cost Management: Budgets & Billing Alerts](./cost-management/README.md)
- [Security Baseline: CloudTrail, GuardDuty, Config](./security-baseline/README.md)
- [Tagging Policy: Standards & Enforcement](./tagging-policy/README.md)

---

## Setting Up

This project follows a **configuration-driven deployment model**. Terraform only deploys what is defined in AWS Parameter Store.

### Step 1: Clone the Repositories

```bash
git clone https://github.com/tstrall/aws-iac.git
git clone https://github.com/tstrall/aws-config.git
git clone https://github.com/tstrall/aws-lambda.git
```

### Step 2: Define and Push Configuration

Use the `aws-config` repo to define what infrastructure or services you want to deploy.  
Then push those configuration entries to AWS Parameter Store using your CI/CD workflow or a helper script.

Each configuration entry is tied to a **nickname** (like `main`), which identifies a specific instance of a component.

For example, to deploy a VPC nicknamed `main`, define a config like:

```json
{
  "cidr_block": "10.0.0.0/16",
  "enable_dns_support": true,
  "enable_dns_hostnames": true
}
```

Push it to Parameter Store under:

```
/aws/vpc/main/config
```

Terraform will read this config and deploy the `vpc` module accordingly.

---

### Step 3: Deploy with Terraform

Each Terraform component is **nickname-driven**.  
The nickname determines which configuration entry is read from Parameter Store.

To deploy the `vpc` component using the config at `/aws/vpc/main/config`:

```bash
cd aws-iac/components/vpc
terraform init
terraform apply -var="nickname=main"
```

Terraform will:

- Read the config from `/aws/vpc/main/config`
- Deploy the infrastructure
- Write outputs to `/aws/vpc/main/runtime`

---

## Security & Compliance

- All deployments are controlled through Git, ensuring version history and approvals
- IAM policies can restrict who modifies `/aws/.../config` entries, enabling secure delegation
- Secrets are stored in AWS Secrets Manager, keeping sensitive information secure

---

## Project Background

This project represents independent work and architectural ideas developed over years of hands-on AWS experience. The implementations are original and designed for clarity, repeatability, and low friction in multi-account AWS environments.

---

## Next Steps

Want to implement this in your AWS environment?

- Fork and customize the repos to fit your organization’s needs
- Set up a CI/CD pipeline to sync config with Parameter Store
- Define IAM policies and tagging standards to enforce structure and visibility

---

Questions or ideas? Open an issue or submit a pull request.  
Like this approach? Star the repo and follow for updates!
