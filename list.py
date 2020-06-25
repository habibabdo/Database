
import os

from Flask import flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# app.config['DATABASE_URL'] = "C:/Users/HD997/Database/"
# DATABASE_URL="postgres://localhost:5432/database"

engine = create_engine(os.getenv('//root:1234@ip:80, 443/salon '))

db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.executr('SELECT origin, destination,duration FROM flights').fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.distination} ,{flight.duration}  minutes.")


if __name__ == '__main':
    main()
