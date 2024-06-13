# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.domain_mappings_full_listing import DomainMappingsFullListing

class TestDomainMappingsFullListing(unittest.TestCase):
    """DomainMappingsFullListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainMappingsFullListing:
        """Test DomainMappingsFullListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainMappingsFullListing`
        """
        model = DomainMappingsFullListing()
        if include_optional:
            return DomainMappingsFullListing(
                items = [
                    openapi_client.models.domain_mapping.DomainMapping(
                        domain_id = '', 
                        website_id = '', 
                        domain = '', 
                        mapping_kind = 'primary', 
                        document_root = '', 
                        cert = openapi_client.models.domain_ssl_cert.DomainSslCert(
                            cn = '', 
                            expires = '', 
                            issued = '', 
                            issuer = '', 
                            sans = [
                                ''
                                ], 
                            force_https = True, ), 
                        cloudflare_status = 'Connected', 
                        cloudflare_friendly_name = '', 
                        cloudflare_token_id = '', )
                    ]
            )
        else:
            return DomainMappingsFullListing(
                items = [
                    openapi_client.models.domain_mapping.DomainMapping(
                        domain_id = '', 
                        website_id = '', 
                        domain = '', 
                        mapping_kind = 'primary', 
                        document_root = '', 
                        cert = openapi_client.models.domain_ssl_cert.DomainSslCert(
                            cn = '', 
                            expires = '', 
                            issued = '', 
                            issuer = '', 
                            sans = [
                                ''
                                ], 
                            force_https = True, ), 
                        cloudflare_status = 'Connected', 
                        cloudflare_friendly_name = '', 
                        cloudflare_token_id = '', )
                    ],
        )
        """

    def testDomainMappingsFullListing(self):
        """Test DomainMappingsFullListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
