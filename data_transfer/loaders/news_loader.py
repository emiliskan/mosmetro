import traceback

from pymongo import MongoClient

from core.db_connection import get_db_client
from loaders.base_loader import AbstractNewsLoader
from models.news_models import NewsModel


class NewsLoader(AbstractNewsLoader):

    def __init__(self, db: MongoClient):
        self.db = db

    def load(self, data: list[NewsModel]):
        news_collection = self.db['news']
        for news in data:
            try:
                news_collection.update_one({'id': news.id}, {"$set": news.dict()}, upsert=True)
            except Exception:
                print(traceback.format_exc())


def get_news_loader() -> NewsLoader:
    db_client = get_db_client()
    return NewsLoader(
        db=db_client,
    )
