# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.metrics_api import MetricsApi


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_website_metrics(self) -> None:
        """Test case for get_website_metrics

        Get website metrics
        """
        pass


if __name__ == '__main__':
    unittest.main()