#!/usr/bin/python3
""" Script to print all inserts State and City objects into
    the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
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
    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    my_session.add(state)
    my_session.commit()
    my_session.close()
