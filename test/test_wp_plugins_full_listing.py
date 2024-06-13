# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.wp_plugins_full_listing import WpPluginsFullListing

class TestWpPluginsFullListing(unittest.TestCase):
    """WpPluginsFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WpPluginsFullListing:
        """Test WpPluginsFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WpPluginsFullListing`
        """
        model = WpPluginsFullListing()
        if include_optional:
            return WpPluginsFullListing(
                items = [
                    openapi_client.models.wp_plugin.WpPlugin(
                        name = '', 
                        uri = '', 
                        description = '', 
                        version = '', 
                        update = 'available', 
                        auto_update = 'enabled', 
                        status = 'active', 
                        author = '', )
                    ]
            )
        else:
            return WpPluginsFullListing(
                items = [
                    openapi_client.models.wp_plugin.WpPlugin(
                        name = '', 
                        uri = '', 
                        description = '', 
                        version = '', 
                        update = 'available', 
                        auto_update = 'enabled', 
                        status = 'active', 
                        author = '', )
                    ],
        )
        """

    def testWpPluginsFullListing(self):
        """Test WpPluginsFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()