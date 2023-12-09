#!/bin/sh

echo "Waiting for Kafka Connect to start listening on kafka-connect ⏳"

while [ `curl -s -o /dev/null -w %{http_code} http://kafka-connect:8083/connectors` -ge 200 -and `${http_code}`.eq.200 ] ; 
do 
    echo $(date) " Kafka Connect listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://kafka-connect:8083/connectors) " (waiting for 5)"
    sleep 5 
done
nc -vz kafka-connect 8083
echo "\n--\n+> Creating Kafka Connect Cassandra sink"

./create-cassandra-sink.sh 

sleep infinity
