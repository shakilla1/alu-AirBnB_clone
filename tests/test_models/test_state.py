#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_attributes(self):
        item = State()
        self.assertTrue(hasattr(item, "name"))
        self.assertEqual(item.name, "")


if __name__ == '__main__':
    unittest.main()
