from core.celery_app import app
from loaders.news_loader import get_news_loader
from scrapers.news_scraper import get_news_scraper
from transfer import Transfer


@app.task(name="scrap_news", acks_late=True, task_eager_propagates=True)
def scrap_news():
    news_transfer: Transfer = Transfer(
        scraper=get_news_scraper(),
        loader=get_news_loader(),
    )
    news_transfer.transfer()
