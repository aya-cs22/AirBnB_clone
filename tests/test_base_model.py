import unittest
from datetime import timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''A class for testing the BaseModel class.'''

    def setUp(self):
        '''A method for instanciation'''
        self.myinstance = BaseModel()
        
    def test_save(self):
       '''Testing save method that updates the updated_at attr'''
       initialUpdate = self.myinstance.updated_at
       self.myinstance.save()
       self.assertNotEqual(initialUpdate, self.myinstance.updated_at)
       self.assertTrue((self.myinstance.updated_at - self.myinstance.created_at) <= timedelta(seconds=1))

       """ test positional args """
       with self.assertRaises(TypeError):
            self.myinstance.save(7)

    def test_str(self):

        '''Testing the __str__ method of the BaseModel class.'''
        instance_str = str(self.myinstance)
        self.assertIn(self.myinstance.__class__.__name__, instance_str)
        self.assertIn(self.myinstance.id, instance_str)
        self.assertIn(str(self.myinstance.__dict__), instance_str)

if __name__ == '__main__':
    unittest.main()
