from flask import Flask, request, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
import requests
import json
import logging
from models import Weather, connect_db, db
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'postgresql:///forepast')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'ihaveasecret')

debug = DebugToolbarExtension(app)
connect_db(app)

API_BASE_URL = 'http://www.metaweather.com/api/location'

logger = logging.getLogger()


@app.route('/', methods=['GET'])
def homepage():
    """shows list of popular US locations
    with links to more information about each city"""
    """displays retrieval form"""
    """has button for retrieval"""
    """on submit requests information for city and selected date
    shows results on template page"""

    return render_template('display.html')

@app.route('/city', methods=['GET'])
def show_city():
    """shows details of city"""

    location = request.args.get('location')
    date = request.args.get('date')
    resp_city = requests.get(f"{API_BASE_URL}/search", params={'query': location, 'limit': 1})
    logger.info(type(resp_city))


    data = resp_city.json()

    location_name = data[0]['title']
    location_type = data[0]['location_type']
    location_woeid = data[0]['woeid']

    resp_weather = requests.get(f"{API_BASE_URL}/{location_woeid}/{date}")
    logger.info(type(resp_weather))
    data_weather = resp_weather.json()

    min_temp = data_weather[0]['min_temp'] * 9//5 + 32
    max_temp = data_weather[0]['max_temp'] * 9//5 + 32
    the_temp = data_weather[0]['the_temp'] * 9//5 + 32
    date = data_weather[0]['applicable_date']
    humidity = data_weather[0]['humidity']
    wind_speed = data_weather[0]['wind_speed']
    wind_direction = data_weather[0]['wind_direction']
    air_pressure = data_weather[0]['air_pressure']
    visibility = data_weather[0]['visibility']


    new_weather_info = Weather(woeid=location_woeid,
                               location = location_name,
                               location_type = location_type,
                               applicable_date = date,
                               wind_speed = wind_speed,
                               wind_direction = wind_direction,
                               the_temp = the_temp,
                               max_temp = max_temp,
                               min_temp = min_temp,
                               air_pressure = air_pressure,
                               humidity = humidity,
                               visibility = visibility)
    db.session.add(new_weather_info)
    db.session.commit()

    fahrenheit_min_temp = f'{min_temp * 9/5 + 32 }'
    print('#######################FARENHEIT TEMP############')
    print(fahrenheit_min_temp)


    return render_template('city_template.html',
        title = location_name,
        woeid = location_woeid,
        min_temp = min_temp,
        max_temp = max_temp,
        date = date,
        humidity = humidity,
        wind_speed = wind_speed,
        wind_direction = wind_direction,
        air_pressure = air_pressure,
        visibility = visibility)

@app.route('/', methods=['GET'])
def back_button():
    """goes back to previous page"""

    return render_template('display.html')
