# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.web_server_rewrite import WebServerRewrite

class TestWebServerRewrite(unittest.TestCase):
    """WebServerRewrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebServerRewrite:
        """Test WebServerRewrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebServerRewrite`
        """
        model = WebServerRewrite()
        if include_optional:
            return WebServerRewrite(
                path = '',
                destination_file = ''
            )
        else:
            return WebServerRewrite(
                path = '',
                destination_file = '',
        )
        """

    def testWebServerRewrite(self):
        """Test WebServerRewrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
