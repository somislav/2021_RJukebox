import os

# PATHS TO CONFIGURATION FILES
logger_config = os.path.join(os.getenv('CONFIGURATIONS', ''), 'logger_config.ini')


# PATHS TO TEMPLATE FILES
song_table = 'song_table.template'
user_table = 'user_table.template'

song_insert = 'song_insert.template'
user_insert = 'user_insert.template'

add_column = 'add_column.template'
check_for_column = 'check_for_column.template'
