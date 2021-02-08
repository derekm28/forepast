from flask import Flask, request, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db
import requests
import json
#from location import Location

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///forepast'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all

API_BASE_URL = requests.get('http://metaweather.com/api/location')

#data = resp.json()

#converter = Converter()


@app.route('/home', methods=['GET'])
def homepage():
    """shows list of popular US locations
    with links to more information about each city"""
    """displays retrieval form"""
    """has button for retrieval"""
    """on submit requests information for city and selected date
    shows results on template page"""

    #location = Location.query.all(location_id)
    return render_template('display.html')

@app.route('/city', methods=['GET'])
def show_city():
    """shows details of city"""

    location = request.args['location']
    date = request.args['date']
    resp = requests.get(f"{API_BASE_URL}/search", params={'term': 'location', 'limit': 1})
    data = resp.json()
    title = data.title()


    # info = request.form
    # location = resp[data.title.woeid]
    # date = resp[data.applicable_date]



    #city = Location.query.get_or_404(id)

    #return jsonify(city=city.serialize())

    return render_template('city_template.html', location = location, date = date, data = data)


@app.route('/city', methods = ['POST'])
def create_city(title):
    """inserts city search results data into db"""

    location = request.args['location']
    date = request.args['date']
    resp = requests.get(f"{API_BASE_URL}/search", params={'term': 'location', 'limit': 1})
    data = resp.json()
    title = data.title()

    #search_res = (title=)



@app.route('/city', methods=['GET'])
def display_weather_info():
    """displays searched weather information at bottom of form"""

    # requests values from form
    #location =
    location = request.form["name"]
    date = request.form["date"]

    new_location = Location(location=city, date=applicable_date)
    db.session.add(new_location)
    db.session.commit()

    return render_template('city_template', location=location)
