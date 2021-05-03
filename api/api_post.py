import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify

from utilities.db_util import connect_execute_query


api_post = Blueprint('api_post', __name__)


# Routes go here
