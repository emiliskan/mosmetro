from flask import Flask
from flask import request

from models.news_model import NewsModel
from services.news import get_last_news
from utils.routes import response_json_list

app = Flask(__name__)


@app.route('/news/', methods=['GET'])
@response_json_list
def get_last_news_route() -> list:
    day_count: int = int(request.args.get('day_count', 10))
    offset: int = int(request.args.get('offset', 0))
    limit: int = int(request.args.get('limit', 10))

    news: list[NewsModel] = get_last_news(day_count, offset, limit)
    return [item.dict() for item in news]


if __name__ == "__main__":
    app.run(host='0.0.0.0')
