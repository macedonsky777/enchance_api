# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.licence_key import LicenceKey

class TestLicenceKey(unittest.TestCase):
    """LicenceKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenceKey:
        """Test LicenceKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenceKey`
        """
        model = LicenceKey()
        if include_optional:
            return LicenceKey(
                key = ''
            )
        else:
            return LicenceKey(
                key = '',
        )
        """

    def testLicenceKey(self):
        """Test LicenceKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()