import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import request

from utilities.db_util import connect_execute_query
from utilities.token_utilities import token_required


api_getter = Blueprint('api_getter', __name__)

song_params = ['song_name', 'artist', 'genre', 'yt_link']
vote_params = ['sort', 'song_name', 'artist', 'genre', 'votes']

genre_valid = ['Rock', 'HipHop', 'Metal', 'Pop', 'RnB']
sort_valid = ['asc', 'desc']


@api_getter.route('/api/songs')
def get_songs():
    return _handle_request(song_params, 'songs')


@api_getter.route('/api/votes')
def get_votes():
    return _handle_request(vote_params, 'votes')


@api_getter.route('/api/votes/top/<int:count>')
def get_top_votes(count: int):
    return _handle_request(vote_params, 'votes', count)


@token_required
def _handle_request(wanted_params: list, endpoint: str, top_count: int = 0):
    logging.info(f"User requested list of {endpoint}.")
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
                logging.info(f"User requested {param} to be {request.args.get(param)}.")
                where_query += f"{' AND' if where_query else ''} {param}='{request.args.get(param)}'"

        where_query = f" WHERE{where_query}" if where_query else ''

        values = [param for param in wanted_params if param != 'sort']
        values_str = ','.join(values)

        query = f"SELECT {values_str} FROM songs{where_query}"
        songs = connect_execute_query(query)

        response = [ dict(zip(values, song)) for song in songs ]

        sort_desc = 'sort' in request.args and request.args.get('sort') == 'desc'

        logging.info(f"Results will be sorted in {'descending' if sort_desc else 'ascending'} order")
        response = sorted(response, key=lambda k: k['votes'], reverse=sort_desc)

        if top_count != 0:
            logging.info(f"User requested first {top_count} results.")
            response = response[-top_count:] if sort_desc else response[:top_count]

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
