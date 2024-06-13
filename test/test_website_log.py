# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.website_log import WebsiteLog

class TestWebsiteLog(unittest.TestCase):
    """WebsiteLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsiteLog:
        """Test WebsiteLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsiteLog`
        """
        model = WebsiteLog()
        if include_optional:
            return WebsiteLog(
                created_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                status = 'ok',
                metadata = None
            )
        else:
            return WebsiteLog(
                created_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                status = 'ok',
        )
        """

    def testWebsiteLog(self):
        """Test WebsiteLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
