#!/bin/bash

set -e
service uwsgi start
service nginx restart 
