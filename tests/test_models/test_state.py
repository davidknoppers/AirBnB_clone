#!/usr/bin/python3
""" Test State Module """
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Unit Tests for State Class """
    def setUp(self):
        """ Setup instances of the State Class """
        self.PA = State()
        self.ME = State()
        self.ME.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.PA.id != self.ME.id)
        self.assertFalse(hasattr(self.PA, "updated_at"))
        self.assertTrue(hasattr(self.PA, "name"))
        self.assertTrue(hasattr(self.ME, "name"))
        self.assertTrue(self.PA.created_at != self.ME.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.PA.created_at) is datetime.datetime)
        self.assertTrue(type(self.PA.name) is str)
        a_json = self.PA.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Testing updating  """
        b_date = self.ME.updated_at
        self.ME.save()
        b_date2 = self.ME.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
