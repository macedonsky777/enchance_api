# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_object_entity import ActivityObjectEntity

class TestActivityObjectEntity(unittest.TestCase):
    """ActivityObjectEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityObjectEntity:
        """Test ActivityObjectEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityObjectEntity`
        """
        model = ActivityObjectEntity()
        if include_optional:
            return ActivityObjectEntity(
                type = 'website',
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
            return ActivityObjectEntity(
                type = 'website',
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

    def testActivityObjectEntity(self):
        """Test ActivityObjectEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
