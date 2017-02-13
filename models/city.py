#!/usr/bin/python3
from models import *


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        """
        Needs two unique attributes, inherits the rest
        """
        self.name = ""
        self.state_id = ""
        super().__init__(*args, **kwargs)
