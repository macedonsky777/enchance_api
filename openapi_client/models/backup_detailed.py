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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.backup_kind import BackupKind
from openapi_client.models.backup_storage_kind import BackupStorageKind
from openapi_client.models.operation_status import OperationStatus
from typing import Optional, Set
from typing_extensions import Self

class BackupDetailed(BaseModel):
    """
    BackupDetailed
    """ # noqa: E501
    id: StrictInt
    website_id: StrictStr = Field(alias="websiteId")
    started_at: datetime = Field(alias="startedAt")
    finished_at: Optional[datetime] = Field(default=None, alias="finishedAt")
    snapshot_dir_name: StrictStr = Field(alias="snapshotDirName")
    size: Optional[StrictInt] = None
    home_dir_status: Optional[OperationStatus] = Field(default=None, alias="homeDirStatus")
    files_size: Optional[StrictInt] = Field(default=None, alias="filesSize")
    mysql_dbs_status: Optional[OperationStatus] = Field(default=None, alias="mysqlDbsStatus")
    mysql_dbs: Optional[List[StrictStr]] = Field(default=None, alias="mysqlDbs")
    mysql_dbs_size: Optional[StrictInt] = Field(default=None, alias="mysqlDbsSize")
    emails_status: Optional[OperationStatus] = Field(default=None, alias="emailsStatus")
    emails: Optional[List[StrictStr]] = Field(default=None, description="The addresses of the backed up mailboxes.")
    email_domains: Optional[List[StrictStr]] = Field(default=None, description="The domain ids of the backed up mailboxes.", alias="emailDomains")
    emails_size: Optional[StrictInt] = Field(default=None, alias="emailsSize")
    kind: BackupKind
    description: Optional[StrictStr] = None
    storage_kind: BackupStorageKind = Field(alias="storageKind")
    __properties: ClassVar[List[str]] = ["id", "websiteId", "startedAt", "finishedAt", "snapshotDirName", "size", "homeDirStatus", "filesSize", "mysqlDbsStatus", "mysqlDbs", "mysqlDbsSize", "emailsStatus", "emails", "emailDomains", "emailsSize", "kind", "description", "storageKind"]

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
        """Create an instance of BackupDetailed from a JSON string"""
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
        """Create an instance of BackupDetailed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "websiteId": obj.get("websiteId"),
            "startedAt": obj.get("startedAt"),
            "finishedAt": obj.get("finishedAt"),
            "snapshotDirName": obj.get("snapshotDirName"),
            "size": obj.get("size"),
            "homeDirStatus": obj.get("homeDirStatus"),
            "filesSize": obj.get("filesSize"),
            "mysqlDbsStatus": obj.get("mysqlDbsStatus"),
            "mysqlDbs": obj.get("mysqlDbs"),
            "mysqlDbsSize": obj.get("mysqlDbsSize"),
            "emailsStatus": obj.get("emailsStatus"),
            "emails": obj.get("emails"),
            "emailDomains": obj.get("emailDomains"),
            "emailsSize": obj.get("emailsSize"),
            "kind": obj.get("kind"),
            "description": obj.get("description"),
            "storageKind": obj.get("storageKind")
        })
        return _obj


