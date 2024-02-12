#!/usr/bin/python3
'''A module containign the base class from which all other classes will inherit'''

import uuid
from datetime import datetime

class BaseModel:
    '''The baseModel class'''

    def __init__(self, id=None, created_at=None, updated_at=None):
        '''Initiation of the base class

        Args:
        id (str, optional): User unique ID. Defaults to a new UUID.
            created_at (datetime, optional): Time when the class
            was created. Defaults to the current datetime.
            updated_at (datetime, optional): Last update
            time. Defaults to the current datetime.
        '''

        self.id = str(uuid.uuid4())
        self.created_at =  datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''Beautifying the printed output'''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Upadtes updatedat to current date time'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary'''

        mydict = {}
        instances = ("id", "created_at", "updated_at")
        for key, value in self.__dict__.items():
            if key in instances and value is not None:
                key_formatted = key
                if key == "created_at" or key == "updated_at":
                    key_formatted = value.isoformat()
                mydict[key_formatted] = repr(value)
        mydict['__class__'] = repr(self.__class__.__name__)
        return mydict
