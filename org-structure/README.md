# 🏗️ AWS Organization Structure Setup: dev & prod Sub-Accounts

This guide walks through enabling **AWS Organizations** and creating two sub-accounts: one for `dev` and one for `prod`. It assumes you're already using **IAM Identity Center** with an admin user in your management/root account.

---

## 🎯 Goal

- Enable AWS Organizations (if not already enabled)
- Create two sub-accounts: `dev` and `prod`
- Organize them into Organizational Units (OUs)
- Assign Identity Center users or groups to sub-accounts using permission sets

---

## ✅ Step 1: Enable AWS Organizations

1. Log in as your Identity Center admin (e.g., `admin`) using the AWS access portal
2. Go to the **Organizations** service
3. If prompted, click **Enable AWS Organizations**
4. Choose **Enable All Features** (not consolidated billing only)

✅ You’ve now created an organization. Your current account is the **management account** (a.k.a. root or payer account).

---

## 🧱 Step 2: Create Organizational Units (OUs)

1. In the Organizations console, go to **Organize accounts**
2. Click **Add organizational unit**
   - Name the first one `dev`
   - Repeat to create `prod`

✅ OUs help you group and control accounts more easily.

---

## 🆕 Step 3: Create `dev` and `prod` Member Accounts

1. In Organizations, go to **Accounts** → **Add an AWS account**
2. Choose **Create an AWS account**
3. Fill in:
   - **Account name:** `dev`
   - **Email address:** use something like `yourname+dev@example.com`
   - Leave IAM role name default (e.g., `OrganizationAccountAccessRole`)
4. Repeat for the `prod` account (use `yourname+prod@example.com`)

> ✅ Tip: Gmail and most email systems let you use aliases with `+` to receive all account emails at one inbox.

Each account takes a minute or two to create.

---

## 📦 Step 4: Move Accounts into OUs

1. Once `dev` and `prod` accounts are created, go back to **Organize accounts**
2. Drag `dev` into the `dev` OU, and `prod` into the `prod` OU

✅ You’ve now grouped your accounts logically for future policy management.

---

## 👤 Step 5: Assign Identity Center Access to Sub-Accounts

1. Go to **IAM Identity Center** → **AWS accounts**
2. You’ll now see the new `dev` and `prod` accounts listed
3. Select the `dev` account → click **Assign users or groups**
4. Choose your user (e.g., `admin`) or an Identity Center group
5. Reuse or create a permission set:
   - Name: `AdministratorAccess` or `DeveloperAccess`
   - Base on AWS-managed policy: `AdministratorAccess`
   - Set session duration (e.g., 8 hours)
   - Add tags (`Environment = dev`, etc.)
6. Repeat for the `prod` account

✅ Your Identity Center admin can now access all accounts from the central portal.

---

## 🔁 Optional: Cross-Account Role Access (CLI or Terraform)

If you need programmatic access to `dev`/`prod` accounts (e.g., from CI/CD pipelines or Terraform):

- Use the default `OrganizationAccountAccessRole` for cross-account IAM
- Or create custom IAM roles in each account and allow your Identity Center user to assume them

Let me know if you'd like to scaffold this with Terraform.

---

## 🧩 Optional Next Steps

- Set up **SCPs (Service Control Policies)** to restrict sensitive actions
- Enable **AWS Config, CloudTrail, and GuardDuty** in each account
- Set up **centralized billing and log collection** to the management account
- Define **tag policies** to enforce tagging across accounts

---

## ✅ Summary

You now have:
- A secure AWS Organization with `dev` and `prod` accounts
- Identity Center access provisioned for each environment
- A clean foundation for account-based isolation, access control, and tagging

Use this setup as the backbone of your multi-environment AWS strategy.

**Last Updated:** April 2025

