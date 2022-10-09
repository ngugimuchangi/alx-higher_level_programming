#!/usr/bin/python3
""" Script that deletes State objects
    from the database hbtn_0e_6_usa
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
    for state in my_session.query(State).filter(State.name.like("%a%")):
        my_session.delete(state)
    my_session.commit()
    my_session.close()
