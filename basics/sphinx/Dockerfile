#ARGUMENTS
ARG VER=3.7

FROM python:$VER-alpine3.7

ARG DIR=docs
ARG REQUIREMENT=requirements.text

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# install git
RUN apk update && apk upgrade && apk add --no-cache git
# ADD MAKE FOR PREVIEW
RUN apk add make 

# upgrade pip
RUN python -m pip install pip --upgrade 

# INSTALL SPHINX
RUN pip install sphinx sphinx-autobuild

# INSTALL SPHINX THEMES
# RUN pip install sphinx_rtd_theme


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
