#! /bin/bash
## This script is used to test the docker container once it is up and running

echo "Using newly created docker image to test the  build"


DOCKER_IMAGE_NAME=${1}
TAG=${2}
current_folder=${ROOT_FOLDER}/xprbuild/docker

if [[ -z "$DOCKER_IMAGE_NAME" ]]
then
        DOCKER_IMAGE_NAME=${PROJECT_NAME}
fi
if [[ -z "$TAG" ]]
then
        TAG=${PROJECT_VERSION}
fi

cmd="docker run ${DOCKER_IMAGE_NAME}:${TAG} /bin/bash xprbuild/system/linux/test.sh"
echo "Docker Test  command -> $cmd"
exec $cmd

