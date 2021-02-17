from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Location(db.Model):
    """Process for loading db with popular tourist cities"""

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(db.String, nullable=False)
    timezone = db.Column(db.TEXT, nullable=False)
    woeid = db.Column(db.INTEGER, nullable=False)

    # def serialize():
    #     return{
    #         'id' = self.id,
    #         'city' = self.city,
    #         'type' = self.type,
    #         'timezone' = self.timezone,
    #         'woeid' = self.woeid
    #     }

    def __repr__(self):
        return f'<Location {self.id} location={self.location} type={self.location_type} timezone={self.timezone} woeid={self.woeid}'


    @classmethod
    def get_location(cls, location):
        """request info for location,

        Args: location_name

        Returns: location object"""

        try:
           #create location info object
            city = data.title
            location_type = data.type
            time = data.time
            timezone = data.timezone

            return data(
                title,
                type,
                latt_long,
                time,
                timezone
            )

        except:
            return False



    @classmethod
    def add_info_to_locations_table(location_name, location_type):
        """inserts info into db"""

        """Args: location_name, location_type

        Returns: true or false if details are added"""

        db.session.add(location_info)
        db.session.commit()
