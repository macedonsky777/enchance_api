# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.server_groups import ServerGroups

class TestServerGroups(unittest.TestCase):
    """ServerGroups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerGroups:
        """Test ServerGroups
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerGroups`
        """
        model = ServerGroups()
        if include_optional:
            return ServerGroups(
                items = [
                    openapi_client.models.server_group.ServerGroup(
                        id = '', 
                        name = '', 
                        server_count = 1.337, 
                        created_at = '', )
                    ]
            )
        else:
            return ServerGroups(
        )
        """

    def testServerGroups(self):
        """Test ServerGroups"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
