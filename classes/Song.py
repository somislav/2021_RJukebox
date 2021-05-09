import logging
import defaults
import uuid
import jwt
import os


from db_templates.load_template import load_db_template
from utilities.db_util import connect_execute_query


class Song:
    def __init__(self, artist, genre, song_name, yt_link):
        self.artist = artist
        self.genre = genre
        self.song_name = song_name
        self.yt_link = yt_link
    
    def check_if_song_exists(self) -> bool:
        query=f"SELECT * FROM songs WHERE UPPER(artist)=\'{self.artist.upper()}\' AND UPPER(song_name)=\'{self.song_name.upper()}\'"
        result=connect_execute_query(query)
        if result:
            logging.warning(f"Song [{self.artist}:{self.song_name}] you wanted to add already exists.")
            return False 
        else:
            return True


    def input_song(self) -> bool:
        if self.check_if_song_exists():
            logging.info(f"Adding [{self.artist.upper()}:{self.song_name}] song into db.")

            template = load_db_template(defaults.song_insert)
            insert_query = template.render(song_name=self.song_name, artist=self.artist, genre=self.genre, yt_link=self.yt_link)

            connect_execute_query(insert_query)
            
            return True

        return False
    