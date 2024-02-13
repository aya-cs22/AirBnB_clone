import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''A class for testing the BaseModel class.'''

    def setUp(self):
        '''A method for instanciation'''
        self.myinstance = BaseModel()

    def test_to_dict(self):
        '''Testing the to_dict method of the BaseModel class.'''
        my_model_dict = self.myinstance.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('_class_', my_model_dict)
        self.assertEqual(my_model_dict['_class_'], 'BaseModel')

    def test_save(self):
        '''Testing save method that updates the updated_at attr'''
        initial_update = self.myinstance.updated_at
        self.myinstance.save()
        self.assertNotEqual(initial_update, self.myinstance.updated_at)

if __name__ == '__main__':
    unittest.main()
