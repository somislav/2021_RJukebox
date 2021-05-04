import os
import logging
import defaults
import mysql.connector


from db_templates.load_template import load_db_template


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


def connect_execute_query(query: str) -> list:
  logging.info(f"Executing query: {query}")
  try:
    my_db = connect_to_db(os.getenv('DB_NAME'))
    cursor = my_db.cursor()
    
    result=execute_query(query, cursor)
    return result
  except Exception as e:
    logging.error(f"Couldn't execute query [{query}]: {e}")
    return []
  finally:
    logging.info("Closing DB after executing query.")

    if my_db:
      my_db.commit()
    if cursor:
      cursor.close()
    if my_db:
      my_db.close()


def execute_query(query : str, cursor):
  try:
    cursor.execute(query)
    return [result for result in cursor]
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

def add_table_column(cursor, table_name: str , column: str , data_type: str, default: str =""):
  try:
    if not check_if_column_exists(cursor, table_name, column):
      template=load_db_template(defaults.add_column)
      query=template.render(table_name=table_name, column=column, data_type=data_type, default=default)
      logging.info(f"Executing query: [{query}]")
      cursor.execute(query)
      logging.info(f"Added column [{column}] to table [{table_name}]")
  except Exception as e:
    logging.exception(f"Exception [{e}] was made while adding column [{column}] in [{table_name}].")

def check_if_column_exists(cursor, table_name: str , column: str) -> bool:
  try:
    template=load_db_template(defaults.check_for_column)
    query=template.render(table_name=table_name,column=column)
    logging.info(f"Checking if column [{column}] in table [{table_name}] exists.")
    cursor.execute(query)
    if [result[0] for result in cursor]:
      logging.warning(f"Column [{column}] already exist.")
      return True
    return False
  except Exception as e:
    logging.exception(f"Exception while checking if [{column}] exists.")
    return None


