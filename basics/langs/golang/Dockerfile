#ARGUMENTS
ARG ver=1.9.6

FROM golang:$ver-alpine3.7

ARG dir=code

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# install git
RUN apk update && apk upgrade && apk add --no-cache git

# COPY PROJECT FILES
RUN mkdir /$dir
WORKDIR /$dir
ADD . .

# docker run --rm -it -v "$(pwd)"/:/dir image_id -p 8808:8808
# VOLUME /$dir 

# upgrade 
# RUN go get -d -v ./...
# RUN go install -v ./...

# EXPOSE 10040

ENTRYPOINT ["/bin/ash"]
