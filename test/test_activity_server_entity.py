# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_server_entity import ActivityServerEntity

class TestActivityServerEntity(unittest.TestCase):
    """ActivityServerEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityServerEntity:
        """Test ActivityServerEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityServerEntity`
        """
        model = ActivityServerEntity()
        if include_optional:
            return ActivityServerEntity(
                type = 'server',
                content = openapi_client.models.activity_server_entity_content.ActivityServerEntity_content(
                    id = '', 
                    detail = openapi_client.models.activity_server_entity_content_detail.ActivityServerEntity_content_detail(
                        ok = openapi_client.models.activity_server_entity_detail.ActivityServerEntityDetail(
                            friendly_name = '', 
                            hostname = '', ), 
                        error = openapi_client.models.http_error.HttpError(
                            code = '', 
                            message = '', ), ), )
            )
        else:
            return ActivityServerEntity(
                type = 'server',
                content = openapi_client.models.activity_server_entity_content.ActivityServerEntity_content(
                    id = '', 
                    detail = openapi_client.models.activity_server_entity_content_detail.ActivityServerEntity_content_detail(
                        ok = openapi_client.models.activity_server_entity_detail.ActivityServerEntityDetail(
                            friendly_name = '', 
                            hostname = '', ), 
                        error = openapi_client.models.http_error.HttpError(
                            code = '', 
                            message = '', ), ), ),
        )
        """

    def testActivityServerEntity(self):
        """Test ActivityServerEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
