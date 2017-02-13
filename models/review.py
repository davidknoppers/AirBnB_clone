#!/usr/bin/python3
from models import *
"""
Basic class
Inherits from BaseModel
Has some unique attributes
"""


class Review(BaseModel):
    """
    Basic class
    Inherits from BaseModel
    Has some unique attributes
    """
    def __init__(self, *args, **kwargs):
        """
        Basic class
        Inherits from BaseModel
        Has some unique attributes
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
