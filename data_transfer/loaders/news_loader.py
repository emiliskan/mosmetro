from pymongo import MongoClient

from core.db_connection import get_db_client
from loaders.base_loader import AbstractLoader
from models.news_models import NewsModel


class NewsLoader(AbstractLoader):

    def __init__(self, db: MongoClient):
        self.db = db

    def load(self, data: list[NewsModel]):
        news_collection = self.db['news']
        for article in data:
            news_collection.update_one({'id': article.id}, {'$set': article.dict()}, upsert=True)


def get_news_loader() -> NewsLoader:
    db_client = get_db_client()
    return NewsLoader(
        db=db_client,
    )
