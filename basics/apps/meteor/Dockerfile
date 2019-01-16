FROM ubuntu:16.04

LABEL maintainer "imyme6yo@gmail.com"

ARG dir=code

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && apt-get upgrade -y
RUN apt-get -y install vim curl git

RUN groupadd meteor

RUN useradd -m  -d /home/meteor meteor -g meteor

USER meteor

RUN curl https://install.meteor.com/ | sh 

#RUN cp "/home/meteor/.meteor/packages/meteor-tool/1.7.0_5/mt-os.linux.x86_64/scripts/admin/launch-meteor" /usr/bin/meteor

ENV PATH "$PATH:/home/meteor/.meteor"
ENV PATH "$PATH:$HOME/.meteor"

RUN echo $PATH

RUN mkdir /home/meteor/$dir
WORKDIR /home/meteor/$dir

ADD . .

ENV DEVIAN_FRONTEND teletype

ENTRYPOINT ["/bin/bash"]
