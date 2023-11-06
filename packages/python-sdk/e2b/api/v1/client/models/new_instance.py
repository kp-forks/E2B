# coding: utf-8

"""
    E2B API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from pydantic import BaseModel, Field, StrictStr


class NewInstance(BaseModel):
    """
    NewInstance
    """

    env_id: StrictStr = Field(
        ..., alias="envID", description="Identifier of the required environment"
    )
    __properties = ["envID"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NewInstance:
        """Create an instance of NewInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NewInstance:
        """Create an instance of NewInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NewInstance.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError(
                    "Error due to additional fields (not defined in NewInstance) in the input: "
                    + obj
                )

        _obj = NewInstance.parse_obj({"env_id": obj.get("envID")})
        return _obj