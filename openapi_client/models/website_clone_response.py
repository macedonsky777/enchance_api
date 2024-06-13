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
from openapi_client.models.website_clone_enum_status import WebsiteCloneEnumStatus
from typing import Optional, Set
from typing_extensions import Self

class WebsiteCloneResponse(BaseModel):
    """
    WebsiteCloneResponse
    """ # noqa: E501
    id: StrictStr
    source_website_id: StrictStr = Field(alias="sourceWebsiteId")
    dest_website_id: Optional[StrictStr] = Field(default=None, alias="destWebsiteId")
    exclude_paths: List[StrictStr] = Field(alias="excludePaths")
    include_databases: List[StrictStr] = Field(alias="includeDatabases")
    include_database_users: List[StrictStr] = Field(alias="includeDatabaseUsers")
    delete_files_from_destination: StrictBool = Field(alias="deleteFilesFromDestination")
    status: WebsiteCloneEnumStatus
    sync_php_version: StrictBool = Field(alias="syncPhpVersion")
    __properties: ClassVar[List[str]] = ["id", "sourceWebsiteId", "destWebsiteId", "excludePaths", "includeDatabases", "includeDatabaseUsers", "deleteFilesFromDestination", "status", "syncPhpVersion"]

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
        """Create an instance of WebsiteCloneResponse from a JSON string"""
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
        """Create an instance of WebsiteCloneResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "sourceWebsiteId": obj.get("sourceWebsiteId"),
            "destWebsiteId": obj.get("destWebsiteId"),
            "excludePaths": obj.get("excludePaths"),
            "includeDatabases": obj.get("includeDatabases"),
            "includeDatabaseUsers": obj.get("includeDatabaseUsers"),
            "deleteFilesFromDestination": obj.get("deleteFilesFromDestination"),
            "status": obj.get("status"),
            "syncPhpVersion": obj.get("syncPhpVersion")
        })
        return _obj

