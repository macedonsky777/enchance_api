# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_login_entity_content import ActivityLoginEntityContent

class TestActivityLoginEntityContent(unittest.TestCase):
    """ActivityLoginEntityContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityLoginEntityContent:
        """Test ActivityLoginEntityContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityLoginEntityContent`
        """
        model = ActivityLoginEntityContent()
        if include_optional:
            return ActivityLoginEntityContent(
                id = '',
                detail = openapi_client.models.activity_login_entity_content_detail.ActivityLoginEntity_content_detail(
                    ok = openapi_client.models.activity_login_entity_detail.ActivityLoginEntityDetail(
                        name = '', 
                        email = '', 
                        realm_id = '', ), 
                    error = openapi_client.models.http_error.HttpError(
                        code = '', 
                        message = '', ), )
            )
        else:
            return ActivityLoginEntityContent(
                id = '',
                detail = openapi_client.models.activity_login_entity_content_detail.ActivityLoginEntity_content_detail(
                    ok = openapi_client.models.activity_login_entity_detail.ActivityLoginEntityDetail(
                        name = '', 
                        email = '', 
                        realm_id = '', ), 
                    error = openapi_client.models.http_error.HttpError(
                        code = '', 
                        message = '', ), ),
        )
        """

    def testActivityLoginEntityContent(self):
        """Test ActivityLoginEntityContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
