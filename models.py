from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Weather(db.Model):
    """Weather Information Model"""

    __tablename__ = 'weather_info'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    woeid = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)
    location_type = db.Column(db.String, nullable=False)
    applicable_date = db.Column(db.Date, nullable=False)
    wind_speed = db.Column(db.FLOAT, nullable=True)
    wind_direction = db.Column(db.TEXT, nullable=True)
    the_temp = db.Column(db.INTEGER, nullable=True)
    max_temp = db.Column(db.INTEGER, nullable=True)
    min_temp = db.Column(db.INTEGER, nullable=True)
    air_pressure = db.Column(db.FLOAT, nullable=True)
    humidity = db.Column(db.FLOAT, nullable=True)
    visibility = db.Column(db.FLOAT, nullable=True)

    def __init__(self, woeid, location, location_type, applicable_date, wind_speed,\
                 wind_direction, the_temp, max_temp, min_temp, air_pressure, humidity, visibility):
        self.woeid = woeid
        self.location = location
        self.location_type = location_type
        self.applicable_date = applicable_date
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.the_temp = the_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.air_pressure = air_pressure
        self.humidity = humidity
        self.visibility = visibility

        db.create_all()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
