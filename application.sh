#!/bin/bash -ex

# *** PROJECT PATHS ***
export CONFIGURATIONS=configurations
export DB_TEMPLATES=db_templates

# *** PROJECT VARIABLES ***
export DB_NAME=rjukebox

export TEST_RUN=true

# *** FLASK SETTINGS ***
export FLASK_APP=application.py
export FLASK_ENV=development

# *** PYTHONPATH ***
export PYTHONPATH=${PWD}:${PYTHONPATH}
echo $PYTHONPATH

flask run --no-reload
