#!/usr/bin/python3
""" Test the Place subclass"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """ Unit Tests for Place subclass """
    def setUp(self):
        """ Make some places """
        self.memphis = Place()
        self.napa = Place()
        self.napa.save()

    def test_setup(self):
        """ Testing instance creation"""
        self.assertTrue(self.memphis.id != self.napa.id)
        self.assertFalse(hasattr(self.memphis, "updated_at"))
        self.assertTrue(hasattr(self.napa, "updated_at"))
        self.assertTrue(hasattr(self.memphis, "name"))
        self.assertTrue(hasattr(self.napa, "name"))
        self.assertTrue(hasattr(self.memphis, "user_id"))
        self.assertTrue(hasattr(self.napa, "user_id"))
        self.assertTrue(hasattr(self.memphis, "city_id"))
        self.assertTrue(hasattr(self.napa, "city_id"))
        self.assertTrue(hasattr(self.memphis, "description"))
        self.assertTrue(hasattr(self.napa, "description"))
        self.assertTrue(hasattr(self.memphis, "number_rooms"))
        self.assertTrue(hasattr(self.napa, "number_rooms"))
        self.assertTrue(hasattr(self.memphis, "number_bathrooms"))
        self.assertTrue(hasattr(self.napa, "number_bathrooms"))
        self.assertTrue(hasattr(self.memphis, "max_guest"))
        self.assertTrue(hasattr(self.napa, "max_guest"))
        self.assertTrue(hasattr(self.memphis, "price_by_night"))
        self.assertTrue(hasattr(self.napa, "price_by_night"))
        self.assertTrue(hasattr(self.memphis, "latitude"))
        self.assertTrue(hasattr(self.napa, "longitude"))
        self.assertTrue(hasattr(self.memphis, "amenities"))
        self.assertTrue(hasattr(self.napa, "amenities"))
        self.assertTrue(self.memphis.created_at != self.napa.created_at)

    def test_types(self):
        """ Testing types """
        self.assertTrue(type(self.memphis.created_at) is datetime.datetime)
        self.assertTrue(type(self.memphis.name) is str)
        self.assertTrue(type(self.memphis.number_rooms) is int)
        self.assertTrue(type(self.memphis.number_bathrooms) is int)
        self.assertTrue(type(self.memphis.max_guest) is int)
        self.assertTrue(type(self.memphis.price_by_night) is int)
        self.assertTrue(type(self.memphis.latitude) is float)
        self.assertTrue(type(self.memphis.longitude) is float)
        self.assertTrue(type(self.memphis.amenities) is list)
        a_json = self.memphis.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Testing updating  """
        update_time_1 = self.napa.updated_at
        self.napa.save()
        update_time_2 = self.napa.updated_at
        self.assertTrue(update_time_1 != update_time_2)

if __name__ == '__main__':
    unittest.main()
