import json
import names
import jwt
import uuid
import os
import random
import string
import logging
from utilities.hash_utilities import generate_hash


def create_users() -> list:
    try:
        logging.info("Creating test users.")
        data = []

        for i in range(10):
            data.append({
            'user':names.get_full_name(),
            'password':generate_hash(f'12{i}45'),
            'token': str(uuid.uuid4())
            })

        return data
    except Exception as e:
        logging.exception(f"Exception raised while creating users: {e}")
        return []


def create_songs() -> list:
    try:
        logging.info("Creating test songs.")

        data = []
        yt_base = "https://www.youtube.com/watch?v="
        letters = string.ascii_letters
        genres = [ 'Rock', 'HipHop', 'Metal', 'Pop', 'RnB' ]

        for i in range(10):
            yt_link = yt_base + ''.join(random.choice(letters) for i in range(10))
            artist = names.get_first_name()
            song_name = names.get_last_name()
            genre = random.choice(genres)

            data.append({ 'song_name': song_name, 'artist': artist, 'genre': genre, 'yt_link': yt_link })

        return data
    except Exception as e:
        logging.exception(f"Error happened while creating test songs: {e}")
        return []
