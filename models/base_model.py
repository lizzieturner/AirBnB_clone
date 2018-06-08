#!/usr/bin/python3
''' module for BaseModel class '''
from datetime import datetime
import json
import uuid

class BaseModel:
    ''' BaseModel class '''
    def __init__(self):
        '''
        initation of basemodel
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        Return:
        string represntation fo object
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        ''' updates date for updated_at attribute '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns dictonary with all key values of instance '''
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return self.__dict__
