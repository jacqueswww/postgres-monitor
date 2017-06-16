#
# Ubuntu Dockerfile
#
# Forked from: https://github.com/dockerfile/ubuntu
#

# Pull base image.
FROM ubuntu:16.04

# Install.
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python3-psycopg2 && \
  rm -rf /var/lib/apt/lists/*


# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# copy monitor script
COPY monitor.py /root/monitor.py
RUN chmod +x /root/monitor.py

# Define default command.
CMD ["/root/monitor.py"]

