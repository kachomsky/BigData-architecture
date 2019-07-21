#!/bin/bash
docker network create hadoop
cd Hadoop/Base
docker build -t hadoop-base-tfg .
cd ../Namenode
docker build -t namenode-tfg .
cd ../Datanode
docker build -t datanode-tfg .
cd ../../Spark
docker build -t spark-tfg .