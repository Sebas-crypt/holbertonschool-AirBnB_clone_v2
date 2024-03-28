#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """Getter for cities"""
            related_cities = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    related_cities.append(city)
            return related_cities
