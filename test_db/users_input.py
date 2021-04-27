import jwt
import json
import mysql.connector
import os
from dotenv import dotenv_values
from create_users import create_users
from utilities.db_util import check_if_table_exists

def input_user(mydb, cursor):
    if check_if_table_exists(cursor,"users"):
        create_users()

        with open("users.json") as json_file:
            data = json.load(json_file)

        for d in data['users']:
            cursor.execute("INSERT INTO users (user,password) VALUES (%s,%s)",(d['user'], d['password']))

        mydb.commit()
        print("Users added.")
        return True
    else:
        print("Added users.")
        return False