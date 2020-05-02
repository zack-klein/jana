import unittest

from unittest.mock import patch

from jana import gcp_secretmanager


class TestJana(unittest.TestCase):
    def setUp(self):
        self.secret_name = "a fake secret"
        self.secret_value = "a fake secret value"
        self.gcp_project = "a fake project"
        self.secret_version = "x"

    @patch("jana.gcp_secretmanager.secretmanager")
    def test_fetch_secret_calls_access_secret_version(self, sm_mock):
        fake_sm = sm_mock.SecretManagerServiceClient()
        gcp_secretmanager.fetch_gcp_secret_manager_secret(
            self.secret_name, self.gcp_project, self.secret_version
        )
        # TODO: Improve to make more precise
        fake_sm.access_secret_version.assert_called_once()

    @patch("jana.gcp_secretmanager.secretmanager")
    def test_put_secret_calls_create_secret_add_version(self, sm_mock):
        fake_sm = sm_mock.SecretManagerServiceClient()
        gcp_secretmanager.put_gcp_secret_manager_secret(
            self.secret_name, self.secret_value, self.gcp_project
        )
        # TODO: Improve to make more precise
        fake_sm.create_secret.assert_called_once()
        fake_sm.add_secret_version.assert_called_once()

    @patch("jana.gcp_secretmanager.secretmanager")
    def test_drop_secret_calls_delete_secret(self, sm_mock):
        fake_sm = sm_mock.SecretManagerServiceClient()
        gcp_secretmanager.drop_gcp_secret_manager_secret(
            self.secret_name, self.gcp_project
        )
        # TODO: Improve to make more precise
        fake_sm.delete_secret.assert_called_once()

    @patch("jana.gcp_secretmanager.secretmanager")
    def test_update_secret_calls_add_secret_version(self, sm_mock):
        fake_sm = sm_mock.SecretManagerServiceClient()
        gcp_secretmanager.update_gcp_secret_manager_secret(
            self.secret_name, self.secret_value, self.gcp_project
        )
        fake_sm.add_secret_version.assert_called_once()
