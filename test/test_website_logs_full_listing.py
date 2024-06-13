# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.website_logs_full_listing import WebsiteLogsFullListing

class TestWebsiteLogsFullListing(unittest.TestCase):
    """WebsiteLogsFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsiteLogsFullListing:
        """Test WebsiteLogsFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsiteLogsFullListing`
        """
        model = WebsiteLogsFullListing()
        if include_optional:
            return WebsiteLogsFullListing(
                items = [
                    openapi_client.models.website_log.WebsiteLog(
                        created_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        status = 'ok', 
                        metadata = null, )
                    ]
            )
        else:
            return WebsiteLogsFullListing(
                items = [
                    openapi_client.models.website_log.WebsiteLog(
                        created_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        status = 'ok', 
                        metadata = null, )
                    ],
        )
        """

    def testWebsiteLogsFullListing(self):
        """Test WebsiteLogsFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
