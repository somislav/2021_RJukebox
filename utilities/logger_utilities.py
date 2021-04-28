import logging
import os
from datetime import datetime
import pathlib

from utilities.config_parser import parse_json_config

def setup_logger(config_path):
    config = parse_json_config(config_path)

    if not config:
        logging.basicConfig(level=logging.DEBUG)
        return

    formatting = config['format']
    file_name = _get_filename(config['base_file_name'])

    logFormatter = logging.Formatter(formatting)

    fileHandler = logging.FileHandler(file_name, encoding=config['encoding'])
    fileHandler.setFormatter(logFormatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)

    logging.basicConfig(
        level=logging.INFO,
        format=formatting,
        handlers=[
            fileHandler,
            consoleHandler
        ]
    )

    _clean_old_logs(config['keep_days'])


def _get_filename(base_name):
    today_date = datetime.today().strftime('%Y_%m_%d_%H_%M')

    return f"{base_name}_{today_date}.log"


def _clean_old_logs(days_old: int) -> None:
    print(f"Cleaning logs older than [{days_old}] days.")

    log_files = [entry.name for entry in os.scandir(os.getcwd()) if 'applicationLogs' in entry.name]

    for log_file in log_files:
        try:
            print(f"Found log file [{log_file}]")

            created_at = pathlib.Path(log_file).stat().st_ctime
            created_days_ago = (datetime.now() - datetime.fromtimestamp(created_at)).days
            print(f"Created [{created_days_ago}] days ago.")

            if created_days_ago < days_old:
                continue

            print(f"Deleting log file [{log_file}]")
            os.remove(log_file)
        except Exception as e:
            print(f"Error happened while deleting log file [{log_file}]: {e}")
