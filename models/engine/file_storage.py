#!/usr/bin/python3
''' FileStorage module '''
import json
from models.base_model import BaseModel


class FileStorage:
    '''FileStorage class'''

    def __init__(self):
        '''
        initation of FileStorage class
        '''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''
        Return:
        the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in objects with key classname.id

        Args:
        object
        '''
        self.__objects.update({'{}.{}'.format
                               (obj.__class__.__name__, obj.id): obj})

    def save(self):
        '''
        serializes __objects to JSON file
        '''
        newdict = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:

            for k, v in self.__objects.items():
                newdict[k] = v.to_dict()

            json.dumps(newdict, f)

    def reload(self):
        '''
        deserializes the JSON file
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                self.__objects = json.load(f)
        except:
            pass
