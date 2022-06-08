#!/bin/bash

docker run --name cassandra-server --network hw8-network -p 9042:9042 -d cassandra:latest
sleep 100
docker cp /home/lastgenius/Documents/bigdata/hw8/create-tables.cql cassandra-server:/
docker exec -it cassandra-server cqlsh -f create-tables.cql
