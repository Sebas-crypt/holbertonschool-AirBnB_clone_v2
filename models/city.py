#!/usr/bin/python3
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
    __tablename__ = 'cities'
    state_id = ""
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    places = relationship("Place", cascade="delete", backref="cities")
