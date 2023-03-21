import unittest
import json
from flask_testing import TestCase
from setup import app
from test import test_all_indicator_extraction, test_language_detect

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_language_detect(self):
        test_language_detect(self)

    def test_all_indicator(self):
        test_all_indicator_extraction(self)


if __name__ == '__main__':
    unittest.main()
