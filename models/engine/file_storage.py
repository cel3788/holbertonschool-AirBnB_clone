#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects in the storage."""
        return FileStorage.__objects

    def new(self, obj):
        """Add the object to the current database."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save the current database to the JSON file."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Reload the current database from the JSON file."""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
