#!/usr/bin/python3
"""Defines the Amenity class that inherits BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
        """Represent an amenity class.

        Attributes:
            name (str): The name of the amenity of format str
        """

        name = ""
