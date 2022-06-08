#!/bin/bash

docker build . -t app
docker run -p 5000:5000 --network hw4-network --rm app
