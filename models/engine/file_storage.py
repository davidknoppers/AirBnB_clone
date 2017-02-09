#!/usr/bin/python3
import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        self.reload()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj is not None:
            FileStorage.__objects[obj.id] = obj.__dict__

    def save(self):
        serialized = {}
        for key in self.__objects.keys():
            serialized[key] = self.objects[key].to_json()
        with open(FileStorage.__file_path, mode='w+', encoding='utf-8') as MyFile:
            json.dump(serial, MyFile)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as MyFile:
                try:
                    obj = json.loads(MyFile)
                    for key in obj.keys():
                        Filestorage.__objects[key] = BaseModel(obj[key])
                except Exception as e:
                    print("Error storing json:", e)
        except Exception:
            pass
