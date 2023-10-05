import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        data = json.loads(response.data.decode('utf-8'))
    
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
