#!usr/bin/python3
'''A module to create a unique instance of FileStorage class'''

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload
