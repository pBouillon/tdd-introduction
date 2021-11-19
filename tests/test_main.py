import unittest

from app.main import APP_NAME, greeting_message


class TestMain(unittest.TestCase):

    def is_app_name_in_greeting_message(self):
        self.assertIn(APP_NAME, greeting_message())
