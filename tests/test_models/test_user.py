#!/usr/bin/python3
""" Test State Module """
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """ Unit Tests for User Class """
    def setUp(self):
        """ Setup instances of the User Class """
        self.prof_G = User()
        self.ju = User()
        self.ju.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.prof_G.id != self.ju.id)
        self.assertFalse(hasattr(self.prof_G, "updated_at"))
        self.assertTrue(hasattr(self.prof_G, "email"))
        self.assertTrue(hasattr(self.ju, "email"))
        self.assertTrue(hasattr(self.prof_G, "password"))
        self.assertTrue(hasattr(self.ju, "password"))
        self.assertTrue(hasattr(self.prof_G, "first_name"))
        self.assertTrue(hasattr(self.ju, "first_name"))
        self.assertTrue(hasattr(self.prof_G, "last_name"))
        self.assertTrue(hasattr(self.ju, "last_name"))
        self.assertTrue(self.prof_G.created_at != self.ju.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.prof_G.created_at) is datetime.datetime)
        self.assertTrue(type(self.prof_G.first_name) is str)
        self.assertTrue(type(self.prof_G.email) is str)
        self.assertTrue(type(self.prof_G.last_name) is str)
        self.assertTrue(type(self.prof_G.password) is str)
        a_json = self.prof_G.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Testing updating  """
        b_date = self.ju.updated_at
        self.ju.save()
        b_date2 = self.ju.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
