# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_crontab_value_cmd_cron_cmd import UpdateCrontabValueCmdCronCmd

class TestUpdateCrontabValueCmdCronCmd(unittest.TestCase):
    """UpdateCrontabValueCmdCronCmd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCrontabValueCmdCronCmd:
        """Test UpdateCrontabValueCmdCronCmd
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCrontabValueCmdCronCmd`
        """
        model = UpdateCrontabValueCmdCronCmd()
        if include_optional:
            return UpdateCrontabValueCmdCronCmd(
                line_number = 1.337,
                expr = ''
            )
        else:
            return UpdateCrontabValueCmdCronCmd(
                line_number = 1.337,
        )
        """

    def testUpdateCrontabValueCmdCronCmd(self):
        """Test UpdateCrontabValueCmdCronCmd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()