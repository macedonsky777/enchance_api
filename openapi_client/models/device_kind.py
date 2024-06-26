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


class DeviceKind(str, Enum):
    """
    The type of the btrfs device, if `device` the block device must already exist, otherwise (with `sparseFile`) it will be created from a new (not existing) sparse file. In both cases the block device will be formatted to btrfs and mounted in the given mount point.
    """

    """
    allowed enum values
    """
    DEVICE = 'device'
    SPARSEFILE = 'sparseFile'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeviceKind from a JSON string"""
        return cls(json.loads(json_str))


