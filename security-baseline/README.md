# Security Baseline

This guide walks through the essential security services that should be enabled in every AWS account — particularly in production or shared environments.

These services are foundational for visibility, compliance, and incident response across your organization.

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

- Go to **CloudTrail** in the AWS Console
- Choose **"Create trail"**
- Enable a **multi-region trail**
- Store logs in an S3 bucket (you can reuse across accounts)
- (Optional) Enable CloudTrail Insights to detect unusual API usage patterns

---

### 2. Enable AWS Config

AWS Config records the configuration history and compliance state of your AWS resources.

- Go to **AWS Config**
- Set up a **recording group** (record all resources, all regions)
- Choose an S3 bucket to store snapshots
- (Optional) Set up rules to detect noncompliant resources

This helps with drift detection, audit trails, and enforcing tagging or encryption requirements.

➡️ See examples below.

---

### 3. Enable GuardDuty

Amazon GuardDuty is a threat detection service that monitors for malicious activity and unauthorized behavior.

- Go to **GuardDuty**
- Click **"Enable GuardDuty"**
- Leave all default settings enabled

GuardDuty continuously analyzes CloudTrail, VPC Flow Logs, and DNS logs.

---

### 4. (Optional) Enable Security Hub

Security Hub provides a centralized view of your security posture by aggregating findings from:

- GuardDuty
- AWS Config
- IAM Access Analyzer
- Other third-party tools

You can enable it from the **Security Hub** console and choose which services to integrate.

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

This rule helps enforce your [Tagging Policy](../tagging-policy/README.md).

---

### S3 Bucket Encryption Rule

Ensure all S3 buckets have default encryption enabled:

- Use managed rule ID: `S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED`

This can help enforce compliance with security standards like SOC2, HIPAA, or internal policies.

---

### IAM Password Policy Rule

Require strong password policies in IAM:

- Rule ID: `IAM_PASSWORD_POLICY`
- Detects weak or missing account password settings

---

## Recommended Order of Operations

If you're working within an AWS Organization:

- Enable these services in the **management account** first
- Use **AWS Config Aggregators** or **GuardDuty Organizations** to collect findings across accounts
- Ensure **CloudTrail logs** are stored in a centralized logging bucket (with versioning and access logging enabled)

---

## Next Steps

Once security monitoring is enabled:

- [Review the Tagging Policy](../tagging-policy/README.md) — Enforce required tags using AWS Config rules
- [Ensure Identity Center is configured](../identity-center/README.md) — Avoid relying on IAM users for ongoing access
- [Begin deploying infrastructure](../quickstarts/serverless-site.md) — Start applying these practices in real-world projects

---

📚 Return to the [AWS Deployment Guide](../README.md)
