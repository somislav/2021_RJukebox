import json
import names
import logging
from utilities.hash_utilities import generate_hash


def create_users():
    try:
        data = {}
        data['users'] = []

        for i in range(10):
            data['users'].append({
            'user':names.get_full_name(),
            'password':generate_hash('12345')
            })

        with open("users.json", 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        logging.exception(f"Exception raised while creating users: {e}")
        raise e