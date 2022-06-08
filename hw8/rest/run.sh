#!/bin/bash

docker build -f rest/Dockerfile . -t app
docker run -p 5000:5000 --network hw8-network --rm app