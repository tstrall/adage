# 🔄 Cross-Account Access via IAM Identity Center

This guide explains how to manage **cross-account access** using **IAM Identity Center** in a multi-account AWS Organization (e.g., management, dev, prod). It shows how users log in once and access multiple accounts based on permission sets.

---

## 🎯 Goal

- Allow a single Identity Center user to access multiple AWS accounts (e.g., `dev`, `prod`, `management`)
- Use permission sets to define access levels
- Centralize login via the AWS access portal

---

## 🧠 Key Concepts

| Term                      | Meaning                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| **Management account**    | The root account in your AWS Organization                               |
| **Member account**        | A sub-account like `dev` or `prod` managed under Organizations          |
| **Permission set**        | A reusable access policy attached to a user/group for a specific account |
| **Identity Center portal**| Central login URL for all AWS account access via SSO                    |

---

## 🪜 Step-by-Step Access Setup

### 1. Confirm AWS Organization is Enabled

- Your `dev` and `prod` accounts should be created and organized under OUs
- Identity Center should be enabled in the **management account**

### 2. Assign Users to Member Accounts

1. Go to **IAM Identity Center** → **AWS Accounts**
2. You’ll see all accounts (`management`, `dev`, `prod`)
3. Select each account and click **Assign users or groups**
4. Choose your user (e.g., `admin@example.com`)
5. Attach a **permission set**, e.g.:
   - `AdministratorAccess` for full control
   - `ReadOnlyAccess` for limited access
6. Repeat for each environment as needed

✅ One user, multiple roles across accounts.

---

## 🧭 How Users Access Multiple Accounts

1. Open the Identity Center portal URL (e.g., `https://your-alias.awsapps.com/start`)
2. Log in using your Identity Center credentials
3. You’ll see a **tile for each AWS account** where you have access
4. Each tile shows one or more **permission set roles** (e.g., `AdministratorAccess`, `ReadOnlyAccess`)
5. Click to launch a console session for the desired account/role

---

## 🔄 Role Switching & Session Behavior

- Each permission set appears as a separate role in the portal
- Users can open multiple roles in separate tabs (e.g., dev in one tab, prod in another)
- Session duration is controlled per permission set (default: 1–12 hours)

---

## 🛠️ Programmatic Access (Optional)

To use the AWS CLI or SDKs with Identity Center credentials:

1. Install the latest AWS CLI
2. Run:
```bash
aws configure sso
```
3. Follow prompts to:
   - Enter your SSO start URL
   - Select the account and role (e.g., `dev` → `AdministratorAccess`)
   - Name the profile (e.g., `dev-admin`)

4. Use the profile in CLI commands:
```bash
aws s3 ls --profile dev-admin
```

✅ Programmatic access will use temporary credentials managed by Identity Center.

---

## 🔐 Optional: Additional IAM Roles Within Member Accounts

For more advanced delegation:
- Create IAM roles in `dev` or `prod`
- Allow trusted Identity Center users or roles to assume them
- Useful for break-glass access, CI/CD, or granular control beyond permission sets

---

## ✅ Summary

You now have:
- A centralized login for users to access multiple AWS accounts
- Role-based access managed through Identity Center
- CLI and SDK integration using `aws configure sso`

This model simplifies security, access management, and auditing in a multi-account AWS setup.

**Last Updated:** April 2025

