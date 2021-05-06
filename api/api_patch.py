import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import request

from utilities.db_util import connect_execute_query
from utilities.token_utilities import token_required
from db_templates.load_template import load_db_template
import defaults


api_patch = Blueprint('api_patch', __name__)


@api_patch.route('/api/songs/name', methods=['PATCH'])
def change_song_name():
    return _handle_patch_request('song_name')


@api_patch.route('/api/songs/artist', methods=['PATCH'])
def change_artist():
    return _handle_patch_request('artist')


@api_patch.route('/api/songs/genre', methods=['PATCH'])
def change_genre():
    return _handle_patch_request('genre')


@api_patch.route('/api/songs/link', methods=['PATCH'])
def change_yt_link():
    return _handle_patch_request('yt_link')


@token_required
def _handle_patch_request(field: str):
    try:
        logging.info(f"User requested [{field}] change")

        if not _required_params():
            return make_response("Invalid parameter(s)", 406)

        update_value = request.args.get('update')
        song_name = request.args.get('song_name')
        artist = request.args.get('artist')

        template = load_db_template(defaults.update_songs_column)
        query = template.render(field=field, update_value=update_value, song_name=song_name, artist=artist)

        connect_execute_query(query)

        logging.info(f"[{field}] successfully changed to {update_value}.")

        return make_response(f"Successfully changed [{field}] field.", 200)
    except Exception as e:
        logging.error(f"Unexpected error happened: {e}")
        return make_response("Unprocessable entity", 430)


def _required_params() -> bool:
    valid_params = [ 'song_name', 'artist', 'update' ]
    return set(valid_params) == set([arg for arg in request.args])
