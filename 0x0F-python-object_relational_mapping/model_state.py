#!/usr/bin/python3
"""This script contains the class definition of a State
   and an instance Base = declarative_base()
   Usage: ./6-model_state.py <mysql username> \
                             <mysql password> \
                             <database name>
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Declarative mapping for `states` table

    Attributes:
        __tablename__ (str): name of MySQL table to store states
        id (sqlalchemy.int): state's id
        name (sqlalchemy.str): state's name
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
