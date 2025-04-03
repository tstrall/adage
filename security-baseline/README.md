# Security Baseline

This guide walks through the essential security services that should be enabled in every AWS account — particularly in production or shared environments.

These services are foundational for visibility, compliance, and incident response across your organization.

---

## ⚠️ Cost Awareness

All of the services recommended on this page **potentially incur cost**, though some may be reasonable under the Free Tier or offer free trials.

- CloudTrail: Free for management events, but S3 storage can cost
- AWS Config: Charged per configuration item recorded
- GuardDuty: Free for 30 days, then per-GB/event
- Security Hub: Free for 30 days, then per rule/finding

We recommend enabling these even in development accounts, but monitoring usage and billing early on.

---

## Why This Matters

Enabling these baseline services allows you to:

- Track who did what, when, and where
- Detect suspicious behavior or unauthorized changes
- Comply with security best practices and audits
- Build a foundation for alerts, forensic investigation, and cost control

---

## Steps

### 1. Enable CloudTrail

CloudTrail records API activity and resource changes in your AWS account.

- ✅ **Cost Note**: One multi-region trail for management events is free for 90 days.  
  Logs stored in S3 may incur storage charges depending on size and retention.

**To enable:**

- Go to **CloudTrail** in the AWS Console
- Choose **"Create trail"**
- Enable a **multi-region trail**
- Store logs in an S3 bucket (you can reuse across accounts)
- (Optional) Enable CloudTrail Insights to detect unusual API usage patterns

---

### 2. Enable AWS Config

AWS Config records the configuration history and compliance state of your AWS resources.

- ⚠️ **Cost Note**: Charged per configuration item recorded, which can grow quickly in large environments.  
  Free Tier covers 7 configuration items per region.

**To enable:**

- Go to **AWS Config**
- Set up a **recording group** (record all resources, all regions)
- Choose an S3 bucket to store snapshots
- (Optional) Set up rules to detect noncompliant resources

➡️ See below for example rules.

---

### 3. Enable GuardDuty

Amazon GuardDuty is a threat detection service that monitors for malicious activity and unauthorized behavior.

- ⚠️ **Cost Note**: Free for 30 days, then charged based on analyzed data volume (CloudTrail, VPC Flow Logs, DNS logs).

**To enable:**

- Go to **GuardDuty**
- Click **"Enable GuardDuty"**
- Leave all default settings enabled

---

### 4. (Optional) Enable Security Hub

Security Hub provides a centralized view of your security posture by aggregating findings from GuardDuty, AWS Config, and other services.

- ⚠️ **Cost Note**: Free for 30 days, then charges based on active security standards and findings.

**To enable:**

- Go to **Security Hub**
- Click **"Enable Security Hub"**
- Choose which standards and integrations to enable (e.g., CIS, AWS Foundational)

---

## Example AWS Config Rules

Once AWS Config is enabled, you can define rules to enforce specific security and tagging requirements.

### Required Tags Rule

This built-in rule checks whether required tags (e.g., `Project`, `Environment`) are present:

```json
{
  "ConfigRuleName": "required-tags",
  "SourceIdentifier": "REQUIRED_TAGS",
  "InputParameters": {
    "tag1Key": "Project",
    "tag2Key": "Environment",
    "tag3Key": "Owner"
  }
}
```

➡️ Supports your [Tagging Policy](../tagging-policy/README.md)

---

### S3 Bucket Encryption Rule

Ensure all S3 buckets have default encryption enabled:

- Rule ID: `S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED`

---

### IAM Password Policy Rule

Require strong password policies in IAM:

- Rule ID: `IAM_PASSWORD_POLICY`

---

## Recommended Order of Operations

If you're working within an AWS Organization:

- Ensure **CloudTrail logs** are stored in a centralized logging bucket (with versioning and access logging enabled)
- Enable these services in the **management account** first
- Use **AWS Config Aggregators** or **GuardDuty Organizations** to collect findings across accounts

---

## Next Steps

Once security monitoring is enabled:

- [Review the Tagging Policy](../tagging-policy/README.md) — Enforce required tags using AWS Config rules
- [Track costs and activate cost allocation tags](../cost-management/README.md) — Ensure you can attribute spend across environments

---

📚 Return to the [AWS Deployment Guide](../README.md)
