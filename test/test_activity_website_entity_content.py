# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_website_entity_content import ActivityWebsiteEntityContent

class TestActivityWebsiteEntityContent(unittest.TestCase):
    """ActivityWebsiteEntityContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityWebsiteEntityContent:
        """Test ActivityWebsiteEntityContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityWebsiteEntityContent`
        """
        model = ActivityWebsiteEntityContent()
        if include_optional:
            return ActivityWebsiteEntityContent(
                id = '',
                detail = openapi_client.models.activity_website_entity_content_detail.ActivityWebsiteEntity_content_detail(
                    ok = openapi_client.models.activity_website_entity_detail.ActivityWebsiteEntityDetail(
                        domain = '', 
                        subscription_id = '', 
                        org_id = '', ), 
                    error = openapi_client.models.http_error.HttpError(
                        code = '', 
                        message = '', ), )
            )
        else:
            return ActivityWebsiteEntityContent(
                id = '',
                detail = openapi_client.models.activity_website_entity_content_detail.ActivityWebsiteEntity_content_detail(
                    ok = openapi_client.models.activity_website_entity_detail.ActivityWebsiteEntityDetail(
                        domain = '', 
                        subscription_id = '', 
                        org_id = '', ), 
                    error = openapi_client.models.http_error.HttpError(
                        code = '', 
                        message = '', ), ),
        )
        """

    def testActivityWebsiteEntityContent(self):
        """Test ActivityWebsiteEntityContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
