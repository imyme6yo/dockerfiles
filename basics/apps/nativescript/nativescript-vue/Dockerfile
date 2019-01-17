# Dockerfile for nativescript-vue project
# AUTHOR: jon "imyme6yo@gmail.com"
# CREATE DATE: 20190117
# UPDATE DATE: 20190117
ARG VER=8.12.0
# ARG VER=10.11.0

FROM imyme6yo/nativescript:node10.6-stretch

# ARGUMENTS OF CONTAINER
ARG DIR_NAME=code
ARG PROJECT_NAME=project

# MAINTAINER
LABEL maintainer "imyme6yo@gmail.com"

#INSTALL NATIVESCRIPT
#RUN npm install -g --unsafe-perm nativescript
RUN npm install -g @vue/cli @vue/cli-init

# COPY PROJECT FILES
RUN mkdir ${DIR_NAME}
ADD . ${DIR_NAME}
WORKDIR ${DIR_NAME}/${PROJECT_NAME}
RUN npm install



