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
    # Go to your login page
    driver.get("http://16.171.162.11:5100/login")
    print("Opened login page")

    # Fill form (replace with actual test credentials)
    driver.find_element(By.NAME, "email").send_keys("your_test_email@example.com")
    driver.find_element(By.NAME, "password").send_keys("your_test_password")

    # Click login button
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    print("Clicked login")

    time.sleep(3)

    # Check for logout or dashboard presence
    try:
        driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
        print("✅ Login successful!")
    except NoSuchElementException:
        print("❌ Login failed: Logout not found.")

finally:
    driver.quit()
