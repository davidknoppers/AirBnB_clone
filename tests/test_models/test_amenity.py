#!/usr/bin/python3
""" Testing the Amenity Subclass """
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ Testing the Amenity Subclass """
    def setUp(self):
        """ Create instances of the Amenity Class """
        self.clawfoot_tub = Amenity()
        self.free_nutella = Amenity()
        self.free_nutella.save()

    def test_setup(self):
        """ Make sure setup works normally"""
        self.assertTrue(self.clawfoot_tub.id != self.free_nutella.id)
        self.assertFalse(hasattr(self.clawfoot_tub, "updated_at"))
        self.assertTrue(hasattr(self.clawfoot_tub, "name"))
        self.assertTrue(hasattr(self.free_nutella, "name"))
        self.assertTrue(self.clawfoot_tub.created_at !=
                        self.free_nutella.created_at)

    def test_types(self):
        """ Testing types """
        self.assertTrue(type(self.clawfoot_tub.created_at) is
                        datetime.datetime)
        self.assertTrue(type(self.clawfoot_tub.name) is str)
        a_json = self.clawfoot_tub.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Testing updates"""
        b_date = self.free_nutella.updated_at
        self.free_nutella.save()
        b_date2 = self.free_nutella.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
