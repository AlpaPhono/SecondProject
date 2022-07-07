from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes


class TestBase(TestCase):
    def create_app(self):
        return app


class Testprefix(TestBase):
    @patch('application.routes.choice',return_value = "Young")
    def test_get_prefix(self,patched):
        response = self.client.get(url_for('get_text'))
        self.assert200(response)
        self.assertIn(b"Young",response.data)