# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 20190722
# @UPDATE: 20190723

# ARGUMENTs

ARG NODE_VERSION=8.16.0
# ARG ALPINE_VERSION=3.9

FROM node:${NODE_VERSION}-alpine

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# ARGUMENTs
ARG DIR_NAME=code
ARG PROJECT_NAME=myapp
ARG PORT=9212

# Install Alpine Packages
RUN apk update

# Install vue-cli
RUN npm install -g @vue/cli

# Create Project by Default Settings
RUN vue create ${PROJECT_NAME} --default

RUN mkdir ${DIR_NAME}
WORKDIR ${DIR_NAME}/${PROJECT_NAME}

RUN vue add apollo
RUN vue add router
RUN vue add vuex

#
# docker build -t vue:$(echo "${PWD##*/}") --build-arg DIR_NAME=$(echo "${PWD##*/}") --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
#
# docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") vue:$(echo "${PWD##*/}") -p ${PORT}:${PORT} ash
# npm run serve -- --port ${PORT}