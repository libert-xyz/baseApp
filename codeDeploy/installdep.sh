#!/bin/bash
set -e

cd /var/www/baseApp
virtualenv --python python3 venv
source venv/bin/activate
pip install -r requirements.txt
