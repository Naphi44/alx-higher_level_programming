#!/usr/bin/python3
"""This script lists all State objects from the database hbtn_0e_6_usa
   Usage:  ./10-model_state_my_get.py   <mysql username> /
                                        <mysql password> /
                                        <database name> /
                                        <search name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    username, password, db, searchname = argv[1], argv[2], argv[3], argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        if (state.name == searchname):
            print("{}".format(state.id))
            exit(1)
        else:
            continue
    print("Not found")
