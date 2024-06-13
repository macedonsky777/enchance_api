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


class SettingKind(str, Enum):
    """
    SettingKind
    """

    """
    allowed enum values
    """
    PHPINI = 'phpIni'
    PHPFPM = 'phpFpm'
    APACHE = 'apache'
    POSTFIX = 'postfix'
    SGED = 'sged'
    RSPAMD = 'rspamd'
    DOVECOT = 'dovecot'
    WEBSITEBACKUP = 'websiteBackup'
    SCREENSHOTD = 'screenshotd'
    HARDDELETEGC = 'hardDeleteGC'
    LETSENCRYPT = 'letsencrypt'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SettingKind from a JSON string"""
        return cls(json.loads(json_str))


