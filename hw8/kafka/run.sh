#!/bin/bash

docker build -f kafka/Dockerfile . -t kafka_write
docker run --network hw8-network --rm kafka_write