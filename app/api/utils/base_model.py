from abc import ABC, abstractmethod
from ..utils.database_model import DatabaseModel


class Model(ABC, DatabaseModel):
    """ Base model class for objects """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def exists(self, key, value):
        pass

    @abstractmethod
    def where(self, key, value):
        pass

    @abstractmethod
    def delete(self, id):
        pass
