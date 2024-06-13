# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_subscription import NewSubscription

class TestNewSubscription(unittest.TestCase):
    """NewSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewSubscription:
        """Test NewSubscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewSubscription`
        """
        model = NewSubscription()
        if include_optional:
            return NewSubscription(
                plan_id = 56,
                dedicated_servers = openapi_client.models.subscription_dedicated_servers.SubscriptionDedicatedServers(
                    app_server_id = '', 
                    backup_server_id = '', 
                    db_server_id = '', 
                    email_server_id = '', ),
                friendly_name = ''
            )
        else:
            return NewSubscription(
                plan_id = 56,
        )
        """

    def testNewSubscription(self):
        """Test NewSubscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
