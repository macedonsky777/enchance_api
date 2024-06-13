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
from openapi_client.models.cloud_flare_status import CloudFlareStatus
from openapi_client.models.domain_mapping_kind import DomainMappingKind
from openapi_client.models.domain_ssl_cert import DomainSslCert
from typing import Optional, Set
from typing_extensions import Self

class DomainMapping(BaseModel):
    """
    DomainMapping
    """ # noqa: E501
    domain_id: StrictStr = Field(alias="domainId")
    website_id: StrictStr = Field(alias="websiteId")
    domain: StrictStr
    mapping_kind: DomainMappingKind = Field(alias="mappingKind")
    document_root: StrictStr = Field(alias="documentRoot")
    cert: Optional[DomainSslCert] = None
    cloudflare_status: CloudFlareStatus = Field(alias="cloudflareStatus")
    cloudflare_friendly_name: Optional[StrictStr] = Field(default=None, alias="cloudflareFriendlyName")
    cloudflare_token_id: Optional[StrictStr] = Field(default=None, alias="cloudflareTokenId")
    __properties: ClassVar[List[str]] = ["domainId", "websiteId", "domain", "mappingKind", "documentRoot", "cert", "cloudflareStatus", "cloudflareFriendlyName", "cloudflareTokenId"]

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
        """Create an instance of DomainMapping from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cert
        if self.cert:
            _dict['cert'] = self.cert.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domainId": obj.get("domainId"),
            "websiteId": obj.get("websiteId"),
            "domain": obj.get("domain"),
            "mappingKind": obj.get("mappingKind"),
            "documentRoot": obj.get("documentRoot"),
            "cert": DomainSslCert.from_dict(obj["cert"]) if obj.get("cert") is not None else None,
            "cloudflareStatus": obj.get("cloudflareStatus"),
            "cloudflareFriendlyName": obj.get("cloudflareFriendlyName"),
            "cloudflareTokenId": obj.get("cloudflareTokenId")
        })
        return _obj


