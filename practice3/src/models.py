from typing import Annotated, Optional

from bson.objectid import ObjectId
from pydantic import BaseModel, PositiveInt, constr


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


str_16 = Annotated[str, constr(max_length=16)]
str_32 = Annotated[str, constr(max_length=32)]
str_128 = Annotated[str, constr(max_length=128)]


class EmployeeBase(BaseModel):
    first_name: str_32
    second_name: str_32
    email: Optional[str_128]
    tel: str_16


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id_: int

    class Config:
        json_encoders = {ObjectId: str}


class ProductBase(BaseModel):
    name: str_128
    price: float
    count: PositiveInt


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id_: PyObjectId

    class Config:
        json_encoders = {ObjectId: str}
