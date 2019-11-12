# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 20180921
# @UPDATE: 20191009

# Arguments
ARG GO_VER=1.13.1
ARG ALPINE_VER=3.10

FROM golang:${GO_VER}-alpine${ALPINE_VER}

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# Arguments
ARG DIR=code

# install git
RUN apk update && apk upgrade && apk add --no-cache git

# COPY PROJECT FILES
RUN mkdir /${DIR}
WORKDIR /${DIR}
ADD . .

# docker run --rm -it -v "$(pwd)"/:/dir image_id -p 8808:8808
# VOLUME /$dir 

# upgrade 
# RUN go get -d -v ./...
# RUN go install -v ./...

# EXPOSE 10040

#
# docker build -t vue:$(echo "${PWD##*/}") --build-arg DIR_NAME=$(echo "${PWD##*/}") --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
#
# docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") vue:$(echo "${PWD##*/}") -p ${PORT}:${PORT} ash
# npm run serve -- --port ${PORT}