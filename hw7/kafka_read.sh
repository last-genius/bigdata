#!/bin/bash

docker build -f Dockerfile.read -t hw7 .
docker run --network hw7-network -v /home/lastgenius/Documents/bigdata/hw7:/hw7 --rm hw7