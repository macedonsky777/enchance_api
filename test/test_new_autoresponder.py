# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.new_autoresponder import NewAutoresponder

class TestNewAutoresponder(unittest.TestCase):
    """NewAutoresponder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewAutoresponder:
        """Test NewAutoresponder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewAutoresponder`
        """
        model = NewAutoresponder()
        if include_optional:
            return NewAutoresponder(
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                enabled = True,
                subject = '',
                body = ''
            )
        else:
            return NewAutoresponder(
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                enabled = True,
                subject = '',
                body = '',
        )
        """

    def testNewAutoresponder(self):
        """Test NewAutoresponder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
