#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_attributes(self):
        item = Place()
        self.assertTrue(hasattr(item, "city_id"))
        self.assertTrue(hasattr(item, "user_id"))
        self.assertTrue(hasattr(item, "name"))
        self.assertTrue(hasattr(item, "description"))
        self.assertTrue(hasattr(item, "number_rooms"))
        self.assertTrue(hasattr(item, "number_bathrooms"))
        self.assertTrue(hasattr(item, "max_guest"))
        self.assertTrue(hasattr(item, "price_by_night"))
        self.assertTrue(hasattr(item, "latitude"))
        self.assertTrue(hasattr(item, "longitude"))
        self.assertTrue(hasattr(item, "amenity_ids"))
        self.assertEqual(item.number_rooms, 0)
        self.assertEqual(item.latitude, 0.0)

if __name__ == '__main__':
    unittest.main()