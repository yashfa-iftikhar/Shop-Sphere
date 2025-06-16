# test_invalid_email_format.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://16.171.162.11:5100/login")
    print("Opened login page")

    # Fill in invalid email and any password
    driver.find_element(By.NAME, "email").send_keys("invalid-email")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")

    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)

    if "login" in driver.current_url:
        print("✅ Invalid email format test passed")
    else:
        print("❌ Unexpected result after submitting invalid email format")

finally:
    driver.quit()
