#!/usr/bin/python3
'''A module containign the base class
from which all other classes will inherit'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''The baseModel class'''

    def __init__(self, *args, **kwargs):
        '''Initiation of the base class
        '''

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.id = kwargs["id"]
            self.created_at = kwargs["created_at"]

    def __str__(self):
        '''Beautifying the printed output'''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Upadtes updated_at to current date time'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary representation of the instance'''
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict['__class__'] = self.__class__.__name__
        return mydict
