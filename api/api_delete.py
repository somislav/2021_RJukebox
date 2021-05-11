import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import request

from utilities.db_util import connect_execute_query
from utilities.token_utilities import owner_token_required

from classes.Song import Song

api_delete = Blueprint('api_delete', __name__)

valid_params=['song_name','artist']

@api_delete.route('/api/songs',methods=['DELETE'])
def delete_song():
    if not all(param in valid_params for param in request.args):
        return make_response("Invalid parameter(s)",420)
    song_name=request.args.get('song_name')
    artist=request.args.get('artist')
    return _handle_delete_request(song_name,artist)


@owner_token_required
def _handle_delete_request(song_name: str,artist:str):
    try:
        logging.info(f"User requested delete of {song_name}.")
       
        if not _song_in_db(song_name,artist):
            return make_response("Bad song_name value", 405)
    
        query = f"DELETE FROM songs where song_name='{song_name}' and artist='{artist}'"
        songs = connect_execute_query(query)
        return make_response("Song is successfully deleted from database.")

    except Exception as e:
        logging.error(f"Error happened while using /api/songs endpoint: {e}")
        return make_response('Could not get the results. Please try later.', 430)


def _song_in_db(song_name:str,artist:str) -> bool:
    query=f"SELECT song_name from songs where song_name='{song_name}' and artist ='{artist}'"
    found = connect_execute_query(query)
    if not found:
        logging.info("Song is not in the database.")
        return False
    return True