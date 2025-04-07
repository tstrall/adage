# Identity Center Setup

This guide walks through enabling AWS IAM Identity Center (formerly AWS SSO) and configuring an admin user to securely manage the account.

This setup replaces traditional IAM users with a centralized, secure, and scalable identity model that works across multiple accounts in an organization.

---

## Why Use IAM Identity Center?

IAM Identity Center lets you:

- Create users with secure credentials (no more IAM access keys)
- Assign permission sets across multiple AWS accounts
- Use the AWS access portal for federated login
- Easily separate human access from automated roles

---

## Steps

### 1. Enable IAM Identity Center

- From the AWS Console, go to **IAM Identity Center**
- If prompted, choose a region (usually `us-east-1` or wherever you manage org-wide services)
- Click **“Enable”** to create the Identity Center instance

Once enabled, this becomes your centralized identity and access control plane.

---

### 2. Create an Admin User

- Go to **Users** in the Identity Center console
- Click **Add user**
- Enter a username (e.g., `admin`) and your email address
- Choose whether to auto-generate a password or set one manually

You’ll receive a welcome email (if enabled) with login instructions.

---

### 3. Create a Permission Set

- In the left menu, go to **Permission sets**
- Click **Create permission set**
- Choose **"Use an existing AWS managed policy"**
- Select **AdministratorAccess**

This defines what the user can do after logging in.

---

### 4. Assign Access to the Account

- Go to **AWS Accounts** → select your account
- Click **Assign users or groups**
- Select the new `admin` user
- Select the `AdministratorAccess` permission set

✅ Your user now has admin access to the account via the AWS access portal.

---

### 5. Log in via the Access Portal

- Go to the **Access Portal URL** (shown in the Identity Center dashboard)
  - It looks like: `https://d-abc123.awsapps.com/start`
- Log in with the admin user's email and password
- Choose the account and permission set you want to access

From now on, you can use this portal to manage infrastructure securely — without using the root user.

---

## Next Steps

If you're following the [AWS Bootstrap Checklist](../bootstrap-checklist.md), continue with:

- [Enabling AWS Organizations](../org-structure/README.md) — Set up organizational units and member accounts
- [Applying the Security Baseline](../security-baseline/README.md) — Enable CloudTrail, GuardDuty, and more
- [Defining Tagging and Cost Tracking](../tagging-policy/README.md) and [Cost Management](../cost-management/README.md)

---

📚 Return to the [AWS Deployment Guide](../README.md)
