# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsApi()

    def tearDown(self) -> None:
        pass

    def test_add_orchd_login_policy_email_blacklist(self) -> None:
        """Test case for add_orchd_login_policy_email_blacklist

        Set the orchd login policy email blacklist as a whole
        """
        pass

    def test_add_orchd_login_policy_email_whitelist(self) -> None:
        """Test case for add_orchd_login_policy_email_whitelist

        Set the orchd login policy email whitelist as a whole
        """
        pass

    def test_add_orchd_login_policy_ip_blacklist(self) -> None:
        """Test case for add_orchd_login_policy_ip_blacklist

        Set the orchd login policy ip blacklist as a whole
        """
        pass

    def test_add_orchd_login_policy_ip_whitelist(self) -> None:
        """Test case for add_orchd_login_policy_ip_whitelist

        Set the orchd login policy ip whitelist as a whole
        """
        pass

    def test_add_orchd_login_policy_settings(self) -> None:
        """Test case for add_orchd_login_policy_settings

        Set a single orchd login policy setting
        """
        pass

    def test_create_backup_remote_storage_s3(self) -> None:
        """Test case for create_backup_remote_storage_s3

        Create S3 object storage settings at platform level.
        """
        pass

    def test_create_settings(self) -> None:
        """Test case for create_settings

        Create settings
        """
        pass

    def test_delete_backup_remote_storage_s3(self) -> None:
        """Test case for delete_backup_remote_storage_s3

        Delete S3 object storage settings at platform level.
        """
        pass

    def test_delete_global_service_setting(self) -> None:
        """Test case for delete_global_service_setting

        Delete a single global service setting
        """
        pass

    def test_delete_orchd_login_policy_email_blacklist(self) -> None:
        """Test case for delete_orchd_login_policy_email_blacklist

        Delete an orchd login policy email blacklist
        """
        pass

    def test_delete_orchd_login_policy_email_whitelist(self) -> None:
        """Test case for delete_orchd_login_policy_email_whitelist

        Delete an orchd login policy email whitelist
        """
        pass

    def test_delete_orchd_login_policy_ip_blacklist(self) -> None:
        """Test case for delete_orchd_login_policy_ip_blacklist

        Delete an orchd login policy ip blacklist
        """
        pass

    def test_delete_orchd_login_policy_ip_whitelist(self) -> None:
        """Test case for delete_orchd_login_policy_ip_whitelist

        Delete an orchd login policy ip whitelist
        """
        pass

    def test_delete_setting(self) -> None:
        """Test case for delete_setting

        Remove the specified setting
        """
        pass

    def test_get_backup_remote_storage_s3(self) -> None:
        """Test case for get_backup_remote_storage_s3

        Get S3 object storage settings at platform level.
        """
        pass

    def test_get_demo_mode(self) -> None:
        """Test case for get_demo_mode

        Get the demo mode status of the orchd service
        """
        pass

    def test_get_docker_registry(self) -> None:
        """Test case for get_docker_registry

        Gets the Docker registry credentials.
        """
        pass

    def test_get_global_service_setting(self) -> None:
        """Test case for get_global_service_setting

        Get the value for a particular global service setting
        """
        pass

    def test_get_orchd_log_settings(self) -> None:
        """Test case for get_orchd_log_settings

        Get the orchd log settings
        """
        pass

    def test_get_orchd_login_policy_email_blacklist(self) -> None:
        """Test case for get_orchd_login_policy_email_blacklist

        Get the orchd login policy email blacklist
        """
        pass

    def test_get_orchd_login_policy_email_whitelist(self) -> None:
        """Test case for get_orchd_login_policy_email_whitelist

        Get the orchd login policy email whitelist
        """
        pass

    def test_get_orchd_login_policy_ip_blacklist(self) -> None:
        """Test case for get_orchd_login_policy_ip_blacklist

        Get the orchd login policy ip blacklist
        """
        pass

    def test_get_orchd_login_policy_ip_whitelist(self) -> None:
        """Test case for get_orchd_login_policy_ip_whitelist

        Get the orchd login policy ip whitelist
        """
        pass

    def test_get_orchd_login_policy_settings(self) -> None:
        """Test case for get_orchd_login_policy_settings

        Get the orchd login policy settings
        """
        pass

    def test_get_prohibited_domains(self) -> None:
        """Test case for get_prohibited_domains

        Get the platform level prohibited domains as a newline separated list
        """
        pass

    def test_get_setting(self) -> None:
        """Test case for get_setting

        Get the specified setting
        """
        pass

    def test_get_settings(self) -> None:
        """Test case for get_settings

        Get all current settings
        """
        pass

    def test_set_docker_registry(self) -> None:
        """Test case for set_docker_registry

        Updates the Docker registry credentials.
        """
        pass

    def test_set_global_service_setting(self) -> None:
        """Test case for set_global_service_setting

        Set a single global service setting
        """
        pass

    def test_set_orchd_log_settings(self) -> None:
        """Test case for set_orchd_log_settings

        Set the orchd log settings
        """
        pass

    def test_set_prohibited_domains(self) -> None:
        """Test case for set_prohibited_domains

        Set the platform level prohibited domains
        """
        pass

    def test_update_backup_remote_storage_s3(self) -> None:
        """Test case for update_backup_remote_storage_s3

        Update S3 object storage settings at platform level.
        """
        pass

    def test_update_setting(self) -> None:
        """Test case for update_setting

        Create or update the specified setting
        """
        pass


if __name__ == '__main__':
    unittest.main()
