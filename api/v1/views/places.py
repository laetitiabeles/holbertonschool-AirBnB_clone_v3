#!/usr/bin/python3
""" places module for the API """

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User


# GET all places
# =============================================================================


@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
def get_places(city_id):
    """Retrieves the list of all Place objects"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])


# GET a place by ID
# =============================================================================


@app_views.route("/places/<place_id>", methods=["GET"], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


# DELETE a place by ID
# =============================================================================


@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({})


# CREATE a new place
# =============================================================================


@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def post_place(city_id):
    """Creates a Place"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    if "user_id" not in data:
        abort(400, "Missing user_id")
    user = storage.get(User, data["user_id"])
    if user is None:
        abort(404)
    if "name" not in data:
        abort(400, "Missing name")
    data["city_id"] = city_id
    place = Place(**data)
    place.save()
    return jsonify(place.to_dict()), 201


# UPDATE a place by ID
# ===========================================================================


@app_views.route("/places/<place_id>", methods=["PUT"], strict_slashes=False)
def put_place(place_id):
    """Updates a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    for key, value in data.items():
        if key not in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict())
