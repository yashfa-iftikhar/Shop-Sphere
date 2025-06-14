# test_login_redirect_or_error.py
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
    driver.get("http://13.61.27.31:5100/login")
    print("Opened login page")

    # Enter invalid credentials
    driver.find_element(By.NAME, "email").send_keys("invalid@user.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

    time.sleep(3)

    current_url = driver.current_url
    if "login" in current_url or "error" in driver.page_source.lower():
        print("✅ Login attempt failed as expected and stayed on login page or showed error")
    else:
        print(f"❌ Unexpected redirection to: {current_url}")

finally:
    driver.quit()
