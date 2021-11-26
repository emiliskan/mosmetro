from config.settings import config

from pymongo import MongoClient

client = MongoClient(config.db_connect.connection)


def get_db_client():
    return client['metro']
