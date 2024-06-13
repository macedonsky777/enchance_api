# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.logins_api import LoginsApi


class TestLoginsApi(unittest.TestCase):
    """LoginsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoginsApi()

    def tearDown(self) -> None:
        pass

    def test_create_login(self) -> None:
        """Test case for create_login

        Create a new login
        """
        pass

    def test_create_otp_session(self) -> None:
        """Test case for create_otp_session

        Create a new session for login with a one-time-password
        """
        pass

    def test_create_session(self) -> None:
        """Test case for create_session

        Create a new session for login
        """
        pass

    def test_delete_current_session(self) -> None:
        """Test case for delete_current_session

        Delete current session
        """
        pass

    def test_delete_login_avatar(self) -> None:
        """Test case for delete_login_avatar

        Remove login avatar
        """
        pass

    def test_delete_session(self) -> None:
        """Test case for delete_session

        Delete current session
        """
        pass

    def test_delete_sessions(self) -> None:
        """Test case for delete_sessions

        Delete sessions
        """
        pass

    def test_finish_password_recovery(self) -> None:
        """Test case for finish_password_recovery

        Finish a password recovery
        """
        pass

    def test_get_customer_logins(self) -> None:
        """Test case for get_customer_logins

        List customer logins for org
        """
        pass

    def test_get_login(self) -> None:
        """Test case for get_login

        Get login info
        """
        pass

    def test_get_login_memberships(self) -> None:
        """Test case for get_login_memberships

        Get login memberships
        """
        pass

    def test_get_logins(self) -> None:
        """Test case for get_logins

        Query all logins
        """
        pass

    def test_get_org_logins(self) -> None:
        """Test case for get_org_logins

        Query logins belonging to organization
        """
        pass

    def test_get_sessions(self) -> None:
        """Test case for get_sessions

        Get all login sessions
        """
        pass

    def test_resend_pin(self) -> None:
        """Test case for resend_pin

        Resends 2FA sign-in code.
        """
        pass

    def test_set_customer_login_password(self) -> None:
        """Test case for set_customer_login_password

        Set password for login
        """
        pass

    def test_set_login_avatar(self) -> None:
        """Test case for set_login_avatar

        Set login avatar
        """
        pass

    def test_start_password_recovery(self) -> None:
        """Test case for start_password_recovery

        Start a new password recovery for login
        """
        pass

    def test_update_login_info(self) -> None:
        """Test case for update_login_info

        Update login info
        """
        pass

    def test_validate_password_recovery(self) -> None:
        """Test case for validate_password_recovery

        Validate a password recovery secret
        """
        pass

    def test_verify2_fa(self) -> None:
        """Test case for verify2_fa

        Verifies 2FA sign-in code.
        """
        pass


if __name__ == '__main__':
    unittest.main()
