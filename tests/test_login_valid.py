from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from utils import create_driver

def test_successful_login():
    driver = create_driver()

    try:
        driver.get("http://13.61.27.31:5100/login")
        print("Opened login page")

        # Fill form (use actual test credentials that work)
        driver.find_element(By.NAME, "email").send_keys("your_test_email@example.com")
        driver.find_element(By.NAME, "password").send_keys("your_test_password")

        # Click login button
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        print("Clicked login")

        time.sleep(3)

        # Check for Logout link to confirm login success
        try:
            driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
            print("✅ Test Passed: Login successful!")
        except NoSuchElementException:
            print("❌ Test Failed: Login failed - Logout link not found.")

    finally:
        driver.quit()
