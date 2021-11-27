import json

from flask import Flask, request

from models.news_model import NewsModel
from services.news import get_last_news

app = Flask(__name__)


@app.route('/news/', methods=['GET'])
def get_last_news_route():
    """
    Получение новостей за последние day дней

    day: int - количество дней от текущей даты за которое нужны новости
    limit: int - ограничение в количестве результатов
    offset: int - смещение для организации пагинации
    """

    day: int = int(request.args.get('day', 10))
    offset: int = int(request.args.get('offset', 0))
    limit: int = int(request.args.get('limit', 10))

    news: list[NewsModel] = get_last_news(day, offset, limit)
    return json.dumps([article.dict() for article in news], default=str)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
