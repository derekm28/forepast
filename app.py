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

    location = request.args.get('location')
    date = request.args.get('date')
    resp = requests.get(f"{API_BASE_URL}/search", params={'query': location, 'limit': 1})
    logger.info(type(resp))


    data = resp.json()
    print('.........########1#######.....')
    print(data)
    print('.........#########2#########.....')
    print(data[0]['title'])

    title = data[0]['title']



    # info = request.form
    # location = resp(data.title.woeid)
    # date = resp(data.applicable_date)



    #city = Location.query.get_or_404(id)

    #return jsonify(city=city.serialize())

    return render_template('city_template.html')



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
