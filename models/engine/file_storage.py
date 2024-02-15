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
        '''Save the object to __objects'''

        ObjCN = obj.__class__.__name__
        ObjKey = ObjCN + "." + obj.id
        self.__objects[ObjKey] = obj

    def save(self):
        from models.base_model import BaseModel
        '''serialize the dict of objs to json file'''
 
        dictionarToSer = {}
        for k, v in FileStorage.__objects.items():
            dictionarToSer[k] = v.to_dict()
        with open((self.__file_path + ".json"), 'w') as jf:
            json.dump(dictionarToSer, jf)
    
    def reload(self):
        '''deserializes the json file, if exists
        to objects'''

        if self.__file_path:
            with open((self.__file_path + ".json"), 'r') as f:
                FileStorage.__objects = json.load(f)

