#!usr/bin/python3
import uuid
import models
from datetime import datetime, date, time

class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            for i in args[0]:
                setattr(self, i, args[0][i])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def my_number(self, my_number):
        self.my_number = my_number

    def name(self, name):
        self.name = name

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).
                                     __name__, self.id, self.__dict__)

    def to_json(self):
        """Shout out to Danton"""
        temp = {}
        for i in self.__dict__.keys():
            if (isinstance(self.__dict__[i], datetime)):
                temp[i] = str(self.__dict__[i])
            else:
                temp[i] = self.__dict__[i]
        temp['__class__'] = self.__class__.__name__
        return(temp)
