# ARGUMENT OF VERSION
# DATE: 20180921
# ARGUMENTS OF IMAGES

# LTS 8.12.0
# CURRENT 10.11.0

ARG VER=8.12.0
# ARG VER=10.11.0

FROM node:$VER-alpine

# ARGUMENTS OF CONTAINER
ARG DIR=likepub

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

#INSTALL IONIC
RUN npm install -g ionic

# COPY PROJECT FILES blank/tabs/sidemenu/blank/super/tutorial
RUN ionic start /${DIR} blank

#RUN npm install

# docker run --rm -it -v "$(pwd)"/:/likepub likepub:test
VOLUME /${DIR}

EXPOSE 9119

ENTRYPOINT ["/bin/ash"]
