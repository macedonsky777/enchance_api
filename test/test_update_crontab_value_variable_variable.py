# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_crontab_value_variable_variable import UpdateCrontabValueVariableVariable

class TestUpdateCrontabValueVariableVariable(unittest.TestCase):
    """UpdateCrontabValueVariableVariable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCrontabValueVariableVariable:
        """Test UpdateCrontabValueVariableVariable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCrontabValueVariableVariable`
        """
        model = UpdateCrontabValueVariableVariable()
        if include_optional:
            return UpdateCrontabValueVariableVariable(
                line_number = 1.337,
                key = '',
                val = ''
            )
        else:
            return UpdateCrontabValueVariableVariable(
                line_number = 1.337,
        )
        """

    def testUpdateCrontabValueVariableVariable(self):
        """Test UpdateCrontabValueVariableVariable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
