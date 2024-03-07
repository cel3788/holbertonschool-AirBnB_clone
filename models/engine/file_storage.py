import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objs = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    json_data = json.load(file)
                    for key, value in json_data.items():
                        class_name, obj_id = key.split('.')
                        class_name = class_name.split('__')[-1]
                        cls = eval(class_name)
                        obj = cls(**value)
                        self.__objects[key] = obj
                except Exception as e:
                    print("Error loading objects from JSON:", e)
                    pass
