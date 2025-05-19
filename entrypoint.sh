#!/usr/bin/env bash

# This is the docker entrypoint for the Hermes web app
# In dev mode just run the flask dev server
# In prod run gunicorn

PRODUCT="prototype"

# Run monit daemon, which is in charge of ensuring proxysql is running
# Monit will start proxysql and if it ever dies it will restart it
# https://mmonit.com/monit/
# chmod 700 /home/app/prototype/config/monitrc
# monit -c /home/app/prototype/config/monitrc &

# We use the flask dev server for local development
echo "Starting flask dev server..."

exec flask run --host 0.0.0.0 --port 9000
