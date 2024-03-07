from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(TestCase):
    """Test cases for the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up method to initialize class-level objects for testing"""
        cls.obj = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Tear down method to clean up class-level resources after all tests"""
        del cls.obj
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test case to check if instance is created successfully"""
        self.assertIsInstance(self.obj, BaseModel)
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_str_representation(self):
        """Test case to check string representation of instance"""
        expected_str = "[BaseModel] ({}) {}".format(self.obj.id, self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_str)

    def test_save_method(self):
        """Test case to check if save method updates updated_at"""
        previous_updated_at = self.obj.updated_at
        self.obj.save()
        self.assertNotEqual(previous_updated_at, self.obj.updated_at)

    def test_to_dict_method(self):
        """Test case to check if to_dict method returns correct dictionary"""
        obj_dict = self.obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], "BaseModel")
        self.assertEqual(obj_dict['created_at'], self.obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.obj.updated_at.isoformat())

    def test_from_dict_method(self):
        """Test case to check if object is created from dictionary"""
        obj_dict = self.obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(self.obj.id, new_obj.id)
        self.assertEqual(self.obj.created_at, new_obj.created_at)
        self.assertEqual(self.obj.updated_at, new_obj.updated_at)

if __name__ == "__main__":
    unittest.main()