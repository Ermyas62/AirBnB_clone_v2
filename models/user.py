#!/usr/bin/python3
"""module to define class User"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.temp import HBNB_TYPE_STORAGE, DB


class User(BaseModel, Base):
    """
    This class define user by various attributes
    """
    __tablename__ = 'users'
    if getenv(HBNB_TYPE_STORAGE) == DB:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
