#!/bin/sh

export FLASK_APP=./generate_email/index.py

pipenv run flask --app ./generate_email/index --debug run -h 0.0.0.0