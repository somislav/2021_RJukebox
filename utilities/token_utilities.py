from flask import request
from flask import jsonify
from flask import make_response

import jwt
import os
import logging

from utilities.db_util import connect_execute_query


def token_required(func):
    def decor(*args, **kwargs):
        secret = os.getenv('SECRET_KEY')

        if 'Authorization' not in request.headers:
            return make_response("Token auth is required for this endpoint.", 403)

        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.split(" ")[1] if auth_header else ""

        try:
            token = jwt.decode(auth_token, secret, algorithms=["HS256"])['token']
            token_query = f"SELECT * FROM users WHERE token='{token}'"
            result = connect_execute_query(token_query)

            if not result:
                return make_response("Invalid token.", 405)

            logging.info(f"User [{result[0][1]}] is authenticated to use this API Endpoint")
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error happened during authentication: [{e}]")
            return make_response("Invalid token.", 405)

    return decor
