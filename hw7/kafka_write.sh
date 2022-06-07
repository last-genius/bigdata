#!/bin/bash

docker build -f Dockerfile.write -t hw7 .
docker run --network hw7-network --rm hw7
