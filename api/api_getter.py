import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import request

from utilities.db_util import connect_execute_query


api_getter = Blueprint('api_getter', __name__)

song_params = ['song_name', 'artist', 'genre', 'yt_link']


@api_getter.route('/api/songs')
def get_songs():
    logging.info("User requested list of songs.")
    try:
        if invalid_parameters():
            logging.info("Bad parameter added to request.")
            return make_response(f"Bad parameter", 420)

        where_query = ''
        for param in song_params:
            if param in request.args:
                logging.info(f"User requested {param} to be {request.args.get(param)}.")
                where_query += f"{' AND' if where_query else ''} {param}='{request.args.get(param)}'"

        where_query = f" WHERE{where_query}" if where_query else ''

        query = f"SELECT * FROM songs{where_query}"
        songs = connect_execute_query(query)
        response = [ { 'song_name': song[1], 'artist': song[2], 'genre': song[3], 'yt_link': song[4] } for song in songs ]

        return jsonify(response)
    except Exception as e:
        logging.error(f"Error happened while using /api/songs endpoint: {e}")
        return make_response('Could not get the results. Please try later.', 430)


def invalid_parameters():
    return any(arg not in song_params for arg in request.args)
