# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.rewrite_chain_rule import RewriteChainRule

class TestRewriteChainRule(unittest.TestCase):
    """RewriteChainRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RewriteChainRule:
        """Test RewriteChainRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RewriteChainRule`
        """
        model = RewriteChainRule()
        if include_optional:
            return RewriteChainRule(
                pattern = '',
                substitution = '',
                flags = [
                    ''
                    ]
            )
        else:
            return RewriteChainRule(
                pattern = '',
                substitution = '',
                flags = [
                    ''
                    ],
        )
        """

    def testRewriteChainRule(self):
        """Test RewriteChainRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
