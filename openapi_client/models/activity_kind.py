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


class ActivityKind(str, Enum):
    """
    Different activities that happen in orchd. There will be a lot of changes to the values of this enum as time goes by, consider this non-exhausive and be graceful with unknown values.
    """

    """
    allowed enum values
    """
    ADDED = 'added'
    REMOVED = 'removed'
    CLONED = 'cloned'
    IMPORTED = 'imported'
    BACKEDUP = 'backedUp'
    ERRORRAISED = 'errorRaised'
    BACKUPERROR = 'backupError'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActivityKind from a JSON string"""
        return cls(json.loads(json_str))


