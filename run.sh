#!/bin/bash
set -e

echo "=== Cleaning old output ==="
docker exec namenode hdfs dfs -rm -r -f /output

echo "=== Submitting MapReduce job ==="
docker exec namenode hadoop jar \
  /opt/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
  -files /tmp/mapper.py,/tmp/reducer.py,/tmp/stopwords.txt \
  -input /books \
  -output /output \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py"

echo "=== Output ==="
docker exec namenode hdfs dfs -cat /output/part-00000