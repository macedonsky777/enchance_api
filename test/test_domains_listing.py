# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.domains_listing import DomainsListing

class TestDomainsListing(unittest.TestCase):
    """DomainsListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainsListing:
        """Test DomainsListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainsListing`
        """
        model = DomainsListing()
        if include_optional:
            return DomainsListing(
                items = [
                    openapi_client.models.domain.Domain(
                        id = '', 
                        org_id = '', 
                        domain = '', 
                        dkim = True, 
                        spf = True, 
                        cloudflare_status = 'Connected', 
                        cloudflare_token_friendly_name = '', )
                    ],
                total = 56
            )
        else:
            return DomainsListing(
                items = [
                    openapi_client.models.domain.Domain(
                        id = '', 
                        org_id = '', 
                        domain = '', 
                        dkim = True, 
                        spf = True, 
                        cloudflare_status = 'Connected', 
                        cloudflare_token_friendly_name = '', )
                    ],
                total = 56,
        )
        """

    def testDomainsListing(self):
        """Test DomainsListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
