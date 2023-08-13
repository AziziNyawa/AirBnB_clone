#!/usr/bin/python3
"""Defines the Class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of the City Class

    Attr:
        state_id (str): The states id
        name: The name of the city in str format
    """

    state_id = ""
    name = ""
