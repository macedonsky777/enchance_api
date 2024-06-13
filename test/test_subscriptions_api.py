# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.subscriptions_api import SubscriptionsApi


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SubscriptionsApi()

    def tearDown(self) -> None:
        pass

    def test_calculate_resource_usage(self) -> None:
        """Test case for calculate_resource_usage

        Re-Calculates all subscription resources
        """
        pass

    def test_create_customer_subscription(self) -> None:
        """Test case for create_customer_subscription

        Create a subscriptions for a customer
        """
        pass

    def test_delete_subscription(self) -> None:
        """Test case for delete_subscription

        Delete subscription
        """
        pass

    def test_get_customer_subscriptions(self) -> None:
        """Test case for get_customer_subscriptions

        Get customer subscriptions
        """
        pass

    def test_get_subscription(self) -> None:
        """Test case for get_subscription

        Get subscription
        """
        pass

    def test_get_subscription_bandwidth_usage(self) -> None:
        """Test case for get_subscription_bandwidth_usage

        Get subscription bandwidth
        """
        pass

    def test_get_subscriptions_to_parent(self) -> None:
        """Test case for get_subscriptions_to_parent

        Get subscriptions to parent
        """
        pass

    def test_update_subscription(self) -> None:
        """Test case for update_subscription

        Update subscription
        """
        pass


if __name__ == '__main__':
    unittest.main()