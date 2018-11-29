FROM ubuntu:16.04

MAINTAINER jon "imyme6yo@gmail.com"

ARG appname

EXPOSE 8088

RUN apt-get update && apt-get -y install curl

RUN curl https://install.meteor.com/ | sh 

RUN meteor create $appname

WORKDIR /$appname

RUN meteor remove blaze-html-templates

RUN add angular-templates

RUN meteor npm install
