import abc

from models.news_models import NewsModel


class NewsLoaderAbstract(abc.ABC):

    @abc.abstractmethod
    def load(self, data: list[NewsModel]) -> None:
        ...
