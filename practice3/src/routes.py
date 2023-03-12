from typing import List

from fastapi import APIRouter, Depends
from src import services
from src.db import get_mongo_conn, get_postgres_conn
from src.models import Employee, EmployeeCreate, Product, ProductCreate, PyObjectId

api_router = APIRouter()


@api_router.get(
    "/product",
    response_model=List[Product],
)
async def get_products(
    *,
    mongo_conn=Depends(get_mongo_conn),
):
    products = await services.get_product_list(mongo_conn=mongo_conn)

    return products


@api_router.post(
    "/product",
    response_model=Product,
    status_code=201,
)
async def create_product(
    product_in: ProductCreate,
    *,
    mongo_conn=Depends(get_mongo_conn),
):
    product = await services.create_product(product_in, mongo_conn=mongo_conn)

    return product


@api_router.delete(
    "/product/{product_id}",
    status_code=204,
)
async def delete_product(
    product_id: PyObjectId,
    *,
    mongo_conn=Depends(get_mongo_conn),
):
    await services.delete_product(product_id, mongo_conn=mongo_conn)


@api_router.get(
    "/employee",
    response_model=List[Employee],
)
async def get_employees(
    *,
    postgres_conn=Depends(get_postgres_conn),
):
    employees = await services.get_employee_list(postgres_conn=postgres_conn)

    return employees


@api_router.post(
    "/employee",
    response_model=Employee,
    status_code=201,
)
async def create_employee(
    employee_in: EmployeeCreate,
    *,
    postgres_conn=Depends(get_postgres_conn),
):
    employee = await services.create_employee(employee_in, postgres_conn=postgres_conn)

    return employee


@api_router.delete(
    "/employee/{employee_id}",
    status_code=204,
)
async def delete_employee(
    employee_id: int,
    *,
    postgres_conn=Depends(get_postgres_conn),
):
    await services.delete_employee(employee_id, postgres_conn=postgres_conn)
