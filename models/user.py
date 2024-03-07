#!/usr/bin/python3
"""This module defines the User class."""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """A class that represents a user."""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Set a password with md5 encryption."""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

# Optimise this test.