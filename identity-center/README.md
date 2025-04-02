# Identity Center Setup

This guide explains how to enable AWS IAM Identity Center, create an admin user, assign permissions, and prepare your account for secure, role-based access.

It replaces the legacy approach of creating IAM users directly, and is now the default AWS-recommended method for managing access.

---

## Overview

Identity Center allows you to:

- Use a built-in or external directory for user authentication
- Assign users to accounts using **permission sets**
- Log in to multiple AWS accounts via a central portal
- Eliminate the need for IAM users and long-lived credentials

This is the foundation for all access across your AWS environment.

---

## Steps

### 1. Log in as Root and Enable Identity Center

- Sign in to the [AWS Console](https://console.aws.amazon.com/) as the root user
- Go to **IAM Identity Center** (region: `us-east-1` recommended)
- Click **Enable**

This will create an Identity Center instance tied to your organization.

### 2. Create a User

- Use the built-in directory for now (you can switch to an external identity source later)
- Create a user named `admin` with a valid email address
- Accept the default settings (no groups needed yet)
- The user will receive an email with a temporary password

### 3. Create a Permission Set

- Go to **Permission Sets**
- Click **Create permission set**
- Choose **Custom permissions** or start with AWS-managed **AdministratorAccess**
- Optionally:
  - Set session duration (default: 1 hour)
  - Add tags (e.g. `Environment=mgmt`, `AccessLevel=admin`)
- Save the permission set

### 4. Assign the User to the Account

- Go to **AWS Accounts**
- Select your current account
- Choose **Assign users or groups**
- Assign the `admin` user and attach the permission set

### 5. Log In via the Access Portal

- Visit your organization’s access portal URL (shown in the console)
- Log in as the `admin` user using the emailed credentials
- You should see a tile for the account and role you’ve been assigned

---

## After This

Once you can log in using IAM Identity Center, you’re ready to create additional accounts, roles, and permission sets.

Continue with the next guide:

👉 [Organization Structure](../org-structure/README.md)

---

📚 View all setup guides in the [AWS Deployment Guide](../README.md)
