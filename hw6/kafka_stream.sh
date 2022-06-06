#!/bin/bash

docker build -t hw6 .
docker run --network hw6-network --rm hw6
