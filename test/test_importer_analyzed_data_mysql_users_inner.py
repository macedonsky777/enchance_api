# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.importer_analyzed_data_mysql_users_inner import ImporterAnalyzedDataMysqlUsersInner

class TestImporterAnalyzedDataMysqlUsersInner(unittest.TestCase):
    """ImporterAnalyzedDataMysqlUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImporterAnalyzedDataMysqlUsersInner:
        """Test ImporterAnalyzedDataMysqlUsersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImporterAnalyzedDataMysqlUsersInner`
        """
        model = ImporterAnalyzedDataMysqlUsersInner()
        if include_optional:
            return ImporterAnalyzedDataMysqlUsersInner(
                username = '',
                auth_plugin = ''
            )
        else:
            return ImporterAnalyzedDataMysqlUsersInner(
                username = '',
                auth_plugin = '',
        )
        """

    def testImporterAnalyzedDataMysqlUsersInner(self):
        """Test ImporterAnalyzedDataMysqlUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
