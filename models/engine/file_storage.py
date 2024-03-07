import json
import os

class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances."""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    serialized_objs = json.load(file)
                    for key, value in serialized_objs.items():
                        class_name, obj_id = key.split('.')
                        class_name = class_name.split('__')[-1]
                        cls = eval(class_name)
                        obj = cls(**value)
                        self.__objects[key] = obj
                except Exception as e:
                    print("Error loading objects from JSON:", e)
                    pass