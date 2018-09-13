FROM ubuntu:16.04

MAINTAINER jon "imyme6yo@gmail.com"

ARG dir=code

RUN apt-get update
RUN apt-get -y install curl git

RUN addgroup meteor

RUN useradd meteor -g meteor -m -s /bin/bash

USER meteor

RUN curl https://install.meteor.com/ | sh 

#RUN cp "/home/meteor/.meteor/packages/meteor-tool/1.7.0_5/mt-os.linux.x86_64/scripts/admin/launch-meteor" /usr/bin/meteor

RUN export PATH=$PATH:~/.meteor

RUN mkdir /home/meteor/$dir
WORKDIR /home/meteor/$dir

RUN git clone https://github.com/meteor-vue/vue-meteor.git $dir

ADD . .

WORKDIR /home/meteor/$dir/$dir
RUN ln -s ../$dir/packages packages
RUN meteor npm install

