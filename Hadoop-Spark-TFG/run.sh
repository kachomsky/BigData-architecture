# Paramos y eliminamos los contenedores si ya existen
echo "**** Parando y eliminando conetenedores ****"
docker stop node1
docker stop node2
docker stop namenode
docker stop spark
docker stop client-spark
docker rm node1 --force
docker rm node2 --force
docker rm namenode --force
docker rm spark --force
docker rm client-spark --force

#docker ps -a | awk 'NR > 1 {print $1}' | xargs docker rm

#Iniciando datanodes
if [ "$1" == "" ] ;
then
        echo "**** Iniciando 1 datanode ****"
        #docker run -dti --net hadoop --net-alias node1  -h node1 --name node1 --link namenode --link spark datanode-tfg
        docker run -dti --net hadoop --net-alias node1 -h node1 -p 52479:8042 -p 52477:9864 --name node1 datanode-tfg
        docker run -dti --net hadoop --net-alias node2 -h node2 -p 52478:9864 -p 52480:8042 --name node2 datanode-tfg
        #-p 9864:9864
else
        counter=1
        for datanode in $(seq 1 $1);
        do
                echo "**** Iniciando datanode$counter ****"
                #commandSTR="docker run -dti --net hadoop --net-alias node$counter  -h node$counter --name node$counter --link namenode --link spark datanode-tfg"
                commandSTR="docker run -dti --net hadoop --net-alias node$counter -h node$counter -p 52477:9866 --name node$counter datanode-tfg"
                eval $commandSTR
                counter=$((counter+1))
        done
fi

# Iniciamos namenode y spark
echo "**** Iniciando Namenode ****"
docker run -d --net hadoop --net-alias namenode --name namenode -h namenode -p 52476:8032 -p 52475:9000 -p 52471:9870 -p 52472:8088 namenode-tfg

echo "**** Iniciando Spark ****"
docker run -dti --net hadoop --net-alias spark --name spark -h spark -p 52473:4044 spark-tfg

echo "**** Iniciando cliente ****"
docker run -d --net hadoop --net-alias client-spark --name client-spark -h client-spark -p 52474:22 spark-tfg
