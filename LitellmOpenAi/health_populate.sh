#!/bin/bash

while true; do
    HEALTH_STATUS=$(docker inspect --format='{{.State.Health.Status}}' open-webui)

    if [ "$HEALTH_STATUS" = "healthy" ]; then
        echo "Container is healthy. Running the populate script..."
        docker exec -it open-webui python3 populate_db.py
        break
    fi
    echo "Waiting for container to become healthy..."
    sleep 5
done
