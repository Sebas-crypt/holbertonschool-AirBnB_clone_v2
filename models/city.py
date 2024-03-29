#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> seba


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
=======
=======

"""
A module that defines the ORM class for City table
"""
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
>>>>>>> seba
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            'Place', backref='cities', cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
