#!usr/bin/python3
import uuid
import models
from datetime import datetime, date, time
"""
Base model for all other classes
Sets up attributes for other classes to inherit
Features basic information
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        creates a basemodel using setattr
        """
        if len(args) > 0:
            for i in args[0]:
                setattr(self, i, args[0][i])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def my_number(self, my_number):
        """
        simple setter for number
        """
        self.my_number = my_number

    def name(self, name):
        """
        simple setter for name
        """
        self.name = name

    def save(self):
        """
        calls filestorage to save stuff
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        returns string rep of an object
        """
        return "[{}] ({}) {}".format(type(self).
                                     __name__, self.id, self.__dict__)

    def to_json(self):
        """
        Shout out to Danton for the help
        converts objects to json for storage
        """
        temp = {}
        for i in self.__dict__.keys():
            if (isinstance(self.__dict__[i], datetime)):
                temp[i] = str(self.__dict__[i])
            else:
                temp[i] = self.__dict__[i]
        temp['__class__'] = self.__class__.__name__
        return(temp)
