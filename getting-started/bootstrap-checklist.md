# AWS Bootstrap Checklist (For First-Time Setup)

> 🎯 Goal: Set up a **secure, taggable, and automation-ready AWS account**  
> 🧠 This is the minimum manual setup required before you start automating with Terraform.

---

## ✅ Step 1: Create and Secure the Root Account

- [ ] Go to [aws.amazon.com](https://aws.amazon.com) and **sign up for a new account**
- [ ] Set a strong password
- [ ] Set a **support email you control**
- [ ] **Enable MFA** on the root account
- [ ] Set up **billing alerts** and **budgets** (see [Cost Management](../cost-management/README.md))
- [ ] (Optional) Enable **Free Tier usage alerts**

---

## ✅ Step 2: Enable IAM Identity Center

- [ ] Go to the **IAM Identity Center** service (default region: `us-east-1`)
- [ ] Click **Enable**
- [ ] Accept the default identity source (built-in directory)
- [ ] Create a user:
  - Username: `admin`
  - Email: your email
- [ ] Wait for the email and set a password

📌 This lays the foundation for all access going forward.  
➡️ [Follow full setup »](../identity-center/README.md)

---

## ✅ Step 3: Create a Permission Set

- [ ] Assign the new admin user to your current account
- [ ] Create a permission set:
  - Name: `AdministratorAccess`
  - Policy: AWS-managed `AdministratorAccess`
  - Duration: 8 hours
  - Tags: `Environment=mgmt`, `AccessLevel=admin`

✅ After this, you can now log in as your named admin using the AWS SSO portal.  
➡️ [Assign and manage access »](../cross-account-access/README.md)

---

## ✅ Step 4: Log In as Your Admin

- [ ] Visit your Identity Center portal URL (from the welcome email or Identity Center console)
- [ ] Log in as your named user
- [ ] You should now see a tile for the management account with an `AdministratorAccess` role

---

## ✅ Step 5: Recommended Next Steps

| Task | Why It Helps | Guide |
|------|--------------|-------|
| Enable AWS Organizations | Create `dev`/`prod` sub-accounts | [Org Structure](../org-structure/README.md) |
| Turn on GuardDuty, CloudTrail, Config | Security visibility and logging | [Security Baseline](../security-baseline/README.md) |
| Create a tagging policy | Enforce best practices and cost allocation | [Tagging Policy](../tagging-policy/README.md) |
| Set up budgets and alerts | Stay within Free Tier or limits | [Cost Management](../cost-management/README.md) |

---

## 📌 After This

Once the manual steps above are done, you’re ready to:

- Clone and use the [Infrastructure as Code repo (aws-iac)](https://github.com/tstrall/aws-iac)
- Start defining environments and components via [aws-config](https://github.com/tstrall/aws-config)
- Deploy independently managed services from [aws-lambda](https://github.com/tstrall/aws-lambda)

---

**Last Updated:** April 2025

