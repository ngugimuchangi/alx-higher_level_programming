#!/usr/bin/python3
""" State class definition file
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ State class representation """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")
