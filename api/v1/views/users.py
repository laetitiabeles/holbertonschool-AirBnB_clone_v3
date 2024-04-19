#!/usr/bin/python3
""" users module for the API """

# Import necessary Flask modules and classes
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.user import User


# GET all users
# ============================================================================


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])


# GET a user by ID
# ============================================================================


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


# DELETE a user by ID
# ============================================================================


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User by ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({})


# CREATE a new user
# ============================================================================


@app_views.route("/users", methods=["POST"], strict_slashes=False)
def post_user():
    """Creates a User"""
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    if "email" not in data:
        abort(400, "Missing email")
    if "password" not in data:
        abort(400, "Missing password")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


# UPDATE a user by ID
# ============================================================================


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def put_user(user_id):
    """Updates a User"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    for key, value in data.items():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
