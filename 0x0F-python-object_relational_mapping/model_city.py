#!/usr/bin/python3
""" City table database representation
"""
from model_state import Base, State
from sqlalchemy import ForeignKey, Column, Integer, String


class City(Base):
    """ City table definition
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
