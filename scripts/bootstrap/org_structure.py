import argparse
import boto3
import json
import logging
import sys
import os
from botocore.exceptions import ClientError

def get_prefix(args):
    return args.prefix or os.getenv("IAC_PREFIX", "/iac")

def ensure_organization(org_client, dry_run):
    try:
        org_client.describe_organization()
        logging.info("Organization already exists.")
    except org_client.exceptions.AWSOrganizationsNotInUseException:
        if dry_run:
            logging.info("[Dry Run] Would create organization with ALL features")
        else:
            org_client.create_organization(FeatureSet="ALL")
            logging.info("Created organization with ALL features")

def get_root_id(org_client):
    roots = org_client.list_roots()
    return roots["Roots"][0]["Id"]

def list_existing_ous(org_client, root_id):
    response = org_client.list_organizational_units_for_parent(ParentId=root_id)
    return {ou["Name"]: ou["Id"] for ou in response["OrganizationalUnits"]}

def create_organizational_units(org_client, root_id, environments, dry_run):
    existing_ous = list_existing_ous(org_client, root_id)
    for entry in environments:
        name = entry["environment"]
        if name in existing_ous:
            logging.info("OU '%s' already exists. Skipping.", name)
        elif dry_run:
            logging.info("[Dry Run] Would create OU '%s' under root '%s'", name, root_id)
        else:
            response = org_client.create_organizational_unit(ParentId=root_id, Name=name)
            logging.info("Created OU '%s': %s", name, response["OrganizationalUnit"]["Id"])

def list_existing_accounts(org_client):
    paginator = org_client.get_paginator("list_accounts")
    account_map = {}
    for page in paginator.paginate():
        for acct in page["Accounts"]:
            account_map[acct["Email"]] = acct["Id"]
    return account_map

def create_accounts(org_client, environments, account_types, dry_run):
    existing_accounts = list_existing_accounts(org_client)
    for env_entry in environments:
        env = env_entry["environment"]
        base_email = env_entry["email"]
        for acct_type in account_types:
            name = f"{env}-{acct_type}"
            email = f"{name}@{base_email.split('@')[-1]}"
            if email in existing_accounts:
                logging.info("Account '%s' with email '%s' already exists. Skipping.", name, email)
                continue
            if dry_run:
                logging.info("[Dry Run] Would create account '%s' with email '%s'", name, email)
            else:
                try:
                    response = org_client.create_account(
                        AccountName=name,
                        Email=email,
                        RoleName="OrganizationAccountAccessRole"
                    )
                    logging.info("Requested creation of account '%s': RequestId=%s", name, response["CreateAccountStatus"]["Id"])
                except ClientError as e:
                    logging.error("Failed to create account '%s': %s", name, e)

def write_environment_param(account_id, environment, dry_run, args):
    role_arn = f"arn:aws:iam::{account_id}:role/OrganizationAccountAccessRole"
    sts = boto3.client("sts")
    try:
        assumed = sts.assume_role(RoleArn=role_arn, RoleSessionName="SetEnvironment")
        creds = assumed["Credentials"]
        ssm = boto3.client(
            "ssm",
            aws_access_key_id=creds["AccessKeyId"],
            aws_secret_access_key=creds["SecretAccessKey"],
            aws_session_token=creds["SessionToken"],
        )
        prefix = get_prefix(args)
        param_name = f"{prefix}/environment"
        if dry_run:
            logging.info("[Dry Run] Would write %s = %s to account %s", param_name, environment, account_id)
        else:
            ssm.put_parameter(
                Name=param_name,
                Value=environment,
                Type="String",
                Overwrite=True
            )
            logging.info("Wrote %s = %s to account %s", param_name, environment, account_id)
    except ClientError as e:
        logging.error("Could not assume role into account %s: %s", account_id, e)

def populate_environment_tags(org_client, environments, account_types, dry_run, args):
    existing_accounts = list_existing_accounts(org_client)
    for env_entry in environments:
        env = env_entry["environment"]
        base_email = env_entry["email"]
        for acct_type in account_types:
            email = f"{env}-{acct_type}@{base_email.split('@')[-1]}"
            if email not in existing_accounts:
                logging.warning("Account with email '%s' not found. Cannot set environment.", email)
                continue
            write_environment_param(existing_accounts[email], env, dry_run, args)

def main():
    parser = argparse.ArgumentParser(
        description="Bootstraps AWS Org and accounts. Use --prefix or set IAC_PREFIX to override default path prefix (/iac)."
    )
    parser.add_argument("--config", required=True, help="Path to JSON config file")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without executing")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    parser.add_argument("--prefix", help="Override IAC prefix (default is IAC_PREFIX env var or '/iac')")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING)

    try:
        with open(args.config, "r") as f:
            config = json.load(f)
    except Exception as e:
        logging.error("Failed to load config file: %s", e)
        sys.exit(1)

    environments = config.get("organizational_units", [])
    account_types = config.get("accounts", [])

    org_client = boto3.client("organizations")

    ensure_organization(org_client, args.dry_run)
    root_id = get_root_id(org_client)
    create_organizational_units(org_client, root_id, environments, args.dry_run)
    create_accounts(org_client, environments, account_types, args.dry_run)
    populate_environment_tags(org_client, environments, account_types, args.dry_run, args)

if __name__ == "__main__":
    main()
