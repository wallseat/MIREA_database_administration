from typing import List

from asyncpg.connection import Connection
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import parse_obj_as
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertOneResult
from src.models import Employee, EmployeeCreate, Product, ProductCreate
from src.settings import settings

PRODUCT_COLLECTION = "products"


def get_product_collection(mongo_conn: AsyncIOMotorClient) -> Collection:
    db: Database = mongo_conn.get_database(settings.MONGO_DB)
    return db.get_collection(PRODUCT_COLLECTION)


async def create_product(
    obj_in: ProductCreate,
    *,
    mongo_conn: AsyncIOMotorClient,
) -> Product:
    col = get_product_collection(mongo_conn)

    obj_in_dict = obj_in.dict()
    result: InsertOneResult = await col.insert_one(obj_in_dict)

    return Product.parse_obj(obj_in_dict | {"id_": result.inserted_id})


async def get_product_list(
    *,
    mongo_conn: AsyncIOMotorClient,
) -> List[Product]:
    col = get_product_collection(mongo_conn)

    result = col.find()
    products = [product | {"id_": product["_id"]} async for product in result]

    return parse_obj_as(List[Product], products)


async def delete_product(
    id_: ObjectId,
    *,
    mongo_conn: AsyncIOMotorClient,
) -> None:
    col = get_product_collection(mongo_conn)

    await col.delete_one({"_id": id_})


async def create_employee(
    obj_in: EmployeeCreate,
    *,
    postgres_conn: Connection,
) -> Employee:
    id_: int = await postgres_conn.fetchval(
        """
        INSERT INTO practice3.employee (first_name, second_name, email, tel)
        VALUES ($1, $2, $3, $4) 
        RETURNING id""",
        obj_in.first_name,
        obj_in.second_name,
        obj_in.email,
        obj_in.tel,
    )

    return Employee.parse_obj(obj_in.dict() | {"id_": id_})


async def get_employee_list(
    *,
    postgres_conn: Connection,
) -> List[Employee]:
    result = await postgres_conn.fetch(
        "SELECT id as id_, first_name, second_name, email, tel FROM practice3.employee"
    )

    return parse_obj_as(List[Employee], result)


async def delete_employee(
    id_: int,
    *,
    postgres_conn: Connection,
) -> None:
    await postgres_conn.execute("DELETE FROM practice3.employee WHERE id = $1", id_)
