from datetime import datetime, timedelta

from config.database import get_db_client
from models.news_model import NewsModel


def get_last_news(day_count: int = 10, offset: int = 0, limit: int = 10) -> list[NewsModel]:
    db = get_db_client()
    news = db['news']

    until_date = datetime.now() - timedelta(days=day_count)
    news_db = news.find({
        'date': {
            '$gte': until_date,
        },
    }).sort('id').skip(offset).limit(limit)

    for article in news_db:
        yield NewsModel(**article)
