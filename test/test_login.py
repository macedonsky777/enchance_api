# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.login import Login

class TestLogin(unittest.TestCase):
    """Login unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Login:
        """Test Login
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Login`
        """
        model = Login()
        if include_optional:
            return Login(
                id = '',
                email = '',
                name = '',
                color_code = '',
                registered_at = '',
                avatar_path = '',
                password_last_changed_at = '',
                auth_method = 'basic',
                locale = 'af'
            )
        else:
            return Login(
                id = '',
                email = '',
                name = '',
                color_code = '',
                registered_at = '',
                auth_method = 'basic',
                locale = 'af',
        )
        """

    def testLogin(self):
        """Test Login"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
