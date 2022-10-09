#!/usr/bin/python3
""" Script to print all City objects from
    the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    username, password, db_name = argv[1:]
    engine = create_engine("mysql+mysqldb://{}:{}:@localhost/{}".format(
                            username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()
    for state, city in my_session.query(State, City).\
            filter(State.id == City.state_id).\
            order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    my_session.close()
