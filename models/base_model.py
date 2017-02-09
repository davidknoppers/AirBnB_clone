#!usr/bin/python3
import datetime, uuid
from models.engine.file_storage import FileStorage

storage=FileStorage()

class BaseModel:
    def __init__(self, *args, **kwargs):
        for i in args:
            if type(i) is dict:
                i[created_at] = datetime.strptime(arg[created_at])
                i[updated_at] = datetime.strptime(arg[updated_at])
                self.__dict__ = i
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.datetime(now)
                storage.new(self)
    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()
    def __str__(self):
        return "[{}] ({}) {}".format(__name__, str(self.id), self.__dict__)
    def to_json(self):
        temp = self.__dict__.copy()
        temp["__class__"] = type(self).__name__
        return temp
