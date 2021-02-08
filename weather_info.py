import flask_sqlalchemy from SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Location info API"""
resp = requests.get(
    'https://www.metaweather.com/api/location/search?query=',
    params={'title': '', limit 1}
)

data = resp.json()

class Preload_Location_Info_Table():
    """Process for loading db table with popular tourist cities information"""

    __tablename__ = 'weather_info'

    location = db.Column(db.String, primary_key=True, info={'label': 'City'})
    location_type = db.Column(db.String, nullable=False)
    applicable_date = db.Colum(db.Date, nullable=False)
    wind_speed = db.Column(db.FLOAT, nullable=True)
    wind_direction = db.Column(db.TEXT, nullable-True)
    (min|max|the)_temp = db.Column(db.INTEGER, nullable=False)
    air_pressure = db.Column(db.FLOAT, nullable=True)
    humidity = db.Column(db.FLOAT, nullable=False)
    visibility = db.Column(db.FLOAT, nullable=True)



    @classmethod
    def add_info_to_table(location_name, location_type, ):
        """inserts info into database table"""

        """Args: location_name, location_type

        Returns: true or false if details are added"""

        db.session.add(location_info)
        db.session.commit()
