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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.my_sql_auth_plugin import MySQLAuthPlugin
from typing import Optional, Set
from typing_extensions import Self

class MySQLUser(BaseModel):
    """
    MySQLUser
    """ # noqa: E501
    id: StrictStr
    db_id: Optional[StrictStr] = Field(default=None, alias="dbId")
    username: StrictStr
    access_hosts: List[StrictStr] = Field(alias="accessHosts")
    auth_plugin: MySQLAuthPlugin = Field(alias="authPlugin")
    grants: Dict[str, Any] = Field(description="Table names mapped to a list of privileges on that table. The wildcard \"*\" means the privileges are granted for all tables.")
    created_at: StrictStr = Field(alias="createdAt")
    is_ephemeral: Optional[StrictBool] = Field(default=False, description="A flag which marks short-lived mysql accounts. If an account is created as ephemeral, it will be deleted few hours after it's been created. Throwaway accounts are useful for phpMyAdmin logins.", alias="isEphemeral")
    __properties: ClassVar[List[str]] = ["id", "dbId", "username", "accessHosts", "authPlugin", "grants", "createdAt", "isEphemeral"]

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
        """Create an instance of MySQLUser from a JSON string"""
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
        """Create an instance of MySQLUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "dbId": obj.get("dbId"),
            "username": obj.get("username"),
            "accessHosts": obj.get("accessHosts"),
            "authPlugin": obj.get("authPlugin"),
            "grants": obj.get("grants"),
            "createdAt": obj.get("createdAt"),
            "isEphemeral": obj.get("isEphemeral") if obj.get("isEphemeral") is not None else False
        })
        return _obj

