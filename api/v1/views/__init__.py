#!/usr/bin/python3

'''
Initialize the blueprint
'''

# Importing Blueprint from Flask
from flask import Blueprint

# Creating a Blueprint named 'app_views' with URL prefix '/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing views from different modules
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
