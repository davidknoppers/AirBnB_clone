#!/usr/bin/python3
from models import *
"""
Basic class
Inherits from basemodel and adds a ton of attributes
Doesn't do much yet
"""


class Place(BaseModel):
    """
    Basic class
    Inherits from basemodel and adds a ton of attributes
    Doesn't do much yet
    """
    def __init__(self, *args, **kwargs):
        """
        Basic class
        Inherits from basemodel and adds a ton of attributes
        Doesn't do much yet
        """
        super().__init__()
        self.amenities = [""]
        self.city_id = ""
        self.description = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.max_guest = 0
        self.name = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.price_by_night = 0
        self.number_rooms = 0
        self.user_id = ""
