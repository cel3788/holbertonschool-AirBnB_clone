#!/usr/bin/python3
"""
This module contains the class BaseModel.
"""
import uuid
from datetime import datetime


class BaseModel():
    """This class defines all common attributes and methods for other classes.
    """
    class_name = "BaseModel"

    def __init__(self):
        """Initialisation of the attributes of the class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of instance."""
        return f"[{self.class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates instance attribute updated_at with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary of instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.class_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
