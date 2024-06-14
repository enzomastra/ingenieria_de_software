from abc import ABC, abstractmethod
from app import db
from app.models import Client

class Create(ABC):
    @abstractmethod
    def create(self, entity:Client):
        pass

class Read(ABC):
    @abstractmethod
    def find_by_id(self, id:int):
        pass

class Update(ABC):
    @abstractmethod
    def update(self, entity:Client, id:int):
        pass

class Delete(ABC):
    @abstractmethod
    def delete(self, entity:Client):
        pass