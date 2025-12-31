#!/bin/bash

echo "Cleaning up Docker resources..."

# Stop and remove containers
docker-compose down --remove-orphans

# Remove unused images
docker image prune -f

# Remove unused volumes (be careful with this in production)
# docker volume prune -f

# Remove unused networks
docker network prune -f

# Remove dangling images
docker rmi $(docker images -f "dangling=true" -q) 2>/dev/null || true

echo "Docker cleanup completed."