# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.org_owner_update import OrgOwnerUpdate

class TestOrgOwnerUpdate(unittest.TestCase):
    """OrgOwnerUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgOwnerUpdate:
        """Test OrgOwnerUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgOwnerUpdate`
        """
        model = OrgOwnerUpdate()
        if include_optional:
            return OrgOwnerUpdate(
                member_id = ''
            )
        else:
            return OrgOwnerUpdate(
                member_id = '',
        )
        """

    def testOrgOwnerUpdate(self):
        """Test OrgOwnerUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
