#!/usr/bin/python3
import json
import os
from models import *


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        serialized = {}
        for key in FileStorage.__objects.keys():
            serialized[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode='w') as MyFile:
            MyFile.write(json.dumps(serialized))

    def reload(self):
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as MyFile:
                FileStorage.__objects = {}
                temp = json.load(MyFile)
                for i in temp.keys():
                    class_ = temp[i].pop("__class__", None)
                    cr_at = temp[i]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[i]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(class_)(temp[i])
        except Exception as e:
            pass
