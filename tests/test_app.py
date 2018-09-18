from api.views import app
import unittest

class AppTestCase(unittest.TestCase):
    def test_get(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/orders', content_type='')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/orders', content_type='')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        tester = app.test_client(self)
        response = tester.put('/api/v1/orders/<int:orderId>', content_type='')
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete('/api/v1/orders/<int:orderId>', content_type='')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()