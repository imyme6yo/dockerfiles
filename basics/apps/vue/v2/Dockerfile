# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 20190722
# @UPDATE: 20200316

# ARGUMENTs
ARG NODE_VERSION=13.10.1
ARG ALPINE_VERSION=3.10

FROM node:${NODE_VERSION}-alpine${ALPINE_VERSION}

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

# ENVs
ENV HOST 0.0.0.0

# Arguments
ARG DIR_NAME=code
ARG PROJECT_NAME=myapp
ARG PORT=9212

# Install Alpine Packages
RUN apk update && apk upgrade

# Install vue-cli
RUN npm install -g @vue/cli


RUN mkdir ${DIR_NAME}
# Create Project by Default Settings
WORKDIR ${DIR_NAME}
COPY . .
RUN chmod +x startup.sh

ENTRYPOINT ["./startup.sh"]
#
# docker build -t vue:$(echo "${PWD##*/}") --build-arg DIR_NAME=$(echo "${PWD##*/}") --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
#
# docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") vue:$(echo "${PWD##*/}") -p ${PORT}:${PORT} ash
# npm run serve -- --port ${PORT}