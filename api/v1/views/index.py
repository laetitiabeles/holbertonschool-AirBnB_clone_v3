#!/usr/bin/python3

'''
Index for API routes
'''


from flask import jsonify
from api.v1.views import app_views
from models import storage
from models import Amenity, City, Place, Review, State, User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    '''
    Return the status of API
    '''
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ stats of API"""
    object_count = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(object_count)
