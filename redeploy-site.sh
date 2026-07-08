#!/bin/bash

echo "Step 1: Entering project folder..."

cd /root/arshiya-hussain-portfolio

echo "Step 1: Pulling latest changes..."

git fetch && git reset origin/main --hard

echo "Step 3: Installing dependencies..."

source /root/arshiya-hussain-portfolio/python3-virtualenv/bin/activate

pip install -r requirements.txt

echo "Step 4: Restarting Flask Server..."
systemctl daemon-reload
systemctl restart myportfolio

echo "Deployment Complete!"
systemctl status myportfolio
