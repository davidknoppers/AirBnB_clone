#!/usr/bin/python3
"""
User, inherits from BaseModel
"""
from models import *


class User(BaseModel):
    """
    User, inherits from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Uses super() to simplify inheritance for User
        """
        super().__init__(*args, **kwargs)
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
