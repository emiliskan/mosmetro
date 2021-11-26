import abc

from models.news_models import NewsModel


class AbstractNewsLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, data: list[NewsModel]) -> None:
        ...
