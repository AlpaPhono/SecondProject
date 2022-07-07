from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes


class TestBase(TestCase):
    def create_app(self):
        return app


class Testprefix(TestBase):
    def test_get_prefix(self):
        suffix = "Soul" 
        prefix = "Badu"
        name =(prefix)+(suffix)
        response = self.client.get(url_for('prize'),data=name)
        self.assert200(response)
        self.assertIn(b"You could be an RNB artist",response.data)
