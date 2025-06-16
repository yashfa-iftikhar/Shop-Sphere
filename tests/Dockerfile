FROM python:3.11-slim

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 \
    libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 libxcomposite1 libxdamage1 \
    libxrandr2 xdg-utils libu2f-udev libvulkan1 libgbm1

# Install Google Chrome (stable version)
RUN wget -q -O google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome.deb \
    && rm google-chrome.deb

# Install compatible ChromeDriver (version matching Chrome 125)
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '[0-9.]+' | head -1 | cut -d'.' -f1-3) \
    && wget -q https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Set environment variable
ENV PATH="/usr/local/bin/chromedriver:$PATH"

# Set working directory
WORKDIR /tests

# Copy test files
COPY . /tests

# Install Python dependencies
RUN pip install --no-cache-dir selenium webdriver-manager pytest

# Default command: run all tests
CMD ["pytest"]
