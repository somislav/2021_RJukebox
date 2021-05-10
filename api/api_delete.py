import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify

from utilities.db_util import connect_execute_query


api_delete = Blueprint('api_delete', __name__)

"""
@api_delete.route('api/songs')
def delete_song(song)
    return _handle_request() #sta treba vracati?

def _handle_request(wanted_params: str, endpoint: str):
    logging.info(f"User requested delete of {endpoint}.")
    try:
        if invalid_parameters(wanted_params):
            logging.info("Bad parameter added to request.")
            return make_response(f"Bad parameter", 420)

        if invalid_param_value():
            logging.info("Bad parameter values added to request.")
            return make_response("Bad parameter value", 421)

        where_query = ''
        for param in wanted_params:
            if param == 'sort':
                continue

            if param in request.args:
                logging.info(f"User requested {param} to be {request.args.delete(param)}.")
                where_query += f"{' AND' if where_query else ''} {param}='{request.args.delete(param)}'"

        where_query = f" WHERE{where_query}" if where_query else ''

        values = [param for param in wanted_params if param != 'sort']
        values_str = ','.join(values)

        query = f"DELETE {values_str} FROM songs{where_query}"
        songs = connect_execute_query(query)

        query = f"DELETE {values_str} FROM users{where_query}"
        songs = connect_execute_query(query)

        return jsonify(response)
    except Exception as e:
        logging.error(f"Error happened while using /api/{endpoint} endpoint: {e}")
        return make_response('Could not get the results. Please try later.', 430)


def invalid_parameters(params):
    return any(arg not in params for arg in request.args)


def invalid_param_value():
    if 'genre' in request.args:
        if request.args.get('genre') not in genre_valid:
            return True
    if 'sort' in request.args:
        if request.args.get('sort') not in sort_valid:
            return True
    return False
    """