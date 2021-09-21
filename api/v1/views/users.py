#!/usr/bin/python3
"""users
"""

from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users_():
    """ Retrieves a list of users """
    users = storage.all(User).values()
    list_ = []
    for user in users:
        list_.append(user.to_dict())
    return jsonify(list_)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_(user_id):
    """ Retrieves an user by id """
    user = storage.get(User, user_id)
    if not user:
        """if not user"""
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_users_(user_id):
    """ Deletes """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def post_users_():
    """ MOTHODS DELETE """

    request_ = request.get_json()

    if not request_:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    if "email" not in request_:
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if "password" not in request__:
        return make_response(jsonify({'error': 'Missing password'}), 400)
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_users_(user_id):
    """ Updates an user object by id """

    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    ignore = ['id', 'email', 'created_at', 'updated_at']

    for key, value in request_.items():
        if key not in key_ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
