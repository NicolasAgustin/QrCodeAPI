#!/bin/bash

echo "COMMAND" ${COMMAND}

init_app() {
    echo "Start it"
    cd /app
    flask run -h 0.0.0.0 -p 5000
}

case "${COMMAND}" in
    init) init_app;;
    *) init_app;;
esac