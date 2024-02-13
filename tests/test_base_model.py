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


if __name__ == '__main__':
    unittest.main()
