import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''A class for testing the BaseModel class.'''

    def test_base_model_initialization(self):
        '''Tests that a BaseModel instance is initialized correctly.'''
        base_model_instance = BaseModel()
        self.assertIsInstance(base_model_instance, BaseModel)
        self.assertIsNotNone(base_model_instance.id)
        self.assertIsInstance(base_model_instance.created_at, datetime)
        self.assertIsInstance(base_model_instance.updated_at, datetime)

    def test_base_model_to_dict(self):
        '''Tests that the to_dict method returns the correct dictionary representation.'''
        base_model_instance = BaseModel()
        base_model_dict = base_model_instance.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
