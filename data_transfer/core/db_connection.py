from core.config import settings

from pymongo import MongoClient

client = MongoClient(settings.db_connect.connection)


def get_db_client():
    return client['metro']
