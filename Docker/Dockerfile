# Use the official Playwright Python image from Microsoft Container Registry (MCR)
FROM mcr.microsoft.com/playwright/python:v1.53.0-noble-amd64

# Install pip and required packages in one RUN command
RUN pip install --upgrade pip && \
    pip install browser-use==0.5.2
# Create and set the working directory
WORKDIR /work
