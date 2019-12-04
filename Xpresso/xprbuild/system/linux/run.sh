#! /bin/bash
## This script is used to run the project. It shuold contain the script which will run the project
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user


# Run the application
export ROOT_FOLDER=$PWD
export PYTHONPATH=${ROOT_FOLDER}
export PYTHONUNBUFFERED=1
export XPRESSO_CONFIG_PATH=config/common_stage.json
export XPRESSO_PACKAGE_PATH=${ROOT_FOLDER}

#TODO USE Gunicorn to run it
python3 ${ROOT_FOLDER}/xpresso/ai/server/controller/api_server/api_server.py
