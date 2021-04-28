import mysql.connector
import logging
from test_db.create_table import create_table
from test_db.users_input import input_user
from utilities.db_util import connect_to_db, execute_query,check_if_db_exists

def setup_db():
  mydb=connect_to_db()
  if not mydb:
    raise Exception(f"Connecting to db unsuccessful.")

  mycursor=mydb.cursor()
  if not check_if_db_exists(mycursor,"RJukebox"):
    query="CREATE DATABASE RJukebox"
    execute_query(query,mycursor)
    logging.info(f"Created RJukebox database.")
  else:
    logging.info(f"Database already exists.")

  mycursor.close()
  mydb.close()

  mydb=connect_to_db("RJukebox")
  mycursor=mydb.cursor()

  create_table(mycursor, 'users', 'user_table.template', 'id')
  create_table(mycursor, 'songs','song_table.template', 'id')
  input_user(mydb,mycursor)

  mycursor.close()
  mydb.close()