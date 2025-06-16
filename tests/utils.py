# utils.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import shutil
import atexit
import os

# Track temporary dirs to clean up later
_temp_dirs = []

def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Unique temp directory for each test run
    temp_profile = tempfile.mkdtemp()
    _temp_dirs.append(temp_profile)  # Track for cleanup
    options.add_argument(f"--user-data-dir={temp_profile}")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# Cleanup function to delete all temp user profiles
def _cleanup_temp_dirs():
    for path in _temp_dirs:
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception as e:
            print(f"Could not clean temp dir {path}: {e}")

atexit.register(_cleanup_temp_dirs)
