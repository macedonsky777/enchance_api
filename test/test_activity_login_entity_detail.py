# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity_login_entity_detail import ActivityLoginEntityDetail

class TestActivityLoginEntityDetail(unittest.TestCase):
    """ActivityLoginEntityDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityLoginEntityDetail:
        """Test ActivityLoginEntityDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityLoginEntityDetail`
        """
        model = ActivityLoginEntityDetail()
        if include_optional:
            return ActivityLoginEntityDetail(
                name = '',
                email = '',
                realm_id = ''
            )
        else:
            return ActivityLoginEntityDetail(
                name = '',
                email = '',
                realm_id = '',
        )
        """

    def testActivityLoginEntityDetail(self):
        """Test ActivityLoginEntityDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
