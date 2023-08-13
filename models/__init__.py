#!/usr/bin/python3
"""__init__method for models director"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
