#!/usr/bin/env bash

echo "Creating Virtual Environment..."
python3 -m venv venv
source venv/bin/activate

echo "Building Project Packages..."
python3 -m pip install -r requirements.txt

echo "Collecting Static Files..."
python3 manage.py collectstatic --noinput --clear