# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.licence_api import LicenceApi


class TestLicenceApi(unittest.TestCase):
    """LicenceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LicenceApi()

    def tearDown(self) -> None:
        pass

    def test_get_licence_info(self) -> None:
        """Test case for get_licence_info

        Get current licence status
        """
        pass

    def test_refresh_licence(self) -> None:
        """Test case for refresh_licence

        Updates licence key if provided, and refresh licence status by calling home servers. NOTE: calling without any licence_key body, only refreshes the current licence status
        """
        pass


if __name__ == '__main__':
    unittest.main()
