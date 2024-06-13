# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CloudFlareApiKey(BaseModel):
    """
    CloudFlareApiKey
    """ # noqa: E501
    id: StrictStr
    token: StrictStr
    updated_at: date = Field(alias="updatedAt")
    friendly_name: StrictStr = Field(alias="friendlyName")
    last_sync: Optional[date] = Field(default=None, alias="lastSync")
    last_message: Optional[StrictStr] = Field(default=None, alias="lastMessage")
    domains: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["id", "token", "updatedAt", "friendlyName", "lastSync", "lastMessage", "domains"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CloudFlareApiKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudFlareApiKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "token": obj.get("token"),
            "updatedAt": obj.get("updatedAt"),
            "friendlyName": obj.get("friendlyName"),
            "lastSync": obj.get("lastSync"),
            "lastMessage": obj.get("lastMessage"),
            "domains": obj.get("domains")
        })
        return _obj

