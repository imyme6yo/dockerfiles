# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT DATE: 20190218
# @UPDATE DATE: 20190916
# ARGUMENTS OF IMAGES

ARG NODE_VERSION=10.16.3
ARG ALPINE_VERSION=3.8
ARG TAG=${NODE_VERSION}-alpine
# ARG VERSION=10.11.0

FROM node:${TAG}

# MAINTAINER
LABEL maintainer "imyme6yo@gmail.com"

# ARGUMENTS OF CONTAINER
ARG DIR_NAME=code
ARG PROJECT_NAME=code

# Install Alpine Packages
RUN apk update && apk upgrade

# COPY PROJECT FILES
RUN mkdir ${DIR_NAME}
WORKDIR ${DIR_NAME}
ADD . ${DIR_NAME}
WORKDIR ${DIR_NAME}/${PROJECT_NAME}

RUN npm install

#MAKING CONTAINER 
# # docker build -t $(echo "${PWD##*/}"):dev --build-arg DIRNAME=$(echo "${PWD##*/}") .
#RUNNING CONTAINER
# # docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") $(echo "${PWD##*/}"):dev ash
