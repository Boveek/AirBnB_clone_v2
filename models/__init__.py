#!/usr/bin/python3
"""This module initializes the storage variable based on the environment"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City


storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
classes = {
    'State': State,
    'City': City
}
