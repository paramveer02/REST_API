# Base image of our container
FROM python:3.10

# Environment Variable instructs docker to send output straight in terminal
# without buffering it first
ENV PYTHONUNBUFFERED 1

# Create root directory for our project in container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy current directory content into container at /app
ADD . /app/

# Install all specified packages in the requirements.txt
RUN pip install -r requirements.txt

