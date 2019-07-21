FROM hadoop-base-tfg:latest

RUN mkdir -p /opt/hadoop/data/dataNode
EXPOSE 9864 9866
VOLUME /opt/hadoop/data
CMD [ "sh", "-c", "service ssh start; bash"]