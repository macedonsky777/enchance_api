# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.importer_analyzed_data_crontabs_inner import ImporterAnalyzedDataCrontabsInner

class TestImporterAnalyzedDataCrontabsInner(unittest.TestCase):
    """ImporterAnalyzedDataCrontabsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImporterAnalyzedDataCrontabsInner:
        """Test ImporterAnalyzedDataCrontabsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImporterAnalyzedDataCrontabsInner`
        """
        model = ImporterAnalyzedDataCrontabsInner()
        if include_optional:
            return ImporterAnalyzedDataCrontabsInner(
                username = '',
                crontab = ''
            )
        else:
            return ImporterAnalyzedDataCrontabsInner(
                username = '',
                crontab = '',
        )
        """

    def testImporterAnalyzedDataCrontabsInner(self):
        """Test ImporterAnalyzedDataCrontabsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()