# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.interface_ip import InterfaceIp

class TestInterfaceIp(unittest.TestCase):
    """InterfaceIp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceIp:
        """Test InterfaceIp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceIp`
        """
        model = InterfaceIp()
        if include_optional:
            return InterfaceIp(
                ip = '192.168.0.1',
                prefix = '255.255.192.0',
                kind = 'primary'
            )
        else:
            return InterfaceIp(
                ip = '192.168.0.1',
                prefix = '255.255.192.0',
                kind = 'primary',
        )
        """

    def testInterfaceIp(self):
        """Test InterfaceIp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
