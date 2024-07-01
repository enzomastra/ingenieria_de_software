import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app, db
from app.models import Client
from app.services import ClientService





class ClientTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client_service = ClientService()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    

        
    def create_entity(self):
        entity = Client(
            name='Client 1',
            surname='Client 1 Surname',
            phone_number='123456789',
            email='clientemail@gmail.com',
            dni='123456786',
            address='Client 1 Address',
            password='clientpassword'
        )
        self.client_service.create(entity)
        return entity
    
    def test_create_client(self):
        entity = self.create_entity()
        self.assertTrue(entity.id)

    def test_find_by_id_client(self):
        entity = self.create_entity()
        self.assertTrue(self.client_service.find_by_id(entity.id))

    def test_find_all_client(self):
        entity = self.create_entity()
        self.assertTrue(self.client_service.find_all())

    def test_update_client(self):
        entity = self.create_entity()
        entity.name = "Juanito"
        self.client_service.update(entity, entity.id)
        self.assertEqual(Client.query.get(entity.id).name, "Juanito")
    
    def test_delete_client(self):
        entity = self.create_entity()
        self.client_service.delete(entity.id)
        self.assertFalse(Client.query.get(entity.id))

if __name__ == '__main__':
    unittest.main()