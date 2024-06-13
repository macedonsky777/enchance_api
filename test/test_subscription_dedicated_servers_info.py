# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.subscription_dedicated_servers_info import SubscriptionDedicatedServersInfo

class TestSubscriptionDedicatedServersInfo(unittest.TestCase):
    """SubscriptionDedicatedServersInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionDedicatedServersInfo:
        """Test SubscriptionDedicatedServersInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionDedicatedServersInfo`
        """
        model = SubscriptionDedicatedServersInfo()
        if include_optional:
            return SubscriptionDedicatedServersInfo(
                app_server = openapi_client.models.subscription_dedicated_server.SubscriptionDedicatedServer(
                    name = '', 
                    id = '', ),
                backup_server = openapi_client.models.subscription_dedicated_server.SubscriptionDedicatedServer(
                    name = '', 
                    id = '', ),
                db_server = openapi_client.models.subscription_dedicated_server.SubscriptionDedicatedServer(
                    name = '', 
                    id = '', ),
                email_server = openapi_client.models.subscription_dedicated_server.SubscriptionDedicatedServer(
                    name = '', 
                    id = '', )
            )
        else:
            return SubscriptionDedicatedServersInfo(
        )
        """

    def testSubscriptionDedicatedServersInfo(self):
        """Test SubscriptionDedicatedServersInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()