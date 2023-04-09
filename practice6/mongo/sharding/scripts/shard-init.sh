#!/bin/bash

echo "rs.initiate({_id: \"${RS_NAME}\", members: [{_id: 0, host: \"${HOST_NAME}:27018\"}]})" | mongosh --port 27018
sleep 10
echo "rs.status()" | mongosh --port 27018
