import logging
import mysql.connector
from dotenv import dotenv_values

import defaults
from create_test_data import create_users, create_songs
from db_templates.load_template import load_db_template
from utilities.db_util import check_if_table_exists

def input_user(my_db, cursor) -> bool:
    if not check_if_table_exists(cursor, "users"):
        logging.error("Table [users] doesn't exist. Can't input users.")
        return False

    template = load_db_template(defaults.user_insert)
    users = create_users()

    for user in users:
        insert_query = template.render(user=user['user'], password=user['password'])
        cursor.execute(insert_query)

    my_db.commit()
    logging.info(f"Users successfully added.")

    return True


def input_songs(my_db, cursor) -> bool:
    if not check_if_table_exists(cursor, 'songs'):
        logging.warning("Table [songs] doesn't exist. Can't input songs.")
        return False
    
    template = load_db_template(defaults.song_insert)
    
    songs = create_songs()
    for song in songs:
        insert_query = template.render(song_name=song['song_name'], artist=song['artist'], genre=song['genre'], yt_link=song['yt_link'])
        cursor.execute(insert_query)
    
    my_db.commit()
    logging.info("Songs successfully added to DB.")

    return True
