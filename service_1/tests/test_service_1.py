from application import app
from flask_testing import TestCase
from flask import url_for
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFront(TestBase):
    def test_get_front(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_text', text = 'Soul')
            m.get('http://service_3:5000/get_suffix', text = 'Badu')
            m.get('http://service_4:5000/genre', text = 'You could be an RNB artist')
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'You could be an RNB artist', response.data)
    
    def test_get_front_again(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_text', text = 'Young')
            m.get('http://service_3:5000/get_suffix', text = 'Money')
            m.get('http://service_4:5000/genre', text = 'You could be a Rap Artist')
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Potential Genre: You could be a Rap Artist', response.data)