import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import request
from classes.User import User

from utilities.db_util import connect_execute_query


api_post = Blueprint('api_post', __name__)


# Routes go here
@api_post.route('/api/user_import', methods=['POST'])
def user_import():
    try:
        name=request.args.get('name')
        password=request.args.get('password')
        user = User(name, password)
        user.input_user()
        return user.name
    except Exception as e:
        logging.exception(f"Exception [{e}]: while adding user")