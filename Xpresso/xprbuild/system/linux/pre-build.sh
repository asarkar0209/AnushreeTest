#! /bin/bash
## This script is used to setup the build environment. It is used setup the build and test environment. It performs
## either of these tasks
##   1. Install Linux Libraries
##   2. Setup environment
##   3. Download data required to perform build.
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user

set -e

# Installing Python 3
if command -v python3 &> /dev/null; then
  echo "Python Found. Skipping Python installations"
else
  echo "Python not found. Installing python"
  add-apt-repository -y ppa:deadsnakes/ppa
  apt-get install python3.7
fi

# Installing pytest
pip3 install -U pytest pytest-cov
