# Tagging Policy

A consistent tagging strategy makes it easy to track costs, organize infrastructure, and manage security policies across AWS accounts.

This guide defines the required and recommended tags for all AWS resources deployed through this framework.

---

## Why Tags Matter

Tags allow you to:

- Track costs by project, environment, or owner
- Organize resources across accounts and regions
- Enforce policies or generate reports
- Enable automated cleanup, backup, or monitoring tools

---

## Required Tags

All Terraform modules and manually created resources should use the following standard tags:

| Tag Key     | Description                         | Example        |
|-------------|-------------------------------------|----------------|
| `Project`   | Name of the system or microservice  | `auth-service` |
| `Environment` | Deployment stage or lifecycle      | `dev` / `prod` |
| `Owner`     | Team or person responsible          | `jdoe`         |

These tags must be consistently applied. Additional custom tags are allowed but must not conflict with reserved names.

---

## Recommended Tags

Depending on your setup, you may also include:

- `BillingGroup` – For shared-cost reporting
- `GitRepo` – Link to source code for traceability
- `SupportLevel` – e.g., `critical`, `low`, `ops-only`
- `DataClassification` – e.g., `public`, `internal`, `confidential`

---

## Tag Activation for Cost Reporting

Just adding tags to resources isn’t enough — AWS requires you to **explicitly activate tag keys** for cost and usage reporting.

Here’s how it works:

1. Deploy a resource (e.g., an S3 bucket or VPC) with tags like `Project`, `Environment`, or `Owner`
2. Wait 24–48 hours for AWS to detect those tag keys
3. Go to **Billing > Cost Allocation Tags** in the AWS Console
4. Select the tags and click **“Activate”**

Once activated, these tags will appear in:

- **Cost Explorer**
- **Budgets**
- **CSV usage reports**
- **Athena-based usage queries** (if enabled)

If you skip this step, the tags won’t show up in any billing reports — even if your resources are correctly tagged.

➡️ You can also refer to the [Cost Management Guide](../cost-management/README.md) for a step-by-step walkthrough.

---

## Tag Governance

As your organization grows, consider using:

- **Tag Policies (via AWS Organizations)** – To enforce required keys and accepted values
- **Resource Groups** – To group resources by tag
- **Budgets and alerts scoped to tag values** – For per-project cost monitoring

---

## AWS Bootstrap Checklist Complete

- Return to the [AWS Bootstrap Checklist](../bootstrap-checklist.md)

---

📚 Return to the [AWS Deployment Guide](../README.md)
