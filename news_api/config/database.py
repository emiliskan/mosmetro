from pymongo import MongoClient
from config.settings import config

client = MongoClient(config.db_connect.connection)


def get_db_client():
    return client[config.db_connect.name]
