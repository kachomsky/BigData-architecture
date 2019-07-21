docker stop node1
docker stop node2
docker stop namenode
docker stop spark
docker rm node1 --force
docker rm node2 --force
docker rm namenode --force
docker rm spark --force
