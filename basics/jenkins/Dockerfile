# @AUTHOR: jon "imyme6yo@gmail.com"
# @DRAFT: 20190722
# @UPDATE: 20190723

# Arguments

ARG JENKINS_VERSION=2.60.3
# ARG ALPINE_VERSION=3.9

FROM jenkins:${JENKINS_VERSION}-alpine

# Labels
# Maintainer
LABEL maintainer="jon"
LABEL email="imyme6yo@gmail.com"

#
# docker build -t vue:$(echo "${PWD##*/}") --build-arg DIR_NAME=$(echo "${PWD##*/}") --build-arg PROJECT_NAME=$(echo "${PWD##*/}") .
#
# docker run --rm -it -v $(pwd)/:/$(echo "${PWD##*/}") vue:$(echo "${PWD##*/}") -p ${PORT}:${PORT} ash
# npm run serve -- --port ${PORT}