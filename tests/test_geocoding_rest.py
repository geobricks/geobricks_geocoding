import json
import unittest
from flask import Flask
from geobricks_geocoding.rest.geocoding_rest import app


class GeobricksTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(app, url_prefix='/geocoding')
        self.tester = self.app.test_client(self)

    def test_discovery(self):
        response = self.tester.get('/geocoding/discovery/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(out['title'], 'Geocoding service')

    def test_find_geocoding(self):
        response = self.tester.get('/geocoding/place/Rome', content_type='application/json')
        location = json.loads(response.data)
        self.assertEqual(location, [[41.8933439, 12.4830718]])