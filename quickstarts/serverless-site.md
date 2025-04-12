# Serverless Static Website Quickstart

![Serverless Static Website](../img/serverless-site.drawio.png)

This guide walks you through deploying a fully serverless, secure static website using:

- Amazon S3 for hosting HTML/JS assets  
- CloudFront for global CDN delivery  
- Route 53 for DNS and custom domain support  
- ACM for HTTPS certificates  
- IAM roles and tagging policies for security and cost visibility

---

## Before You Begin

If this is your first time working in AWS with this system, start here:

👉 [Getting Started](../GETTING_STARTED.md)

That guide walks you through creating a secure AWS account, enabling Identity Center, and setting up access. You’ll need that baseline in place before deploying infrastructure using this model.

---

## Deployment Overview

This is a two-step deployment process:

1. **Push configuration to AWS Parameter Store**  
   Define your static site using the [`aws-config`](https://github.com/tstrall/aws-config) repository, and push the config to Parameter Store.

2. **Deploy infrastructure with Terraform**  
   Run Terraform from the [`aws-iac`](https://github.com/tstrall/aws-iac) repo. It reads the configuration from Parameter Store and builds the required AWS infrastructure.

All infrastructure is driven by config. Nothing gets deployed unless it’s defined in Parameter Store.

➡️ [See AWS Deployment Strategies »](../deployment/README.md)

---

## Step-by-Step Plan

This Quickstart will eventually include the following components:

### 1. DNS Setup (Route 53)

- **If your domain is already using AWS Route 53 as its name server**, you can skip this step.

- **If you do not have a DNS domain**, you can also skip this step.
  - Your site will still be accessible via an AWS-generated HTTPS URL.
  - Be sure to set `"enable_custom_domain": false` in your config at `aws-config/<ENV>/serverless-site/<NICKNAME>`:

    ```json
    {
      "site_name": "www.mysite.com",
      "enable_custom_domain": false,
      ...
    }
    ```

- **Otherwise**, deploy the [`route53-zone`](https://github.com/tstrall/aws-iac/tree/main/components/route53-zone) component to configure AWS Route 53 as your domain’s DNS name server.
  - Use the existing [`strall-com` config](https://github.com/tstrall/aws-config/blob/main/iac/prod/route53-zone/strall-com/config.json) as a reference.
  - That example includes an `MX` record for forwarding email through [ImprovMX](https://improvmx.com/).
    - **Remove the `MX` record** if you don’t want email forwarding.
    - **Otherwise,** create a free account on [ImprovMX](https://improvmx.com/) to enable email forwarding for your domain.


To deploy:

```sh
cd aws-config/
AWS_PROFILE=dev-iac ./scripts/deploy.sh route53-zone <nickname>
```

```sh
cd aws-iac/
AWS_PROFILE=dev-iac ./scripts/deploy.sh route53-zone <nickname>
```

### 2. Deploy AWS Infrastructure

- See [aws-config](https://github.com/tstrall/aws-config/) Github repo
- Define website configuration, based on existing entry [strall-com](https://github.com/tstrall/aws-config/blob/main/iac/prod/serverless-site/strall-com/config.json)

```
cd aws-config/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site <nickname>
```

```
cd aws-iac/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site <nickname>
```

### 3. Deploy Static Website 

- See [strall.com](strall.com) Github repo for a static site example:

```
cd strall.com/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site <nickname>
```

---

## Repositories Involved

- [`aws-iac`](https://github.com/tstrall/aws-iac) – Terraform modules (in progress)  
- [`aws-config`](https://github.com/tstrall/aws-config) – JSON-based configuration definitions  

---

View all setup guides at [Adage: AWS Deployment Framework](../README.md)
