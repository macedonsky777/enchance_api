# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.customers_api import CustomersApi


class TestCustomersApi(unittest.TestCase):
    """CustomersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CustomersApi()

    def tearDown(self) -> None:
        pass

    def test_create_customer(self) -> None:
        """Test case for create_customer

        Create a customer organization
        """
        pass

    def test_create_customer_subscription(self) -> None:
        """Test case for create_customer_subscription

        Create a subscriptions for a customer
        """
        pass

    def test_get_customer_subscriptions(self) -> None:
        """Test case for get_customer_subscriptions

        Get customer subscriptions
        """
        pass

    def test_get_org_customers(self) -> None:
        """Test case for get_org_customers

        Get organization customers
        """
        pass


if __name__ == '__main__':
    unittest.main()
