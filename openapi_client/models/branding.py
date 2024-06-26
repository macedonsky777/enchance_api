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
from openapi_client.models.cp_locale import CPLocale
from openapi_client.models.setting import Setting
from typing import Optional, Set
from typing_extensions import Self

class Branding(BaseModel):
    """
    Branding
    """ # noqa: E501
    org_name: StrictStr = Field(alias="orgName")
    parent: Optional[StrictStr] = None
    control_panel_domain: Optional[StrictStr] = Field(default=None, alias="controlPanelDomain")
    php_my_admin_domain: Optional[StrictStr] = Field(default=None, alias="phpMyAdminDomain")
    roundcube_domain: Optional[StrictStr] = Field(default=None, alias="roundcubeDomain")
    logo_path: Optional[StrictStr] = Field(default=None, alias="logoPath")
    inverse_logo_path: Optional[StrictStr] = Field(default=None, alias="inverseLogoPath")
    inverse_icon_path: Optional[StrictStr] = Field(default=None, alias="inverseIconPath")
    login_image_path: Optional[StrictStr] = Field(default=None, alias="loginImagePath")
    favicon_path: Optional[StrictStr] = Field(default=None, alias="faviconPath")
    name_servers: Optional[List[StrictStr]] = Field(default=None, alias="nameServers")
    settings: List[Setting]
    staging_domain: Optional[StrictStr] = Field(default=None, alias="stagingDomain")
    locale: CPLocale
    __properties: ClassVar[List[str]] = ["orgName", "parent", "controlPanelDomain", "phpMyAdminDomain", "roundcubeDomain", "logoPath", "inverseLogoPath", "inverseIconPath", "loginImagePath", "faviconPath", "nameServers", "settings", "stagingDomain", "locale"]

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
        """Create an instance of Branding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in settings (list)
        _items = []
        if self.settings:
            for _item in self.settings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['settings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Branding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orgName": obj.get("orgName"),
            "parent": obj.get("parent"),
            "controlPanelDomain": obj.get("controlPanelDomain"),
            "phpMyAdminDomain": obj.get("phpMyAdminDomain"),
            "roundcubeDomain": obj.get("roundcubeDomain"),
            "logoPath": obj.get("logoPath"),
            "inverseLogoPath": obj.get("inverseLogoPath"),
            "inverseIconPath": obj.get("inverseIconPath"),
            "loginImagePath": obj.get("loginImagePath"),
            "faviconPath": obj.get("faviconPath"),
            "nameServers": obj.get("nameServers"),
            "settings": [Setting.from_dict(_item) for _item in obj["settings"]] if obj.get("settings") is not None else None,
            "stagingDomain": obj.get("stagingDomain"),
            "locale": obj.get("locale")
        })
        return _obj


