# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.roles_summary import RolesSummary

class TestRolesSummary(unittest.TestCase):
    """RolesSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RolesSummary:
        """Test RolesSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RolesSummary`
        """
        model = RolesSummary()
        if include_optional:
            return RolesSummary(
                email = openapi_client.models.role_summary.RoleSummary(
                    state = 'enabled', 
                    status = 'unknown', ),
                backup = openapi_client.models.role_summary.RoleSummary(
                    state = 'enabled', 
                    status = 'unknown', ),
                database = openapi_client.models.role_summary.RoleSummary(
                    state = 'enabled', 
                    status = 'unknown', ),
                application = openapi_client.models.role_summary.RoleSummary(
                    state = 'enabled', 
                    status = 'unknown', ),
                dns = openapi_client.models.role_summary.RoleSummary(
                    state = 'enabled', 
                    status = 'unknown', ),
                control_panel = openapi_client.models.role_summary.RoleSummary(
                    state = 'enabled', 
                    status = 'unknown', )
            )
        else:
            return RolesSummary(
        )
        """

    def testRolesSummary(self):
        """Test RolesSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
