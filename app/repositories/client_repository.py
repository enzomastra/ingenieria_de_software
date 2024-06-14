from app.models.client import Client
from app.repositories.base_repository import BaseRepository

class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)
        from app import db
        self.__model = Client
        self.__db = db
        
    def find_by_name(self, name) -> Client:
        return self.__db.session.query(self.__model).filter_by(name=name).first()
    
    def find_by_brand(self, brand) ->  Client:
        return self.__db.session.query(self.__model).filter_by(brand=brand).first()

    def update(self, entity: Client, id: int):
        try:
            existing_entity = self.__db.session.query(self.__model).get(id)
            if existing_entity:
                existing_entity.name = entity.name
                existing_entity.surname = entity.surname
                existing_entity.phone_number = entity.phone_number
                existing_entity.email = entity.email
                existing_entity.dni = entity.dni
                existing_entity.address = entity.address
                existing_entity.password = entity.password
                self.__db.session.commit()
                return existing_entity
            else:
                return None
        except Exception as e:
            self.__db.session.rollback()
            raise e
