#!/usr/bin/python3
"""
the engine to store the information in json file!
"""
import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    """for storing info in a json file"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        FileStorage.__objects["{}.{}".format
                              (obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes the dictionary to the json file"""

        with open(FileStorage.__file_path, "w") as json_file:
            temp_dict = {}
            for key, value in FileStorage.__objects.items():
                temp_dict[key] = value.to_dict()
            json.dump(temp_dict, json_file)

    def reload(self):
        """deserializes the json file to __objects"""

        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                temp_dict = json.load(json_file)
                for key, value in temp_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        else:
            pass
