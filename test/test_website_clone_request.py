# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.website_clone_request import WebsiteCloneRequest

class TestWebsiteCloneRequest(unittest.TestCase):
    """WebsiteCloneRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsiteCloneRequest:
        """Test WebsiteCloneRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsiteCloneRequest`
        """
        model = WebsiteCloneRequest()
        if include_optional:
            return WebsiteCloneRequest(
                run_wp_search_replace = True,
                source_website_id = '',
                dest_website_id = '',
                exclude_paths = [
                    ''
                    ],
                include_databases = [
                    ''
                    ],
                include_database_users = [
                    ''
                    ],
                delete_files_from_destination = True,
                sync_php_version = True,
                new_website = openapi_client.models.website_clone_new_website.WebsiteCloneNewWebsite(
                    domain = '', 
                    subscription_id = 56, 
                    app_server_id = '', 
                    backup_server_id = '', 
                    db_server_id = '', 
                    email_server_id = '', 
                    server_group_id = '', 
                    php_version = 'php56', 
                    kind = 'normal', )
            )
        else:
            return WebsiteCloneRequest(
                source_website_id = '',
                exclude_paths = [
                    ''
                    ],
                delete_files_from_destination = True,
                sync_php_version = True,
        )
        """

    def testWebsiteCloneRequest(self):
        """Test WebsiteCloneRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()