from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup headless Chrome options
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")
opts.add_argument("--no-sandbox")

# Auto-install correct ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)

try:
    # Go to the login page
    driver.get("http://13.61.27.31:5100/login")
    print("Opened login page")

    # Fill login form with invalid credentials
    driver.find_element(By.NAME, "email").send_keys("wronguser@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")

    # Click the login button
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    print("Clicked login with invalid credentials")

    time.sleep(3)

    # Check if login was incorrectly successful
    try:
        driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
        print("❌ Test Failed: Login succeeded with invalid credentials")
    except NoSuchElementException:
        print("✅ Test Passed: Login failed as expected with invalid credentials")

finally:
    driver.quit()
