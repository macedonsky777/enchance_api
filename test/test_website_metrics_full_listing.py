# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.website_metrics_full_listing import WebsiteMetricsFullListing

class TestWebsiteMetricsFullListing(unittest.TestCase):
    """WebsiteMetricsFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsiteMetricsFullListing:
        """Test WebsiteMetricsFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsiteMetricsFullListing`
        """
        model = WebsiteMetricsFullListing()
        if include_optional:
            return WebsiteMetricsFullListing(
                items = [
                    openapi_client.models.metrics_entry.MetricsEntry(
                        datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        bytes_received = 1.337, 
                        bytes_sent = 1.337, 
                        unique_hits = 1.337, 
                        bot_hits = 1.337, 
                        total_hits = 1.337, )
                    ]
            )
        else:
            return WebsiteMetricsFullListing(
                items = [
                    openapi_client.models.metrics_entry.MetricsEntry(
                        datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        bytes_received = 1.337, 
                        bytes_sent = 1.337, 
                        unique_hits = 1.337, 
                        bot_hits = 1.337, 
                        total_hits = 1.337, )
                    ],
        )
        """

    def testWebsiteMetricsFullListing(self):
        """Test WebsiteMetricsFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()