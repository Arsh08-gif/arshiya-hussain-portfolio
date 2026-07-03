#!/bin/bash

echo "Step1: Killing the tmux sessions.."

tmux kill-server 2>/dev/null

echo "Step 2: Entering project folder..."

cd /root/arshiya-hussain-portfolio

echo "Step 3: Pulling latest changes..."

git fetch && git reset origin/main --hard

echo "Step 4: Installing dependencies..."

source /root/arshiya-hussain-portfolio/python3-virtualenv/bin/activate

pip install -r requirements.txt

echo "Step 5: Starting Flask server in tmux..."

tmux new-session -d -s flask -c /root/arshiya-hussain-portfolio 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
