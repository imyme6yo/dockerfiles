# @AUTHOR: jon "imyme6yo@gmail.com"
# @CREATE: 20190115
# @UPDATE: 20191111

ARG PYTHON_VERSION=3.7.2
ARG ALPINE_VERSION=3.7

FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

LABEL maintainer "jon"
LABEL email "imyme6yo@gmail.com"

ARG DIR=code
ARG PACKAGES=requirements.txt

RUN apk update && apk update
RUN python -m pip install pip --upgrade

RUN mkdir ${DIR}
ADD . ${DIR}
WORKDIR ${DIR}

RUN pip install -r requirements
#RUN pip install -r $PACKAGES

#MAKING CONTAINER 
# # docker build -t $(echo "${PWD##*/}"):dev --build-arg DIRNAME=$(echo "${PWD##*/}") .
#RUNNING CONTAINER
# # docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") $(echo "${PWD##*/}"):dev ash