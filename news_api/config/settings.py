from typing import Optional

from pydantic import BaseSettings, Field, validator


class DBConnection(BaseSettings):
    host: str = Field('localhost', env='MONGO_HOST')
    port: int = Field(27017, env='MONGO_PORT')
    user: str = Field('root', env='MONGO_USERNAME')
    password: str = Field('example', env='MONGO_PASSWORD')
    name: str = Field('metro', env='MONGO_DATABASE')
    connection: str = ''

    @validator('connection', pre=True)
    def set_connection(cls, v: Optional[str], values: dict) -> str:
        return f'mongodb://{values["user"]}:{values["password"]}@{values["host"]}:{values["port"]}'


class Config(BaseSettings):
    debug = Field(False, env="DEBUG")
    flask_host = Field("0.0.0.0", env="NEWS_API_HOST")
    flask_port = Field(5000, env="NEWS_API_PORT")
    db_connect: DBConnection = DBConnection()


config = Config()
