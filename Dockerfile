# Use an official Python runtime as a parent image
FROM ubuntu:16.04

ENV USERNAME prosynt
ENV HOME=/home/$USERNAME

USER root

# Facilitate X11 Forwarding
RUN echo "$USERNAME:$USERNAME" | chpasswd && \
    usermod --shell /bin/bash $USERNAME && \
    usermod -aG sudo $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
# Replace 1000 with your user/group id
    usermod  --uid 1000 $USERNAME && \
    groupmod --gid 1000 $USERNAME && \
# Install needed packages
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install build-essential checkinstall && \
    apt-get -y install gcc g++ && \
    apt-get -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
USER $USERNAME

# Set the working directory
WORKDIR /workd

# Copy the current directory contents into the container at /prosynt
ADD . /workd

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "test1.py"]
