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
from openapi_client.models.update_application_role import UpdateApplicationRole
from openapi_client.models.update_backup_role import UpdateBackupRole
from openapi_client.models.update_database_role import UpdateDatabaseRole
from openapi_client.models.update_dns_role import UpdateDnsRole
from openapi_client.models.update_email_role import UpdateEmailRole
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPDATESERVERROLEREQUEST_ONE_OF_SCHEMAS = ["UpdateApplicationRole", "UpdateBackupRole", "UpdateDatabaseRole", "UpdateDnsRole", "UpdateEmailRole"]

class UpdateServerRoleRequest(BaseModel):
    """
    UpdateServerRoleRequest
    """
    # data type: UpdateEmailRole
    oneof_schema_1_validator: Optional[UpdateEmailRole] = None
    # data type: UpdateBackupRole
    oneof_schema_2_validator: Optional[UpdateBackupRole] = None
    # data type: UpdateDatabaseRole
    oneof_schema_3_validator: Optional[UpdateDatabaseRole] = None
    # data type: UpdateApplicationRole
    oneof_schema_4_validator: Optional[UpdateApplicationRole] = None
    # data type: UpdateDnsRole
    oneof_schema_5_validator: Optional[UpdateDnsRole] = None
    actual_instance: Optional[Union[UpdateApplicationRole, UpdateBackupRole, UpdateDatabaseRole, UpdateDnsRole, UpdateEmailRole]] = None
    one_of_schemas: Set[str] = { "UpdateApplicationRole", "UpdateBackupRole", "UpdateDatabaseRole", "UpdateDnsRole", "UpdateEmailRole" }

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
        instance = UpdateServerRoleRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: UpdateEmailRole
        if not isinstance(v, UpdateEmailRole):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateEmailRole`")
        else:
            match += 1
        # validate data type: UpdateBackupRole
        if not isinstance(v, UpdateBackupRole):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateBackupRole`")
        else:
            match += 1
        # validate data type: UpdateDatabaseRole
        if not isinstance(v, UpdateDatabaseRole):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateDatabaseRole`")
        else:
            match += 1
        # validate data type: UpdateApplicationRole
        if not isinstance(v, UpdateApplicationRole):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateApplicationRole`")
        else:
            match += 1
        # validate data type: UpdateDnsRole
        if not isinstance(v, UpdateDnsRole):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateDnsRole`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateServerRoleRequest with oneOf schemas: UpdateApplicationRole, UpdateBackupRole, UpdateDatabaseRole, UpdateDnsRole, UpdateEmailRole. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateServerRoleRequest with oneOf schemas: UpdateApplicationRole, UpdateBackupRole, UpdateDatabaseRole, UpdateDnsRole, UpdateEmailRole. Details: " + ", ".join(error_messages))
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

        # deserialize data into UpdateEmailRole
        try:
            instance.actual_instance = UpdateEmailRole.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateBackupRole
        try:
            instance.actual_instance = UpdateBackupRole.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateDatabaseRole
        try:
            instance.actual_instance = UpdateDatabaseRole.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateApplicationRole
        try:
            instance.actual_instance = UpdateApplicationRole.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateDnsRole
        try:
            instance.actual_instance = UpdateDnsRole.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateServerRoleRequest with oneOf schemas: UpdateApplicationRole, UpdateBackupRole, UpdateDatabaseRole, UpdateDnsRole, UpdateEmailRole. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateServerRoleRequest with oneOf schemas: UpdateApplicationRole, UpdateBackupRole, UpdateDatabaseRole, UpdateDnsRole, UpdateEmailRole. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], UpdateApplicationRole, UpdateBackupRole, UpdateDatabaseRole, UpdateDnsRole, UpdateEmailRole]]:
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


