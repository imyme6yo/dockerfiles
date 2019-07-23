# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 20180921
# @UPDATE: 20190723

# Arguments
ARG GO_VER=1.9.6
ARG ALPINE_VER=3.7

FROM golang:${GO_VER}-alpine${ALPINE_VER}}

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# Arguments
ARG DIR=code

# install git
RUN apk update && apk upgrade && apk add --no-cache git

# COPY PROJECT FILES
RUN mkdir /$dir
WORKDIR /$dir
ADD . .

# docker run --rm -it -v "$(pwd)"/:/dir image_id -p 8808:8808
# VOLUME /$dir 

# upgrade 
RUN go get -u github.com/labstack/echo/...
# RUN go get -d -v ./...
# RUN go install -v ./...

# EXPOSE 10040

ENTRYPOINT ["/bin/ash"]
