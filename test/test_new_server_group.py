# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_server_group import NewServerGroup

class TestNewServerGroup(unittest.TestCase):
    """NewServerGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewServerGroup:
        """Test NewServerGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewServerGroup`
        """
        model = NewServerGroup()
        if include_optional:
            return NewServerGroup(
                name = ''
            )
        else:
            return NewServerGroup(
                name = '',
        )
        """

    def testNewServerGroup(self):
        """Test NewServerGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
