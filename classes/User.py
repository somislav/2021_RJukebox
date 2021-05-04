import logging
import defaults
import uuid
import jwt
import os

from utilities.hash_utilities import generate_hash
from db_templates.load_template import load_db_template
from utilities.db_util import connect_execute_query


class User:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    
    def validate_user(self) -> bool:
        query=f"SELECT user FROM users WHERE user=\'{self.name}\'"
        result=connect_execute_query(query)
        if result:
            logging.warning(f"User by the name {result[0][0]} already exists.")
            return False
        else:
            logging.info(f"User with name {self.name} is valid.")
            return True

    def input_user(self) -> bool:
        if self.validate_user():
            logging.info(f"Adding {self.name} user into db.")
            token = str(uuid.uuid4())

            template = load_db_template(defaults.user_insert)
            insert_query = template.render(user=self.name, password=generate_hash(self.password), token=token)

            connect_execute_query(insert_query)
            
            return True

        return False

    def get_encoded_token(self) -> str:
        try:
            query = f"SELECT token FROM users WHERE user='{self.name}'"
            result = connect_execute_query(query)

            if result:
                token = result[0][0]
                return str(jwt.encode({'token': token}, os.getenv('SECRET_KEY'), algorithm="HS256"))
            else:
                logging.warning(f"User [{self.name}] is missing from DB. Trying to add him.")
                user_added = self.input_user()

                if not user_added:
                    logging.critical(f"User [{self.name}] failed to be added to the DB.")
                    return None

                logging.info("User successfully added to the DB, acquiring token.")
                result = connect_execute_query(query)

                if not result:
                    return None

                return str(jwt.encode({'token': result[0][0]}, os.getenv('SECRET_KEY'), algorithm="HS256"))
        except Exception as e:
            logging.error(f"Error happened while acquiring token: {e}")
            return None