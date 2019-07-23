# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 190115
# @UPDATE: 190723
# @DESCRIPTION:
#       Dockerfile for flutter project

# Arguments
ARG VERSION=1.0
ARG TAG=${VERSION}-ubuntu18.04

FROM imyme6yo/flutter:${TAG}

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

ARG DIR_NAME=code
ARG PROJECT_NAME=project

RUN yes | flutter doctor --android-licenses || true

RUN mkdir ${DIR_NAME}
ADD . ${DIR_NAME}
WORKDIR ${DIR_NAME}

RUN npm install

#MAKING CONTAINER 
# # docker build -t $(echo "${PWD##*/}"):dev --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
#RUNNING CONTAINER
# # docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") $(echo "${PWD##*/}"):dev ash
