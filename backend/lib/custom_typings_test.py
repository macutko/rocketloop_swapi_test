import unittest

from lib.custom_typings import URL


class CustomTypings(unittest.TestCase):

    def test_invalid_URL(self):
        with self.assertRaises(ValueError):
            URL("not url")

    def test_invalid_URL_2(self):
        with self.assertRaises(ValueError):
            URL("http://.com")

    def test_invalid_URL_3(self):
        with self.assertRaises(ValueError):
            URL("http:/localhost.com")

    def test_invalid_URL_(self):
        with self.assertRaises(ValueError):
            URL("http:/localhost")