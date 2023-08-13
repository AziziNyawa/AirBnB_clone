#!/usr/bin/python3
"""Defines the User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attr:
        email (str): The email of the user to be used
        password (str): The password of the used by user
        first_name (str): The first of the user
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
