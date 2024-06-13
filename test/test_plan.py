# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.plan import Plan

class TestPlan(unittest.TestCase):
    """Plan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Plan:
        """Test Plan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Plan`
        """
        model = Plan()
        if include_optional:
            return Plan(
                id = 56,
                name = '',
                org_id = '',
                resources = [
                    openapi_client.models.resource.Resource(
                        name = 'customers', 
                        total = 56, )
                    ],
                allowances = [
                    openapi_client.models.allowance.Allowance(
                        name = '', )
                    ],
                selections = [
                    openapi_client.models.selection.Selection(
                        name = '', 
                        value = '', )
                    ],
                subscriptions_count = 56,
                server_group_id = '',
                server_group_ids = [
                    ''
                    ],
                allow_server_group_selection = True,
                created_at = '',
                plan_type = 'shared',
                cgroup_limits = openapi_client.models.cgroup_limits.CgroupLimits(
                    nproc = 1.337, 
                    memory_limit = 1.337, 
                    iops = 1.337, 
                    io_bandwidth = 1.337, 
                    virtual_cpus = 1.337, ),
                fs_quota_limit = openapi_client.models.fs_quota_limit.FsQuotaLimit(
                    total_available = 1.337, ),
                allowed_php_versions = [
                    'php56'
                    ],
                default_php_version = 'php56',
                redis_allowed = True,
                preinstall_wordpress_theme = ''
            )
        else:
            return Plan(
                id = 56,
                name = '',
                org_id = '',
                resources = [
                    openapi_client.models.resource.Resource(
                        name = 'customers', 
                        total = 56, )
                    ],
                allowances = [
                    openapi_client.models.allowance.Allowance(
                        name = '', )
                    ],
                selections = [
                    openapi_client.models.selection.Selection(
                        name = '', 
                        value = '', )
                    ],
                subscriptions_count = 56,
                created_at = '',
                plan_type = 'shared',
                allowed_php_versions = [
                    'php56'
                    ],
                default_php_version = 'php56',
                redis_allowed = True,
        )
        """

    def testPlan(self):
        """Test Plan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
