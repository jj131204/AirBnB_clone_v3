#!/usr/bin/python3
""" Cities"""

from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/states/<state_id>/cities', methods=["GET"], strict_slashes=False)
def cities_(state_id):
    """ get states """

    list_ = []
    storage_ = storage.get(State, state_id)

    if not storage_:
        abort(404)

    for test in storage_.values():
        list_.append(test.to_dict())

    return jsonify(list_)

@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
def get_cities_(city_id):

    city = storage.get(City, city_id)

    if not city:
        """..."""
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=["DELETE"],
                 strict_slashes=False)
def Delete_city_(city_id):
    """ get states """

    city = storage.get(City, city_id)
    if not city:
        abort(404)

    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/states/<state_id>/cities', methods=["POST"], strict_slashes=False)
def Post_city_(state_id):

    state = storage.get(State, state_id)
    if not state:
        abort(404)

    """post state"""
    request_ = request.get_json()

    if not request_:
        abort(400, "Not a JSON")

    if 'name' not in request_:

        abort(400, "Missing name")

    new_ = City(**request_)
    new_.state_id = state_id
    storage.save()
    return make_response(jsonify(new_.to_dict()), 201)

@app_views.route('/cities/<city_id>', methods=["PUT"], strict_slashes=False)
def Put_city_(city_id):
    """put states"""

    request_ = request.get_json()

    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request_:
        abort(400, "Not a JSON")

    for key, value in request_.items():

        ignore = ["id", "created_at", "updated_at"]

        if key not in ignore:

            setattr(state, key, value)

    storage.save()

    return make_response(jsonify(city.to_dict()), 201)
