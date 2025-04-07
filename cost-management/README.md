# Cost Management

This guide helps you set up cost visibility, budget alerts, and tag-based tracking across your AWS accounts.

These steps are designed to work even in a multi-account organization, ensuring that you always have visibility into spending — and can trace costs back to services, projects, or teams.

---

## ⚠️ Cost Awareness

All of the services in this guide are free to enable, but a few actions may generate cost:

- **Budgets**: Creating multiple budgets per account may incur charges beyond the first (which is free).

➡️ Set a budget early and use lightweight resources when testing.

---

## Overview

Good cost management practices help you:

- Avoid surprise bills
- Set monthly budget alerts
- Attribute costs using standardized tags
- Enable cost-aware decision-making at every level

---

## Steps

### 1. Enable Cost Explorer

- Go to the [Billing Console](https://console.aws.amazon.com/billing/)
- Click **Cost Explorer**
- Enable the service (this may take a few hours to become fully active)

This provides visual breakdowns of costs over time.

---

### 2. Set a Monthly Budget

- In the Billing Console, go to **Budgets**
- Click **Create budget**
- Choose **Cost budget**, and set a monthly threshold (e.g., $10)
- Attach an email address to receive alerts

Budgets can be scoped to individual services, accounts, or tag values.

⚠️ **Note**: The first budget per account is free. Additional budgets may incur a small charge.

---

### 3. Activate Cost Allocation Tags

- Go to **Billing > Cost Allocation Tags**

When you first visit this page in a new AWS account, both **User-defined tags** and **AWS-generated tags** may appear empty.  
That’s expected — AWS only shows tag keys that have already been used on a deployed resource.

**To trigger tags to appear:**

1. Deploy a resource (e.g., VPC, S3) with tags like `Project`, `Environment`, or `Owner`
2. Wait 24–48 hours for AWS to detect them
3. Return to **Cost Allocation Tags**
4. Select the tag keys that now appear and click **"Activate"**

Only activated tags will be available in:

- Cost Explorer
- Budgets
- Usage reports and CSV exports

➡️ See the [Tagging Policy Guide](../tagging-policy/README.md) for recommended tags and naming conventions.

---

### 4. Apply Standard Tags

Make sure your infrastructure (via Terraform) and any manually created resources use consistent, approved tags.

Recommended tags:

```hcl
tags = {
  Project     = "networking"
  Environment = "dev"
  Owner       = "yourname"
}
```

These tags allow you to filter costs and usage by team, project, or deployment.

➡️ Review the full [Tagging Policy](../tagging-policy/README.md) for guidelines on required tags, reserved names, and governance practices.

---

## After This

You can now trace AWS costs by:

- Environment (e.g., dev vs. prod)
- Project
- Owner or team

---

## Next Steps

If you're following the [AWS Bootstrap Checklist](../bootstrap-checklist.md), continue with:

- [Identity Center Setup](../identity-center/README.md)
- [Organization Structure](../org-structure/README.md)
- [Security Baseline](../security-baseline/README.md)
- [Tagging Policy](../tagging-policy/README.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
