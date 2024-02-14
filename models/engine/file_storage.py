#!usr/bin/python3
'''A module for serialization and deserialization'''

import json


class FileStorage():
    '''A class that seialize and desrialize objects and files'''

    __file_path = "file"
    __objects = {}

    def all(self):
        '''A method that returns the dictionary of objects'''

        return self.__objects

    def new(self, obj):
        from models.base_model import BaseModel
        '''Converts an object to a dictionary and saves it to
        __objects'''

        newDict = BaseModel.to_dict(obj)
        ObjCN = obj.__class__.__name__
        ObjKey = ObjCN + "." + str(newDict['id'])
        FileStorage.__objects[ObjKey] = newDict

    def save(self):
        '''serialize the dict of objs to json file'''

        with open((self.__file_path + ".json"), 'w') as jf:
            json.dump(self.__objects, jf)

    def reload(self):
        '''deserializes the json file, if exists
        to objects'''

        if self.__file_path:
            with open((self.__file_path + ".json"), 'r') as f:
                FileStorage.__objects = json.load(f)
