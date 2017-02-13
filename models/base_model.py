#!usr/bin/python3
from datetime import datetime, date, time
import uuid
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        dict_flag = 0
        for arg in args:
            if type(arg) is dict:
                dict_flag = 1
                break
        if dict_flag == 1:
            args[0]['created_at'] = datetime.strptime(
                args[0]['created_at'], '%Y-%m-%d %H:%M:%S.%f')
            args[0]['updated_at'] = datetime.strptime(
                args[0]['updated_at'], '%Y-%m-%d %H:%M:%S.%f')
            self.__dict__ = args[0]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def my_number(self, my_number):
        self.my_number = my_number

    def name(self, name):
        self.name = name

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

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
