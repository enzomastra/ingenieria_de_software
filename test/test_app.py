import requests
import unittest

class AppTestCase(unittest.TestCase):
    def test_app(self):
        url = "http://ms1.client.localhost/api/v1/"
        response = requests.get(url, verify=False)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()