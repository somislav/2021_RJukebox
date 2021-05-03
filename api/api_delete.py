import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify

from utilities.db_util import connect_execute_query


api_delete = Blueprint('api_delete', __name__)


# Routes go here
