# Docker file For Tomcat based java project
FROM python:3.7
LABEL PROJECT="xpresso.ai"

COPY . /opt/xpresso.ai
ENV ROOT_FOLDER=/opt/xpresso.ai
ENV PROJECT_NAME=xpresso.ai
ENV PYTHONPATH=$ROOT_FOLDER
ENV XPRESSO_PACKAGE_PATH=$ROOT_FOLDER
WORKDIR $ROOT_FOLDER

# Install dependencies
RUN /bin/bash $ROOT_FOLDER/xprbuild/system/linux/pre-build.sh

# Build the project
RUN /bin/bash $ROOT_FOLDER/xprbuild/system/linux/build.sh

# Clean the project
RUN /bin/bash $ROOT_FOLDER/xprbuild/system/linux/post-build.sh


# Deploy  the project
CMD ["/bin/bash", "xprbuild/system/linux/run.sh"]


