#!/bin/bash

docker build -f kafka-cassandra/Dockerfile . -t kafka_cassandra
docker run --network hw8-network --rm kafka_cassandra