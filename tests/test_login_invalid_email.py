from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from utils import create_driver

def test_invalid_login_credentials():
    driver = create_driver()

    try:
        driver.get("http://13.61.27.31:5100/login")
        print("Opened login page")

        # Fill login form with wrong credentials
        driver.find_element(By.NAME, "email").send_keys("wronguser@example.com")
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        print("Submitted form with invalid credentials")

        time.sleep(2)

        try:
            driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
            print("❌ Test Failed: Logged in with invalid credentials")
        except NoSuchElementException:
            print("✅ Test Passed: Login failed as expected with invalid credentials")

    finally:
        driver.quit()
