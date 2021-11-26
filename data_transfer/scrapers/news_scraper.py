import locale
from datetime import datetime

import requests

import cssutils
from bs4 import BeautifulSoup

from models.news_models import NewsModel
from scrapers.base_scraper import AbstractScraper


class NewsScraper(AbstractScraper):

    def scrap(self) -> list[NewsModel]:

        scraped_data = []

        url = "https://mosmetro.ru/news"
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="page")

        classes = [
            "news-card",
            "news-card hidden",
            "news-card news-card_filled news__decorated",
            "news-card news-card_filled news-card_big news__decorated"
        ]

        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        year = str(datetime.now().year)
        for class_name in classes:
            news = results.find_all("a", class_=class_name)

            for article in news:

                link = article['href']
                article_id = int(link[link.find('=') + 1:])

                caption = article.find("div", class_="news-card__caption").text.strip()

                date = article.find("div", class_="news-card__date").text.strip()
                date = f'{year} {date}'
                date = datetime.strptime(date, "%Y %d %B, %H:%M")

                image = article.find("div", class_="news-card__image")
                style = cssutils.parseStyle(image['style'])
                image_src = style['background-image'].replace('url(', '').replace(')', '')

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
