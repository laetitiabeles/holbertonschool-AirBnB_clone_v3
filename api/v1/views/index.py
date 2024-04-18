#!/usr/bin/python3

'''
Docstring for the module
'''


from flask import jsonify
from api.v1.views import app_views


@app_views.route('status', methods=['GET'])
def status():
    '''
    Return the status
    '''
    return jsonify({"status": "OK"})
