import json
import unittest
from lambda_api.app import predict, handler

class PredictorTests(unittest.TestCase):
    def test_short_distance(self):
        self.assertEqual(predict(2, 2)['prediction'], 'run')

    def test_long_distance(self):
        self.assertEqual(predict(3, 10)['prediction'], 'pass')

    def test_bad_down(self):
        with self.assertRaises(ValueError):
            predict(5, 2)

    def test_lambda_success(self):
        result = handler({'queryStringParameters': {'down': '2', 'distance': '9'}}, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(json.loads(result['body'])['prediction'], 'pass')

    def test_lambda_error(self):
        self.assertEqual(handler({'queryStringParameters': {'down': '0'}}, None)['statusCode'], 400)

if __name__ == '__main__':
    unittest.main()
