#!/bin/bash

docker network create hw4-network
docker run --name cassandra-server --network hw4-network -p 9042:9042 -d cassandra:latest
sleep 90
docker cp /home/lastgenius/Documents/bigdata/hw4/create-tables.cql cassandra-server:/
docker exec -it cassandra-server cqlsh -f create-tables.cql