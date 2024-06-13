# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.login2_fa_remember_me import Login2FARememberMe

class TestLogin2FARememberMe(unittest.TestCase):
    """Login2FARememberMe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Login2FARememberMe:
        """Test Login2FARememberMe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Login2FARememberMe`
        """
        model = Login2FARememberMe()
        if include_optional:
            return Login2FARememberMe(
                device_id = '',
                ttl = 56
            )
        else:
            return Login2FARememberMe(
                device_id = '',
                ttl = 56,
        )
        """

    def testLogin2FARememberMe(self):
        """Test Login2FARememberMe"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
