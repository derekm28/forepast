from flask import Flask, request, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
import json
import logging
from location import Location, db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///forepast'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all

API_BASE_URL = 'http://www.metaweather.com/api/location'

logger = logging.getLogger()

#data = resp.json()

#converter = Converter()


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

    title = data[0]['title']
    print(title)
    woeid = data[0]['woeid']

    resp_weather = requests.get(f"{API_BASE_URL}/{woeid}/{date}")
    logger.info(type(resp_weather))
    data_weather = resp_weather.json()

    print('.........&&&&&&&&&.....')
    print(data_weather)
    print('.........&&&&&&.....')

    min_temp = data_weather[0]['min_temp']
    max_temp = data_weather[0]['max_temp']
    date = data_weather[0]['applicable_date']
    humidity = data_weather[0]['humidity']
    wind_speed = data_weather[0]['wind_speed']
    wind_direction = data_weather[0]['wind_direction']
    air_pressure = data_weather[0]['air_pressure']
    visibility = data_weather[0]['visibility']



    print('##############temp##########################')
    print(min_temp)
    print(max_temp)

    fahrenheit_min_temp = f'{min_temp * 9/5 + 32 }'
    print('#######################FARENHEIT TEMP############')
    print(fahrenheit_min_temp)


    return render_template('city_template.html',
        title = title,
        woeid = woeid,
        min_temp = min_temp,
        max_temp = max_temp,
        date = date,
        humidity = humidity,
        wind_speed = wind_speed,
        wind_direction = wind_direction,
        air_pressure = air_pressure,
        visibility = visibility)



@app.route('/city', methods = ['POST'])
def create_city():
    """inserts city search results data into db"""

    location = request.args.get('location')
    resp = requests.get(f"{API_BASE_URL}/search", params={'query': location, 'limit': 1})
    data = resp.json()
    city = data[0]['title']
    type = data[1]['location_type']
    woeid = data[2]['woeid']

    new_location = Location(city = city, type = type, woeid = woeid)

    db.session.add_all(new_location)
    db.session.commit()
