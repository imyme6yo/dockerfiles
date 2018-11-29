FROM ubuntu:16.04

MAINTAINER jon "imyme6yo@gmail.com"

ARG dir=code

RUN apt-get update
RUN apt-get -y install curl git

RUN groupadd meteor

RUN useradd -m  -d /home/meteor meteor -g meteor

RUN chown meteor:meteor /home/meteor

USER meteor

RUN curl https://install.meteor.com/ | sh 

#RUN cp "/home/meteor/.meteor/packages/meteor-tool/1.7.0_5/mt-os.linux.x86_64/scripts/admin/launch-meteor" /usr/bin/meteor

ENV PATH "$PATH:/home/meteor/.meteor"
RUN echo $PATH

WORKDIR /home/meteor

RUN git clone https://github.com/meteor-vue/vue-meteor.git
RUN git clone https://github.com/meteor-vue/vue-meteor-demo.git $dir
WORKDIR /home/meteor/$dir

RUN ln -s ../vue-meteor/packages packages
RUN meteor npm install

