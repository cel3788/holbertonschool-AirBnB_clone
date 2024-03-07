
# models/__init__.py
"""
this module contains enry point to initialize data storage mechanisme
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()