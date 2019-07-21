FROM hadoop-base-tfg:latest

# set environment vars
ENV HADOOP_HOME /opt/hadoop
ENV SPARK_HOME /opt/spark
ENV SPARK_VERSION 2.4.0
ENV PATH "$PATH:$SPARK_HOME/bin"
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV LD_LIBRARY_PATH $HADOOP_HOME/lib/native:$LD_LIBRARY_PATH

#download and extract Spark
RUN \
  wget https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop2.7.tgz && \
  tar -xvf spark-$SPARK_VERSION-bin-hadoop2.7.tgz && \
  mv spark-$SPARK_VERSION-bin-hadoop2.7 $SPARK_HOME && \
  echo "export SPARK_HOME=$SPARK_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export HADOOP_CONF_DIR=$HADOOP_CONF_DIR" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
  mv $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf

ENV PYSPARK_PYTHON /usr/bin/python3
ENV HDFS_CONF_DIR /opt/hadoop/etc/hadoop/
ENV YARN_CONF_DIR /opt/hadoop/etc/hadoop/

#creating SSH server
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:testtest' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

#copy spark config
ADD configs/spark-defaults.conf $SPARK_HOME/conf/

# expose various ports
EXPOSE 4044 22

CMD ["/usr/sbin/sshd", "-D"]

# start hadoop
# CMD bash start-hadoop.sh
