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
ENV HOME /opt

# Define working directory.
WORKDIR /opt

# copy monitor script
COPY monitor.py /opt/monitor.py
RUN chmod +x /opt/monitor.py

# Define default command.
CMD ["/opt/monitor.py"]

