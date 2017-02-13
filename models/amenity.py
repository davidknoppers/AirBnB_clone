#!/usr/bin/python3
from models import *
"""
Basic Amenity subclass
All it really does is inherit using super()
More functionality in the future
"""


class Amenity(BaseModel):
    """
    Basic Amenity subclass
    All it really does is inherit using super()
    More functionality in the future
    """

    def __init__(self, *args, **kwargs):
        """
        Basic Amenity subclass
        All it really does is inherit using super()
        More functionality in the future
        """

        self.name = ""
        super().__init__(*args, **kwargs)
