#!/usr/bin/python3
from models import *


class Place(BaseModel):
    def __init__(self, *args, **kwargs):
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
