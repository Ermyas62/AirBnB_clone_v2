#!/usr/bin/python3
"""This module instantiate object of class FileStorage"""
import os

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""Unique FileStorage or DBStorage instance for all the models.
"""
storage.reload()
