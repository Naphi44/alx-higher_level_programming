#!/usr/bin/python3
"""This script lists all State objects from the database hbtn_0e_6_usa
   Usage:  ./7-model_state_fetch_all.py <mysql username> /
                                        <mysql password> /
                                        <database name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    username, password, db = argv[1], argv[2], argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
