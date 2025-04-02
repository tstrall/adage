# Tagging Policy

This guide defines how to use consistent tagging across AWS resources to enable cost allocation, security visibility, and team accountability.

Tagging is critical for managing large-scale environments — and becomes even more powerful when enforced through infrastructure and policies.

---

## Overview

Standardized tags help you:

- Attribute AWS costs by project, environment, or team
- Search and filter resources in the console
- Identify ownership for operational issues
- Enforce compliance through automation

---

## Recommended Tags

Apply these tags consistently to **all AWS resources** — whether created manually or through Terraform:

| Tag Key      | Description                         | Example        |
|--------------|-------------------------------------|----------------|
| `Project`    | The name of the project or service  | `networking`   |
| `Environment`| Deployment stage                    | `dev`, `prod`  |
| `Owner`      | Person or team responsible          | `alice`        |
| `CostCenter` | Billing code (if applicable)        | `1234-app-team`|

---

## Enforcing Tags in Terraform

Use the `tags` block in every resource, or define them in your module:

```hcl
tags = {
  Project     = "networking"
  Environment = "dev"
  Owner       = "alice"
}
```

You can also use a shared tagging module or locals block to enforce consistency across modules.

---

## Organizational Tag Policies (Optional)

If your organization has tagging enforcement enabled:

- Go to **AWS Organizations > Tag Policies**
- Create a tag policy that defines required tags and allowed values
- Attach it to the root or specific Organizational Units (OUs)

This lets you block resources that don’t meet your tag standards.

---

## After This

Once tagging is standardized:

- You can filter costs in Cost Explorer by tag
- IAM policies can be scoped by tags
- Resource cleanup and ownership tracking becomes easier

Next:

- [Review cost visibility setup](../cost-management/README.md)
- [Deploy your first tagged infrastructure](../quickstarts/serverless-site.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
