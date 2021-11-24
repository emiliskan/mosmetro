from loaders.base_loader import NewsLoaderAbstract
from scrapers.base_scraper import AbstractScraper


class Transfer:

    def __init__(
            self,
            scraper: AbstractScraper,
            loader: NewsLoaderAbstract,
    ):
        self.scraper = scraper
        self.loader = loader

    def transfer(self):
        data = self.scraper.scrap()
        self.loader.load(data)
