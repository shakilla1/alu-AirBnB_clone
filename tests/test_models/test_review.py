#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attributes(self):
        item = Review()
        self.assertTrue(hasattr(item, "place_id"))
        self.assertTrue(hasattr(item, "user_id"))
        self.assertTrue(hasattr(item, "text"))
        self.assertEqual(item.text, "")

if __name__ == '__main__':
    unittest.main()