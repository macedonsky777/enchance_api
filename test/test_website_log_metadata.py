# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.website_log_metadata import WebsiteLogMetadata

class TestWebsiteLogMetadata(unittest.TestCase):
    """WebsiteLogMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsiteLogMetadata:
        """Test WebsiteLogMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsiteLogMetadata`
        """
        model = WebsiteLogMetadata()
        if include_optional:
            return WebsiteLogMetadata(
                request_time_ms = 56,
                status_code = 56,
                body = ''
            )
        else:
            return WebsiteLogMetadata(
                request_time_ms = 56,
                status_code = 56,
                body = '',
        )
        """

    def testWebsiteLogMetadata(self):
        """Test WebsiteLogMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
