import requests

import cssutils
from bs4 import BeautifulSoup

from core.config import settings
from models.news_models import NewsModel
from scrapers.base_scraper import AbstractScraper


class NewsScraper(AbstractScraper):

    def scrap(self) -> list[NewsModel]:

        scraped_data = []

        URL = "https://mosmetro.ru/news"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="page")

        classes = [
            "news-card",
            "news-card hidden",
            "news-card news-card_filled news__decorated",
            "news-card news-card_filled news-card_big news__decorated"
        ]

        for class_name in classes:
            news = results.find_all("a", class_=class_name)

            for article in news:

                link = article['href']
                article_id = int(link[link.find('=') + 1:])

                caption = article.find("div", class_="news-card__caption").text
                date = article.find("div", class_="news-card__date").text

                image = article.find("div", class_="news-card__image")
                style = cssutils.parseStyle(image)
                image_src = style['background-image']

                news_data = NewsModel(
                    id=article_id,
                    caption=caption,
                    date=date,
                    image_src=image_src,
                )
                scraped_data.append(news_data)

        return scraped_data


def get_news_scraper() -> NewsScraper:
    return NewsScraper()
