#!/bin/bash

set -e

cd /var/www/baseApp
source venv/bin/activate
python3 dbinit.py
python3 db_create_mssg.py
