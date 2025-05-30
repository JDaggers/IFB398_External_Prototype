#!/usr/bin/env bash

PRODUCT="proto"

echo "Installing python dependencies..."

pip install -r requirements.txt

echo "Starting flask dev server..."

exec flask run --host 0.0.0.0 --port 9000
