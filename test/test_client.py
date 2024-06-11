import unittest
from flask import current_app
from app import create_app, db
from sqlalchemy import text
from app.models.client import Client
from app.services.client_services import ClientService

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client_service=ClientService()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()
        
    def test_create_user(self):
        Client.query.delete()
        client=Client(name="Test", surname="Testing", phone_number="123456", email="test@gmail.com", dni="123456", address="Test 22", password="123456")
        
        created_client=self.client_service.create(client)
        self.assertIsNotNone(created_client.id)
        self.assertEqual(created_client.name, "Test")
        self.assertEqual(created_client.surname, "Testing")
        self.assertEqual(created_client.phone_number, "123456")
        self.assertEqual(created_client.email, "test@gmail.com")
        self.assertEqual(created_client.dni, "123456")
        self.assertEqual(created_client.address, "Test 22")
    
    def test_update_user(self):
        Client.query.delete()
        client=Client(name="Test", surname="Testing", phone_number="123456", email="test@gmail.com", dni="123456", address="Test 22", password="123456")

        created_client=self.client_service.create(client)
        created_client.name="Test2"
        updated_client=self.client_service.update(created_client, created_client.id)
        self.assertEqual(client.name, "Test2")

    def test_delete_user(self):
        Client.query.delete()
        client=Client(name="Test", surname="Testing", phone_number="123456", email="test@gmail.com", dni="123456", address="Test 22", password="123456")
        
        created_client=self.client_service.create(client)
        self.client_service.delete(created_client.id)
        self.assertIsNone(Client.query.get(client.id))

    def test_find_user(self):
        Client.query.delete()
        client=Client(name="Test", surname="Testing", phone_number="123456", email="test@gmail.com", dni="123456", address="Test 22", password="123456")
        
        created_client=self.client_service.create(client)
        self.client_service.find_by_id(created_client.id)

    def test_find_all_users(self):
        Client.query.delete()
        client=Client(name="Test", surname="Testing", phone_number="123456", email="test@gmail.com", dni="123456", address="Test 22", password="123456")
        client2=Client(name="Test2", surname="Testing2", phone_number="1234567", email="test2@gmail.com", dni="123457", address="Test 23", password="1234567")

        created_client=self.client_service.create(client)
        created_client2=self.client_service.create(client2)
        self.assertEqual(len(self.client_service.find_all()), 2)


        