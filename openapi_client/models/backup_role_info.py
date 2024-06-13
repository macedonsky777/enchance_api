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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from openapi_client.models.server_role_state import ServerRoleState
from openapi_client.models.service_info import ServiceInfo
from typing import Optional, Set
from typing_extensions import Self

class BackupRoleInfo(BaseModel):
    """
    BackupRoleInfo
    """ # noqa: E501
    state: ServerRoleState
    usage: StrictInt
    snapshots_count: StrictInt = Field(alias="snapshotsCount")
    last24h_snapshots_count: StrictInt = Field(alias="last24hSnapshotsCount")
    bkupd: ServiceInfo
    websites_count: StrictInt = Field(description="The number of websites whose backups are assigned to be on this backup role.", alias="websitesCount")
    __properties: ClassVar[List[str]] = ["state", "usage", "snapshotsCount", "last24hSnapshotsCount", "bkupd", "websitesCount"]

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
        """Create an instance of BackupRoleInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bkupd
        if self.bkupd:
            _dict['bkupd'] = self.bkupd.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupRoleInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "usage": obj.get("usage"),
            "snapshotsCount": obj.get("snapshotsCount"),
            "last24hSnapshotsCount": obj.get("last24hSnapshotsCount"),
            "bkupd": ServiceInfo.from_dict(obj["bkupd"]) if obj.get("bkupd") is not None else None,
            "websitesCount": obj.get("websitesCount")
        })
        return _obj


