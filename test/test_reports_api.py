# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.reports_api import ReportsApi


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportsApi()

    def tearDown(self) -> None:
        pass

    def test_get_login_policy_blocked_ips(self) -> None:
        """Test case for get_login_policy_blocked_ips

        Get blocked ips
        """
        pass

    def test_get_login_policy_blocked_logins(self) -> None:
        """Test case for get_login_policy_blocked_logins

        Get blocked logins
        """
        pass


if __name__ == '__main__':
    unittest.main()
