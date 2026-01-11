#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity"""

    def test_attributes(self):
        item = Amenity()
        self.assertTrue(hasattr(item, "name"))
        self.assertEqual(item.name, "")


if __name__ == "__main__":
    unittest.main()
