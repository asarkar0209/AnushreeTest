#!/bin/bash
## This script is used to create distribution for the xpresso client libraries
##
## DO NOT USE SUDO in the scripts. These scripts are run as sudo user
set -e

if [[ $EUID -ne 0 ]]
then
    echo "ERROR! Please login as root before executing this script. Use 'sudo su' to login as root."
    exit 1
fi

HOST_IP=172.16.1.175
SFTP_PORT=2222
SFTP_DIRECTORY="/data"
# This contains the list fo all files and folder required for client installations
current_version="$(cat VERSION)"
archive_name_latest="xpresso_client_pkg_latest.zip"
archive_name_version="xpresso_client_pkg_${current_version}.zip"
tmp_directory="dist"
package_name="xpresso.ai"
xpresso_temp_dir="${tmp_directory}/${package_name}"
client_files_folder=(VERSION setup.py requirements.txt Makefile ReadMe.md Release.md \
                    xpresso/ai/client xpresso/ai/core xpresso/__init__.py xprbuild samples config)

# copy files to destination folder maintaining the hierarchy
if [[ -z ${ROOT_FOLDER} ]]
then
  echo "Warning: Make sure to run this script from root folder of xpresso.ai"
  ROOT_FOLDER=$PWD
fi

copy_file(){
  src=$1
  dest=$2
  mkdir -p $dest
  relative_directory_path="$(dirname $src)"
  destination_directory="${dest}/${relative_directory_path}"
  mkdir -p $destination_directory
  cp -rf $src $destination_directory
}


echo "Cleaning up"
rm -rf ${xpresso_temp_dir}
mkdir -p ${xpresso_temp_dir}
echo "Creating a new copy of client files and folder"
for folder in "${client_files_folder[@]}";
do
  if [[ -z $folder ]]
  then
    echo "ERROR! ${folder} not found"
    echo "ERROR! Make sure to run the script from root folder of xpresso.ai"
    exit 1
  else
    copy_file $folder $xpresso_temp_dir
  fi
done

# Creating archive
apt-get install -y zip sshpass
cd ${xpresso_temp_dir}/..
zip -r ${archive_name_version} ${package_name}
cp ${archive_name_version} ${archive_name_latest}
sshpass -p 'abzooba@123' sftp -P ${SFTP_PORT} -o StrictHostKeyChecking=no xpresso@${HOST_IP}:${SFTP_DIRECTORY} <<< "put ${archive_name_version}"
sshpass -p 'abzooba@123' sftp -P ${SFTP_PORT} -o StrictHostKeyChecking=no xpresso@${HOST_IP}:${SFTP_DIRECTORY} <<< "put ${archive_name_latest}"

echo "Distribution creation succeeded ==> dist/"


