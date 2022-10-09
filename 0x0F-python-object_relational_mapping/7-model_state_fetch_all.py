#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    username, passwrd, db_name = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           username, passwrd, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()
    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    my_session.close()
