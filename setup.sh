#!/bin/bash
set -e

echo "=== Copying files into namenode ==="
docker cp mapper.py namenode:/tmp/
docker cp reducer.py namenode:/tmp/
docker cp stopwords.txt namenode:/tmp/
docker cp books/ namenode:/tmp/

echo "=== Waiting for safemode to clear ==="
docker exec namenode hdfs dfsadmin -safemode wait

echo "=== Putting books into HDFS ==="
docker exec namenode hdfs dfs -mkdir -p /books
docker exec namenode bash -c "hdfs dfs -put -f /tmp/books/*.txt /books/"

echo "=== Setup done ==="