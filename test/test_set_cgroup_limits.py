# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.set_cgroup_limits import SetCgroupLimits

class TestSetCgroupLimits(unittest.TestCase):
    """SetCgroupLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetCgroupLimits:
        """Test SetCgroupLimits
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetCgroupLimits`
        """
        model = SetCgroupLimits()
        if include_optional:
            return SetCgroupLimits(
                nproc = 1.337,
                memory_limit = 1.337,
                iops = 1.337,
                io_bandwidth = 1.337,
                virtual_cpus = 1.337
            )
        else:
            return SetCgroupLimits(
        )
        """

    def testSetCgroupLimits(self):
        """Test SetCgroupLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
