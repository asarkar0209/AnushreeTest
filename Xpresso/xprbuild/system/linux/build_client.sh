#! /bin/bash
## This script is used to build the project.
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user

# Build the dependencies

set -e

if [[ $EUID -ne 0 ]]
then
    echo "ERROR! Please login as root before executing this script. Use 'sudo su' to login as root."
    exit 1
fi

ROOT_FOLDER=/opt
XPRESSO_BASE_FOLDER=xpresso.ai

install_dependencies(){
  apt-get -y update && apt-get -y upgrade
  apt-get -y install curl \
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
    libxss1
}

install_python(){
  printf "%s\n" "Installing Python dependencies... "
  add-apt-repository -y ppa:deadsnakes/ppa
  apt-get -y install python3.7 libpython3.7-dev
  wget https://bootstrap.pypa.io/get-pip.py
  python3.7 get-pip.py
  python_location=$(command -v python3.7)
  update-alternatives --install /usr/bin/python python "${python_location}" 2
  cp /usr/lib/python3/dist-packages/apt_pkg.cpython-36m-x86_64-linux-gnu.so /usr/lib/python3/dist-packages/apt_pkg.so | true
}

install_xpresso(){
  cd ${ROOT_FOLDER}/${XPRESSO_BASE_FOLDER}
  printf "%s\n" "Installing Xpresso Client... "
  
  #install xprctl
  rm -rf build/ dist/
  pip3 install --upgrade pip
  pip3 install --upgrade setuptools
  python setup.py bdist_wheel
  pip3 uninstall -y xprctl | true
  pip3 install --upgrade dist/xprctl-*.whl

  curl -sL https://deb.nodesource.com/setup_10.x | bash -
  apt-get -y install nodejs xvfb libgtk2.0-0 libgconf-2-4

  npm install -g electron@1.8.4 orca  --unsafe-perm=true --allow-root
  npm install -g orca@1.2.1  --unsafe-perm=true --allow-root

  cp config/xpresso-orca.service /etc/systemd/system/xpresso-orca.service
  systemctl daemon-reload
  systemctl enable xpresso-orca.service
  systemctl start xpresso-orca

  export PYTHONPATH=${ROOT_FOLDER}/${XPRESSO_BASE_FOLDER}:$PYTHONPATH
  echo "PYTHONPATH=${ROOT_FOLDER}/${XPRESSO_BASE_FOLDER}:${PYTHONPATH}" >> /etc/environment

  xprctl -h
  printf "\n%s\n" "All modules are working fine. Successfully installed xprctl."

}

install_alluxio(){
  cd ${ROOT_FOLDER}
  rm -rf ${ROOT_FOLDER}/alluxio-py
  git clone https://github.com/Alluxio/alluxio-py.git
  cd ${ROOT_FOLDER}/alluxio-py
  pip3 install -r requirements.txt
  pip3 install -e . --upgrade
  cd ${ROOT_FOLDER}
}

install_dependencies
install_python
install_alluxio
install_xpresso
