#!/usr/bin/python3
'''defining a State'''
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    """class state creation"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
