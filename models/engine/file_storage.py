#!usr/bin/python3
'''A module for serialization and deserialization'''

import json
import os

class FileStorage():
    '''A class that seialize and desrialize objects and files'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''A method that returns the dictionary of objects'''

        return FileStorage.__objects

    def new(self, obj):
        '''Save the object to __objects'''

        ObjCN = obj.__class__.__name__
        ObjKey = ObjCN + "." + obj.id
        FileStorage.__objects[ObjKey] = obj

    def save(self):
        '''serialize the dict of objs to json file'''
 
        dictionarToSer = {}
        for k, v in FileStorage.__objects.items():
            dictionarToSer[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as jf:
            json.dump(dictionarToSer, jf)
    
    def reload(self):
        from models.base_model import BaseModel
        '''deserializes the json file, if exists
        to objects'''

        if os.path.exists(FileStorage.__file_path):
            with open((FileStorage.__file_path), 'r') as f:
                
