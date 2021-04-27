import mysql.connector
from db_templates.load_template import load_db_template
from utilities.db_util import check_if_table_exists

def create_table(cursor, table_name, template_name: str,primary_key: str,foreign_key: str = ""):
  if not check_if_table_exists(cursor,table_name):
    template = load_db_template(template_name)
    query=template.render(primary_key=primary_key,foreign_key=foreign_key)
    cursor.execute(query)
    print(f"Table created")
    return True
  else:
    print("Table already exists.")
    return False