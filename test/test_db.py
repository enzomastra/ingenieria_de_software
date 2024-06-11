import unittest
from flask import current_app
from app import create_app, db
from sqlalchemy import text

class DbTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
    def tearDown(self):
        db.session.remove()
        self.app_context.pop()
        
    def test_db_connection(self):
        connection, = db.session.query(text("'Hello World'")).one()
        self.assertEqual(connection, "Hello World")

if __name__ == '__main__':
    unittest.main()