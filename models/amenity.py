#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Amenity Module

This Module inherits from BaseModel class.
Amenity Module contains the attributes to be assigned
to the Amenities of the places.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity Class
    Attributes:
        name (str): The Amenity name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
