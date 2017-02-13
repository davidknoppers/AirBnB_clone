#!/usr/bin/python3
""" Test State Module """
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Unit Tests for Review Class """
    def setUp(self):
        """ Setup instances of the Review Class """
        self.gr8_review = Review()
        self.turrible_review = Review()
        self.turrible_review.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.gr8_review.id != self.turrible_review.id)
        self.assertFalse(hasattr(self.gr8_review, "updated_at"))
        self.assertTrue(hasattr(self.gr8_review, "place_id"))
        self.assertTrue(hasattr(self.turrible_review, "place_id"))
        self.assertTrue(hasattr(self.gr8_review, "user_id"))
        self.assertTrue(hasattr(self.turrible_review, "user_id"))
        self.assertTrue(hasattr(self.gr8_review, "text"))
        self.assertTrue(hasattr(self.turrible_review, "text"))
        self.assertTrue(self.gr8_review.created_at !=
                        self.turrible_review.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.gr8_review.created_at) is datetime.datetime)
        self.assertTrue(type(self.gr8_review.place_id) is str)
        self.assertTrue(type(self.gr8_review.user_id) is str)
        self.assertTrue(type(self.gr8_review.text) is str)
        a_json = self.gr8_review.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

    def test_save(self):
        """ Testing updating  """
        b_date = self.turrible_review.updated_at
        self.turrible_review.save()
        b_date2 = self.turrible_review.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
