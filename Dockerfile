# Import Python image from DockerHub
FROM python:3

# Setting PYTHONUNBUFFERED to a non-empty value to send outputs to terminal
ENV PYTHONUNBUFFERED=1

# Settings working directory
WORKDIR /app

# Copying the requirements file to Docker base image
COPY requirements.txt requirements.txt

# Running the installation of pip
RUN pip3 install --upgrade pip

# Installing all the dependencies
RUN pip3 install -r requirements.txt

# Copying all the folders to Docker base image
COPY . /app

# Exposing port for the webserver
EXPOSE 8000