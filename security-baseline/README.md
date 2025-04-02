# 🛡️ Security Baseline: CloudTrail, GuardDuty & AWS Config

This guide outlines a minimal but strong security baseline for AWS environments. It assumes IAM Identity Center is enabled, and applies equally across single-account and multi-account setups.

---

## 🎯 Goal

- Record all AWS API activity using **CloudTrail**
- Enable threat detection via **Amazon GuardDuty**
- Track resource configuration changes with **AWS Config**
- Store logs in a secure, dedicated S3 bucket (optional but recommended)

---

## 📜 Step 1: Enable CloudTrail (All API Activity)

1. Go to **CloudTrail** in the AWS Console
2. Click **Create trail**
3. Trail type: **Organization trail** (if using AWS Organizations), otherwise create a standard trail
4. Name your trail: `org-cloudtrail` or `default-cloudtrail`
5. Apply trail to: **All Regions** (recommended)
6. Create a new S3 bucket for logs, or use an existing secure logging bucket
7. Enable log file validation (recommended)
8. Finish creation

✅ CloudTrail now records all API events and stores them in the configured S3 bucket.

---

## 🛡️ Step 2: Enable Amazon GuardDuty (Threat Detection)

1. Go to **GuardDuty** in the AWS Console
2. Click **Enable GuardDuty**
3. It will begin monitoring for threats such as:
   - Unusual API calls
   - Access from known malicious IPs
   - Unauthorized data access or exfiltration
4. (Optional) If using AWS Organizations, configure a delegated administrator account

✅ GuardDuty starts analyzing logs and events immediately after activation.

---

## 🔍 Step 3: Enable AWS Config (Resource Tracking)

1. Go to **AWS Config** in the Console
2. Click **Set up AWS Config**
3. Record all resources in **All Regions** (recommended)
4. Create or reuse an S3 bucket to store configuration snapshots
5. Create an IAM role if prompted
6. (Optional) Add rules like:
   - Required tags
   - No unencrypted volumes
   - IAM policy change tracking

✅ AWS Config will now track changes to your resources and evaluate compliance rules.

---

## 🗃️ Optional: Centralized Logging Bucket

In multi-account setups:
- Create a dedicated `log-archive` S3 bucket in the management account
- Set bucket policies to allow CloudTrail logs from all accounts
- Enable **Object Lock** or **S3 versioning** for immutability (optional but recommended)

You can also aggregate GuardDuty and Config findings centrally.

---

## 🔒 Best Practices

- Restrict access to log and config buckets using IAM and bucket policies
- Enable MFA and Identity Center enforcement for all users
- Monitor IAM usage and periodically review unused roles or keys
- Use AWS Organizations and SCPs to prevent dangerous actions (e.g., disabling CloudTrail)

---

## ✅ Summary

You now have:
- Full activity logging via CloudTrail
- Threat detection via GuardDuty
- Resource tracking and compliance checks via AWS Config
- (Optionally) centralized logs for visibility and long-term storage

These services form the backbone of your AWS security posture.

**Last Updated:** April 2025

