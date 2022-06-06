#!/bin/bash

docker kill cassandra-node1
docker kill cassandra-node2
docker kill cassandra-node3
docker network rm cassandra-network
