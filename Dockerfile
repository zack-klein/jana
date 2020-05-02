FROM python:3.8-slim-buster

# Add a user, best practice to not run as root:
RUN adduser --gecos "" --disabled-password debian

# Common apt stuff
RUN apt-get update && \
  apt-get install -y nano curl wget gnupg git && \
  echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -y google-cloud-sdk

COPY requirements.txt /home/debian/requirements.txt

# Python packages
RUN pip install --upgrade pip && \
    pip install --upgrade -r /home/debian/requirements.txt

WORKDIR /home/debian/jana

# Customize more here!

USER debian
