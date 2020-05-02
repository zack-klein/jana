import unittest

from unittest.mock import patch

import jana

from jana import aws_secretsmanager


class TestJana(unittest.TestCase):
    def setUp(self):
        self.secret_name = "a fake secret"
        self.secret_value = "a fake secret value"

    @patch("jana.aws_secretsmanager.base64")
    @patch("jana.aws_secretsmanager.boto3")
    def test_fetch_secret_calls_get_secret_value(self, boto3_mock, base64_mock):
        fake_sm = boto3_mock.session.Session().client(
            service_name="secretsmanager", region_name="us-west-1"
        )
        aws_secretsmanager.fetch_aws_secrets_manager_secret(
            self.secret_name, region="us-west-1"
        )
        fake_sm.get_secret_value.assert_called_with(SecretId=self.secret_name)

    @patch("jana.aws_secretsmanager.boto3")
    def test_put_secret_calls_create_secret(self, boto3_mock):
        fake_sm = boto3_mock.session.Session().client(
            service_name="secretsmanager", region_name="us-east-1"
        )
        aws_secretsmanager.put_aws_secrets_manager_secret(
            self.secret_name, self.secret_value, foo="bar"
        )
        fake_sm.create_secret.assert_called_with(
            Name=self.secret_name, SecretString=self.secret_value, foo="bar"
        )


    @patch("jana.aws_secretsmanager.boto3")
    def test_drop_secret_calls_delete_secret(self, boto3_mock):
        fake_sm = boto3_mock.session.Session().client(
            service_name="secretsmanager", region_name="us-east-1"
        )
        aws_secretsmanager.drop_aws_secrets_manager_secret(
            self.secret_name, foo="bar"
        )
        fake_sm.delete_secret.assert_called_with(
            SecretId=self.secret_name, foo="bar"
        )

    @patch("jana.aws_secretsmanager.boto3")
    def test_update_secret_calls_update_secret(self, boto3_mock):
        fake_sm = boto3_mock.session.Session().client(
            service_name="secretsmanager", region_name="us-east-1"
        )
        aws_secretsmanager.update_aws_secrets_manager_secret(
            self.secret_name, self.secret_value, foo='bar'
        )
        fake_sm.update_secret.assert_called_with(
            SecretId=self.secret_name, SecretString=self.secret_value, foo="bar"
        )
