# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_website_app import NewWebsiteApp

class TestNewWebsiteApp(unittest.TestCase):
    """NewWebsiteApp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewWebsiteApp:
        """Test NewWebsiteApp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewWebsiteApp`
        """
        model = NewWebsiteApp()
        if include_optional:
            return NewWebsiteApp(
                app = 'wordpress',
                version = '',
                path = '',
                admin_username = '',
                admin_password = '',
                admin_email = '',
                domain_id = ''
            )
        else:
            return NewWebsiteApp(
                app = 'wordpress',
                admin_username = '',
                admin_password = '',
                admin_email = '',
        )
        """

    def testNewWebsiteApp(self):
        """Test NewWebsiteApp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
