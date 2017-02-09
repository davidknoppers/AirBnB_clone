#!/usr/bin/python3
import json, os

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
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as MyFile:
            MyFile.write(json.dumps(serialized))

    def reload(self):
        from models.base_model import BaseModel
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, mode="r", encoding="utf-8") as MyFile:
                    obj = json.load(MyFile)
                    for key in obj.keys():
                        FileStorage.__objects[key] = BaseModel(obj[key])
            except Exception as e:
                pass
