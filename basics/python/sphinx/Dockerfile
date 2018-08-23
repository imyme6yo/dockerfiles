#ARGUMENTS
ARG VER=3.7

FROM python:$VER-alpine3.7

ARG DIR=docs
ARG REQUIREMENT=requirements.text

# MAINTAINER
MAINTAINER jon "imyme6yo@gmail.com"

# upgrade pip
RUN python -m pip install pip --upgrade 

# INSTALL SPHINX
RUN pip install sphinx sphinx-autobuild

# INSTALL SPHINX THEMES
# RUN pip install sphinx_rtd_theme

# ADD MAKE FOR PREVIEW
RUN apk add make 

# COPY PROJECT FILES
RUN mkdir /$DIR
WORKDIR /$DIR
ADD . .
VOLUME .

# requirements.txt
# RUN pip$VER install -r $REQUIREMENT

EXPOSE 9119

ENTRYPOINT ["/bin/ash"]
