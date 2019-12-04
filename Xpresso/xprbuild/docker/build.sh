#! /bin/bash
## This script is used to build the docker image for the project
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user

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


cmd="docker build -t ${DOCKER_IMAGE_NAME}:${TAG} -f $current_folder/Dockerfile ${ROOT_FOLDER}"
echo "Building the docker image"
echo "Docker build command -> $cmd"
exec $cmd

