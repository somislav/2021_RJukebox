
## db_util.py
- *connect_to_db(db: str="") : connects to desired database if there is one and returns it.*
- *execute_query(query : str,cursor): executes a desired query*
- *check_if_exists(cursor, db : str, query) -> bool : check if a table or a database exists(query="SHOW (TABLES/DATABASES)")*

## hash_utilities.py
- *generate_hash(password: str, algorithm: Algorithm = Algorithm.SHA256)->str : generates a hash string*

## logger_utilities.py
- *setup_logger() : method will setup logger, create a log file and delete old logs*
- *_get_filename() : method will return logger file name in format `applicationLogs_Year_Month_Day_Hour_Minute.log`*
- *_clean_old_logs(days_old: int) : method will delete all logs older than `days_old` days*

## config_parser.py
- *parse_json_config(config_path: str) -> dict : method will parse configuration file in json format and return a dictionary*