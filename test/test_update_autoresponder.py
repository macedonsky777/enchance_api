# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_autoresponder import UpdateAutoresponder

class TestUpdateAutoresponder(unittest.TestCase):
    """UpdateAutoresponder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateAutoresponder:
        """Test UpdateAutoresponder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateAutoresponder`
        """
        model = UpdateAutoresponder()
        if include_optional:
            return UpdateAutoresponder(
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                enabled = True,
                subject = '',
                body = ''
            )
        else:
            return UpdateAutoresponder(
        )
        """

    def testUpdateAutoresponder(self):
        """Test UpdateAutoresponder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
