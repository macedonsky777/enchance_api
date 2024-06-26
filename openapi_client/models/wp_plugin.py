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
from openapi_client.models.wp_plugin_auto_update_status import WPPluginAutoUpdateStatus
from openapi_client.models.wp_plugin_status import WPPluginStatus
from openapi_client.models.wp_plugin_update_available import WPPluginUpdateAvailable
from typing import Optional, Set
from typing_extensions import Self

class WpPlugin(BaseModel):
    """
    Describes the filename and additional plugin information. The filename is the name of the plugin php file, e.g. \"bbpress.php\". If the plugin kind is \"file\", then the file name refers to e.g. \"wp-content/plugins/bbpress.php\". If the kind is \"dir\", then the name refers to \"wp-content/plugins/bbpress/bbpress.php\". The name of the dir is always the same as the name of the file without the php suffix. https://developer.wordpress.org/plugins/plugin-basics/header-requirements/#header-fields
    """ # noqa: E501
    name: StrictStr
    uri: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    version: StrictStr
    update: Optional[WPPluginUpdateAvailable] = None
    auto_update: Optional[WPPluginAutoUpdateStatus] = Field(default=None, alias="autoUpdate")
    status: Optional[WPPluginStatus] = None
    author: StrictStr
    __properties: ClassVar[List[str]] = ["name", "uri", "description", "version", "update", "autoUpdate", "status", "author"]

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
        """Create an instance of WpPlugin from a JSON string"""
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
        """Create an instance of WpPlugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "uri": obj.get("uri"),
            "description": obj.get("description"),
            "version": obj.get("version"),
            "update": obj.get("update"),
            "autoUpdate": obj.get("autoUpdate"),
            "status": obj.get("status"),
            "author": obj.get("author")
        })
        return _obj


