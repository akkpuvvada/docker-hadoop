#!/bin/bash
set -e
sudo service ssh start

# Check the HDFS working
if [ ! -d "/tmp/hadoop-hduser/dfs/name" ]; then
        $HADOOP_HOME/bin/hdfs namenode -format && echo "OK : HDFS namenode format operation finished successfully !"
fi

# Start DFS
$HADOOP_HOME/sbin/start-dfs.sh

# Start yarn which will help to allocate resources
echo "YARNSTART = $YARNSTART"
if [[ -z $YARNSTART || $YARNSTART -ne 0 ]]; then
        echo "running start-yarn.sh"
        $HADOOP_HOME/sbin/start-yarn.sh
fi

# Changing the file permissions
$HADOOP_HOME/bin/hdfs dfs -mkdir /tmp
$HADOOP_HOME/bin/hdfs dfs -mkdir /users
$HADOOP_HOME/bin/hdfs dfs -mkdir /jars
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /tmp
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /users
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /jars

$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave

# keep the container running indefinitely
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log
