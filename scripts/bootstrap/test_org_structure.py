import unittest
from unittest.mock import patch, MagicMock
import org_structure

class TestOrgStructure(unittest.TestCase):

    @patch("org_structure.boto3.client")
    def test_ensure_organization(self, mock_boto_client):
        mock_org = MagicMock()
        mock_boto_client.return_value = mock_org
        # Simulate org already exists
        mock_org.describe_organization.return_value = {"Organization": {"Id": "o-example"}}
        org_structure.ensure_organization(mock_org, dry_run=False)
        mock_org.describe_organization.assert_called_once()

        # Simulate org not in use
        mock_org.describe_organization.side_effect = mock_org.exceptions.AWSOrganizationsNotInUseException({})
        mock_org.create_organization.return_value = {"Organization": {"Id": "o-new"}}
        org_structure.ensure_organization(mock_org, dry_run=True)  # dry-run shouldn't call create

    @patch("org_structure.boto3.client")
    def test_create_organizational_units(self, mock_boto_client):
        mock_org = MagicMock()
        mock_boto_client.return_value = mock_org
        root_id = "r-root"
        mock_org.list_organizational_units_for_parent.return_value = {
            "OrganizationalUnits": [{"Name": "dev", "Id": "ou-dev"}]
        }
        environments = [{"environment": "dev", "email": "dev@example.com"}, {"environment": "prod", "email": "prod@example.com"}]
        org_structure.create_organizational_units(mock_org, root_id, environments, dry_run=True)

    @patch("org_structure.boto3.client")
    def test_create_accounts(self, mock_boto_client):
        mock_org = MagicMock()
        mock_boto_client.return_value = mock_org
        environments = [{"environment": "dev", "email": "dev@example.com"}]
        account_types = ["iac"]
        mock_org.get_paginator.return_value.paginate.return_value = [[{"Email": "dev-iac@example.com", "Id": "123"}]]
        org_structure.create_accounts(mock_org, environments, account_types, dry_run=True)

    @patch("org_structure.boto3.client")
    def test_populate_environment_tags(self, mock_boto_client):
        mock_org = MagicMock()
        mock_sts = MagicMock()
        mock_ssm = MagicMock()
        mock_boto_client.side_effect = lambda service: {
            "organizations": mock_org,
            "sts": mock_sts,
            "ssm": mock_ssm
        }[service]

        mock_org.get_paginator.return_value.paginate.return_value = [[
            {"Email": "dev-iac@example.com", "Id": "123456789012"}
        ]]
        mock_sts.assume_role.return_value = {
            "Credentials": {
                "AccessKeyId": "AKIA...",
                "SecretAccessKey": "secret",
                "SessionToken": "token"
            }
        }

        environments = [{"environment": "dev", "email": "dev@example.com"}]
        account_types = ["iac"]

        org_structure.populate_environment_tags(mock_org, environments, account_types, dry_run=True)

if __name__ == "__main__":
    unittest.main()
