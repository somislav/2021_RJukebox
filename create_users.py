import json
import names
from utilities.hash_utilities import generate_hash

#try cath needed
def create_users():
    data = {}
    data['users'] = []

    for i in range(50):
        data['users'].append({
            'user':names.get_full_name(),
            'password':generate_hash('12345')
        })

    with open("users.json", 'w') as outfile:
        json.dump(data, outfile)