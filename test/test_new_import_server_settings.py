# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_import_server_settings import NewImportServerSettings

class TestNewImportServerSettings(unittest.TestCase):
    """NewImportServerSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewImportServerSettings:
        """Test NewImportServerSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewImportServerSettings`
        """
        model = NewImportServerSettings()
        if include_optional:
            return NewImportServerSettings(
                allow_partial_sync = True,
                hostname = '',
                friendly_name = '',
                ssh_user = '',
                import_type = 'cPanel',
                auth_kind = 'whmToken',
                auth_user = '',
                auth_pass = '',
                ssh_port = 1.337,
                api_port = 1.337
            )
        else:
            return NewImportServerSettings(
                hostname = '',
                friendly_name = '',
                ssh_user = '',
                import_type = 'cPanel',
                auth_kind = 'whmToken',
                auth_user = '',
                auth_pass = '',
                ssh_port = 1.337,
                api_port = 1.337,
        )
        """

    def testNewImportServerSettings(self):
        """Test NewImportServerSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
