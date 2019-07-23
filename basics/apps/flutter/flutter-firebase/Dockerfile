# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 190115
ARG VERSION=1.0

FROM imyme6yo/flutter:${VERSION}-ubuntu18.04

LABEL maintainer "imyme6yo@gmail"

ARG DIR_NAME=code

# RUN flutter create ${DIRNAME}

RUN mkdir ${DIR_NAME}
ADD . ${DIR_NAME}
WORKDIR ${DIR_NAME}

WORKDIR ${DIR_NAME}

