#!/bin/bash

docker network create cassandra-network
docker run --rm --name cassandra-node1 --network cassandra-network -d cassandra:latest
sleep 60
docker run --rm --name cassandra-node2 --network cassandra-network -d -e CASSANDRA_SEEDS=cassandra-node1 cassandra:latest
sleep 60
docker run --rm --name cassandra-node3 --network cassandra-network -d -e CASSANDRA_SEEDS=cassandra-node1,cassandra-node2 cassandra:latest
docker ps
