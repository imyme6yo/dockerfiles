#ARGUMENT OF VERSION
#Date 20180912
ARG VER=8.12
FROM node:$VER-alpine

MAINTAINER jon "imyme6yo@gmail.com"

#ARGUMENTS OF CONTAINER
ARG dir=code

RUN apk update
RUN apk -y add bash curl

# RUN addgroup meteor

# RUN useradd meteor -g meteor -m -s /bin/bash

# USER meteor

# RUN curl https://install.meteor.com/ | sh 

#RUN cp "/home/meteor/.meteor/packages/meteor-tool/1.7.0_5/mt-os.linux.x86_64/scripts/admin/launch-meteor" /usr/bin/meteor

# RUN export PATH=$PATH:~/.meteor

# RUN mkdir /home/meteor/$dir
# WORKDIR /home/meteor/$dir

# RUN git clone https://github.com/meteor-vue/vue-meteor.git $dir

# ADD . .

# WORKDIR /home/meteor/$dir/$dir
# RUN ln -s ../$dir/packages packages
# RUN meteor npm install

