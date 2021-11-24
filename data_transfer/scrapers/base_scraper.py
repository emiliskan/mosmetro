import abc


class AbstractScraper(abc.ABC):

    @abc.abstractmethod
    def scrap(self):
        ...
