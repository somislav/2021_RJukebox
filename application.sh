#!/bin/bash -ex

echo "*** Installing python dependencies ***"
pip3 install -r requirements.txt

# *** PROJECT PATHS ***
export CONFIGURATIONS=configurations
export DB_TEMPLATES=db_templates

# *** PROJECT VARIABLES ***
export DB_NAME=rjukebox
export HOST=localhost

export TEST_RUN=false

# *** FLASK SETTINGS ***
export FLASK_APP=application.py
export FLASK_ENV=development

# *** PYTHONPATH ***
export PYTHONPATH=${PWD}:${PYTHONPATH}
echo $PYTHONPATH
flask run --no-reload
