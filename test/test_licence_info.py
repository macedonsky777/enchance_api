# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.licence_info import LicenceInfo

class TestLicenceInfo(unittest.TestCase):
    """LicenceInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenceInfo:
        """Test LicenceInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenceInfo`
        """
        model = LicenceInfo()
        if include_optional:
            return LicenceInfo(
                key = '',
                status = 'active'
            )
        else:
            return LicenceInfo(
                status = 'active',
        )
        """

    def testLicenceInfo(self):
        """Test LicenceInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()