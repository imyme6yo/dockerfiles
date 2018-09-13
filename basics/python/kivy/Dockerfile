# Dockerfile for kivy with python3

# Future Plan: migration to alpine distribution 

# ARGUMENT OF VERSION
# DATE: 20180913
ARG VER=3.7

FROM python:$VER

# ARGUMENTS OF CONTAINER
ARG DIR=code
ARG REQUIREMENT=requirements.text

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# PACKAGE UPGRADE
RUN apt-get update && apt-get -y upgrade

# INSTALL VIM
RUN apt-get -y install vim

# upgrade pip
RUN python$VER -m pip install pip --upgrade 

# COPY PROJECT FILES
RUN mkdir /$DIR
WORKDIR /$DIR
ADD . .

# docker run --rm -it -v "$(pwd)"/:/code 127f87f3b03b
#VOLUME /$dir 

# requirements.txt
# RUN pip$VER install -r $REQUIREMENT

#EXPOSE 9119

ENTRYPOINT ["/bin/bash"]


# (host)$ xhost+local:docker
# (host)$ docker run --rm -it -v /run/user/1000:/run/user/1000 -v $"(pwd)"/:/code -v /tmp/.X11-unix:/tmp/.X11-unix:ro --privileged --ipc=host --shm-size=1024m --net=host -e DISPLAY=$DISPLAY -e XDG_RUNTIME_DIR=/run/user/1000 
