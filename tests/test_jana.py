import unittest

import jana

from jana import aws_secretsmanager, gcp_secretmanager


AWS_SECRETS_MANAGER = "aws-secretsmanager"
GCP_SECRET_MANAGER = "gcp-secretmanager"


class TestJana(unittest.TestCase):
    def setUp(self):
        # AWS set up
        self.valid_aws_provider = AWS_SECRETS_MANAGER
        self.invalid_aws_provider = "aws-systemsmanager"

        # GCP set up
        self.valid_gcp_provider = GCP_SECRET_MANAGER
        self.invalid_gcp_provider = "gcp-secretmanagerapi"

        # Test key set up
        self.valid_test_provider = "__unittest__"
        self.invalid_test_provider = "__invalid__"

    def test_dispatchers_mapped_correctly(self):
        """
        Test that each dispatcher dictionary has the expected functions.
        """
        # AWS Secrets manager fetch
        expected = jana.SECRET_FETCH_DISPATCHER.get(AWS_SECRETS_MANAGER)
        actual = aws_secretsmanager.fetch_aws_secrets_manager_secret
        self.assertEqual(expected, actual)

        # GCP Secret Manager fetch
        expected = jana.SECRET_FETCH_DISPATCHER.get(GCP_SECRET_MANAGER)
        actual = gcp_secretmanager.fetch_gcp_secret_manager_secret
        self.assertEqual(expected, actual)

        # AWS Secrets manager put
        expected = jana.SECRET_PUT_DISPATCHER.get(AWS_SECRETS_MANAGER)
        actual = aws_secretsmanager.put_aws_secrets_manager_secret
        self.assertEqual(expected, actual)

        # GCP Secret Manager put
        expected = jana.SECRET_PUT_DISPATCHER.get(GCP_SECRET_MANAGER)
        actual = gcp_secretmanager.put_gcp_secret_manager_secret
        self.assertEqual(expected, actual)

        # AWS Secrets manager drop
        expected = jana.SECRET_DROP_DISPATCHER.get(AWS_SECRETS_MANAGER)
        actual = aws_secretsmanager.drop_aws_secrets_manager_secret
        self.assertEqual(expected, actual)

        # GCP Secret Manager drop
        expected = jana.SECRET_DROP_DISPATCHER.get(GCP_SECRET_MANAGER)
        actual = gcp_secretmanager.drop_gcp_secret_manager_secret
        self.assertEqual(expected, actual)

        # AWS Secrets manager update
        expected = jana.SECRET_UPDATE_DISPATCHER.get(AWS_SECRETS_MANAGER)
        actual = aws_secretsmanager.update_aws_secrets_manager_secret
        self.assertEqual(expected, actual)

        # GCP Secret Manager update
        expected = jana.SECRET_UPDATE_DISPATCHER.get(GCP_SECRET_MANAGER)
        actual = gcp_secretmanager.update_gcp_secret_manager_secret
        self.assertEqual(expected, actual)

    def test_dispatched_functions_raise_and_call(self):
        """
        Test that dispatched functions call the function they're supposed to
        and raise an exception when appropriate.
        """
        # Fetch
        expected = "fetch"
        actual = jana.fetch_secret(self.valid_test_provider)
        self.assertEqual(expected, actual)

        with self.assertRaises(NotImplementedError):
            jana.fetch_secret(self.invalid_test_provider)

        # Put
        expected = "put"
        actual = jana.put_secret(self.valid_test_provider)
        self.assertEqual(expected, actual)

        with self.assertRaises(NotImplementedError):
            jana.put_secret(self.invalid_test_provider)

        # Drop
        expected = "drop"
        actual = jana.drop_secret(self.valid_test_provider)
        self.assertEqual(expected, actual)

        with self.assertRaises(NotImplementedError):
            jana.drop_secret(self.invalid_test_provider)

        # Update
        expected = "update"
        actual = jana.update_secret(self.valid_test_provider)
        self.assertEqual(expected, actual)

        with self.assertRaises(NotImplementedError):
            jana.update_secret(self.invalid_test_provider)
