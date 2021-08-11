#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""User Module

This Module inherits from BaseModel class.
User Module contains the user information.

"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User Class
    Attributes:
        email (str): The User's email
        password (str): The User's password
        first_name (str): THe first name of the User
        last_name (str): The last name of the User
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    place = relationship("Place", backref="user",
                         cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete-orphan")
