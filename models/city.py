#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""City Module

This Module inherits from BaseModel class.
City Module contains the attributes to be assigned
to the cities.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City Class

    Attributes:
        state_id (str): The UUID of the State the City is located
        name (str): The City name

    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
