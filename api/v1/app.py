#!/usr/bin/python3
"""flask"""

from flask import Flask, render_template
from models import storage
from api.v1.views import app_views
from os import environ
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def teardown_app(self):
    """closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    """name"""
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
