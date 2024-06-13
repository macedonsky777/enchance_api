# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.settings_full_listing import SettingsFullListing

class TestSettingsFullListing(unittest.TestCase):
    """SettingsFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingsFullListing:
        """Test SettingsFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingsFullListing`
        """
        model = SettingsFullListing()
        if include_optional:
            return SettingsFullListing(
                items = [
                    openapi_client.models.setting.Setting(
                        name = '', 
                        value = null, )
                    ]
            )
        else:
            return SettingsFullListing(
                items = [
                    openapi_client.models.setting.Setting(
                        name = '', 
                        value = null, )
                    ],
        )
        """

    def testSettingsFullListing(self):
        """Test SettingsFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
