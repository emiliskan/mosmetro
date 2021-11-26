from typing import Optional

import pathlib
import logging.config as logging_config

from pydantic import BaseSettings, Field, validator


class DBConnection(BaseSettings):
    host: str = Field('localhost', env='MONGO_HOST')
    port: int = Field(27017, env='MONGO_PORT')
    user: str = Field('root', env='MONGO_USERNAME')
    password: str = Field('example', env='MONGO_PASSWORD')
    connection: str = ''

    @validator("connection", pre=True)
    def set_connection(cls, v: Optional[str], values: dict) -> str:  # noqa
        return f'mongodb://{values["user"]}:{values["password"]}@{values["host"]}:{values["port"]}'


class Settings(BaseSettings):
    test: bool = Field(True, env='SCRAPER_TEST')
    broker_url = Field('pyamqp://guest:guest@localhost//', env='BROKER_URL')
    db_connect: DBConnection = DBConnection()


settings = Settings()
