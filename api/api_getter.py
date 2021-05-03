import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify

from utilities.db_util import connect_execute_query


api_getter = Blueprint('api_getter', __name__)


@api_getter.route('/api/songs')
def get_songs():
    logging.info("User requested list of all songs.")
    try:
        query = "SELECT * FROM songs"
        songs = connect_execute_query(query)
        response = [ { 'song_name': song[1], 'artist': song[2], 'genre': song[3], 'yt_link': song[4] } for song in songs ]

        return jsonify(response)
    except Exception as e:
        logging.error(f"Error happened while using /api/songs endpoint: {e}")
        return make_response('Could not get the results. Please try later.', 430)
