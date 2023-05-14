from typing import Any, Mapping, Optional

from pydantic import BaseSettings, MongoDsn, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DB: str

    POSTGRES_DSN: Optional[str]
    MONGO_DSN: Optional[str]

    class Config:
        env_file = ".env"

    @validator("POSTGRES_DSN", pre=True)
    def construct_postgres_dsn(cls, v: Optional[str], values: Mapping[str, Any]) -> str:
        if v is not None:
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"],
            host=values["POSTGRES_HOST"],
            port=values["POSTGRES_PORT"],
            path="/" + values["POSTGRES_DB"],
        )

    @validator("MONGO_DSN", pre=True)
    def construct_mongo_dsn(cls, v: Optional[str], values: Mapping[str, Any]) -> str:
        if v is not None:
            return v

        return MongoDsn.build(
            scheme="mongodb",
            user=values.get("MONGO_USER"),
            password=values.get("MONGO_PASSWORD"),
            host=values.get("MONGO_HOST"),
            port=values.get("MONGO_PORT"),
        )


settings = Settings()
