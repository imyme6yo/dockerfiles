# rmi
docker ps -a | grep myapp:dev | awk '{print $1}'| xargs docker stop
# stop & rm
docker ps -a | grep myapp:dev | awk '{print $1}'| xargs docker rm
docker images | grep myapp:dev | awk '{print $3}'| xargs docker rmi
# build image
docker build -t myapp:dev .
# run container
docker run --rm -it -v $(pwd):/code -p 8119:3000  myapp:dev sh /code/startup.sh