import abc


class AbstractLoader(abc.ABC):

    @abc.abstractmethod
    def load(self, data: list) -> None:
        ...
