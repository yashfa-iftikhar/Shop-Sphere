# Use an official Python base image
FROM python:3.11-slim

# Install Chrome
RUN apt-get update && apt-get install -y wget gnupg2 curl unzip \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && mv chromedriver /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver

# Set environment variables
ENV PATH="/usr/bin/chromedriver:$PATH"

# Set working directory
WORKDIR /tests

# Copy test files
COPY . /tests

# Install Python dependencies
RUN pip install --no-cache-dir selenium webdriver-manager pytest

# Run all tests
CMD ["pytest"]
