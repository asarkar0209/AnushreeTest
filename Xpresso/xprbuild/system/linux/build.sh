#! /bin/bash
## This script is used to build the project.
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user

set -e

if [[ $EUID -ne 0 ]]
then
    echo "ERROR! Please login as root before executing this script. Use 'sudo su' to login as root."
    exit 1
fi

# Build the dependencies
install_dependencies(){
	apt-get -y update && apt-get -y upgrade
	apt-get -y install build-essential \
		curl \
		libcurl4-openssl-dev \
		libssl-dev \
		libffi-dev \
		git \
		wget \
		tmux \
		libfreetype6 \
		apt-transport-https \
		ca-certificates \
		software-properties-common \
		locales \
		pkg-config \
		nano \
		cmake \
		libxml2-dev \
		libxmlsec1-dev \
		checkinstall \
		libsasl2-dev \
		libldap2-dev \
		unzip \
		libgtkextra-dev \
		libgconf2-dev \
		libnss3 \
		libasound2 \
		libxtst-dev \
		libxss1 \
		libkrb5-dev \
		jq

	add-apt-repository -y ppa:ubuntu-toolchain-r/ppa | true
	apt-get -y install python3.7 libpython3.7-dev 
	wget https://bootstrap.pypa.io/get-pip.py
	python3.7 get-pip.py
	update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
	update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2

	# Updating _gi for python3.7
	cp -rf /usr/lib/python3/dist-packages/gi /usr/local/lib/python3.7/dist-packages/
	cp /usr/lib/python3/dist-packages/gi/_gi.cpython-*-x86_64-linux-gnu.so /usr/local/lib/python3.7/dist-packages/gi/_gi.cpython-37m-x86_64-linux-gnu.so
	cp /usr/lib/python3/dist-packages/apt_pkg.cpython-36m-x86_64-linux-gnu.so /usr/lib/python3/dist-packages/apt_pkg.so | true
}


install_xpresso(){
  pip install -r ${ROOT_FOLDER}/requirements_all.txt --upgrade
  #install xprctl
  pip3 install --upgrade pip
  pip3 install --upgrade setuptools
  python setup.py bdist_wheel
  pip3 uninstall -y xprctl | true
  pip3 install --upgrade dist/xprctl-*.whl
}

install_alluxio(){
	cd /opt
	rm -rf /opt/alluxio-py
	git clone https://github.com/Alluxio/alluxio-py.git
	cd /opt/alluxio-py
	pip install -e . --upgrade
	cd ${ROOT_FOLDER}
}

install_dependencies
install_alluxio
install_xpresso
