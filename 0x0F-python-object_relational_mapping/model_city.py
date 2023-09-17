#!/usr/bin/python3
"""city model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """ class that defines cities instance"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True,
                 autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
