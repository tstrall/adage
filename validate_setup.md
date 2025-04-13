# Validate Your Adage Setup

This checklist helps confirm that your local environment and AWS account are correctly set up before you begin deploying components using the Adage framework.

---

## 1. AWS CLI & SSO Access

✅ Can you authenticate with your management account?
```sh
aws sso login --profile management
```

✅ Can you assume a role into one of your sub-accounts (e.g., `dev-iac`)?
```sh
aws sts get-caller-identity --profile dev-iac
```
Expected output should include:
- Your account ID (e.g., `623155450153`)
- An IAM role like `OrganizationAccountAccessRole`

---

## 2. Terraform & Terragrunt Installed

✅ Check installed versions:
```sh
terraform version
terragrunt --version
```

Recommended:
- Terraform v1.3+
- Terragrunt v0.45.x

---

## 3. File Structure Confirmed

✅ Your `aws-config` repo has a config file like:
```
aws-config/
└── iac/
    └── dev/
        └── serverless-site/
            └── mydemo/
                └── config.json
```

✅ Your `aws-iac` repo has a matching component:
```
aws-iac/
└── components/
    └── serverless-site/
        └── main.tf
```

---

## 4. Config in Parameter Store

✅ Can you fetch the config you deployed?
```sh
aws ssm get-parameter \
  --name "/iac/serverless-site/mydemo/config" \
  --with-decryption \
  --profile dev-iac \
  --output json | jq .
```
This confirms your `deploy.sh` script from `aws-config` succeeded.

---

## 5. Ready to Deploy

✅ Test `aws-iac` with a dry run:
```sh
cd aws-iac/
AWS_PROFILE=dev-iac ./scripts/deploy.sh serverless-site mydemo --plan
```
This confirms that Terraform + Terragrunt can read config and initialize the deployment.

---

If you pass all checks above, you're ready to start deploying real infrastructure.

➡️ [Continue to the Serverless Site Quickstart →](./quickstarts/serverless-site.md)

