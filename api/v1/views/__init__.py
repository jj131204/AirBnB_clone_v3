#!/usr/bin/python3
"""import Blueprint"""

from flask import Blueprint
from api.v1.views.index import *

""" Blueprint """
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
