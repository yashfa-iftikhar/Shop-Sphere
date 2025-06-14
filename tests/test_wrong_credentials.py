# test_wrong_credentials.py
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

    # Enter dummy credentials
    driver.find_element(By.NAME, "email").send_keys("fake@user.com")
    driver.find_element(By.NAME, "password").send_keys("fakepassword")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)

    if "login" in driver.current_url:
        print("✅ Login failed as expected with wrong credentials")
    else:
        print("❌ Login success unexpectedly")

finally:
    driver.quit()
