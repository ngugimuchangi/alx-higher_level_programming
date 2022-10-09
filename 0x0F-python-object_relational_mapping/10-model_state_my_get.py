#!/usr/bin/python3
""" Script that fetches State objects with the letter 'a'
    from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    username, password, db_name, search = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()
    state = my_session.query(State).filter(State.name == search).one_or_none()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    my_session.close()
