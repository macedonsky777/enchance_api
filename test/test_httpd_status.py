# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.httpd_status import HttpdStatus

class TestHttpdStatus(unittest.TestCase):
    """HttpdStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpdStatus:
        """Test HttpdStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpdStatus`
        """
        model = HttpdStatus()
        if include_optional:
            return HttpdStatus(
                raw_output = ''
            )
        else:
            return HttpdStatus(
                raw_output = '',
        )
        """

    def testHttpdStatus(self):
        """Test HttpdStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
