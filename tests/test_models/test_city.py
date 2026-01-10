#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_attributes(self):
        item = City()
        self.assertTrue(hasattr(item, "state_id"))
        self.assertTrue(hasattr(item, "name"))
        self.assertEqual(item.name, "")

if __name__ == '__main__':
    unittest.main()