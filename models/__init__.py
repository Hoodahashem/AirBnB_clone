#!/usr/bin/python3
"""importing the engine and reloading it!"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
