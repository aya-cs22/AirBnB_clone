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

    def test_BaseModel_id(self):
        '''Testing id'''
        self.assertNotEqual(self.myinstance.id, self.B2.id)

    def test_init(self):
        '''Testing type of attributes'''

        self.assertEqual(type(self.myinstance.id), str)
        self.assertEqual(type(self.myinstance.created_at), datetime.datetime)
        self.assertEqual(type(self.myinstance.updated_at), datetime.datetime)

if __name__ == '__main__':
    unittest.main()
