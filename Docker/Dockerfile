# Use the official Playwright Python image from Microsoft Container Registry (MCR)
FROM mcr.microsoft.com/playwright/python:v1.51.0-noble-amd64
# Install pip and required packages in one RUN command
RUN pip install --upgrade pip && \
    pip install pytest-html pytest-playwright && \
    pip install pytest-xdist && \
    apt-get update && \
    apt-get install -y wget && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb

# Create and set the working directory
RUN mkdir /work
WORKDIR /work
