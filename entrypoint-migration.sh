#!/usr/bin/env bash

# This is the docker entrypoint for the Hermes web app
# In dev mode just run the flask dev server
# In prod run gunicorn

PRODUCT="prototype"

# if [[ -f "$PROJECT_ROOT/app/scripts/setup.sh" ]]; then
#     $PROJECT_ROOT/app/scripts/setup.sh
#     if [[ $? != 0 ]]; then
#         echo "[ERROR] $PRODUCT setup.sh failed"
#         exit 1
#     fi
# fi
#
function apply_migrations() {
    echo "Running tools/post_deploy.sh..."
    #./tools/post_deploy.sh
}

apply_migrations
