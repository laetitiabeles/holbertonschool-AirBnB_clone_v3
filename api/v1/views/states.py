#!/usr/bin/python3

'''
States API routes
'''

from api.v1.views import app_views
from flask import abort
from flask import jsonify
from flask import request
from models import storage
from models.state import State


# GET all states
# ============================================================================

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    ''' Return all states '''
    states = storage.all(State)
    states = [state.to_dict() for state in states.values()]
    return jsonify(states)


# GET one state
# ============================================================================

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    ''' Return one state '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


# DELETE one state
# ============================================================================

@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state(state_id):
    ''' Delete one state '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({})


# POST one state
# ============================================================================

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    ''' Create one state '''
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)  # '**' unpacks the dictionary
    state.save()
    return jsonify(state.to_dict()), 201


# PUT one state
# ============================================================================

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    ''' Update one state '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
