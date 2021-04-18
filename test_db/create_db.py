import mysql.connector
import os
from dotenv import dotenv_values
from test_db.create_table import create_table
from test_db.users_input import input_user

config = dotenv_values(".env")

mydb = mysql.connector.connect(
  host="localhost",
  user=config['USER'],
  password=config['PASSWORD'],
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE RJukebox")

mycursor.close()
mydb.close()

create_table('user_table.template', 'id')
create_table('song_table.template', 'id')
input_user()