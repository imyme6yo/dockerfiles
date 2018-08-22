# ARGUMENTS
ARG VER=3.7
ARG DIR=docs

FROM python:$VER-alpine3.7

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# upgrade pip
RUN python$VER -m pip install pip --upgrade 

# requirements.txt
# INSTALL SPHINX
RUN pip install sphinx sphinx-autobuild

# INSTALL SPHINX THEMES
# RUN pip install sphinx_rtd_theme

# ADD MAKE FOR PREVIEW
RUN apk add make 

# COPY PROJECT FILES
RUN mkdir /$DIR
WORKDIR /$DIR
VOLUME .
EXPOSE 9119

ENTRYPOINT ["/bin/ash"]
