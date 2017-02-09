#!/usr/bin/python3
import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as MyFile:
            serialized = {}
            for key in FileStorage.__objects.keys():
                serialized[key] = FileStorage.__objects[key].to_json()
            print("saving file...")
            MyFile.write(json.dumps(serialized))

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as MyFile:
                    Filestorage.__objects = {}
                    obj = json.load(MyFile)
                    for key in obj.keys():
                        Filestorage.__objects[key] = BaseModel(obj[key])
        except Exception as e:
            print(e)
            pass
