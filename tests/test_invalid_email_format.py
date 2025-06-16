from selenium.webdriver.common.by import By
import time
from utils import create_driver

def test_invalid_email_format():
    driver = create_driver()

    try:
        driver.get("http://13.61.27.31:5100/login")
        print("Opened login page")

        # Enter invalid email format and dummy password
        driver.find_element(By.NAME, "email").send_keys("invalid-email")
        driver.find_element(By.NAME, "password").send_keys("wrongpass")

        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        print("Submitted form with invalid email format")

        time.sleep(2)

        if "login" in driver.current_url:
            print("✅ Test Passed: Invalid email rejected (still on login page)")
        else:
            print("❌ Test Failed: Redirected despite invalid email format")

    finally:
        driver.quit()
