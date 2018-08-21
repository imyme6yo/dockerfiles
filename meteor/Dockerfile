FROM ubuntu:16.04

MAINTAINER jon "imyme6yo@gmail.com"

RUN useradd -ms /bin/bash meteor
RUN chown meteor /home/meteor

RUN apt-get update && apt-get -y install curl

USER meteor

RUN curl https://install.meteor.com/ | sh 

USER root 

COPY /home/meteor/.meteor/packages/meteor-tool/1.7.0_4/mt-os.linux.x86_64/scripts/admin/launch-meteor /usr/bin/meteor


USER meteor

EXPOSE 80



