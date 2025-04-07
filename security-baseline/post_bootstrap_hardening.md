# Post-Bootstrap Hardening Guide

This guide provides recommended security hardening steps **after completing the initial bootstrap** of your AWS Organization and environment configuration.

> These steps are optional for a quickstart but strongly recommended for production or long-term setups.

---

## 🔐 Root Account Lockdown

Each AWS account (e.g. `dev-core`, `prod-core`) has a root user with full permissions. Root access should only be used for account recovery.

### ✅ Actions to Take

- [ ] Enable MFA for the root user in **each** member account.
- [ ] Remove any access keys from the root user (if present).
- [ ] Securely store root credentials in an encrypted password manager.
- [ ] Configure alternate contact information (email, phone) for recovery.

---

## 👤 Delegated Admin Roles

Avoid logging in with root access. Instead, create a cross-account admin role.

### 🔧 Setup Example

1. In each `*-core` account, create a role named:

   ```text
   OrganizationAdmin
   ```

2. Allow the `strall.com` management account to assume it:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::<mgmt-account-id>:root"
         },
         "Action": "sts:AssumeRole",
         "Condition": {}
       }
     ]
   }
   ```

3. Attach `AdministratorAccess` or a custom policy as appropriate.

4. Use the AWS Console or CLI from the management account to assume this role when needed.

---

## 👥 Identity Center Integration

If using AWS IAM Identity Center (recommended), assign permissions to Identity Center users instead of direct IAM users.

### 🎯 Permission Sets to Define

| Name | Permissions | Scope |
|------|-------------|-------|
| `OrgAdmin` | Full access | Management account |
| `EnvAdmin` | Full access | `*-core` accounts |
| `ConfigDeployer` | Scoped to Parameter Store + tagging | Config accounts |

---

## 🧪 Verify Access

Once delegated roles are created and Identity Center is enabled:

- [ ] Sign in via SSO and verify access to each account using the assigned role.
- [ ] Test access to AWS Organizations, SSM Parameter Store, IAM, and CloudTrail where applicable.
- [ ] Rotate credentials for users with legacy access if any remain.

---

## 🛡️ Account Hardening Checklist

| Account     | Root MFA | No Root Keys | Delegated Role | Identity Center Access |
|-------------|----------|---------------|----------------|-------------------------|
| `dev-core`  | [ ]      | [ ]           | [ ]            | [ ]                     |
| `prod-core` | [ ]      | [ ]           | [ ]            | [ ]                     |
| `strall.com` (mgmt) | ✅ | ✅ | ✅ | ✅ |

---

## 📎 Related

- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Enable MFA on AWS Root Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)
- [Delegating Access Across AWS Accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html)

---

## 📘 Notes

- This checklist is intentionally general. You can expand it with custom policies and additional roles specific to your architecture.
- Add automation later via Terraform or AWS CDK for reproducibility.
