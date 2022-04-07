#!/usr/bin/python3
""" State Module for HBNB project """
from unittest import result
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """
            return the list of City objects from
            storage linked to the current State
            """
            rets = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    rets.append(city)
            return rets
