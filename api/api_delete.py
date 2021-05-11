import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify

from utilities.db_util import connect_execute_query
from utilities.token_utilities import owner_token_required

from classes.Song import Song

api_delete = Blueprint('api_delete', __name__)


@api_delete.route('/api/songs',methods=['DELETE'])
def delete_song():
    return _handle_owner_token_request('song_name')


@owner_token_required
def _handle_owner_token_request(song_name: str):
    logging.info("DELETE: asking for token auth of the song owner.")
    return _handle_delete_request(song_name)

def handle_delete_request(song_name: str):
    try:
        logging.info(f"User requested delete of {song_name}.")
       
        if not _song_in_db():
            return make_response("Bad song_name value", 405)
    
        query = f"DELETE FROM songs where song_name={song_name}"
        songs = connect_execute_query(query)
        return jsonify(response)

    except Exception as e:
        logging.error(f"Error happened while using /api/songs endpoint: {e}")
        return make_response('Could not get the results. Please try later.', 430)


def _song_in_db(song_name:str) -> bool:
    query=f"SELECT song_name from song where song_name={song_name}"
    found = connect_execute_query(query)
    if found is None:
        logging.info("Song is not in the database.")
        return False
    return True