# ARGUMENT OF VERSION
# DATE: 20180912
ARG VER=3.7

FROM python:$VER-alpine3.7

# ARGUMENTS OF CONTAINER
# ARG VER=3.7
ARG DIR=code
ARG REQUIREMENT=requirements.text

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# INSTALL PACKAGES
RUN apk update && apk upgrade

# UPGRADE PIP
RUN python$VER -m pip install pip --upgrade 

# COPY PROJECT FILES
RUN mkdir /$DIR
WORKDIR /$DIR
ADD . /$DIR

# docker run --rm -it -v "$(pwd)"/:/code 127f87f3b03b
VOLUME /$dir 

# requirements.txt
# RUN pip$VER install -r $REQUIREMENT

EXPOSE 9119

ENTRYPOINT ["/bin/ash"]
