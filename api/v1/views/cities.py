#!/usr/bin/python3
"""RestFul API actions Cities
"""

from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def city_(state_id):
    """ Retrieves list of all cities """
    list_ = []
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    for city in state.cities:
        list_.append(city.to_dict())
    return jsonify(list_)

@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
def get_city_id(city_id):
    """ Retrieves a specific city by id """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
u
def delete_city_(city_id):
    """ Deletes a city by id """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city_(state_id):
    """ Create a city and returns it with status code 201 """
    state = storage.get(State, state_id)

    request_ = request.get_json()

    if not state:
        abort(404)

    if not request_:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "name" not in request_:
        return make_response(jsonify({'error': 'Missing name'}), 400)

    new_ = City(**request_)
    new_.state_id = state_id
    new_.save()
    return make_response(jsonify(new_.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city_(city_id):
    """ updates a city object """
    city = storage.get(City, city_id)

    request_ = request.get_json()

    if not city:
        abort(404)
    if not request_:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    for key, value in request_.items():
        if key not in ignore:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
