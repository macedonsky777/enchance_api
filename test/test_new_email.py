# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_email import NewEmail

class TestNewEmail(unittest.TestCase):
    """NewEmail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewEmail:
        """Test NewEmail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewEmail`
        """
        model = NewEmail()
        if include_optional:
            return NewEmail(
                mailbox_name = '',
                mailbox_password = '',
                username = '',
                aliases = [
                    ''
                    ],
                forwarders = [
                    ''
                    ],
                quota = 56
            )
        else:
            return NewEmail(
                username = '',
        )
        """

    def testNewEmail(self):
        """Test NewEmail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
