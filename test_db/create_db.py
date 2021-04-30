import mysql.connector
import logging
import os
import defaults

from test_db.create_table import create_table
from test_db.users_input import input_user
from utilities.db_util import connect_to_db, execute_query, check_if_db_exists

def setup_db():
  mydb = None
  mycursor = None
  try:
    mydb = connect_to_db()
    if not mydb:
      logging.critical("Connection to DB unsuccessful.")
      return

    mycursor = mydb.cursor()
    db_name = os.getenv('DB_NAME')
    if not check_if_db_exists(mycursor, db_name):
      query = f"CREATE DATABASE {db_name}"
      execute_query(query, mycursor)
      logging.info(f"Created [{db_name}] database.")
    else:
      logging.info(f"Database [{db_name}] already exists.")
  finally:
    if mycursor:
      mycursor.close()
    if mydb:
      mydb.close()

  try:
    mydb = connect_to_db(db_name)
    mycursor = mydb.cursor()

    create_table(mycursor, 'users', defaults.user_table, 'id')
    create_table(mycursor, 'songs', defaults.song_table, 'id')

    if os.getenv('TEST_RUN'):
      input_user(mydb, mycursor)
  finally:
    if mycursor:
      mycursor.close()
    if mydb:
      mydb.close()
