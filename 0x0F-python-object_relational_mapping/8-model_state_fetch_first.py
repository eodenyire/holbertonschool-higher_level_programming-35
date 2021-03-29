#!/usr/bin/python3
"""
Script that prints the first State object from the database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).order_by(State.id).first()
    if s_tate:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    # Close session
    session.close()
