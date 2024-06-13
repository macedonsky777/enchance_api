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


class NetworkStatus(str, Enum):
    """
    NetworkStatus
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    ONLINE = 'online'
    RESTARTING = 'restarting'
    WARNING = 'warning'
    CRITICAL = 'critical'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NetworkStatus from a JSON string"""
        return cls(json.loads(json_str))

