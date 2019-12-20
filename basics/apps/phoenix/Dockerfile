# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT DATE: 20191021
# Dockerfile for angular project

# Arguments
ARG VERSION=1.9.2
ARG TAG=${VERSION}-alpine

FROM elixir:${TAG}

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# Project argurments
ARG DIR_NAME=code
ARG PROJECT_NAME=myapp

# Copy project files
RUN mkdir ${DIR_NAME}
ADD . ${DIR_NAME}

#MAKING CONTAINER 
# # docker build -t $(echo "${PWD##*/}"):dev --build-arg DIR_NAME=$(echo "${PWD##*/}") --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
#RUNNING CONTAINER
# # docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") $(echo "${PWD##*/}"):dev ash
