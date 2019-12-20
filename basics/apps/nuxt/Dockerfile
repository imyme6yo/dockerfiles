# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT DATE: 20190218
# @UPDATE DATE: 20191021

# Arguments
ARG NODE_VERSION=10.16.3
ARG ALPINE_VERSION=3.8
ARG TAG=${NODE_VERSION}-alpine
# ARG VERSION=10.11.0

FROM node:${TAG}

# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# ARGUMENTS OF CONTAINER
ARG DIR_NAME=code
ARG PROJECT_NAME=code

# Install Alpine Packages
RUN apk update && apk upgrade

# Copy project files
RUN mkdir ${DIR_NAME}
WORKDIR ${DIR_NAME}
ADD . ${DIR_NAME}
WORKDIR ${DIR_NAME}/${PROJECT_NAME}

RUN npm install

#MAKING CONTAINER 
# # docker build -t $(echo "${PWD##*/}"):dev --build-arg DIRNAME=$(echo "${PWD##*/}") .
#RUNNING CONTAINER
# # docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") $(echo "${PWD##*/}"):dev ash
