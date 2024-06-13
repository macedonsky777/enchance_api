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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AuthNs(BaseModel):
    """
    Authoritative Name Server
    """ # noqa: E501
    ip: Optional[StrictStr] = Field(default=None, description="Server IP address")
    domain_ips: Optional[List[StrictStr]] = Field(default=None, description="list of resolved ip addresses for the domain", alias="domainIps")
    delegations: Optional[Dict[str, AuthNs]] = Field(default=None, description="Tree of delegated AuthNs servers")
    __properties: ClassVar[List[str]] = ["ip", "domainIps", "delegations"]

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
        """Create an instance of AuthNs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in delegations (dict)
        _field_dict = {}
        if self.delegations:
            for _key in self.delegations:
                if self.delegations[_key]:
                    _field_dict[_key] = self.delegations[_key].to_dict()
            _dict['delegations'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthNs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ip": obj.get("ip"),
            "domainIps": obj.get("domainIps"),
            "delegations": dict(
                (_k, AuthNs.from_dict(_v))
                for _k, _v in obj["delegations"].items()
            )
            if obj.get("delegations") is not None
            else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
AuthNs.model_rebuild(raise_errors=False)
