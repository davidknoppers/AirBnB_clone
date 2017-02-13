#!/usr/bin/python3
"""
Filestorage contains all the functionality for file i/o
This functionality could be in base_model but we've split it up for learning
Reload is currently broken :((
"""
import json
import os
from datetime import *
from models import *


class FileStorage:
    """
    saves, prints, reloads, and makes new objects
    should work for all calls, direct or by object
    employs json serialization/deserialization
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        print all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        make a new object
        """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """
        save an instance
        """
        serialized = {}
        for key in FileStorage.__objects.keys():
            serialized[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode='w') as MyFile:
            MyFile.write(json.dumps(serialized))

    def reload(self):
        """
        load the json file, in theory
        """
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
                    FileStorage.__objects[i] = eval(class_)(temp[i])
        except Exception as e:
            pass
