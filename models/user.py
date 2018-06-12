#!/usr/bin/python3
''' user module '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' User class '''
    def __init__(self):
        ''''
        initation of class User
        '''
        BaseModel.__init__(self)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
