import mysql.connector
import logging

from db_templates.load_template import load_db_template
from utilities.db_util import check_if_table_exists

def create_table(cursor, table_name, template_name: str, primary_key: str, foreign_key: str = "") -> bool:
  try:
    if not check_if_table_exists(cursor, table_name):
      template = load_db_template(template_name)
      query = template.render(primary_key=primary_key, foreign_key=foreign_key)
      logging.info(f"Executing query: {query}")
      cursor.execute(query)

      logging.info(f"Table {table_name} created")
    else:
      logging.warning(f"Table {table_name} already exists.")
    return True
  except Exception as e:
    logging.error(f"Error happened while creating a table [{table_name}]: {e}")
    return False
