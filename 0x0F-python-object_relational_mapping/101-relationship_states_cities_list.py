#!/usr/bin/python3
""" Script to list all States the database
    hbtn_0e_100_usa and their respective cities
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
    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    my_session.close()
