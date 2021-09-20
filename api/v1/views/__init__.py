#!/usr/bin/python3
"""import Blueprint"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

>>>>>>> 9ac88ab47ce9c7f31c7cf57907079a876e0d8063
from api.v1.views.index import *
from api.v1.views.states import *
