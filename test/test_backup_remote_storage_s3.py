# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.backup_remote_storage_s3 import BackupRemoteStorageS3

class TestBackupRemoteStorageS3(unittest.TestCase):
    """BackupRemoteStorageS3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BackupRemoteStorageS3:
        """Test BackupRemoteStorageS3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BackupRemoteStorageS3`
        """
        model = BackupRemoteStorageS3()
        if include_optional:
            return BackupRemoteStorageS3(
                purpose = 'backup',
                region = '',
                endpoint = '',
                bucket = '',
                access_key_id = '',
                prefix = ''
            )
        else:
            return BackupRemoteStorageS3(
                purpose = 'backup',
                region = '',
                endpoint = '',
                bucket = '',
                access_key_id = '',
                prefix = '',
        )
        """

    def testBackupRemoteStorageS3(self):
        """Test BackupRemoteStorageS3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
