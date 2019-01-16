xhost +local:root
docker run --rm -it -v /run/user/1000:/run/user/1000 -v "$(pwd)"/flutter:/flutter -v /tmp/.X11-unix:/tmp/.X11-unix:ro --privileged --ipc=host --shm-size=1024m --net=host -e DISPLAY=$DISPLAY -e XDG_RUNTIME_DIR=/run/user/1000 imyme6yo/flutter:ubuntu-16.04


push image