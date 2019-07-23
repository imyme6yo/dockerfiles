
# @AUTHOR: jon "imyme6yo@gmail"
# @DRAFT: 20180913
# @UPDATE: 20190723

# @DESCRIPTION:
#       Dockerfile for kivy with python3
#       Future Plan: migration to alpine distribution 

# Arguments 
ARG VER=3.7

FROM python:$VER

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# Arguments
ARG DIR=code
ARG REQUIREMENT=requirements.text

# PACKAGE UPGRADE
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y apt-utils

# INSTALL VIM
RUN apt-get install -y vim

# INSTALL DEPENDENCIES
RUN apt-get install -y git python-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev libmtdev-dev

# upgrade pip
RUN python$VER -m pip install pip --upgrade 

# INSTALL KIVY DEPENDENCIES
RUN pip install Cython

# INSTALL KIVY 
RUN pip install kivy

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


# (host)$ xhost +local:docker
# (host)$ docker run --rm -it -v /run/user/1000:/run/user/1000 -v "$(pwd)"/:/code -v /tmp/.X11-unix:/tmp/.X11-unix:ro --privileged --ipc=host --shm-size=1024m --net=host -e DISPLAY=$DISPLAY -e XDG_RUNTIME_DIR=/run/user/1000 
