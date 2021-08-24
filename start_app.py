#!/usr/bin/env bash

pyappver=`cat Pipfile | grep python_version | cut -d ' ' -f 3 | tr '\"' ' '`
pyenv local $pyappver
python -V
#export FLASK_ENV=development
export FLASK_ENV=production
export FLASK_APP=run.py
export FLASK_DEBUG=true
flask run  --host=0.0.0.0 --cert=adhoc
