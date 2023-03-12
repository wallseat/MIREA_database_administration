from fastapi import FastAPI
from src.db import _init_pool, _init_tables
from src.routes import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    await _init_pool()
    await _init_tables()
