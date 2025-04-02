# Cost Management

This guide helps you set up cost visibility, budget alerts, and tag-based tracking across your AWS accounts.

These steps are designed to work even in a multi-account organization, ensuring that you always have visibility into spending — and can trace costs back to services, projects, or teams.

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

### 2. Set a Monthly Budget

- In the Billing Console, go to **Budgets**
- Click **Create budget**
- Choose **Cost budget**, and set a monthly threshold (e.g., $10)
- Attach an email address to receive alerts

Budgets can be scoped to individual services, accounts, or tag values.

### 3. Enable the `CostAllocationTags` Setting

- Go to **Billing > Cost Allocation Tags**
- Activate any relevant tags (e.g., `Project`, `Environment`, `Owner`)
- Only activated tags will appear in billing reports

### 4. Apply Standard Tags

Make sure your infrastructure (via Terraform) and any manual resources use consistent tags.

Recommended tags:

```hcl
tags = {
  Project     = "networking"
  Environment = "dev"
  Owner       = "yourname"
}
```

These tags allow you to filter costs and usage by team, project, or deployment.

---

## After This

You can now trace AWS costs by:

- Environment (e.g., dev vs. prod)
- Project
- Owner or team

Next:

- [Define your tagging policy](../tagging-policy/README.md)
- [Ensure security and audit logging are in place](../security-baseline/README.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
