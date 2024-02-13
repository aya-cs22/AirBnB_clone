import unittest
from datetime import timedelta
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''A class for testing the BaseModel class.'''

    def setUp(self):
        '''A method for instanciation'''
        self.myinstance = BaseModel()
        self.B2 = BaseModel()
        
    def test_save(self):
       '''Testing save method that updates the updated_at attr'''
       initialUpdate = self.myinstance.updated_at
       self.myinstance.save()
       self.assertNotEqual(initialUpdate, self.myinstance.updated_at)
       self.assertTrue((self.myinstance.updated_at - self.myinstance.created_at) <= timedelta(seconds=1))

       """ Test positional args """
       with self.assertRaises(TypeError):
            self.myinstance.save(7)

<<<<<<< HEAD:tests/test_models/test_base_model.py
    def test_BaseModel_id(self):
        '''Testing id'''
        self.assertNotEqual(self.myinstance.id, self.B2.id)

    def test_init(self):
        '''Testing type of attributes'''

        self.assertEqual(type(self.myinstance.id), str)
        self.assertEqual(type(self.myinstance.created_at), datetime.datetime)
        self.assertEqual(type(self.myinstance.updated_at), datetime.datetime)
=======
    def test_str(self):

        '''Testing the __str__ method of the BaseModel class.'''
        instance_str = str(self.myinstance)
        self.assertIn(self.myinstance.__class__.__name__, instance_str)
        self.assertIn(self.myinstance.id, instance_str)
        self.assertIn(str(self.myinstance.__dict__), instance_str)
>>>>>>> 33807f5227859356398c3cd4889361582308b52b:tests/test_base_model.py

if __name__ == '__main__':
    unittest.main()
