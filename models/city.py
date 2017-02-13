#!/usr/bin/python3
from models import *
"""
City is a basic class
Inherits some stuff and gets a name and id
Basically just calls super
"""


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        """
        Needs two unique attributes, inherits the rest
        """
        self.name = ""
        self.state_id = ""
        super().__init__(*args, **kwargs)
