from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


resp = requests.get('http://metaweather.com/api/location/search', params = {'term': '', 'limit': 1})

#data = resp.json()
