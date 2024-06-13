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


class WebsiteLogStatus(str, Enum):
    """
    The status of the website at the time the log was written. Some statuses have additional metadata (ok, slow, failed4xx, failed5xx) whereas some don't (timeout, dnsZoneNotFound, appServerMismatch).
    """

    """
    allowed enum values
    """
    OK = 'ok'
    SLOW = 'slow'
    FAILED4XX = 'failed4xx'
    FAILED5XX = 'failed5xx'
    TIMEOUT = 'timeout'
    DNSZONENOTFOUND = 'dnsZoneNotFound'
    APPSERVERMISMATCH = 'appServerMismatch'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebsiteLogStatus from a JSON string"""
        return cls(json.loads(json_str))

