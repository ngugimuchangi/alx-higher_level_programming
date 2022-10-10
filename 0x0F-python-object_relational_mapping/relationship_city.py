#!/usr/bin/python3
""" City table database representation
"""
from relationship_state import Base, State
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    """ City table definition
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
