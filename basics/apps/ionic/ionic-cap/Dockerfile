# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT_DATE: 20190202
# @UPDATE_DATE: 20190202

# ARGUMENTS OF IMAGES
ARG ANDROID_STUDIO_VERSION=3.2.1
ARG NODE_VERSION=8.15.0
ARG TAG=${ANDROID_STUDIO_VERSION}-node${NODE_VERSION}-stretch
FROM imyme6yo/android-studio:${TAG}

# MAINTAINER
LABEL maintainer "imyme6yo@gmail.com"

# ARGUMENTS OF CONTAINER
ARG DIR_NAME=code
ARG PROJECT_NAME=code

#INSTALL IONIC
RUN npm install -g ionic
RUN npm install -g cordova

# COPY PROJECT FILES
RUN mkdir ${DIR_NAME}
ADD . ${DIR_NAME}

WORKDIR ${DIR_NAME}/${PROJECT_NAME}
RUN npm install

WORKDIR /${DIR_NAME}


# MAKING IMAGE 
# # docker build -t ionic:$(echo "${PWD##*/}") --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
# RUNNING CONTAINER
# # docker run -it -v $(pwd)/:/$(echo "${PWD##*/}") ionic:$(echo "${PWD##*/}") bash
# # docker run -it -v $(pwd)/:/$(echo "${PWD##*/}") ionic:$(echo "${PWD##*/}") -v /run/user/1000:/run/user/1000 -v /tmp/.X11-unix:/tmp/.X11-unix:ro --privileged --ipc=host --shm-size=1024m --net=host -e DISPLAY=$DISPLAY -e XDG_RUNTIME_DIR=/run/user/1000 bash
# DEPLOY APP ON THE DEVICE
# # ionic cordova prepare android
# # ionic cordova run android --device --ld
# EMULATE APP