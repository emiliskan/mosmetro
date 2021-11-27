from core.celery_app import app
from loaders.news_loader import get_news_loader
from scrapers.news_scraper import get_news_scraper


@app.task(name='scrap_news', acks_late=True, task_eager_propagates=True)
def scrap_news():
    scraper = get_news_scraper()
    loader = get_news_loader()

    news = scraper.scrap()
    loader.load(news)
