# AWS Deployment Guide

## 🧠 Core Design Principles

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

➡️ [View the full explanation »](design-principles/README.md)

---

## 📖 Overview

This repository explains how to implement a **Configuration-Driven AWS Deployment Model**, allowing you to:

- **Build AWS infrastructure once, then deploy dynamically via configuration updates.**
- **Separate infrastructure (IaC), configuration (JSON), and application code (Lambdas).**
- **Resolve dependencies dynamically using AWS Parameter Store, eliminating hardcoded references.**
- **Ensure security and auditability by managing deployments through Git.**

---

## 📂 Repository Structure

This model relies on three coordinated repositories:

1️⃣ **[`aws-iac`](https://github.com/tstrall/aws-iac)** – Terraform-based Infrastructure as Code (VPC, RDS, IAM, etc.)  
2️⃣ **[`aws-config`](https://github.com/tstrall/aws-config)** – JSON-based configuration defining what gets deployed  
3️⃣ **[`aws-lambda`](https://github.com/tstrall/aws-lambda)** – Independently deployed Lambda functions

This repository (**`aws-deployment-guide`**) acts as the documentation and setup guide.

---

## 🔗 Quick Links

- **[IaC Repo: aws-iac](https://github.com/tstrall/aws-iac)** – Terraform modules for AWS infrastructure
- **[Config Repo: aws-config](https://github.com/tstrall/aws-config)** – Deployment configurations in JSON
- **[Lambda Repo: aws-lambda](https://github.com/tstrall/aws-lambda)** – Independently deployed Lambda functions
- **[Core Design Principles](./design-principles/)** – Architectural philosophy

---

## 📚 Implementation Guides

These step-by-step setup guides walk through enabling core functionality:

- 🧑‍💼 [Identity Center Admin Setup](./identity-center/README.md)
- 🏗️ [Organization Structure: dev & prod accounts](./org-structure/README.md)
- 🔄 [Cross-Account Access](./cross-account-access/README.md)
- 💰 [Cost Management: Budgets & Billing Alerts](./cost-management/README.md)
- 🛡️ [Security Baseline: CloudTrail, GuardDuty, Config](./security-baseline/README.md)
- 🏷️ [Tagging Policy: Standards & Enforcement](./tagging-policy/README.md)

---

## 🔧 Getting Started

### 1️⃣ Clone the Repositories
```sh
git clone https://github.com/tstrall/aws-deployment-guide.git
git clone https://github.com/tstrall/aws-iac.git
git clone https://github.com/tstrall/aws-config.git
git clone https://github.com/tstrall/aws-lambda.git
```

### 2️⃣ Deploy the Initial Infrastructure
Ensure the config repo has the necessary entries before applying Terraform:
```sh
cd aws-iac/components/vpc
terraform init
terraform apply -var="nickname=main-vpc"
```

### 3️⃣ Deploy Lambda Services Independently
```sh
cd aws-lambda/user-auth-service
./deploy.sh
```

---

## 🔐 Security & Compliance

- **All deployments are controlled through Git**, ensuring version history and approvals
- **IAM policies can restrict who modifies `/aws/.../config` entries**, ensuring **only authorized changes** get deployed
- **Secrets are stored in AWS Secrets Manager**, keeping sensitive information secure

---

## 🧠 Project Background

This project represents independent work and architectural ideas I’ve developed over the years, some of which originated as conceptual proposals or rejected initiatives in prior roles. The implementations are entirely original, built from scratch outside of any employment context.

---

## 📌 Next Steps

Want to implement this in your AWS environment? Here’s what to do next:

1️⃣ **Fork and customize the repos** to fit your organization’s needs  
2️⃣ **Set up a CI/CD pipeline** to automate syncing config updates to AWS Parameter Store  
3️⃣ **Define IAM policies** to ensure secure access control

📩 **Questions? Reach out or contribute!**  
This is an open-source approach, and improvements are always welcome.

---

📢 **Like this approach? Star the repo and follow for updates!** 🚀

