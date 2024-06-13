# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_org_entity_content_detail import ActivityOrgEntityContentDetail

class TestActivityOrgEntityContentDetail(unittest.TestCase):
    """ActivityOrgEntityContentDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityOrgEntityContentDetail:
        """Test ActivityOrgEntityContentDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityOrgEntityContentDetail`
        """
        model = ActivityOrgEntityContentDetail()
        if include_optional:
            return ActivityOrgEntityContentDetail(
                ok = openapi_client.models.activity_org_entity_detail.ActivityOrgEntityDetail(
                    name = '', ),
                error = openapi_client.models.http_error.HttpError(
                    code = '', 
                    detail = '', 
                    message = '', )
            )
        else:
            return ActivityOrgEntityContentDetail(
        )
        """

    def testActivityOrgEntityContentDetail(self):
        """Test ActivityOrgEntityContentDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()