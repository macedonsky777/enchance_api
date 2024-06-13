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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.activity_context_actor import ActivityContextActor
from openapi_client.models.activity_domain_entity import ActivityDomainEntity
from openapi_client.models.activity_error_entity import ActivityErrorEntity
from openapi_client.models.activity_org_entity import ActivityOrgEntity
from openapi_client.models.activity_server_entity import ActivityServerEntity
from openapi_client.models.activity_website_entity import ActivityWebsiteEntity
from typing import Optional, Set
from typing_extensions import Self

class ActivityContext(BaseModel):
    """
    ActivityContext
    """ # noqa: E501
    org: Optional[ActivityOrgEntity] = None
    website: Optional[ActivityWebsiteEntity] = None
    domain: Optional[ActivityDomainEntity] = None
    actor: Optional[ActivityContextActor] = None
    server: Optional[ActivityServerEntity] = None
    error: Optional[ActivityErrorEntity] = None
    __properties: ClassVar[List[str]] = ["org", "website", "domain", "actor", "server", "error"]

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
        """Create an instance of ActivityContext from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of org
        if self.org:
            _dict['org'] = self.org.to_dict()
        # override the default output from pydantic by calling `to_dict()` of website
        if self.website:
            _dict['website'] = self.website.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain
        if self.domain:
            _dict['domain'] = self.domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActivityContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "org": ActivityOrgEntity.from_dict(obj["org"]) if obj.get("org") is not None else None,
            "website": ActivityWebsiteEntity.from_dict(obj["website"]) if obj.get("website") is not None else None,
            "domain": ActivityDomainEntity.from_dict(obj["domain"]) if obj.get("domain") is not None else None,
            "actor": ActivityContextActor.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "server": ActivityServerEntity.from_dict(obj["server"]) if obj.get("server") is not None else None,
            "error": ActivityErrorEntity.from_dict(obj["error"]) if obj.get("error") is not None else None
        })
        return _obj

