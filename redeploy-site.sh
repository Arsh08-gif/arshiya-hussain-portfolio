#!/bin/bash

echo "Step 1: Entering project folder..."

cd /root/arshiya-hussain-portfolio

echo "Step 1: Pulling latest changes..."

git fetch && git reset origin/main --hard

echo "Step 3: Running docker compose..."

docker compose -f docker-compose.prod.yml down

echo "Step 4: Building docker compose.."
 
docker compose -f docker-compose.prod.yml up -d --build
