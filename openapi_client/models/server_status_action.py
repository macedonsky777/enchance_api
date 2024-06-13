# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ServerStatusAction(str, Enum):
    """
    ServerStatusAction
    """

    """
    allowed enum values
    """
    GRACEFULREBOOT = 'gracefulReboot'
    FORCEREBOOT = 'forceReboot'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ServerStatusAction from a JSON string"""
        return cls(json.loads(json_str))


