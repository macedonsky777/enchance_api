# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_access_token import NewAccessToken

class TestNewAccessToken(unittest.TestCase):
    """NewAccessToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewAccessToken:
        """Test NewAccessToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewAccessToken`
        """
        model = NewAccessToken()
        if include_optional:
            return NewAccessToken(
                roles = [
                    'Owner'
                    ],
                token_expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                friendly_name = ''
            )
        else:
            return NewAccessToken(
                roles = [
                    'Owner'
                    ],
        )
        """

    def testNewAccessToken(self):
        """Test NewAccessToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
