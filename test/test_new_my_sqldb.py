# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_my_sqldb import NewMySQLDB

class TestNewMySQLDB(unittest.TestCase):
    """NewMySQLDB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewMySQLDB:
        """Test NewMySQLDB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewMySQLDB`
        """
        model = NewMySQLDB()
        if include_optional:
            return NewMySQLDB(
                name = ''
            )
        else:
            return NewMySQLDB(
                name = '',
        )
        """

    def testNewMySQLDB(self):
        """Test NewMySQLDB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
