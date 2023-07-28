# docker build --build-arg http_proxy=http://10.158.100.1:8080 --build-arg https_proxy=http://10.158.100.1:8080 .

# Start from a base image
FROM python:3.11-slim

# Set environment variables for proxy
ARG http_proxy
ARG https_proxy
ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy
ENV no_proxy=localhost,127.0.0.1

# Set a directory for the app
WORKDIR /usr/src/app

# Create a group and user "app"
RUN groupadd -r app && useradd -r -m -g app -d /home/app app


# Change to the new created user
USER app

# Copy all the files to the container as the specified user
COPY --chown=app:app . .

# Install git as root
USER root
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK Data
RUN python -m nltk.downloader popular

# Switch back to the non-root user to run your application
USER app

