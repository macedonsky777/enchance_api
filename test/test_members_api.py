# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.members_api import MembersApi


class TestMembersApi(unittest.TestCase):
    """MembersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MembersApi()

    def tearDown(self) -> None:
        pass

    def test_create_access_token(self) -> None:
        """Test case for create_access_token

        Create organisation access token
        """
        pass

    def test_create_member(self) -> None:
        """Test case for create_member

        Create organization member
        """
        pass

    def test_delete_access_token(self) -> None:
        """Test case for delete_access_token

        Delete access token member
        """
        pass

    def test_delete_member(self) -> None:
        """Test case for delete_member

        Delete organization member
        """
        pass

    def test_delete_owner(self) -> None:
        """Test case for delete_owner

        Delete organization owner
        """
        pass

    def test_get_access_tokens(self) -> None:
        """Test case for get_access_tokens

        Get access token members
        """
        pass

    def test_get_member(self) -> None:
        """Test case for get_member

        Get organization member
        """
        pass

    def test_get_members(self) -> None:
        """Test case for get_members

        Get organization members
        """
        pass

    def test_get_org_member_login(self) -> None:
        """Test case for get_org_member_login

        Get a One-Time-Password link for the member
        """
        pass

    def test_update_member(self) -> None:
        """Test case for update_member

        Overwrite organization member settings
        """
        pass

    def test_update_owner(self) -> None:
        """Test case for update_owner

        Update organization owner
        """
        pass


if __name__ == '__main__':
    unittest.main()
