# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.dedicated_subscription_info import DedicatedSubscriptionInfo

class TestDedicatedSubscriptionInfo(unittest.TestCase):
    """DedicatedSubscriptionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DedicatedSubscriptionInfo:
        """Test DedicatedSubscriptionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DedicatedSubscriptionInfo`
        """
        model = DedicatedSubscriptionInfo()
        if include_optional:
            return DedicatedSubscriptionInfo(
                subscription_id = 1.337,
                customer_org_id = '',
                customer_org_name = ''
            )
        else:
            return DedicatedSubscriptionInfo(
                subscription_id = 1.337,
                customer_org_id = '',
                customer_org_name = '',
        )
        """

    def testDedicatedSubscriptionInfo(self):
        """Test DedicatedSubscriptionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
