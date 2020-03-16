# rmi
docker ps -a | grep clfun | awk '{print $1}'| xargs docker stop
# stop & rm
docker ps -a | grep clfun | awk '{print $1}'| xargs docker rm
docker images | grep clfun | awk '{print $3}'| xargs docker rmi
# build image
docker build -t clfun:dev .
# run container
docker run --rm -it -v $(pwd):/code -p 9212:3000  clfun:dev clfun:dev ash
# docker run --rm -it -v $(pwd):/code -p 9212:3000  clfun:dev ./startup.sh ash