#!/bin/bash

echo "rs.initiate()" | mongosh --port 27019
sleep 10
echo "rs.status()" | mongosh --port 27019
