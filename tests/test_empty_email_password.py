# test_empty_fields.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://16.171.162.11:5100/login")
    print("Opened login page with empty form")

    # Click login without entering anything
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(2)

    if "login" in driver.current_url:
        print("✅ Empty field validation passed (still on login page)")
    else:
        print("❌ Unexpected behavior on empty login")

finally:
    driver.quit()
