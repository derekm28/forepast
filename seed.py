from models import db, connect_db
from location import Location
from app import app

#create all tables
db.drop_all()
db.create_all()


locations = [
    Location(city='New York', type='city', timezone='EST', woeid='2459115'),
    Location(city='San Francisco', type='city', timezone='', woeid='2487956'),
    Location(city='Washington, DC', type='city', timezone='EST', woeid='2514815'),
    Location(city='Miami, FL', type='city', timezone='EST', woeid='2450022'),
    Location(city='Atlanta, GA', type='city', timezone='EST', woeid='2357024'),
    Location(city='Houston, TX', type='city', timezone='EST', woeid='2424766'),
    Location(city='San Diego', type='city', timezone='EST', woeid='2487889'),
    Location(city='Las Vegas', type='city', timezone='EST', woeid='2436704')
]

db.session.add_all(locations)
db.session.commit()
