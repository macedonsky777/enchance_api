# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.import_migration_entry import ImportMigrationEntry

class TestImportMigrationEntry(unittest.TestCase):
    """ImportMigrationEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportMigrationEntry:
        """Test ImportMigrationEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportMigrationEntry`
        """
        model = ImportMigrationEntry()
        if include_optional:
            return ImportMigrationEntry(
                id = '',
                org_id = '',
                filename = '',
                filesize = 56,
                status = 'unprocessed',
                import_type = 'cPanel',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                percentage_complete = 56,
                primary_domain = ''
            )
        else:
            return ImportMigrationEntry(
                id = '',
                org_id = '',
                filename = '',
                filesize = 56,
                status = 'unprocessed',
                import_type = 'cPanel',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                percentage_complete = 56,
        )
        """

    def testImportMigrationEntry(self):
        """Test ImportMigrationEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
