#!/usr/bin/env bash

PRODUCT="proto"

# Run monit daemon, which is in charge of ensuring proxysql is running
# Monit will start proxysql and if it ever dies it will restart it
# https://mmonit.com/monit/
# chmod 700 /home/app/prototype/config/monitrc
# monit -c /home/app/prototype/config/monitrc &

# We use the flask dev server for local development
echo "Installing python dependencies..."

exec pip install -r requirements.txt

echo "Starting flask dev server..."

exec flask run --host 0.0.0.0 --port 9000
