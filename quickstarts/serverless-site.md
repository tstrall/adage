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

👉 [AWS Bootstrap Checklist](../getting-started/bootstrap-checklist.md)

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

- Create or migrate a hosted zone for your domain  
- Define DNS records (e.g., A, CNAME)

### 2. TLS Certificate (ACM)

- Request a public TLS certificate  
- Validate domain ownership via Route 53

### 3. S3 Website Bucket

- Create a versioned S3 bucket  
- Enforce static content access policies (no public upload, no directory listing)

### 4. CloudFront Distribution

- Use CloudFront to serve the S3 content  
- Enforce HTTPS  
- Route traffic through your custom domain

### 5. IAM & Tagging

- Apply standard tags (`Environment`, `Owner`, `CostCenter`, etc.)  
- Grant access using least-privilege IAM roles for human or CI/CD use

### 6. (Optional) CI/CD Pipeline

- Automate upload of static assets to S3  
- Auto-invalidate CloudFront after deployment

---

## Configuration-Driven Example

A corresponding config entry in `aws-config` might look like:

```json
{
  "nickname": "main-site",
  "domain_name": "example.com",
  "hosted_zone_id": "Z123456ABCDEFG",
  "acm_certificate_arn": "arn:aws:acm:...",
  "default_root_object": "index.html"
}
```

This config is pushed to:

```
/aws/serverless-site/main-site/config
```

And Terraform will write runtime values (e.g., distribution ID, S3 URL) to:

```
/aws/serverless-site/main-site/runtime
```

---

## Repositories Involved

- [`aws-iac`](https://github.com/tstrall/aws-iac) – Terraform modules (in progress)  
- [`aws-config`](https://github.com/tstrall/aws-config) – JSON-based configuration definitions  

---

## Status

This guide is a high-level overview and placeholder while the supporting Terraform modules are under development.

Once modules are complete, this guide will provide a complete walk-through for deploying your own serverless static site.
