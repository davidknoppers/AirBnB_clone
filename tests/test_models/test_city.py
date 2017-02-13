#!/usr/bin/python3
""" Testing the City subclass"""
import unittest
from models.city import City
import datetime


class TestState(unittest.TestCase):
    """ Testing the City subclass"""
    def setUp(self):
        """ Make some cities"""
        self.SF = City()
        self.LA = City()
        self.LA.save()

    def test_setup(self):
        """ Test instance creation"""
        self.assertTrue(self.SF.id != self.LA.id)
        self.assertFalse(hasattr(self.SF, "updated_at"))
        self.assertTrue(hasattr(self.LA, "updated_at"))
        self.assertTrue(hasattr(self.SF, "name"))
        self.assertTrue(hasattr(self.LA, "name"))
        self.assertTrue(hasattr(self.SF, "state_id"))
        self.assertTrue(hasattr(self.LA, "state_id"))
        self.assertTrue(self.SF.created_at != self.LA.created_at)

    def test_types(self):
        """ Testing type functionality"""
        self.assertTrue(type(self.SF.created_at) is datetime.datetime)
        self.assertTrue(type(self.SF.name) is str)
        a_json = self.SF.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Testing updates"""
        b_date = self.LA.updated_at
        self.LA.save()
        b_date2 = self.LA.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
