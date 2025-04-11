# Serverless Static Website Quickstart

This guide walks you through deploying a fully serverless, secure static website using:

- Amazon S3 for hosting HTML/JS assets  
- CloudFront for global CDN delivery  
- Route 53 for DNS and custom domain support  
- ACM for HTTPS certificates  
- IAM roles and tagging policies for security and cost visibility

---

## Before You Begin

If this is your first time working in AWS with this system, start here:

👉 [AWS Bootstrap Checklist](../bootstrap-checklist.md)

That guide walks you through creating a secure AWS account, enabling Identity Center, and setting up access. You’ll need that baseline in place before deploying infrastructure using this model.

---

## Deployment Overview

This is a two-step deployment process:

1. **Push configuration to AWS Parameter Store**  
   Define your static site using the [`aws-config`](https://github.com/tstrall/aws-config) repository, and push the config to Parameter Store.

2. **Deploy infrastructure with Terraform**  
   Run Terraform from the [`aws-iac`](https://github.com/tstrall/aws-iac) repo. It reads the configuration from Parameter Store and builds the required AWS infrastructure.

All infrastructure is driven by config. Nothing gets deployed unless it’s defined in Parameter Store.

---

## Step-by-Step Plan

This Quickstart will eventually include the following components:

### 1. DNS Setup (Route 53)

- If you do not have a DNS domain to use, you can skip this step. Your site will have a AWS generated url.
- Define DNS configuration, based on existing entry [strall-com](https://github.com/tstrall/aws-config/blob/main/iac/prod/route53-zone/strall-com/config.json)

```
cd aws-config/
AWS_PROFILE=dev-iac ./scripts/deploy.sh route53-zone <nickname>

cd aws-iac/
AWS_PROFILE=dev-iac ./scripts/deploy.sh route53-zone <nickname>
```

### 2. Push Configuration to AWS Parameter Store

- See [aws-config](https://github.com/tstrall/aws-config/) Github repo
- Define website configuration, based on existing entry [strall-com](https://github.com/tstrall/aws-config/blob/main/iac/prod/serverless-site/strall-com/config.json)

```
cd aws-config/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site <nickname>
```

### 3. Deploy AWS Infrastructure Using Terraform

- See [aws-iac](https://github.com/tstrall/aws-iac/) Github repo
```
cd aws-iac/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site <nickname>
```

### 4. Deploy Static Website 

- See [strall.com](strall.com) Github repo for a static site example:

```
cd strall.com/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site <nickname>
```

---

## Configuration-Driven Example

A corresponding config entry in `aws-config` might look like:

```json
{
  "site_name": "dev.strall.com",
  "content_bucket_prefix": "strall-com-dev-site",
  "cloudfront_comment": "Static site for strall.com (dev)",
  "index_document": "index.html",
  ...
}
```

This config is pushed to:

```
/aws/serverless-site/strall-com/config
```

And Terraform will write runtime values (e.g., distribution ID, S3 URL) to:

```
/aws/serverless-site/strall-com/runtime
```

---

## Repositories Involved

- [`aws-iac`](https://github.com/tstrall/aws-iac) – Terraform modules (in progress)  
- [`aws-config`](https://github.com/tstrall/aws-config) – JSON-based configuration definitions  

---

## Status

This guide is a high-level overview and placeholder while the supporting Terraform modules are under development.

Once modules are complete, this guide will provide a complete walk-through for deploying your own serverless static site.

---

For more context on the architecture behind this deployment model, see the:

👉 [Core Design Principles](../design-principles/README.md)
