from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash

class Client(db.Model):
    __tablename__ = 'client'
    __id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column("name", db.String(50))
    __surname = db.Column("surname", db.String(50))
    __phone_number = db.Column("phone_number", db.String(50))
    __email = db.Column("email", db.String(50))
    __dni = db.Column("dni", db.String(50))
    __address = db.Column("address", db.String(50))
    __password = db.Column("password", db.String(255))


    def __init__(self, name, surname, phone_number, email, dni, address, password, id=None):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__phone_number = phone_number
        self.__email = email
        self.__dni = dni
        self.__address = address
        self.__password = generate_password_hash(password)

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def _id(self, id: int):
        self.__id = id

    @hybrid_property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @hybrid_property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @hybrid_property
    def phone_number(self) -> str:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    @hybrid_property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @hybrid_property
    def dni(self) -> str:
        return self.__dni

    @dni.setter
    def dni(self, dni: str):
        self.__dni = dni

    @hybrid_property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @hybrid_property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    def __repr__(self):
        return f"Client (id {self.__id}, {self.__name}, {self.__surname}, {self.__phone_number}, {self.__email}, {self.__dni}, {self.__address}, {self.__password})"

    def __eq__(self, o: object) -> bool:
        return self.__id == o.id and self.__name == o.name
