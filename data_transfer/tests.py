from loaders.news_loader import get_news_loader
from scrapers.news_scraper import get_news_scraper
from transfer import Transfer


def _scrap_news():
    scraper = get_news_scraper()
    data = scraper.scrap()
    print(data)


def transfer_news():
    news_transfer: Transfer = Transfer(
        scraper=get_news_scraper(),
        loader=get_news_loader(),
    )
    news_transfer.transfer()


if __name__ == '__main__':
    transfer_news()
