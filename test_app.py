import os
from app import app
import unittest


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        self.client = None

    def test_get(self):
        response = self.client.get('/api/v1/orders', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post('/api/v1/orders', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        response = self.client.put('/api/v1/orders', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        response = self.client.delete('/api/v1/orders', content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()