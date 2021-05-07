import logging

from flask import Blueprint
from flask import make_response
from flask import jsonify
from flask import request
from classes.User import User
from classes.Song import Song

from utilities.db_util import connect_execute_query
from utilities.token_utilities import token_required


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

@api_post.route('/api/add_song', methods=['POST'])
@token_required
def add_song():
    try:
        artist=request.args.get('artist')
        genre=request.args.get('genre')
        song_name=request.args.get('song_name')
        yt_link=request.args.get('yt_link')
        song = Song(artist, genre, song_name, yt_link)
        song.input_song()
        return song.song_name
    except Exception as e:
        logging.exception(f"Exception [{e}]: while adding song [{song.song_name}]")

    