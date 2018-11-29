# ARGUMENT OF VERSION
# DATE: 20180921
# ARGUMENTS OF IMAGES

# LTS 8.12.0
# CURRENT 10.11.0

ARG VER=8.12.0
# ARG VER=10.11.0

FROM node:$VER-alpine

# ARGUMENTS OF CONTAINER
ARG DIR=code

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

#INSTALL IONIC
RUN npm install -g nativescript

# COPY PROJECT FILES
RUN mkdir /$DIR
WORKDIR /$DIR
ADD . /$DIR

RUN npm install

# docker run --rm -it -v "$(pwd)"/:/code 127f87f3b03b
VOLUME /$dir 

# requirements.txt
# RUN pip$VER install -r $REQUIREMENT

EXPOSE 9119

ENTRYPOINT ["/bin/ash"]
