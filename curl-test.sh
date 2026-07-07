#!/bin/bash
curl -X POST http://localhost:5000/api/timeline_post -d 'name=arshiya&email=test@abc.com&content=First script post!'
curl http://localhost:5000/api/timeline_post 
