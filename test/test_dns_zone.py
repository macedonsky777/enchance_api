# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.dns_zone import DnsZone

class TestDnsZone(unittest.TestCase):
    """DnsZone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsZone:
        """Test DnsZone
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsZone`
        """
        model = DnsZone()
        if include_optional:
            return DnsZone(
                origin = '',
                soa = openapi_client.models.dns_soa.DnsSoa(
                    admin_email = '', 
                    name_server = '', 
                    expire = 56, 
                    refresh = 56, 
                    retry = 56, 
                    ttl = 56, ),
                records = [
                    openapi_client.models.dns_record.DnsRecord(
                        id = '', 
                        kind = 'A', 
                        name = '', 
                        value = '', 
                        ttl = 56, 
                        proxy = True, )
                    ],
                dnssec_ds_records = '',
                dnssec_dnskey_records = ''
            )
        else:
            return DnsZone(
                origin = '',
                soa = openapi_client.models.dns_soa.DnsSoa(
                    admin_email = '', 
                    name_server = '', 
                    expire = 56, 
                    refresh = 56, 
                    retry = 56, 
                    ttl = 56, ),
                records = [
                    openapi_client.models.dns_record.DnsRecord(
                        id = '', 
                        kind = 'A', 
                        name = '', 
                        value = '', 
                        ttl = 56, 
                        proxy = True, )
                    ],
        )
        """

    def testDnsZone(self):
        """Test DnsZone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()