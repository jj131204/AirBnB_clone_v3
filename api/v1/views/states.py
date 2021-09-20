#!/usr/bin/python3
"""from"""

from models.state import State
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request


@app_views.route('/states', methods=["GET"], strict_slashes=False)
def states_():
    """ get states """

    list_ = []
    storage_ = storage.all(State)


    for test in storage_.values():
        list_.append(test.to_dict())

    return jsonify(list_)


@app_views.route('/states/<state_id>', methods=["GET"], strict_slashes=False)
def get_states_(state_id=None):
    """ get states """

    states = storage.get(State, state_id)
    if states is None:
        """if not states:"""
        abort(404)

    return jsonify(states.to_dict())


@app_views.route('/states/<state_id>', methods=["DELETE"],
                 strict_slashes=False)
def Delete_states_(state_id):
    """ get states """

    state = storage.get(State, state_id)
    if not state:
        abort(404)

    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)

    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return make_response(jsonify({}), 200)
    return abort(404)


@app_views.route('/states', methods=["POST"], strict_slashes=False)
def Post_states_():
    """post state"""
    request_ = request.get_json()

    if not request_:
        abort(400, "Not a JSON")

    if 'name' not in request_:

        abort(400, "Missing name")

    new_ = State(**request_)
    storage.save()
    return make_response(jsonify(new_.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=["PUT"], strict_slashes=False)
def Put_states_(state_id):
    """put states"""

    request_ = request.get_json()

    state = storage.get(State, state_id)
    if not state:
        abort(404)

    if not request_:
        abort(400, "Not a JSON")

    for key, value in request_.items():

        ignore = ["id", "created_at", "updated_at"]

        if key not in ignore:

            setattr(state, key, value)

    storage.save()

    return make_response(jsonify(state.to_dict()), 201)
