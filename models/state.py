#!/usr/bin/python3
"""Defines the state class that inherits from the BaseModel"""
from models.base_model import BaseModel

class State(BaseModel):
    """Represtation of the State Class

    Attrib:
        name (str): An empty str for the name of state
    """

    name = ""
