# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.ssl_api import SslApi


class TestSslApi(unittest.TestCase):
    """SslApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SslApi()

    def tearDown(self) -> None:
        pass

    def test_get_website_domain_ssl_cert(self) -> None:
        """Test case for get_website_domain_ssl_cert

        Returns the SSL for this website domain
        """
        pass

    def test_get_website_mail_domain_ssl_cert(self) -> None:
        """Test case for get_website_mail_domain_ssl_cert

        Returns the SSL for this website domain with the mail.prefix
        """
        pass

    def test_set_website_domain_force_ssl(self) -> None:
        """Test case for set_website_domain_force_ssl

        Set \"force ssl\" status for domain mapping
        """
        pass

    def test_upload_website_domain_ssl_cert(self) -> None:
        """Test case for upload_website_domain_ssl_cert

        Upload custom ssl certificate, key and optional fullchain for a given website
        """
        pass

    def test_upload_website_mail_domain_ssl_cert(self) -> None:
        """Test case for upload_website_mail_domain_ssl_cert

        Upload SSL for mail.customerdomain.
        """
        pass


if __name__ == '__main__':
    unittest.main()
