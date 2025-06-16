# tests/Dockerfile

FROM selenium/standalone-chrome:latest

# Create app directory
USER root
WORKDIR /tests
COPY . /tests

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip \
    && pip3 install --no-cache-dir selenium webdriver-manager pytest

USER seluser
CMD ["pytest", "--disable-warnings", "--maxfail=1"]
