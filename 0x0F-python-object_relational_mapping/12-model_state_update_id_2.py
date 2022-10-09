#!/usr/bin/python3
""" Script that updates State objects
    in the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    username, password, db_name = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()
    state = my_session.query(State).filter(State.id == 2).one_or_none()
    if state is not None:
        state.name = "New Mexico"
        my_session.add(state)
        my_session.commit()
    my_session.close()
