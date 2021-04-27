
## db_util.py
- *connect_to_db(db: str="") : connects to desired database if there is one and returns it.*
- *execute_query(query : str,cursor): executes a desired query*
- *check_if_exists(cursor, db : str, query) -> bool : check if a table or a database exists(query="SHOW (TABLES/DATABASES)")*
## hash_utilities.py
- *generate_hash(password: str, algorithm: Algorithm = Algorithm.SHA256)->str : generates a hash string*