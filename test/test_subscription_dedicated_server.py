# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.subscription_dedicated_server import SubscriptionDedicatedServer

class TestSubscriptionDedicatedServer(unittest.TestCase):
    """SubscriptionDedicatedServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionDedicatedServer:
        """Test SubscriptionDedicatedServer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionDedicatedServer`
        """
        model = SubscriptionDedicatedServer()
        if include_optional:
            return SubscriptionDedicatedServer(
                name = '',
                id = ''
            )
        else:
            return SubscriptionDedicatedServer(
                name = '',
                id = '',
        )
        """

    def testSubscriptionDedicatedServer(self):
        """Test SubscriptionDedicatedServer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
