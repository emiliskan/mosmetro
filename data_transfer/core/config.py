from typing import Optional

from pydantic import BaseSettings, Field, validator


class DBConnection(BaseSettings):
    host: str = Field('localhost', env='MONGO_HOST')
    port: int = Field(27017, env='MONGO_PORT')
    user: str = Field('root', env='MONGO_USERNAME')
    password: str = Field('example', env='MONGO_PASSWORD')
    name: str = Field('metro', env='MONGO_DATABASE')
    connection: str = ''

    @validator("connection", pre=True)
    def set_connection(cls, v: Optional[str], values: dict) -> str:  # noqa
        return f'mongodb://{values["user"]}:{values["password"]}@{values["host"]}:{values["port"]}'


class Settings(BaseSettings):
    debug: bool = Field(True, env='SCRAPER_DEBUG')
    broker_url = Field('pyamqp://guest:guest@localhost//', env='BROKER_URL')
    db_connect: DBConnection = DBConnection()


settings = Settings()
