# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.crontab_full_listing import CrontabFullListing

class TestCrontabFullListing(unittest.TestCase):
    """CrontabFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CrontabFullListing:
        """Test CrontabFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrontabFullListing`
        """
        model = CrontabFullListing()
        if include_optional:
            return CrontabFullListing(
                items = [
                    null
                    ]
            )
        else:
            return CrontabFullListing(
                items = [
                    null
                    ],
        )
        """

    def testCrontabFullListing(self):
        """Test CrontabFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
