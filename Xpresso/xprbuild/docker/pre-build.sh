#! /bin/bash
## This script is used to install the libraries required to build docker images
## Installing dependencies for docker

install_docker(){
  echo "-------- Installing Docker ----------"
  # Update local cache repo for docker and nvidia-dokcer
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

  distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
  curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  apt-key add -
  curl -s -L https://nvidia.github.io/nvidia-docker/$_distribution/nvidia-docker.list | \
  tee /etc/apt/sources.list.d/nvidia-docker.list
  apt-get -y update
  apt-cache policy docker-ce
  # Install docker and nvidia docker
  apt-get install -y docker-ce nvidia-docker2

  echo "Installing docker-compose"
  curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose

  echo "Installing docker-compose completed"
  echo "-------- Docker Installation Done --------"
}

install_docker
