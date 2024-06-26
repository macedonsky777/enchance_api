# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activities_listing import ActivitiesListing

class TestActivitiesListing(unittest.TestCase):
    """ActivitiesListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivitiesListing:
        """Test ActivitiesListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivitiesListing`
        """
        model = ActivitiesListing()
        if include_optional:
            return ActivitiesListing(
                total = 56,
                items = [
                    openapi_client.models.activity.Activity(
                        id = '', 
                        org_id = '', 
                        kind = 'added', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        context = openapi_client.models.activity_context.ActivityContext(
                            org = openapi_client.models.activity_org_entity.ActivityOrgEntity(
                                type = 'org', 
                                content = openapi_client.models.activity_org_entity_content.ActivityOrgEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_org_entity_content_detail.ActivityOrgEntity_content_detail(
                                        ok = openapi_client.models.activity_org_entity_detail.ActivityOrgEntityDetail(
                                            name = '', ), 
                                        error = openapi_client.models.http_error.HttpError(
                                            code = '', 
                                            message = '', ), ), ), ), 
                            website = openapi_client.models.activity_website_entity.ActivityWebsiteEntity(
                                type = 'website', 
                                content = openapi_client.models.activity_website_entity_content.ActivityWebsiteEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_website_entity_content_detail.ActivityWebsiteEntity_content_detail(), ), ), 
                            domain = openapi_client.models.activity_domain_entity.ActivityDomainEntity(
                                type = 'domain', 
                                content = openapi_client.models.activity_domain_entity_content.ActivityDomainEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_domain_entity_content_detail.ActivityDomainEntity_content_detail(), ), ), 
                            actor = null, 
                            server = openapi_client.models.activity_server_entity.ActivityServerEntity(
                                type = 'server', 
                                content = openapi_client.models.activity_server_entity_content.ActivityServerEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_server_entity_content_detail.ActivityServerEntity_content_detail(), ), ), 
                            error = openapi_client.models.activity_error_entity.ActivityErrorEntity(
                                type = 'error', 
                                content = openapi_client.models.activity_error_entity_content.ActivityErrorEntity_content(
                                    detail = openapi_client.models.http_error.HttpError(
                                        code = '', 
                                        message = '', ), ), ), ), 
                        activity_object = null, )
                    ]
            )
        else:
            return ActivitiesListing(
                total = 56,
                items = [
                    openapi_client.models.activity.Activity(
                        id = '', 
                        org_id = '', 
                        kind = 'added', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        context = openapi_client.models.activity_context.ActivityContext(
                            org = openapi_client.models.activity_org_entity.ActivityOrgEntity(
                                type = 'org', 
                                content = openapi_client.models.activity_org_entity_content.ActivityOrgEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_org_entity_content_detail.ActivityOrgEntity_content_detail(
                                        ok = openapi_client.models.activity_org_entity_detail.ActivityOrgEntityDetail(
                                            name = '', ), 
                                        error = openapi_client.models.http_error.HttpError(
                                            code = '', 
                                            message = '', ), ), ), ), 
                            website = openapi_client.models.activity_website_entity.ActivityWebsiteEntity(
                                type = 'website', 
                                content = openapi_client.models.activity_website_entity_content.ActivityWebsiteEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_website_entity_content_detail.ActivityWebsiteEntity_content_detail(), ), ), 
                            domain = openapi_client.models.activity_domain_entity.ActivityDomainEntity(
                                type = 'domain', 
                                content = openapi_client.models.activity_domain_entity_content.ActivityDomainEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_domain_entity_content_detail.ActivityDomainEntity_content_detail(), ), ), 
                            actor = null, 
                            server = openapi_client.models.activity_server_entity.ActivityServerEntity(
                                type = 'server', 
                                content = openapi_client.models.activity_server_entity_content.ActivityServerEntity_content(
                                    id = '', 
                                    detail = openapi_client.models.activity_server_entity_content_detail.ActivityServerEntity_content_detail(), ), ), 
                            error = openapi_client.models.activity_error_entity.ActivityErrorEntity(
                                type = 'error', 
                                content = openapi_client.models.activity_error_entity_content.ActivityErrorEntity_content(
                                    detail = openapi_client.models.http_error.HttpError(
                                        code = '', 
                                        message = '', ), ), ), ), 
                        activity_object = null, )
                    ],
        )
        """

    def testActivitiesListing(self):
        """Test ActivitiesListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
