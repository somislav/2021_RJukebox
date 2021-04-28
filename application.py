from flask import Flask

import os

from dotenv import load_dotenv
import setup_environment

import defaults

import logging
from utilities.logger_utilities import setup_logger

from test_db.create_db import setup_db

load_dotenv('.env')
setup_logger(defaults.logger_config)

setup_db()
