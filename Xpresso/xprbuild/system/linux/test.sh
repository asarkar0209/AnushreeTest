#! /bin/bash
## This script is used to test the project. After the build is completed test happens.
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user


# Test the dependencies

pylint xpresso
py.test --verbose --cov=xpresso --ignore-glob=test/xpresso_test/ai/admin/controller/*.yml
