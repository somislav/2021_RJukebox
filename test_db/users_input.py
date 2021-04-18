import jwt
import json
import mysql.connector
import os
from dotenv import dotenv_values
from create_users import create_users

def input_user():
  config = dotenv_values(".env")

  create_users()

  with open("users.json") as json_file:
      data = json.load(json_file)

  mydb = mysql.connector.connect(
    host="localhost",
    user=config['USER'],
    password=config['PASSWORD'],
    database="RJukebox"
  )

  mycursor = mydb.cursor()
  for d in data['users']:
      print(d)
      mycursor.execute("INSERT INTO users (user,password) VALUES (%s,%s)",(d['user'], d['password']))

  mydb.commit()
  mycursor.close()
  mydb.close()