import logging
import defaults

from utilities.hash_utilities import generate_hash
from db_templates.load_template import load_db_template
from utilities.db_util import connect_execute_query


class User:
    def __init__(self,name,password):
        self.name=name;
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
            template = load_db_template(defaults.user_insert)
            insert_query = template.render(user=self.name, password=generate_hash(self.password))
            result=connect_execute_query(insert_query)
            
            return True

        return False
