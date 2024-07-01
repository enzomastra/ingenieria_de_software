import requests
import unittest
from dotenv import load_dotenv
import os

load_dotenv()
TEST_APP_URL = os.getenv('TEST_APP_URL')

class AppTestCase(unittest.TestCase):
    def test_app(self):
        url = f"{TEST_APP_URL}"
        response = requests.get(url, verify=False)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()