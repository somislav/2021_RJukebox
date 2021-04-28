import os
import logging
import mysql.connector

def connect_to_db(db: str = ""):
  try:
    db_config = { 
      'host': 'localhost', 
      'user': os.getenv('USER'),
      'password': os.getenv('PASSWORD')
    } 
    if db: 
      db_config['database'] = db 
    mydb = mysql.connector.connect(**db_config)
    return mydb
  except Exception as e:
    logging.error(e)
    return None

def execute_query(query : str, cursor):
  try:
    result = cursor.execute(query)
    return result
  except Exception as e:
    logging.error(f"Failure while executing query [{query}]:{e}")
    return None

def check_if_exists(cursor, db : str, query) -> bool:
  try:
    cursor.execute(query) 
    return any([db == item[0] for item in cursor.fetchall()])
  except Exception as e:
    logging.error(f"Failure while executing query [{query}] : {e}")
    return None

def check_if_table_exists(cursor, table: str) -> bool:
  return check_if_exists(cursor, table, "SHOW TABLES")

def check_if_db_exists(cursor, db: str) -> bool:
  return check_if_exists(cursor, db, "SHOW DATABASES")
