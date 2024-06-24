from app.repositories import ClientRepository
from app import cache
from tenacity import retry, stop_after_attempt, stop_after_delay

class ClientService:
    def __init__(self):
        self.__repo=ClientRepository()

    def find_by_id(self, client_id):
        client = cache.get(f'{client_id}')
        if client is None:
            client = self.__repo.find_by_id(client_id)
            cache.set(f'{client_id}', client, timeout = 50)
        return client
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def find_by_name(self, name):
        client = cache.get(f'{name}')
        if client is None:
            client = self.__repo.find_by_name(name)
            cache.set(f'{name}', client, timeout = 50)
        return client
    

    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def find_all(self):
        return self.__repo.find_all()

    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def update(self, client, client_id):
            client= self.__repo.update(client, client_id)
            cache.set(f'{client.id}', client, timeout = 50)
            return client
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def delete(self, client_id):
        return self.__repo.delete(client_id)
    
    @retry(stop=(stop_after_attempt(10) | stop_after_delay(5)))
    def create(self, client):
        client = self.__repo.create(client)
        cache.set(f'{client.id}', client, timeout = 50)
        return client
