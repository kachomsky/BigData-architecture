FROM hadoop-base-tfg:latest

RUN mkdir -p /opt/hadoop/data/nameNode
EXPOSE 8020 9870 8088 9000 8032
VOLUME /opt/hadoop/data
CMD service ssh start
CMD bash start-hadoop.sh