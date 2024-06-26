# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.backup_detailed import BackupDetailed

class TestBackupDetailed(unittest.TestCase):
    """BackupDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BackupDetailed:
        """Test BackupDetailed
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BackupDetailed`
        """
        model = BackupDetailed()
        if include_optional:
            return BackupDetailed(
                id = 56,
                website_id = '',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                snapshot_dir_name = '',
                size = 56,
                home_dir_status = 'started',
                files_size = 56,
                mysql_dbs_status = 'started',
                mysql_dbs = [
                    ''
                    ],
                mysql_dbs_size = 56,
                emails_status = 'started',
                emails = [
                    ''
                    ],
                email_domains = [
                    ''
                    ],
                emails_size = 56,
                kind = 'manual',
                description = '',
                storage_kind = 'enhance'
            )
        else:
            return BackupDetailed(
                id = 56,
                website_id = '',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                snapshot_dir_name = '',
                kind = 'manual',
                storage_kind = 'enhance',
        )
        """

    def testBackupDetailed(self):
        """Test BackupDetailed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
