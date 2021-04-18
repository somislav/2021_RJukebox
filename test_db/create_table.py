import mysql.connector
import os
from dotenv import dotenv_values
from db_templates.load_template import load_db_template

def create_table(template_name: str,primary_key: str,foreign_key: str = ""):
  config = dotenv_values(".env")

  mydb = mysql.connector.connect(
    host="localhost",
    user=config['USER'],
    password=config['PASSWORD'],
    database="RJukebox"
  )

  mycursor = mydb.cursor()

  template = load_db_template(template_name)

  query=template.render(primary_key=primary_key,foreign_key=foreign_key)

  mycursor.execute(query)

  mycursor.close()
  mydb.close()

