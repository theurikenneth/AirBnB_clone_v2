#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""State Module

This Module inherits from BaseModel class.
State Module contains the attributes to be assigned
to the States.
"""

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """State Class

    Attributes:
        name (str): The State name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ Gets a list of all cities in state """
            return [city for city in models.storage.all(City).values()
                    if self.id == city.state_id]
