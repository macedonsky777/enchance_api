# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.local_remote_body import LocalRemoteBody

class TestLocalRemoteBody(unittest.TestCase):
    """LocalRemoteBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocalRemoteBody:
        """Test LocalRemoteBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocalRemoteBody`
        """
        model = LocalRemoteBody()
        if include_optional:
            return LocalRemoteBody(
                local_remote = 'local'
            )
        else:
            return LocalRemoteBody(
        )
        """

    def testLocalRemoteBody(self):
        """Test LocalRemoteBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
