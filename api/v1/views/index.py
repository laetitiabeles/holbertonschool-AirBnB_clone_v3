#!/usr/bin/python3

'''
Index for API routes
'''


from flask import jsonify
from api.v1.views import app_views


@app_views.route('status', methods=['GET'], strict_slashes=False)
def status():
    '''
    Return the status of API
    '''
    return jsonify({"status": "OK"})
