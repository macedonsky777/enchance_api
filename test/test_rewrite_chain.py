# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.rewrite_chain import RewriteChain

class TestRewriteChain(unittest.TestCase):
    """RewriteChain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RewriteChain:
        """Test RewriteChain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RewriteChain`
        """
        model = RewriteChain()
        if include_optional:
            return RewriteChain(
                line_number = 1.337,
                rule = openapi_client.models.rewrite_chain_rule.RewriteChain_rule(
                    pattern = '', 
                    substitution = '', 
                    flags = [
                        ''
                        ], ),
                conds = [
                    openapi_client.models.rewrite_chain_conds_inner.RewriteChain_conds_inner(
                        test_string = '', 
                        cond_pattern = '', 
                        flags = [
                            ''
                            ], )
                    ]
            )
        else:
            return RewriteChain(
                line_number = 1.337,
                rule = openapi_client.models.rewrite_chain_rule.RewriteChain_rule(
                    pattern = '', 
                    substitution = '', 
                    flags = [
                        ''
                        ], ),
                conds = [
                    openapi_client.models.rewrite_chain_conds_inner.RewriteChain_conds_inner(
                        test_string = '', 
                        cond_pattern = '', 
                        flags = [
                            ''
                            ], )
                    ],
        )
        """

    def testRewriteChain(self):
        """Test RewriteChain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
