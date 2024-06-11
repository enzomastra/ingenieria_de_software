from app.repositories import ClientRepository

class ClientService:
    def __init__(self):
        self.__repo=ClientRepository()

    def find_by_id(self, client_id):
        return self.__repo.find_by_id(client_id)
    
    def find_by_email(self, email):
        return self.__repo.find_by_email(email)
    
    def find_all(self):
        return self.__repo.find_all()
    
    def update(self, client, client_id):
        return self.__repo.update(client, client_id)
    
    def delete(self, client_id):
        return self.__repo.delete(client_id)
    
    def create(self, client):
        return self.__repo.create(client)