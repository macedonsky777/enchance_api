# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.install_api import InstallApi


class TestInstallApi(unittest.TestCase):
    """InstallApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InstallApi()

    def tearDown(self) -> None:
        pass

    def test_controld_version(self) -> None:
        """Test case for controld_version

        Get the compatible controld version
        """
        pass

    def test_get_service_kind_latest_version(self) -> None:
        """Test case for get_service_kind_latest_version

        Get the latest available version of a given service kind
        """
        pass

    def test_install(self) -> None:
        """Test case for install

        Create the master organization owner
        """
        pass

    def test_orchd_status(self) -> None:
        """Test case for orchd_status

        Get the readiness status of the orchd service
        """
        pass

    def test_orchd_version(self) -> None:
        """Test case for orchd_version

        Get the SemVer of the API service
        """
        pass

    def test_update_enhance(self) -> None:
        """Test case for update_enhance

        Updates all services in the cluster.
        """
        pass

    def test_validate_installation(self) -> None:
        """Test case for validate_installation

        Used to validate that the control panel has been initialized.
        """
        pass


if __name__ == '__main__':
    unittest.main()
