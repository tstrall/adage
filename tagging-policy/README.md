# 🏷️ Tagging Policy: Standards, Governance & Enforcement

This document outlines the recommended tagging standards and strategies to support cost tracking, security, governance, and automation across your AWS environment.

---

## 🎯 Goal

- Define a consistent tagging schema
- Enable tag-based cost allocation and filtering
- Support audits, access control, and automation
- (Optional) Enforce tag usage using Tag Policies or Config rules

---

## 🏷️ Recommended Standard Tags

| Key            | Purpose                                | Example Value           |
|----------------|-----------------------------------------|--------------------------|
| `Owner`        | Responsible user/team                  | `admin`, `data-team`     |
| `Environment`  | Lifecycle context                      | `dev`, `prod`, `mgmt`    |
| `Project`      | Business or technical project grouping | `strall-com`, `infra`    |
| `CostCenter`   | For billing and chargeback             | `1000`, `ops`, `core`    |
| `AccessLevel`  | Helps identify roles or permissions    | `read`, `admin`, `ci`    |
| `ProvisionedBy`| Tool or method that created resource   | `terraform`, `console`   |
| `CreatedDate`  | Optional for lifecycle tracking        | `2025-04-02`             |

---

## ✅ Tagging Best Practices

- Use **consistent key names and casing** (e.g., `Environment`, not `environment`)
- Apply tags **automatically** wherever possible (e.g., via Terraform, CDK, or IaC wrappers)
- Tag **all taggable resources**, including:
  - EC2, S3, RDS, Lambda, IAM Roles, Security Groups
  - Budgets, dashboards, VPCs, Parameter Store entries, etc.
- Use **Cost Allocation Tags** in the Billing Console to include selected tags in billing reports

---

## 📊 Enable Cost Allocation Tags

1. Go to **Billing** → **Cost Allocation Tags**
2. Check the box for each tag you want to track (e.g., `Environment`, `Project`, `CostCenter`)
3. Click **Activate**

These tags will appear in Cost Explorer within 24 hours.

---

## 🚨 Optional Enforcement: Tag Policies

To prevent tag drift and enforce standards across accounts, use AWS Organizations **Tag Policies**.

1. Go to **Organizations** → **Tag Policies**
2. Create a policy like:
```json
{
  "tags": {
    "Environment": {
      "tag_key": {
        "@@assign": ["dev", "prod", "mgmt"]
      }
    },
    "Owner": {
      "tag_key": {
        "@@assign": []  // Require but don’t restrict values
      }
    }
  }
}
```
3. Apply the policy to your `dev`, `prod`, or root OU

Tag Policies only work on **supported resource types** and don’t retroactively apply to untagged resources.

---

## 📜 Optional Enforcement: AWS Config Rules

Use AWS Config to detect (but not block) noncompliant resources.

Examples:
- `required-tags`
- `restricted-tag-values`

These can alert you via SNS or appear in Config dashboards.

---

## 🛠️ Tag Automation Ideas

- Use Terraform modules with required `tags = { ... }`
- Create wrapper scripts to enforce tagging via IaC
- Add CI/CD checks for tagging compliance
- Use event-based Lambda triggers to flag or auto-tag missing metadata

---

## ✅ Summary

You now have:
- A baseline tagging schema
- Tag governance tools via Cost Allocation Tags, Tag Policies, and AWS Config
- Strategies for consistent, automated tagging across environments

Consistent tagging is essential for secure, cost-effective, and well-governed AWS operations.

**Last Updated:** April 2025

