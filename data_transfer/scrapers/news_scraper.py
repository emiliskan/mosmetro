import locale
from datetime import datetime

import requests
import cssutils
from bs4 import BeautifulSoup

from models.news_models import NewsModel
from scrapers.base_scraper import AbstractScraper

NEWS_URL = 'https://mosmetro.ru/news'


class NewsScraper(AbstractScraper):

    def scrap(self) -> list[NewsModel]:

        scraped_data = []

        news_html = requests.get(NEWS_URL)
        soup = BeautifulSoup(news_html.content, 'html.parser')
        page = soup.find(id='page')

        news_classes = (
            'news-card',
            'news-card hidden',
            'news-card news-card_filled news__decorated',
            'news-card news-card_filled news-card_big news__decorated',
        )

        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

        year = str(datetime.now().year)

        for class_name in news_classes:
            news = page.find_all('a', class_=class_name)

            for article in news:

                caption = article.find('div', class_='news-card__caption').text.strip()

                # ID новости лежит в ссылке. пр. link /detail/?news=906
                link = article['href']
                article_id = int(link[link.find('=') + 1:])

                # Дата приходит в формате '26 ноября, 20:15', преобразуем его в python объект
                date = article.find('div', class_='news-card__date').text.strip()
                date = f'{year} {date}'
                date = datetime.strptime(date, '%Y %d %B, %H:%M')

                # URL на картинку лежит в стиле background-image
                image = article.find('div', class_='news-card__image')
                style = cssutils.parseStyle(image['style'])
                image_src = style['background-image'].replace('url(', '').replace(')', '')

                news_data = NewsModel(
                    id=article_id,
                    caption=caption,
                    date=date,
                    image_src=image_src,
                    scarp_date=datetime.now(),
                )
                scraped_data.append(news_data)

        return scraped_data


def get_news_scraper() -> NewsScraper:
    return NewsScraper()
