#!/usr/bin/python3
'''A module containign the base class
from which all other classes will inherit'''

import uuid
from datetime import datetime


class BaseModel:
    '''The baseModel class'''

    def __init__(self, *args, **kwargs):
        '''Initiation of the base class
        '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''Beautifying the printed output'''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Upadtes updated_at to current date time'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary representation of the instance'''
        # mydict = {}
        # for key, value in self.__dict__.items():
        #     if key == "created_at" or key == "updated_at":
        #         value = value.isoformat()
        #     mydict[key] = value
        # mydict['__class__'] = self.__class__.__name__
        # return mydict
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
