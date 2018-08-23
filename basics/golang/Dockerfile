#ARGUMENTS
ARG ver=1.9.6

FROM golang:$ver-alpine3.7

ARG dir=code

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# COPY PROJECT FILES
RUN mkdir /$dir
WORKDIR /$dir
ADD . .
VOLUME /$dir 

# upgrade 
# RUN go get -d -v ./...
# RUN go install -v ./...

EXPOSE 10040

ENTRYPOINT ["/bin/ash"]
