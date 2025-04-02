# Security Baseline

This guide outlines the minimum recommended AWS security services to enable across your organization. These services provide monitoring, auditing, and threat detection — even before deploying any application infrastructure.

---

## Overview

The goal of a security baseline is to:

- Monitor all accounts for suspicious activity
- Ensure changes are auditable
- Establish consistent behavior across environments
- Catch misconfigurations early

---

## Services to Enable

### 1. AWS CloudTrail (Organization-wide)

CloudTrail records all account activity (API calls, console actions, etc.).

- Enable CloudTrail in the management account
- Choose “Apply to all accounts in my organization”
- Store logs in a dedicated S3 bucket with versioning
- Use SSE-S3 or SSE-KMS encryption
- Optionally log to CloudWatch Logs or send alerts via EventBridge

### 2. AWS Config

AWS Config tracks resource configuration changes over time.

- Enable in each account, or at the organization level
- Use an aggregator to centralize visibility
- Store snapshots in S3 for auditing

This helps detect drift, noncompliance, or manual changes.

### 3. Amazon GuardDuty

GuardDuty continuously monitors for unusual or malicious activity.

- Enable GuardDuty in each account
- Choose a delegated administrator (usually the security or management account)
- Centralize findings in one account
- Optionally enable auto-remediation via EventBridge rules

---

## Optional Enhancements

- Enable AWS Security Hub to aggregate findings from Config, GuardDuty, and other tools
- Use AWS Detective to visualize relationships and investigate issues
- Set up SCPs (Service Control Policies) to restrict risky actions in production accounts

---

## After This

Once these services are enabled:

- All account activity is logged and auditable
- Security events are centralized
- You can define remediation workflows

Next:

- [Apply consistent tagging](../tagging-policy/README.md)
- [Start deploying infrastructure](../quickstarts/serverless-site.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
