from app.models.client import *
from app import db
from app.repositories.base_repository import BaseRepository
from app.config.database import db

class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)
        self.__model = Client

    def find_by_email(self, email) -> Client:
        return db.session.query(self.__model).filter_by(email=email).first()

    def create(self, entity: db.Model):
        existing_entity = self.find_by_email(entity.email)
        if existing_entity is not None:
            raise ValueError("Email is already registered")
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, entity: db.Model, id: int):
        try:
            existing_entity = db.session.query(self.__model).get(id)
            if existing_entity:
                existing_entity.name = entity.name
                existing_entity.surname = entity.surname
                existing_entity.phone_number = entity.phone_number
                existing_entity.email = entity.email
                existing_entity.dni = entity.dni
                existing_entity.address = entity.address
                existing_entity.password = entity.password
                db.session.commit()
                return existing_entity
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e