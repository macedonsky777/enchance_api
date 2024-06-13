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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.website_app_kind import WebsiteAppKind
from typing import Optional, Set
from typing_extensions import Self

class WebsiteApp(BaseModel):
    """
    WebsiteApp
    """ # noqa: E501
    id: Optional[StrictStr] = None
    app: WebsiteAppKind
    path: Optional[StrictStr] = Field(default=None, description="The path is only present if the app is installed in the root instead of a subfolder. For example if a customer installs Wordpress at '/blog', then the path will be present and equal to 'blog'. But if they install WP in website root, instead of returning '/' or empty string, this property is omitted.")
    default_wp_user_id: Optional[StrictInt] = Field(default=None, description="Only present if default was set by the user. Otherwise, this field isn't there.", alias="defaultWpUserId")
    __properties: ClassVar[List[str]] = ["id", "app", "path", "defaultWpUserId"]

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
        """Create an instance of WebsiteApp from a JSON string"""
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
        """Create an instance of WebsiteApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "app": obj.get("app"),
            "path": obj.get("path"),
            "defaultWpUserId": obj.get("defaultWpUserId")
        })
        return _obj

