import unittest
import json
from flask import Flask
from app import app


class ControllersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_grid(self):
        data = {
            'size': 3,
            'values': '4,2,3,2,2,1,3,2,1'
        }
        response = self.app.post('/sun-spot-analyser-api/grid', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('id' in response_data)

    def test_get_scores(self):
        response = self.app.get('/sun-spot-analyser-api/scores?id=1')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertTrue('scores' in response_data)


if __name__ == '__main__':
    unittest.main()
