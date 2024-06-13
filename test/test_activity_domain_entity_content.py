# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_domain_entity_content import ActivityDomainEntityContent

class TestActivityDomainEntityContent(unittest.TestCase):
    """ActivityDomainEntityContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityDomainEntityContent:
        """Test ActivityDomainEntityContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityDomainEntityContent`
        """
        model = ActivityDomainEntityContent()
        if include_optional:
            return ActivityDomainEntityContent(
                id = '',
                detail = openapi_client.models.activity_domain_entity_content_detail.ActivityDomainEntity_content_detail(
                    ok = openapi_client.models.activity_domain_entity_detail.ActivityDomainEntityDetail(
                        name = '', 
                        org_id = '', 
                        website_id = '', 
                        mapping_kind = 'primary', ), 
                    error = openapi_client.models.http_error.HttpError(
                        code = '', 
                        message = '', ), )
            )
        else:
            return ActivityDomainEntityContent(
                id = '',
                detail = openapi_client.models.activity_domain_entity_content_detail.ActivityDomainEntity_content_detail(
                    ok = openapi_client.models.activity_domain_entity_detail.ActivityDomainEntityDetail(
                        name = '', 
                        org_id = '', 
                        website_id = '', 
                        mapping_kind = 'primary', ), 
                    error = openapi_client.models.http_error.HttpError(
                        code = '', 
                        message = '', ), ),
        )
        """

    def testActivityDomainEntityContent(self):
        """Test ActivityDomainEntityContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()