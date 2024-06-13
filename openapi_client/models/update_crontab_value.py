# coding: utf-8

"""
    orchd

    orchd API docs

    The version of the OpenAPI document: 10.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.update_crontab_value_cmd import UpdateCrontabValueCmd
from openapi_client.models.update_crontab_value_variable import UpdateCrontabValueVariable
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPDATECRONTABVALUE_ONE_OF_SCHEMAS = ["UpdateCrontabValueCmd", "UpdateCrontabValueVariable"]

class UpdateCrontabValue(BaseModel):
    """
    UpdateCrontabValue
    """
    # data type: UpdateCrontabValueVariable
    oneof_schema_1_validator: Optional[UpdateCrontabValueVariable] = None
    # data type: UpdateCrontabValueCmd
    oneof_schema_2_validator: Optional[UpdateCrontabValueCmd] = None
    actual_instance: Optional[Union[UpdateCrontabValueCmd, UpdateCrontabValueVariable]] = None
    one_of_schemas: Set[str] = { "UpdateCrontabValueCmd", "UpdateCrontabValueVariable" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = UpdateCrontabValue.model_construct()
        error_messages = []
        match = 0
        # validate data type: UpdateCrontabValueVariable
        if not isinstance(v, UpdateCrontabValueVariable):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateCrontabValueVariable`")
        else:
            match += 1
        # validate data type: UpdateCrontabValueCmd
        if not isinstance(v, UpdateCrontabValueCmd):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateCrontabValueCmd`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateCrontabValue with oneOf schemas: UpdateCrontabValueCmd, UpdateCrontabValueVariable. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateCrontabValue with oneOf schemas: UpdateCrontabValueCmd, UpdateCrontabValueVariable. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into UpdateCrontabValueVariable
        try:
            instance.actual_instance = UpdateCrontabValueVariable.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateCrontabValueCmd
        try:
            instance.actual_instance = UpdateCrontabValueCmd.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateCrontabValue with oneOf schemas: UpdateCrontabValueCmd, UpdateCrontabValueVariable. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateCrontabValue with oneOf schemas: UpdateCrontabValueCmd, UpdateCrontabValueVariable. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], UpdateCrontabValueCmd, UpdateCrontabValueVariable]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

