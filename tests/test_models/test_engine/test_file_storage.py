#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def tearDown(self):
        """Remove file.json after test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method"""
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)

    def test_new(self):
        """Test new method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        key = "BaseModel.{}".format(my_model.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        key = "BaseModel.{}".format(my_model.id)
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()