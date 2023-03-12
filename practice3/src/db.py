from typing import Any, AsyncGenerator

import asyncpg
from asyncpg.connection import Connection
from asyncpg.pool import Pool
from motor.motor_asyncio import AsyncIOMotorClient
from src.settings import settings

_client = AsyncIOMotorClient(settings.MONGO_DSN)

_pool: Pool = None


async def _init_pool():
    global _pool

    _pool = await asyncpg.create_pool(settings.POSTGRES_DSN)


async def _init_tables():
    async with _pool.acquire() as conn:
        conn: Connection

        await conn.execute(
            """
            CREATE SCHEMA IF NOT EXISTS practice3;
            
            CREATE TABLE IF NOT EXISTS practice3.employee (
                id SERIAL,
                first_name VARCHAR(32),
                second_name VARCHAR(32),
                email VARCHAR(128),
                tel VARCHAR(16)
            );
            """
        )


async def get_mongo_conn() -> AsyncGenerator[AsyncIOMotorClient, Any]:
    async with await _client.start_session():
        yield _client


async def get_postgres_conn() -> AsyncGenerator[asyncpg.Connection, Any]:
    async with _pool.acquire() as conn:
        yield conn
