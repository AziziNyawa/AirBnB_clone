#!/usr/bin/python3
"""Defines the place class and inherits from BaseModel"""
from models.base_model import BaseModel

class Place(BaseModel):
    """ Represents the Place class and has the following:
    Attr:
        city_id: The city id
        user_id: The user identification
        name: The name of the place  its located
        description (str): The full description of the place
        number_rooms: The number of available rooms
        number of bathrooms: available to accommodate the users
        max_guest: Type init and maximu guest
        price_by_night: The prices per night
        latitude: Float type of the place
        longitude: The longitude of the place
        amenity_ids : A list of amentity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
