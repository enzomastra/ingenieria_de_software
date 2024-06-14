from app.repositories import ClientRepository
from app import cache

class ClientService:
    def __init__(self):
        self.__repo=ClientRepository()

    def find_by_id(self, client_id):
        client = cache.get(f'{client_id}')
        if client is None:
            client = self.__repo.find_by_id(client_id)
            cache.set(f'{client_id}', client, timeout = 50)
        return client
    
    def find_by_name(self, name):
        client = cache.get(f'{name}')
        if client is None:
            client = self.__repo.find_by_name(name)
            cache.set(f'{name}', client, timeout = 50)
        return client
    
    def find_all(self):
        return self.__repo.find_all()

    def update(self, client, client_id):
            return self.__repo.update(client, client_id)
    
    def delete(self, client_id):
        return self.__repo.delete(client_id)
    
    def create(self, client):
        client = self.__repo.create(client)
        cache.set(f'{client.id}', client, timeout = 50)
        return client
