# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ftp_users_full_listing import FtpUsersFullListing

class TestFtpUsersFullListing(unittest.TestCase):
    """FtpUsersFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FtpUsersFullListing:
        """Test FtpUsersFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FtpUsersFullListing`
        """
        model = FtpUsersFullListing()
        if include_optional:
            return FtpUsersFullListing(
                items = [
                    openapi_client.models.ftp_user.FtpUser(
                        id = '', 
                        account = '', 
                        home_dir = '', 
                        website_id = '', )
                    ]
            )
        else:
            return FtpUsersFullListing(
                items = [
                    openapi_client.models.ftp_user.FtpUser(
                        id = '', 
                        account = '', 
                        home_dir = '', 
                        website_id = '', )
                    ],
        )
        """

    def testFtpUsersFullListing(self):
        """Test FtpUsersFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
