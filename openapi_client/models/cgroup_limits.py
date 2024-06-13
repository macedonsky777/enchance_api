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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CgroupLimits(BaseModel):
    """
    CgroupLimits
    """ # noqa: E501
    nproc: Optional[Union[StrictFloat, StrictInt]]
    memory_limit: Optional[Union[StrictFloat, StrictInt]] = Field(alias="memoryLimit")
    iops: Optional[Union[StrictFloat, StrictInt]]
    io_bandwidth: Optional[Union[StrictFloat, StrictInt]] = Field(alias="ioBandwidth")
    virtual_cpus: Optional[Union[StrictFloat, StrictInt]] = Field(alias="virtualCpus")
    __properties: ClassVar[List[str]] = ["nproc", "memoryLimit", "iops", "ioBandwidth", "virtualCpus"]

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
        """Create an instance of CgroupLimits from a JSON string"""
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
        # set to None if nproc (nullable) is None
        # and model_fields_set contains the field
        if self.nproc is None and "nproc" in self.model_fields_set:
            _dict['nproc'] = None

        # set to None if memory_limit (nullable) is None
        # and model_fields_set contains the field
        if self.memory_limit is None and "memory_limit" in self.model_fields_set:
            _dict['memoryLimit'] = None

        # set to None if iops (nullable) is None
        # and model_fields_set contains the field
        if self.iops is None and "iops" in self.model_fields_set:
            _dict['iops'] = None

        # set to None if io_bandwidth (nullable) is None
        # and model_fields_set contains the field
        if self.io_bandwidth is None and "io_bandwidth" in self.model_fields_set:
            _dict['ioBandwidth'] = None

        # set to None if virtual_cpus (nullable) is None
        # and model_fields_set contains the field
        if self.virtual_cpus is None and "virtual_cpus" in self.model_fields_set:
            _dict['virtualCpus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CgroupLimits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nproc": obj.get("nproc"),
            "memoryLimit": obj.get("memoryLimit"),
            "iops": obj.get("iops"),
            "ioBandwidth": obj.get("ioBandwidth"),
            "virtualCpus": obj.get("virtualCpus")
        })
        return _obj


