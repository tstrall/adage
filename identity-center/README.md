# ✅ AWS Identity Center Admin Setup (Root-to-Admin Transition)

This guide documents the secure setup of an AWS account using **IAM Identity Center (formerly AWS SSO)**. It replaces root access with a named admin identity and prepares the account for scalable, secure use—including multi-account and cost visibility support.

---

## 🌟 Goal

- Secure the root user
- Set up a named Identity Center admin user (e.g., `admin@example.com`)
- Use **IAM Identity Center** for modern, centralized identity management
- Prepare for multi-account (`dev`, `prod`) and cost analysis via tagging

---

## 🔐 Step 1: Secure the Root Account

1. Log in to the AWS Console using the root account (e.g., `your-email@example.com`)
2. Go to **My Security Credentials**
3. Enable **Multi-Factor Authentication (MFA)** using a virtual authenticator (e.g., Google Authenticator)
4. Set a strong password
5. Log out of the root account

📅 **Root account is now secured and reserved for emergency or billing access only.**

---

## 🌐 Step 2: Enable IAM Identity Center

1. Log back in to the AWS Console as root
2. Navigate to **IAM Identity Center** (`us-east-1` is the default and recommended region)
3. Click **Enable** to activate Identity Center
4. Accept the default identity source: **"Identity Center directory"**

🚀 IAM Identity Center is now active and ready for user management.

---

## 👤 Step 3: Create Admin User

1. In Identity Center, go to **Users** > **Add user**
2. Set:
   - **Username:** `admin`
   - **Email address:** your actual email
   - (Optional) Add first and last name
3. Skip group assignment if no groups yet created
4. Click **Add user**
5. AWS sends a welcome email with a login link

📅 A secure identity-based admin user is now created.

---

## 🛡️ Step 4: Create Permission Set

1. In Identity Center, go to **AWS Accounts**
2. Select your current account (Management account)
3. Click **Assign users or groups**
4. Choose the newly created user (e.g., `admin`)
5. Click **Create new permission set**
   - Name: `AdministratorAccess`
   - Base it on AWS managed policy: **AdministratorAccess**
   - Session duration: **8 hours**
   - Relay State: **leave blank**
   - Tags:
     - `Owner = admin`
     - `Environment = management`
     - `AccessLevel = admin`
     - `ProvisionedBy = identity-center`
6. Complete the wizard to create and assign the permission set

🚀 The user now has full admin access to the account via Identity Center.

---

## 🚪 Step 5: Log in as Admin

1. Open the Identity Center portal URL:  
   `https://<your-alias>.awsapps.com/start`
2. Login with the credentials emailed to the user
3. Select the AWS account and click the `AdministratorAccess` role

🔍 This opens the AWS Console as the new admin—no root access needed for day-to-day use.

---

## 💺 Optional Next Steps

### 📅 Cost Controls
- Enable **billing alerts** and create a monthly **budget**
- Activate **Cost Explorer**
- Tag resources with consistent `Owner`, `Environment`, `CostCenter` values

### 🔒 Security Enhancements
- Enable **CloudTrail** and send logs to S3
- Turn on **GuardDuty** (free trial, low-cost afterward)
- (Optional) Enable **AWS Config** for resource tracking

### 🏛️ Multi-Account Setup
- Enable **AWS Organizations**
- Create `dev` and `prod` sub-accounts
- Share Identity Center permission sets across all accounts

---

## 📂 Tagging Strategy Example

| Key            | Example Value     | Purpose                           |
|----------------|-------------------|-----------------------------------|
| `Owner`        | `admin`           | Who owns or created the resource  |
| `Environment`  | `management`      | Classify by lifecycle stage       |
| `AccessLevel`  | `admin`           | Useful for identity tracking      |
| `ProvisionedBy`| `identity-center` | Useful for audit and traceability |
| `CostCenter`   | `core` or `1000`  | Supports billing allocation       |

---

## 📅 Summary

You now have:
- MFA-protected root account
- A named admin user using IAM Identity Center
- Full admin access through permission sets
- A secure, scalable, and taggable foundation

**Next up:** Enable AWS Organizations and build out your `dev` and `prod` environments!

---

**Last Updated:** April 2025  

